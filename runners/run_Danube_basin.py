from veget.vegetLib.vegetLib.veget import VegET
import os

"""
This runner was made on 9/21/2020 from Oct 2002-Dec 2019. This run is being done locally but more runs
 (for the Danube, Ganges-Bramaputra etc) will be run in the cloud if possible...
"""

config_root = r'C:\WaterSmart\Projects\VegET_Basins\Ganges'
shape_root = r'C:\WaterSmart\Projects\VegET_Basins\Ganges'

tile_lst = ['G1.shp', 'G2.shp', 'G3.shp', 'G4.shp', 'G5.shp', 'G6.shp']
# testing
# tile_lst = ['D4.shp']
config_list = ['D1', 'D2', 'D3', 'D4', 'D5', 'D6']
# testing
# config_list = ['D4']

for conf, tile in zip(config_list, tile_lst):
    tilename = tile.split('.')[0]
    shapefile = os.path.join(shape_root, tile)
    config_path = os.path.join(config_root, conf)

    veggie = VegET(veget_config_path=config_path,
                   tile=tilename,
                   shp=shapefile)
    veggie.run_veg_et()