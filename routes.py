from flask import render_template, jsonify, request
import json

from app import app, db
from model import *
from orm import *


@app.route('/')
def main():
    return render_template('home.html')


@app.route('/createProject', methods=["GET", "POST"])
def create_project():
    if request.method == 'POST':
        data = request.form
        limit = int(data['limit'])
        print(list(data.items()))
        #[('cityOpt', 'Москва'), ('MskDistrictOpt', 'ЦАО'), ('spbDistrictOpt', 'Центральный'), ('buildingType', 'Больница'), ('schoolType', 'no')]
        if data['cityOpt'] == "Москва":
            # req = History(
            #     city=data['cityOpt'],
            #     district=data['MskDistrictOpt'],
            #     building_type=data['buildingType'],
            #     school_type=data['schoolType'],
            #     limit=int(data['limit'])
            #     #     score=modelmsk.score()
            # )
            # db.session.add(req)
            # db.session.commit()

            return render_template('createProject.html',  model_score=hospital_model(
                data['cityOpt'],
                data['MskDistrictOpt'],
                limit,
                'isCardiology' in data,
                'isOntology' in data,
                'isPulmotology' in data,
                'isNeurology' in data,
                'isTheraphy' in data,
                'isSurgery' in data
            ))
        else:
            # req = History(
            #     city=data['cityOpt'],
            #     district=data['spbDistrictOpt'],
            #     building_type=data['buildingType'],
            #     school_type=data['schoolType'],
            #     limit=int(data['limit']),
            # #     score=modelspb.score()
            # )
            # db.session.add(req)
            # db.session.commit()

            return render_template('createProject.html',  model_score=hospital_model(
                data['cityOpt'],
                data['spbDistrictOpt'],
                limit,
                'isCardiology' in data,
                'isOntology' in data,
                'isPulmotology' in data,
                'isNeurology' in data,
                'isTheraphy' in data,
                'isSurgery' in data
            ))
    else:
        return render_template('createProject.html', model_score=False)


@app.route('/contact')
def contact():
    return render_template('contact.html')
