# WhatsApp Bot Project

This project implements a WhatsApp bot using Twilio, Flask, and GPT40. We can implement it later with Anthropic API.

## Prerequisites

- Python 3.7+
- A Twilio account
- An OpenAI API key

## Setup Instructions

1. Clone the repository:
git clone https://github.com/PatrickAttankurugu/whatsapp_bot.git

cd whatsapp_bot

2. Create a virtual environment and activate it:
   
python -m venv venv
source venv/bin/activate 

On Windows, use venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

4. Create a `.env` file in the project root and add your Twilio and OpenAI credentials:

TWILIO_ACCOUNT_SID=your_account_sid

TWILIO_AUTH_TOKEN=your_auth_token

OPENAI_API_KEY=your_openai_api_key

5. Sign up for a Twilio account and obtain a Twilio phone number.

6. Set up a Twilio WhatsApp Sandbox or use the production WhatsApp API (requires approval).

7. Configure your Twilio WhatsApp number to send incoming messages to your webhook URL:
`https://your-domain.com/webhook`

8. Start the Flask application:
python main.py

9. Use a tool like ngrok to expose your local server to the internet if testing locally.

## Usage

Send a message to your Twilio WhatsApp number. The bot will respond based on the conversation history and the OpenAI language model.

## Project Structure

- `main.py`: Main application file containing the Flask routes and bot logic
- `error_handlers.py`: Error handling functions
- `requirements.txt`: List of Python dependencies
- `.env`: Environment variables (not tracked in git)
- `whatsapp_bot.log`: Log file for messages and errors

## Logging

The application logs messages and errors to `whatsapp_bot.log`.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Twilio for providing the WhatsApp API
- OpenAI for the language model
- Flask for the web framework

## Contact

Project Link: [https://github.com/PatrickAttankurugu/whatsapp_bot](https://github.com/PatrickAttankurugu/whatsapp_bot)

## Note for Collaborators

- The main Twilio number for this project is +1 (415) 523-8886.
- If you're setting up your own development environment, you'll need to create your own Twilio account and obtain a separate Twilio number for testing.
- Make sure to never commit your `.env` file or expose your API keys.
- If you're outside Ghana, you may need to adjust some settings or permissions in your Twilio account.

Remember to always follow best practices for security and data privacy when working with API keys and user data.