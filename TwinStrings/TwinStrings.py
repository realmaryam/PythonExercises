def func1(list1 , list2):
    length = len(list1)
    
    if (length%2 != 0):
        for i in range(length):
            if list1[i] != list2[i]:
                return 0
        return 1
    
    if length == 1 :
        if list1 == list2:
            return 1
        else:
            return 0
    
    l1 = list1[0:int(length/2)]
    l2 = list1[int(length/2):length]
    
    t1 = list2[0:int(length/2)]
    t2 = list2[int(length/2):length]
    
    if ((func1(l1,t1) and func1(l2,t2)) or (func1(l1,t2) and func1(l2,t1))):
        return 1
    else:
        return 0
     
a = input()
list1 = list(map(str, a))

b = input()
list2 = list(map(str, b))

if(func1(list1,list2)):
    print('YES')
else:
    print('NO')