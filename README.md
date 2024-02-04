# ChatBot-
simple conversational agent that responds to user inputs based on predefined recognition patterns. 




functionality:

    User Input Processing:
        The bot takes user input as a string and splits it into a list of words using a regular expression.
        It converts the input to lowercase for case-insensitive matching.

    Message Probability Calculation:
        For each predefined response, it calculates a probability score based on the presence of recognized words in the user's input.
        The probability score is the percentage of recognized words in the user's input out of the total recognized words.

    Required Words Check:
        It checks if certain required words are present in the user's input. If they are, it ensures a higher probability for that response.

    Response Selection:
        The bot maintains a list of response probabilities for each predefined response.
        It selects the response with the highest probability as the best match.

    Continuous Interaction:
        The bot runs in a continuous loop, prompting the user for input and providing responses.
        If the calculated probability for the best match is below a certain threshold, it returns a default "unknown" response.

    Predefined Responses:
        The bot has predefined responses for greetings, well-being inquiries, expressions of gratitude, and inquiries about eating habits, location, age, feelings, jokes, and goodbyes.

    Long Responses:
        Some responses are delegated to a separate module (long_responses) for better organization.
        Examples include responses related to eating habits, feelings, jokes, and goodbyes.
