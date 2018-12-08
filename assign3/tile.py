m=int(input("m=?"))
n=int(input("n=?"))
a=int(input("a=?"))
b=int(input("b=?"))
t=int(m*n/a/b)
# 数据报错
import sys
if (m*n)%(a*b)!=0:#墙的面积无法整除砖的面积
	print("Can't be fully covered!")
	sys.exit()
if max(m,n)<max(a,b):#砖长(宽)大于墙长(宽)
	print("a or b is too large!")
	sys.exit()
#制作表格点坐标列表
#x,y是起始坐标，a,b是步长
def mesh(x,y,a,b):
    list=[]
    for i in range(x,x+a):
        for j in range(y,y+b):
            list.append((i,j))
    return list
#制作砖的边框点列表
def frame(x,y,a,b):
    list=[(x,y),(x+a-1,y),(x,y+b-1),(x+a-1,y+b-1)]
    if a>b:
        for i in range(0,a,b):
            list.append((x+i,y))
            list.append((x+i,y+b-1))
    if b>a:
        for i in range(0,b,a):
            list.append((x,y+i))
            list.append((x+a-1,y+i))
    return list
#将砖的点从墙上扣掉的函数
def removE(i,j,a,b,plot):
    for point in mesh(i,j,a,b):
        plot.remove(point)
    return plot
#砖的左下角顶点转化为坐标序号
def number(brick):
    return brick[0][0]+brick[0][1]*m
#坐标序号转化为坐标
def point(number):
    return (number%m,number//m)

option=[]
Plot=mesh(0,0,m,n)
#定义主函数
def tile(ans,k=t,plot=Plot):
    if k==0:
        option.append(ans.copy())
    else:
        for num in range(number(ans[t-k-1]),m*n):
            i,j=point(num)[0],point(num)[1]
            plot_1=plot.copy()
            plot_2=plot.copy()
            # 横向 #判断墙上是否可以取下一块砖
            if set(frame(i,j,a,b)).issubset(plot):
                #将砖坐标加入ans
                ans[t-k]=mesh(i,j,a,b)
                #在墙中删除砖坐标
                tile(ans,k-1,removE(i,j,a,b,plot_1))
            # 纵向
            if a!=b and set(frame(i,j,b,a)).issubset(plot):
                ans[t-k]=mesh(i,j,b,a)
                tile(ans,k-1,removE(i,j,b,a,plot_2))
                break
# 计时，主程序运行
import time
c=time.time()
tile([None]*(t-1)+[[(0,0)]])
d=time.time()
print("runtime:",d-c,"sec")
if len(option)==0:
	print("There is no option!")
	sys.exit()
#打印，可视化
print("The number of the options:",len(option)) 
p=int(input("Print how many?:"))
for (i,ans) in enumerate(option[:p]):
        print(i,":",ans)
        print("")
answer=option[int(input("Which option?"))]
#画图部分
import turtle
t=turtle.Turtle()
t.speed(0)
t.shape("blank")
def draw(tuple1,tuple2):
    a,b=20*(tuple1[0]-0.5-m/2),20*(tuple1[1]-0.5-n/2)
    c,d=20*(tuple2[0]+0.5-m/2),20*(tuple2[1]+0.5-n/2)
    t.penup()
    t.goto(a,b)
    t.pendown()#到达砖砖左下角的点开始绘图
    t.goto(c,b)
    t.goto(c,d)
    t.goto(a,d)
    t.goto(a,b)
for brick in answer:
    draw(brick[0],brick[-1])