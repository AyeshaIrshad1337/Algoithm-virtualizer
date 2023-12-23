import line1
import line2
import line3 
import bruteforce
import grahamscan
import jarvismarch
import quickelimination
import quickandgrahamcombine
import streamlit
print('enter 1 for Intersection of  line and 2 for convexhull')
num = int(input())
if num==1:
    print('Intersection of Lines')
    print('enter 1 to find intersection by algebra')
    print('enter 2 to find intersection by Orientation')
    print('enter 3 to find intersection by Vectorisation')
    num = int(input())
    if num==1:
        print('enter line one in this format (X1,Y1,X2,Y2)')
        lineone = input()
        numbers = lineone[1:-1].split(',')
        lineone=tuple(map(int,numbers))
        
        print('enter line 2 in this format (X1,Y1,X2,Y2)')
        linetwo= input()
        numbers = linetwo[1:-1].split(',')
        linetwo = tuple(map(int,numbers))
        intersection_point =   line1.find_intersection_point(lineone, linetwo)
        print("Intersection Point:", intersection_point)
        line1.plot_lines_and_intersection(lineone, linetwo, intersection_point)
    elif num==2:
         
         print('enter line one in this format (X1,Y1,X2,Y2)')
         line_input = input("Enter line in this format (X1, y1, x2, y2): ")
         numbers = line_input[1:-1].split(',')
         x1, y1, x2, y2 = map(float, numbers)
         point1 = line2.Point(x1, y1)
         point2 = line2.Point(x2, y2)
         line_input2 = input("Enter line in this format (X1, y1, x2, y2): ")
         numbers = line_input2[1:-1].split(',')
         x3, y3, x4, y4 = map(float, numbers)
         point3 = line2.Point(x3, y3)
         point4 = line2.Point(x4, y4)

         lineone = line2.Line(point1, point2)
         linetwo = line2.Line(point3, point4)
         line2.IntersectbyOrient(lineone,linetwo)
    elif num==3:
         print('enter line one in this format (X1,Y1,X2,Y2)')
         line_input = input("Enter line in this format (X1, y1, x2, y2): ")
         numbers = line_input[1:-1].split(',')
         x1, y1, x2, y2 = map(float, numbers)
         point1 = line3.Point(x1, y1)
         point2 = line3.Point(x2, y2)
         line_input2 = input("Enter line in this format (X1, y1, x2, y2): ")
         numbers = line_input2[1:-1].split(',')
         x3, y3, x4, y4 = map(float, numbers)
         point3 = line3.Point(x3, y3)
         point4 = line3.Point(x4, y4)

         lineone = line3.Line(point1, point2)
         linetwo = line3.Line(point3, point4)
         line3.Vectorisation(lineone,linetwo)
             
elif num==2:
    print('Finding Convex hull by points')
    print('enter 1 for Bruteforce')
    print('enter 2 for Grahamscan')
    print('enter 3 for jarvismarch')
    print('enter 4 for QuickElimination')
    print('enter 5 for Researchbased')
    num = int(input())
    if num==1:
        bruteforce.InputandStart()
    elif num==2:
        grahamscan.InputandStart()
    elif num==3:
        jarvismarch.InputandStart()
    elif num==4:
        quickelimination.InputandStart()
    elif num==5:
         quickandgrahamcombine.InputandStart()
                    