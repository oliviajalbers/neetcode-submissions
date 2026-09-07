class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        total = 0
        i = -1
        for op in operations:
            length = len(score)
            if op == '+':
                score.append(score[length - 1] + score[length - 2])
            elif op == 'D':
                score.append(score[length - 1] * 2)
            elif op == 'C':
                score.pop()
            else:
                score.append(int(op))
        for s in score:
            total += s
        return total
        