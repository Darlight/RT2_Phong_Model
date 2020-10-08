"""
Universidad del Valle de Guatemala
Gráficas por computadora
Seccion 10
Lic. Dennis Aldana
Mario Perdomo
18029

tracing.py
Proposito: Render of objects via Ray Intersect Algorithm
"""


import struct
from collections import namedtuple
from math_functions import *

#Structures from the Bitmap Render
def char(c):
    return struct.pack("=c", c.encode("ascii"))


def word(w):
    return struct.pack("=h", w)


def dword(d):
    return struct.pack("=l", d)

#Colors
def color(r, g, b):
    return bytes([b, g, r])


#Colors
BLACK = color(0, 0, 0)
PURPLISH = color(255, 204, 204)
WHITE = color(255, 255, 255)


#The file
def writebmp(filename, width, height, pixels):
    f = open(filename, "bw")

    # File header (14 bytes)
    f.write(char("B"))
    f.write(char("M"))
    f.write(dword(14 + 40 + width * height * 3))
    f.write(dword(0))
    f.write(dword(14 + 40))

    # Image header (40 bytes)
    f.write(dword(40))
    f.write(dword(width))
    f.write(dword(height))
    f.write(word(1))
    f.write(word(24))
    f.write(dword(0))
    f.write(dword(width * height * 3))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))
    f.write(dword(0))

    # Pixel data (width x height x 3 pixels)
    for x in range(height):
        for y in range(width):
            f.write(pixels[x][y])
    f.close()



#Circumference Object
class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, direction):
        L = sub(self.center, orig)
        tca = dot(L, direction)
        l = length(L)
        d2 = l ** 2 - tca ** 2
        if d2 > self.radius ** 2:
            return False
        thc = (self.radius ** 2 - d2) ** 1 / 2
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1
        if t0 < 0:
            return False
        return True


#Raymap
class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.models = []
        self.clear()
        self.current_color = WHITE

    def clear(self):
        self.pixels = [[PURPLISH for x in range(self.width)] for y in range(self.height)]

    def write(self, filename):
        writebmp(filename, self.width, self.height, self.pixels)

    def finish(self, filename="output.bmp"):
        self.render()
        self.write(filename)

    def point(self, x, y, c=None):
        try:
            self.pixels[y][x] = c or self.current_color
        except:
            pass

    def cast_ray(self, orig, direction):
        for model in self.models:
            if model.ray_intersect(orig, direction):
                return model.material.diffuse
        return PURPLISH

    def render(self):
        fov = int(pi / 2)
        for y in range(self.height):
            for x in range(self.width):
                i = (
                    (2 * (x + 0.5) / self.width - 1)
                    * tan(fov / 2)
                    * self.width
                    / self.height
                )
                j = -(2 * (y + 0.5) / self.height - 1) * tan(fov / 2)
                direction = norm(V3(i, j, -1))
                self.pixels[y][x] = self.cast_ray(V3(0, 0, 0), direction)