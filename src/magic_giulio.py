# -*- coding: utf-8 -*-

# This is a simple Hello World Alexa Skill, built using
# the implementation of handler classes approach in skill builder.
import logging
import random
from magic_giulio_response_set import parseJson
import requests
import csv
import os.path

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

response_set = parseJson("./brava_ilaria_response_set.json")


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Benvenuto in Alexa Skills Kit, puoi dirmi ciao, chiedere di Ilaria o cercare i voli!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Magic Giulio", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response


name_slot_female = "Ilaria"
name_slot_male = "Giulio"

endpoint_domain = ""
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "endpoint.config")
with open(path, 'r') as config:
    endpoint_domain = config.read().replace('\n', '')

class BravaIlariaIntentHandler(AbstractRequestHandler):

    """Handler for BravaIlaria Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("BravaIlaria")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        slots = handler_input.request_envelope.request.intent.slots
        logger.log(logging.INFO, "Slots = " + str(slots))

        if name_slot_female in slots and slots[name_slot_female].value is not None:
            name = slots[name_slot_female].value
            logger.log(logging.INFO, "Slot [" + name_slot_female + "] = " + name)
            if name.lower() == "ilaria":
                responses = response_set["BravaIlaria"]["responses"]
                speech_text = random.choice(responses)
            else:
                responses = response_set["BravaIlariaDonna"]["responses"]
                speech_text = random.choice(responses)
        elif name_slot_male in slots and slots[name_slot_male].value is not None:
            responses = response_set["BravaIlariaUomo"]["responses"]
            speech_text = random.choice(responses)
        else:
            speech_text = "non pretendere che faccia complimenti a qualcuno senza nome !"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Magic Giulio <3 Ilaria", speech_text)).set_should_end_session(
            True)
        return handler_input.response_builder.response


class CercaVoliIntentHandler(AbstractRequestHandler):
    """Handler for BravaIlaria Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("CercaVoli")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        slots = handler_input.request_envelope.request.intent.slots
        logger.log(logging.INFO, "Slots = " + str(slots))
        cityA = "cityA"
        cityB = "cityB"

        if cityA in slots and slots[cityA].value is not None and cityB in slots and slots[cityB].value is not None:
            #do search
            logger.log(logging.INFO, "From: " + slots[cityA].value + " to: " + slots[cityB].value)

            if endpoint_domain == "":
                speech_text = "Non so dove cercare i prezzi dei voli. Contatta lo sviluppatore."
            else:
                url = endpoint_domain + "/api/v1/flight/" + slots[cityA].value + "/" + slots[cityB].value
                logger.log(logging.INFO, "URL:" + url)
                r = requests.get(url, timeout=30)
                json_response = r.json()
                logger.log(logging.INFO, json_response)
                

                speech_text = "Non sono ancora completa ... chiedi al mio sviluppatore di completarmi "
        else:
            speech_text = "Non ho capito quali sono le città da cui vuoi partire e arrivare."

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Magic Giulio - voli", speech_text)).set_should_end_session(
            True)
        return handler_input.response_builder.response


class CiaoIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("CiaoIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Ciao, Magic Giulio e' a tua completa disposizione"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Magic Giulio", speech_text)).set_should_end_session(
            True)
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Puoi dirmi ciao o puoi chiedere quanto e' brava Ilaria."

        handler_input.response_builder.speak(speech_text).ask(
            speech_text).set_card(SimpleCard(
                "Magic Giulio", speech_text))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Ciao!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Magic Giulio", speech_text))
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = (
            "Magic Giulio non riesce ad aiutarti in questo.  "
            "Puoi dirmi ciao!!")
        reprompt = "Puoi dire ciao!!"
        handler_input.response_builder.speak(speech_text).ask(reprompt)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return handler_input.response_builder.response


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speech = "Mi dispiace, ma Magic Giulio non e' riuscito a capire la tua domanda."
        handler_input.response_builder.speak(speech).ask(speech)

        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())

sb.add_request_handler(BravaIlariaIntentHandler())
sb.add_request_handler(CiaoIntentHandler())
sb.add_request_handler(CercaVoliIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()
