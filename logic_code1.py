import pyautogui
import time


def preencher_campo(coord_x, coord_y, texto):
    pyautogui.click(coord_x, coord_y)
    pyautogui.write(texto)


def clicar_botao(coord_x, coord_y):
    pyautogui.click(coord_x, coord_y)


def preencher_formulario(campos):
    for campo in campos:
        preencher_campo(campo[0], campo[1], campo[2])


campos_formulario = [
    (300, 200, "João da Silva"),   
    (300, 250, "joao@example.com"), 
    (300, 300, "Mensagem automatizada para preencher o formulário.") 
]
botao_enviar = (300, 350)


time.sleep(3)

preencher_formulario(campos_formulario)

clicar_botao(botao_enviar[0], botao_enviar[1])
