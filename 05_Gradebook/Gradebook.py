# Project 005: GRADEBOOK

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Create lists
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

# Create 2d list
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
print(gradebook,'\n')

# Append new list item
gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])
print(gradebook,'\n')

# Modify gradebook
gradebook[-1][-1] +=5
print(gradebook,'\n')

# Removing item list
gradebook[2].remove(85)
gradebook[2].append("Pass")
# gradebook[2][1] = "Pass"    # alternative method
print(gradebook,'\n')

# Retrieving last_semester_gradebook list
print(last_semester_gradebook,'\n')

# Combine lists
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)

