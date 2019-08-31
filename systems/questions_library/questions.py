## clue is 'name' or 'your'
#keys must correspond with the keys in the answers dictionaries module 
clues = {
    'greetings': [
        
       {
           'type': 'evening_greetings',
           'clues': ['good evening', 'evening']
       },
          
        {
            'type': 'greetings',
            'clues': ['how are you','how']
       }
    ],

    'open_web': [

        {
        'type': 'go_to_website',
        'clues': ['wwwdot', 'www', 'www.', 'dotcom', '.com', 'com', 
                    'org', '.org', '.ng','dotorgdotng', 'dotorg.ng',
                    'com.ng', 'dot', '.',
                  '.orgdotng', 'orgdotng',  '.com.ng', '.org.ng', 'ng', 'orgng']
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
        }
    ],

    'age': [
         {
            'type': 'bot_age',
            'clues': ['how old are you', 'what is your age', 'what is your age?', 'your age', 'age?', 'you?', 'old?', 'how old you?']
        
        }
    ],
    
    'place_order': [

            {
                'type': 'place_order',
                'clues': ['place this order']
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


 

