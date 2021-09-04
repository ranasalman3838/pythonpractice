p1={'name':'salman','age':'22'}
p2={'name':'Ehtsham','age':'22'}
p3={'name':'Habib','age':'22','languges':['urdu','ragrii','english']}
people=[p1,p2,p3]
for p in people:
    for name,val  in p.items():
        print(f"{name} : {val} ")

pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
print(f"you ordered a {pizza['crust']} - crust pizza with ")
for toppings in pizza['toppings']:
    print("\t"+toppings)


favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name,languages in favorite_languages.items():
    print(f"{name} favourite languages are :")
    for language in languages:
        print(f"\t {language}")


users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
for username,userinfo in users.items():
    print(f"Username: {username}")
    fullname=f"{userinfo['first']} {userinfo['last']}"
    location=userinfo['location']
    print(f"Full Name: {fullname.title()}")
    print(f"Location: {location}")





