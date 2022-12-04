import sys

def get_interval_sets(pair):
    start, end = [ int(i) for i in pair[0].split('-') ]
    s1 = set([ i for i in range(start,end+1)])
    #print(s1)
    start, end = [ int(i) for i in pair[1].split('-') ]
    s2 = set([i for i in range(start,end+1)])
    #print(s2)
    return s1, s2

def day1(interval_pairs) -> tuple:
    contained_intervals = 0
    for pair in interval_pairs:
        s1, s2 = get_interval_sets(pair)
        if s1.intersection(s2) == s1 or s1.intersection(s2) == s2:
            contained_intervals += 1
    print(f"{contained_intervals} conained intervals")


def day2(interval_pairs):
    intersecting_intervals = 0
    for pair in interval_pairs:
        s1, s2 = get_interval_sets(pair)
        if len(s1.intersection(s2)) > 0:
            intersecting_intervals += 1
    print(f"{intersecting_intervals} inervals intersect")



def main():
    interval_pairs = [ s.strip().split(',') for s in open(sys.argv[1], 'r') ]
    day1(interval_pairs)
    day2(interval_pairs)

if __name__ == '__main__':
    main()