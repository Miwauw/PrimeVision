# -*- coding: utf-8 -*-
"""
Simple examples demonstrating the use of GLMeshItem.

"""

## Add path to library (just for examples; you do not need this)


from pyqtgraph.Qt import QtCore, QtGui,QtWidgets 
import pyqtgraph.opengl as gl
import pyqtgraph as pg

import numpy as np
import sys
import math


app = QtGui.QApplication(sys.argv)
w = gl.GLViewWidget()
w.opts['distance'] = 40
w.setWindowTitle('pyqtgraph example: GLLinePlotItem')
w.setGeometry(0, 110, 1920, 1080)
w.show()



# create the background grids
gx = gl.GLGridItem()
gx.rotate(90, 0, 1, 0)
gx.translate(-20, 0, 20)
gx.scale(2,2,2)
w.addItem(gx)
gy = gl.GLGridItem()
gy.rotate(90, 1, 0, 0)
gy.translate(0, -20, 20)
gy.scale(2,2,2)
w.addItem(gy)
gz = gl.GLGridItem()
gz.translate(0, 0, 0)
gz.scale(2,2,2)
w.addItem(gz)


size = 200
x = np.linspace(-4, 4, size+1).reshape(size+1,1)
y = np.linspace(-4, 4, size+1).reshape(1,size+1)


Coordinate = [0,0,0]
X = [0,0,0,0,0,0]
Angle = [0,0,0,0,0,0]
A = [0,0,0,0,0,0]
Length = [1.273,6.120,5.723,1.639,1.157,0.922]
Am = [0,-0.6120,-0.5723,0,0,0]
Dm = [0.1273,0,0,0.1639,0.1157,0.0922]
Arad = [math.pi/2,0,0,math.pi/2,-math.pi/2,0]
JEndEffector = np.zeros((5,4,4))
Matrice = np.zeros((6,4,4))
Finished = [False,False,False,False,False,False]
AllFinished = False



#Item 0
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [.5,.5],length=Length[0])
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m0 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m0.translate(0, 0, 0)
w.addItem(m0)

#Item 1
md = gl.MeshData.sphere(rows=50, cols=50,radius=.5)
# colors = np.ones((md.faceCount(), 4), dtype=float)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S1 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S1.translate(0, 0, Length[0])
S1.setParentItem(m0)
w.addItem(S1)

#Item 2
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [.5,.5],length=1)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m2 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m2.setParentItem(S1)
m2.translate(0, 1, 0)
m2.rotate(90,1,0,0,True)
w.addItem(m2)


#Item 3
md = gl.MeshData.sphere(rows=50, cols=50,radius=.5)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S2 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S2.setParentItem(m2)
S2.translate(0, 0, 0)
w.addItem(S2)

#Item 4
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [.5,.5],length=Length[1])
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m4 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m4.setParentItem(S2)
m4.rotate(-90,0,1,0,True)
w.addItem(m4)

#Item 5
md = gl.MeshData.sphere(rows=50, cols=50,radius=.5)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S3 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S3.setParentItem(m4)
S3.translate(0, 0, Length[1])
w.addItem(S3)


#Item 6
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [.5,.5],length=1)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m6 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m6.translate(0, -1, Length[1]+1)
m6.rotate(90,0,1,0,True)
m6.setParentItem(S3)
m6.translate(0, 1, -(Length[1]+1))
w.addItem(m6)

#Item 7
md = gl.MeshData.sphere(rows=50, cols=50,radius=.5)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S4 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S4.setParentItem(m6)
S4.translate(0, 0, 1)
w.addItem(S4)


#Item 8
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [.5,.5],length=Length[2])
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m8 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m8.translate(0, -1, (Length[2]+1))
m8.rotate(-90,0,1,0,True)
m8.setParentItem(S4)
m8.translate(0, 1, -(Length[2]+1))
w.addItem(m8)


#Item 9
md = gl.MeshData.sphere(rows=50, cols=50,radius=.5)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S5 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S5.setParentItem(m8)
S5.translate(0, 0, Length[2])
w.addItem(S5)


#Item 9
md = gl.MeshData.sphere(rows=50, cols=50,radius=.5)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S20 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S20.translate(0, 0, 0)
w.addItem(S20)

# #Item 10
# md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [.5,.5],length=Length[3])
# colors[::2,0] = 0
# colors[:,1] = np.linspace(0, 1, colors.shape[0])
# md.setFaceColors(colors)
# m10 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
# m10.translate(0, 0, (Length[2]+1))
# m10.rotate(90,0,1,0,True)
# m10.setParentItem(S5)
# m10.translate(0, 0, -(Length[2]+1))
# w.addItem(m10)


