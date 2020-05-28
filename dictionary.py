import json
import difflib
from difflib import get_close_matches

with open("E:/courses/courses from udemy/the python mega courses_build 10 real world application/Application_onedictionary/content.json","r+") as f:
    data = json.load(f)
#excontent= json.load(open("E:/courses/courses from udemy/the python mega courses_build 10 real world application/Application_onedictionary/content.json",encoding='utf-8'))
def translate_word(wo):
    word = wo.lower()
    if word in data:
        #check if hat word is present in data then return that word's value
        return data[word]
        #len bcz below line is a list object so to check whether lenght is breater than 0
    elif len(get_close_matches(word, data.keys())) > 0:
        continue_input = input("did you mean %s instead? Enter Y to proceed or N to stop :  " % get_close_matches(word,data.keys())[0])
        if continue_input == "Y":
            return data[get_close_matches(word,data.keys())[0]]
            #if user pass y and pass that word else you need not to return anything
            # but bcz of indentation it will not goes to else so elif
        elif (continue_input == "N"):
            return "word you are searching for does'nt exists.. We will update it soon"
        else:
            return "we did'nt understand your entry"
    else:
        #thiNs else bcz we dont want none as output
        return "The word does not exists. Please double check it"

wordtocheck = input("Please enter word to find in dictionary: ")
final_meaning = (translate_word(wordtocheck))
print(final_meaning)
#if type(final_meaning) == list:
#    for values in final_meaning:
 #       print(values)
 #   else:
 #       print(values)