from systems.core_sys import CoreSystem as Core
import pyttsx3
import speech_recognition as sr
import inspect, datetime, webbrowser


engine = pyttsx3.init()



class NervousSystem(Core):

    def __init__(self, bot_name = None):
        if(bot_name == None):
            self.switch_bot = True
            self.bot_name = 'Siri'
            self.mood = "I am not sad. Why are you interested?"
        
    
    def see(self):
        return "I can see"

    def listen(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)

            while self.switch_bot is True:
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
        import systems.answers_data as answers
        engine.setProperty('rate', 135)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

       
        ## check the type of data returned by 
        engine.say(answers.answers[parent_clue])
        engine.runAndWait()
        engine.stop()

    
        
    def resolve_request(self, parent_clue, child_type, word_bit, information_supplied, callback_function=None):
        import systems.date_resolutor as date_resolutor
        ## Now actually resolve the request .. 

        print("Word bit", word_bit)

        if child_type == 'about_bot':
            self.talk(parent_clue, child_type)

        if child_type == 'web_request':
            # This is a request.. 
            feedback = self.request_web_page(parent_clue, child_type)
            self.ask_question_and_wait(feedback, parent_clue, child_type)

        if child_type == 'go_to_website':
            print("Going to {}".format(information_supplied))
            ## check the information supplied .. 

            print(" ** Here are the bits: ", word_bit)

            if len(word_bit) > 3 and word_bit[3:] == 'ng':
                ## this a .com.ng site
                word_bit = list(word_bit)
                print(word_bit)
                word_bit = word_bit.insert(-3, '.')

                word_bit = "".join(word_bit[:])

                info = information_supplied[-5:]

                information_supplied = info + word_bit

                print(information_supplied)

            webbrowser.open("http://"+information_supplied)
            # -- Turn the not off at this point .. self.switch_bot = False





        if child_type == 'bot_age':
            self.talk(parent_clue, child_type)
    

        if child_type == 'mood_check':
            self.talk(parent_clue, child_type)

        if child_type == 'place_order':
            ## Start by placing an order .. 
            print("Placing the order ...")
            print("Here is the word bit : ", word_bit)
            print("Here is the information entered: ", information_supplied)
        



        if child_type == 'date_today':
            
            today = datetime.datetime.today()
            day_of_week = today.weekday()
            # check from the date_resolutor .. 

            day_today = date_resolutor.days_of_the_week[day_of_week]

            day_of_month = today.day

            this_year = today.year

            this_month = today.month

            month_today = date_resolutor.months_of_the_year[this_month]

            self.day_of_month = day_of_month

            self.day_today = day_today

            self.this_year = this_year

            self.this_month = month_today

            ## Create the overall date information 
            self.today_information = "Today is {}, {}, {}, {}".format(day_today, day_of_month, month_today, this_year)

           
            self.talk(parent_clue, child_type)
        
        if child_type == 'greetings':
            print("Asking about me ...")
            print(parent_clue)
            print(child_type)
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
                print("Here is the information: ", information)
                information_data = information.split()
                ## check the category of question ... 
                print("Information split: ",  information_data)
                size_of_split = len(information_data)
                if size_of_split == 1:
                    try:
                        information_data = information_data[0].split(".")
                    except:
                        print("This is not a website")
                else:
                    ## check that one of the items contains a . indicating web
                    ## .. reference .. 
                    joined_split_items = ''.join(information_data[:])
                    
                    print("Complete split items: ", joined_split_items)

                    if "." in joined_split_items:
                        ## this is a website ... 
                        joined_split_items = joined_split_items.strip()
                        brief_info_list = [joined_split_items]

                        information = joined_split_items

                        information_data = brief_info_list[0].split(".")
                   



                    ##pass this complete split to this rectify function

                
                print(information_data)
                from systems.questions_library import questions
                for clue, words in questions.clues.items():
                    for word in words:
                        for word_key, word_value in word.items():
                            if word_key is not 'type':
                                for word_bit in word_value:
                                    if word_bit in information_data:
                                        ## check the clue ..
                                        self.resolve_request(clue, word['type'], word_bit, information)
                        
                    
                  
                  

        
        



