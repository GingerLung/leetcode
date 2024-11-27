"""
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
# python 3.12.4

def plusOne(digits):
    # for index in reversed(digits):
    # 從最後一位數字開始（最右邊）
    # n = len(digits)  # 取得數字陣列的長度
    for i in range(n - 1, -1, -1):  # 從陣列的最後一位開始遍歷
        # 如果當前數字是 9，將其設為 0，並進位
        if digits[i] == 9:
            digits[i] = 0
        else:
            # 如果當前數字不是 9，則直接加 1，並返回結果
            digits[i] += 1
            return digits
    
    # 如果跳出迴圈，表示所有數字都是 9
    # 需要在陣列前面加上一個 1
    return [1] + digits

if __name__=="__main__":
    digits = [1,2,3]
    print(plusOne(digits))

    digits = [4,3,2,1]
    print(plusOne(digits))

    digits = [9]
    print(plusOne(digits))




##########
# Frank. #
##########