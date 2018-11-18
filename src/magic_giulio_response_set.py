import os
import json


"""Magic giulio response set in a JSON structure"""
def parseJson(filename):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, filename), encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        return data
