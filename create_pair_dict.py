import itertools
import pickle


with open('students.txt', 'r') as f:
    students = [student.strip() for student in f]

pair_gen = itertools.combinations(students, 2)
pairs = [sorted([student1, student2]) for (student1, student2) in pair_gen]
pairs = {tuple(pair):0 for pair in pairs}

for pair in pairs.iteritems():
    print pair

with open('pair_dict.pkl', 'w') as f:
    pickle.dump(pairs, f)
