
class Day19:
    '''
        Time Complexity: O(N*M)
        Space Complexity: O(N*M)
    '''
    def get_max(self, MAT, N, M):
        DP = [[0] * M] * N
        for index in range(M):
            DP[0][index] = MAT[0][index]
        for j in range(1,N):
            L = [0] * M
            R = [0] * M
            L[0],R[M-1] = DP[j-1][0], DP[j-1][M-1]
            for i in range(1,M):
                L[i] = min(L[i-1], DP[j-1][i])
            for i in range(M-2,-1,-1):
                R[i] = min(R[i+1], DP[j-1][i])
            for i in range(M):
                if i == 0:
                    DP[j][i] = R[i+1] + MAT[j][i]
                elif i == M-1:
                    DP[j][i] = L[i-1] + MAT[j][i]
                else:
                    DP[j][i] = min(L[i-1], R[i+1]) + MAT[j][i]
        return min(DP[N-1])

if __name__ == "__main__":
    day19 = Day19()
    cost_matrix = \
        [[7, 3, 8, 6, 1, 2],
         [5, 6, 7, 2, 4, 3],
         [10, 1, 4, 9, 7, 6]]
    assert day19.get_max(cost_matrix,
                                     len(cost_matrix), len(cost_matrix[0])) == 4
    cost_matrix = \
        [[7, 3, 8, 6, 1, 2],
         [5, 6, 7, 2, 4, 3],
         [10, 1, 4, 9, 7, 6],
         [10, 1, 4, 9, 7, 6]]
    assert day19.get_max(cost_matrix,
                                     len(cost_matrix), len(cost_matrix[0])) == 8