import pymongo
from datetime import datetime

def database_upload(object_name, img_code):

    #getting current day as this will be the name of our collection 

    localcurrentdateandtime = datetime.now() # Get the local date and time
    currentdatetime = localcurrentdateandtime.strftime("%m/%d/%Y") # Get the current date from the local date and time

    # Connect to the MongoDB server (replace the connection string with your actual MongoDB URL)
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Creating a database
    db = client["FindMe"]
    collection = db[currentdatetime]
    img_code = img_code.tolist()

    unique_code = []
    index = 0

    while index < len(img_code[0]):
        unique_code.append(img_code[0][index])
        index += 1
    # # #Opening file with the unique code
    # unique_code = {}
    # # # fp = open("/Users/lamiayous/Projects/FindMe/autoencoder/code_img_0.txt", "r")

    # # #storing code into "unique_code" array
    # for code in img_code:
    #     unique_code.append(code)

    index=0

    # Create data objects
    data_entry1 = {"vehicle": object_name, "encoded": [unique_code[index]], "date and time": localcurrentdateandtime }

    #adding the data object to the collection
    collection.insert_one(data_entry1)

    #then get the object id of the entry that has just been entered
    query = {"date and time": localcurrentdateandtime}
    document = collection.find_one(query)

    object_id = document["_id"]
    print(object_id)

    #updating the index
    index = 1

    #adding the rest of the unique code into the "encoded" array

    while index < len(unique_code):
        collection.update_one({"_id": object_id}, {"$push": {"encoded": unique_code[index]}})
        index += 1