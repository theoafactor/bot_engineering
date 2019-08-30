from systems import nervous_sys 
import time


## instantiate 
## This process should power up important things about this Artificial inteeligence .. 

nervous = nervous_sys.NervousSystem()


#Name of Bot 
bot_name = nervous.bot_name

##See 
seeing = nervous.see()



### Functions 
def askQuestion(question):
    time.sleep(3)
    nervous.hear(question)


def listen():
    nervous.listen()



