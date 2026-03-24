page_title = "My About Me Page"
page_lang = "ja"

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

# The reason the replace method has an option to add a third argument named "count"...
# It's because the same "My Page" or lang text might show up...
# Multiple times in a longer HTML document.
# Setting count to 1 ensures only the first occurance is replaced...
# Instead of changing other document parts by accident.

html = html.replace("My Page", page_title, 1)
html = html.replace('lang="en"', f'lang="{page_lang}"', 1)

print(html)
