from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS
from model.person import Person

app = Flask(__name__)
CORS(app)
# load the file with the corresponding data
dfPersons = pd.read_csv('data/data.csv', sep=';')

@app.route('/', methods=['GET'])
def route_default():
    return jsonify({'available endpoints': {"person_by_id": "/sample/person/id", "all_persons": "/sample/persons"}})


@app.route('/sample/person/<id>', methods=['GET'])
def route_get_person_by_id(id):
    format_id = int(id) - 1
    if format_id >= len(dfPersons.index):
        return '{"Error": "id not available"}'
    else:
        p = Person(
            pid=str(dfPersons['pid'].values[format_id]),
            name=str(dfPersons['Name'].values[format_id]),
            vorname=str(dfPersons['Vorname'].values[format_id]),
            position=str(dfPersons['Position'].values[format_id]),
            telefon=str(dfPersons['Telefon'].values[format_id]),
            email=str(dfPersons['Email'].values[format_id])
        )
    return p.to_json()


@app.route('/sample/persons', methods=['GET'])
def route_get_persons():
    if len(dfPersons.index) == 0:
        return '{"Error": "no data available"}'
    else:
        persons = []
        for index, row in dfPersons.iterrows():
            p = Person(
                pid=str(row['pid']),
                name=str(row['Name']),
                vorname=str(row['Vorname']),
                position=str(row['Position']),
                telefon=str(row['Telefon']),
                email=str(row['Email'])
            )
            persons.append(p)
    persons_json = list(map(lambda person: person.to_json(), persons))
    return jsonify(persons_json)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7222)

