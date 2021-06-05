#Declare List Variant
print("#Declare List Variant")
NumAndStr = [1, 2, 3]
print(NumAndStr)
print(len(NumAndStr))
print(NumAndStr[1])
#output:
#[1, 2, 3]          Index:0, 1, 2
#3
#2

print("\n")

#Insert & Append Element In List
print("#Insert & Append Element In List")
NumAndStr.insert(1, "ONE")
NumAndStr.insert(3, "TWO")
NumAndStr.append("THREE")
print(NumAndStr)
#output:
#[1, 'ONE', 2, 'TWO', 3, 'THREE']

print("\n")

#Remove Last List Element
print("#Remove Last List Element")
NumAndStr.pop()
print(NumAndStr)
#output:
#[1, 'ONE', 2, 'TWO', 3]

print("\n")

#Remove Element 1 (1 is not index, 1 is the element of LIST:NumAndStr)
print("#Remove Element 1 (1 is not index, 1 is the element of LIST:NumAndStr)")
NumAndStr.remove(1)
print(NumAndStr)
#output:
#['ONE', 2, 'TWO', 3]

print("\n")

#Extend list in current list
print("#Extend list in current list")
NumAndStr.extend([4, "Four"])
print(NumAndStr)
#output:
#['ONE', 2, 'TWO', 3, 4, 'Four']

print("\n")

#Del Element
print("#Del Element")
del NumAndStr[0]        #['ONE', 2, 'TWO', 3, 4, 'Four'] -> [2, 'TWO', 3, 4, 'Four']
print(NumAndStr)
del NumAndStr[2:4]      #[2, 'TWO', 3, 4, 'Four'] -> [2, 'TWO', 'Four'] del index2 & 3 element
print(NumAndStr)
#[2, 'TWO', 3, 4, 'Four']
#[2, 'TWO', 'Four']

print("\n")

#Clear List
print("#Clear List")
NumAndStr.clear()
print(NumAndStr)
#output:
#[]

print("\n")

#Output LIST Element by While
NumAndStr = [1, 2, 3]
print("#Output list [1, 2, 3] by while statement")
Count = 0
while Count < len(NumAndStr):
    print(NumAndStr[Count])
    Count = Count + 1
#output:
#1
#2
#3

print("\n")

#Output LIST Element by for
NumAndStr = [1, 2, 3]
print("#Output list [1, 2, 3] by for statement")
for element_NumAndStr in NumAndStr:
    print(element_NumAndStr)
#output:
#1
#2
#3
