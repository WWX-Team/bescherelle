# -*- coding: utf-8 -*-
"""

"""
###############################################################################
#                                                                             #
#  ~ TROPHÉE NSI                                                           ~  #
#                                                                             #
#  - Projet proposé par Wilhelm, Anselme et Lorick                            #
#                                                                             #
#  #########################################################################  #
#  #                                                                       #  #
#  #                                                                       #  #
#  #                                                                       #  #
#  #                                                                       #  #
#  #                                                                       #  #
#  #########################################################################  #
#                                                                             #
###############################################################################
"""
 - Initialisation du programme
"""
###############################################################################
# Import des MODULES
import tkinter as tk
from scripts import conjuguer

theme = {
        'title'      : '#80002a',
        'bg'         : '#1a0008',
        'bg_entry'   : '#660022',
        'bg_button'  : '#80002a',  
        'text_entry' : 'white',
        'text_button': 'white',
        'typo'       : 'Helvetica',
        'back'       : ['#a31743', '#96b2cb', '#e1b876', '#274e13', '#7c608f', '#f45f59']
        }
###############################################################################
"""
 - Fonction affichage
"""
 
def conjuguer_return():
    """
    affiche la fonction [conjuguer] de [scripts.py] après que l'utilisateur 
    ai cliqué sur [button_search]
    """
    verbe = entry_search.get()
    cj = conjuguer(verbe)
    
    window_return = tk.Tk()
    window_return.title('Le Petit Pascal')   
    window_return.geometry('1080x720')
    window_return.minsize(480, 360)
    window_return.iconbitmap("../img/LPP_only_logo.ico")
    window_return.config(background=theme['bg'])
    
    frame_return = tk.Frame(
                                window_return, 
                                bg = theme['bg']
                            )
    
    row = 0
    iteration = 0
    
    for mode in cj['modes'].keys():
        frame_gen = tk.Frame(
                                frame_return,
                                bg = theme['back'][iteration % len(theme['back'])]
                             )
        
        frame_mode = tk.Frame(
                                frame_gen,
                                bg = theme['back'][iteration % len(theme['back'])]
                             )
        
        label_return = tk.Label( 
                                    frame_mode,
                                    text    = cj['!affichage']['?' + mode],
                                    justify = 'center',
                                    font    = (theme['typo'], 20), 
                                    bg      = theme['back'][iteration % len(theme['back'])], 
                                    fg      = 'white'
                                )
        
        label_return.pack()       
        frame_mode.grid(row=row, column=0, sticky='w') 
        
        row += 1
        
        for temps in cj['modes'][mode].keys():
            if   isinstance(cj['modes'][mode][temps], str):
                """si liste"""
                
            elif isinstance(cj['modes'][mode][temps], list) :
                frame_temps = tk.Frame(
                                            frame_gen,
                                            bg = theme['back'][iteration % len(theme['back'])]
                                       )                                              
                                                        
                label_return2 = tk.Label( 
                                            frame_temps,
                                            text    = cj['!affichage'][mode]['?' + temps],
                                            justify = 'center',
                                            font    = (theme['typo'], 10), 
                                            bg      = theme['back'][iteration % len(theme['back'])], 
                                            fg      = 'white'
                                        )
                
                label_return2.pack()
                frame_temps.grid(row=row, column=0, sticky='w')
                
                
                
                for term in cj['modes'][mode][temps]:
                    frame_term = tk.Frame(
                                                frame_gen,
                                                bg = theme['back'][iteration % len(theme['back'])]
                                           )
                    
                    label_return3 = tk.Label( 
                                                frame_term,
                                                text    = term,
                                                justify = 'center',
                                                font    = (theme['typo'], 10), 
                                                bg      = theme['back'][iteration % len(theme['back'])], 
                                                fg      = 'white'
                                            )
                    
                    label_return3.pack()
                    frame_term.grid(row=row, column=1, sticky='w')
                
                row += 1
                
        frame_gen.pack()
        
        iteration += 1
           
    frame_return.pack(side='top')
    
    window_return.mainloop()
###############################################################################
"""
 - Gestion TKINTER
"""

window = tk.Tk() 

# Personnalisation
window.title('Le Petit Pascal')   
window.geometry('1080x720')
window.minsize(480, 360)
window.iconbitmap("../img/LPP_only_logo.ico")
window.config(background=theme['bg'])
              
frame = tk.Frame(
                    window, 
                    bg = theme['bg']
                )

frame_title = tk.Frame(
                            frame,
                            bg = theme['bg']
                       )

# Image
image_logo = tk.PhotoImage(
                                file="../img/lpp.png"
                            )

canvas_logo = tk.Canvas(
                                frame_title,
                                width              = 560,
                                height             = 359,
                                bg                 = theme['bg'],
                                bd                 = 0,
                                highlightthickness = 0
                        )
canvas_logo.create_image(560/2,359/2, image=image_logo)
canvas_logo.pack()

frame_title.grid(row=0, column=0, sticky='n', pady=20)

# Input
frame_input = tk.Frame(
                                frame, 
                                bg = theme['bg']
                        )

entry_search = tk.Entry(
                                frame_input, 
                                font = (theme['typo'], 20), 
                                bg   = theme['bg_entry'], 
                                fg   = theme['text_entry']
                        )
entry_search.pack()

button_search = tk.Button(
                                frame_input,  
                                text             = 'Rechercher', 
                                font             = (theme['typo'],20), 
                                bg               = theme['bg_button'], 
                                fg               = theme['text_button'],
                                activebackground = theme['bg_entry'],
                                relief           = 'raised',
                                command          = conjuguer_return
                          )
button_search.pack(pady=10, fill='x')

frame_input.grid(row=1, column=0, sticky='s', pady=20) 



frame.pack(side='top')                           

###############################################################################
"""
 - Boucle principale
"""
window.mainloop()
 - Boucle principale
"""
window.mainloop()

