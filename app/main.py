from flask import Flask, jsonify
import pandas as pd
from flask_cors import CORS
from model.person import Person
from model.company import Company

app = Flask(__name__)
CORS(app)
dfPersons = pd.read_csv('data/data.csv', sep=';')
dfCompanies = pd.read_csv('data/datasets_1455_2602_us_companies.csv', sep=',')

@app.route('/', methods=['GET'])
def route_default():
    return jsonify({'available endpoints': {"person_by_id": "/eggsapi/person/id", "all_persons": "/eggsapi/persons",
                                            "company_by_id": "/eggsapi/company/id", "all_companies": "/eggsapi/companies"}})


@app.route('/eggsapi/person/<id>', methods=['GET'])
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


@app.route('/eggsapi/persons', methods=['GET'])
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


@app.route('/eggsapi/company/<id>', methods=['GET'])
def route_get_company_by_id(id):
    format_id = int(id) - 1
    if format_id >= len(dfCompanies.index):
        return '{"Error": "id not available"}'
    else:
        c = Company(
            company_name_id=str(dfCompanies['company_name_id'].values[format_id]),
            url=str(dfCompanies['url'].values[format_id]),
            year_founded=str(dfCompanies['year_founded'].values[format_id]),
            city=str(dfCompanies['city'].values[format_id]),
            state=str(dfCompanies['state'].values[format_id]),
            zip_code=str(dfCompanies['zip_code'].values[format_id]),
            country=str(dfCompanies['country'].values[format_id]),
            full_time_employees=str(dfCompanies['full_time_employees'].values[format_id]),
            company_type=str(dfCompanies['company_type'].values[format_id]),
            company_category=str(dfCompanies['company_category'].values[format_id]),
            revenue_source=str(dfCompanies['revenue_source'].values[format_id]),
            business_model=str(dfCompanies['business_model'].values[format_id]),
            social_impact=str(dfCompanies['social_impact'].values[format_id]),
            description=str(dfCompanies['description'].values[format_id]),
            description_short=str(dfCompanies['description_short'].values[format_id]),
            source_count=str(dfCompanies['source_count'].values[format_id]),
            data_types=str(dfCompanies['data_types'].values[format_id]),
            example_uses=str(dfCompanies['example_uses'].values[format_id]),
            data_impacts=str(dfCompanies['data_impacts'].values[format_id]),
            financial_info=str(dfCompanies['financial_info'].values[format_id]),
            last_updated=str(dfCompanies['last_updated'].values[format_id]),
        )
    return c.to_json()


@app.route('/eggsapi/companies', methods=['GET'])
def route_get_companies():
    if len(dfCompanies.index) == 0:
        return '{"Error": "no data available"}'
    else:
        companies = []
        for index, row in dfCompanies.iterrows():
            c = Company(
                company_name_id=str(row['company_name_id']),
                url=str(row['url']),
                year_founded=str(row['year_founded']),
                city=str(row['city']),
                state=str(row['state']),
                zip_code=str(row['zip_code']),
                country=str(row['country']),
                full_time_employees=str(row['full_time_employees']),
                company_type=str(row['company_type']),
                company_category=str(row['company_category']),
                revenue_source=str(row['revenue_source']),
                business_model=str(row['business_model']),
                social_impact=str(row['social_impact']),
                description=str(row['description']),
                description_short=str(row['description_short']),
                source_count=str(row['source_count']),
                data_types=str(row['data_types']),
                example_uses=str(row['example_uses']),
                data_impacts=str(row['data_impacts']),
                financial_info=str(row['financial_info']),
                last_updated=str(row['last_updated']),
            )
            companies.append(c)

        companies_json = list(map(lambda company: company.to_json(), companies))

    return jsonify(companies_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7222)

