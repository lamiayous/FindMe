import pymongo
from datetime import datetime

#getting current day as this will be the name of our collection 

localcurrentdateandtime = datetime.now() # Get the local date and time
currentdatetime = localcurrentdateandtime.strftime("%m/%d/%Y") # Get the current date from the local date and time

# Connect to the MongoDB server (replace the connection string with your actual MongoDB URL)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Creating a database
db = client["FindMe"]
collection = db["entry"]

#Opening file with the unique code

# uniqueCode = open(r'E\Users\lamiayous\Projects\FindMe\autencoder\', 'r'')

# Create data objects
data_entry1 = {"vehicle": "Car", "encoded": "audi", "date and time": localcurrentdateandtime }

# Insert data into the collection
collection.insert_one(data_entry1)