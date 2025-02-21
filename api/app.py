import os
import requests
from flask import Flask, request
from flask_cors import CORS, cross_origin
from typing import Optional
from sqlalchemy import String
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session

DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass

class WeatherCondition(Base):
    __tablename__ = "weather_condition"

    id: Mapped[int] = mapped_column(primary_key=True)
    temp_f: Mapped[int]
    condition: Mapped[str] = mapped_column(String(30))
    city: Mapped[Optional[str]]
    reported_by: Mapped[str] = mapped_column(String(30))


app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

WORKER_URI = os.environ.get("WORKER_URI")

Base.metadata.create_all(engine)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/dowork")
def do_work():
    return requests.get(f'{WORKER_URI}/hello').content

@app.route("/weather/")
@cross_origin()
def weather():
    weather_reports = []
    with Session(engine) as session:
        stmt = select(WeatherCondition)
        reports = session.scalars(stmt)

        print('***************** data *****************')
        # print(dir(reports))

        for report in reports:
            print(report)
            weather_reports.append({
                'id': report.id,
                'temp_f': report.temp_f,
                'condition': report.condition,
                'city': report.city,
                'reported_by': report.reported_by,
            })
            print(weather_reports)
    return weather_reports


@app.route("/report_weather", methods=['POST'])
@cross_origin()
def report_weather():
    data = request.get_json()  # a multidict containing POST data

    temp = data.get('temperature', None)
    condition = data.get('condition', None)
    city = data.get('city', None)
    reported_by = data.get('reported_by', None)

    with Session(engine) as session:
        weather = WeatherCondition(
            temp_f=temp,
            condition=condition,
            city=city,
            reported_by=reported_by
        )

        session.add_all([weather])
        session.commit()

    return "Thanks."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
