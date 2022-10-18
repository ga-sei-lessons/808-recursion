# recursive function is one that calls itself
def navel_gazer():
    # do some logic
    print('hmmm....')
    # invokes itself
    navel_gazer()

# navel_gazer()

# elements of a recursive function
# 1. must have a 'base case' -- condition that terminates the recursion
# 2. recursive case -- condition in which the function invokes iteself
# 3. must change its state to move closer to the base case each time the function recurses
# for (state;     base case;    drive state towards base case )
# for (let i = 0; i < arr.len; i++)

# def print_loop(end_num, current_num = 0):
#     # loop up to end_num and print out each number
#     # iterative 
#     # for i in range(0, end_num + 1):
#     #     print('current number:', i)
#     # recursive logic
#     print('current number:', current_num)
#     # base case -- stops the recursion
#     if current_num == end_num:
#         return
#     # recursive case
#     print_loop(end_num, current_num + 1) # drives state towards base case


# print_loop(20)

# manage state by modifying input value given
def print_loop_two(end_num):
    # base case -- end_num is less than zero
    if end_num < 0:
        return
    
    # function logic
    print('current number is:', end_num)

    # recursive case that drives state towards the base case
    print_loop_two(end_num - 1)

# setting a higher recursion limit
import sys
sys.setrecursionlimit(5000)
# print_loop_two(4994)

# accept a value n and compute the sum of numbers from 0 to n

def sum_to(n):
    # base case
    if n <= 0:
        return 0
    # recursive case
    print(f'n is currently: {n}')
    return n + sum_to(n - 1)

print(sum_to(100))