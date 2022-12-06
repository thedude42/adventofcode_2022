import sys
import re

instruction_re = re.compile(r'move (\d+) from (\d+) to (\d+)')

class CrateStack:

    def __init__(self, stack_list) -> None:
        self.__stack = stack_list
        #print(f"creating CrateStack with list {stack_list}")
    
    @property
    def top(self):
        return self.__stack[-1]
    
    def push(self, crate: str):
        self.__stack.append(crate)
    
    def pop(self) -> str:
        return self.__stack.pop()
    
    def __repr__(self) -> str:
        crate_strings = [ f"[{c}]" for c in self.__stack ]
        return ' '.join(crate_strings)

class CargoCrane:

    def __init__(self, crates: list[CrateStack]) -> None:
        self.__crates = crates
        assert type(self.__crates) == list
    
    def process_instruction(self, instruction):
        m = instruction_re.match(instruction)
        if not m:
            raise Exception(f"instruction is not the expected form: '{instruction}'")
        to_move = []
        number_to_move = int(m.group(1))
        from_stack = int(m.group(2)) - 1
        to_stack = int(m.group(3)) - 1
        for n in range(0,number_to_move):
            to_move.append(self.__crates[from_stack].pop())
        for c in to_move:
            self.__crates[to_stack].push(c)
    
    def improved_process_instruction(self, instruction):
        m = instruction_re.match(instruction)
        if not m:
            raise Exception(f"instruction is not the expected form: '{instruction}'")
        to_move = []
        number_to_move = int(m.group(1))
        from_stack = int(m.group(2)) - 1
        to_stack = int(m.group(3)) - 1
        for n in range(0,number_to_move):
            to_move.append(self.__crates[from_stack].pop())
        for c in to_move[::-1]:
            self.__crates[to_stack].push(c)
    
    def get_top_crates(self) -> list[str]:
        return [ c.top for c in self.__crates ]
    
    def __repr__(self) -> str:
        stacks = []
        for i, stack in enumerate(self.__crates):
            stacks.append(f"{i+1} {stack}")
        return "\n".join(stacks)

def part2(crane: CargoCrane, instructions: list[str]):
    for instruction in instructions:
        crane.improved_process_instruction(instruction)
    print(''.join(crane.get_top_crates()))


def part1(crane: CargoCrane, instructions: list[str]):
    for instruction in instructions:
        crane.process_instruction(instruction)
    print(''.join(crane.get_top_crates()))
    

def get_crate_stacks(input_list, stacks) -> CrateStack:
    crate_stack_lists = [ [] for _ in range(0,stacks) ]
    for line in input_list:
        # parse the input list we generated from the puzzle input "header":
        # 1. we are given the number of 'stacks'
        # 2. we know the layout of the input
        # 3. therefore calculating the position of a stack is always the same: 
        #    either the position in the line is blank or it is a "crate" 
        for stack, position in enumerate(range(1, len(line), 4)):
            #print(f"examining input line {line} at index {stack} position {position}")
            if line[position] != ' ':
                crate_stack_lists[stack].append(line[position])
        # now the lists inside 'crate_stack_lists' represents each stack, but in reverse order,
        # that is, the first item in the list is the "top" of the stack, so we need to fix that...
    return [ CrateStack(l[::-1]) for l in crate_stack_lists ]

def main():
    lines = [ line for line in open(sys.argv[1], 'r') ]
    start_state = []
    instructions = []
    start_lines = 0
    start_parsed = False
    stacks = 0
    crane = None
    for line in lines:
        if not start_parsed:
            if line[1] == '1':
                stacks = int(line[-3])
                start_parsed = True
            else:
                start_lines += 1
                start_state.append(line)
                #print(f"appended line:\n\t{line}")
        else:
            if not line.strip() == '':
                instructions.append(line)
    part1(CargoCrane(get_crate_stacks(start_state, stacks)), instructions)
    part2(CargoCrane(get_crate_stacks(start_state, stacks)), instructions)


if __name__ == '__main__':
    main()