import logging
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
import random
import traceback
from error_handlers import handle_twilio_error, handle_general_error
from twilio.base.exceptions import TwilioRestException
from collections import deque

# Set up logging
logging.basicConfig(filename='whatsapp_bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

app = Flask(__name__)
llm = OpenAI(temperature=0.7, max_tokens=100)

# Conversation memory
conversation_history = {}
MAX_HISTORY = 5

@app.route("/webhook", methods=['POST'])
def webhook():
    try:
        incoming_msg = request.values.get('Body', '').strip()
        sender = request.values.get('From', '')
        logging.info(f"Received message from {sender}: {incoming_msg}")

        resp = MessagingResponse()
        msg = resp.message()
        
        bot_identifiers = [
            "[Bot] ",
            "[Not Patrick] ",
            "[Patrick's Sarcastic Assistant] ",
            "[Beep Boop] ",
            "[Totally Not Human] "
        ]
        
        # Get or create conversation history for this user
        if sender not in conversation_history:
            conversation_history[sender] = deque(maxlen=MAX_HISTORY)
        
        # Add user message to history
        conversation_history[sender].append(f"Human: {incoming_msg}")
        
        # Construct prompt with conversation history
        history = "\n".join(conversation_history[sender])
        prompt = f"""
        Here's the conversation history:
        {history}
        
        Respond to the last message. Be fun, sarcastic, and engaging in your response.
        Keep it concise (1-2 sentences max).
        Do not pretend to be Patrick or a human.
        """
        
        response = llm.invoke(prompt)
        logging.info(f"Generated response: {response}")
        
        full_response = f"{random.choice(bot_identifiers)}{response.strip()}"
        msg.body(full_response)
        
        # Add bot response to history
        conversation_history[sender].append(f"Bot: {full_response}")
        
        return str(resp)
    
    except TwilioRestException as e:
        return handle_twilio_error(e)
    except Exception as e:
        return handle_general_error(e)

@app.route("/test", methods=['GET'])
def test():
    logging.info("Test route accessed")
    return "WhatsApp bot is running!", 200

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unhandled exception: {str(e)}")
    logging.error(traceback.format_exc())
    return "An unexpected error occurred", 500

if __name__ == "__main__":
    logging.info("Starting Flask application...")
    app.run(debug=True)