from bs4 import BeautifulSoup
import os
import requests
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, CollectionInvalid
import datetime as dt
import unicodedata
import pandas as pd
import numpy as np

def find_class(soup, class_string):
    '''
    helper function for getting class information out of the soup for a page
    INPUT:
        - soup, soup object for a page
        - class_string, string of class label to grab
    OUTPUT: soup result set
    '''
    return soup.findAll(class_=class_string)

def find_parks_list(soup):
    return soup.findAll(id_="list_parks")

def get_mongo_collection(database_name, collection_name):
    # Save to mongodb the information from the web.
    # Store both the whole url and the div components

    db_client = MongoClient()
    database = db_client[database_name]
    collection = database[collection_name]
    return collection

'''

db.post.insert([
   {
      title: 'MongoDB Overview', 
      description: 'MongoDB is no sql database',
      by: 'tutorials point',
      url: 'http://www.tutorialspoint.com',
      tags: ['mongodb', 'database', 'NoSQL'],
      likes: 100
   }
'''

""" # Replace the ca with all the state codes
nps_state_parks_url = 'https://www.nps.gov/state/ca/index.htm'
soup = BeautifulSoup(requests.get(nps_state_parks_url).content, 'html.parser')

collection = getMongoConnection("nationalparks", "htmldata")
#Insert the raw html
collection.insert_one({"url" : "https://www.nps.gov/state/ca/index.htm", "raw_html" : soup.prettify() })

'''
# Each park items
<div class="col-md-9 col-sm-9 col-xs-12 table-cell list_left">
<h2></h2># This field has the type. Possible values: National Monument,National Park,National Historic Site, National Recreation Area
<h3><a href="/alca/" id="anch_9">Alcatraz Island</a></h3> #  This has the name of the national site
<h4>San Francisco, CA</h4> # This field has City followed by , and then state code
<p>
Alcatraz Island offers a close-up look at the site of the first lighthouse and US built fort on the West Coast, the infamous federal penitentiary long off-limits to the public, and the history making 18 month occupation by Indians of All Tribes. Rich in history, there is also a natural side to the Rock—gardens, tide pools, bird colonies, and bay views beyond compare.
</p> # this field has the description
</div>

'''

"""

def get_information(park, state_code):
    '''
    This will take the div tag of the park and return a key value pairs for the items I want to store.
      h2 tag had the type of the national site. Eg: National Monument,National Park,National Historic Site, National Recreation Area
     h3 tag had the name of the national site
     h4 tag had the city and state code separated by ,
      p tag had the description of the park.
    
     parkname:name of the park
     state:state where the park is located
     city:city of the park location
     type:type of park. Possible values:National Monument,National Park,National Historic Site, National Recreation Area
     description:text description of the park
    
    
    <div class="col-md-9 col-sm-9 col-xs-12 table-cell list_left">
    <h2>National Monument</h2>
    <h3><a href="/labe/">Lava Beds</a></h3>
    <h4>Tulelake, CA</h4>
    <p>
    Lava Beds National Monument is a land of turmoil, both geological and historical. Over the last half-million years, volcanic eruptions on the Medicine Lake shield volcano have created a rugged landscape dotted with diverse volcanic features. More than 700 caves, Native American rock art sites, historic battlefields and campsites, and a high desert wilderness experience await you!
    </p>
    </div>
    '''
    
    park_type = (park.find('h2')).contents
    
    if ((park.find('h2')).contents):
        park_type = (park.find('h2')).contents[0]
    else:
        park_type = ""
    park_name = ((park.find('h3')).find('a')).contents[0]

    # Park city was throwing an error because of the missing city so putting a check
    if((park.find('h4')).contents):
        park_city = ((park.find('h4')).contents[0]).split(",")[0]
    else:
        park_city = ""
    
    park_state = state_code
    park_description = (park.find('p')).contents[0]
    
    
    #create a dictionary so you can insert the values into mongo
    park_dict = {"park_name": park_name, "park_type":park_type, "park_city": park_city, "park_state": park_state, "park_desc": park_description}
    return park_dict
    

def pipeline_to_insert_data(state_codes_list):
    nps_parks_data_to_insert_list = []

    for i in range(0,len(state_codes_list)):
        url = 'https://www.nps.gov/state/%s/index.htm' % (state_codes_list[i].lower())
        soup = BeautifulSoup(requests.get(url).content, 'html.parser')
        # Construct entries to insert the raw html
        insert_html_row = {"state_cd":state_codes_list[i],\
                      "url":url,\
                      "raw_html":soup.prettify()}
        
        nps_parks_data_to_insert_list.append(insert_html_row)
        # Get the park list as a soup resultlist object from the soup object
        parks_list = find_class(soup, "col-md-9 col-sm-9 col-xs-12 table-cell list_left")
        for j in range(0,len(parks_list)):
            park_information_row = get_information(parks_list[j],state_codes_list[i])
            nps_parks_data_to_insert_list.append(park_information_row)

        
        
    return nps_parks_data_to_insert_list




# Read the state list
cwd = os.getcwd()
state_info = pd.read_csv("../data/state_province_codes.csv",skiprows=1)
state_list = state_info['State_Cd'].tolist()


#Construct the data 
data_to_insert = pipeline_to_insert_data(state_list)

#Get the Mongo Collection
collection = get_mongo_collection('nationalparks','htmldata')
collection.insert_many(data_to_insert)
    





