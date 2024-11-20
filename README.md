# DataScienceIndustrialization
A project to industrialize a Data Science model through containerization.

## Table of contents

- [Project Description](#project-description)
- [Technologies and Libraries Used](#technologies-and-libraries-used)
- [Quick start](#quick-start)
- [Project Organization](#project-organization)
- [Contributors](#contributors)

## Project Description

(Describe the project, the valuable scope, the usages and include the use of GenAI - Why...)

## Technologies and Libraries Used

(List all the technologies/libraries used and explain why - potentially include the versions to say that if it doesn't work you have to add in the requirements.txt e.g. keras 1.2.5)

## Quick Start

1. Delete the virtual environment and create a new one.

```linux
pip install --upgrade pip virtualenv
python -m venv myvenv
./myvenv/Scripts/activate   # On Windows
source .venv/bin/activate   # On Unix/MacOS
```

2. Open Docker Desktop and make sure that you are logged and that the Docker Engine is launched.

```linux
docker build -t weather-classification .
```

N.B. Can take time!
If this command doesn't work, try to log out and then log in again.

3. ...

## Project Organization

```text
DSindustrialization/
├── data/
    ├── .jpg files
    └── pretrained_model.h5
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

(Explain each folders and files)


## Contributors

**Salma**: <[https://github.com/tarifasalma15](https://github.com/tarifasalma15)>
**Nourhene**: <[https://github.com/nourhene2](https://github.com/nourhene2)>
**Christian**: <[https://github.com/mbialeuk](https://github.com/mbialeuk)>
**Chelsie**: <[https://github.com/chelsie1234](https://github.com/chelsie1234)>
