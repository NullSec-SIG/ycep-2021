import json


# Source from https://corona.lmao.ninja/v2/countries
COVID_DATA_FILE = './covid_data.json'


with open(COVID_DATA_FILE, 'r') as covid_data:
    COVID_DATA = json.load(covid_data)


COUNTRY_LIST = [country_data["country"] for country_data in COVID_DATA]


COUNTRY_MAP = {country_data["country"]: country_data for country_data in COVID_DATA}


def get_all_data() -> dict:
    return COVID_DATA


def get_countries() -> list:
    return COUNTRY_LIST


def get_country_details(country_name) -> dict:
    return COUNTRY_MAP.get(country_name)
