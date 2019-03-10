import random

def rand5():
    rand = random.randint(1, 5)
    return rand

def rand7():

    vals = [
        [ 1, 2, 3, 4, 5 ],
        [ 6, 7, 1, 2, 3 ],
        [ 4, 5, 6, 7, 1 ],
        [ 2, 3, 4, 5, 6 ],
        [ 7, 0, 0, 0, 0 ]
    ]

    result = 0
    while (result == 0):
        i = rand5()
        j = rand5()
        result = vals[i-1][j-1]

    return result


if __name__ == '__main__':

    for i in range(100):
        print(rand7())