import turtle 
sides = int(input("number of sides"))
while (sides < 3) or (sides > 8) or (sides == 7): 
    sides = input("number of sides") 
for count in range(1, sides+1): 
    turtle.forward(100) 
    turtle.right(360/sides) 
