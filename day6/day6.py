import sys

def part1(inputbuffer):
    read_stream = set()
    chars_read = 0
    for i in range(0,len(inputbuffer)-4):
        window_end = i+4
        if len(set(inputbuffer[i:window_end])) == 4:
            print(f"packet boundary: {window_end}")
            break

def part2(inputbuffer):
    read_stream = set()
    chars_read = 0
    for i in range(0,len(inputbuffer)-14):
        window_end = i+14
        if len(set(inputbuffer[i:window_end])) == 14:
            print(f"message boundary: {window_end}")
            break


def main():
    input_buffer = open(sys.argv[1], 'r').readline()
    part1(input_buffer)
    part2(input_buffer)

if __name__ == '__main__':
    main()