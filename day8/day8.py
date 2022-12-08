import sys

class Forrest:

    def __init__(self, forrest_array) -> None:
        self.__forrest_array = forrest_array
        self.__visible_array = self._init_visible()
    
    @property
    def visible_array(self):
        return self.__visible_array
    
    def get_max_visibility_score(self) -> int:
        max_score = -1
        for i in range(len(self.__forrest_array)):
            for j in range(len(self.__forrest_array[0])):
                view_score = self._vertical_view_score(i,j) * self._lateral_view_score(i,j)
                if view_score > max_score:
                    max_score = view_score
        return max_score

    
    def _init_visible(self):
        visible_array = []
        visible_array.append([ True for _ in range(len(self.__forrest_array[0])) ])
        for _ in range(1,len(self.__forrest_array) - 1):
            middle_list = [ False for _ in range(1,len(self.__forrest_array[0]) - 1)]
            middle_list.insert(0, True)
            middle_list.append(True)
            visible_array.append(middle_list)
        visible_array.append([ True for _ in range(len(self.__forrest_array[0])) ])
        return visible_array

    def _look_lateral(self, i, j):
        lvisibility = []
        for jl in range(0, j):
            if self.__forrest_array[i][j] <= self.__forrest_array[i][jl]:
                lvisibility.append(False)
        lvisibility = all(lvisibility)
        rvisibility = []
        for jr in range(j+1, len(self.__forrest_array[i])):
            if self.__forrest_array[i][j] <= self.__forrest_array[i][jr]:
                rvisibility.append(False)
        rvisibility = all(rvisibility)
        visibility = any([lvisibility, rvisibility])
        return visibility
    
    def _lateral_view_score(self, i, j) -> int:
        left_score = 0
        right_score = 0
        for jl in range(j-1, -1, -1):
            left_score += 1
            if self.__forrest_array[i][j] <= self.__forrest_array[i][jl]:
                break
        for jr in range(j+1, len(self.__forrest_array[i])):
            right_score += 1
            if self.__forrest_array[i][j] <= self.__forrest_array[i][jr]:
                break
        return left_score * right_score
    
    def _vertical_view_score(self, i, j) -> int:
        top_score = 0
        bottom_score = 0
        for it in range(i-1, -1, -1):
            top_score += 1
            if self.__forrest_array[i][j] <= self.__forrest_array[it][j]:
                break
        for ib in range(i+1, len(self.__forrest_array)):
            bottom_score += 1
            if self.__forrest_array[i][j] <= self.__forrest_array[ib][j]:
                break
        return top_score * bottom_score
    
    def _look_vertical(self, i , j):
        tvisibility = []
        for it in range(i-1, -1, -1):
            if self.__forrest_array[i][j] <= self.__forrest_array[it][j]:
                tvisibility.append(False)
        tvisibility = all(tvisibility)
        bvisibility = []
        for ib in range(i+1, len(self.__forrest_array)):
            if self.__forrest_array[i][j] <= self.__forrest_array[ib][j]:
                bvisibility.append(False)
        bvisibility = all(bvisibility)
        visibility = any([tvisibility, bvisibility])
        return visibility
    
    def get_visible_set(self) -> set:
        grid_tuples = set()
        for i in range(1, len(self.__forrest_array) - 1):
            for j in range(1, len(self.__forrest_array[0] )- 1):
                if self._look_lateral(i,j) or self._look_vertical(i,j):
                    self.__visible_array[i][j] = True
        for i in range(len(self.__forrest_array)):
            for j in range(len(self.__forrest_array[0])):
                if self.__visible_array[i][j]:
                    grid_tuples.add((i,j))
        return grid_tuples
    
    def __repr__(self) -> str:
        grids = []
        for line in self.__forrest_array:
            grids.append(f"{line}")
        grids.append('---')
        for line in self.__visible_array:
            grids.append(f"{line}")
        return "\n".join(grids)


def part1(input_list):
    f = Forrest(input_list)
    visible_tuples = f.get_visible_set()
    print(f"Part1: {len(visible_tuples)} visible trees")

def part2(input_list):
    f = Forrest(input_list)
    print(f"max visible distance: {f.get_max_visibility_score()}")

def main():
    input_lines = [ line.strip() for line in open(sys.argv[1], 'r') ]
    part1(input_lines)
    part2(input_lines)

if __name__ == '__main__':
    main()