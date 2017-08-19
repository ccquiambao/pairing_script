import sys
import pickle
import itertools

if len(sys.argv) != 2:
    print 'Bai~'
    print sys.argv
    sys.exit()

with open(sys.argv[1]) as f:
    pairs = []
    for line in f:
        pair = sorted(line.split())
        pairs.append(pair)

with open('pair_dict.pkl', 'r') as f:
    pair_dict = pickle.load(f)

for pair in pairs:
    if len(pair) == 2:
        pair = tuple(pair)
        pair_dict[pair] += 1

    else:
        for pair in itertools.combinations(pair, 2):
            pair = sorted(list(pair))
            pair = tuple(pair)
            pair_dict[pair] += 1

print sum(pair_dict.itervalues())

with open('pair_dict.pkl', 'w') as f:
    pickle.dump(pair_dict, f)
