"""
# recursive solution
def is_interleave_recursive(s, x, y, x_orig, y_orig):

    # base case match
    if len(s) == 1 and (x[0] == s[0] or y[0] == s[0]):
        return True
    # no match
    if x[0] != s[0] and y[0] != s[0]:
        return False
    # if first char of s is matched recursively call is_interleave with substring of s and x
    if x[0] == s[0]:
        # if x is only one char, reset it to the original and set full_match_x to True
        if len(x) == 1:
            x += x_orig
        return is_interleave_recursive(s[1:], x[1:], y, x_orig, y_orig)
    # if first char of s is matched recursively call is_interleave with substring of s and y
    if y[0] == s[0]:
        # if y is only one char, reset it to the original and set full_match_y to True
        if len(y) == 1:
            y += y_orig
        return is_interleave_recursive(s[1:], x, y[1:], x_orig, y_orig)
"""


def is_interleave(s, x, y):
    # too short to determine
    if len(x) + len(y) > len(s):
        return False
    # create list of lists representing a grid of size len(s) X len(s)
    path = [[False] * len(s) for i in range(len(s))]

    for i in range(len(s)):
        for j in range(len(s)):

            # check the first element seperately
            if i == 0 and j == 0:
                if s[0] == x[0] or s[0] == y[0]:
                    path[0][0] = True
                    continue

            # ensure we dont go out of bounds
            if i + j > len(s)-1:
                continue

            # is the cell above true and does s match x
            if i > 0 and path[i - 1][j] and s[i + j] == x[i % len(x)]:
                path[i][j] = True
                # return true if we've matched all of s
                if i + j == len(s) - 1:
                    return True
            # is the cell to the left true and does s match x
            elif j > 0:
                if path[i][j - 1] and s[i + j] == y[j % len(y)]:
                    path[i][j] = True
                    # return true if we've matched all of s
                    if i + j == len(s) - 1:
                        return True
            else:
                path[i][j] = False
    return False


if __name__ == "__main__":

    path = is_interleave('100010101', '101', '0')
    print(path)