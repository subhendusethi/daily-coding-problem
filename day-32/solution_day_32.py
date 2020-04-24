from math import log

class Day32:
    '''
        Time Complexity: O(N^3)
        Space Comlpexity: O(N)
        Bellman Ford
    '''
    @staticmethod
    def check_arbitrage(cost_matrix):
        num_vertices = len(cost_matrix)
        for i in range(num_vertices):
            for j in range(num_vertices):
                cost_matrix[i][j] = -log(cost_matrix[i][j])

        dp = [float('inf') for _ in range(num_vertices)]
        dp[0] = 0

        for _ in range(num_vertices-1):
            for u in range(num_vertices):
                for v in range(num_vertices):
                    if dp[v] > dp[u] + cost_matrix[u][v]:
                        dp[v] = dp[u] + cost_matrix[u][v]

        for u in range(num_vertices):
            for v in range(num_vertices):
                if dp[v] > dp[u] + cost_matrix[u][v]:
                    return True
        return False

if __name__ == '__main__':
    day_32 = Day32()
    mat = [[1, 0.23, 0.25, 16.43, 18.21, 4.94],\
           [4.34, 1, 1.11, 71.40, 79.09, 21.44],\
           [3.93, 0.90, 1, 64.52, 71.48, 19.37],\
           [0.061, 0.014, 0.015, 1, 1.11, 0.30],\
           [0.055, 0.013, 0.014, 0.90, 1, 0.27],\
           [0.20, 0.047, 0.052, 3.33, 3.69, 1]]
    assert day_32.check_arbitrage(mat)

    mat1 = [[1, 2], [0.5, 1]]
    assert not day_32.check_arbitrage(mat1)