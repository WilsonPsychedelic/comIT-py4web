freshco_data = [
    {
        "name": "Bananas",
        "price": "$1.99",
        "image_url": "https://via.placeholder.com/50"
    },
    {
        "name": "Apples",
        "price": "$3.49",
        "image_url": "https://via.placeholder.com/50"
    },
    {
        "name": "Milk",
        "price": "$4.29",
        "image_url": "https://via.placeholder.com/50"
    }
]

with open("template.html", "r", encoding="utf-8") as file:
    html_base = file.read()

table_rows = ""

for item in freshco_data:
    name = item["name"]
    price = item["price"]
    image_url = item["image_url"]

    row = f"""
    <tr>
        <td>{name}</td>
        <td>{price}</td>
        <td>
            <img src="{image_url}" width="50" height="50" alt="{name}">
        </td>
        <td class="flex gap-2">
            <button class="btn btn-square btn-error text-white">D</button>
            <button class-"btn btn-sqaure btn-success text-white">E</button>
        </td>
    </tr>
    """

    table_rows+= row

page_content = f"""
<div class="p-6">
    <h1 class="text-4xl font-bold mb-6 text-center">FreshCo Products</h1>

    <div class="overflow-x-auto">
        <table class="table table-zebra w-full">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Picture</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </div>
</div>
"""

html_final = html_base.replace("</body>", page_content + "\n</body>")

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_final)

print("index.html created successfully")
