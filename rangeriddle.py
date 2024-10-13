# 1. The Range Riddle
# Objective: The aim of this assignment is to deepen your understanding of Python's range() function.

# Task 1: Your Mood Today Write a program that prints off different moods 
# for each day of the week. Create a list of moods such as "Happy", "Sad", 
# "Energetic", and "Calm". Using the range() function, loop through every 
# day of the week and for each day, randomly select a mood from the list 
# and print it. Ensure that your program includes the use of the random module to select the mood.

# Example Outcome: An example output could be "On Wednesday, you were feeling happy." "On Thursday you were feeling sad."
import random

# set lists of moods and days of the week to variables
moods = ['happy', 'sad', 'energetic', 'anxious', 'ecstatic', 'motivated', 'lazy']
day = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# use random.shuffle to randomize the
random.shuffle(moods)

# set a for loop to iterate through the length of moods and then use those numbers as the indexing method to print them out.
# The indexes can be the same since the lists are the same length and since moods is rondomized now we will still acheive a random output
for mood in range(len(moods)):
    print(f"Today is {day[mood]}, and I feel {moods[mood]}!")
