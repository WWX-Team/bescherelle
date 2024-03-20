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
import tkinter
import scripts

theme = {
        'title'      : '#b21948',
        'bg'         : '#000000',
        'bg_input'   : '#b21948',
        'text_input' : 'white',
        'typo'       : 'Arial'
        }
###############################################################################
"""
 - Gestion TKINTER
"""

window = tkinter.Tk() 

# Personnalisation
window.title('Bescherelle')   # Nom à trouver
window.geometry('1080x720')
window.minsize(480, 360)
#window.iconbitmap()
window.config(background=theme['bg'])
              
# Titre
frame = tkinter.Frame(window, bg=theme['bg'])

label_title = tkinter.Label(frame, text='TITRE', font=(theme['typo'], 60), bg=theme['bg'], fg=theme['title'])   # typo à trouver
label_title.pack(pady=25, expand='YES')



# Input 
frame_input = tkinter.Frame(frame, bg=theme['bg'])
                            
entry_search = tkinter.Entry(frame_input, font=(theme['typo'], 20), bg=theme['bg_input'], fg=theme['text_input'])
verbe = entry_search.get()
entry_search.pack()

button_search = tkinter.Button(frame_input, text='Rechercher', font=(theme['typo'],20), bg=theme['bg_input'], fg=theme['text_input'], command=scripts.conjuguer)
button_search.pack(pady=10, fill='x')

frame_input.pack() 



frame.pack(side='top')                           

###############################################################################
"""
 - Boucle principale
"""
window.mainloop()

