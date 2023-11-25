import pygame
import glm
from numpy import array, float32
from OpenGL.GL import *


class modelo(object):
    def __init__(self, dat):
        self.vbf = array(dat, dtype=float32)
        self.vb = glGenBuffers(1)
        self.va = glGenVertexArrays(1)
        self.pos = glm.vec3(0.0, 0.0, 0.0)
        self.rttn = glm.vec3(0.0, 0.0, 0.0)
        self.tama = glm.vec3(1.0, 1.0, 1.0)
        self.txtusup= self.txtud= self.txtubf= self.rtxtusup= self.rtxtudt= self.rtxtubf = None

    def cntxtu(self, dire):
        self.rtxtusup = pygame.image.load(dire)
        self.rtxtudt = pygame.image.tostring(self.rtxtusup, "RGB", True)
        self.rtxtubf = glGenTextures(1)

    def gmmat(self):
        idnt = glm.mat4(1.0)
        pas = glm.rotate(idnt, glm.radians(self.rttn.x), glm.vec3(1.0, 0.0, 0.0))
        yw = glm.rotate(idnt, glm.radians(self.rttn.y), glm.vec3(0.0, 1.0, 0.0))
        gr = glm.rotate(idnt, glm.radians(self.rttn.z), glm.vec3(0.0, 0.0, 1.0))
        transmat = glm.translate(idnt, self.pos)
        rttmat = pas * yw * gr
        tamamat = glm.scale(idnt, self.tama)
        return transmat * rttmat * tamamat


    def crgartxtu(self, dire):
        self.txtusup = pygame.image.load(dire)
        self.txtud = pygame.image.tostring(self.txtusup, "RGB", True)
        self.txtubf = glGenTextures(1)

    def renderizar(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vb)
        glBindVertexArray(self.va)
        glBufferData(GL_ARRAY_BUFFER,self.vbf.nbytes,self.vbf,GL_STATIC_DRAW)
        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,32,ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1,2,GL_FLOAT,GL_FALSE,32,ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.txtubf)
        glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,self.txtusup.get_width(),self.txtusup.get_height(),0,GL_RGB,GL_UNSIGNED_BYTE,self.txtud)
        glGenerateTextureMipmap(self.txtubf)
        glActiveTexture(GL_TEXTURE1)
        #glBindTexture(GL_TEXTURE_2D, self.rtxtubf)
        #glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,self.rtxtusup.get_width(),self.rtxtusup.get_height(),0,GL_RGB,GL_UNSIGNED_BYTE,self.rtxtudt)
        #glGenerateTextureMipmap(self.rtxtubf)
        glVertexAttribPointer(2,3,GL_FLOAT,GL_FALSE, 32,ctypes.c_void_p(20))
        glEnableVertexAttribArray(2)
        glDrawArrays(GL_TRIANGLES, 0, len(self.vbf) // 8)
