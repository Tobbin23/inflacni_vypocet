"""
	__autor__ = Tobbin23
	__verse__ = 1.2
"""
import PySimpleGUI as sg
import math
from PIL import Image
import io
#sg.theme("LightBlue")
sg.change_look_and_feel("DarkGray")
sg.set_options(font=("TESET",20))
sg.theme_button_color((sg.theme_background_color(), sg.theme_background_color()))
sg.theme_border_width(0)
def ama(f="./image/Draw_money.png", maxsize=(400,200)):
    img = Image.open(f)
    img.thumbnail(maxsize)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()

image_exit = "./image/Action-exit-icon.png"
image_dolar = "./image/USD.png"
image_trash = "./image/trash2.png"
layout1 = [[sg.Image(data=ama(),size=(400,200),key="-mage-")],
           [sg.Text("Tobbin23",size=(20,2), pad=(80,2))]]

layout2 = [[sg.Text('Zjistěte, jak inflace ovliňuje vaše úspory',size=(40,2))],
           
           [sg.Text("Úspory",size=(7,1), 
                    pad=(5,2)), sg.Input(size=(25,25),
                                         key='-castka-',
                                         background_color="black",
                                         text_color="Lime",
                                         pad=(10,1), 
                                         justification="center"),
            sg.Text("KČ", size=(5,1))],
           
           [sg.Text("Inflace",size=(7,1),
                    pad=(5,2)),sg.Input(size=(25,25), 
                                        justification="center",
                                        pad=(10,1),
                                        background_color="black",
                                        text_color="Lime",
                                        key='-inflace-'),
            sg.Text("%", size=(2,0))],
           
        
           [sg.Text("Roky",size=(4,1)),sg.Input(size=(25,25),
                                                
                                                justification="center",
                                                pad=(60,0),
                                                background_color="black",
                                                text_color="Lime",
                                                key='-roky-')],
           
           [sg.Output(size=(30,4),key="-OUT-",
                      background_color="blue",
                      text_color="white",
                      pad=(60,8))],
           
           [sg.Button(image_filename=image_dolar,
                      image_size=(60,50),
                      image_subsample=2,
                      bind_return_key=True,
                      pad=(80,1),
                      key=("-Spocite-")
                      ),
            
            sg.Button(image_filename=image_exit,
                      image_size=(80,60),
                      image_subsample=2,
                      key="Exit"),
            sg.Button(image_filename=image_trash,
                      size=(10,1), pad=(80,0),
                      key="-smazat-")]
           #[sg.Text("__autor__Tobbin23")]
           ]
layout = [[sg.Column(layout1),
           sg.Column(layout2)]]
#vr = [[sg.Column(layout ,element_justification="center")]]
window = sg.Window("Inflační kalkulačka", 
                   layout,
                   icon=r"./image/cash.png",
                   grab_anywhere=True,
                   )



while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event =="Exit":
        break
            
    elif event == "-smazat-":    
        window.find_element("-OUT-").Update("")    
    elif event:
        try:
            max_line = 2
            out = ""
            castka = int(values['-castka-'])
            inflace = float(values['-inflace-'])
            roky = int(values["-roky-"])
            vypocet = castka * (math.pow(1 / ( 1 + inflace / 100) , roky))
            
            rozdil = castka - vypocet
            vysledek = (f"{round(vypocet, 2)}Kč rozdil -{round(rozdil, 2)}Kč\t")
            for i in vysledek:
                out += i
                                
            print(out)

            
                
        except:
            vysledek = 'Invalid'
            #rozdil = "Invalid"
            
        
        #window["-OUT-"].update(vysledek, out)
        
    else:
        break
