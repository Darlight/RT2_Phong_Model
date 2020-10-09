"""
Universidad del Valle de Guatemala
Gráficas por computadora
Seccion 10
Lic. Dennis Aldana
Mario Perdomo
18029

main.py
Proposito: Bears built with Raytracing
"""
from tracing import *
from material import *
from math_functions import V3
from light import Light
from sphere import *

raymap = Raytracer(500, 500)
raymap.light = Light(
    position=V3(20, 15, 30),
    intensity=1.4
)
raymap.currentbg_color = PURPLISH
print("Rendering now...")
raymap.models = [

    #Brown Bear with red belly
    Sphere(V3(3.2, -1.3, -15), 2, rubber),
    Sphere(V3(4.9, 0, -14.5), 1.1, brown_skin),
    Sphere(V3(1.5, 0, -14.5), 1.1, brown_skin),
    Sphere(V3(4.3, -2.6, -14.1), 1.1, brown_skin),
    Sphere(V3(1.9, -2.6, -14.1), 1.1, brown_skin),
    Sphere(V3(3.2, 1.6, -14.9), 1.7, brown_skin),
    Sphere(V3(4.2, 2.7, -14.4), 0.7, brown_darkerskin),
    Sphere(V3(2.2, 2.7, -14.4), 0.7, brown_darkerskin),
    Sphere(V3(3.2, 1.3, -13.52), 0.6, brown_darkerskin),
    Sphere(V3(2.8, 2.1, -13.5), 0.2, eye),
    Sphere(V3(3.6, 2.1, -13.5), 0.2, eye),
    Sphere(V3(3.6, 2.1, -13.1), 0.15, eye),

    #White Bear
    Sphere(V3(-3.2, -1.3, -15), 2, white_skin),
    Sphere(V3(-1.5, 0, -14.5), 1.1, white_skin),
    Sphere(V3(-4.9, 0, -14.5), 1.1, white_skin),
    Sphere(V3(-2.1, -2.6, -14.1), 1.1, white_skin),
    Sphere(V3(-4.5, -2.6, -14.1), 1.1, white_skin),
    Sphere(V3(-3.2, 1.6, -14.9), 1.7, white_skin),
    Sphere(V3(-3.2, 1.6, -14.9), 1.7, white_skin),
    Sphere(V3(-2.2, 2.7, -14.4), 0.7, white_skin),
    Sphere(V3(-4.2, 2.7, -14.4), 0.7, white_skin),
    Sphere(V3(-3.2, 1.3, -13.3), 0.2, white_skin),
    Sphere(V3(-3.6, 2.1, -13.5), 0.2, eye),
    Sphere(V3(-2.8, 2.1, -13.5), 0.2, eye),
]
raymap.finish()
print("Bear plushies done!  \n")