# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

# input
# customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
# n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.

# A:
# set up array of elements size = # of tills
# iterate over customers, add each value to the smallest element value
# get max of the values in the array

def queue_time(customers, n):
    tills = [0] * n

    for customer in customers:
        tills[tills.index(min(tills))] += customer

    return max(tills)

print(queue_time([10,2,3,3], 2) == 10)
print(queue_time([2,3,10], 2) == 12)
