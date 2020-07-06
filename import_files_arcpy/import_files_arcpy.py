import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")

# get the data frame
df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

#----------INSERINDO MAPEAMENTO DE USO--------------------------------------
#definindo mapa de entrada
map_vect=r"D:\____data\__GitRepositorios\repositorios_pythongis\arcpy\import_files_arcpy\dados/mapeamento_uso.shp"
# criando um novo layer
map_vect_obj= arcpy.mapping.Layer(map_vect)
# adicionando "mapeamento_uso.shp" no dataframe "CURRENT" no final da lista
arcpy.mapping.AddLayer(df, map_vect_obj,"BOTTOM")
#----------------------------------------------------------------------------

#----------INSERINDO MAPEAMENTO DE USO--------------------------------------
#definindo mapa de entrada
limite=r"D:\____data\__GitRepositorios\repositorios_pythongis\arcpy\import_files_arcpy\dados/limite.shp"
# criando um novo layer
limite_obj= arcpy.mapping.Layer(limite)
# adicionando "mapeamento_uso.shp" no dataframe "CURRENT" no final da lista
arcpy.mapping.AddLayer(df, limite_obj,"BOTTOM")
#----------------------------------------------------------------------------

#----------INSERINDO MAPEAMENTO DE USO--------------------------------------
#definindo mapa de entrada
landsat_tif=r"D:\____data\__GitRepositorios\repositorios_pythongis\arcpy\import_files_arcpy\dados/landsat.tif"
# criando um novo layer
landsat_tif_obj= arcpy.mapping.Layer(landsat_tif)
# adicionando "mapeamento_uso.shp" no dataframe "CURRENT" no final da lista
arcpy.mapping.AddLayer(df, landsat_tif_obj,"BOTTOM")
#----------------------------------------------------------------------------
