"""
Universidad del Valle de Guatemala
Gráficas por computadora
Seccion 10
Lic. Dennis Aldana
Mario Perdomo
18029

main.py
Proposito: Snowman built by the render engine  
"""
from tracing import *

snow = Material(diffuse=color(255, 250, 250))
buttons = Material(diffuse=BLACK)
eyes = Material(diffuse=WHITE)
carrot = Material(diffuse=color(255, 108, 25))

raymap = Raytracer(800, 800)
raymap.models = [
    # Face
    Sphere(V3(0.24, -2.08, -6), 0.06, buttons),
    Sphere(V3(-0.24, -2.08, -6), 0.06, buttons),
    #Eyes
    Sphere(V3(0.24, -2.08, -6), 0.14, eyes),
    Sphere(V3(-0.24, -2.08, -6), 0.14, eyes), 
    #Nose
    Sphere(V3(0, -1.82, -6), 0.16, carrot),
    #smile
    Sphere(V3(-0.3, -1.62, -6), 0.06, buttons),
    Sphere(V3(-0.14, -1.48, -6), 0.06, buttons),
    Sphere(V3(0.14, -1.48, -6), 0.06, buttons),
    Sphere(V3(0.3, -1.62, -6), 0.06, buttons),
    # Buttons
    Sphere(V3(0, -0.6, -6), 0.16, buttons),
    Sphere(V3(0, 0.2, -6), 0.24, buttons),
    Sphere(V3(0, 1.42, -6), 0.32, buttons),
    # Body  
    Sphere(V3(0, -1.8, -6), 0.76, snow),
    Sphere(V3(0, -0.4, -6), 0.94, snow),
    Sphere(V3(0, 1.74, -8), 1.8, snow)
]

raymap.finish()
print("Snowman Done \n")