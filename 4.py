from collections import namedtuple
"""           ---       s                                  m                       ---  
 

color -->          gr | y | r                       gr | y | r 

Gucci -            ggrs | gys | grs           
Fendi -                     
Versace -                         

"""


Designer = namedtuple("Designer", "name color size")

gucci = Designer("Gucci", ("green", "yellow", "red"),("s", "m", "l"))
fendi = Designer("Fendi", ("green", "yellow", "red"),("s", "m", "l"))
versace = Designer("Versace", ("green", "yellow", "red"),("s", "m", "l"))


print(gucci)