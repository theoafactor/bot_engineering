from systems.core_sys import CoreSystem as Core
import pyttsx3
import speech_recognition as sr
import inspect
import datetime



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


    def found(self):
        pass

    def get_mood(self):
        pass
    

    def open_web_page(self):
        return "What website do you want me to open?"


    def talk(self, parent_clue, child_type):
        import systems.answers_library.answers

        #engine = pyttsx3.init()
        #engine.setProperty('rate', 135)
        #voices = engine.getProperty('voices')
        #engine.setProperty('voice', voices[0].id)


        #engine.say(answers.answers[info])

        print("Getting the date for today ... ")
       
        ## check the type of data returned by 
        #engine.say(answers.answers[parent_clue])
         

        #engine.say(answers.answers[info])
        #engine.runAndWait()
        #engine.stop()

    
        
    def resolve_request(self, parent_clue, child_type, callback_function=None):
        import systems.date_resolutor as date_resolutor
        ## Now actually resolve the request .. 
        if child_type == 'web_request':
            # This is a request.. 
            feedback = self.request_web_page(parent_clue, child_type)
            self.ask_question_and_wait(feedback, parent_clue, child_type)

        if child_type == 'date_today':
            
            today = datetime.datetime.today()

            day_of_week = today.weekday()


            # check from the date_resolutor .. 

            day_today = date_resolutor.days_of_the_week[day_of_week]

            self.day_today = day_today

           
            self.talk(parent_clue, child_type)


        
    


    def ask_question_and_wait(self, request_question, parent_clue, child_type):
        engine = pyttsx3.init()
        engine.setProperty('rate', 135)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        engine.say(request_question)
        engine.runAndWait()



        


    
    def request_web_page(self, parent_clue, child_type):
        ##  ask for the web page to open.. 

        print(parent_clue)

        print(child_type)
        return "which website?"
        

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
                                #self.talk(clue)
                                pass
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
                        for word_key, word_value in word.items():
                            if word_key is not 'type':
                                for word_bit in word_value:
                                    if word_bit in information_data:
                                        ## check the clue ..
                                        self.resolve_request(clue, word['type'])
                        
                    
                  
                  

        
        



