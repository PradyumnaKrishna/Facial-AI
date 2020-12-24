# Getting Started

> Author: Pradyumna Krishna<br>
> UPDATED: 24/12/2020

<br>

**The Structure*** **of this Repository is like:**
```
Facial-AI
├── Docs
│   └── Docs related to this repository
├── FER
│   ├── edit.py
│   ├── haarcascade_frontalface_default.xml
│   ├── main.py
│   ├── model_weight.h5
│   ├── model.json
│   └── predict.py
├── templates
│   └── HTML templates that rendered by flasks
├── app.yaml
├── main.py
├── Procfile
└── requirements.txt
```

- **`Docs`**: This Directory contains docs related to this repository.
- **`FER`**: This Directory contians main files related to the web application. It contains a Flask Blueprint.
  - **`edit.py`**: This file take the image or file as an input and process it. Find no of faces and faces using `haarcascade` and apply TensorFlow model on them.
  - **`haarcascade_frontalface_default.xml`**: Used to detect faces.
  - **`main.py`**: Flask Blueprint, route web app, take user inputs and give output accordingly.
  - **`mode_weight.h5`**: Contains TensorFlow model used to predict emotions.
  - **`model.json`**: Contains layers of the TensorFlow model.
  - **`predict.py`**: Load the TensorFlow model and predict the emotion after taking input.
- **`templates`**: This Directory Contains HTML Templates that are rendered by flask.
- **`app.yaml`**: Stores configuration data, GCP or Google App Engine Configuration for deploy this applicaiton.
- **`main.py`**: Loads the Flask Blueprint present at `FER` directory and run it.
- **`Procfile`**: Stores configuration data, Heroku configuration for deploy this application.
- **`requirements.txt`**: Contains `python` libraries required for this web application to run.

**Next: [The Web Application](The%20Web%20Application.md)**

<h2></h2>
<sup>*Not including readme or license files.</sup>