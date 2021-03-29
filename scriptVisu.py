import pandas as pd
#Make a data frame with dots to show on the map
MTP = pd.DataFrame({
    'lat':[43.61620945549243,43.60969924926758,43.61465,43.6266977,43.6266977,43.6138841,43.57883,43.57926,43.5907,43.6157418],
    'lon':[3.874408006668091,3.896939992904663,3.8336,3.8956288,3.8956288,3.8684671,3.93324,3.93327,3.81324,3.9096322],
    'name':['Albert1er','Berracase','Celleneuve','Delmas1','Delmas2','Gerhardt','Lattes1','Lattes2','Laverure','VieillePoste'],
}, dtype = str)

MTP.tail(10)

import numpy as np
Totem = pd.DataFrame({
    'Albert1er':[692,501,1199,1215,1345,1270,1185,793,674,1337,1418,1211,1444,1160,884,645,1317,1453,1483,1457,1418,619,706,1312,1572,1539,1486,1496,837,683,1229,1543,1544,1657,1144,922,530,992,829,1382,758,1128,652,576,583,1056,1272,1308,1274,972,730,1664,1696,1667,1596,1747,1097,704,1441,1730,1826,1711,1670,1083,711,1462,1794,1823,1679,1554,1011,856,1641,1839,1907,1969],

    'Berracasa':[909,959,837,873,510,522,846,965,728,1034,1142,706,978,735,927,971,935,996,1020,1110,1037,409,1226,956,1231,1015,985,1034,712,1251,851,1072,1149,1301,694,1063,539,718,542,1368,516,868,554,790,387,948,1299,1194,1281,1357,1065,1312,1180,1163,1150,1305,1506,801,1165,1377,1513,1257,1211,1332,1157,971,1339,1169,1138,1034,1051,1379,1218,1406,1549,1530],

    'Celleneuve':[541,259,285,535,586,515,576,540,376,345,594,629,473,569,499,417,336,630,627,558,668,634,253,415,606,708,606,654,548,350,316,541727,637,678,468,383,273,442,379,549,282,436,290,299,238,472,566,471,578,410,336,722,754,577,746,676,499,300,623,757,743,673,632,444,348,643,677,641,688,615,452,342,664,737,761,783],

    'Delmas1':[332,217,524,551,548,609,592,376,366,586,615,475,612,468,446,326,565,623,566,611,641,281,330,621,677,598,606,644,361,376,545,658,654,659,468,441,232,424,318,620,276,448,300,313,249,508,576,538,600,431,338,682,698,696,747,7,532,300,639,711,761,740,725,499,356,638,737,687,714,612,518,406,660,780,729,807],

    'Delmas2':[59,50,70,37,65,54,58,55,36,56,40,39,42,47,55,62,58,53,38,49,58,64,70,59,63,43,63,57,59,55,70,56,58,22,56,47,67,47,57,33,30,39,60,69,63,60,74,51,56,82,85,56,82,85,56,58,78,49,57,55,56,21,76,85,69,89,61,55,67,65,64,58,91,46,77,72],

    'Gerhardt':[669,379,1108,1196,1208,1145,1111,660,416,1146,1277,1066,1156,1003,730,432,1172,1229,1191,1215,1210,553,455,1206,1343,1292,1204,1159,713,510,1126,1365,1236,1273,1028,735,378,775,773,953,647,810,553,386,502,903,921,968,935,707,470,1347,1415,1254,1392,1253,812,461,1273,1464,1358,1372,1294,87,502,1321,1460,1359,1297,1157,846,587,1306,1481,1332,1422],

    'Lattes1':[236,209,149,219,242,246,246,222,384,546,368,307,208,350,1,386,438,326,1,343,413,393,152,532,297,440,321,328,315,219,525,290,435,340,494,184,423,221,227,144,585,125,308,245,356,91,353,524,450,536,654,537,454,363,383,395,541,720,318,436,476,513,421,409,705,493,260,460,332,379,326,410,726,355,483,557],

    'Lattes2':[42,16,91,73,84,79,76,58,60,94,97,55,90,46,70,48,110,88,89,110,87,35,67,72,122,107,82,101,50,55,75,84,93,103,56,58,25,70,61,117,30,64,27,38,48,92,88,83,92,52,41,101,91,96,105,114,94,41,113,90,139,101,91,63,104,72,89,96,84,95,59,69,87,105,121,148],

    'Laverure':[193,128,252,126,174,146,148,123,130,160,138,140,144,139,87,294,305,186,224,88,78,261,326,155,0,206,126,0,437,120,318,200,194,152,132,382,142,266,227,300,86,233,117,54,42,130,147,285,43,311,245,277,349,294,198,289,221,210,383,195,325,268,159,328,292,126,244,175,228,147,268,428,130,294,312,316],

        'VieillePoste':[57,41,242,213,167,237,195,90,95,227,278,182,260,156,88,74,228,253,218,223,256,76,106,251,266,225,244,201,71,83,213,244,242,248,210,84,53,195,158,229,136,152,46,60,135,225,226,280,207,116,97,305,318,285,297,294,137,108,279,330,305,309,275,132,108,269,317,258,286,240,95,129,297,326,346,370]


    },dtype = str)


Totem['date'] = pd.date_range(start='02/04/2021', periods=len(Totem), freq='D')

Totem.tail(22)

import folium

Montpellier = [43.6100, 3.88888]
c= folium.Map(location=Montpellier,zoom_start=12.45)
#1
folium.Marker(location=[43.61620945549243,3.874408006668091],popup='Albert1er : 1291 bikes',tooltip='',icon=folium.Icon(color='pink',icon='heart')).add_to(c)
#2
folium.Marker(location=[43.60969924926758,3.896939992904663],popup='Berracasa : 1035 bikes',tooltip='',icon=folium.Icon(color='blue',icon='heart')).add_to(c)
#3
folium.Marker(location=[43.61465,3.8336],popup='Celleneuve : 553 bikes',tooltip='',icon=folium.Icon(color='green',icon='heart')).add_to(c)
#4
folium.Marker(location=[43.6266977,3.8956288],popup='Delmas1 : 565 bikes',tooltip='',icon=folium.Icon(color='orange',icon='heart')).add_to(c)
#5
folium.Marker(location=[43.6266977,3.8956288],popup='Delmas2 : 58 bikes',tooltip='',icon=folium.Icon(color='purple',icon='heart')).add_to(c)
#6
folium.Marker(location=[43.6138841,3.8684671],popup='Gerhardt : 1135 bikes',tooltip='',icon=folium.Icon(color='orange',icon='heart')).add_to(c)
#7
folium.Marker(location=[43.57883,3.93324],popup='Lattes1 : 359 bikes',tooltip='',icon=folium.Icon(color='red',icon='heart')).add_to(c)
#8
folium.Marker(location=[43.57926,3.93327],popup='Lattes2 : 84 bikes',tooltip='',icon=folium.Icon(color='black',icon='heart')).add_to(c)
#9
folium.Marker(location=[43.5907,3.81324],popup='Laverure : 194 bikes',tooltip='',icon=folium.Icon(color='lightgreen',icon='heart')).add_to(c)
#10
folium.Marker(location=[43.5907,3.81324],popup='Vieille Poste : 224 bikes',tooltip='',icon=folium.Icon(color='darkblue',icon='heart')).add_to(c)


display(c)

print(Totem.median())