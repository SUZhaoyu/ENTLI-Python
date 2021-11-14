import arcpy
from arcpy import env
import os
import traceback

print("Removing old files...")
# os.system("del/S/Q C:\Users\\tonysu\\Desktop\\ENTLI\\Master\\RasterLabels")
# os.system("del/S/Q C:\Users\\tonysu\\Desktop\\ENTLI\\Master\\Temp")
os.system("del/S/Q C:\Users\\tonysu\\Desktop\\ENTLI\\Master\\Images\\raw_input\\train")
os.system("del/S/Q C:\Users\\tonysu\\Desktop\\ENTLI\\Master\\Images\\raw_input\\valid")
os.system("del/S/Q C:\Users\\tonysu\\Desktop\\ENTLI\\Master\\Images\\raw_input\\test")


print("Processing...")
env.workspace = "C:/Users/tonysu/Desktop/ENTLI/Master"

try:
	# Convert to Rasters
    # print("Converting polygons to rasters...")
    # arcpy.PolygonToRaster_conversion("ShapeLabels/Scars_main.shp", "FID", "Temp/Lantau_scars_temp.tif", 
    #                                  "CELL_CENTER", "NONE", 0.5)


    # Training Area

    
    print("Processing for training area...")
    print("Clipping...")
    
    arcpy.Clip_management(
        "Images/Lantau_later_RGB.tif","806975.650861 810070.633858 817203.966341 817341.971337",
        "Images/raw_input/train/posterior_RGB.tif", "SelectedZones/Training Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "Images/Lantau_former_RGB.tif","806975.650861 810070.633858 817203.966341 817341.971337",
        "Images/raw_input/train/prior_RGB.tif", "SelectedZones/Training Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "Images/Lantau_DTM.tif","806975.650861 810070.633858 817203.966341 817341.971337",
        "Images/raw_input/train/DTM.tif", "SelectedZones/Training Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "RasterLabels/Lantau_Scars.tif","806975.650861 810070.633858 817203.966341 817341.971337",
        "Images/raw_input/train/scars.tif", "SelectedZones/Training Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "RasterLabels/Lantau_Holes.tif","806975.650861 810070.633858 817203.966341 817341.971337",
        "Images/raw_input/train/void.tif", "SelectedZones/Training Area.shp", "0", "NONE", "MAINTAIN_EXTENT")


    
    # Validation Area
    print("Processing for validation area...")
    print("Clipping...")
    arcpy.Clip_management(
        "Images/Lantau_later_RGB.tif","802586.116884 811617.476207 806973.578209 815684.035101",
        "Images/raw_input/valid/posterior_RGB.tif", "SelectedZones/Validation Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "Images/Lantau_former_RGB.tif","802586.116884 811617.476207 806973.578209 815684.035101",
        "Images/raw_input/valid/prior_RGB.tif", "SelectedZones/Validation Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "Images/Lantau_DTM.tif","802586.116884 811617.476207 806973.578209 815684.035101",
        "Images/raw_input/valid/DTM.tif", "SelectedZones/Validation Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "RasterLabels/Lantau_Scars.tif","802586.116884 811617.476207 806973.578209 815684.035101",
        "Images/raw_input/valid/scars.tif", "SelectedZones/Validation Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "RasterLabels/Lantau_Holes.tif","802586.116884 811617.476207 806973.578209 815684.035101",
        "Images/raw_input/valid/void.tif", "SelectedZones/Validation Area.shp", "0", "NONE", "MAINTAIN_EXTENT")


    # Testing Area
    print("Processing for testing area...")
    print("Clipping...")
    arcpy.Clip_management(
        "Images/Lantau_later_RGB.tif","801446.249189 807108.644343 806975.408175 811617.476207",
        "Images/raw_input/test/posterior_RGB.tif", "SelectedZones/Testing Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "Images/Lantau_former_RGB.tif","801446.249189 807108.644343 806975.408175 811617.476207",
        "Images/raw_input/test/prior_RGB.tif", "SelectedZones/Testing Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "Images/Lantau_DTM.tif","801446.249189 807108.644343 806975.408175 811617.476207",
        "Images/raw_input/test/DTM.tif", "SelectedZones/Testing Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "RasterLabels/Lantau_Scars.tif","801446.249189 807108.644343 806975.408175 811617.476207",
        "Images/raw_input/test/scars.tif", "SelectedZones/Testing Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    arcpy.Clip_management(
        "RasterLabels/Lantau_Holes.tif","801446.249189 807108.644343 806975.408175 811617.476207",
        "Images/raw_input/test/void.tif", "SelectedZones/Testing Area.shp", "0", "NONE", "MAINTAIN_EXTENT")


    
    # arcpy.Clip_management(
    #     "Temp/Lantau_scars_temp.tif","801443.305260 806500.647480 806260.569176 814944.841629",
    #     "Images/Output/Scars_Valid.tif", "SelectedZones/Validation Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    # arcpy.Clip_management(
    #     "Images/Lantau_later_RGB.tif","801443.305260 806500.647480 806260.569176 814944.841629",
    #     "Images/Output/Valid_later_RGB.tif", "SelectedZones/Validation Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    # arcpy.Clip_management(
    #     "Images/Lantau_former_RGB.tif","801443.305260 806500.647480 806260.569176 814944.841629",
    #     "Images/Output/Valid_former_RGB.tif", "SelectedZones/Validation Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    # arcpy.Clip_management(
    #     "Images/Lantau_DTM.tif","801443.305260 806500.647480 806260.569176 814944.841629",
    #     "Images/Output/Valid_DTM.tif", "SelectedZones/Validation Area.shp", "0", "NONE", "MAINTAIN_EXTENT")
    # print("Resampling")
    # arcpy.Resample_management("Temp/Scars_Validation_temp.tif", "Images_output/Scars_Validation.tif", "0.5 0.5", "NEAREST")

    print("Process Completed!")
    os.system('pause')

except:
    traceback.print_exc() 
    os.system('pause')

