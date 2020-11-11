#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 13:40:54 2020

@author: asimmaredia

This program identifies handwritten text from image files using Google's Vision AI.
To successfully run this script on your device, you will need valid credentials.
To acquire credentials go to your google cloud console.

"""



import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

# Verifies your credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="--your json credentials--"

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('--your image file name--')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs label detection on the image file
response = client.text_detection(image=image)
texts = response.text_annotations

#print text recognized from the image provided.
print('Detected in text: ')
print('Labels:')
for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    
