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
        'typo'       : 'Helvetica'     
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
 
    frame_return = tk.Frame(
                                     frame, 
                                     bg = theme['bg']
                            )
    
    for mode in cj['modes'].keys():
        frame_mode = tk.Frame(
                                frame_return,
                                bg = theme['bg']
                            )
        label_return = tk.Label( 
                                    frame_mode,
                                    text    = cj['!affichage'],
                                    justify = 'center',
                                    font    = (theme['typo'], 20), 
                                    bg      = theme['bg'], 
                                    fg      = theme['title']
                                )
        for temps in cj['modes'][mode].keys():
            if   isinstance(temps, list):
                """si liste"""
                
            elif isinstance(temps, str) :
                label_return2 = tk.Label( 
                                            frame_return,
                                            text    = cj['!affichage'][mode],
                                            justify = 'center',
                                            font    = (theme['typo'], 20), 
                                            bg      = theme['bg'], 
                                            fg      = theme['title']
                                        )
                
  #              for term in cj['modes'][mode][temps].keys():
  #                  label_return3 = tk.Label( 
  #                                              frame_return,
  #                                              text    = cj['!affichage'][mode][temps],
  #                                              justify = 'center',
  #                                              font    = (theme['typo'], 20), 
  #                                              bg      = theme['bg'], 
  #                                              fg      = theme['title']
  #                                          )
                label_return.pack()
                label_return2.pack()
  #              label_return3.pack()
    
        frame_mode.pack()
    frame_return.grid(row=2, column=0, sticky='n')
###############################################################################
"""
 - Gestion TKINTER
"""

window = tk.Tk() 

# Personnalisation
window.title('Le Petit Pascal')   # Nom à trouver
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

