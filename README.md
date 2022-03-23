# streamlit-MS
Stremlit template for metabolic syndrome prediction using machine learning algorithm

## Table of contents
* [Table of contents](#Table-of-contents)
* [project structure](#Project-structure)
* [Technologies](#Technologies)
* [Setup](#Setup)
* [Status](#Status)
* [Reference](#Reference)

## Project structure
```
    .
    ├── script                  # Main Directory for python script 
    ├── requirement.txt         # Text file containing requirement library
    ├── main.py                 # Main python script for run application
    ├── .gitignore              # File containing list of file not upload to github
    └── README.md

```

## Technologies
* python 3.9.7
* streamlit 1.0.0

## Setup
Clone this project then install requirement libraries with following command
```
    >pip install -r requirement.txt
```
Or install to your virtual environment of choice (eg. poetry, conda, etc.)

Then try run following script to check your installation
```
    > python
    >>> import streamlit
    >>> streamlit.__version__
    '1.0.0'
```
if your console return similar output then your installation is finished

## Status
As of writing this markdown file, this project is not compatible for using. Most template for streamlit model is completed except the final model which doesn't have specific input variable yet. Also machine learning for this application is not completed yet due to problem in data cleaning process. 

In summary our current features and todo includes:

* features
    * Working template script for multipage streamlit application
    * Completed application script for model number 1-3
    * Each page uses form as a way to accept data thus improved performance by reduce number of refresh used.

* todo
    * Improve documentation
    * Intensive testing
    * Optimization
    * Incompleted application script for model number 4
    * Completed machine learning model for applications

## Reference
* [Streamlit documentation](https://docs.streamlit.io/library/get-started)
* [Building Multi Page Web App Using Streamlit by praneer nihar in medium.com](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4)
