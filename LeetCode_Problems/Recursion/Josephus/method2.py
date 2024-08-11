def findTheWinner(n, k):
    #write code here
    def josephus(n):
        if n == 1:
            return 0
        #recursive case
        return (josephus(n-1) + k)%n
    return josephus(n) + 1