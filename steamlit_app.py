import streamlit
import pandas
import requests 
import snowflake.connector
from urllib.error import URLError

streamlit.header('Breakfast Menu')
streamlit.text('🧇 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🍗 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avacado')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Lets put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

#To debug issue
#streamlit.write("Printing fruits selected")
#streamlit.write(*fruits_selected)

fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the Page
streamlit.dataframe(fruits_selected)

#New Section to display FruityVice api response
streamlit.header('Fruityvice Fruit Advice')



#take input from user
fruit_choice = streamlit.text_input('What fruit do you like information about', 'kiwi')
streamlit.write('You have entered',fruit_choice)

#import requests 
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)

#take the json version of response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output it on the screen as a table
streamlit.dataframe(fruityvice_normalized)
streamlit.stop()



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")

my_data_row = my_cur.fetchone()

streamlit.header("The Fruit Load List contians")

streamlit.dataframe(my_data_row)

#take second input from user
fruit_to_add = streamlit.text_input('What fruit would you like to add?')
streamlit.write('thanks for adding',fruit_to_add)

my_cur.execute("insert into fruit_load_list values('from streamlit')")

