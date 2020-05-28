import os
import json

from .log_logger import log_make_logger

LOG=log_make_logger('BOXY_THINGYS')

def box_make_poly(tile_name, increment=10):
    # example tile_name 40N-160E
    coord_list = []
    ul_lat = tile_name.split('N')[0]
    ul_lon = tile_name.split('N')[-1]
    ul_lon = ul_lon.split('E')[0] # remove the E for eastings
    ul_lat = int(ul_lat)
    ul_lon = int(ul_lon)
    ul_lon_lat = [ul_lon, ul_lat]
    ur_lon_lat = [ul_lon + increment, ul_lat]
    lr_lon_lat = [ul_lon + increment, ul_lat - increment]
    ll_lon_lat = [ul_lon, ul_lat - increment]

    coord_list.append(ul_lon_lat)
    coord_list.append(ur_lon_lat)
    coord_list.append(lr_lon_lat)
    coord_list.append(ll_lon_lat)
    coord_list.append(ul_lon_lat)

    return coord_list

def box_w_geojson(filename,polyc):
    geos = []

    poly = {
        'type': 'Feature',
        'properties': {},
        'geometry': {
            'type': 'Polygon',
            'coordinates': [polyc]
        }
    }
    geos.append(poly)

    geometries = {
        'type': 'FeatureCollection',
        'features': geos,
    }

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(geometries, f, ensure_ascii=False, indent=4)


def box_w_shape(geojson_filename):
    shp_filename = geojson_filename.split('.json')[0] + '.shp'
    print(geojson_filename,shp_filename)
    cmd='ogr2ogr -f \"ESRI Shapefile\" {} {}'.format(shp_filename, geojson_filename)
    os.system(cmd)


def box_create_ugly_proprietary_shapefile_plus_json_from_tile(temp_dir, tile):
    LOG.info('temp dir here is {}'.format(temp_dir))
