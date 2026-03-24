page_title = "My About Me Page"
page_lang = "ja"

stylesheet = "main.min.css"
script_file = "bundle.js"

h1 = "Welcome to My Page"
h2 = "About This Project"
h3 = "Technical Details"

paragraph_text = "This project was built entirely using Python string methods."
img_src = "hero.jpg"
img_alt = "A hero image for the page"

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
html = html.replace('lang="en"', f'lang="{page_lang}', 1)

style_pos = html.find("styles.css")
html = html[:style_pos] + stylesheet + html[style_pos + len("styles.css"):]

script_pos = html.find("apps.js")
html = html[:script_pos] + script_file + html[script_pos + len("app.js"):]

body_content = (
    f" <h1>{h1}</h1>\n"
    f" <h2>{h2}</h2>\n"
    f" <h3>{h3}</h3>\n"
)

parts = html.split("<body>", 1)

p_tag = f"<p>{paragraph_text}</p>"
img_tag = '<img src="' + img_src + '" alt="' + img_alt + '" />'

closing_tags = ["</h1>", "</h2>", "</h3>"]

last_heading_pos = -1
last_heading_tag = ""

for tag in closing_tags:
    pos = html.rfind(tag)

    if pos != -1 and pos > last_heading_pos:
        last_heading_pos = pos
        last_heading_tag = tag
insert_pos = last_heading_pos + len(last_heading_tag)

html = (
    html[:insert_pos]
    + "\n"
    + " " + p_tag + "\n"
    + " " + img_tag
    + html[insert_pos:]
)

print(html)
