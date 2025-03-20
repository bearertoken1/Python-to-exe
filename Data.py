

import psutil
import ctypes
from ctypes import wintypes
import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu, Frame, Label, Button, Entry, Text, Scrollbar
import threading
import time
import os
import base64
import zlib

PREDEFINED_KEY = "oq56oRRx42r4EVyYDCJ0ifsARt4v0L4hlOpH"

dumping = False
selected_process = None
modified_memory = {}

def is_debugged():
    kernel32 = ctypes.windll.kernel32
    return kernel32.IsDebuggerPresent()

def is_eac_running():
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] == "EasyAntiCheat.exe":
                return True
        except psutil.NoSuchProcess:
            pass
    return False

def list_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            processes.append((proc.info['pid'], proc.info['name']))
        except psutil.NoSuchProcess:
            pass
    return processes

def dump_process_memory(pid):
    global dumping, modified_memory
    memory_dump = []

    with open("memory_dump.txt", "w") as dump_file:
        while dumping:
            try:
                process_handle = ctypes.windll.kernel32.OpenProcess(0x0010 | 0x0400, False, pid)
                if process_handle:
                    mem_basic_info = wintypes.MEMORY_BASIC_INFORMATION()
                    mem_size = ctypes.sizeof(mem_basic_info)
                    current_addr = 0

                    while True:
                        result = ctypes.windll.kernel32.VirtualQueryEx(process_handle, current_addr, ctypes.byref(mem_basic_info), mem_size)
                        if result == 0:
                            break
                        if mem_basic_info.State == 0x1000 and mem_basic_info.Protect in (0x40, 0x20):
                            buffer = ctypes.create_string_buffer(mem_basic_info.RegionSize)
                            bytes_read = ctypes.c_size_t(0)
                            if ctypes.windll.kernel32.ReadProcessMemory(process_handle, mem_basic_info.BaseAddress, buffer, mem_basic_info.RegionSize, ctypes.byref(bytes_read)):
                                memory_dump.append((hex(mem_basic_info.BaseAddress), buffer.raw.hex()))
                                modified_memory[hex(mem_basic_info.BaseAddress)] = buffer.raw.hex()
                        current_addr += mem_basic_info.RegionSize

                    ctypes.windll.kernel32.CloseHandle(process_handle)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

            dump_file.write("\n".join(f"Address: {addr}, Data: {data}" for addr, data in memory_dump) + "\n")
            memory_dump.clear()
            time.sleep(1)

def start_dumping():
    global dumping, selected_process
    if selected_process is None:
        messagebox.showerror("Error", "Please select a process to dump.")
        return

    dumping = True
    dump_thread = threading.Thread(target=dump_process_memory, args=(selected_process,))
    dump_thread.start()
    messagebox.showinfo("Info", "Started dumping memory to memory_dump.txt")

def stop_dumping():
    global dumping
    dumping = False
    messagebox.showinfo("Info", "Stopped dumping memory.")

def inject_memory():
    global selected_process, modified_memory
    if selected_process is None:
        messagebox.showerror("Error", "Please select a process to inject memory.")
        return

    try:
        process_handle = ctypes.windll.kernel32.OpenProcess(0x0020 | 0x0400, False, selected_process)
        if process_handle:
            for addr, data in modified_memory.items():
                buffer = ctypes.create_string_buffer(bytes.fromhex(data))
                bytes_written = ctypes.c_size_t(0)
                ctypes.windll.kernel32.WriteProcessMemory(process_handle, int(addr, 16), buffer, len(buffer), ctypes.byref(bytes_written))
            ctypes.windll.kernel32.CloseHandle(process_handle)
            messagebox.showinfo("Info", "Memory injected successfully.")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        messagebox.showerror("Error", "Failed to inject memory.")

def check_key():
    user_key = key_entry.get()
    if user_key == PREDEFINED_KEY:
        key_window.destroy()
        start_application()
    else:
        messagebox.showerror("Error", "Invalid key. Access denied.")
        root.quit()

def start_application():
    global selected_process, modified_memory

    root.title("NUKE's BUGGER")
    root.geometry("600x400")
    root.configure(bg="#2E2E2E")

    credits_label = Label(root, text="Credits: iNukedYou\nDiscord: inukedyou", bg="#2E2E2E", fg="white")
    credits_label.pack(pady=5)

    process_list = list_processes()
    process_names = [f"{pid}: {name}" for pid, name in process_list]
    selected_process_var = StringVar(root)
    selected_process_var.set("Select a process")

    process_menu = OptionMenu(root, selected_process_var, *process_names, command=lambda x: set_selected_process(x))
    process_menu.pack(pady=10)

    start_button = Button(root, text="Start Dumping", command=start_dumping)
    start_button.pack(pady=10)

    stop_button = Button(root, text="Stop Dumping", command=stop_dumping)
    stop_button.pack(pady=10)

    memory_text = Text(root, height=10, width=70, bg="#FFFFFF", fg="#000000")
    memory_text.pack(pady=10)

    inject_button = Button(root, text="Inject Memory", command=inject_memory)
    inject_button.pack(pady=10)

    def update_memory_text():
        memory_text.delete(1.0, tk.END)
        for addr, data in modified_memory.items():
            memory_text.insert(tk.END, f"Address: {addr}, Data: {data}\n")

    update_button = Button(root, text="Update Memory", command=update_memory_text)
    update_button.pack(pady=10)

    root.mainloop()

def set_selected_process(process_name):
    global selected_process
    selected_process = int(process_name.split(":")[0])

key_window = tk.Tk()
key_window.title("Enter Key")
key_window.geometry("300x150")
key_window.configure(bg="#2E2E2E")

key_label = Label(key_window, text="Enter the access key:", bg="#2E2E2E", fg="white")
key_label.pack(pady=10)

key_entry = Entry(key_window, show="*", width=30)
key_entry.pack(pady=5)

check_button = Button(key_window, text="Submit", command=check_key)
check_button.pack(pady=10)

if is_debugged() or is_eac_running():
    messagebox.showerror("Error", "Debugger or Easy Anti-Cheat detected. Exiting.")
    key_window.quit()

key_window.mainloop()
