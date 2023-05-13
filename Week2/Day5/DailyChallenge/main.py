
# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension

# Option 1. Split and sort methods
def list_and_sort(str_input):
    list1 = str_input.split(",")
    list1.sort()
    return list1
# Option 2. Split and list Comprehension.
# I think that they whant us to use some sort algoritm in loop or make new list.index
# So, I take very famouse bubble sort
def sort_2(list):
    
    unsorted = True
    while unsorted:
        unsorted = False             # this was moved out of the for loop
        for element in range(0,len(list) - 1):
            if list[element] > list[element + 1]:
                temp = list[element + 1]
                list[element + 1] = list[element]
                list[element] = temp
                # print badList        # comment this out when you're done testing
                unsorted = True      # this was moved up from the else block
    
    return list

#Option 3. There is one solution with list Comprehension
def sort_3(string):
    
    result = [m for m in string.split(',')]
    count = len(result)
    
 
    for outer in range(count-1): 
        for n in range(count-outer-1):
            if result[n] > result[n+1]:
                result[n],result[n+1] = result[n+1],result[n]
    return result
   
   

def list_to_str(list):
    output = ','.join(list)
    print(output)
    return output

input = "without,hello,bag,world"
list_to_str(list_and_sort(input))

sort_2(list_and_sort(input))
list_to_str(sort_3(input))
