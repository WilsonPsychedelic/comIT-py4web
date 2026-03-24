page_title = "My About Me Page"
page_lang = "ja"

stylesheet = "main.min.css"
script_file = "bundle.js"

h1 = "Welcome to My Page"
h2 = "About This Project"
h3 = "Technical Details"

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
</body>
</html>
"""

html = html.replace("My Page", page_title, 1)
html = html.replace('lang=en"', f'lang="{page_lang}"', 1)

style_pos = html.find("styles.css")
html = html[:style_pos] + stylesheet + html[style_pos + len("styles.css"):]

body_content = (
    f" <h1>{h1}</h1>\n"
    f" <h2>{h2}</h2>\n"
    f" <h3>{h3}</h3>\n"
)

parts = html.split("<body>")

# Using maxsplit=1 is safer because the <body> tag might be contained...
# Elsewhere in the page. Limiting Max Split ensures we don't accidentally...
# Break the document and we only divide the string at the real body tag.

html = parts[0] + "<body>\n" + body_content + parts[1]

print(html)
