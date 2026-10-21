from turtle import*
import colorsys
tracer(9)
h=1
bgcolor("yellow")
pensize(5)

for i in range(19):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    circle(19-i,90)
    lt(90)
    lt(20)
    circle(19-i,90)
    lt(50)
done()