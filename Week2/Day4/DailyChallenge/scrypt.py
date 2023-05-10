    
    # Given a “Matrix” string:
    # The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
        
    # # 7i3
    # # Tsi
    # # h%x
    # # i #
    # # sM 
    # # $a 
    # # #t%
    # # ^r!
    # To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, 
    # selecting only the alpha characters and connecting them. Then he replaces every group of symbols between 
    # two alpha characters by a space.

#Using his technique, try to decode this matrix.
# matrix_string = ("7i3","Tsi","h%x","i #","sM ","$a ", "#t%", "^r!")
# matrix_list = []
# for i in range(len(matrix_string)):
#     matrix_list.append([])
#     for j in range(len(matrix_string[i])):
#         matrix_list[i].append(matrix_string[i][j])

matrix_string = ("7i3Tsih%xi #sM $a #t%^r!")

# matrix_list = [[]]
# i = 0
# j = 0

# for symb in matrix_string:
   
#     matrix_list[i].append(symb)
#     j += 1
#     if j > 2:
#         i += 1
#         j = 0
#         matrix_list.append([])

def matrix_string_to_list(in_string):
    matrix_list = [[]]
    i = 0
    j = 0

    for symb in in_string:
    
        matrix_list[i].append(symb)
        j += 1
        if j > 2:
            i += 1
            j = 0
            if i < int(len(in_string)/3): matrix_list.append([])
    return matrix_list



    #Option 1. Evry symbol(group of symbols) between two alpha characters replace by a space. 
    #So, didgit between two alpha characters shhould replace for space
def encode_option1(in_list):
    res_string = ""
    space = ""
    for i in range(len(in_list[0])):
        for j in in_list:
            if j[i].isalpha():
                res_string += space
                space = ""
                res_string += j[i]
            else:
                if len(res_string) > 0:
                    space = " "
    return res_string             


matrix_list = matrix_string_to_list(matrix_string)
print(matrix_string)
print(matrix_list)
res = encode_option1(matrix_list)
print("Option 1 : ", res)

    #Option 2. Only group of symbols(qity >=2)) between two alpha characters replace by a space. 
    #So, didgit between two alpha characters should be deleted

def encode_option2(in_list):
    res_string = ""
    space = ""
    symb_qty = 0
    
    for i in range(len(in_list[0])):
        for j in in_list:
            if j[i].isalpha():
                res_string += space
                space = ""
                symb_qty = 0
                res_string += j[i]
                
            else:
                symb_qty += 1
                if len(res_string) > 0 and symb_qty >= 2:
                    space = " "
    return res_string             

res = encode_option2(matrix_list)
print("Option 2 : ", res)



