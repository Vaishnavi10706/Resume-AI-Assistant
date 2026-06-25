from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Resume AI Assistant Backend Running"

if __name__ == "__main__":
    app.run(debug=True)

# import datetime
# import time

# name = input("Please enter Your Name:")
# presentHour = datetime.datetime.now().hour
# if (5<= presentHour <=11):
#   print('Good Morning!',name, 'How can I help you')
# elif (12 <= presentHour <= 15):
#   print('Good Afternoon!',name, 'How can I help you')
# else:
#   print('Good Evening!',name, 'How can I help you')

# print("Namaste! Welcome to the Rule Based Chat Assistant.")
# print("You can ask me basic question. Typr 'bye' to exit from the bot")

# # Chatbot Memory Creation 

# responses = {
#   "hello" : "Hi, Welcome. How can I help you?",
#   "how are you": "I am very fine. Thank You",
#   "who are you": "I am smart AI chartbot",
#   "motivate me": "Keep going. Every bug of your project makes you a better developer.",
#   "happy": "Great to hear that",
#   "what is python": "It is a programming language. it is beginner friendly and easy to learn."
# }

# # Function getResponseOfBot
# def getResponseOfBot(userQuestion):
#   userQuestion = userQuestion.lower()
#   for key in responses:
#     if key in userQuestion:
#       return responses[key]
#   return "Sorry I don't know this yet. I am still in learning mode."

# # Take user input
# while True:
#   userInput = input("Please ask you question:")
#   reply = getResponseOfBot(userInput)
#   print("Bot Response:",reply)

#   if "bye" in userInput.lower():
#     break