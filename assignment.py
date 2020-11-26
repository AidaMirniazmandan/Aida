print("Programming assignments - 03")
print("Author: Aida Mirniazmandan")
print("----------------------------\r")
A=input ("Enter the number of polygon points: ")
P=int (A)
if P<3:
  print ("The number of polygon points is not valid")
else:
  print("Enter x and y coordinations for polygon points ...")
  print("Exmaple: Between X and Y is one space====> X Y")
  i = 1 
  f = open("data.txt", "w")
  f.write("                        \r")
  f.write("Point       x              y\r")
  f.write("---------------------------------\r")
  coordx=[]
  coordy=[]
  while i <= P:
    message = 'Point ' + str(i)  +': '
    x, y= [int(x) for x in input(message).split()]
    B= "{:.2f}".format(x)
    C= "{:.2f}".format(y)
    print("X is {} and Y is {}".format(x, y))
    i += 1
    coordx.append(B)
    coordy.append(C)
    f = open("data.txt", "a")
    f.write(str(i-1)+"           "+str(B)+"           "+str(C)+"      \r")
    f.close()
f = open("data.txt", "r")
print(f.read())
le= int(len(coordx))
j=0
sum=0
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
while j<le-1:
  x=float(coordx[j])
  x1=float(coordx[j+1])
  y=float(coordy[j])
  y1=float(coordy[j+1])
  S=0.5*((x+x1)*(y1-y))
  S1=(-1/6)*((x1-x)*(pow(y1,2)+(y*y1)+pow(y,2)))
  S2=(1/6)*((y1-y)*(pow(x1,2)+(x*x1)+pow(x,2)))
  S3=(-1/12)*((x1-x)*(pow(y1,3)+(pow(y1,2)*y)+(y1*pow(y,2))+pow(y,3)))
  S4=(1/12)*((y1-y)*(pow(x1,3)+(pow(x1,2)*x)+(x1*pow(x,2))+pow(x,3)))
  S5=(-1/24)*(y1-y)*(y1*(3*pow(x1,2))+2*x1*x+pow(x,2)+y*(3*pow(x,2)+2*x1*x+pow(x1,2)))
  j += 1
  sum = sum + float(S)
  sum1 = sum1 + float(S1)
  sum2 = sum2 + float(S2)
  sum3 = sum3 + float(S3)
  sum4 = sum4 + float(S4)
  sum5 = sum5 + float(S5)
print("Geometric characteristics:")  
print("Ax:         ","{:.2f}".format(sum))
print("Sx:         ","{:.2f}".format(sum1))
print("Sy:         ","{:.2f}".format(sum2))
print("Ix:         ","{:.2f}".format(sum3))
print("Iy:         ","{:.2f}".format(sum4))
print("Ixy:       ","{:.2f}".format(sum5))
xt=sum2/sum
print("xt:         ","{:.2f}".format(xt))
yt=sum1/sum
print("yt:         ","{:.2f}".format(yt))
print("Ixt:        ","{:.2f}".format(sum3-pow(yt,2)*sum))
print("Iyt:        ","{:.2f}".format(sum4-pow(xt,2)*sum))
print("Ixyt:       ","{:.2f}".format(sum5+xt*yt*sum))
print("Programming by Aida Mirniazmandan")