class Node:
 
  def __init__(self,item = 0):
    self.key = item
    self.left,self.right = None,None
 
 
# Root of BST
root = Node()
 
root = None
 
# This method mainly
# calls insertRec()
def insert(key):
  global root
  root = insertRec(root, key)
 
# A recursive function to
# insert a new key in BST
def insertRec(root, key):
 
  # If the tree is empty,
  # return a new node
 
  if (root == None):
    root = Node(key)
    return root
 
  # Otherwise, recur
  # down the tree
  if (key < root.key):
    root.left = insertRec(root.left, key)
  elif (key > root.key):
    root.right = insertRec(root.right, key)
 
  # return the root
  return root
 
# A function to do
# inorder traversal of BST
def inorderRec(root):
  if (root != None):
    inorderRec(root.left)
    print(root.key ,end = " ")
    inorderRec(root.right)
   
def treeins(arr):
  for i in range(len(arr)):
    insert(arr[i])
 
# Driver Code
arr = [69, 853, 118, 774, 1106, 29, 797, 1171, 1441, 816, 519, 1631, 263, 1353, 626, 163, 1155, 1126, 23, 1234, 1001, 838, 1079, 1657, 1598, 17, 251, 1747, 1180, 1233, 80, 896, 1138, 367, 1554, 1004, 1411, 693, 528, 1591, 581, 1284, 285, 512, 484, 455, 869, 531, 1094, 199, 1115, 764, 7, 1242, 269, 1694, 1520, 282, 1967, 505, 414, 567, 1710, 1226, 1360, 1368, 1062, 1986, 1968, 666, 1258, 723, 1013, 686, 1501, 1315, 1684, 1227, 620, 897, 931, 974, 363, 1575, 925, 1301, 1536, 83, 144, 1400, 1567, 1941, 194, 855, 127, 1323, 1983, 1815, 1579, 1621, 694, 1585, 1609, 1032, 71, 1101, 130, 1835, 926, 1506, 614, 1117, 1901, 177, 1646, 1257, 351, 328, 1966, 840, 1653, 861, 1586, 38, 636, 1933, 1273, 757, 603, 1075, 1033, 642, 1665, 1810, 310, 753, 1857, 629, 407, 785, 157, 1658, 1072, 794, 1866, 1251, 1961, 146, 436, 26, 1281, 49, 1926, 543, 1316, 1128, 1860, 1652, 1024, 929, 818, 1837, 430, 893, 1153, 313, 1204, 641, 1975, 1849, 185, 660, 604, 1836, 186, 1334, 857, 563, 52, 1332, 1798, 1565, 1344, 1497, 59, 1879, 645, 507, 968, 1080, 268, 1196, 13, 93, 188, 1366, 1699, 1398, 239, 449, 472, 1594, 1254, 1098, 793, 1753, 852, 1016, 728, 1455, 1696, 1139, 224, 733, 921, 470, 615, 671, 1086, 826, 1546, 1863, 1840, 139, 876, 628, 1377, 129, 1112, 1317, 971, 1116, 1760, 104, 1629, 1346, 1561, 1044, 918, 1465, 275, 1917, 1786, 1246, 1130, 113, 1152, 1958, 1170, 1913, 1599, 81, 1187, 281, 485, 1600, 1107, 1888, 1496, 1754, 1394, 651, 950, 1091, 1637, 1829, 1868, 1061, 1005, 64, 1737, 532, 1438, 1198, 1812, 1951, 836, 1531, 1819, 502, 1396, 717, 1691, 683, 359, 384, 621, 471, 76, 632, 264, 843, 315, 595, 1125, 1476, 587, 534, 768, 1239, 1589, 1851, 1154, 1820, 1310, 1792, 1650, 486, 630, 1992, 1479, 1372, 443, 755, 1147, 524, 558, 1450, 650, 1504, 1256, 892, 705, 997, 1280, 584, 226, 260, 89, 438, 1105, 940, 316, 410, 746, 399, 1029, 322, 673, 389, 707, 1238, 821, 1046, 1453, 508, 1087, 1996, 77, 1484, 1192, 510, 318, 227, 675, 1738, 721, 1403, 606, 731, 1775, 739, 11, 304, 736, 99, 882, 839, 361, 1184, 1512, 257, 613, 758, 1003, 45, 530, 713, 1030, 452, 823, 183, 1887, 1404, 374, 63, 31, 1241, 1290, 1193, 439, 1744, 1218, 1947, 248, 1164, 1502, 935, 1113, 996, 644, 1040, 236, 159, 835, 1692, 444, 167, 1499, 520, 1745, 1871, 916, 437, 582, 152, 748, 523, 960, 1841, 799, 253, 562, 1026, 655, 235, 1937, 1743, 1777, 812, 977, 1456, 611, 190, 1899, 1787, 722, 1838, 1513, 347, 1647, 1898, 659, 1977, 1801, 844, 1288, 542, 394, 1449, 781, 237, 769, 464, 154, 60, 1733, 1111, 749, 1580, 1210, 496, 846, 141, 1225, 661, 85, 1391, 715, 919, 910, 1839, 1759, 500, 1853, 822, 1577, 1808, 1103, 599, 379, 479, 588, 1864, 1667, 138, 187, 1347, 1077, 1988, 600, 1896, 612, 988, 1905, 750, 463, 254, 1017, 1388, 740, 1200, 58, 1613, 295, 405, 1842, 1278, 1492, 854, 133, 653, 1785, 1025, 880, 1869, 1463, 1041, 1610, 346, 1664, 461, 314, 688, 1142, 837, 397, 1099, 1891, 1165, 884, 1179, 815, 966, 1511, 336, 87, 1488, 338, 466, 135, 1047, 1336, 1491, 1249, 1050, 1960, 24, 1740, 1470, 1337, 296, 1374, 1467, 432, 1642, 647, 306, 18, 330, 1440, 1780, 1583, 1701, 751, 1772, 451, 392, 1984, 776, 1749, 789, 1177, 573, 1222, 360, 225, 1803, 35, 1766, 213, 1410, 362, 564, 1515, 1295, 4, 981, 333, 1547, 1015, 1329, 709, 701, 1659, 859, 1855, 937, 1709, 1822, 1885, 1936, 535, 1686, 446, 1188, 160, 1313, 1418, 1661, 1660, 1569, 678, 350, 964, 434, 1949, 1185, 556, 450, 61, 672, 400, 1219, 1327, 1417, 887, 811, 1603, 766, 1230, 967, 545, 759, 78, 754, 406, 1651, 1244, 1636, 1910, 800, 1286, 1999, 1980, 42, 357, 619, 1228, 895, 539, 124, 1049, 98, 206, 1739, 1059, 1416, 777, 1900, 1971, 1955, 108, 514, 735, 279, 1021, 788, 685, 106, 708, 548, 311, 284, 232, 283, 1205, 465, 1592, 1494, 169, 57, 1544, 1897, 145, 317, 1556, 1473, 1503, 1308, 1669, 623, 597, 301, 90, 729, 1573, 1525, 1022, 536, 1012, 230, 1120, 711, 331, 1172, 703, 924, 1962, 182, 517, 637, 1263, 689, 54, 787, 91, 1073, 216, 1624, 355, 382, 1508, 271, 205, 343, 762, 1471, 1454, 1720, 975, 1439, 1946, 1432, 1943, 1423, 1203, 494, 68, 242, 1084, 1908, 657, 1266, 1201, 170, 1711, 1640, 866, 3, 1954, 6, 756, 1190, 1890, 1844, 1216, 1712, 1677, 1136, 1953, 427, 1673, 1924, 1874, 1533, 1123, 1607, 627, 979, 1078, 1302, 1963, 1929, 1543, 1732, 1335, 865, 1058, 193, 652, 1909, 1159, 1035, 1157, 814, 1023, 712, 795, 1389, 1550, 15, 79, 1276, 593, 513, 335, 501, 27, 1314, 1826, 416, 1847, 810, 1068, 662, 1830, 278, 339, 1867, 1805, 74, 1509, 1178, 1761, 1297, 1183, 25, 1320, 1833, 1889, 352, 431, 537, 103, 738, 834, 1312, 1794, 576, 915, 1564, 458, 447, 419, 1262, 533, 47, 1250, 858, 1292, 454, 1199, 1054, 40, 128, 1383, 1870, 972, 697, 158, 334, 1705, 1816, 219, 1370, 908, 899, 959, 241, 829, 1892, 726, 324, 752, 32, 1379, 1588, 469, 1356, 97, 1615, 1325, 770, 150, 598, 819, 544, 856, 803, 1593, 1283, 1872, 1813, 1275, 1763, 527, 1085, 1255, 596, 550, 498, 1264, 639, 1097, 368, 198, 1042, 265, 1486, 1823, 1923, 610, 200, 39, 1505, 763, 1832, 572, 180, 1670, 1672, 1475, 1236, 480, 1722, 161, 1702, 1299, 1355, 1976, 809, 1373, 132, 646, 1195, 515, 796, 453, 376, 1141, 594, 1462, 1197, 1655, 1354, 448, 1979, 1818, 590, 1480, 478, 1055, 702, 1294, 371, 1734, 1451, 84, 115, 727, 286, 321, 1419, 546, 1630, 1854, 1376, 204, 649, 1168, 176, 1676, 1207, 690, 1291, 348, 1287, 1790, 487, 1298, 1151, 28, 1526, 879, 547, 1306, 1715, 386, 1845, 1904, 592, 1605, 695, 1421, 1048, 149, 1518, 938, 126, 1162, 421, 1144, 1289, 1548, 395, 1634, 1765, 1597, 566, 565, 1552, 706, 445, 489, 1922, 218, 401, 1748, 680, 201, 62, 342, 387, 1721, 969, 120, 1969, 1528, 1043, 1537, 1719, 696, 1067, 830, 1648, 1345, 993, 934, 441, 172, 775, 923, 0, 37, 1119, 1535, 791, 238, 922, 490, 1688, 1135, 440, 1232, 1420, 1167, 714, 1433, 1100, 877, 941, 274, 94, 1507, 509, 1124, 364, 917, 1928, 1682, 1285, 1319, 953, 1311, 1581, 1070, 1321, 1240, 1557, 687, 1639, 1563, 1680, 634, 1442, 983, 140, 677, 1534, 909, 234, 300, 1260, 987, 162, 1752, 1270, 197, 907, 1156, 72, 1572, 155, 1914, 222, 1595, 1477, 273, 1365, 356, 860, 827, 1474, 1974, 1724, 1814, 412, 1935, 1401, 1791, 1859, 506, 540, 965, 156, 220, 1340, 1981, 1102, 1683, 396, 900, 734, 1472, 1726, 920, 1608, 214, 828, 944, 1945, 1614, 460, 1036, 111, 1985, 51, 737, 1549, 973, 1751, 1862, 211, 1371, 1269, 1735, 780, 1104, 699, 1395, 1333, 1940, 1811, 1920, 1606, 136, 1700, 1300, 664, 372, 1375, 366, 1243, 1911, 529, 1517, 53, 602, 792, 340, 462, 1957, 955, 33, 1742, 327, 1799, 1882, 579, 902, 1330, 1407, 1545, 122, 1018, 1989, 1846, 30, 525, 570, 1666, 1689, 905, 747, 1906, 1088, 481, 1802, 457, 560, 589, 888, 1530, 1678, 871, 100, 165, 1131, 958, 1028, 933, 1852, 1723, 277, 760, 1769, 228, 1140, 1495, 215, 1448, 244, 1057, 608, 1948, 1405, 1880, 1668, 963, 349, 1995, 246, 151, 1132, 1930, 1654, 798, 551, 119, 622, 48, 320, 233, 329, 1529, 50, 1931, 173, 1774, 1727, 1341, 743, 1542, 435, 261, 1357, 1237, 1993, 1014, 605, 1768, 1817, 991, 1679, 943, 1532, 824, 1641, 1382, 957, 1997, 1741, 1362, 1827, 832, 848, 477, 1108, 1956, 885, 255, 1490, 8, 951, 1378, 607, 65, 1424, 1604, 1555, 1964, 586, 88, 555, 511, 670, 1381, 1959, 1858, 932, 1783, 1797, 1331, 998, 1725, 259, 1611, 1426, 1010, 1083, 804, 365, 1894, 1972, 962, 1991, 262, 945, 1212, 1215, 1252, 1431, 516, 1481, 428, 1093, 1145, 1245, 1982, 12, 1865, 1415, 1096, 1414, 209, 1209, 1487, 1523, 1127, 171, 1562, 820, 1406, 1987, 388, 773, 1163, 745, 1831, 1428, 109, 995, 992, 741, 1878, 638, 1174, 1092, 1466, 779, 1397, 616, 1779, 378, 166, 1146, 1850, 1825, 1069, 1729, 1469, 287, 1457, 1387, 402, 398, 353, 521, 223, 849, 1539, 202, 1305, 609, 110, 575, 1186, 1782, 147, 1649, 174, 930, 1081, 326, 1587, 210, 1796, 1633, 665, 112, 1027, 418, 1182, 574, 1221, 1191, 95, 1903, 1821, 1482, 1809, 1326, 1307, 585, 411, 221, 377, 806, 633, 429, 391, 1767, 648, 299, 1884, 1784, 189, 272, 114, 1181, 207, 358, 928, 1443, 1148, 1459, 643, 308, 1519, 497, 1912, 1541, 1731, 1717, 467, 1143, 1662, 142, 1434, 1425, 1109, 1446, 1452, 847, 1915, 1718, 1876, 1385, 1427, 946, 1628, 1698, 303, 873, 1361, 552, 825, 1500, 1211, 802, 1773, 499, 952, 1350, 1447, 1848, 1762, 1674, 1217, 1063, 1620, 663, 1461, 212, 1045, 904, 1095, 294, 1268, 541, 307, 1220, 44, 1938, 1750, 710, 1527, 580, 890, 1412, 1934, 1343, 1110, 1804, 631, 1161, 1800, 491, 1944, 518, 55, 554, 82, 413, 961, 985, 1483, 1020, 984, 1687, 1778, 123, 805, 1369, 1703, 1590, 148, 483, 179, 784, 1364, 1114, 989, 341, 1514, 872, 1644, 549, 1384, 1367, 1788, 1622, 1133, 1834, 164, 716, 1444, 654, 1510, 1009, 22, 765, 724, 1916, 476, 676, 719, 1707, 978, 1413, 947, 1770, 867, 1566, 1570, 153, 889, 196, 1965, 863, 625, 1274, 203, 1643, 325, 504, 618, 601, 1576, 914, 1248, 240, 1485, 1259, 1214, 1601, 1602, 1627, 1730, 868, 990, 841, 1524, 559, 1303, 34, 761, 1806, 1626, 1056, 1363, 1907, 682, 1656, 1693, 1758, 1736, 417, 1776, 474, 912, 720, 668, 1380, 1002, 403, 267, 1282, 1359, 20, 1011, 245, 252, 790, 813, 911, 1795, 1090, 1675, 1522, 442, 332, 1789, 423, 473, 1757, 976, 1039, 999, 247, 488, 290, 1574, 373, 1253, 1582, 1713, 298, 288, 1129, 5, 337, 1089, 354, 1279, 817, 1695, 883, 1568, 117, 369, 936, 982, 1521, 1224, 772, 1781, 1064, 143, 1690, 1645, 635, 1540, 591, 732, 1873, 1296, 433, 913, 1489, 1942, 1000, 1223, 96, 700, 468, 1714, 1208, 19, 1137, 891, 1756, 43, 459, 250, 1618, 894, 1994, 1277, 1881, 266, 1052, 903, 1386, 783, 10, 1925, 692, 1584, 1352, 1619, 986, 684, 305, 1066, 231, 1617, 67, 1771, 1060, 1663, 70, 344, 1065, 1990, 1704, 640, 744, 121, 1213, 1919, 482, 771, 1150, 679, 1635, 1074, 526, 116, 767, 323, 568, 1053, 41, 571, 1596, 297, 312, 1560, 1393, 1493, 293, 1, 886, 1322, 674, 1436, 1623, 125, 583, 1861, 243, 1970, 1173, 851, 875, 1422, 1883, 291, 970, 1950, 1895, 807, 1247, 1408, 1231, 229, 102, 1807, 280, 778, 289, 420, 656, 1118, 456, 493, 319, 1235, 105, 1399, 881, 86, 1551, 1902, 1616, 380, 1271, 1006, 1261, 1037, 503, 948, 21, 1918, 1875, 874, 901, 1031, 1671, 1149, 393, 1019, 1681, 1318, 1697, 1122, 681, 256, 980, 1625, 404, 1338, 1435, 1175, 1755, 617, 1828, 1460, 1351, 1189, 66, 1402, 1632, 383, 249, 56, 578, 9, 557, 939, 1272, 862, 16, 718, 370, 850, 1978, 1952, 270, 658, 131, 1728, 1176, 1392, 137, 1409, 46, 1464, 1538, 475, 698, 667, 870, 1468, 1746, 704, 553, 1206, 833, 831, 1160, 75, 2, 742, 1877, 1706, 1571, 1429, 898, 1886, 217, 1071, 577, 1437, 942, 1202, 192, 1324, 730, 258, 390, 309, 415, 1612, 878, 1169, 1267, 1342, 409, 424, 842, 302, 1685, 1339, 1166, 107, 538, 92, 669, 375, 1038, 1390, 691, 14, 181, 569, 561, 381, 1349, 906, 1638, 195, 845, 1716, 168, 101, 36, 1076, 1194, 1553, 1358, 345, 1328, 1939, 1973, 786, 495, 949, 1558, 808, 1158, 1034, 208, 408, 1445, 1708, 1998, 1932, 1764, 73, 1516, 1921, 276, 191, 178, 1309, 1008, 782, 1559, 1229, 184, 1498, 385, 1134, 1051, 1082, 1007, 522, 927, 1824, 1893, 426, 422, 425, 1458, 492, 624, 956, 1578, 175, 1304, 1478, 954, 1927, 1121, 994, 725, 1843, 1793, 864, 1348, 1293, 801, 1430, 292, 1856, 134, 1265]

treeins(arr)
inorderRec(root)
