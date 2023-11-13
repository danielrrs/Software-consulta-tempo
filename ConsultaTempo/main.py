import tkinter
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

import requests
from datetime import datetime
import json

import pytz
import pycountry_convert as pc


cor_preta = "#444466"
cor_branco = "#feffff"
cor_azul = "#6f9fbd"

fundo_dia = "#00BFFF"
fundo_tarde = "#DAA520"
fundo_noite = "#483D8B"

fundo = fundo_dia


janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient = HORIZONTAL).grid(row = 0, columnspan = 1, ipadx = 157)


frame_top = Frame(janela, width=320, height=50, bg=fundo, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_body = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_body.grid(row=2, column=0, sticky=NW)


estilo = ttk.Style(janela)
estilo.theme_use('clam')

global imagem


#função de retorno das informações

def informacao():
    
    chave_api = "a94117987ef6b55c1bc18ba716a0da6b"
    cidade = e_local.get()
    api_link ='https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&lang=pt_br'.format(cidade,chave_api)


    r = requests.get(api_link)

    dados = r.json()
    

    pais_codigo = dados['sys']['country']


    fuso_horario = pytz.country_timezones[pais_codigo]


    pais = pytz.country_names[pais_codigo] 


    zona = pytz.timezone(fuso_horario[0])
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")



    Calculo_kelvin_Celcius = dados['main']['temp'] - 273.15
    temperatura_celcius = int(Calculo_kelvin_Celcius) 
    pressao = dados['main']['pressure']
    umidade = dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descricao = dados['weather'][0]['description']


    def pais_to_continente(p):
        pais_alpha = pc.country_name_to_country_alpha2(p)
        pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)
        
        return pais_continente_nome

    continente = pais_to_continente(pais)
    
    
    

    l_cidade['text'] = cidade + " - " + pais + " / " + continente
    l_data['text'] = zona_horas
    l_temperatura['text'] = temperatura_celcius
    l_clima['text'] ="Céu: "+str(descricao)
    l_pressao['text'] = "Pressão: "+str(pressao)
    l_velocidade['text'] = "Velocidade: "+str(velocidade)
    l_simbolo['text'] = '°'
    
    
    
    
 #troca dos fundos
 
    zona_periodo = datetime.now(zona)
    zona_periodo = zona_periodo.strftime("%H") 
    
    global imagem
    
    zona_periodo = int(zona_periodo)
        
    if 6<= zona_periodo < 12:
        imagem = Image.open('imagens/soldodia.png')
        fundo = fundo_dia
    
    elif 12<= zona_periodo < 18:
        imagem = Image.open('imagens/soldatarde.png')
        fundo = fundo_tarde
        
    else:
        imagem = Image.open('imagens/lua.png')
        fundo = fundo_noite

        
    imagem = imagem.resize((130,130))
    imagem = ImageTk.PhotoImage(imagem)

    l_icon = Label(frame_body, image=imagem, bg=fundo)
    l_icon.place(x=180, y=50) 
            
            
    janela.configure(bg=fundo)
    frame_top.configure(bg=fundo)
    frame_body.configure(bg=fundo)
        
    l_cidade['bg'] = fundo
    l_data['bg'] = fundo
    l_temperatura['bg'] = fundo
    l_clima['bg'] = fundo
    l_velocidade['bg'] = fundo
    l_simbolo['bg'] = fundo
    l_pressao['bg'] = fundo
    
        
    
    
       
    
    

    codigo_pais = pc.country_name_to_country_alpha2("China", cn_name_format="default")
    continente_nome = pc.country_alpha2_to_continent_code(codigo_pais)


#frametop config

e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)
bot_ver = Button(frame_top, command=informacao, text='Ver Clima', bg=cor_branco, fg= cor_preta,font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE)
bot_ver .place(x=250, y=10) 

#framebody config

l_cidade = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_branco,font=("Arial 14"))
l_cidade.place(x=10, y=4) 

l_data  = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_branco,font=("Arial 10"))
l_data.place(x=10, y=54) 

l_temperatura = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_branco,font=("Arial 45"))
l_temperatura.place(x=10, y=100) 

l_simbolo = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_branco,font=("Arial 30 bold "))
l_simbolo.place(x=85, y=110) 

l_nome = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_branco,font=("Arial 10"))
l_nome.place(x=85, y=140) 


l_pressao = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_branco,font=("Arial 10"))
l_pressao.place(x=10, y=185) 

l_velocidade = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_branco,font=("Arial 10"))
l_velocidade.place(x=10, y=212) 


l_clima = Label(frame_body, text='', anchor='center',bg=fundo, fg=cor_branco,font=("Arial 10"))
l_clima.place(x=150, y=190) 



janela.mainloop()

