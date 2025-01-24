# This problem was asked by Quora.

# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

# As another example, given the string "google", you should return "elgoogle".


def find_min_inserts_palindrome(s):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i > j:
            return (0, "")
        if i == j:
            return (0, s[i])
        if s[i] == s[j]:
            inserts, sub_pal = dp(i + 1, j - 1)
            res = (inserts, s[i] + sub_pal + s[j])
        else:
            # Option 1: add s[j] to both ends
            inserts1, sub_pal1 = dp(i, j - 1)
            option1 = (inserts1 + 1, s[j] + sub_pal1 + s[j])
            # Option 2: add s[i] to both ends
            inserts2, sub_pal2 = dp(i + 1, j)
            option2 = (inserts2 + 1, s[i] + sub_pal2 + s[i])
            # Choose the better option
            if option1[0] < option2[0]:
                res = option1
            elif option2[0] < option1[0]:
                res = option2
            else:
                res = option1 if option1[1] < option2[1] else option2
        memo[(i, j)] = res
        return res

    _, result = dp(0, len(s) - 1)
    return result


print(find_min_inserts_palindrome("google"))