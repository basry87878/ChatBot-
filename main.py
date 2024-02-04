import re
import long_responses as long


def message_probability(user_message,
                        recognised_words,
                        single_response=False,
                        required_words=[]):
  message_certainty = 0
  has_required_words = True

  for word in user_message:
    if word in recognised_words:
      message_certainty += 1

  # calculate percentage of recognized words
  percentage = float(message_certainty) / float(len(recognised_words))

  for word in required_words:
    if word not in user_message:
      has_required_words = False
      break

  if has_required_words or single_response:
    return int(percentage * 100)
  else:
    return 0  # lowest value


def check_all_messages(message):
  highest_prob_list = {}

  def response(bot_response,
               list_of_words,
               single_response=False,
               required_words=[]):
    nonlocal highest_prob_list
    highest_prob_list[bot_response] = message_probability(
        message, list_of_words, single_response, required_words)

  # responses---------------------------------------------
  response('Greetings!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
  response('I\'m doing well, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
  response('You\'re welcome!', ['thank', 'you'], required_words=['thank'])
  response(long.R_EATING, ['tell', 'me', 'about', 'your', 'eating', 'habits'], required_words=['you', 'eat'])
  response(long.R_LOCATION, ['where', 'are', 'you', 'from'], required_words=['where', 'you', 'from'])
  response(long.R_AGE, ['how', 'old', 'are', 'you'], required_words=['how', 'old'])
  response(long.R_FEELINGS, ['tell', 'me', 'about', 'your', 'feelings'], required_words=['you', 'feel'])
  response(long.R_JOKE, ['tell', 'me', 'a', 'joke'], required_words=['tell', 'joke'])
  response(long.R_GOODBYE, ['goodbye', 'bye', 'see', 'you'], required_words=['goodbye', 'bye', 'see', 'you'])


  best_match = max(highest_prob_list, key=highest_prob_list.get)
  # print(highest_prob_list)

  return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
  # split the message into an array to analyze each word separately
  split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
  response = check_all_messages(split_message)
  return response


# testing the response
while True:
  print('Bot: ' + get_response(input('You: ')))
