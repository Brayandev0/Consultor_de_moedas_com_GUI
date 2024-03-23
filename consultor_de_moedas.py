# Criador         : Brayan vieira 
# função          : Um sistema pratico e simples de consultar valores com interface grafica
# versão          : 1.0
# data da criação : 20/2/2024
import flet as ft 
import requests
moeda__ = ""
#Realiza a requisição da api
def requisicao(moeda_escolhida):
     API = f"https://economia.awesomeapi.com.br/last/{moeda_escolhida}"
     informacoes = requests.get(API)
     dados = informacoes.json()
     for indice,total in dados.items():
          texto__.value += f"{total["name"]}"
          info_moeda.value += f"\nCompra : {total["bid"]} R$ \n"
          info_moeda.value += f"\nVenda  : {total["ask"]} R$ \n"
          info_moeda.value += f"\nMaior Alta  : {total["high"]} R$ \n"
          info_moeda.value += f"\nMaior Baixa : {total["low"]} R$ \n"
          info_moeda.value += f"\nPorcentagem de variação : {total["pctChange"]} R$ \n"
#Verifica a moeda e define para a requisição
def verificando_a_moeda(moeda):
       match moeda:
            case "dolar":
                moeda_requisitada = "USD-BRL"
            case "euro":
                moeda_requisitada = "EUR-BRL"
            case "btc":
                moeda_requisitada = "BTC-BRL"
            case "libra":
                moeda_requisitada = "GBP-BRL"
            case "ethereum":
                moeda_requisitada = "ETH-BRL"
            case "ruble":
                moeda_requisitada = "BRL-RUB"
       return moeda_requisitada
# Pagina principal
def main(pagina: ft.Page):
        pagina.title = "cotação de Moedas"
        pagina.window_width = 650
        pagina.window_height = 550
        def fechar_e_abrir_a_outra(e,moeda):
                global moeda__
                moeda__ = verificando_a_moeda(moeda)
                pagina.window_close()
        texto_principal = ft.TextField(value="Bem vindo ao Consultor de Moedas ",text_align="center", )
        texto_secundario = ft.Text(value=" \n \n \n Clique em uma das moedas acima para ver a cotação atual", style=ft.TextStyle.italic )
        BTC1 = ft.TextButton(text="Bitcoin", icon=ft.icons.CURRENCY_BITCOIN_OUTLINED, on_click=lambda e: fechar_e_abrir_a_outra(None,"btc"))
        dolar = ft.TextButton(text="$ Dolar", scale=1.2 , on_click=lambda e: fechar_e_abrir_a_outra(None,"dolar") )
        euro = ft.TextButton(text="Euro", icon=ft.icons.EURO,on_click=lambda e: fechar_e_abrir_a_outra(None,"euro") )
        ruble = ft.TextButton(text="Rublo Russo", icon=ft.icons.CURRENCY_RUBLE ,on_click=lambda e: fechar_e_abrir_a_outra(None,"ruble"))
        etherum = ft.TextButton(text="Ethereum", icon=ft.icons.CURRENCY_EXCHANGE,on_click=lambda e: fechar_e_abrir_a_outra(None,"ethereum") )
        Libra_esterlina = ft.TextButton(text="Libra Esterlina", icon=ft.icons.CURRENCY_POUND, on_click=lambda e: fechar_e_abrir_a_outra(None,"libra") )


        pagina.add(
            ft.Row(
                [texto_principal],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [dolar,BTC1, etherum],
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            ft.Row(
                [euro,ruble, Libra_esterlina],
                alignment=ft.MainAxisAlignment.SPACE_AROUND
            ),
            ft.Row([texto_secundario],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY)
                )
ft.app(target=main)
# Verifica a variavel para garantir q haja valor e a pagina n abrir com erro
if moeda__:
    def pagina2(pagina: ft.Page):
            pagina.window_width = 400
            pagina.window_height = 500
            global info_moeda
            global texto__
            pagina.title = "Consultar moedas"
            def exit(e):
                 pagina.window_close()
            texto__ = ft.TextField(value=" ")
            info_moeda = ft.Text(value="", font_family=ft.TextStyle.italic)
            Voltar = ft.TextButton(text="Sair", on_click=exit)
            requisicao(moeda__)
            pagina.add(
                ft.Row([texto__, Voltar],
                       alignment=ft.alignment.center_right),
                ft.Row(
                     [info_moeda],
                     alignment=ft.alignment.center_right
                )

            )
    ft.app(target=pagina2)
