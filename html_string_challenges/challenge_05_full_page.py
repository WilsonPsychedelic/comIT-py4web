page_lang = "es"
page_title = "Full Page Challenge"

stylesheet = "app.min.css"
script_file = "main.bundle.js"

h1 = "Welcome to My Page"
h2 = "About This Project"
h3 = "Technical Details"

paragraph_text = "This project was built entirely using Python string methods."
img_src = "hero.jpg"
img_alt = "A hero image for the page"
second_paragraph_prefix = "This page is titled: "

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

html = html.replace('lang="en"', f'lang="{page_lang}"', 1)
html = html.replace("My Page", page_title, 1)

style_pos = html.find("styles.css")
html = html[:style_pos] + stylesheet + html[style_pos + len("styles.css"):]

script_pos = html.find("app.js")
html = html[:script_pos] + script_file + html[script_pos + len("app.js"):]

styles_count = html.count("styles.css")
appjs_count = html.count("app.js")

if styles_count == 0 and appjs_count == 0:
    print("Asset replacement check: both styles.css and app.js were successfully replaced.")
else:
    if styles_count > 0:
        print("Error: styles.css was not fully replaced.")
    if appjs_count > 0:
        print("Error: app.js was not fully replaced.")

body_content = (
    f"    <h1>{h1}</h1>\n"
    f"    <h2>{h2}</h2>\n"
    f"    <h3>{h3}</h3>\n"
)

parts = html.split("<body>", 1)
html = parts[0] + "<body>\n" + body_content + parts[1]

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
    + "    " + p_tag + "\n"
    + "    " + img_tag
    + html[insert_pos:]
)

title_start = html.find("<title>") + len("<title>")
title_end = html.find("</title>")
extracted_title = html[title_start:title_end]

second_p_tag = f"    <p>{second_paragraph_prefix}{extracted_title}</p>\n"

body_close_pos = html.find("</body>")
html = html[:body_close_pos] + second_p_tag + html[body_close_pos:]

print("Final Validation Report:")
print("✅ <title>Full Page Challenge</title> is present"
      if html.count("<title>Full Page Challenge</title>") == 1
      else "❌ <title>Full Page Challenge</title> is present")

print("✅ <h1> appears"
      if html.count("<h1>") == 1
      else "❌ <h1> appears")

print("✅ <h2> appears"
      if html.count("<h2>") == 1
      else "❌ <h2> appears")

print("✅ <h3> appears"
      if html.count("<h3>") == 1
      else "❌ <h3> appears")

print("✅ <img appears exactly once"
      if html.count("<img") == 1
      else "❌ <img appears exactly once")

print("✅ <p> appears exactly twice"
      if html.count("<p>") == 2
      else "❌ <p> appears exactly twice")

print("✅ String starts with <!DOCTYPE html>"
      if html.startswith("<!DOCTYPE html>")
      else "❌ String starts with <!DOCTYPE html>")

print("✅ String ends with </html>"
      if html.strip().endswith("</html>")
      else "❌ String ends with </html>")

print("\nFinal HTML:\n")
print(html)

print("\nTag Content Extraction Test:")

tags_to_test = ["title", "h1", "h2", "h3"]

for tag in tags_to_test:

    open_tag = "<" + tag + ">"
    close_tag = "</" + tag + ">"

    start = html.find(open_tag)
    end = html.find(close_tag)

    if start != -1 and end != -1:
        start = start + len(open_tag)
        content = html[start:end]
        print(f"{tag} content:", content)
    else:
        print(f"{tag} content: not found")
