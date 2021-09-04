# # User input and While Loops
# m=input("Enter Your Name buddy:")
# print(f"Hello {m}")
#
# a=9
# while a!=20:
#     print(a)
#     a=a+1
#
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# filling a dictionary with user input
responses={}
isactive = True
while isactive:
    name=input('Enter Your name :')
    response=input('where you like to go :')
    responses[name] = response
    repeat=input('Add another entry?(yes or no)')
    if repeat == 'no':
        isactive = False
print('\n Poll Results')
for name , response in responses.items():
    print(f"{name} would like to go to {response}")