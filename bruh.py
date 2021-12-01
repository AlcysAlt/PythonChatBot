#The AI Takeover has started
import random
questions = ["Ask me anything:", "What's your favourite hobby, "]

user_answer_hobby = " "
user_answer_random = " "

hobbies = [user_answer_hobby, "sports", "video games", "anime", "music", "art", "tinkering with electronics", "programming", "producing music", "laughing at the failures of humanity"]

modifiers = ["I personally like", "I prefer", "personally I dislike", "I personally hate", "I personally love"]
modifiers_2 = ["What a coinicidence, I also like ", "I hate ", "I love "]

answers_yesNo = ["Yes", "No"]


print("Welcome mortal, I am bruh.py, the world's most advanced computer program...")

name = input("So what's your name?")



while True:
    question =(random.choice(questions))
    
    if question == "Ask me anything:":
        user_answer_random = input(question)
        print (random.choice(answers_yesNo))
        
    elif question == "What's your favourite hobby, ":
        user_answer_hobby = input(question + name + "?")
        generate_hobby = random.choice(hobbies)
        if generate_hobby == user_answer_hobby:
            print (modifiers_2 + user_answer_hobby)
        else:
            generate_hobby = random.choice(hobbies)
            print ("As for me, " + random.choice(modifiers) + " " + random.choice(hobbies))



            
            



