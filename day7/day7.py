import sys
import re

size_re = re.compile(r'^(\d+)$')

class FileSystem:

    def __init__(self, size=None) -> None:
        self.__dirs = {'/': set()}
        self.__cwd = '/'
        self.__files = {}
        if size:
            self.__size = int(size)
    
    @property
    def cwd(self) -> str:
        return self.__cwd
    
    @property
    def size(self):
        return self.__size
    
    @property
    def usage(self) -> int:
        return sum([ v for _, v in self.__files.items() ])
    
    @property
    def available_space(self) -> int:
        if self.size == None:
            return -1
        return self.size - self.usage

    def cd(self, dir: str):
        if dir == self.__cwd:
            return
        elif dir == '..':
            for k, v in self.__dirs.items():
                if self.__cwd in v:
                    self.__cwd = k
                    return
            raise Exception(f"having a time finding parent directory for {self.__cwd}:\n{self.__dirs}")
        elif not self.__cwd + dir + '/' in self.__dirs[self.__cwd]:
            raise Exception(f"can't cd to {dir} from {self.__cwd}")
        self.__cwd = self.__cwd + dir + '/'
        if not self.__cwd in self.__dirs.keys():
            self.__dirs[self.__cwd] = set()

    def ls(self, output: list):
        for item in output:
            meta, val = item.split()
            m = size_re.match(meta)
            if m:
                self.__files[self.__cwd+val] = int(meta)
            elif meta == 'dir':
                self.__dirs[self.__cwd].add(self.__cwd + val + '/')
                self.__dirs[self.__cwd + val + '/'] = set()
    
    def get_directory_sizes(self) -> dict:
        dir_sizes = {}
        for dir in self.__dirs.keys():
            dir_sizes[dir] = sum([ v for k, v in self.__files.items() if dir in k ])
        return dir_sizes
    
    def find_sum_of_at_most_100000(self) -> int:
        dir_sizes_at_most_100000 = [ v for k,v in self.get_directory_sizes().items() if v <= 100000 ]
        return sum(dir_sizes_at_most_100000)
    
    def find_smallest_dir_to_make_size_available(self, target_availability: int) -> int:
        dir_sizes = self.get_directory_sizes()
        for dir, size in sorted(dir_sizes.items(), key=lambda x: x[1]):
            if self.available_space + size >= target_availability:
                return size



def parse_input(input_lines, size=None) -> FileSystem:
    fs = FileSystem(size)
    i = 0
    while i < len(input_lines):
        print(f"CWD = {fs.cwd}")
        if input_lines[i][0] == '$':
            print(f"processing line {input_lines[i]} where i={i}")
            print(f"{input_lines[i][2:4]}")
            if input_lines[i][2:4] == 'cd':
                print(f"doing cd {input_lines[i][5:]}")
                fs.cd(input_lines[i][5:].strip())
                i += 1
            elif input_lines[i][2:4] == 'ls':
                print(f"doing {input_lines[i]}")
                i += 1
                j = i
                while input_lines[j][0] != '$':
                    j += 1
                    if len(input_lines) == j:
                        break
                print(f"doing ls for list {input_lines[i:j]}")
                fs.ls(input_lines[i:j])
                i = j
    return fs

def part1(input_lines):
    fs = parse_input(input_lines)
    print(f"part1: {fs.find_sum_of_at_most_100000()}")

def part2(input_lines):
    fs = parse_input(input_lines, size=70000000)
    print(f"part2: size of smallest directory that fulfills the requirements: {fs.find_smallest_dir_to_make_size_available(30000000)}")


def main():
    input_lines = [ line.strip() for line in open(sys.argv[1]) ]
    part1(input_lines)
    part2(input_lines)

if __name__ == '__main__':
    main()