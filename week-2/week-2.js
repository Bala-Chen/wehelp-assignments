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
    let sumSalary = 0;
    for(j = 0; j < data["count"]; j++){
        let empSalary = data["employees"][j]&&data["employees"][j]["salary"];
        sumSalary += empSalary
    };
    console.log(sumSalary / data["count"]);
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
//Time complexity :O(n^2)
function maxProduct(nums){
    let multiply = []
    for (i = 0; i < nums.length; i++){
        for(n = 0; n < nums.length; n++){
            if (i == n){
                continue
            };
            let mulNum = nums[i] * nums[n];
            if (multiply.includes(mulNum) == false){
                multiply.push(mulNum)
            }
        }
    }
    mulMax = Math.max.apply(null,multiply);
    console.log(mulMax)
}

maxProduct([5,20,2,6])
maxProduct([10,-20,0,3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1,-2,0])

//Q4
function twoSum(nums,target){
    let dict = {};
    for(let numIndex = 0; numIndex < nums.length;numIndex++){
        dict[nums[numIndex]] = numIndex;
    }
    for(let numIndex2 = 0; numIndex2 < nums.length;numIndex2++){
        let goal = target - nums[numIndex2];
        if (goal in dict && numIndex2 != dict[goal]){
            return [numIndex2,dict[goal]]
        }
    }    
}
let result = twoSum([2,11,7,15],9);
console.log(result);

//Q5
//Time complexity :O(n)
function maxZeros(nums){
    let maxCount = []
    let count = 0
    for(let i in nums){
        if (nums[i] == 0){
            count = count + 1
        };
        if (nums[i] != 0){
            maxCount.push(count);
            count = 0;
            continue
        };
    };
    maxCount.push(count);
    console.log(Math.max.apply(null,maxCount));
}
maxZeros([0,1,0,0])
maxZeros([1,0,0,0,0,1,0,1,0,0])
maxZeros([1,1,1,1,1])
maxZeros([0,0,0,1,1])