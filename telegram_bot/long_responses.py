# long_responses.py

R_EATING = "I cannot eat because I am not human; I'm a Bot, obviously!"
R_LOCATION = "I exist in the digital realm, so I don't have a physical location like humans do."
R_AGE = "I don't have an age; I'm just a piece of software. How can I assist you     today?"
R_FEELINGS = "I don't have feelings, but I'm always ready to help and chat with you."
R_JOKE = "Sure, here's a joke for you: Why don't scientists trust atoms? Because they make up everything!"
R_GOODBYE = "Goodbye! If you have more questions or just want to chat, feel free to return anytime."


def unknown():
    response_options = ['Could you please re-phrase that?', "I'm not sure what you mean.", "Interesting point!", "What does that mean?"]
    return random.choice(response_options)
