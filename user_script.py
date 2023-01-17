"""
Complete the script.
"""
# DOMAIN LISTED: PUZZLES
#Code for Task 4 Project included below. I have also included my practice code.
#This coding will measure three puzzle box sizes three siblings will randomly grab from the shelf.

"""Find three tpuzzle box sizes values."""
print()
print("REQUEST ALL PUZZLE BOX SIZES")
print("----------------------------")
box1 = float(input('Enter first puzzle box size: '))
print(box1)
box2 = float(input('Enter second puzzle box size: '))
print(box2)
box3 = float(input('Enter third puzzle box size: '))
print(box3)
print()
print("SUM OF ALL PUZZLE BOX SIZES")
print("---------------------------")
value_sum = box1+box2+box3
print(value_sum)
print()
print("AVERAGE OF ALL PUZZLE BOX SIZES")
print("-------------------------------")
value_average=value_sum/3
print(round(value_average,2))
print()
print("PRODUCT OF ALL PUZZLE BOX SIZES")
print("-------------------------------")
value_product = box1*box2*box3
print(value_product)
print()
print("SMALLEST OF ALL PUZZLE BOX SIZES")
print("--------------------------------")
minimum=min(box1,box2,box3)
print('Minimum value is', minimum)
print()
print("LARGEST OF ALL PUZZLE BOX SIZES")
print("-------------------------------")
maximum=max(box1,box2,box3)
print('Maximum value is', maximum)
print()
print("RANGE OF ALL PUZZLE BOX SIZES")
print("-----------------------------")
print('Range: ',minimum,'-',maximum)
print()
print("WHAT SIZE WAS THE SECOND PUZZLE BOX CHOSEN?")
print("------------------------------------------")
print('Small  = 100 and less pieces')
print('Medium = 101 to 500 pieces')
print('Large  = 501 and greater pieces')
print()
print("Second value entered: ",box2)
print()
if box2 < 101:
    print("The second puzzle box chosen is a small box.")
if box2 >= 101 and box2 <=500:
    print("The second puzzle box chosen is a medium box.")
if box2 > 500:
    print("The second puzzle box chosen is a large box.")
print()
print()