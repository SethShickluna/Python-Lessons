
lst = [1, 2, 34, 4,65, 6, 78, 86, 9]

for index in range(len(lst)):
    print(index, lst[index])
    

lst = [1, 2, 3]
    
def centered_average(nums):
  
  sum_ = sum(nums) 
  min_ = min(nums) 
  max_ = max(nums) 
  
  c = sum_ - max_ - min_ 
  
  return int(c / (len(nums) -2))

print(centered_average(lst))