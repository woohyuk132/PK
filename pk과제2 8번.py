from pylab import plot, show
import math

tmax = (math.log(2.2)-math.log(0.18))/(2.2-0.18)
def min(a,b):
    return ((2.2*b/30.3)*((math.exp(-0.18*a)/(1-math.exp(-0.18*a)))-(math.exp(-2.2*a)/(1-math.exp(-2.2*a)))))

def max(a,b):
    return ((2.2*b/30.3)*((math.exp(-0.18*tmax)/(1-math.exp(-0.18*a)))-(math.exp(-2.2*tmax)/(1-math.exp(-2.2*a)))))

x = 0.1
while x <= 9:
    y=0
    while y <= 700:
        if min(x,y) >= 10 and max(x,y) <= 45:
            plot(x,y,'o',color='#7f7f7f')
        y += 10
    x += 0.1

show()
