#  converts distance in km to miles
# takes user name and capitalizes the name 

name = input('Enter your name:')
distance_km = input('Enter distance in Km:')
# convert the distance_km from string to float first
distance_mi = float(distance_km)/1.609
print(f'Hi {name.capitalize()}! {distance_km} km is {round(distance_mi,2)} miles.')