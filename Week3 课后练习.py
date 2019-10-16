
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#生成并打印2020年的日历

year=["January","February","March","April","May","June","July","August","September","October","Novermber","December"]
moin=["Mo","Tu","We","Th","Fr","Sa","Su"]

def print_cell(f):
    print("      ",year[f-1])
    for i in range(0,7):
        print(moin[i],end=" ")
    print("\n")
    print_date(f)
    return

def print_date(a):
    b=[31,29,31,30,31,30,31,31,30,31,30,31]
    c=[2,5,6,2,4,0,2,5,1,3,6,1]
    print(" "*c[a-1]*3,end="")
    d=1
    while(d<=b[a-1]):
        print(repr(d).rjust(2),end=" ")
        d+=1
        if (d+c[a-1]-1)%7==0:
            print("\n")
    print("\n\n")
    return
        
x=1
while x <=12:
    print_cell(x)
    x+=1


# In[ ]:

