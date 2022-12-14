'''
Practice: Which Prize
Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points.

Points	Prize
1 - 50	wooden rabbit
51 - 150	no prize
151 - 180	wafer-thin mint
181 - 200	penguin
All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.

In your if statement, assign the result variable to a string holding the appropriate message based on the value of points. If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Oh dear, no prize this time."

Note: Feel free to test run your code with other inputs, but when you submit your answer, only use the original input of points = 174. You can hide your other inputs by commenting them out.
'''
'''points = 174  # use this input to make your submission'''
points = int(input())

# # write your if statement here
# 1 - 50	wooden rabbit
# 51 - 150	no prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin
w_rab = range(1, 50)
n_pr = range(51, 150)
w_t_m = range(151, 180)
peng = range(181, 200)

if points in w_rab or points == 50:
    result = "Congratulations! You won a wooden rabbit!"
    print(result)
elif points in n_pr or points == 150:
    result = "Oh dear, no prize this time."
    print(result)
elif points in w_t_m or points == 180:
    result = "Congratulations! You won a wafer-thin mint!"
    print(result)
elif points in peng or points == 200:
    result = "Congratulations! You won a penguin!"
    print(result)
else:
    result = "INVALID POINTS"
    print(result)


#CORRECTION
'''
points = 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)
'''