# FindMe
Find me is a content based search and retrieval project. You can query images from a database by uploading images that look like the images you are looking for. FindMe returns images most relevant to your search. In future, this will be used to query certain object the user is looking for from a video stream. However right now, FindMe can only retrieve car images from an example database.

## Download Repository
...

## Querying Car Image
...

## How it Works

For now, FindMe takes an image from the user and passes it to the YOLOv8 object detector. This object detector returns the name of the object detected and the bounding boxes of where in the image it was detected. FindMe crops the image so to only contain the detected image and passes this to an encoder. The encoder generates a embedding of 256 dimensions. This basically extracts the most important features of the image. From the encoder we get a "unqiue code" consisting of 256 numbers for each slightly different image the user inputs. 

If we want to upload an image to a database, the "unique code", name of object detected and other relevant information is added into the database. I used MongoDb for this project.

<p align="center">
![system_arch](https://github.com/lamiayous/FindMe/assets/124199862/5b8a20bb-d8af-45b2-8b49-00ef78f7bb51)
</p>

If we want to query an image, MongoDb takes the "unqiue code" and applies vector search using K-Nearest Neighbour algorithm and calulcating using dotproduct to check the similiarty of the query image with the other images in the database.

### Object Detector

FindMe uses the YOLOv8 object detector for the detecting part of the project. We trained the model using thousands of training images of cars.

<p align="center">
 <img width="265" alt="Screenshot 2023-09-13 at 21 10 14" src="https://github.com/lamiayous/FindMe/assets/124199862/ac4f5f9d-7099-4c82-bf0c-78802e3f731a">
</p>

This object detector returns many things, but FindMe only reqires three things, namely, the number of objects detected, the name of the object detected and the bounding box co-ordinate of where in the image the object was detected.

We crop this image to contain only the detected image.

<p align="center">
 <img width="386" alt="Screenshot 2023-09-13 at 21 11 57" src="https://github.com/lamiayous/FindMe/assets/124199862/4a68da7c-2338-410b-91dd-503e01fe9cb2">
<p align="center">

### Encoder
The encoder was first trained by adding a decoder, essentially making an autoencoder, to reconstruct the original image. Fundamentally, the encoder returns a 256 dimension feature space, the decoder takes those number and tries recontrsuct an image. 

Once trained, the encoder is used to generate the "unique codes"

The image below shows how the image is passed through the encoder.

<p align="center">
 <img width="972" alt="Screenshot 2023-09-14 at 23 45 07" src="https://github.com/lamiayous/FindMe/assets/124199862/221855f1-fc8a-41ad-aa92-c35005d60d65">
<p align="center">
                                            Encoder




### Database
The database used was MongoDB. With MongoDB, semantic search can be easily implemented and thus makes the query part of the project easy.

## In Practice
