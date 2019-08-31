from systems.nervous_sys import NervousSystem

nervous_system = NervousSystem()


answers = {
    'greetings': 'I am fine, thank you',
    'bio': "My name is "+nervous_system.bot_name,
    'age': 'I am one year old',
    'mood': nervous_system.mood,
    'open_web': nervous_system.open_web_page,
    'web_search': 'Opening the page',
    'date': nervous_system.day_today
}
