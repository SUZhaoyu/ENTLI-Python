# ENTLI-Python
The Python scripts for ENTLI project preprocessing with ArcGIS.

## Prerequisite
ArcGIS should be properly installed, and all the scripts should be executed with the Python interpreter provided by ArcGIS. A typical directory for such interpreter: `C:\Python27\ArcGIS<version>\python.exe`.

The directory path in the scripts should be modified accordingly, **and special caution should be paid to the `del\S\Q` command. DOUBLE CONFIRM BEFORE EXECUTION ⚠️**

The hyper-parameters in the script shall not be modified. The coordinates for rectangle areas should be modified under `Hong_Kong_1980_Grid` coordinate system, only if users intend to change the training/testing area split.

## Script Description
**labels.py:** Converts `.shp` polygons into `.tif` rasters.

**clip.py:** Clips the raster data (including raw input and labels) by rectangle coordinates.
