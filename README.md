# FindMe
Find me is a content based search and retrieval project. You can query images from a database by uploading images that look like the images you are looking for. FindMe returns images most relevant to your search. In future, this will be used to query certain object the user is looking for from a video stream. However right now, FindMe can only retrieve car images from an example database.

## Download Repository
...

## Querying Car Image
...

## How it Works
For now, FindMe takes an image from the user and passes it to the YOLOv8 object detector. This object detector returns the name of the object detected and the bounding boxes of where in the image it was detected. FindMe crops the image so to only contain the detected image and passes this to an encoder. The encoder generates a embedding of 256 dimensions. This basically extracts the most important features of the image. From the encoder we get a "unqiue code" consisting of 256 numbers for each slightly different image the user inputs. 

If we want to upload an image to a database, the "unique code", name of object detected and other relevant information is added into the database. I used MongoDb for this project.

If we want to query an image, MongoDb takes the "unqiue code" and applies vector search using K-Nearest Neighbour algorithm and calulcating using dotproduct to check the similiarty of the query image with the other images in the database.
<style type="text/css">
 body
  {
  background-color:black;
  }
#box 
  {
  width:300px;
  height:300px;
  background-color:white;
  border: 1px solid white;
  }
.circle 
  {
  border-radius:50%;
  width:100%;
  height:100%;
  }
</style>
<div id="box">
 <p align="center">
 <img width="376" alt="Screenshot 2023-09-13 at 17 02 01" src="https://github.com/lamiayous/FindMe/assets/124199862/06749e30-1b72-42da-96e4-31c68b3d752b">
 </p>
</div>

### Object Detector
...

### Encoder
...

### Database
...

## In Practice
