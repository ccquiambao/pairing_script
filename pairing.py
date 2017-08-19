import itertools
import numpy as np
import random
import pickle
import sys

def make_pairs(student_lst, pair_dict):
    low_score = sum(pair_dict.itervalues()) + 1000
    final_lst = None
    final_dict = None

    for _ in xrange(1000):
        random.shuffle(student_lst)
        pair_gen = itertools.izip(student_lst[:-3:2], student_lst[1:-3:2])
        pairs = [tuple(sorted([student1, student2])) for (student1, student2) in pair_gen]

        remains = itertools.combinations(student_lst[-3:], 2)
        for student1, student2 in remains:
            pair = sorted([student1, student2])
            pair = tuple(pair)
            pairs.append(pair)

        temp_dict = pair_dict.copy()
        for pair in pairs:
            temp_dict[pair] += 1

        cur_score = sum(temp_dict.itervalues())
        if cur_score < low_score:
            final_lst = student_lst[:]
            final_dict = temp_dict.copy()

    if final_lst and final_dict:
        return final_lst, final_dict

    else:
        return student_lst, temp_dict


def print_pairs(student_lst):
    for ind, student in enumerate(student_lst[:-3], 1):
        print '{:12}'.format(student.strip()),
        if not ind % 2:
            print

    for student in student_lst[-3:]:
        print '{:12}'.format(student),


if __name__ == '__main__':

    with open('students.txt', 'r') as f:
        students = [student.strip() for student in f]

    with open('pair_dict.pkl', 'r') as f:
        pair_dict = pickle.load(f)

    pairs, updated_dict = make_pairs(students, pair_dict)
    print_pairs(pairs)
    print sum(updated_dict.itervalues())

    confirm = raw_input('List okay?')
    if confirm != 'y':
        sys.exit()
    with open('pair_dict.pkl', 'w') as f:
        pickle.dump(updated_dict, f)
