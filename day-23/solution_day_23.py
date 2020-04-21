import copy

class Day23:
    '''
        Time Complexity: O(NM)
        Space Complexity: O(NM)
    '''
    @staticmethod
    def get_shortest_path(walls, start, end):
        if walls[start[0]][start[1]]:
            return None
        sp = {
            start : 0
        }
        directions = [(-1,0), (0,-1), (1,0), (0, 1)]
        queue = [start]
        N,M = len(walls),len(walls[0])
        while len(queue):
            cx,cy = queue.pop(0)
            for direction in directions:
                nx,ny = cx+direction[0],cy+direction[1]
                if not(nx>=0 and nx<N and ny>=0 and ny<M) or ((nx,ny) in sp) or walls[nx][ny]:
                    continue
                sp[(nx,ny)] = sp[(cx,cy)] + 1
                queue.append((nx,ny))
        if end in sp:
            return sp[end]
        return None

    '''
        Time Complexity: O(NM)
        Space Complexity: O(M + N)
    '''
    @staticmethod
    def get_shortest_path_optimized(walls, start, end):
        if walls[start[0]][start[1]]:
            return None
        walls[start[0]][start[1]] = 0
        directions = [(-1,0), (0,-1), (1,0), (0, 1)]
        queue = [start]
        N,M = len(walls),len(walls[0])
        while len(queue):
            cx,cy = queue.pop(0)
            for direction in directions:
                nx,ny = cx+direction[0],cy+direction[1]
                if not(nx>=0 and nx<N and ny>=0 and ny<M) or (type(walls[nx][ny]) ==  int) or walls[nx][ny] == True:
                    continue
                walls[nx][ny] = walls[cx][cy] + 1
                queue.append((nx,ny))
        if type(walls[end[0]][end[1]]) == int:
            return walls[end[0]][end[1]]
        return None

if __name__ == '__main__':
    day_23 = Day23()
    walls_0 = [
        [False, False, False, False],
        [True, True, False, True],
        [False, False, False, False],
        [False, False, False, False]
    ]

    assert day_23.get_shortest_path(walls_0, (3,0), (0,0)) == 7
    assert day_23.get_shortest_path(walls_0, (0,0), (0,0)) == 0
    assert not day_23.get_shortest_path(walls_0, (3,0), (1,3))

    assert day_23.get_shortest_path_optimized(copy.deepcopy(walls_0), (3,0), (0,0)) == 7
    assert day_23.get_shortest_path_optimized(copy.deepcopy(walls_0), (0,0), (0,0)) == 0
    assert not day_23.get_shortest_path_optimized(copy.deepcopy(walls_0), (3,0), (1,3))

    walls_1 = [
        [False, False, True, False],
        [True, True, True, True],
        [False, False, False, False],
        [False, False, True, False]
    ]
    assert not day_23.get_shortest_path(walls_1, (3, 0), (0, 0))
    assert day_23.get_shortest_path(walls_1, (3, 0), (3, 3)) == 5

    assert not day_23.get_shortest_path_optimized(copy.deepcopy(walls_1), (3, 0), (0, 0))
    assert day_23.get_shortest_path_optimized(copy.deepcopy(walls_1), (3, 0), (3, 3)) == 5

