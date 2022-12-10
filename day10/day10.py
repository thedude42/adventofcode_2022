import sys

class Cpu:

    def __init__(self, triggers: list=None) -> None:
        self.__clock = 0
        self.__register_X = 1
        if triggers is None:
            self.__clock_trigers = []
        else:
            self. __clock_trigers = triggers
        self.__screen = [ '.' for _ in range(240) ]
    
    @property
    def clock(self):
        return self.__clock
    
    @property
    def next_trigger(self):
        if len(self.__clock_trigers) == 0:
            return -1
        return self.__clock_trigers[0]
    
    @property
    def X(self) -> int:
        if self.__register_X == None:
            return 0
        return self.__register_X
    
    @X.setter
    def X(self, x: int):
        assert type(x) == int
        self.__register_X = x
    
    def tick(self):
        '''
        advances the clock and writes to the screen
        '''
        assert self.clock <= 240
        self.__screen[self.clock] = self._sprite_pixel_at_X()
        self.__clock += 1
    
    def _sprite_pixel_at_X(self) -> str:
        x_difference = (self.clock % 40) - self.X
        if x_difference >= -1 and x_difference <= 1:
            print(f"difference for #:{x_difference}")
            return '#'
        print(f"difference for .:{x_difference}")
        return '.'
    
    def do_clock_trigger(self) -> tuple:
        self.__clock_trigers.pop(0)
        return self.X, self.clock
    
    def _do_noop(self, noop) -> tuple:
        self.tick()
        x_at_signal = clock_at_signal = None
        if self.next_trigger == self.clock:
            x_at_signal, clock_at_signal = self.do_clock_trigger()
            return True, x_at_signal, clock_at_signal
        return False, x_at_signal, clock_at_signal
    
    def _do_addx(self, instruction) -> tuple:
        op, arg = instruction.split()
        assert op == 'addx'
        emit_signal = False
        x_at_signal = clock_at_signal = None
        arg = int(arg)
        self.tick()
        if self.next_trigger == self.clock:
            emit_signal = True
            x_at_signal, clock_at_signal = self.do_clock_trigger()
        self.tick()
        if self.next_trigger == self.clock:
            emit_signal = True
            x_at_signal, clock_at_signal = self.do_clock_trigger()
        self.X += arg
        return emit_signal, x_at_signal, clock_at_signal

    def execute(self, instruction) -> int:
        emit_signal = False
        x_at_signal = None
        clock_at_signal = None
        op_function = None
        if instruction == 'noop':
            op_function = self._do_noop
        else:
            op_function = self._do_addx
        emit_signal, x_at_signal, clock_at_signal = op_function(instruction)
        if emit_signal:
            return clock_at_signal * x_at_signal
        return None
    
    def __repr__(self):
        start = 0
        render = []
        #print(f"RAW SCREEN:\n{self.__screen}")
        for x in range(40, 241, 40):
            #print(f"start:{start} x:{x}")
            render.append(''.join(self.__screen[start:x]))
            start = x
        #print(f"RAW RENDER LIST:\n{render}")
        return "\n".join(render)

def part1(input_list):
    triggers = [20, 60, 100, 140, 180, 220]
    cpu = Cpu(triggers)
    signals = [ x for x in [ cpu.execute(instruction) for instruction in input_list] if x is not None ]
    print(signals)
    print(f"Sum of the signals: {sum(signals)}")

def part2(input_list):
    cpu = Cpu()
    for instruction in input_list:
        cpu.execute(instruction)
    print(cpu)

def main():
    input_lines = [ line.strip() for line in open(sys.argv[1], 'r') ]
    part1(input_lines)
    part2(input_lines)

if __name__ == '__main__':
    main()