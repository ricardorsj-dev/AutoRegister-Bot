import pyautogui
import time

pyautogui.PAUSE = 0.7

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)

pyautogui.hotkey("ctrl", "l")

pyautogui.write(
    "https://dlp.hashtagtreinamentos.com/python/intensivao/login",
    interval=0.05
)

pyautogui.press("enter")

time.sleep(5)

pyautogui.click (x=687, y=409)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha muito dificil dificilima")
pyautogui.click(x=658, y=578)

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    pyautogui.click(x=620, y=291)
    codigo = str(tabela.loc [linha, "codigo"])
    pyautogui.write (codigo)
    pyautogui.press("tab")
    marca = str(tabela.loc [linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc [linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc [linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc [linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    custo = str(tabela.loc [linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc [linha, "obs"])
    if obs != "nan":
       pyautogui.write(obs)
       print("passou")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    
    

    










    

































