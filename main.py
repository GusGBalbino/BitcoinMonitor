from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import requests
import json


#Cores
black = "#444466" 
white = "#feffff"   
blue = "#6f9fbd"
fundo =  "#484f60"

#Configuração da Janela
janela = Tk()
janela.title('Monitor')
janela.geometry('320x250')
janela.configure(bg=fundo)

#Divisor de frames da janela
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=1)

#Configuração de frames 
up_frame = Frame(janela, width=400, height=55, bg=white, pady=0, padx=0, relief='flat')
up_frame.grid(row=1, column=0)

down_frame =  Frame(janela, width=320, height=300, bg=fundo, pady=0, padx=0, relief='flat')
down_frame.grid(row=2, column=0, sticky=NW)

#Caracterização e configuração de frames

imagem = Image.open('imagens/bitcoin.png')
imagem = imagem.resize((30,30), Image.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

lbicon = Label(up_frame, image=imagem, bg=white, compound=LEFT, relief=FLAT)
lbicon.place(x=10, y=10)

lname = Label(up_frame, text='Bitcoin Price Tracker',bg=white,fg=black, relief=FLAT, anchor='center', font=('Sylfaen 20'))
lname.place(x=50, y=6)

#----------------------------------------------------------------
def getBitcoin():

    apiLink = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CBRL'

    response = requests.get(apiLink)

    dados = response.json()

    valorUSD = float(dados['USD'])
    usdFormatado = 'US$ - {:,.3f}'.format(valorUSD)
    usd['text'] = usdFormatado

    valorEUR = float(dados['EUR'])
    eurFormatado = '€ - {:,.3f}'.format(valorEUR)
    eur['text'] = eurFormatado

    valorBRL = float(dados['BRL'])
    brlFormatado = 'R$ - {:,.3f}'.format(valorBRL)
    brl['text'] = brlFormatado

    down_frame.after(1000, getBitcoin)

#----------------------------------------------------------------
usd =  Label(down_frame, text='',width=14,bg=fundo,fg=white, relief=FLAT, anchor='center', font=('Sylfaen 15'))
usd.place(x=60, y=40)

eur =  Label(down_frame, text='',width=14,bg=fundo,fg=white, relief=FLAT, anchor='center', font=('Sylfaen 15'))
eur.place(x= 60, y=80)

brl =  Label(down_frame, text='',width=14,bg=fundo,fg=white, relief=FLAT, anchor='center', font=('Sylfaen 15'))
brl.place(x=60, y=120)

getBitcoin()

janela.mainloop()
