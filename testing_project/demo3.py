import statistics

li = [1, 2, 2, 3, 3, 3,2]

#print ("Mean:",statistics.mean(li))
#print (statistics.mean(li))

#print ("Mode: ",statistics.mode(li))
#print (statistics.mode(li))

print ("The median of list element is : ",end="")
print (statistics.median(li))

print ("The lower median of list element is : ",statistics.median_low(li))
#print (statistics.median_low(li))

print ("The higher median of list element is : ",end="")
print (statistics.median_high(li))
