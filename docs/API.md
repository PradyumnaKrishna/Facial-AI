# Continuous Integration and Continuous Delivery

> Author: Pradyumna Krishna<br>
> UPDATED: 28/03/2021

<br>

Today, I made an API which predicts emotion, this api can be used publicly or by anyone in any project. This API
returns response with no of faces, their coordiantes, emotions and probability of the guessed emotion. This API uses
my TensorFlow model which has 70% testing and 70% validation accuracy.

## How to use

The API url is `/FER/api/v1/` present at the latest website hosted on (possible that website is no longer hosted), send
a `POST` request using curl or postman, and uploading the file.

**CURL Request Example**

   ```bash
   curl -F image=@<path-to-file> http://<domain>/FER/api/v1/
   # a running example
   curl -F image=@face.jpg http://127.0.0.1:5000/FER/api/v1/
   ```

**Using Python `requests`**

   ```python
   import requests
   url = 'http://127.0.0.1:5000/FER/api/v1/
   files = {'image': open('face.jpg', 'rb')}
   requests.post(url, files=files)
   ```

It will give you response accordingly, Example `JSON` response is present below:

   ```json
   {
       "data": {
           "0": {
               "coordinates": {
                   "h": 284,
                   "w": 284,
                   "x": 397,
                   "y": 138
               },
               "emotion": "Neutral",
               "probability": {
                   "Angry": 0.05442037433385849,
                   "Disgust": 0.0001229508634423837,
                   "Fear": 0.023583699017763138,
                   "Happy": 0.0007338053546845913,
                   "Neutral": 0.7785017490386963,
                   "Sad": 0.14203275740146637,
                   "Surprise": 0.0006046505877748132
               }
           }
       },
       "message": "Yes! 1 face(s) detected!"
   }
   ```

* Point to Note: the image is resized to max-width of 1200px and max-height of 600px. Thats why,
the response coordinates are also changed.

**Back: [Setup](Setup.md)**<br>
**Next: [The Web Application](The-Web-Application.md)**