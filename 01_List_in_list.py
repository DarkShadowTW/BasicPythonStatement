#Declare
NumAndStr = [
    [0, "ZERO"],
    [1, "ONE"],
    [2, "TWO"]
]
print(NumAndStr)
print(NumAndStr[1])
print(NumAndStr[1][1])
#output
#[[0, 'ZERO'], [1, 'ONE'], [2, 'TWO']]
#[1, 'ONE']
#ONE

#Insert & Extend List in List
NumAndStr.extend([[4, "FOUR"]])
print(NumAndStr)
NumAndStr.insert(3, [[3, "THREE"]])
print(NumAndStr)
#output
#[[0, 'ZERO'], [1, 'ONE'], [2, 'TWO'], [4, 'FOUR']]
#[[0, 'ZERO'], [1, 'ONE'], [2, 'TWO'], [[3, 'THREE']], [4, 'FOUR']]