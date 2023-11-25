vrshad = """
    #version 450 core
    layout (location = 0) in vec3 pos;
    layout (location = 1) in vec2 txcrds;
    layout (location = 2) in vec3 nrms;
    uniform mat4 mdmat;
    uniform mat4 vmat;
    uniform mat4 pmat;    
    out vec2 UVs;
    out vec3 nrm;
    void main() {
        gl_Position = pmat * vmat * mdmat * vec4(pos, 1.0);
        UVs = txcrds;
        nrm = (mdmat * vec4(nrms, 0.0)).xyz;
    }
"""

frshad = """
    #version 450 core
    layout (binding = 0) uniform sampler2D tex;    
    in vec2 UVs;
    in vec3 nrm;
    out vec4 fragColor;
    void main() {
        fragColor = texture(tex, UVs);
    }
"""

gourdad_shader = """
    #version 450 core
    layout (binding = 0) uniform sampler2D tex;
    uniform vec3 dluz;
    uniform float Lint;
    in vec2 UVs;
    in vec3 nrm;
    out vec4 fragColor;
    void main() {
        float intensity = dot(nrm, -dluz) * Lint;
        fragColor = texture(tex, UVs) * intensity;
    }
"""

bw_shader = """
    #version 450 core
    layout (binding = 0) uniform sampler2D tex;
    uniform float relo;
    in vec2 UVs;
    in vec3 nrm;
    out vec4 fragColor;
    void main() {
        vec4 color = texture(tex, UVs);
        float luminance = dot(color.rgb, vec3(0.2, 0.7, 0.07));
        fragColor = vec4(luminance, luminance, luminance, 1.0);
    }
"""

pixel_shader = """
    #version 450 core
    layout (binding = 0) uniform sampler2D tex;
    uniform float relo;
    uniform float fatness;
    in vec2 UVs;
    out vec4 fragColor;
    void main() {
        float ptama = 1.0 / 64.0;
        vec2 pxlu = floor(UVs / ptama) * ptama;
        fragColor = texture(tex, pxlu);
    } 
"""

light_shader = """
    #version 450 core
    layout (binding = 0) uniform sampler2D tex;
    uniform float relo;
    uniform float fatness;
    uniform vec3 dluz;
    uniform float Lint;
    uniform float hint;
    in vec2 UVs;
    in vec3 nrm;
    out vec4 fragColor;
    void main() {
        float intensity = dot(nrm, -dluz) * Lint*20;
        float f = pow(intensity, hint);
        fragColor = texture(tex, UVs) * f;
    }
"""
rgb_shader = """
    #version 450 core
    layout (binding = 0) uniform sampler2D tex;
    uniform float relo;
    in vec2 UVs;
    in vec3 nrm;
    out vec4 fragColor;
    void main() {
        vec3 n = normalize(nrm);
        vec3 r = vec3(sin(relo), sin(relo + 2.0), sin(relo + 4.0));
        vec3 nnorm = normalize(n + r);
        float intensity = dot(nnorm, -vec3(1.0, 1.0, 1.0));
        fragColor = vec4(nnorm, 1.0) * intensity;
    }
"""
