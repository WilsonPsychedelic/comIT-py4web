# using data analytics tools
import requests
import json
import pandas as pd

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

# use of list comprehension create a list of dictionaries to select only 3 elements from every item -> name, price, pic, image_url
results_Freshco = [{'name': item['name'], 'price': item['price_text'], 'pic': item['image_url']} for item in data_freshco]

##### data processing
# creating a dataframe
dataframe = pd.DataFrame(results_Freshco)
# displaying first lines
print(dataframe.head())

# generating a html table
html_table = dataframe.to_html()

# generating html file
with open("pandas_table.html", "w") as table:
  table.write(html_table)
  
# displawying the image in the table
# helper function to change url link
def format_as_img(url):
    return f'<img src="{url}" width="100">'

# modifying the dataframe
styled_df = dataframe.style.format({'pic': format_as_img})

# creating table
html_table_img = styled_df.to_html()

# writing new files with pics
with open("pandas_table_img.html", "w") as table:
  table.write(html_table_img)