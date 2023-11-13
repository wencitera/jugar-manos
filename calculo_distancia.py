import numpy as np

def calculate_distance(x1,y1,x2,y2):
    p1 = np.array([x1,y1])
    p2 = np.array([x2,y2])
    return np.linalg.norm(p1-p2)

if __name__ == "__main__":
    cord_x1 = int(input('Ingrese valor de la coordenada x1:'))
    cord_x2 = int(input('Ingrese valor de la coordenada y1:'))
    cord_y1 = int(input('Ingrese valor de la coordenada x2:'))
    cord_y2 = int(input('Ingrese valor de la coordenada y2:'))

    dist = round(calculate_distance(cord_x1, cord_y1, cord_x2, cord_y2), 2)
    print(f'La distancia calculada es: {dist}')