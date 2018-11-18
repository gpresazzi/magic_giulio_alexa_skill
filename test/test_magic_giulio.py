import subprocess
import re
import json
import os


def parseJson(filename):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(__location__, filename), encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        return data


response_set = parseJson("../src/brava_ilaria_response_set.json")
brava_response = response_set["BravaIlaria"]["responses"]


def get_alexa_text_speak(function_name, json_event):
    list_of_commands = ['python-lambda-local', '-f', function_name, './src/magic_giulio.py',
                                       './test/test-json/' + json_event]
    process = subprocess.check_output(list_of_commands, timeout=2)
    result_string = 'RESULT:'
    out = process.decode('UTF-8')
    response_array = out.split('[root')
    if len(response_array) < 3:
        raise Exception(f"Unable to parse the response of the command: {list_of_commands}")

    result_element = response_array[4]

    index = result_element.find(result_string)
    if index < 0:
        raise Exception(f"RESULT object not found as a response." +
                        f"try to run the command with a different input. {list_of_commands}")

    matchObj = re.search(r'<speak>(.*)</speak>', result_element, re.M | re.I)
    speak_text = matchObj.group(1)

    string_json = result_element[index + len(result_string):len(result_element)-1]
    string_json = string_json.replace('\'', '\"')
    string_json = string_json.replace('True', 'true')
    string_json = string_json.replace('False', 'false')

    return speak_text


def test_brava_ilaria():
    json='brava-ilaria-1.json'
    speak_response = get_alexa_text_speak('handler', json)
    print(speak_response)
    assert speak_response in response_set["BravaIlaria"]["responses"]


def test_brava_ilaria_donna():
    json='brava-ilaria-donna-1.json'
    speak_response = get_alexa_text_speak('handler', json)
    print(speak_response)
    assert speak_response in response_set["BravaIlariaDonna"]["responses"]


def test_brava_ilaria_uomo():
    json='brava-ilaria-uomo-1.json'
    speak_response = get_alexa_text_speak('handler', json)
    print(speak_response)
    assert speak_response in response_set["BravaIlariaUomo"]["responses"]