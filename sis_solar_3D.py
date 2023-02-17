from vpython import *

# Criar o Sol e planetas
sun = sphere(pos=vector(0, 0, 0), radius=2, color=color.yellow)
earth = sphere(pos=vector(10, 0, 0), radius=1, color=color.blue)
mars = sphere(pos=vector(15, 0, 0), radius=0.8, color=color.red)
venus = sphere(pos=vector(7, 0, 0), radius=0.9, color=color.orange)
mercury = sphere(pos=vector(3, 0, 0), radius=0.5, color=color.white)
jupiter = sphere(pos=vector(20, 0, 0), radius=2.5, color=color.cyan)

# Criar os eixos de coordenadas
x_axis = cylinder(pos=vector(0,0,0), axis=vector(25,0,0), radius=0.1, color=color.white)
y_axis = cylinder(pos=vector(0,0,0), axis=vector(0,25,0), radius=0.1, color=color.white)
z_axis = cylinder(pos=vector(0,0,0), axis=vector(0,0,25), radius=0.1, color=color.white)

# Definir as velocidades iniciais dos planetas
earth.velocity = vector(0, 0, 2)
mars.velocity = vector(0, 0, 1.5)
venus.velocity = vector(0, 0, 1.8)
mercury.velocity = vector(0, 0, 2.2)
jupiter.velocity = vector(0, 0, 0.8)

# Definir a taxa de atualização do modelo
dt = 0.01

# Criar um loop para atualizar a posição dos planetas
while True:
    rate(100)
    earth.pos = earth.pos + earth.velocity*dt
    mars.pos = mars.pos + mars.velocity*dt
    venus.pos = venus.pos + venus.velocity*dt
    mercury.pos = mercury.pos + mercury.velocity*dt
    jupiter.pos = jupiter.pos + jupiter.velocity*dt
