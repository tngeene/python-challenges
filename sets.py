blue_eyes = {'Olivia', 'Jack', 'Lily', 'Josh'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Luke'}
o_blood = {'Mia', 'Josh', 'Lily', 'Olivia'}
b_blood = {'Jack', 'Amelia'}
a_blood = {'Harry'}
ab_blood = {'Mike'}

# people with both blue eyes and blond hair
blond_blue = blue_eyes.union(blond_hair)
print(f'People in the sets of blue eyes and blond hair are {blond_blue}')

# people with only blue eyes and blond hair
blue_blond = blue_eyes.intersection(blond_hair)
print(f'people with blue eyes and blond hair are {blue_blond}')

# people with only blue eyes but no blond hair
blue_not_blond = blue_eyes.difference(blond_hair)
print(f'people with blue eyes but no blond hair are {blue_not_blond}')