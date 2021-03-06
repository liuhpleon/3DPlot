# Read Data from CSV files and parse them into vertex and x, y, z lists

import csv

class DataImport:
    def __init__(self, file):
        self.file = file
        self.__init_xyzs()

    def __read_vertex(self):
        self.vertexs = []
        with open(self.file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                vertex = []
                if len(row) == 0:
                    break
                for item in row[0].split(" "):
                    if len(item) > 0:
                        vertex.append(float(item))
                self.vertexs.append(vertex)
        return self.vertexs

    def __init_xyzs(self):
        self.xs = []
        self.ys = []
        self.zs = []
        for vertex in self.__read_vertex():
            self.xs.append(vertex[0])
            self.ys.append(vertex[1])
            self.zs.append(vertex[2])

    def get_vertex(self):
        return self.vertexs

    def get_xs(self):
        return self.xs

    def get_ys(self):
        return self.ys

    def get_zs(self):
        return self.zs
