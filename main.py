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

raymap = Raytracer(800, 800)
raymap.light = Light(
    position=V3(30, 15, 50),
    intensity=1.1
)
raymap.current_color = PURPLISH

raymap.models = []

raymap.finish()
print("Bear plushies done!  \n")