<img src="https://raw.githubusercontent.com/PradyumnaKrishna/PradyumnaKrishna/master/logo.svg" alt="Logo" title="Logo" align="right" height="50" width="50"/>

# Facial-AI [![Version][Version-Badge]][Version] [![Build Status][Build-Badge]][Travis-CI] [![Coverage][Codecov-Badge]][Codecov] [![License: MIT][License-Badge]](LICENSE.md)

<br>

<p align="center"><b>THIS REPOSITORY IS LICENSED UNDER <a href="https://github.com/PradyumnaKrishna/Facial-AI/blob/main/LICENSE.md">MIT LICENSE</a></b></p>

<br>

This is a very simple Flask app that let the user upload an image and detects how many (if any) faces are there and
their respective emotions in the picture.

Haarcascade is used to detect the faces in the image, which is allowed to use my TensorFlow model to predict the emotion
of human. I trained it in my repository [FER](https://github.com/PradyumnaKrishna/FER).

## Get Started

Use Docker or Virtual Environment to run this web application.
To get started:

1. Clone the repository
   ```bash
   git clone https://github.com/PradyumnaKrishna/Facial-AI
   ```
3. Install Dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
4. Run the flask server
   ```bash
   python3 main.py
   ```

Read more information or instructions about the setup at [docs](docs/Setup.md).

## Hosted on Azure App Service

Google App Engine Flexible isn't free that's why I moved to Azure App Service. Again it gave the ability to run it and
work fine* under their free tier.

Give a try at <http://facial-ai.azurewebsites.net>, use some [test](test) cases and rate our accuracy.

*I used Docker Image to for deployment last time, I was using git but due to some problem I switched over it.

## CI/CD using Travis-CI

Recently, I learned about Travis-CI and want to configure it for this repository. Now whenever I commit it test my code
using test.py and deploy it to Google App Service and Azure App Service when I push tagged commit.
[Read more](Docs/CI-CD.md)

## Docs and References

- [Read these Docs](docs/Setup.md) to learn how to use this run this web application.
- [Read these Docs](docs/The-Web-Application.md) to understand this web application.
- Learn About [Docker](https://www.freecodecamp.org/news/the-docker-handbook/) and [CI-CD](docs/CI-CD.md)

## Issues & Suggestions

If any issues and suggestions to me, you can create an [issue](https://github.com/PradyumnaKrishna/FER/issues).

## Donate

> **Why Donate?** GCP or Google App Engine isn't free

- Promote This Repo
- [Donate](https://www.paypal.me/pradyumnakrishna)

<h2></h2>

[Build-Badge]:          https://www.travis-ci.com/PradyumnaKrishna/Facial-AI.svg?branch=main

[Codecov-Badge]:        https://codecov.io/gh/PradyumnaKrishna/Facial-AI/branch/main/graph/badge.svg?token=SDFIZWFE3V

[Codecov]:              https://codecov.io/gh/PradyumnaKrishna/Facial-AI

[Travis-CI]:            https://www.travis-ci.com/PradyumnaKrishna/Facial-AI

[License-Badge]:        https://img.shields.io/badge/License-MIT-red.svg

[Version]:              https://github.com/PradyumnaKrishna/Facial-AI/tags/

[Version-Badge]:        https://img.shields.io/github/v/tag/PradyumnaKrishna/Facial-AI?label=Version