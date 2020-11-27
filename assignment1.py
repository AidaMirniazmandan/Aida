print("Programming assignments - 03")
print("Author: Aida Mirniazmandan")
print("----------------------------\r")
A=input ("Enter the number of polygon points > 3: ")
P=int (A)
if P<4:
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
    x, y= [float(x) for x in input(message).split()]
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
  print("")
  print("Programming by Aida Mirniazmandan")
  k=0
  if sum<20 and sum>0:
     from tkinter import *  
     from tkinter import ttk  
     app=Tk()  
     f = open("data.txt", "r")
     app.title("BIM A+**Assignment 03**Aida Mirniazmandan")  
     name=ttk.Label(app, text=f.read())  
     name1=ttk.Label(app, text="Ax:     {:.2f}".format(sum))
     name2=ttk.Label(app, text="Sx:     {:.2f}".format(sum1))
     name3=ttk.Label(app, text="Sy:     {:.2f}".format(sum2))
     name4=ttk.Label(app, text="Ix:     {:.2f}".format(sum3))
     name5=ttk.Label(app, text="Iy:     {:.2f}".format(sum4))
     name6=ttk.Label(app, text="Ixy:    {:.2f}".format(sum5))
     name7=ttk.Label(app, text="xt:     {:.2f}".format(xt))
     name8=ttk.Label(app, text="yt:     {:.2f}".format(yt))
     name9=ttk.Label(app, text="Ixt:    {:.2f}".format(sum3-pow(yt,2)*sum))
     name10=ttk.Label(app,text="Iyt:    {:.2f}".format(sum4-pow(xt,2)*sum))
     name11=ttk.Label(app,text="Ixyt:   {:.2f}".format(sum5+xt*yt*sum))
     name.pack()  
     name1.pack()
     name2.pack() 
     name3.pack()
     name4.pack()
     name5.pack()
     name6.pack()
     name7.pack()
     name8.pack()
     name9.pack()
     name10.pack()
     name11.pack()
     canvas=Canvas(app)  
     canvas.pack()  
     canvas.config(width=800,height=600)  
     while k<le-1:
       xo=float(coordx[k])
       yo=float(coordy[k])
       xo1=float(coordx[k+1])
       yo1=float(coordy[k+1])
       x0=float(coordx[0])
       y0=float(coordy[0])
       xe=float(coordx[le-1])
       ye=float(coordy[le-1])
       k +=1
       H=50
       G=400
       M=180
       line=canvas.create_line((xo*H+M,(-yo*H+G)),(xo1*H+M,(-yo1*H+G)),fill='Blue',width=2)
       text=canvas.create_text((xo*H+M,(-yo*H+G)),fill="red",font="Times 20 italic bold",text="A{:.0f}".format(k))
     line=canvas.create_line((xe*H+M,(-ye*H+G)),(x0*H+M,(-y0*H+G)),fill='Blue',width=2)
     text=canvas.create_text((xe*H+M,(-ye*H+G)),fill="red",font="Times 20 italic bold",text="A{:.0f}".format(le)) 
     text=canvas.create_text((400,20),fill="blue",font="Times 12 italic bold",text="Programming By Aida Mirniazmandan") 
     app.mainloop()