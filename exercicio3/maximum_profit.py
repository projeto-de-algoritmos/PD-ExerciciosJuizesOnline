class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        # Lista de tupla com os jobs por ordem de fim
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        qtd_jobs = len(jobs)

        # armazena as soluçÕes parciais do problema
        dp = [0] * (qtd_jobs + 1)

        # armazena o índice do último trabalho compatível com o trabalho i, ou 0 se nenhum trabalho anterior for compatível.
        p = [0] * (qtd_jobs + 1)

        # tenta encontrar o trabalho mais recente que é compatível com o trabalho atual
        for i in range(qtd_jobs - 1, -1, -1):
            j = i - 1
            while j >= 0 or p[i] != 0:
                if jobs[j][1] <= jobs[i][0]:
                    p[i + 1] = j + 1
                    break
                j -= 1

        # Define o caso base, indicando que o máximo lucro obtido até o momento 0 (nenhum trabalho) é 0.
        dp[0] = 0

        for i in range(1, qtd_jobs + 1):
            dp[i] = max(jobs[i - 1][2] + dp[p[i]], dp[i - 1])

        return max(dp)


if __name__ == '__main__':
    solver = Solution()

    startTime = input()
    endTime = input()
    profit = input()

    print(solver.jobScheduling(
        list(map(int, startTime.split(','))), 
        list(map(int, endTime.split(','))) , 
        list(map(int, profit.split(',')))
    ))
