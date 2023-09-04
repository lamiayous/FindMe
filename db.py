import pymongo
from datetime import datetime
import numpy as np
def tensor_to_list(img_code):
     # converting tensor into a list
    img_code = img_code.tolist()
    unique_code = []

    for index in range(len(img_code[0])):
        unique_code.append(img_code[0][index])

    unique_code = unique_code/np.linalg.norm(unique_code, axis=0)
    return unique_code

def semantic_search(unique_code, collection):
    results = collection.aggregate([
        {
            '$search': {
                "index": "SemanticSearch",
                "knnBeta": {
                    "vector": unique_code,
                    "k": 1,
                    "path": "encoded"}
            }
        }
    ])
    return results


def database_upload(object_name, img_code):

    #getting current day as this will be the name of our collection 
    localcurrentdateandtime = datetime.now() # Get the local date and time
    currentdatetime = localcurrentdateandtime.strftime("%m/%d/%Y") # Get the current date from the local date and time

    # Connect to the MongoDB server (replace the connection string with your actual MongoDB URL)
    client = pymongo.MongoClient("mongodb+srv://LamiaYous02:Lulu4283*@cluster0.7cbim5b.mongodb.net/?retryWrites=true&w=majority")

    # Creating a database
    db = client["FindMe"]
    collection = db[currentdatetime]
    
    unique_code = tensor_to_list(img_code)

    # Create data objects
    data_entry1 = {"vehicle": object_name, "encoded": [unique_code[0]], "date and time": localcurrentdateandtime }

    #adding the data object to the collection
    collection.insert_one(data_entry1)

    #then get the object id of the entry that has just been entered
    query = {"date and time": localcurrentdateandtime}
    document = collection.find_one(query)
    object_id = document["_id"]

    #adding the rest of the unique code into the "encoded" array
    for index in range(len(unique_code)):
        collection.update_one({"_id": object_id}, {"$push": {"encoded": unique_code[index+1]}}) #plus 1 because we already added the first value of the code

def database_query(img_code):
    localcurrentdateandtime = datetime.now() # Get the local date and time
    currentdatetime = localcurrentdateandtime.strftime("%m/%d/%Y") # Get the current date from the local date and time

    # Connect to the MongoDB server (replace the connection string with your actual MongoDB URL)
    client = pymongo.MongoClient("mongodb+srv://LamiaYous02:Lulu4283*@cluster0.7cbim5b.mongodb.net/?retryWrites=true&w=majority")

    # Creating a database
    db = client["FindMe"]
    collection = db[currentdatetime]
    
    unique_code = tensor_to_list(img_code)

    results = semantic_search(unique_code, collection)

    for document in results:
        print(f'Time: {document["date and time"]},\nID: {document["_id"]}\n')