from variables import *

class Terrain(object):
    # terrain types: earth 0, water 1, rock 2,
    colors = [ [0.38, 0.29, 0.03], [ 0.25, 0.64, 0.87 ], [ 0.5, 0.52, 0.53 ] ]
    # colors = [ [0.15, 0.70, 0.15], [ 0.25, 0.74, 0.87 ], [ 0.5, 0.52, 0.53 ] ]
    def __init__(self, terrainType):
        self.color = self.colors[terrainType]
