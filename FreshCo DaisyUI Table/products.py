# reading a csv
file_path = "output_data.csv"
def csv_reader(file_path):
    """Reads a CSV file and return a multiline string"""
    with open(file_path, "r") as csv:
        data = csv.read()
    return data

#print(csv_reader(file_path))

# split lines
data=csv_reader(file_path)
lines=data.split("\n")
print(lines[5:6])

final_products = {}
keys = ["id", "name", "price"]
final_products = dict.fromkeys(keys, " ")
print(final_products)
products = []

for line in lines:
    line_list = line.split(",")
    products.append({'id': line_list[0], 'name': line_list[1], 'price': line_list[2]})

    print(products[51])

    print("ID".center(5), "NAME", "PRICE".rjust(10))
    
    for product in products:
        print(product['id'], product['name'], product['price'])
        
