from itertools import permutations

def permut_numb(input_str):
    perms = permutations(input_str)

    for perm in perms:
        print("".join(perm))

user_input = input("String: ")

print("permut in string:")
