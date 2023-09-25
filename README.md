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
<img width="812" alt="system_arch" src="https://github.com/lamiayous/FindMe/assets/124199862/deb448f8-5526-4dcf-8183-a7756a2a52c4">
</p>

If we want to query an image, MongoDb takes the "unqiue code" and applies vector search using K-Nearest Neighbour algorithm and calulcating using dotproduct to check the similiarty of the query image with the other images in the database.

### Object Detector

FindMe uses the YOLOv8 object detector for the detecting part of the project. We trained the model using thousands of training images of cars.

<p align="center">
 <img width="816" alt="obj_det" src="https://github.com/lamiayous/FindMe/assets/124199862/fdfc27d2-ed04-468a-b77a-b67fff71b098">
</p>

This object detector returns many things, but FindMe only reqires three things, namely, the number of objects detected, the name of the object detected and the bounding box co-ordinate of where in the image the object was detected.

We crop this image to contain only the detected image.

### Encoder
The Encoder used in this project also comes from another repository of mine (https://github.com/lamiayous/autoencoder). However, FindMe uses the encoder from the autoencoder to extract a "unique code".
The encoder was first trained by adding a decoder, essentially making an autoencoder, to reconstruct the original image. Fundamentally, the encoder returns a 256 dimension feature space, the decoder takes those number and tries recontrsuct an image. 

Once trained, the encoder is used to generate the "unique codes"

The image below shows how the image is passed through the encoder.

<p align="center">
<img width="671" alt="img_FindMe" src="https://github.com/lamiayous/FindMe/assets/124199862/ede24929-504e-4fe5-965a-f87b417aa606">
<p align="center">
                                            Encoder


### Database
The database used was MongoDB. With MongoDB, semantic search can be easily implemented and thus makes the query part of the project easy.

## In Practice

### Querying an Image:
$ python findme.py --query car car.img
