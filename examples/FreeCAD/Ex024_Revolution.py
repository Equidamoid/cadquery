#File: Ex024_Revolution.py
#To use this example file, you need to first follow the "Using CadQuery From Inside FreeCAD"
#instructions here: https://github.com/dcowden/cadquery#installing----using-cadquery-from-inside-freecad

#You run this example by typing the following in the FreeCAD python console, making sure to change
#the path to this example, and the name of the example appropriately.
#import sys
#sys.path.append('/home/user/Downloads/cadquery/examples/FreeCAD')
#import Ex024_Revolution

#If you need to reload the part after making a change, you can use the following lines within the FreeCAD console.
#reload(Ex024_Revolution)

#You'll need to delete the original shape that was created, and the new shape should be named sequentially (Shape001, etc).

#You can also tie these blocks of code to macros, buttons, and keybindings in FreeCAD for quicker access.
#You can get a more information on this example at http://parametricparts.com/docs/examples.html#an-extruded-prismatic-solid

import cadquery
import Part

#The dimensions of the model. These can be modified rather than changing the shape's code directly.
rectangle_width = 15.0
rectange_length = 15.0
angleDegrees = 360.0

#Extrude a cylindrical plate with a rectangular hole in the middle of it
result = cadquery.Workplane("front").rect(rectangle_width, rectange_length).revolve(angleDegrees)

#Get a cadquery solid object
solid = result.val()

#Use the wrapped property of a cadquery primitive to get a FreeCAD solid
Part.show(solid.wrapped)

#Would like to zoom to fit the part here, but FreeCAD doesn't seem to have that scripting functionality
