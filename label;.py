# Name: PolygonToRaster_Ex_02.py
# Description: Converts polygon features to a raster dataset.

# Import system modules
import arcpy
from arcpy import env
import os
import traceback


#Delete old files:
print("Removing old files...")
# You need to change the path accordingly.
os.system("del/S/Q C:\Users\\tonysu\\Desktop\\ENTLI\\Master\\RasterLabels")
os.system("del/S/Q C:\Users\\tonysu\\Desktop\\ENTLI\\Master\\Temp")
# Set environment settings
env.workspace = "C:/Users/tonysu/Desktop/ENTLI/Master"

# Set local variables

valField = "FID"
assignmentType = "CELL_CENTER"
priorityField = "NONE"
cellSize = 0.5

try:
#Execute PolygonToRaster
    print('PolygonToRaster:')
    inFeatures = "ShapeLabels/Scars_main.shp"
    outRaster = "Temp/scars_temp.tif"
    arcpy.PolygonToRaster_conversion(inFeatures, valField, outRaster, 
                                     assignmentType, priorityField, cellSize)
    print('{} finished.'.format(inFeatures))

    inFeatures = "ShapeLabels/Holes.shp"
    outRaster = "Temp/holes_temp.tif"
    arcpy.PolygonToRaster_conversion(inFeatures, valField, outRaster, 
                                     assignmentType, priorityField, cellSize)
    print('{} finished.'.format(inFeatures))

    inFeatures = "ShapeLabels/Buildings.shp"
    outRaster = "Temp/buildings_temp.tif"
    arcpy.PolygonToRaster_conversion(inFeatures, valField, outRaster, 
                                     assignmentType, priorityField, cellSize)
    print('{} finished.'.format(inFeatures))

    inFeatures = "ShapeLabels/Building_Masks.shp"
    outRaster = "Temp/building_masks_temp.tif"
    arcpy.PolygonToRaster_conversion(inFeatures, valField, outRaster, 
                                     assignmentType, priorityField, cellSize)
    print('{} finished.'.format(inFeatures))

    print('Clipping:')

    
    outputExtent = "Images/before_2008.tif"
    RecTangle = "792061.000000 805074.000000 829048.500000 824415.500000"

    inputRaster = "Temp/scars_temp.tif"
    outputRaster = "RasterLabels/scars.tif"
    arcpy.Clip_management(inputRaster, RecTangle, outputRaster, outputExtent,
                          "0", "NONE", "MAINTAIN_EXTENT")
    print('{} finished.'.format(inputRaster))

    inputRaster = "Temp/holes_temp.tif"
    outputRaster = "RasterLabels/holes.tif"
    arcpy.Clip_management(inputRaster, RecTangle, outputRaster, outputExtent,
                          "0", "NONE", "MAINTAIN_EXTENT")
    print('{} finished.'.format(inputRaster))

    inputRaster = "Temp/buildings_temp.tif"
    outputRaster = "RasterLabels/buildings.tif"
    arcpy.Clip_management(inputRaster, RecTangle, outputRaster, outputExtent,
                          "0", "NONE", "MAINTAIN_EXTENT")
    print('{} finished.'.format(inputRaster))

    inputRaster = "Temp/building_masks_temp.tif"
    outputRaster = "RasterLabels/building_masks.tif"
    arcpy.Clip_management(inputRaster, RecTangle, outputRaster, outputExtent,
                          "0", "NONE", "MAINTAIN_EXTENT")
    print('{} finished.'.format(inputRaster))


    print("Process Completed!")
    os.system('pause')
except:
    traceback.print_exc() 
    os.system('pause')