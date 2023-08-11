from mathLib import matMatMult


def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["viewMatrix"]

    # Convertir el vértice a una matriz columna 4x1 agregando un valor de 1
    vt = [[vertex[0]], [vertex[1]], [vertex[2]], [1]]
    # Realizar la multiplicación de la matriz del modelo con el vértice
    vt = matMatMult(vpMatrix, matMatMult(projectionMatrix, matMatMult(viewMatrix, matMatMult(modelMatrix, vt))))
    # Convertir la matriz resultado de nuevo a un vértice (lista)
    vt = [vt[0][0],vt[1][0],vt[2][0]]
    return vt


def fragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    if texture is not None:
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    # Calculate the intensity of the color (brightness)
    intensity = (color[0] + color[1] + color[2]) / 3.0

    # Define the toon shading levels (adjust as needed)
    levels = 4

    # Calculate the new color value based on toon shading levels
    if intensity > 0.8:
        color = (1, 1, 1)  # High intensity, use white color for cuerpo
    elif intensity > 0.6:
        color = (1, 1, 1)  # Medium-high intensity, use white color for cuerpo
    elif intensity > 0.4:
        color = (0.9, 0.5, 0)  # Medium intensity, use orange color for camisa

    return color






