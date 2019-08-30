from collections import namedtuple
import inspect

User = namedtuple("User", "firstname middlename lastname user_id")

user = User("Olu", "Ade", "Ade", 123)

inspected = inspect.getmembers(User)

check = [a for a in inspected if not(a[0].startswith('__') or a[0].endswith('__') or a[0].startswith('_'))]



print(check)