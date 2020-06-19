'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2:
        return 0
    return helper(word, 0, len(word)-2)

def helper(word, curr_idx, end):
    if curr_idx == end:
        if word[curr_idx:] == "th":
            return 1
        else:
            return 0
    if word[curr_idx:curr_idx+2] == "th":
        return 1 + helper(word, curr_idx+1, end)
    else:
        return helper(word, curr_idx+1, end)
