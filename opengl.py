import pygame
import glm
import math
from pygame.locals import *
from Render import Render
from modelo import modelo
from Shaders import *
from objeto import Objt

width = 1080
height = 600
pygame.init()
pantalla = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
relo = pygame.time.Clock()

Render = Render(pantalla)
vertsha = vrshad
fragsha = frshad
Render.shaders(vertsha, fragsha)
click = False
posi = None

Nmodelo = 0
modelos = []
def cambiarm(dir):
    global Nmodelo
    global modelos
    if dir == "SIG":
        if Nmodelo == len(modelos) - 1:
            Nmodelo = 0
        else:
            Nmodelo += 1
    else:
        if Nmodelo == 0:
            Nmodelo = len(modelos) - 1
        else:
            Nmodelo -= 1
    pygame.mixer.music.load(musica[Nmodelo])
    pygame.mixer.music.play(-1)
    Render.escena.clear()
    Render.escena.append(modelos[Nmodelo]['mdlo'])
    Render.Lint = modelos[Nmodelo]['Lint']
    Render.hint = modelos[Nmodelo]['hint']
    Render.obje = modelos[Nmodelo]['ver']
    Render.cpos = glm.vec3(0.0, 0.0, 0.0)
    Render.dluz = modelos[Nmodelo]['dluz']

obi = Objt("modelos/gato.obj").datan()
mdlo = modelo(obi)
mdlo.crgartxtu("textura/gato.bmp")
mdlo.pos.z = -15
mdlo.pos.y = -10
mdlo.rttn.x = 270
mdlo.tama = glm.vec3(0.2, 0.2, 0.2)
Md = {"mdlo": mdlo,"Lint": 5.0,"hint": 0.3,"ver": glm.vec3(mdlo.pos.x, mdlo.pos.y + 2 , mdlo.pos.z),"dluz": glm.vec3(0, 0, -1)}
modelos.append(Md)
obi = Objt("modelos/mono.obj").datan()
mdlo = modelo(obi)
mdlo.crgartxtu("textura/mono.bmp")
mdlo.pos.z = -15
mdlo.pos.y = -10
mdlo.rttn.x = 270
mdlo.tama = glm.vec3(0.2, 0.2, 0.2)
Md = {"mdlo": mdlo,"Lint": 5.0,"hint": 0.3,"ver": glm.vec3(mdlo.pos.x, mdlo.pos.y + 2 , mdlo.pos.z),"dluz": glm.vec3(0, 0, -1)}
modelos.append(Md)
obi = Objt("modelos/pajaro.obj").datan()
mdlo = modelo(obi)
mdlo.crgartxtu("textura/pajaro.bmp")
mdlo.pos.z = -15
mdlo.pos.y = -10
mdlo.rttn.x = 270
mdlo.tama = glm.vec3(0.3, 0.3, 0.3)
Md = {"mdlo": mdlo,"Lint": 5.0,"hint": 0.3,"ver": glm.vec3(mdlo.pos.x, mdlo.pos.y + 2 , mdlo.pos.z),"dluz": glm.vec3(0, 0, -1)}
modelos.append(Md)
obi = Objt("modelos/pato.obj").datan()
mdlo = modelo(obi)
mdlo.crgartxtu("textura/pato.bmp")
mdlo.pos.z = -15
mdlo.pos.y = -2
mdlo.rttn.x = 270
mdlo.tama = glm.vec3(0.2, 0.2, 0.2)
Md = {"mdlo": mdlo,"Lint": 5.0,"hint": 0.3,"ver": glm.vec3(mdlo.pos.x, mdlo.pos.y + 2 , mdlo.pos.z),"dluz": glm.vec3(0, 0, -1)}
modelos.append(Md)
obi = Objt("modelos/perro.obj").datan()
mdlo = modelo(obi)
mdlo.crgartxtu("textura/perro.bmp")
mdlo.pos.z = -15
mdlo.pos.y = -10
mdlo.rttn.x = 270
mdlo.tama = glm.vec3(0.2, 0.2, 0.2)
Md = {"mdlo": mdlo,"Lint": 5.0,"hint": 0.3,"ver": glm.vec3(mdlo.pos.x, mdlo.pos.y + 2 , mdlo.pos.z),"dluz": glm.vec3(0, 0, -1)}
modelos.append(Md)
musica=["musica/gato.mp3","musica/mono.mp3","musica/pajaro.mp3","musica/pato.mp3","musica/perro.mp3"]
Render.escena.append(modelos[Nmodelo]['mdlo'])
Render.Lint = modelos[Nmodelo]['Lint']
Render.hint = modelos[Nmodelo]['hint']
Render.obje = modelos[Nmodelo]['ver']
Render.dluz = modelos[Nmodelo]['dluz']
isRunning = True
pausa=False
sens = 0.1
sens_x = 1
sens_z = 0.5
sens_y = 0.1
angu = 0.0
dist = abs(Render.cpos.z- modelos[Nmodelo]['mdlo'].pos.z)
radi = dist
pygame.mixer.music.load(musica[0])
pygame.mixer.music.play(-1)
while isRunning:        
    Render.cpos.x = math.sin(math.radians(angu)) * radi + modelos[Nmodelo]['mdlo'].pos.x
    Render.cpos.z = math.cos(math.radians(angu)) * radi + modelos[Nmodelo]['mdlo'].pos.z
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            if event.key == pygame.K_r:
                fragsha = frshad
                vertsha = vrshad
            if event.key == pygame.K_1:
                fragsha = gourdad_shader
            if event.key == pygame.K_2:
                fragsha = bw_shader
            if event.key == pygame.K_3:
                fragsha = pixel_shader
            if event.key == pygame.K_4:
                fragsha = light_shader
            if event.key == pygame.K_5:
                fragsha = rgb_shader
            if event.key == pygame.K_w:
                Render.cpos.z -= sens
            if event.key == pygame.K_s:
                Render.cpos.z += sens
            if event.key == pygame.K_a:
                Render.cpos.x -= sens
            if event.key == pygame.K_d:
                Render.cpos.x += sens
            if event.key == pygame.K_SPACE:
                if pausa:
                    pygame.mixer.music.unpause()
                    pausa=False
                else:
                    pygame.mixer.music.pause()
                    pausa=True  
            if event.key == pygame.K_RIGHT:
                cambiarm("SIG")
                angu = 0.0
                radi = dist
            if event.key == pygame.K_LEFT:
                cambiarm("ANT")
                angu = 0.0
                radi = dist
            Render.shaders(vertsha, fragsha)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                click = True
                posi = pygame.mouse.get_pos()
            elif event.button == 4:
                if radi > dist * 0.5:
                    radi -= sens_z             
            elif event.button == 5:
                if radi < dist * 1.5:
                    radi += sens_z
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  
                click = False
        elif event.type == pygame.MOUSEMOTION:
            if click:
                npos = pygame.mouse.get_pos()
                dlx = npos[0] - posi[0]
                dly = npos[1] - posi[1]
                angu += dlx * -sens_x
                angu %= 360
                if dist > Render.cpos.y + dly * -sens_y and dist * -1.5 < Render.cpos.y + dly * -sens_y:
                    Render.cpos.y += dly * -sens_y
                posi = npos
    Render.cambvmat()
    Render.renderizar()
    pygame.display.flip()
pygame.quit()

