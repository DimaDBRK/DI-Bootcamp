# Week4 Day4
# Dmitry Dubrov
# Daily Challenge : Web API To DB

# Instructions
# Using this API, create the functionality which will write 10 random 
# countries to your database.

# These are the attributes which you should populate your tables with: 
# name, capital, flag, subregion, population.

import requests
import json
import pprint
import psycopg2
import random
# Instructions
# Using this API, create the functionality which will write 10 random countries to your database.
# These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.
# Connect to your PostgreSQL database

connection = psycopg2.connect(
    database="Public",
    user='postgres',
    password='Kachkanar',
    host='localhost', #or IP address
    port='5432'
)

table = 'countries'
cursor = connection.cursor()
# Table will be in database
# CREATE TABLE countries (
# 	id SERIAL PRIMARY KEY, 
# 	name VARCHAR(100) NOT NULL,
# 	capital VARCHAR(50) NOT NULL,
# 	flag_code VARCHAR(50) NOT NULL,
# 	subregion VARCHAR(50) NOT NULL,
# 	population INTEGER);
# Create a table to store country data if it doesn't exist
# query = f'''
# CREATE TABLE countries (
#     id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, capital VARCHAR(50) NOT NULL, flag_code VARCHAR(50) NOT NULL, subregion VARCHAR(50) NOT NULL, population INTEGER)"
# '''
# cursor.execute(query)
# connection.commit() #saving the changes in the database

# Get info countries from  API
countries_api = requests.get('https://restcountries.com/v3.1/all')
countries_api.raise_for_status() # Check for errors
data = countries_api.json()

# Iterate over the selected countries and insert data into the database
for i in range(10):
  choice = random.choice(data)
  name = choice['name']['official'].replace("'","")
  capital = choice['capital'][0].replace("'","")
  flag = choice['flags']['png']
  subregion = choice['subregion'].replace("'","")
  population = choice['population']
  
  query = f'''
INSERT INTO countries (name, capital, flag_code, subregion, population)
VALUES ('{name}', '{capital}', '{flag}', '{subregion}', '{population}');'''
  
  cursor.execute(query)
  connection.commit()
  
# Close  cursor - connection
cursor.close()
connection.close()

#Test

# Result in Table
# 1	"Argentine Republic"	"Buenos Aires"	"https://flagcdn.com/w320/ar.png"	"South America"	45376763
# 2	"Cook Islands"	"Avarua"	"https://flagcdn.com/w320/ck.png"	"Polynesia"	18100
# 3	"Slovak Republic"	"Bratislava"	"https://flagcdn.com/w320/sk.png"	"Central Europe"	5458827
# 4	"Republic of Trinidad and Tobago"	"Port of Spain"	"https://flagcdn.com/w320/tt.png"	"Caribbean"	1399491
# 5	"Saint Lucia"	"Castries"	"https://flagcdn.com/w320/lc.png"	"Caribbean"	183629
# 6	"Republic of Finland"	"Helsinki"	"https://flagcdn.com/w320/fi.png"	"Northern Europe"	5530719
# 7	"Swiss Confederation"	"Bern"	"https://flagcdn.com/w320/ch.png"	"Western Europe"	8654622
# 8	"State of Israel"	"Jerusalem"	"https://flagcdn.com/w320/il.png"	"Western Asia"	9216900
# 9	"Republic of Equatorial Guinea"	"Malabo"	"https://flagcdn.com/w320/gq.png"	"Middle Africa"	1402985
# 10	"Niue"	"Alofi"	"https://flagcdn.com/w320/nu.png"	"Polynesia"	1470

# pprint.pprint(data[0]['population'])
# print(type(data))
# name = data[0]['name']['common']
# capital = data[0]['capital'][0]
# flag = data[0]['flag']
# subregion = data[0]['subregion']
# population = data[0]['population']
# pprint.pprint(data[0]['name']['official'].replace("'",""))
