from geojson import FeatureCollection, Feature, Point
import csv
import json

features = []
csvpath = r'shanghai_10_6_305_test.csv'
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile, delimiter=',')
    for heading, _type, updatetime, lat, lon, mmsi, name, speed in reader:#需要和csv中数量对应
        # stalat, stalong = map(float,(StartLat, StartLong)) # start point
        # endlat, endlong = map(float,(EndLat, EndLong))    # end point
        features.append(
            Feature(
                geometry=Point((float(lon), float(lat))),
                properties={
                    'mmsi': mmsi,
                    'type': _type,
                    'updatetime': updatetime,
                    'hour': int(updatetime[11]),
                    'min': int(updatetime[13:]),
                    'heading': float(heading),
					'name': name,
                    'speed': float(speed)
                }
            )
        )


collection = FeatureCollection(features)
with open("shanghai_10_6_305_test.geojson", "w") as f:
    # f.write('%s' % collection + '\n')
    f.write(json.dumps(collection, sort_keys=False, indent=4))

#船只类型统计
# dict = {}
# for i in range(len(features)):
#     shiptype = features[i].properties['type']
#     if shiptype in dict:
#         dict[shiptype][1] = dict[shiptype][1] + 1
#     else:
#         dict[shiptype] = [shiptype, 1]
# print(sorted(dict.items(), key = lambda x:x[1][1], reverse = True))

#时间分布统计
# import datetime
# timelist = []
# hourlist = []
# minlist = []
# for i in range(len(features)):
#     time = features[i].properties['updatetime']
#     timelist.append(time[11:])
#     hourlist.append(time[11])
#     minlist.append(time[13:])
# print(hourlist)
# dict = {}
# for i in range(len(features)):
#     if hourlist[i] in dict:
#         dict[hourlist[i]][1] = dict[hourlist[i]][1] + 1
#     else:
#         dict[hourlist[i]] = [hourlist[i], 1]
# print(sorted(dict.items(), key = lambda x:x[1][1], reverse = True))