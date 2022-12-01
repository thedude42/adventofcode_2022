import sys


class ElfFoodInventory:

    def __init__(self, item_calories: list) -> None:
        self.__item_calories = item_calories
    
    @property
    def calories_list(self) -> list:
        return self.__item_calories
    
    @property
    def total_calories(self) -> int:
        return sum(self.__item_calories)


def get_elf_dict(input_data: list) -> dict:
    elves = {}
    next_elf_data = []
    elf_idx = 1
    for line in input_data:
        if line == '':
            elves[elf_idx] = ElfFoodInventory(next_elf_data)
            next_elf_data = []
            elf_idx += 1
        else:
            next_elf_data.append(int(line))
    else:
        if len(next_elf_data) > 0:
            elves[elf_idx] = ElfFoodInventory(next_elf_data)
    return elves

def part1(input_data) -> int:
    elf_dict = get_elf_dict(input_data)
    return max([elf.total_calories for elf in elf_dict.values()])

def part2(input_data) -> int:
    elf_dict = get_elf_dict(input_data)
    all_total_calories = sorted([elf.total_calories for elf in elf_dict.values()], reverse=True)
    return sum(all_total_calories[0:3])

def main():
    input_data = [ x.strip() for x in open(sys.argv[1], 'r')]
    print(part1(input_data))
    print(part2(input_data))

if __name__ == '__main__':
    main()