# 20. Write a Python class to find the three elements that sum to zero from a list of n real numbers. 
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]] 

class SumZero:
    def checker(self, ls):
        result = []

        for i in ls:
            for j in ls[ls.index(i)+1:]:
                for k in ls[ls.index(j)+1:]:
                    if j + k + i == 0:
                        result.append([i,j,k])

        return result

result = SumZero()
print(result.checker([-25, -10, -7, -3, 2, 4, 8, 10]))