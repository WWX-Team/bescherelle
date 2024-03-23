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
    
    frame_return = tk.Frame(
                                     frame, 
                                     bg   = theme['bg']
                            )

    label_return = tk.Label( 
                                     frame_return,
                                     text = conjuguer(verbe),
                                     justify = 'center',
                                     font = (theme['typo'], 20), 
                                     bg   = theme['bg'], 
                                     fg   = theme['title']
                            )
    label_return.pack()
    
    frame_return.pack(side='bottom')
###############################################################################
"""
 - Gestion TKINTER
"""

window = tk.Tk() 

# Personnalisation
window.title('Bescherelle')   # Nom à trouver
window.geometry('1080x720')
window.minsize(480, 360)
#window.iconbitmap()
window.config(background=theme['bg'])
              
# Titre
frame = tk.Frame(window, bg=theme['bg'])

label_title = tk.Label(
                                frame, 
                                text = 'Le Saint Bescherelle', 
                                font = ('Impact', 60), 
                                bg   = theme['bg'], 
                                fg   = theme['title']
                        )  
 
label_title.pack(pady=25, expand='YES')



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
                                 text    = 'Rechercher', 
                                 font    = (theme['typo'],20), 
                                 bg      = theme['bg_button'], 
                                 fg      = theme['text_button'], 
                                 command = conjuguer_return
                          )
button_search.pack(pady=10, fill='x')

frame_input.pack() 



frame.pack(side='top')                           

###############################################################################
"""
 - Boucle principale
"""
window.mainloop()
