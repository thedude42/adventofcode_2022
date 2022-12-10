import sys

class RopeState:

    def __init__(self, num_knots: int=2) -> None:
        self.__knots = [(0,0) for _ in range(num_knots)]
        self.__tail_visits = set()
        self.__tail_visits.add(self.__knots[-1])
        self.__num_instructions_processed = 0
    
    @property
    def tail_visited(self) -> int:
        return len(self.__tail_visits)
    
    @property
    def H(self) -> tuple:
        return self.__knots[0]
    
    @H.setter
    def H(self, new_coords: tuple):
        assert type(new_coords) == tuple and \
                len(new_coords) == 2 and \
                type(new_coords[0]) == int and \
                type(new_coords[1]) == int
        self.__knots[0] = new_coords
    
    def do_instruction(self, instructon: str):
        direction, distance = instructon.split()
        self.__num_instructions_processed += 1
        if direction == 'R':
            self._do_R(int(distance))
        elif direction == 'U':
            self._do_U(int(distance))
        elif direction == 'L':
            self._do_L(int(distance))
        elif direction == 'D':
            self._do_D(int(distance))
        else:
            raise Exception(f"Instruction not right? '{instructon}'")
        
    
    def _resolve_tail(self):
        adjacent_knots_indexes = [
            t for t in zip(
                [i for i in range(0,len(self.__knots) - 1)], [j for j in range(1,len(self.__knots))]
            )
        ]
        #print(f"after H move:{self.__knots}")
        for front, back in adjacent_knots_indexes:
            #print(f"front:{front} back:{back}")
            x_difference = self.__knots[front][0] - self.__knots[back][0]
            y_difference = self.__knots[front][1] - self.__knots[back][1]
            if x_difference == 2:
                if y_difference in [1,2]:
                    self.__knots[back] = (self.__knots[back][0] + 1, self.__knots[back][1] + 1)
                elif y_difference  in [-1, -2]:
                    self.__knots[back] = (self.__knots[back][0] + 1, self.__knots[back][1] - 1)
                elif y_difference == 0:
                    self.__knots[back] = (self.__knots[back][0] + 1, self.__knots[back][1])
                elif y_difference < -2 or y_difference > 2:
                    raise Exception(f"Y dimension moved more than -2 cells away on instruction {self.__num_instructions_processed} with front={front} back={back}?")
            elif y_difference == 2:
                if x_difference in [1,2]:
                    self.__knots[back] = (self.__knots[back][0] + 1, self.__knots[back][1] + 1)
                elif x_difference  in [-1, -2]:
                    self.__knots[back] = (self.__knots[back][0] - 1, self.__knots[back][1] + 1)
                elif x_difference == 0:
                    self.__knots[back] = (self.__knots[back][0], self.__knots[back][1] + 1)
                elif x_difference < -2 or y_difference < -2:
                    raise Exception(f"X dimension moved more than -2 cells away on instruction {self.__num_instructions_processed} with front={front} back={back}?")
            elif y_difference == -2:
                if x_difference  in [1,2]:
                    self.__knots[back] = (self.__knots[back][0] + 1, self.__knots[back][1] - 1)
                elif x_difference  in [-1, -2]:
                    self.__knots[back] = (self.__knots[back][0] - 1, self.__knots[back][1] - 1)
                elif x_difference == 0:
                    self.__knots[back] = (self.__knots[back][0], self.__knots[back][1] - 1)
                elif x_difference < -2 or y_difference < -2:
                     raise Exception(f"X dimension moved more than -2 cells away on instruction {self.__num_instructions_processed} with front={front} back={back}?")
            elif x_difference == -2:
                if y_difference  in [1,2]:
                    self.__knots[back] = (self.__knots[back][0] - 1, self.__knots[back][1] + 1)
                elif y_difference in [-1, -2]:
                    self.__knots[back] = (self.__knots[back][0] - 1, self.__knots[back][1] - 1)
                elif y_difference == 0:
                    self.__knots[back] = (self.__knots[back][0] - 1, self.__knots[back][1])
                elif y_difference < -2 or y_difference > 2:
                    raise Exception(f"Y dimension moved more than -2 cells away on instruction {self.__num_instructions_processed} with front={front} back={back}?")
            elif x_difference > 2 or x_difference < -2 or y_difference > 2 or y_difference < -2:
                raise Exception(f"shouldn't get here... xdiff:{x_difference} ydiff:{y_difference}")
            #print(f"after resolve: {self.__knots}")
            self.__tail_visits.add(self.__knots[-1])


    def _do_R(self, n: int):
        for _ in range(n):
            self.H = (self.H[0] + 1, self.H[1])
            self._resolve_tail()
    
    def _do_U(self, n: int):
        for _ in range(n):
            self.H = (self.H[0], self.H[1] + 1)
            self._resolve_tail()
    
    def _do_L(self, n: int):
         for _ in range(n):
            self.H = (self.H[0] - 1, self.H[1])
            self._resolve_tail()
    
    def _do_D(self, n: int):
         for _ in range(n):
            self.H = (self.H[0], self.H[1] - 1)
            self._resolve_tail()

def part1(input_list):
    rope = RopeState()
    for instructon in input_list:
        rope.do_instruction(instructon)
    print(f"visited cells: {rope.tail_visited}")

def part2(input_list):
    rope = RopeState(10)
    for instructon in input_list:
        rope.do_instruction(instructon)
    print(f"visited cells: {rope.tail_visited}")
    

def main():
    input_lines = [ line.strip() for line in open(sys.argv[1], 'r') ]
    #print(input_lines)
    part1(input_lines)
    part2(input_lines)

if __name__ == '__main__':
    main()