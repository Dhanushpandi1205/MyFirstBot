import os
import openai
from dotenv import load_dotenv
from flask import Flask, request, render_template

load_dotenv()  # ✅ Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")  # ✅ Read key from .env

# Initialize your Flask app
app = Flask(__name__)

# Replace this with your OpenAI API key


# Store conversation
messages = [{"role": "system", "content": "You are a helpful assistant."}]

@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_message = request.form["message"]
        messages.append({"role": "user", "content": user_message})

        # Send message to OpenAI and get response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if available
            messages=messages
        )

        bot_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": bot_reply})

        return render_template("chat.html", user_input=user_message, bot_reply=bot_reply)

    return render_template("chat.html")

if __name__ == "__main__":
  
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)

