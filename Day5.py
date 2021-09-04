# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.

# def city_country(city, country):
#     f = f"{city.title()},{country.title()}"
#     return f
#
#
# formatedoutput = city_country('Islamabad', 'Pakistan')
# print(formatedoutput)


# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
def make_album(artist_name,album_title,t_songs):
    d = {'artist_name':artist_name,'album_title':album_title, 'total_songs': t_songs}
    return d


m=make_album('Salman','freewela',33)
print(m)

while True:
    print("Enter 'q' at any time to quit")
    name=input('Enter your name :')
    if name=='q':
        break
    album_name=input('Enter your album name:')
    if name=='q':
        break
    t_songs=input('Enter no of songs you have in album:')
    if name=='q':
        break
    c = make_album(name, album_name, t_songs)
    print(c)








