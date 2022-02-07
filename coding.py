# chetan first question perfact square matrix

import math
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
m = len(a[0])
c = 0
ans = 0
for i in range(n):
    if i%2==0:
        for j in range(m):
            c += a[i][j]
            x = math.sqrt(c)
            if x - int(x)==0:
                ans = max(c,ans)
                c = 0
    else:
        for j in range(m-1,-1,-1):
            c += a[i][j]
            x = math.sqrt(c)
            if x - int(x)==0:
                ans = max(c,ans)
                c = 0
print(ans)

# chetan 2nd question string and number seprator matrix

def seprator(s):
    s1 = ''
    s2 = ''
    for i in s:
        if i>='0' and i<='9':
            s1 += i
        else:
            s2 += i
    return int(s1), s2

n1 = list(map(str, input().split(',')))
n2 = list(map(int, input().split(',')))
d = dict()
ans = []
for i in n2:
    d[i] = True
for i in n1:
    num, st = seprator(i)
    if d.get(num,False):
        ans.append([num,st])
    else:
        ans.append(['NA','NA'])
n = len(ans)
for i in range(n):
    if i != n-1:
        print(ans[i][0],end=',')
    else:
        print(ans[i][0])
for i in range(n):
    if i != n-1:
        print(ans[i][1],end=',')
    else:
        print(ans[i][1])

# ---------------------------------------------------------------------------------------------------------

# MD binary matrix question

m = int(input())
mat = []
for i in range(m):
    mat.append(list(map(str,input().split(','))))
d = dict()
n = len(mat[0])
for i in range(m):
    x = set(mat[i])
    for j in x:
        d[j] = d.get(j,0)+1

for i in range(m):
    c0, c1 = 0, 0
    for j in range(n):
        if d[mat[i][j]]==m:
            mat[i][j] = 0
            c0 += 1
        elif d[mat[i][j]] > m//2:
            if i%2!=0:
                mat[i][j] = 0
                c0 += 1
            else:
                mat[i][j] = 1
                c1 += 1
        else:
            mat[i][j] = 1
            c1 += 1
    if c0 == c1:
        for j in range(n):
            mat[i][j] = 1 if j%2==0 else 0
    elif c0 != c1:
        for j in range(n):
            if j < c1//2 + c1%2:
                mat[i][j] = 1
            elif j < c1//2 + c1%2 + c0:
                mat[i][j] = 0
            else:
                mat[i][j] = 1
for i in range(m):
    for j in range(n):
        if j != n-1:
            print(mat[i][j], end=',')
        else:
            print(mat[i][j])
----------------------------------------------------------------------------------

# Rohit friend question special factor question

