import glm
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

class Render(object):
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.escena = []
        self.ccol = [0.0, 0.0, 0.0, 1.0]
        _, _, self.width, self.height = pantalla.get_rect()
        self.bs = None
        self.pmat = glm.perspective(glm.radians(60.0),self.width / self.height,0.1,1000.0        )
        self.tiemp = 0.0
        self.dluz = glm.vec3(1, 0, 0)
        self.Lint = 1.0
        self.hint = 0.5
        self.cpos = glm.vec3(0.0, 0.0, 0.0)
        self.crttn = glm.vec3(0.0, 0.0, 0.0)
        self.obje = glm.vec3(0.0, 0.0, 0.0)
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, self.width, self.height)

    def cambvmat(self):
        self.vmat = glm.lookAt(self.cpos,self.obje,glm.vec3(0.0, 1.0, 0.0))

    def gvmat(self):
        idnt = glm.mat4(1.0)
        pas = glm.rotate(idnt, glm.radians(self.crttn.x), glm.vec3(1.0, 0.0, 0.0))
        yw = glm.rotate(idnt, glm.radians(self.crttn.y), glm.vec3(0.0, 1.0, 0.0))
        gr = glm.rotate(idnt, glm.radians(self.crttn.z), glm.vec3(0.0, 0.0, 1.0))
        rttmat = pas * yw * gr
        transmat = glm.translate(idnt, self.crttn)
        cmat = transmat * rttmat
        return glm.inverse(cmat)

    def shaders(self, vrshad=None, frshad=None):
        self.bs = None if vrshad is None and frshad is None else compileProgram(compileShader(vrshad, GL_VERTEX_SHADER),compileShader(frshad, GL_FRAGMENT_SHADER))
            
    def renderizar(self):
        glClearColor(*self.ccol)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if self.bs:
            glUseProgram(self.bs)
            glUniformMatrix4fv(glGetUniformLocation(self.bs, "vmat"),1,GL_FALSE,glm.value_ptr(self.vmat))
            glUniformMatrix4fv(glGetUniformLocation(self.bs, "pmat"),1,GL_FALSE,glm.value_ptr(self.pmat))
            glUniform1f(glGetUniformLocation(self.bs, "relo"),self.tiemp)
            glUniform3fv(glGetUniformLocation(self.bs, "dluz"),1,glm.value_ptr(self.dluz))
            glUniform1f(glGetUniformLocation(self.bs, "Lint"),self.Lint)
            glUniform1f(glGetUniformLocation(self.bs, "hint"),self.hint)
        for objeto in self.escena:
            if self.bs:
                glUniformMatrix4fv(glGetUniformLocation(self.bs, "mdmat"),1,GL_FALSE,glm.value_ptr(objeto.gmmat()))
            objeto.renderizar()
