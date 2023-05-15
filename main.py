import random as rnd
import matplotlib.pyplot as plt
import math

plt.ylim(-10,10)
plt.xlim(-10,10)

plt.gca().set_aspect('equal', adjustable='box')

print("Input number of repetitions")
n = int(input())
#number of point in the circle
p_in = 0
#number of all points
p_all = 0

Xvalues = [None]
Yvalues = [None]

XvaluesIN = [None]
YvaluesIN = [None]
for i in range(n):
    #generate random number
    x = rnd.uniform(-10,10)
    y = rnd.uniform(-10,10)

    if(i % 10 == 0):
        #write percentage
        percentage = (i*100)/n
        print(str(percentage) + " %")
    #check distance
    d = math.sqrt((x*x)+(y*y))
    if(d < 10):
        #set point
        #IN CIRCLE
        p_in += 1
        p_all += 1
        XvaluesIN.append(x)
        YvaluesIN.append(y)

    else:
        #set point
        #IN SQUARE
        p_all += 1
        Xvalues.append(x)
        Yvalues.append(y)

    
    if(len(XvaluesIN) > 5000000 or len(Xvalues) > 5000000):
        #after some time there might be to much RAM USSAGE
        print("scattering points IN TO PREVENT RAM OVERUSSAGE")
        plt.scatter(XvaluesIN,YvaluesIN,1,c='#ff0000')
        print("scattering points OUT TO PREVENT RAM OVERUSSAGE")
        plt.scatter(Xvalues,Yvalues,1,c='#00ff00')

        Xvalues = [None]
        Yvalues = [None]

        XvaluesIN = [None]
        YvaluesIN = [None]
        


print("scattering points IN")
plt.scatter(XvaluesIN,YvaluesIN,1,c='#ff0000')
print("scattering points OUT")
plt.scatter(Xvalues,Yvalues,1,c='#00ff00')
print("counting PI")
pi = (4 * p_in)/p_all
s = "PI" + str(pi)
plt.xlabel(s)
save_i = "S_REP_" + str(n) + ".png"
print("showing image")
plt.show()
print("saving image")
plt.savefig(save_i)
