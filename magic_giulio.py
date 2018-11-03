# -*- coding: utf-8 -*-

# This is a simple Hello World Alexa Skill, built using
# the implementation of handler classes approach in skill builder.
import logging
import random

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


class BravaIlariaIntentHandler(AbstractRequestHandler):
    """Handler for BravaIlaria Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("BravaIlaria")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        response = ["Ilaria è bravissima !",
                    "Come si farebbe senza Ilaria !",
                    "Nessuno è piu bravo di Ilaria.",
                    "Magic Giulio ha occhi solo per ilaria"]

        speech_text = random.choice(response)

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

        speech_text = "Questa funzione non è ancora implementata."

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
