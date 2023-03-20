import re
import long_responses as long


"""

    Our currently defined functions:                                                                STRUCTURES USED:
    ------------------------------------                                                            -------------------------------
        - message_probability(msg, rec_words, sg_resp, req_words):                                  DEFINE FUNCTION
            - set certainty = 0                                                                     DECLARE VARIABLE
            - loop through and count number of words - increment certainty                          LOOP, ARITHMETIC OP
            - calculate percentage of recognized words: certainty / number of recognized words      ARITHMETIC OP
            - run through required words - check if certain words are there                         LOOP, IF-CONDITIONAL
            - must either return required words or single response                                  IF-CONDITIONAL

        - check_all_messages(msg):                                                                  DEFINE FUNCTION
            - declare empty dictionary                                                              DECLARE DICTIONARY
            - define a new function: response(resp, list, single, req) --> highest_prob_list{}      DEFINE                          
            - populate with a few responses at the outset                                           USE FUNCTION
            - best_match = max(highest_prob_list, key=highest_prob_list.get): return highest prob   SET VARIABLE

        - get_response(usr_input):                                                                  DEFINE FUNCTION
            - lower all words in user input                                                         MANIPULATE VARIABLE
            - parse the words using regular expression: split when hitting [,;?!.-]                 MANIPULATE VARIABLE
            - run the result through check_all_messages() --> fetches most likely response          RETURN MOST LIKELY RESPONSE

    Main:
    ------------------------------------
        - run forever while = True: ...                                                             LOOP

"""


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
