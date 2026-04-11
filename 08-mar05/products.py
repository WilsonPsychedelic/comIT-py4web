# reading a csv
file_path = "output_data.csv"

# function that reads file content
def csv_reader(file_path):
    """reads a csv file and return a multiline string"""
    with open(file_path,"r") as csv:
        data = csv.read()        
    return data

#print(csv_reader(file_path))

# assigning the file content to a variable
data = csv_reader(file_path)
# creating a list of the lines in the file
lines = data.split("\n")
# print(lines[5:6])


# list to host the products as dictionaries
products = []

# converting lines from the csv into dictionaries
# produces many incorrect lines - multiple "," in the name
for line in lines:
    line_list = line.split(",")
    print()
    products.append({'id': line_list[0], 'name': line_list[1], 'price': line_list[2]})
    
print(products[51])

# header to display products
print("ID".center(5), "NAME","PRICE".rjust(10))

# printing list of data from individual dictionaries - carries error from spliting using ","
for product in products:
     print(product["id"], product["name"], product["price"])
    
