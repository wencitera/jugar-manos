import cv2

def create(frame):
    altura, ancho, _ = frame.shape

    # Coordenadas y dimensiones de los rectángulos del borde
    borde1 = (0, 0, ancho // 3, altura)
    borde2 = (ancho // 3, 0, 2 * (ancho // 3), altura)
    borde3 = (2 * (ancho // 3), 0, ancho, altura)

    # Coordenadas y dimensiones de los rectángulos del footer
    altura_footer = altura - 50
    footer1 = (0, altura_footer, ancho // 3, altura)
    footer2 = (ancho // 3, altura_footer, 2 * (ancho // 3), altura)
    footer3 = (2 * (ancho // 3), altura_footer, ancho, altura)

    # Dibujar los rectángulos del borde
    cv2.rectangle(frame, (borde1[0], borde1[1]), (borde1[2], borde1[3]), (0, 0, 255), 2)
    cv2.rectangle(frame, (borde2[0], borde2[1]), (borde2[2], borde2[3]), (0, 0, 255), 2)
    cv2.rectangle(frame, (borde3[0], borde3[1]), (borde3[2], borde3[3]), (0, 0, 255), 2)

    # Dibujar los rectángulos del footer
    cv2.rectangle(frame, (footer1[0], footer1[1]), (footer1[2], footer1[3]), (255, 255, 255), -1)
    cv2.rectangle(frame, (footer2[0], footer2[1]), (footer2[2], footer2[3]), (255, 255, 255), -1)
    cv2.rectangle(frame, (footer3[0], footer3[1]), (footer3[2], footer3[3]), (255, 255, 255), -1)

    # Texto en los footers
    font = cv2.FONT_HERSHEY_SIMPLEX
    escala = 0.5
    grosor = 1
    color_texto = (0, 0, 0)  # Negro
    cv2.putText(frame, "Mover hacia atras", (footer1[0] + 10, footer1[1] + 30), font, escala, color_texto, grosor)
    cv2.putText(frame, "Cerrar mano para saltar", (footer2[0] + 10, footer2[1] + 30), font, escala, color_texto, grosor)
    cv2.putText(frame, "Mover hacia adelante", (footer3[0] + 10, footer3[1] + 30), font, escala, color_texto, grosor)


