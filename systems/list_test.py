users = ['Olu', 'Ade', 'Segun', 'Seyi']

user_var = ''

user_var2 = ''

counter = 0

for user in users:
    if counter < 2:
        user_var = user_var.strip() + ' ' + user 

        counter = counter + 1
    else:
        user_var2 = user_var2.strip() + ' ' + user 
        counter = counter + 1


print(user_var)
print(user_var2)

total_list = []

total_list.append(user_var)
total_list.append(user_var2)

print(total_list)