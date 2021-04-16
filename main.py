# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def merge(data):
    i = 0
    j = 2
    while i < len(data) - 2:
        for k in range(j, len(data)):
            if k % 2 == 0:
                if data[j] <= data[i + 1] and data[j + 1] <= data[i + 1]:
                    data.pop(j)
                    data.pop(j)
                elif data[j] <= data[i + 1] and data[j + 1] >= data[i + 1]:
                    data.pop(i + 1)
                    data.pop(j - 1)
                elif data[j] <= data[i] and data[j + 1] >= data[i + 1]:
                    data.pop(i)
                    data.pop(i)
                elif data[j] <= data[i] and data[j + 1] <= data[i + 1]:
                    data.pop(i)
                    data.pop(j)
        i += 2
        j += 2
    return data

def appearance(intervals):
    data = intervals
    answer = 0
    data['pupil'] = merge(data['pupil'])
    data['tutor'] = merge(data['tutor'])

    for i in range (0, len(data['pupil'])):
        if i%2 == 0:
            if data['pupil'][i] <= data['lesson'][1] and data['pupil'][i+1] >= data['lesson'][0]:
                if data['lesson'][0] > data['pupil'][i]:
                    start = data['lesson'][0]
                else:
                    start = data['pupil'][i]
                if data['lesson'][1] < data['pupil'][i+1]:
                    end = data['lesson'][1]
                else:
                    end = data['pupil'][i+1]
                for j in range (0, len(data['tutor'])):
                    if j%2 == 0:
                        if data['tutor'][j] <= end and data['tutor'][j+1] >= start:
                            if data['tutor'][j] >= start and data['tutor'][j+1] <= end:
                                answer += data['tutor'][j+1] - data['tutor'][j]
                            elif data['tutor'][j] <= start and data['tutor'][j+1] <= end:
                                answer += data['tutor'][j+1] - start
                            elif data['tutor'][j] >= start and data['tutor'][j+1] >= end:
                                answer += end - data['tutor'][j]
                            elif data['tutor'][j] <= start and data['tutor'][j+1] >= end:
                                answer += end - start
    return answer






tests = [
   {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
    'answer': 3117
    },
   {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
   {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
