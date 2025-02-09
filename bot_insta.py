import time
import pyautogui

if __name__ == "__main__":

    # time.sleep(10)

    # position = pyautogui.position()

    # print(position)

    #----------------#
    
    x = 805
    y = 663
    time.sleep(5)
    
    #COM REPETICOES PRA MUDAR O TEXTO A CADA 20 COMENTARIOS 

    repeticoes = 20

    for i in range(repeticoes):

        pyautogui.write("rosao", interval=0.3)

        pyautogui.press('enter')

        time.sleep(10)

        pass


    #SEM CONTAGEM DE REPETICAO

    # while True:
    #     # pyautogui.moveTo(x, y)
    #     # time.sleep(2)

    #     pyautogui.write('VIBE', interval=0.3)

    #     pyautogui.press('enter')

    #     time.sleep(10)

    #     pass

    pass