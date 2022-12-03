file1 = open(
    "C:\\Users\\tains\\ADVENT-OF-CODE-2022\\Day1 - Calorie Counting\\input.txt", 'r')

count = 0
maxSum1 = 0
maxSum2 = 0
maxSum3 = 0

sum = 0

while True:

    # Get next line from file
    line = file1.readline()
    
    if line.strip() == '':
        maxSum1 = max(sum,maxSum1)
        if maxSum1 > maxSum2:
            maxSum1, maxSum2 = maxSum2, maxSum1 
        
        if maxSum2 > maxSum3:
            maxSum2, maxSum3 = maxSum3, maxSum2
        

        sum = 0
        count += 1
    else:
        count = 0
        line = int(line)
        sum += line
    
    if count == 2:
        break
file1.close()

print(maxSum1 + maxSum2 + maxSum3)
