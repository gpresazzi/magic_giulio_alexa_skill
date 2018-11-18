import subprocess
import re


brava_response = ["Ilaria è bravissima !",
                "Come si farebbe senza Ilaria !",
                "Nessuno è piu bravo di Ilaria.",
                "Magic Giulio ha occhi solo per ilaria"]

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
    assert speak_response in brava_response


def test_brava_ilaria_donna():
    json='brava-ilaria-donna-1.json'
    speak_response = get_alexa_text_speak('handler', json)
    print(speak_response)
    assert speak_response.lower() == "Sei brava, ma non sarai mai brava quanto Ilaria.".lower()


def test_brava_ilaria_uomo():
    json='brava-ilaria-uomo-1.json'
    speak_response = get_alexa_text_speak('handler', json)
    print(speak_response)
    assert speak_response.lower() == "magic giulio non e' cosi' sensibile da fare complimenti a uomini".lower()