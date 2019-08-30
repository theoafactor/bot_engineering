from systems.core_sys import CoreSystem as Core
import pyttsx3
import speech_recognition as sr
import inspect

class NervousSystem(Core):

    def __init__(self, bot_name = None):
        if(bot_name == None):
            self.bot_name = 'Siri'
            self.mood = "I am not sad. Why are you interested?"
        
    
    def see(self):
        return "I can see"

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Start talking... : ")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)

                ## check for clue using the text .. 
                self.hear(text)
                #print("You said: {}".format(text))
            except:
                print("Sorry could not recognize your voice")

    def get_mood(self):
        pass
    

    def open_web_page(self):
        return "What website do you want me to open?"


    def talk(self, info):
        from systems.answers_library import answers
        engine = pyttsx3.init()
        engine.setProperty('rate', 135)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        check = answers.answers[info]


        #engine.say(answers.answers[info])

        print("Printing the clue from the answers package: ", info)

        print(type(answers.answers[info]))
       
        ## check the type of data returned by 
        engine.say(answers.answers[info])
         


        #engine.say(answers.answers[info])
        engine.runAndWait()
        engine.stop()

    
        
    
    def hear(self, information):
        ## check type of information
        ## - new:: convert the information to lowercase 
        information = information.lower()
        check = information.find('?')
        if check != None:
            information_list = list(information)
            quest = information_list[-1]
            if quest == '?':
                print("Is this your question? \n" + information)
                print("\n")
                confirmation = input("Enter Y to confirm, N to decline: ")
                confirmation = confirmation.lower()
                if confirmation == 'y' or confirmation == 'yes':
                    information_data = information.split()
                    ## check the category of question ... 
                    #print(information_data)
                    from systems.questions_library import questions
                    for clue, words in questions.clues.items():
                        for word in words:
                            if word in information_data:
                                self.talk(clue)
                                break
                        else:
                            pass
                        
        
                    
            else:
                #print("This is not a question")
                information_data = information.split()
                

                
                ## check the category of question ... 
                print(information_data)
                from systems.questions_library import questions
                for clue, words in questions.clues.items():
                    for word in words:
                        if word in information_data:
                            self.talk(clue)
                            break
                        else:
                            print(word)
                            pass
                    else:
                        print('Checking ...')
                        pass

        
        



