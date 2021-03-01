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

d = (x**2 + y**2) * 0.1
d2 = d ** 1 + 0.1
## precompute height values for all frames
phi = np.arange(0, 1.2, 1.2/300.)
z = (d[np.newaxis,...] + phi.reshape(phi.shape[0], 1, 1)) / d2[np.newaxis,...]
phase = 0

X = [0,0,0,0,0]
Angle = [0,0,0,0,0]
A = [0,0,0,0,0]
Finished = [False,False,False,False,False]
AllFinished = False



#Item 0
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [1.0,1.0],length=2)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m0 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m0.translate(0, 0, 0)
w.addItem(m0)

#Item 1
md = gl.MeshData.sphere(rows=50, cols=50,radius=1.0)
# colors = np.ones((md.faceCount(), 4), dtype=float)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S1 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S1.translate(0, 0, 2)
S1.setParentItem(m0)
w.addItem(S1)

#Item 2
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [1.0,1.0],length=2)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m2 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m2.setParentItem(S1)
m2.translate(0, 0, 0)
m2.rotate(90,1,0,0,True)
w.addItem(m2)


#Item 3
md = gl.MeshData.sphere(rows=50, cols=50,radius=1.0)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S2 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S2.setParentItem(m2)
S2.translate(0, 0, 2)
w.addItem(S2)

#Item 4
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [1.0,1.0],length=10)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m4 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m4.setParentItem(S2)
m4.rotate(-90,1,0,0,True)
w.addItem(m4)

#Item 5
md = gl.MeshData.sphere(rows=50, cols=50,radius=1.0)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S3 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S3.setParentItem(m4)
S3.translate(0, 0, 10)
w.addItem(S3)


#Item 6
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [1.0,1.0],length=2)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m6 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m6.translate(0, -2, 12)
m6.rotate(90,1,0,0,True)
m6.setParentItem(S3)
m6.translate(0, 4, -12)
w.addItem(m6)

#Item 7
md = gl.MeshData.sphere(rows=50, cols=50,radius=1.0)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S4 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S4.setParentItem(m6)
S4.translate(0, 0, 0)
w.addItem(S4)


#Item 8
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [1.0,1.0],length=10)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m8 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m8.translate(0, -2, 12)
m8.rotate(-90,1,0,0,True)
m8.setParentItem(S4)
m8.translate(0, 2, -12)
w.addItem(m8)


#Item 9
md = gl.MeshData.sphere(rows=50, cols=50,radius=1.0)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S5 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S5.setParentItem(m8)
S5.translate(0, 0, 10)
w.addItem(S5)


#Item 10
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [1.0,1.0],length=2)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m10 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m10.translate(0, -2, 12)
m10.rotate(-90,1,0,0,True)
m10.setParentItem(S5)
m10.translate(0, 0, -12)
w.addItem(m10)


#Item 11
md = gl.MeshData.sphere(rows=50, cols=50,radius=1.0)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S6 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S6.setParentItem(m10)
S6.translate(0, 0, 0)
w.addItem(S6)


#Item 12
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [1.0,1.0],length=2)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m12 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m12.translate(0, -2, 12)
m12.rotate(-90,1,0,0,True)
m12.setParentItem(S6)
m12.translate(0, 0, -12)
w.addItem(m12)


#Item 13
md = gl.MeshData.sphere(rows=50, cols=50,radius=1.0)
colors = np.ones((md.faceCount(), 4), dtype=float)
colors[::2,0] = 0
colors[:,2] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
S7 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
S7.setParentItem(m12)
S7.translate(0, 0, 0)
w.addItem(S7)

#Item 14
md = gl.MeshData.cylinder(rows= 50, cols= 50,radius= [1.0,0.0],length=3)
colors[::2,0] = 0
colors[:,1] = np.linspace(0, 1, colors.shape[0])
md.setFaceColors(colors)
m14 = gl.GLMeshItem(meshdata=md, smooth=False)#, shader='balloon')
m14.translate(0, -2, 12)
m14.rotate(-90,1,0,0,True)
m14.setParentItem(S7)
m14.translate(0, 2, -12)
w.addItem(m14)



def start():
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()


X[0] = int(input("Enter angle for motor 1: "))
X[1] = int(input("Enter angle for motor 2: "))
X[2] = int(input("Enter angle for motor 3: "))
X[3] = int(input("Enter angle for motor 4: "))
X[4] = int(input("Enter angle for motor 5: "))



def update():

    
    

    w.updateGL()
    m0.rotate(A[0],0,0,1,True)
    S1.rotate(A[1],0,1,0,True)
    S3.rotate(A[2],0,1,0,True)
    S5.rotate(A[3],0,1,0,True)
    S6.rotate(A[4],0,1,0,True)
    w.updateGL()
    print(Angle[0])
    print("Angle1")
    print(X[0])
    print("X0")
    
    
def UserInput():
    global Angle,AllFinished,X
    
    
    for x in range (5):
        if X[x] > 0:
            Angle[x] += X[x]/1000
            A[x] = X[x]/1000
            if Angle[x] > X[x]:
                A[x] = 0
                Finished[x] = True
        if X[x] < 0:
            Angle[x] += X[x]/1000
            A[x] = X[x] / 1000
            if Angle[x] < X[x]:
                A[x] = 0
                Finished[x] = True



    for x in range(5):
        AllFinished = True
        if Finished[x] == False:
            AllFinished = False
        if AllFinished == True:
            X[0] = int(input("Enter angle for motor 1: "))
            X[1] = int(input("Enter angle for motor 2: "))
            X[2] = int(input("Enter angle for motor 3: "))
            X[3] = int(input("Enter angle for motor 4: "))
            X[4] = int(input("Enter angle for motor 5: "))
            for x in range (5):
                Finished[x] = False
                Angle[x] = 0
    
    
     
    

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