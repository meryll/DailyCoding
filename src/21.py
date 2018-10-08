'''
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''

def overlap(a, b):

    return not a[1] < b[0]

def find(intervals):
    used = []
    count = 1
    used.append(intervals[0])

    for i in range(1, len(intervals)):
        if overlap(intervals[i-1], intervals[i]):
            count+=1

    return count



if __name__ == '__main__':

    intervals = [(30, 75), (0, 50), (60, 150), (130, 199)]
    print(find(intervals))
