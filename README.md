# Flask App Data Dashboard

This is a python Flask app data dashboard that pulls data from the World Bank API. The visualizations are made with the plotly library.

Here is a working version of the app: [https://world-bank-dashboard-api.herokuapp.com](https://world-bank-dashboard-api.herokuapp.com)

# Getting Started

To get the app working locally:
1. Clone or download the repository locally
2. Within the world_bank_api_dashboard directory, create a virtual Python environment with the Terminal command `python3 -m venv flaskapp` where `flaskapp` is the name of your environment. You can choose any name.
3. Activate the virtual environment with the command `source flaskapp/bin/activate`
4. Then run the command `pip install -r requirements.txt`
5. Next, set the FLASK_APP variable to worldbank.py by running the following command `export FLASK_APP=worldbank.py`.
6. And finally, run the command `python -m flask run` to start the app
7. The terminal will output the local web address and port where the app is running. As an example, this might be `http://127.0.0.1:5000/`. Now, open a web browser and go to that web address.

# Prerequisites

You will need [Python3 installed](https://www.python.org/downloads/) on your local machine.

# Deployment

This flask app can be used as a template for visualizing your own data. Use
the template to enhance your professional portfolio. 

## Prerequisites

To install the flask app, you need:
- python3
- python packages in the requirements.txt file
 
 Install the packages with
``` 
 pip install -r requirements.txt
```

## Installing

On a MacOS/linux system, installation is easy. Open a terminal, and go into 
the directory with the flask app files.  

## TODO Fill out the rest of the instructions
