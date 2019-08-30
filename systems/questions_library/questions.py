## clue is 'name' or 'your'
#keys must correspond with the keys in the answers dictionaries module 
clues = {
    'greetings': [
        
       {
            'type': 'greetings',
            'clues': ['how are you','how']
       },

       {
           'type': 'evening_greetings',
           'clues': ['good evening', 'evening']
       }
    ],

    'open_web': [

       {
        'type': 'opens_url',
        'clues': ['go to this website', 'website']
       }
    ],

    'web_search': [

        {
        'type': 'web_request',
        'clues': ['go to this website', 'website']
        }
    ],

    'bio': [

        {
            'type': 'about_bot',
            'clues': ['what is your name', 'your name?', 'name', 'name?']
        },

        {
            'type': 'bot_age',
            'clues': ['how old are you', 'what is your age', 'what is your age?', 'your age', 'age?', 'you?', 'old?', 'how old you?']
        
        }
    ],

    'mood': [
        {
            'type': 'mood_check',
            'clues': ['are you happy', 'are you happy?', 'happy', 'happy?', 'are you sad?', 'why are you happy?']
        }
    ],

    'date': [
        {
            'type': "date_today",
            "clues": ["what is today", "today's date", "date", "today"]
        }
    ]

    
}


 

