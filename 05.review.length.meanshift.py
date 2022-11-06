import pandas as pd
import numpy as np
import statistics
import copy


df = pd.read_json("D:/ESILV/Annee_5/Vietnam/cours/Data_mining_2/archive/yelp_academic_dataset_review.json", lines=True, nrows=10000)
df["length"] = df["text"].str.len()
data = df["length"].to_list()


class Point:
    def __init__(self, text):
        self.text = text
        self.data = len(text)
        self.mode = self.data


    def calcDist(self, point):
        return abs(point.data-point.modex)


    def k(self, point, h):
        pass


    def shiftMode(self, points):
        oldMode = self.mode
        mode = sum(p.data * k(p.data - self.mode) for p in points) / sum([k(p.data - self.mode) for p in points])

        return oldMode


    def meanshift(points, t):
        for p in points:
            while True:
                oldMode = p.shiftMode(points)
                if abs(oldMode - p.mode) < t:
                    break
