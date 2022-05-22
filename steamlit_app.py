import streamlit
import pandas

streamlit.header('Breakfast Menu')
streamlit.text('🧇 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🍗 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avacado')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

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
import requests 
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/watermelon')
streamlit.text(fruityvice_response)
