"""
program that finds the longest common substring in two words, and prints a before
and after image of the matrix used to find the answer
author: Satchel Peterson
"""

class plane_tester(object):
    def matrix_init(len1, len2): # Initializes a matrix of size (len1+1)x(len2+1)
        dp_matrix = [[0] * (len2+1) for _ in range(len1+1)]
        return dp_matrix
    
    def print_matrix(dp_matrix): # Prints the matrix in a readable format
        len1, len2 = len(dp_matrix[0]), len(dp_matrix)
        stringbuilder = ""
        print("[")
        for i in range(len2):
            if(stringbuilder):
                stringbuilder += "]"
                print(stringbuilder)
            stringbuilder = ""
            for j in range(len1):
                if(not stringbuilder):
                    stringbuilder += "["
                stringbuilder += (str(dp_matrix[i][j]))
                if(j!=len1-1):
                    stringbuilder += ", "
        if(stringbuilder):
            stringbuilder+="]"
            print(stringbuilder)
        print("]")

    def longest_common_substring(text1, text2, dp): # Finds the longest common substring in text1 and text2
        len1, len2 = len(text1), len(text2)
        for i in range(len1):
            for j in range(len2):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp

    #driver code
    text1 = "samsunlaxg"
    text2 = "galaxymobile"
    matrix = matrix_init(len(text1), len(text2))
    print_matrix(matrix)
    print("\n")
    new_matrix = longest_common_substring(text1, text2, matrix)
    print_matrix(new_matrix)
    print("\n")
    print(new_matrix)
    print("\n")
    print("longest common substring is: " + str(new_matrix[-1][-1]))