def factors(n,s):
    c = 0
    for i in range(1, n//2+1):
        if n%i == 0 and str(i) in s:
            c += 1
    if str(n) in s:
        c += 1
    return c


s = input()
ans, c = 0, 0
n = len(s)
d = dict()
for i in range(n-1):
    x = factors(int(s[i]+s[i+1]), s)
    if x >= c:
        c = x
        ans = max(ans, int(s[i]+s[i+1]))
print(ans)

# input : 2340567
# output : 56
    
#  Rohit friend 2nd question sort differece question 

s = input()
f = ['' for i in range(26)]
n = len(s)
c = 0
z1, z2 = 0, 0
x1, x2 = 'z', 'a'
y1, y2 = 9, 0
i1, i2, i3, i4 = 0, 0, 0, 0
for i in range(n):
    if s[i] >= 'a' and s[i] <= 'z':
        z1 = -1
        if s[i] < x1:
            x1 = s[i]
            i1 = i
        if s[i] > x2:
            x2 = s[i]
            i2 = i
        f[ord(s[i])-97] += s[i]
    else:
        z2 = -1
        t = int(s[i])
        c += t
        if t < y1:
            y1 = t
            i3 = i
        if t > y2:
            y2 = t
            i4 = i
print(i1,i2,i3,i4)
if (z1 == -1 and z2 == 0) or (z1 == 0 and z2 == -1):
    print(-1)
else:
    s1 = ''.join(f)
    print(s1,end="")
    print(abs(i2-i1),end=":")
    print(c,end="")
    print(abs(i4-i3))
    
# input : gt4r22w72     output : egrtw2:153

# >>>>>>>>>> Rohit friend 3rd question 2 array common problem

def oneWord(n):
    n = str(n)
    while len(n)>1:
        c = 0
        for i in n:
            c += int(i)
        n = str(c)
    return int(n)
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr = list(set(arr1)&set(arr2))
if len(arr)==0:
    print(-1)
else:
    y = min(arr)
    if y==0:
        print(-1)
    else:
        x = oneWord(y)
        if x > len(arr1) or x > len(arr2):
            print(-1)
        else:
            arr1.sort()
            arr2.sort()
            ans = [arr1[-1*x:],arr2[-1*x:]]
            print(ans)
#  input1 : 0,17,61,65,90    5,0,1,4,100    output : -1 becuase no commn element
#  input2 : 101,101,610,447,389     610,4,101,4,101    output : 447,610    101,610

--------------------------------------------------------------------------------

# Rohit first question remove dublicate and append X if list is empty

a = list(map(str, input().split(',')))
arr = []
d = dict()
z = 0
for i in a:
    temp = []
    for word in i.split():
        if word not in d:
            temp.append(word)
            d[word] = 1
        else:
            z = -1
    if len(temp)==0:
        arr.append('X')
    else:
        arr.append(' '.join(temp))
if z == 0:
    print("-1")
else:
    print(arr)

# input : God sees th sees people,god is great great,people sees the god
# output : God sees the people /n god is great /n X
# input2 : All that glitters,is,not gold
# output : -1

# >>>>>>> Rohit 2nd question armostrong number

def amstrong(s):
    n = len(s)
    c = 0 
    for i in s:
        c += int(i)**n
    return c == int(s)

arr = list(map(str, input().split(',')))
n = len(arr)
d = dict()
ans = []
for i in range(n-1):
    for j in range(i+1,n):
        if amstrong(arr[i]+arr[j]) and d.get(arr[i]+arr[j],True):
            d[arr[i]+arr[j]] = False
            ans.append(arr[i]+arr[j])
if len(ans)==0:
    print(-1)
else:
    print(','.join(ans))


# input : 15,3,1,70,53,71  output : 153,370,371
# input1 : 9,3,2,11,1   output : -1

------------------------------------------------------------------------------------------------------------
# >>>>>>> animesh 2nd question smallest substring all unique charater sliding window

def smallest(s, pat):
    d = dict()
    for i in pat:
        d[i] = d.get(i,0)+1
    count = len(d)
    n = len(s)
    ans = 2*n
    res = ''
    i, j = 0,0
    while j < n:
        if d.get(s[j],'#') != '#':
            d[s[j]] -= 1
            if d[s[j]] == 0:
                count -= 1
        if count > 0:
            j += 1
        else:
            while count == 0 and i <= j:
                if d.get(s[i],'#') != '#':
                    d[s[i]] += 1
                if d[s[i]] == 1:
                    count += 1
                i += 1
            if j - i + 2 < ans:
                res = s[i-1:j+1]
                ans = j - i + 2
            j += 1
    if ans == 2*n:
        return -1
    return ans, res


s = input()
s = s.split(',')
c, z = 99999999, ''
for i in s:
    x, y = smallest(i, set(i))
    if x < c:
        c = x
        z = y[:]

print(z)

# input : Assign,zzzzzzxzsdxs,Madammxmsgn,1a12231a
# output : xzsd

# >>>>>>> Animesh 2nd qusetion 



-------------------------------------------------------------------------
# Khushi 1st question sort a given column and sum all row 

m = int(input())
mat = []
for i in range(m):
    mat.append(list(map(int, input().split(','))))
k = int(input())
d = []
for i in range(m):
    d.append([mat[i][k], i])
d.sort(key = lambda x : (x[0],x[1]))
ans = []
for curr in d:
    ans.append(sum(mat[curr[1]]))
n = len(ans)
for i in range(n):
    if i != n-1:
        print(ans[i],end=',')
    else:
        print(ans[i])
 
    
