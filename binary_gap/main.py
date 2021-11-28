
def solution(N):
    # write your code in Python 3.6

    string = str(bin(N))[2:]

    curr_max = 0
    curr_gap = 0

    for c in string:
        if (c == '1'):
            if (curr_gap > curr_max):
                curr_max = curr_gap

            curr_gap = 0

        if (c == '0'):
            curr_gap += 1

        

    return curr_max

print(solution(1041))
