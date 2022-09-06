alien_0 = {'color': 'green', 'point': 5}

print(alien_0['color'])
print(alien_0['point'])

point = alien_0['point']
print(f"You just earned {point} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0 = {'color': 'blue'}
print(f"alien color now is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"alien color now is {alien_0['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
x_increment = None
print(f"Originial x-position : {alien_0['x_position']}")
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] += x_increment
print(f"New x-position : {alien_0['x_position']}, this alien is {alien_0['speed']}")

print(f"\nThis original dictionary :")
print(alien_0)
del alien_0['speed']
print(f"This the new dictionary")
print(alien_0)