# #Item 11
# md = gl.MeshData.sphere(rows=50, cols=50,radius=.5)
# colors = np.ones((md.faceCount(), 4), dtype=float)
# colors[::2,0] = 0
# colors[:,2] = np.linspace(0, 1, colors.shape[0])
# md.setFaceColors(colors)
# S6 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
# S6.setParentItem(m10)
# S6.translate(0, 0, Length[3])
# w.addItem(S6)


# #Item 12
# md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [.5,.5],length=Length[4])
# colors[::2,0] = 0
# colors[:,1] = np.linspace(0, 1, colors.shape[0])
# md.setFaceColors(colors)
# m12 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
# m12.translate(0, -1, (Length[2]+1))
# m12.rotate(-90,1,0,0,True)
# m12.setParentItem(S6)
# m12.translate(0, 0, -(Length[2]+1))
# w.addItem(m12)


# #Item 13
# md = gl.MeshData.sphere(rows=50, cols=50,radius=.5)
# colors = np.ones((md.faceCount(), 4), dtype=float)
# colors[::2,0] = 0
# colors[:,2] = np.linspace(0, 1, colors.shape[0])
# md.setFaceColors(colors)
# S7 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
# S7.setParentItem(m12)
# S7.translate(0, 0, 0)
# w.addItem(S7)

# #Item 14
# md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [.5,0.0],length=Length[5])
# colors[::2,0] = 0
# colors[:,1] = np.linspace(0, 1, colors.shape[0])
# md.setFaceColors(colors)
# m14 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
# m14.translate(0, -1, (Length[2]+1))
# m14.rotate(90,1,0,0,True)
# m14.setParentItem(S7)
# m14.translate(0, 1, -(Length[2]+1))
# w.addItem(m14)


# #Item 15
# md = gl.MeshData.sphere(rows=50, cols=50,radius=.5)
# colors = np.ones((md.faceCount(), 4), dtype=float)
# colors[::2,0] = 0
# colors[:,2] = np.linspace(0, 1, colors.shape[0])
# md.setFaceColors(colors)
# S8 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
# w.addItem(S8)


def Inverse(X,Y,Z):
    global Lenght
    A = Length[2]
    B = Length[1]
    C = math.sqrt( (math.sqrt((X**2)+(Y**2)))**2    +   (Z - Length[0])**2 )
    a = math.degrees(math.acos( ((A**2) + (B**2) - (C**2)) / (2*A*B) ))
    b = math.degrees(math.acos( ((B**2) + (C**2) - (A**2)) / (2*B*C) ))
    c = math.degrees(math.acos( ((C**2) + (A**2) - (B**2)) / (2*A*C) ))
    Phi_1 = math.degrees(math.atan( (Z-Length[0]) / math.sqrt((X**2) + (Y**2)) )) + b
    Phi_2 = 180 - a
    if Y >= 0:
        Phi_Angle =  math.degrees(math.atan(Y/X))
    if Y < 0:
        Phi_Angle =  math.degrees(math.atan(Y/X)) + 180
        if Phi_Angle > 180:
            Phi_Angle =  (math.degrees(math.atan(Y/X)) + 180) - 360
    return -Phi_1,Phi_2,Phi_Angle+90 




def Cube(L,W,D):
    vertexes = np.array([[D, 0, 0], #0
                         [0, 0, 0], #1
                         [0, W, 0], #2
                         [D, W, 0], #3
                         [D, 0, L], #4
                         [0, 0, L], #5
                         [0, W, L], #6
                         [D, W, L]])#7
    faces = np.array([[1,5,4], [1,0,4],
                      [1,5,6], [1,2,6],
                      [1,2,3], [1,0,3],
                      [7,3,0], [7,4,0],
                      [7,6,2], [7,3,2],
                      [7,6,5], [7,4,5]])
    colors = np.array([[1,0,0,1] for i in range(12)])
    cube = gl.GLMeshItem(vertexes=vertexes, faces=faces, faceColors=colors, drawEdges=True, edgeColor=(0, 0, 0, 1))
    return cube


# #Stelling
# Q1 = Cube(12,1,1)
# Q1.translate(-5,-4,0)
# w.addItem(Q1)

# Q2 = Cube(12,1,1)
# Q2.translate(-5,4,0)
# w.addItem(Q2)

# Q3 = Cube(12,1,1)
# Q3.translate(-10,-4,0)
# w.addItem(Q3)

# Q4 = Cube(12,1,1)
# Q4.translate(-10,4,0)
# w.addItem(Q4)

# Q5 = Cube(0.5,9,6)
# Q5.translate(-10,-4,6)
# w.addItem(Q5)

# Q5 = Cube(0.5,9,6)
# Q5.translate(-10,-4,12)
# w.addItem(Q5)

