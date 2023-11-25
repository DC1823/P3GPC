class Objt(object):
    def __init__(self, filename):
        with open(filename,"r") as file:
            self.ln = file.read().splitlines()
        self.nrms = []
        self.caras = []
        self.vertices = []
        self.texcoords = []
        for linea in self.ln:
            try:
                pfx, val = linea.split(" ", 1)
            except:
                continue
            if pfx =="v":
               self.vertices.append(list(map(float, list(filter(None,val.split(" "))))))
            elif pfx =="vt":
               self.texcoords.append(list(map(float, list(filter(None,val.split(" "))))))
            elif pfx =="vn":
               self.nrms.append(list(map(float, list(filter(None,val.split(" "))))))
            elif pfx == "f": #Faces
                self.caras.append([list(map(int, list(filter(None,vert.split("/"))))) for vert in list(filter(None,val.split(" ")))])

    def datan(self):
        obinf = []
        for cara in self.caras:
            if len(cara) == 3:
                for vinf in cara:
                    vid, txtcrds, nid = vinf
                    vrtx = self.vertices[vid - 1]
                    nrms = self.nrms[nid - 1]
                    uv = self.texcoords[txtcrds - 1]
                    uv = [uv[0], uv[1]]
                    obinf.extend(vrtx + uv + nrms)
            elif len(cara) == 4:
                for i in [0, 1, 2]:
                    vinf = cara[i]
                    vid, txtcrds, nid = vinf
                    vrtx = self.vertices[vid - 1]
                    nrms = self.nrms[nid - 1]
                    uv = self.texcoords[txtcrds - 1]
                    uv = [uv[0], uv[1]]
                    obinf.extend(vrtx + uv + nrms)
                for i in [0, 2, 3]:
                    vinf = cara[i]
                    vid, txtcrds, nid = vinf
                    vrtx = self.vertices[vid - 1]
                    nrms = self.nrms[nid - 1]
                    uv = self.texcoords[txtcrds - 1]
                    uv = [uv[0], uv[1]]
                    obinf.extend(vrtx + uv + nrms)

        return obinf