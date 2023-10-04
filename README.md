# FindMe
Find me is a content-based search and retrieval project. FindMe can query images from a database by using example-based search. All that is needed to do, is give FindMe an example of an image and it returns images most relevant to the search. In future, this will be used to query certain object the user is looking for from a video stream. However, for now, FindMe can only retrieve car images from an example database.

## Download Repository
...

## How it Works

For now, FindMe takes an image from the user and passes it to the YOLOv8 object detector. This object detector returns the name of the object detected and the bounding boxes of where in the image it was detected. FindMe crops the image so that it only contain the detected image and passes this to an encoder. The encoder generates an embedding of 256 dimensions. This extracts the most important features of the image. From the encoder, we get a "unqiue code" consisting of 256 numbers for each different image the user inputs. 

For indexing an image to a database, the "unique code", name of object detected and other relevant information is added into the database (MongoDB was used).

<p align="center">
<img width="812" alt="system_arch" src="https://github.com/lamiayous/FindMe/assets/124199862/deb448f8-5526-4dcf-8183-a7756a2a52c4">
</p>

For querying an image, MongoDb takes the "unqiue code" and applies vector search using K-Nearest Neighbour algorithm and calculating using dotproduct to check the similiarty of the query image with the other images in the database.

### Object Detector

FindMe uses the YOLOv8 object detector for the detecting part of the project. We trained the model using thousands of training images of cars.

<p align="center">
 <img width="816" alt="obj_det" src="https://github.com/lamiayous/FindMe/assets/124199862/fdfc27d2-ed04-468a-b77a-b67fff71b098">
</p>

This object detector returns many things, but FindMe only reqires three things, namely, the number of objects detected, the name of the object detected and the bounding box co-ordinate of where in the image the object was detected.

We crop this image to contain only the detected image.

### Encoder
The Encoder used in this project also comes from another repository (https://github.com/lamiayous/autoencoder). However, FindMe uses the encoder from the autoencoder to extract a "unique code" and doesn't use the decoder .
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
```console
$ python findme.py --query car car.img
```
- findme.py: Running the project
- --query: Telling FindMe to query an image from a database
- car: Telling FindMe what kind of object looking for
- car.img: Showing FindMe an example of an image (This is the example search part of the Project)

For now, FindMe output the ObjectId for the top 3 images in the database that look like car.jpg
In the following example, there are about 15 images of cars in the database, None of which is a black dodge car.
When we give FindMe to look for similiar cars to a black dodge, it will return the following images.


<p align="center">
 <img width="300" alt="black" src="https://github.com/lamiayous/FindMe/assets/124199862/7f92bcea-6e56-49c3-a8a6-3eccce7641fa">
<p align="center">
                                   Query Image

<p align="center">
 <img width="300" alt="super_car" src="https://github.com/lamiayous/FindMe/assets/124199862/9d5177d3-dc51-47aa-b357-a5ba3c6f43fc">
<p align="center">
                                  Returned image (1/3)
<p align="center">
 <img width="300" alt="blk" src="https://github.com/lamiayous/FindMe/assets/124199862/9b179624-2647-4d09-af24-1b127a9591b8">
<p align="center">
                                 Returned image (2/3)
 
<p align="center">
 <img width="300" alt="yellow" src="https://github.com/lamiayous/FindMe/assets/124199862/39b90025-5d76-4cbd-9379-64758397d353">
<p align="center">
                                 Returned image (3/3)
 
