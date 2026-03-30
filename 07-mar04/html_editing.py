<<<<<<< HEAD
# Last time modified: 03/13/26
# Author: Wilson Psychedelic
=======
# Last time modified: 03/04/26
# Author: y44k0v
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8

html_base = ""

with open("garbage.html", "r") as website:
    html_base = website.read()
    

page_title = "MY Python Website"

<<<<<<< HEAD
html_modified = html_base.replace("<title>Document", f"<title>{page_title}</title>")

daisy_ui = """
<!-- Daisy UI -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>

<!-- Daisy UI themes -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />
=======
html_modified = html_base.replace("<title>Document", f"<title>{page_title}") 

# print(html_modified)

daisy_ui ="""

<!-- Daisy UI -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<!-- Daisy ui themes -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />

>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8
"""

html_modified = html_modified.replace("</head>", daisy_ui +"\n</head>" )

theme = "cyberpunk"
html_modified = html_modified.replace('<html lang="en">', f'<html lang="en" data-theme="{theme}">')

nav_bar = """
<div class="navbar bg-base-100 shadow-sm">
<<<<<<< HEAD
<div class="flex-1">
  <a class="btn btn-ghost text-xl">My Python Site</a>
</div>
<div class="flex-none">
    <ul class="menu menu-horizontal px-l">
      <li><a class="btn btn-ghost">Home</a></li>
      <li><a class="btn btn-ghost">About</a></li>
      <li><a class="btn btn-ghost">Contact</a></li>
    </ul>
  </div>
</div>
"""

card = """
<div class="flex justify-center mt-10">
  <div class="card bg-base-100 w-96 shadow-xl m-6">
    <div class="card-body">
      <h2 class="card-title">Hello!</h2>
      <p>This element was added using Python.</p>
      <div class="card-actions justify-end">
      <button class="btn btn-primary">Cool</button>
      </div>
    </div>
  </div>
</div>
"""
hero = """
<div class="hero bg-base-200 min-h-screen">
  <div class="hero-content text-center">
    <div class="max-w-md">
      <h1 class = "text-5xl font-bold">Welcome to My Python Website</h1>
      <p class="py-6">
      This page was generated using Python and styled with DaisyUI.
      </p>
      <button class ="btn btn-primary">Explore</button>
    </div>
  </div>
</div>
"""

footer = """
<footer class="footer footer-center bg-base-300 p-4">
  <aside>
    <p>Copyright © 2026 - My Python Website</p>
  </aside>
</footer>
"""

html_modified = html_modified.replace('</body>', nav_bar + hero + card + footer + "\n</body>")


with open("index.html", "w") as file:
    file.write(html_modified)
=======
  <a class="btn btn-ghost text-xl">daisyUI</a>
</div>
"""


html_modified = html_modified.replace('<body>', '<body>\n'+nav_bar)

with open("index.html", "w") as file:
    file.write(html_modified)
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8
