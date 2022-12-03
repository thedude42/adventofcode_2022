import sys
from collections import defaultdict
from functools import reduce

class Rucksack:

    def __init__(self, contents: str) -> None:
        self._set_compartments(contents)
    
    def _set_compartments(self, contents: str) -> None:
        self.__compartment1 = defaultdict(int)
        self.__compartment2 = defaultdict(int)
        for c in contents[:int(len(contents)/2)]:
            self.__compartment1[c] += 1
        for c in contents[int(len(contents)/2):]:
            self.__compartment2[c] += 1
    
    @property
    def item_types(self) -> set:
        return set(self.__compartment1.keys()).union(set(self.__compartment2.keys()))
    
    def get_common_item_between_compartment(self) -> set:
        c1 = set(self.__compartment1.keys())
        c2 = set(self.__compartment2.keys())
        return c1.intersection(c2).pop()

def get_item_priority(c):
    if str.islower(c):
        return ord(c) - 96
    elif str.isupper(c):
        return ord(c) - 38
    else:
        raise Exception(f"wtf is {c}?")

def find_badge(group_list):
    return reduce(lambda a, b: a.intersection(b), [rucksack.item_types for rucksack in group_list]).pop()

def part2(input):
    rucksacks = [ Rucksack(line) for line in input ]
    assert len(rucksacks) % 3 == 0
    groups = []
    for x in range(0,len(rucksacks), 3):
        groups.append(rucksacks[x:x+3])
    print(f"part2: {sum([ get_item_priority(badge) for badge in [ find_badge(g) for g in groups ]])}")
    

def part1(input):
    rucksacks = [ Rucksack(line) for line in input ]
    print(f"part1: {sum([get_item_priority(r.get_common_item_between_compartment()) for r in rucksacks])}")

def main():
    rucksacks = [ line.strip() for line in open(sys.argv[1], 'r') ]
    part1(rucksacks)
    part2(rucksacks)

if __name__ == '__main__':
     main()