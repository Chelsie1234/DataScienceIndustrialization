# DataScienceIndustrialization
A project to industrialize a Data Science model through containerization. This project is about making a machine learning model easy to use and ready for real-world applications by **packaging it into a Docker container**. Think of it as creating a portable box that anyone can run without worrying about setup.

## Table of contents

- [Project Description](#project-description)
  - [What does the project do?](#what-does-the-project-do)
  - [How does it work?](#how-does-it-work)
  - [Extra Features](#extra-features)
  - [Why is this useful?](#why-is-this-useful)
  - [Who benefits from this?](#who-benefits-from-this)
  - [Scopes of the Project](#scopes-of-the-project)
- [Technologies, Libraries, and Language Used](#technologies-libraries-and-language-used)
- [Quick Start](#quick-start)
  - [Method 1](#method-1)
  - [Method 2](#method-2)
- [Project Organization](#project-organization)
- [Contributors](#contributors)

## Project Description

For this project, we used GenAI to help us in the documentation process and to make an understandable markdown more quickly.

### What does the project do?
- It uses a **weather classification model** to look at pictures and decide if the weather in the image is **"sunny"**, **"foggy"**...

### How does it work?
1. **Prepare the Model and Script**:
   - Start with a pre-trained weather classification model.

2. **Build a Docker Container**:
   - Use Docker (a tool that makes software run anywhere) to create a container (a self-contained environment).
   - The container includes:
     - The Python program and all the libraries it needs.
     - A way to process images stored in a folder.
     - A way to save results (predictions) to another folder.

3. **What Happens When You Run It?**
   - The container automatically:
     - Loads all the pictures in the input folder.
     - Predicts the weather for each picture.
     - Saves the results in a CSV file (a table with the image name and the prediction).
   - If it’s told to, it skips already processed images to save time.

### Extra Features:
- **Bonus 1**: It’s smart enough not to repeat work unless you specifically tell it to.
- **Bonus 2**: Uses automation tools to make updates and deployment faster and easier.

### Why is this useful?
It makes complex machine learning models:
- **Easy to use**: No special setup needed; just run the container.
- **Portable**: Works the same on any computer.
- **Efficient**: Handles images and predictions automatically.

### Who benefits from this?
Anyone who wants to use machine learning models without having to be a technical expert or spend hours setting up the environment.

### Scopes of the Project:

1. <U>End-to-End Deployment</U>:

    * This project transforms a local machine learning model into a fully-deployed, automated service that can be used by non-technical teams.
    * The containerized solution ensures easy portability, scalability, and reliability.

2. <U>Predictive Insights</U>:

    * Automatically analyzes a directory of images and classifies them into weather categories.
    * Outputs results in a structured format (CSV), which can be used for downstream tasks like weather reporting, forecasting, or data visualization.

3. <U>Automation</U>:

    * Automation using GitHub Actions ensures a streamlined deployment process.

4. <U>Resilience in Real-Time Use</U>:

    * Implements mechanisms to avoid re-processing already predicted images, saving computation time and improving efficiency.
    * Fault tolerance is achieved through clean and documented code and Docker orchestration.

5. <U>Wide Usability</U>:

    Can be extended for commercial use cases like:
    * Tourism (weather impact visualization for vacation planning).
    * Agriculture (helping farmers monitor weather conditions for crops).
    * Insurance (risk prediction based on weather).


## Technologies, Libraries, and Language Used

<p align="center">
  <a href="https://www.python.org">
    <img alt="Python" src="https://i0.wp.com/junilearning.com/wp-content/uploads/2020/06/python-programming-language.webp?fit=800%2C800&ssl=1" height="50" />
  </a>
  &nbsp;
  <a href="https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/">
    <img alt="Virtualenv" src="https://www.cheatsheet.fr/wp-content/uploads/2019/09/python-virtual-environments.png" height="50" />
  </a>
  &nbsp;
  <a href="https://keras.io/">
    <img alt="Keras" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Keras_logo.svg/1200px-Keras_logo.svg.png" height="50" />
  </a>
  &nbsp;
  <a href="https://numpy.org/">
    <img alt="Numpy" src="https://avatars.githubusercontent.com/u/288276?s=280&v=4" height="50" />
  </a>
  &nbsp;
  <a href="https://pandas.pydata.org/">
    <img alt="Pandas" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKPePf0eI9lrP20Ym-P0v-_B2yB6IHRoQiWw&s" height="50" />
  </a>
</p>

<p align="center">
  <a href="https://www.tensorflow.org/?hl=en">
    <img alt="TensorFlow" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Tensorflow_logo.svg/langfr-220px-Tensorflow_logo.svg.png" height="50" />
  </a>
  &nbsp;
  <a href="https://scikit-learn.org/stable/">
    <img alt="Scikit-learn" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/800px-Scikit_learn_logo_small.svg.png" height="50" />
  </a>
  &nbsp;
  <a href="https://seaborn.pydata.org/">
    <img alt="Seaborn" src="https://cdn.prod.website-files.com/60ec34540d013784844d2ee2/61fe97cb292d1f79de62e1d1_Seaborn%20-%20Bibliotheque%20Python.png" height="50" />
  </a>
  &nbsp;
  <a href="https://matplotlib.org/">
    <img alt="Matplotlib" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" height="50" />
  </a>
  &nbsp;
  <a href="https://tqdm.github.io/">
    <img alt="TQDM" src="https://avatars.githubusercontent.com/u/12731565?v=4" height="50" />
  </a>
</p>

<p align="center">
  <a href="https://www.docker.com/">
    <img alt="Docker" src="https://logos-world.net/wp-content/uploads/2021/02/Docker-Emblem.png" height="50" />
  </a>
  &nbsp;
  <a href="https://hub.docker.com/">
    <img alt="Docker Hub" src="https://miro.medium.com/v2/resize:fit:734/0*sCPc1Ib1zT0Lg1vi.png" height="50" />
  </a>
</p>


## Quick Start

### Method 1:

1. The following command will locally installed the Docker image in Docker Desktop but has it is really heavy (mostly because of the model) so you can wait or go directly to the method 2.

```docker pull tarifasalma/datascience_industrialization:latest```

2. To execute the container:

```docker run --name container-datascience tarifasalma/datascience_industrialization:latest```

3. To verify files that exist in the container (our predictions):

```docker exec -it container-datascience ls -l /app/output```

### Method 2:

1. **Clone this repository.**

2. **Open your terminal and go to your associated folder with the command ```cd```.**

3. **Create a new virtual environment to handle the packages.**

```
pip install --upgrade pip virtualenv
```
<br>
```
python -m venv myvenv
```

On Windows:
```
./myvenv/Scripts/activate
```

On Unix/MacOS:
```
source .venv/bin/activate
```

4. **Open Docker Desktop and make sure that you are logged and that the Docker Engine is launched.**

```
docker build -t weather-classification .
```

N.B. Can take time!
If this command doesn't work, try to log out and then log in again.
When it's done, you should see a new Docker Image named "weather-classification".

5. **Run the image to create a container with the following command:**

```
docker run `
    -v "${PWD}/data:/app/data" `
    -v "${PWD}/output:/app/output" `
    "weather-classification"
```

If it's not working try to replace the ``` ` ``` by ```\```
At the end, you should be able to see a new CSV file appearing at the end of the output folder with the predictions done.<br>Also a new container as been created in Docker Desktop and if you run the container and you go to ```files --> app --> output```, you should see the predictions CSV files.

## Project Organization

```text
DSindustrialization/
├── .github/workflows/
    └── docker-hub-image.yml
├── data/
    └── images.jpg
├── output/
    └── predictions.csv
├── myvenv/
    ├── bin
    ├── include
    ├── lib
    ├── share
    └── pyvenv.cfg
├── dockerfile
├── requirements.txt
├── weather-classification-TP.ipynb
└── weather-classification-TP.py
```

- **.github/workflows** contains the file to make the process of build the containerize process automated. It is triggered by every pull or push to the main branch.
- **data** contains all the images that we want to predict.
- **output** contains all the csv files of our predictions (name_of_the_image, prediction).
- **myvenv** contains all of our packages.
- **dockerfile** contains the process to install the dependencies and copy in the Docker Container the python file, the model, the data (input) and output folders.
- **requirements.txt** contains all the needed libraries.
- **weather-classification-TP** contains our executable script to run our predictions.


## Contributors

**[Salma](https://github.com/tarifasalma15)**<br>
**[Nourhene](https://github.com/nourhene2)**<br>
**[Christian](https://github.com/mbialeuk)**<br>
**[Chelsie](https://github.com/chelsie1234)**<br>
