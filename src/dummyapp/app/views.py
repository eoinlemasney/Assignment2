 # dummyapp/app/views.py
from flask import render_template
from app import app
from systeminfo.main import get_platform 
import systeminfo

@app.route('/')
def index():
        returnDict = {}
        returnDict['user'] = 'Eoin Le Masney'
        returnDict['title'] = 'Home'
        returnDict['sys'] = systeminfo.get_platform_info()
        return render_template("index.html", **returnDict)
