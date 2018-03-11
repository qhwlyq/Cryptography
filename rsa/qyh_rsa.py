import random
import os
#快速模幂运算a**b%c
def mm(a,b,c):
    a=a%c
    ans=1
    while b!=0:
        if b&1:
            ans=(ans*a)%c
        b>>=1
        a=(a*a)%c
    return ans
#模逆运算
def extendedGCD1(a, b):
    if b == 0:
        return (1, 0, a)
    (x, y, r) = extendedGCD1(b, a%b)
    tmp = x
    x = y
    y = tmp - (a//b) * y
    return (x, y, r)
#Miller-Rabin素性检测算法
def primetest(n,k):
    print('\n检测：'+str(n))
    s=0
    while (n-1)%2**(s+1)==0:
        s=s+1
    t=(n-1)//2**s
    while k>0:
        print('   第 '+str(21-k)+' 轮检测: ')
        k=k-1
        b=random.randint(2,n-2)
        for i in range(s):
            j=(2**i)*t
            r=mm(b,j,n)#b**j%n 快速模幂运算
            if r==1 or r==n-1:
                print('       True')#测试
                break
            elif i==s-1:
                print('       False')#测试
                return False
    return True
#生成大素数p,q
def bigprime():
    a=10**32
    k=20
    j=1
    while j==1:
        i=1
        while i==1:
            p=random.randint(a,a*10)#(a,a*10)
            if p%2!=0 and p%3!=0 and p%5!=0:
                i=0
        flag=primetest(p,k)
        if flag==True:
            j=0
            return p
#生成密钥
def keyscreate():
    p=0
    q=0
    e=65537
    phi=0
    while p==q:
        p=bigprime()
        q=bigprime()
        phi=(p-1)*(q-1)
    n=p*q
    d=(extendedGCD1(e,phi)[0])%phi
    keys=[n,e,p,q,d,phi]
    print('公钥n= '+str(keys[0]))
    print('公钥e= '+str(keys[1]))
    print('\n私钥p= '+str(keys[2]))
    print('私钥q= '+str(keys[3]))
    print('私钥d= '+str(keys[4]))
    print('私钥phi(n)= '+str(keys[5]))
    with open('Keys.txt','w',encoding='utf-8') as keysfile:
        keysfile.write('n='+str(n))
        keysfile.write('\ne='+str(e))
        keysfile.write('\np='+str(p))
        keysfile.write('\nq='+str(q))
        keysfile.write('\nd='+str(d))
        keysfile.write('\nphi='+str(phi))
    return keys
#加密
def e_rsa(m,n,e):
    c=mm(m,e,n)
    return c
#解密
def d_rsa(c,n,d):
    m=mm(c,d,n)
    return m

if __name__=='__main__':
    i=0
    keys=[]
    while i==0:
        optionflag = int(input('请选择加密（0）或者解密（1）：'))
        if optionflag == 0:
            keys=keyscreate()
            m=input('请输入明文: ')
            with open('M.txt','w',encoding='utf-8') as mfile:
                mfile.write(m)
            c=e_rsa(eval(m),keys[0],keys[1])
            with open('C.txt','w',encoding='utf-8') as cfile:
                cfile.write(str(c))
            os.system('pause')
        elif optionflag == 1:
            with open('Keys.txt','r',encoding='utf-8') as keysfile:
                for line in keysfile:
                    key=line.rstrip().strip('nepqdphi=')
                    keys.append(int(key))
            with open('C.txt','r',encoding='utf-8') as cfile:
                c=cfile.read()
                c=int(c)
                print('读取的密文为：'+str(c))
            m=d_rsa(c,keys[0],keys[4])
            print('明文为： '+str(m))
            keys=[]
            os.system('pause')
            os.system('cls')
        else:
            print('请输入0或1!')
            os.system('pause')
            os.system('cls')

