#Q1
def calculate(min,max):
    sum = 0
    for i in range(min,max+1):       
        sum += i
    print(sum)

calculate(1,3)
calculate(4,8)

#Q2
def avg(data):
    sum_salary = 0
    for j in range(data["count"]):
        emp_salary = (data["employees"][j]["salary"])
        sum_salary += emp_salary
    avg_salary = sum_salary / (data["count"])
    print(avg_salary)
  
avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
                {
            "name":"Bob",
            "salary":60000
        },
                {
            "name":"Jenny",
            "salary":50000
        }
    ]
})

#Q3
def maxProduct(nums):
    multiply = []
    for i in range(len(nums)):
        for n in range(len(nums)):
            if i == n:
                continue
            mul_num = nums[i] * nums[n]
            if mul_num not in multiply:
                multiply.append(mul_num)
    print(max(multiply))

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])

#Q4
def twoSum(nums,target):
    num_index = 0 
    for num in nums:
        num_index += 1
        if target - num in nums[num_index:]:
            return [num_index-1, nums[num_index:].index(target-num) + num_index]

result = twoSum([2,11,7,15],9)
print(result)

#Q5
def maxZeros(nums):
    max_count = []
    count = 0
    for num in nums:
        if num == 0:
            count += 1
        if num != 0:
            max_count.append(count)
            count = 0
            continue
    max_count.append(count)
    print(max(max_count))

maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])
maxZeros([0,0,0,1,1])