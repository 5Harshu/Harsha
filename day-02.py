'''def climbstairs(n):
    steps=[]
    steps.append(1)
    steps.append(2)
    for i in range(2,n):
        steps.append(steps[i-1]+steps[i-2])
    return steps[n-1]
n=4
print(climbstairs(n))'''




'''def checkyear(year):
    if(year%4)==0:
        if (year%100)==0:
            if(year%400)==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#driver code
year=2001
if(checkyear(year)):
    print("leap year")
else:
    print("not a leap year")'''




'''countofwords=len("hello this is python programming".split())
print("count of words in the given sentence:",countofwords)
print(len("hello this is python programming".split()))
print(len(input("enter input:").split()))'''


'''a=[1,6,8,9,6]
b=[5,9,3,67,95,67,3,1]
a.extend(b)
print(a)
a.sort()
print(a)'''


'''class solution:
    def update(op,v):
         if op=="+": stack.append(v)
         if op=="-": stack.append(-v)
         if op=="+": stack.append(stack.pop()*v)#for BC II and BC III
         if op=="/": stack.append(int(stack.pop()/v))#for BC II and BC III
    it,num,stack,sign=0,0,[],"+"
    while it<len(s):
        if s[it].isdigit():
            num=num*10+int(s[it])
        elif s[it]in "+-*/":
            update(sign,num)
            num,sign=0,s[it]
        elif s[it]=="(":#For BC I and III
            num,j=self.calculate(s[it+1:])
            it=it+j
        elif s[it]==")":#For BC I and BC III
            update(sign,num)
return sum(stack), it+1
it+=1
update(sign,num)
return sum(stack)'''


    
        

      

    
        
