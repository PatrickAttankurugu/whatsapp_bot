import logging
from twilio.twiml.messaging_response import MessagingResponse

def handle_openai_error(e):
    logging.error(f"OpenAI API error: {str(e)}")
    resp = MessagingResponse()
    resp.message("[Bot] My circuits are a bit overloaded. Can you try again?")
    return str(resp)

def handle_twilio_error(e):
    logging.error(f"Twilio API error: {str(e)}")
    return "Error processing Twilio request", 400

def handle_general_error(e):
    logging.error(f"General error: {str(e)}")
    resp = MessagingResponse()
    resp.message("[Bot] Oops! I tripped over a binary. Let's try that again.")
    return str(resp)