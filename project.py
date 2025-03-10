from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

# Set up the Google API Key for the Generative AI service
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key="AIzaSyBBDTaQOfnHwHBTIHMmcNX_7FUpMoBgL24")

# Initialize the model and chat session
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# Create Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('book1.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    # Get user input from the request JSON
    user_input = f"You are a smart assistant. Your goal is to provide short, clear, and conversational responses to the user's input. Your tone should be casual, friendly, and human-like, with a touch of wit where appropriate. The response should be in a single, readable paragraph—no bullet points or lists. It must be structured in a way that's easy for a text-to-speech engine to read smoothly. Keep it concise and engaging, perfect for verbal communication. Input: {request.json.get('message')}"
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Send message to the bot
        response_raw = chat.send_message(user_input)

        # Debugging print to check the full response from the model
        print("Full response:", response_raw.text)

        # Ensure response_raw is valid and contains text
        if response_raw and response_raw.text:
            # Strip whitespace and return the full response text
            response = response_raw.text.strip()
        else:
            response = "I'm sorry, I couldn't generate a response."

        # Send response back to the frontend
        return jsonify({"response": response})

    except Exception as e:
        # If any error occurs, print and return the error message
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
