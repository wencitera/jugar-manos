import time
import webbrowser
import pygetwindow as gw
import win32gui
import win32con
__URL = 'https://supermario-game.com/es'
__WINDOW_TITLE = "Juego de Super Mario Bros en línea"
focused = False

def open_mario():
    webbrowser.open(__URL)
      # Reemplaza con el título de la ventana que deseas redimensionar
    time.sleep(1.5)
    window = gw.getWindowsWithTitle(__WINDOW_TITLE)[0]
    window.maximize()
    if window is not None:
        # Obtiene el identificador de la ventana
        hwnd = win32gui.FindWindow(None, window.title)

        if hwnd:
            # Cambia el estado de la ventana de maximizado a normal (si está maximizado)
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

            # Calcula las nuevas dimensiones para la ventana
            new_width = 1920 // 2
            new_height = 1080

            # Redimensiona la ventana
            win32gui.MoveWindow(hwnd, -8, -8, new_width, new_height, True)
        else:
            print("No se pudo encontrar el identificador de la ventana")
    else:
        print("La ventana no se encontró")
    
def focus_game():
    global focused
    if not focused: 
        # Search for a window with the specified title
        time.sleep(2)
        window = gw.getWindowsWithTitle(__WINDOW_TITLE)[0]

        if window is not None:
            # Focus the first window with the specified title
            window.activate()
            focused = True
        else:
            print("La ventana no se encontró")

    
if __name__ == '__main__':
    open_mario()
    focus_game()