# 要求一
def calculate(min, max, step):
    result=0
    i=min
    while i<=max: 
        result+=i
        i=i+step
    print(result)
# 請用你的程式補完這個函式的區塊
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0



# 要求二
def avg(data):
    total=0
    num=0
    for i in range(len(data["employees"])): #先決定迴圈要跑幾次
        if data["employees"][i]["manager"]==False:
            total+=data["employees"][i]["salary"]
            num+=1
    print(total/num)

avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式



# 要求三：
def func(a):
    def multipy(b,c):
        print(a+b*c)
    return multipy
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果



#要求4 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
def maxProduct(nums):
    from itertools import combinations
    list=[]
    for i in combinations(nums,2):
        x=i[0]*i[1]
        list.append(x)
    print(max(list))

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10


# 要求5
def twoSum(nums, target):
    from itertools import combinations #算怎和的套件
    for i in combinations(nums,2): #從nums中挑兩個出來組合成list
        if i[0]+i[1]==target:
            list=[]
            list.append(nums.index(i[0])) #查找特定資料在list中的位置
            list.append(nums.index(i[1]))
            return list

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


#要求6
def maxZeros(nums):
    count= 0
    countnote= []
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            countnote.append(count)
            count = 0
    countnote.append(count)

    print(max(countnote))

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3

maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]) # 得到 6