# Q6 = Cube(0.5,9,6)
# Q6.translate(-10,-4,0)
# w.addItem(Q6)

#######################################################



def start():
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()



Coordinate[0] = int(input("X Coordinate: "))
Coordinate[1] = int(input("Y Coordinate: "))
Coordinate[2] = int(input("Z Coordinate: "))

X[1],X[2],X[0] = Inverse(Coordinate[0],Coordinate[1],Coordinate[2])
print(X[1],X[2],X[0])
S20.translate(Coordinate[0], Coordinate[1], Coordinate[2])

# X[0] = int(input("Enter angle for motor 1: "))
# X[1] = int(input("Enter angle for motor 2: "))
# X[2] = int(input("Enter angle for motor 3: "))
# X[3] = int(input("Enter angle for motor 4: "))
# X[4] = int(input("Enter angle for motor 5: "))
# X[5] = int(input("Enter angle for motor 6: "))



def update():
    w.updateGL()
    m0.rotate(-A[0],0,0,1,True)
    S1.rotate(-A[1],0,1,0,True)
    S3.rotate(A[2],1,0,0,True)

    # S5.rotate(A[3],1,0,0,True)
    # S6.rotate(-A[4],0,1,0,True)
    # S7.rotate(A[5],0,1,0,True)
    

    for x in range (6):
        global JEndEffector
        Matrice[x,0,0] = math.cos(math.radians(Angle[x]))
        Matrice[x,0,1] = -math.sin(math.radians(Angle[x])) * math.cos(Arad[x])
        Matrice[x,0,2] = math.sin(math.radians(Angle[x])) * math.sin(Arad[x])
        Matrice[x,0,3] = Am[x] * math.cos(math.radians(Angle[x]))
        
        Matrice[x,1,0] = math.sin(math.radians(Angle[x]))
        Matrice[x,1,1] = math.cos(math.radians(Angle[x])) * math.cos(Arad[x])
        Matrice[x,1,2] = -math.cos(math.radians(Angle[x])) * math.sin(Arad[x])
        Matrice[x,1,3] = Am[x] * math.sin(math.radians(Angle[x]))
        
        Matrice[x,2,0] = 0
        Matrice[x,2,1] = math.sin(Arad[x])
        Matrice[x,2,2] = math.cos(Arad[x])
        Matrice[x,2,3] = Dm[x]
        
        Matrice[x,3,0] = 0
        Matrice[x,3,1] = 0
        Matrice[x,3,2] = 0
        Matrice[x,3,3] = 1

        JEndEffector = np.zeros((5,4,4))
        
        for i in range(4):
           # iterate through columns of Y
           for j in range(4):
               # iterate through rows of Y
               for k in range(4):
                   JEndEffector[0][i][j] += Matrice[0][i][k] * Matrice[1][k][j]
                   
        for h in range(4):
            for i in range(4):
           # iterate through columns of Y
               for j in range(4):
                   # iterate through rows of Y
                   for k in range(4):
                       JEndEffector[h+1][i][j] += JEndEffector[h][i][k] * Matrice[h+2][k][j]
                       
        # S8.translate((10*JEndEffector[4,0,3]), (10*JEndEffector[4,1,3]), (10*JEndEffector[4,2,3]))
        
        
        # print("EndEffector coordinates")
        # print(10*JEndEffector[4,0,3])
        # print(10*JEndEffector[4,1,3])
        # print(10*JEndEffector[4,2,3])
        # w.updateGL()
        # S8.translate(-(10*JEndEffector[4,0,3]), -(10*JEndEffector[4,1,3]), -(10*JEndEffector[4,2,3]))


    
def UserInput():
    global Angle,AllFinished,X
    for x in range (6):
        if X[x] > 0:
            Angle[x] += X[x]/500
            A[x] = X[x]/500
            if Angle[x] > X[x]:
                A[x] = 0
                Finished[x] = True
        if X[x] < 0:
            Angle[x] += X[x]/500
            A[x] = X[x] / 500
            if Angle[x] < X[x]:
                A[x] = 0
                Finished[x] = True


    for x in range(6):
        AllFinished = True
        if Finished[x] == False:
            AllFinished = False
        if AllFinished == True:
            
            S20.translate(-Coordinate[0], -Coordinate[1], -Coordinate[2])
            Coordinate[0] = int(input("X Coordinate: "))
            Coordinate[1] = int(input("Y Coordinate: "))
            Coordinate[2] = int(input("Z Coordinate: "))
            
            X[1],X[2],X[0] = Inverse(Coordinate[0],Coordinate[1],Coordinate[2])
            S20.translate(Coordinate[0], Coordinate[1], Coordinate[2])
            print(X[1],X[2],X[0])
            

            
 


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.timeout.connect(UserInput)
timer.start(30)
start()



# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':

    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()