import heatmap # http://jjguy.com/heatmap/
import random
import csv
 
if __name__ == "__main__":
    pts = []
    for point in csv.reader(open('bad3.csv')):
      pts.append((float(point[0]), float(point[1])))
 
    print "Processing %d points..." % len(pts)
 
    hm = heatmap.Heatmap()
    pts = [(random.uniform(-125,25), random.uniform(-65,48)) for x in range(1000)]
    hm.heatmap(pts)
    hm.saveKML("bad3.kml")
