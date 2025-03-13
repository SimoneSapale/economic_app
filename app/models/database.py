from flask_sqlalchemy import SQLAlchemy
import json
import pandas as pd

db = SQLAlchemy()

class GDP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    gdp = db.Column(db.Float, nullable=False)

class Inflation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    inflation = db.Column(db.Float, nullable=False)

def init_db():
    db.create_all()
    
    # Check if data already exists
    if GDP.query.count() == 0:
        # Load GDP data
        gdp_data = [
            {"year": 2014, "gdp": 25.1},
            {"year": 2015, "gdp": 26.3},
            {"year": 2016, "gdp": 27.6},
            {"year": 2017, "gdp": 29.5},
            {"year": 2018, "gdp": 31.4},
            {"year": 2019, "gdp": 33.0},
            {"year": 2020, "gdp": 32.2},
            {"year": 2021, "gdp": 35.5},
            {"year": 2022, "gdp": 37.8},
            {"year": 2023, "gdp": 38.5}
        ]
        
        # Duplicate data to reach 50 records
        gdp_extended = []
        for i in range(5):
            for item in gdp_data:
                gdp_extended.append({"year": item["year"] + i*10, "gdp": item["gdp"] * (1 + i*0.1)})
        
        for item in gdp_extended:
            db.session.add(GDP(year=item["year"], gdp=item["gdp"]))
    
    if Inflation.query.count() == 0:
        # Load inflation data
        inflation_data = [
            {"year": 2014, "inflation": 0.6},
            {"year": 2015, "inflation": 0.2},
            {"year": 2016, "inflation": 0.1},
            {"year": 2017, "inflation": 2.9},
            {"year": 2018, "inflation": 2.5},
            {"year": 2019, "inflation": 2.8},
            {"year": 2020, "inflation": 0.2},
            {"year": 2021, "inflation": 3.3},
            {"year": 2022, "inflation": 17.3},
            {"year": 2023, "inflation": 8.9}
        ]
        
        # Duplicate data to reach 50 records
        inflation_extended = []
        for i in range(5):
            for item in inflation_data:
                inflation_extended.append({"year": item["year"] + i*10, "inflation": item["inflation"] * (1 + i*0.2)})
        
        for item in inflation_extended:
            db.session.add(Inflation(year=item["year"], inflation=item["inflation"]))
    
    db.session.commit()
