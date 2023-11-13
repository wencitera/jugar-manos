import cv2  # Librería para trabajar con imágenes y videos.
import mediapipe as mp  #  
import calculo_distancia as cal_dist
import keyboard as kb
import open_game
import rectangle
# El módulo drawing_utils proporciona utilidades para dibujar puntos clave,
# líneas y formas en imágenes o videos
mp_drawing = mp.solutions.drawing_utils

# El módulo hands proporciona funcionalidades para detectar y rastrear 
# las manos en imágenes o videos en tiempo real.
mp_hands = mp.solutions.hands

open_game.open_mario()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Se crea un contexto para utilizar la función Hands
# el contexto with asegurará que los recursos relacionados 
# con la detección de manos se configuren adecuadamente al principio
# y se liberen correctamente al final
with mp_hands.Hands(
    static_image_mode=False,  # Indica si se va a analizar imagen estatica o video.
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
        

       # Se realiza la captura del frame 
       while True:
        ret, frame = cap.read()
        if ret == False:
            break

        # Se obtien las dimensiones del frame
        height, width, _ = frame.shape
        # Se realiza una rotación horizontal porque se asume que la imagen está espejada por la webcam
        frame = cv2.flip(frame, 1)
        # Las dectecciones se realizan con modo RGB, por eso se realiza conversion.
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  

        rectangle.create(frame)

        # Una vez listo el frame se procesa (se obtinen dos resultados: multi_handedness y hand_landmarks)
        # multi_handedness es una coleccion de datos: { index, score, label}
        results = hands.process(frame_rgb)

        # Imprime en consola los resultado de la detección.
        #print("Handedness: ", results.multi_handedness)

        if results.multi_hand_landmarks is not None:  # Impide que se ejecute este bloque de código sino hay deteccion
            for hand_landmarks in results.multi_hand_landmarks:  # Ciclo que recorre los 21 puntos por cada mano detectada 
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=5),  # color para los puntos, thickness es el grosor de linea
                    mp_drawing.DrawingSpec(color=(255,0,255), thickness=1, circle_radius=5))  # color para las conexiones

                # Obtine las coordenadas x e y del 
                x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * width)
                y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * height)

                x2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * width)
                y2 = int(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * height)

                dist = cal_dist.calculate_distance(x1,y1,x2,y2)
            
                # Distancia 
                if dist > 0 and dist < 160:
                    # Salto
                    kb.press('w')
                else:
                    kb.release('w')


                pos_centro_mano_x = int(hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x * width)
                
                if pos_centro_mano_x > width * 0.66:
                    kb.press('d')
                elif pos_centro_mano_x < width * 0.33:
                    kb.press('a')
                else:
                    kb.release('d')
                    kb.release('a')
            

        
        # Muestra el frame con todos los puntos y las interconexiones
        cv2.imshow('Jugar con Manos',frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break
# La función release() libera la captura de video o cualquier otro recurso
# relacionado con la fuente de video.
cap.release()  
# Esta función de OpenCV se utiliza para cerrar todas las 
# ventanas creadas por la aplicación
cv2.destroyAllWindows()
    