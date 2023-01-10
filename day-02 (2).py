'''class slolution:
    def lettercombinations(self,digits):
        if(len(digits)==0):
            return[]
        
        digit2char={'1': '',     '2': 'abc',  '3': 'def',
                    '4': 'ghi',  '5': 'jkl',  '6': 'mno',
                    '7': 'pqrs', '8': 'tuv',  '9': 'wxzy', '0':''}
        
        resus=['']
        
        for d in digits:
            tem=[]
            for c in digit2char[d]:
                tem=tem+[r+c for r in resus]
                
            resus=tem
            
        return resus
    ob=solution()
    print(ob.lettercombinations('87'))'''



'''class solution(object):
    def generateparenthesis(self,n):
        result=[]
        self.generateparenthesisUtil(n,n,"",result)
        return result
    def genarateparenthesisUtill(self,left,right,temp,result):
        if lest==0 and right==0:
            result.append(temp)
            return
        if left>0:
            self.generateparenthesisUtil(left-1,right,temp+'(',result)
        if right>left:
            self.generateparanthesisUtil(left,right-1,temp+')',result)
ob=solution()
print(ob.generateparenthesis(4))'''



'''def ismatch(s: str,p: str)-> bool:
    rows,coloums=(len(s),len(p))
    #base conditions
    if rows==0 and columns==0:
        return True
    if columns==0:
        return False
    #DP array
    dp=[[False for j in range(columns+1)]for i in range(rows+1)]
    #since empty string and empty pattren are a match
    dp[0][0]=True
    #deals with pattren containing*
    for i in range(2,columns+1):
        if p[i-1]=='*':
            dp[0][i]=dp[0][i-2]
    #for remaining charcters
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            if s[i-1]==p[j-1] or p[j-1]=='.':
                dp[i][j]=dp[i-1][j-1]
            elif j>1 and p[j-1]=='*':
                dp[i][j]=dp[i][j-2]
                if p[j-2]=='.' or p[j-2]==s[i-1]:
                    dp[i][j]=dp[i][j] or dp[i-1][j]
    return dp[rows][columns]
print(ismatch("a","aa"))'''



'''month=input("Input the month(e.g.January'February etc.):")
day=int(input("Input the day:"))

if month in ('January','February','march'):
    season='winter'
elif month in ('april','may','june'):
    season='spring'
elif month in ('july','august','september'):
    season='summer'
else:
    season='autumn'

if (month=='march')and(day>19):
    season='spring'
elif(month=='june')and(day>20):
    season='summer'
elif(month=='september')and(day>21):
    season='autumn'
elif(month=='december')and(day>20):
    season='winter'
print("season is",season)'''


'''def commonwords(sent1,sent2):
    sen1=set(sent1,sent2)
    sen2=set(sent2)
    common=list(sen1.intersection(sen2))
    return common
def removecommonwords(sent1,sent2):
    sentence1=list(sent1.split())
    sentence2=list(sent2.split())
    commonlist=commonwords(sentence1,sentence2)
    word=0
    for i in range(len(sentence1)):
        if sentence1[word] in commonlist:
            sentence2.pop(word)
            word=word-1
            word+=1
            print(*sentence1)
            print(*sentence2)'''
