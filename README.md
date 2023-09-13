# FindMe
Find me is a content based search and retrieval project. You can query images from a database by uploading images that look like the images you are looking for. FindMe returns images most relevant to your search. In future, this will be used to query certain object the user is looking for from a video stream. However right now, FindMe can only retrieve car images from an example database.

## Download Repository
...

## Querying Car Image
...

## How it Works
For now, FindMe takes an image provided by the user and detects where a car can be found in the image using YOLOv8 object detector. This object detector return the bounding box for the detected image/images. It also returns the name of the detected image, which will be used later on. FindMe crops the image so as to only contain the detected image (car) and feeds this to an encoder. The encoder generates embeddings of a dimension of 256. This encoder basically extracts the important features of the image and when we pass an image through the encoder we get a "unique code" consisting of 256 normlaized numbers. 

FindMe uses the "uniique code" and name of detected image (in this case it can only be a car) and then uploads this information into a database. I used MongoDb for this. For a visual representation on how FindMe works, look at the below figure1.1

          <img width="380" alt="Screenshot 2023-09-13 at 16 52 44" src="https://github.com/lamiayous/FindMe/assets/124199862/33bd2753-81d6-4217-9b70-191bf65fe418">
                                                                            "figure1.1"


### Object Detector
...

### Encoder
...

### Database
...

## In Practice
