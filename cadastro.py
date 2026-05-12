import pyautogui

def cadastrar_produto(tabela, linha):

    pyautogui.click(x=620, y=291)

    campos = [
        "codigo",
        "marca",
        "tipo",
        "categoria",
        "preco_unitario",
        "custo"
    ]

    for campo in campos:
        valor = str(tabela.loc[linha, campo])

        pyautogui.write(valor)
        pyautogui.press("tab")
