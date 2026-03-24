page_title = "My About Me Page"
page_lang = "ja"

stylesheet = "main.min.css"
script_file = "bundle.js"

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
html = html.replace('lang="en"', f'lang="{page_lang}"', 1)

style_pos = html.find("styles.css")

html = html[:style_pos] + stylesheet + html[style_pos + len("styles.css"):]

script_pos = html.find("app.js")

html = html[:script_pos] + script_file + html[script_pos + len("app.js"):]

# Restricting search ranges is important in large HTML templates because
# Attributes like src and href can appear multiple times.
# You avoid accidentally modifying the wrong tag or replacing a filename
# Belonging to a different part of the page by limiting where the search occurs.

print(html)
