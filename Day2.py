a={'a':4, 'b':33}
print_vlue=a.get('a','no such value is present')
print(print_vlue)


person={'name':'Waqas' , 'age':22 ,'city':'Okara Cantt'}
print('Data of Friend\n')
print(person['name'])
print(person['age'])
print(person['city'])
for key, value in person.items():
    print(f"{key} : {value}")
for k,m in person.items():
    print(f"The {k} runs through {m}")


# f=[]
# for f in range(30):
#     n = {'sa':'s', 'wq':'this is not fair'}
#     f.append(n)
# print(f)
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens)