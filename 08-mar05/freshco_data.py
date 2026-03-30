import requests
import json
# link obtained from freshco website flyer section using developer tools
url_freshco_mar_5_11_2026 = "https://dam.flippenterprise.net/flyerkit/publication/7813184/products?display_type=all&locale=en&access_token=881f0b9feea3693a704952a69b2a037a"

# Function to get the data as list of dictionaries - full information
def get_data(url):
  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()  # Automatically parses the JSON response
  except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    exit()
  except json.JSONDecodeError:
    print("Error decoding JSON")
    exit()
  return data

# calling the previous function to get the full data into a variable called data_freshco
data_freshco = get_data(url_freshco_mar_5_11_2026)
print(len(data_freshco)) # to know how many products we have
print(type(data_freshco)) # to check what king of data structure we have (list)
# print(data_freshco[0]) # to explore the one item in the list, user data_freshco[start_index:end_index_excluded] for a range of items 


# use of list comprehension create a list of dictionaries to select only 3 elements from every item -> name, price, pic, image_url
results_Freshco = [{'name': item['name'], 'price': item['price_text'], 'pic': item['image_url']} for item in data_freshco]
# print(results_Freshco[0]) # to explore a single element in results_freshco that is a list of dictionnaries

# the previous code for results_Freshco can be can be rewritten in the following way:

# list to store the dictionaries
results_Freshco_2 = [] 
# iterating over the list with the full product information to extra only name, price, and pic
for item in data_freshco:
  results_Freshco_2.append({'name': item['name'], 'price': item['price_text'], 'pic': item['image_url']})

# check if both methods produce the same result
print("Are results_Freshco and results_Freshco_2 the same?: ", results_Freshco == results_Freshco_2)

#finding the longest string in the names:

# initializing to max value
max_name_length = 0
for product in results_Freshco:
    # comparing the length of the name with the max variable
    if len(product['name']) > max_name_length:
        # when is larger than the original value (0) the variable is updated with the new value
        max_name_length = len(product['name'])
        # inspecting the maximum values found
        print(max_name_length)
        
# the previous loop produced 156 as maximum value        
print("NAME".center(max_name_length), "PRICE") 

# displaying all products on the terminal(long lines) - only name and price
for product in results_Freshco:
    print(product['name'].center(max_name_length), product['price'])
    

# filtering out items with no price by creating a list of dictionaries with prices
# this excludes the items with no price (price is as string)
filtered_products = [d for d in results_Freshco if d['price'] != ""]
print(len(filtered_products)) # total itmes 
print(filtered_products[35]) # selecting a single item

# the previous list can be obtained as:
filtered_products_2 = []
for d in results_Freshco:
  if d['price'] != "":
    filtered_products_2.append(d)
    
# verifying that both methods produce the same result    
print("Are filtered_products and filtered_products_2, equivalent?: ", filtered_products == filtered_products_2)


