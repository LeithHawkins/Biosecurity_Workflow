# Set the necessary product code
import arcinfo


# Import arcpy module
import arcpy



# Local variables:
GIS101DELIVERY_RESTRICTED_DBO_BOUND_ADMIN_HOLDINGS__2_ = "GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS"
GIS101DELIVERY_RESTRICTED_DBO_BOUND_ADMIN_HOLDINGS__3_ = GIS101DELIVERY_RESTRICTED_DBO_BOUND_ADMIN_HOLDINGS__2_
GIS101DELIVERY_RESTRICTED_DBO_BOUND_ADMIN_HOLDINGS = GIS101DELIVERY_RESTRICTED_DBO_BOUND_ADMIN_HOLDINGS__3_
Workflow_gdb = "C:\\Users\\hawkinle\\Desktop\\STDTAS\\Workflow\\Data\\Workflow.gdb"
Selected_Holding = "C:\\Users\\hawkinle\\Desktop\\STDTAS\\Workflow\\Data\\Workflow.gdb\\Selected_Holding"
Buffer_1000 = "C:\\Users\\hawkinle\\Desktop\\STDTAS\\Workflow\\Data\\Workflow.gdb\\Buffer_1000"
Interesection_1km = "C:\\Users\\hawkinle\\Desktop\\STDTAS\\Workflow\\Data\\Workflow.gdb\\Interesection_1km"
Erased_Feature = "C:\\Users\\hawkinle\\Desktop\\STDTAS\\Workflow\\Data\\Workflow.gdb\\Erased_Feature"
Point_shp = "C:\\Users\\hawkinle\\Desktop\\STDTAS\\Workflow\\Data\\Point.shp"
Buffer_600 = "C:\\Users\\hawkinle\\Desktop\\STDTAS\\Workflow\\Data\\Workflow.gdb\\Buffer_600"
No_Bait_zone = "C:\\Users\\hawkinle\\Desktop\\STDTAS\\Workflow\\Data\\Workflow.gdb\\No_Bait_zone"
GIS101DELIVERY_RESTRICTED_DBO_LAND_OWN_PROPERTY = "C:\\Database_connections\\GIS101Delivery_Restricted.sde\\GIS101DELIVERY_RESTRICTED.DBO.LAND_OWN_PROPERTY"
LAND_OWN_PROPERTY_Clip = "C:\\Users\\hawkinle\\Documents\\ArcGIS\\Default.gdb\\LAND_OWN_PROPERTY_Clip"
LAND_OWN_PROPERTY_Clip_Disso = "C:\\Users\\hawkinle\\Documents\\ArcGIS\\Default.gdb\\LAND_OWN_PROPERTY_Clip_Disso"
Erased_Feature_Guras = "C:\\Users\\hawkinle\\Desktop\\STDTAS\\Workflow\\Data\\Workflow.gdb\\Erased_Feature_Guras"

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(GIS101DELIVERY_RESTRICTED_DBO_BOUND_ADMIN_HOLDINGS__2_, "NEW_SELECTION", "Holding_Reference_Number = 108091786")

# Process: Feature Class to Feature Class
arcpy.FeatureClassToFeatureClass_conversion(GIS101DELIVERY_RESTRICTED_DBO_BOUND_ADMIN_HOLDINGS__3_, Workflow_gdb, "Selected_Holding", "", "Holding_Reference_Number \"Holding_Reference_Number\" true true false 4 Long 0 10 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Holding_Reference_Number,-1,-1;Holding_Name \"Holding_Name\" true true false 255 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Holding_Name,-1,-1;Holding_Location_Address \"Holding_Location_Address\" true true false 457 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Holding_Location_Address,-1,-1;Local_Land_Services_Region_Id \"Local_Land_Services_Region_Id\" true true false 100 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Local_Land_Services_Region_Id,-1,-1;Local_Land_Services_Region_Name \"Local_Land_Services_Region_Name\" true true false 255 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Local_Land_Services_Region_Name,-1,-1;RLPB_Board_Name \"RLPB_Board_Name\" true true false 255 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,RLPB_Board_Name,-1,-1;Property_Identification_Code \"Property_Identification_Code\" true true false 255 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Property_Identification_Code,-1,-1;Occupier_Id \"Occupier_Id\" true true false 100 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Occupier_Id,-1,-1;Occupier_Full_Name \"Occupier_Full_Name\" true true false 255 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Occupier_Full_Name,-1,-1;Occupier_Mailing_Address \"Occupier_Mailing_Address\" true true false 457 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Occupier_Mailing_Address,-1,-1;Occupier_Home_Phone \"Occupier_Home_Phone\" true true false 320 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Occupier_Home_Phone,-1,-1;Occupier_Mobile_Phone \"Occupier_Mobile_Phone\" true true false 320 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Occupier_Mobile_Phone,-1,-1;Occupier_Email_Address \"Occupier_Email_Address\" true true false 320 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Occupier_Email_Address,-1,-1;Total_Area \"Total_Area\" true true false 8 Double 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Total_Area,-1,-1;Is_Rateable_Indicator \"Is_Rateable_Indicator\" true true false 1 Text 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Is_Rateable_Indicator,-1,-1;Rateable_Area \"Rateable_Area\" true true false 8 Double 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Rateable_Area,-1,-1;Nominal_Notional_Carrying_Cap \"Nominal_Notional_Carrying_Cap\" true true false 8 Double 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,Nominal_Notional_Carrying_Cap,-1,-1;SHAPE_STArea__ \"SHAPE_STArea__\" false true true 0 Double 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,SHAPE.STArea(),-1,-1;SHAPE_STLength__ \"SHAPE_STLength__\" false true true 0 Double 0 0 ,First,#,GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS,SHAPE.STLength(),-1,-1", "")

# Process: Buffer (2)
arcpy.Buffer_analysis(Selected_Holding, Buffer_1000, "1000 Meters", "FULL", "ROUND", "NONE", "", "PLANAR")

# Process: Select Layer By Attribute (2)
arcpy.SelectLayerByAttribute_management(GIS101DELIVERY_RESTRICTED_DBO_BOUND_ADMIN_HOLDINGS__3_, "CLEAR_SELECTION", "")

# Process: Intersect
arcpy.Intersect_analysis("C:\\Users\\hawkinle\\Desktop\\STDTAS\\Workflow\\Data\\Workflow.gdb\\Buffer_1000 #;GIS101DELIVERY_RESTRICTED.DBO.BOUND_ADMIN_HOLDINGS #", Interesection_1km, "ALL", "", "INPUT")

# Process: Erase
arcpy.Erase_analysis(Interesection_1km, Selected_Holding, Erased_Feature, "")

# Process: Buffer
arcpy.Buffer_analysis(Point_shp, Buffer_600, "600 Meters", "FULL", "ROUND", "NONE", "", "PLANAR")

# Process: Clip
arcpy.Clip_analysis(Selected_Holding, Buffer_600, No_Bait_zone, "")

# Process: Clip (2)
arcpy.Clip_analysis(GIS101DELIVERY_RESTRICTED_DBO_LAND_OWN_PROPERTY, Buffer_1000, LAND_OWN_PROPERTY_Clip, "")

# Process: Dissolve
arcpy.Dissolve_management(LAND_OWN_PROPERTY_Clip, LAND_OWN_PROPERTY_Clip_Disso, "GEO_LOCN_ID", "", "MULTI_PART", "DISSOLVE_LINES")

# Process: Erase (2)
arcpy.Erase_analysis(LAND_OWN_PROPERTY_Clip_Disso, Selected_Holding, Erased_Feature_Guras, "")

