def task1():
    numbers=[20,60,65,23,12,56]
    total=0
    num=0
    print(numbers[::-1])
    for i in range(0,6):
        total+=numbers[i]
        num+=1
        
    print(numbers)
    print(total)
    average=total/num
    print(average)

def task2():
    name=['Blue','Sonic','Sliver','Mario','Link','Peach']
    index=0
    search=input('Search for a name in the array')
    for x in range(0,5):
        if search==name[x]:
            index=1+x
        else:
            pass
    if index==0:
        print('That name is not located in the list try again')
        task2()
    else:
        print('Index Number',index)
def task3():
    quarter=[]
    Outlet1Sales = [10, 12,15,10]
    Outlet2Sales = [5,8,3,6]
    Outlet3Sales = [10,12,15,10]
    for i in range(0,4):
        salesfigure=Outlet1Sales[i] + Outlet2Sales[i] + Outlet3Sales[i]
        quarter.append(salesfigure)
    print(quarter)
    for x in range(0,4):
        print('Total for quarter',x,'is',quarter[x])
    print('Thats it')
    
 
    
        
    

    
    
