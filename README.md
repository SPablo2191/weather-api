# WEATHER API REST ☁️⛈️🌧️🌦️🌥️🌤️

## Introduction:

Welcome to the weather API powered by [Open Weather](https://openweathermap.org/)

## Table of content:

- [Author](#author👀)
- [Technologies](#technologies-👨‍💻)
- [Environments](#environments-💻)
- [Configuration](#configuration-🤖)
- [Modules](#modules-🚨)

## Author👀

- [Pablo Sandoval](https://github.com/SPablo2191)

## Technologies 👨‍💻

![FastAPI](https://img.shields.io/badge/FastAPI-0.101.1-brightgreen.svg)

## Environments 💻

![Linux](https://img.shields.io/badge/Linux-compatible-green)
![Windows](https://img.shields.io/badge/Windows-compatible-green)

## Configuration 🤖
## Installation 🤖
To use the project locally, you need to follow these steps:

1) Enter the following commands in the console:

```bash
python3 -m venv [nameOfTheVirtualEnvironment]
```

This command will create a virtual environment for you to later import packages there. To activate it, use the following command:

```bash
source nameOfTheVirtualEnvironment/bin/activate
```
NOTE: In case you are working on Windows, the virtual environment is created with scripts, so you need to activate the virtual environment as follows:

```bash
nameOfTheVirtualEnvironment\Scripts\activate.bat
```
And to deactivate it (in both cases), use:

```bash
deactivate
```

2) Then run the following command to obtain the packages used in the API:

```bash
pip install -r requirements.txt
```

3) Finally run the following command in the terminal:

```bash
cd src/ && uvicorn main:app --reload
```

## Modules 🚨
