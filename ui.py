import line1
import line2
import line3 
import bruteforce
import grahamscan
import jarvismarch
import quickelimination
import quickandgrahamcombine
import streamlit as st
st.title('Line Intersection and Convex Hull')
st.sidebar.title('Menu')
st.sidebar.write('Enter 1 for Intersection of  line and 2 for convexhull')
num = st.sidebar.number_input('',min_value=1,max_value=2)
if num==1:
    st.write('Intersection of Lines')
    st.write('enter 1 to find intersection by algebra')
    st.write('enter 2 to find intersection by Orientation')
    st.write('enter 3 to find intersection by Vectorisation')
    num = st.number_input('',min_value=1,max_value=3)
    if num==1:
        st.write('enter line one in this format (X1,Y1,X2,Y2)')
        lineone = st.text_input('')
        numbers = lineone[1:-1].split(',')
        lineone=tuple(map(int,numbers))
        
        st.write('enter line 2 in this format (X1,Y1,X2,Y2)')
        linetwo= st.text_input('')
        numbers = linetwo[1:-1].split(',')
        linetwo = tuple(map(int,numbers))
        intersection_point =   line1.find_intersection_point(lineone, linetwo)
        st.write("Intersection Point:", intersection_point)
        line1.plot_lines_and_intersection(lineone, linetwo, intersection_point)
    elif num==2:
         
         st.write('enter line one in this format (X1,Y1,X2,Y2)')
         line_input = st.text_input("Enter line in this format (X1, y1, x2, y2): ")
         numbers = line_input[1:-1].split(',')
         x1, y1, x2, y2 = map(float, numbers)
         point1 = line2.Point(x1, y1)
         point2 = line2.Point(x2, y2)
         line_input2 = st.text_input("Enter line in this format (X1, y1, x2, y2): ")
         numbers = line_input2[1:-1].split(',')
         x3, y3, x4, y4 = map(float, numbers)
         point3 = line2.Point(x3, y3)
         point4 = line2.Point(x4, y4)

         lineone = line2.Line(point1, point2)
         linetwo = line2.Line(point3, point4)
         line2.IntersectbyOrient(lineone,linetwo)
    elif num==3:
         st.write('enter line one in this format (X1,Y1,X2,Y2)')
         line_input = st.text_input("Enter line in this format (X1, y1, x2, y2): ")