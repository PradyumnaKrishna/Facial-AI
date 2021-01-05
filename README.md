<img src="https://raw.githubusercontent.com/PradyumnaKrishna/PradyumnaKrishna/master/logo.svg" alt="Logo" title="Logo" align="right" height="50" width="50"/>

# Facial-AI [![Version][Version-Badge]][Version] [![License: MIT][License-Badge]](LICENSE.md)
<br>

<p align="center"><b>
THIS REPOSITORY IS LICENSED UNDER <a href="https://github.com/PradyumnaKrishna/Facial-AI/blob/main/LICENSE.md">MIT LICENSE</a></b></p>

<br>

This is a very simple Flask app that let's the user upload an image and detects how many (if any) faces are there and their respective emotions in the picture.

Haarcascade is used to detect the faces in the image, which is allowed to use my TensorFlow model to predict the emotion of human. I trained it in my repository [FER](https://github.com/PradyumnaKrishna/FER).

## Hosted on Google App Engine

Because Heroku Weak Servers, To run TensorFlow with Flask, I need to go for Google App Engine Flexible. It gave the ability to run it and its working fine* under 1 CPU and 1 GB Ram.

Give a try at <https://facial-ai.appspot.com>, use some [test](test) cases and rate our accuracy.

## Docs and References


- [Read these Docs](Docs/The%20Web%20Application.md) to understand this web application.
- [Read these Docs](Docs/Getting%20Started.md) to learn how to use this repository as a template.
- [Read these Docs](Docs/Getting%20Started.md) to deploy your own TensorFlow model on Platform as a Service(PaaS).

## Issues & Suggestions
 If any issues and suggestions to me, you can create an [issue](https://github.com/PradyumnaKrishna/FER/issues).

 ## Donate
> **Why Donate?** GCP or Google App Engine isn't free
 - Promote This Repo
 - [Donate](https://www.paypal.me/pradyumnakrishna)
 
<h2></h2>
<sup>*Image file smaller than 2 MB or medium resolution not more than 2000 Pixels. If unsupported file uploaded then error occurs.</sup>

[License-Badge]:        https://img.shields.io/badge/License-MIT-red.svg
[Version]:              https://github.com/PradyumnaKrishna/Facial-AI/tags/
[Version-Badge]:        https://img.shields.io/github/v/tag/PradyumnaKrishna/Facial-AI?label=Version