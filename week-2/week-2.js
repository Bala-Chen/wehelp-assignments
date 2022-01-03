//Q1
function calculate(min,max){
    let sum = 0;
    for (i = min;i <= max; i++){
        sum = sum + i;
    }
    console.log(sum)
}
calculate(1,3)
calculate(4,8)

//Q2
function avg(data){
    let sum_salary = 0;
    for(j = 0; j < data["count"]; j++){
        let emp_salary = data["employees"][j]&&data["employees"][j]["salary"];
        sum_salary += emp_salary
    };
    console.log(sum_salary / data["count"]);
}

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
});

//Q3
function maxProduct(nums){
    let multiply = []
    for (i = 0; i < nums.length; i++){
        for(n = 0; n < nums.length; n++){
            if (i == n){
                continue
            };
            let mul_num = nums[i] * nums[n];
            if (multiply.includes(mul_num) == false){
                multiply.push(mul_num)
            }
        }
    }
    mul_max = Math.max.apply(null,multiply);
    console.log(mul_max)
}

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])

//Q4
function twoSum(nums,target){
    let dict = {};
    for(let num_index = 0; num_index < nums.length;num_index++){
        dict[nums[num_index]] = num_index;
    }
    for(let num_index_2 = 0; num_index_2 < nums.length;num_index_2++){
        let goal = target - nums[num_index_2];
        if (goal in dict && num_index_2 != dict[goal]){
            return [num_index_2,dict[goal]]
        }
    }    
}
let result = twoSum([2,11,7,15],9);
console.log(result);

//Q5
function maxZeros(nums){
    let max_count = []
    let count = 0
    for(let i in nums){
        if (nums[i] == 0){
            count = count + 1
        };
        if (nums[i] != 0){
            max_count.push(count);
            count = 0;
            continue
        };
    };
    max_count.push(count);
    console.log(Math.max.apply(null,max_count));
}
maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])
maxZeros([0,0,0,1,1])