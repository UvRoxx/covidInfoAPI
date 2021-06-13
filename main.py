from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import requests

app = Flask(__name__)


@app.route('/')
def home():
    parent_data = requests.get("https://disease.sh/v3/covid-19/historical/all?lastdays=120","html.parser").json()
    parent_data['recovered'] = requests.get('https://disease.sh/v3/covid-19/vaccine/coverage?lastdays=all&fullData=false',"html.parser").json()
    return jsonify(parent_data)



if __name__ == "__main__":
    app.run(debug=True)
