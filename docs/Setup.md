# Getting Started

> Author: Pradyumna Krishna<br>
> UPDATED: 23/03/2021

<br>

Initally, when I made this web application, I used `virtualenv` in python to debug and run the `flask`. But as the time passes away,
I learned Docker and today there are two ways to set this application up. Lets talk about both of them:

## Docker

I created and pushed the Docker Images of my web application to [DockerHub](https://hub.docker.com/repository/docker/ipradyumna/facial-ai) and you can get it from [Github Packages](https://github.com/users/PradyumnaKrishna/packages/container/package/facial-ai) also.

### Run Web Application*

1. Pull the Docker Image:
    ```bash
    docker pull ghcr.io/pradyumnakrishna/facial-ai
    
    OR

    docker pull ipradyumna/facial-ai
    ```

2. Run the Docker image:
   ```bash
   docker run -p 8000:5000 facial-ai
   ```
   here, `8000` is your `localhost` port and `5000` is the `container` port.

3. Visit `https://127.0.0.1:8000`, where you find the web applicaiton running.

<sup>* Here you don't have to clone the repository</sup>

### To Build the Docker Image

1. Clone the Repository
   ```bash
   git clone https://github.com/PradyumnaKrishna/Facial-AI
   ```
2. Build the Docker Image
   ```bash
   docker build -t facial-ai .
   ```
   Here, provided [`Dockerfile`](../Dockerfile) which consist the config to build the docker image, If you have arm64 architecture then this Dockerfile will not work becuase tensorflow doesn't have a arm64 image. 
3. Now you can run the Docker Image using step 2 from above tutorial.

This tutorial will work to run the web applicaiton using Docker.

## Python Virtualenv
**`I recommend using Docker method`**

1. Clone the repository
   ```bash
   git clone https://github.com/PradyumnaKrishna/Facial-AI
   ```
2. Create and Activate Virtual Environment (optional)
   ```bash
   pip3 install virtualenv
   virtualenv env
   source ./env/bin/activate
   ```
3. Install Dependencies
   ```bash
   pip3 install -r requirements.txt 
   # use this command inside repository folder
   ```
4. Run the flask server
   ```bash
   python3 main.py
   ```
5. Visit `https://127.0.0.1:8000`, where you find the web applicaiton running.

That's all the information about how to setup this web application on your computer.

**Back: [Getting Started](Getting-Started.md)**<br>
**Next: [The Web Application](The-Web-Application.md)**