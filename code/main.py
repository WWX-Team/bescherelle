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
# Sur certains OS, nommé tkinter, d'autres, Tkinter, ce court code résoud cette division.
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
# Import des FONCTIONS LOCALES
from scripts import conjuguer, conjuger_an_temps_est_composé
# Définitions des THÈMES
theme = {
        'title'      : '#80002a',
        'bg'         : '#1a0008',
        'bg_entry'   : '#660022',
        'bg_button'  : '#80002a',  
        'text_entry' : 'white',
        'text_button': 'white',
        'typo'       : 'Helvetica',
        'back'       : ['#a31743', '#0f9473', '#5a8bb7', '#df941b', '#885ca5', '#d04f32'],
        'back_1'     : ['#ac2e55', '#269e81', '#6a96be', '#e29e31', '#936cae', '#d46046'],
        'back_2'     : ['#b54568', '#3ea98f', '#8badcc', '#e5a948', '#9f7cb7', '#d9725a'],
        'back_3'     : ['#be5c7b', '#57b49d', '#8badcc', '#e8b45f', '#ab8cc0', '#de836f']
        }
###############################################################################
"""
 - Fonction affichage
"""
 
def conjuguer_return(x : int = 0, y : int = 0):
    """
    affiche la fonction [conjuguer] de [scripts.py] après que l'utilisateur ait cliqué sur [button_search]
    """
    verbe = entry_search.get()
    if len(verbe) <= 1: verbe = 'chanter'
    cj = conjuguer(verbe)
    if cj == None: return
    
    window_return = tk.Tk()
    window_return.title('Le Petit Pascal')   
    window_return.geometry('960x720')
    window_return.minsize(960, 720)
    window_return.maxsize(960, 1920)
    window_return.iconbitmap("../img/LPP_only_logo.ico")
    window_return.config(background=theme['bg']) 
    
    columnSimple  = tk.Frame(window_return, bg = '#565656')
    columnComposé = tk.Frame(window_return, bg = '#565656')
    
    columnSimple.place (relx= 0.1,  rely= 0, relwidth = 0.3, relheight = 1)
    columnComposé.place(relx= 0.6,  rely= 0,  relwidth = 0.3, relheight = 1)
    __composé = True
    print()
    for quelle_frame in (columnSimple, columnComposé):
        if __composé :
            __composé   = False
            __composé_t = "Temps Simples"
        else         :
            __composé   = True
            __composé_t = "Temps Composés"
        
        aligner_modes = tk.Frame(
                                quelle_frame,
                                bg = theme['title']
                             )
        type_temps   = tk.Label( 
                                    aligner_modes,
                                    text    = __composé_t,
                                    justify = 'center',
                                    font    = (theme['typo'], 15), 
                                    bg = '#242424',
                                    fg = 'white'
                                )
        type_temps.pack()
        # Break
        iteration = 0
        for mode in cj['modes'].keys():
            # BREAK 
            frame_mode = tk.Frame(
                                aligner_modes,
                                bg = theme['back'][iteration % len(theme['back'])],
                             )
            # BREAK
            label_return = tk.Label( 
                                    frame_mode,
                                    text    = cj['!affichage']['?' + mode],
                                    justify = 'center',
                                    font    = (theme['typo'], 12), 
                                    bg      = theme['back'][iteration % len(theme['back'])], 
                                    fg      = 'white'
                                )
            label_return.pack()
            # BREAK 
            for temps in cj['modes'][mode].keys():
                if conjuger_an_temps_est_composé(mode = mode, temps = temps) == __composé:
                    frame_temps = tk.Frame(
                                            frame_mode,
                                            bg = theme['back_1'][iteration % len(theme['back'])]
                                       )
                    #                                      
                    label_return2 = tk.Label( 
                                            frame_temps,
                                            text    = cj['!affichage'][mode]['?' + temps],
                                            justify = 'center',
                                            font    = (theme['typo'], 10), 
                                            bg      = theme['back_1'][iteration % len(theme['back'])], 
                                            fg      = 'white'
                                        )
                    label_return2.pack()
                    #              
                    frame_term = tk.Frame(
                                                frame_temps,
                                                bg = theme['back_2'][iteration % len(theme['back'])]
                                           )
                    for term in cj['modes'][mode][temps]:
                        if term != None:        label_return3 = tk.Label( 
                                                frame_term,
                                                text    = term,
                                                justify = 'center',
                                                font    = (theme['typo'], 9), 
                                                bg      = theme['back_2'][iteration % len(theme['back'])], 
                                                fg      = 'white'
                                            )
                        # BREAK
                        label_return3.pack()
                    frame_term.pack()
                    frame_temps.pack(padx=10, pady=1)
                    # BREAK
            frame_mode.pack()
            iteration += 1
        aligner_modes.place(relx= 0.1, rely= 0,  relwidth = 0.8, relheight = 1)
        aligner_modes.pack()
    # BREAK    
    window_return.mainloop()

###############################################################################
"""
 - Gestion TKINTER
"""

window = tk.Tk() 

# Personnalisation
window.title('Le Petit Pascal')   
window.minsize(480, 360)
window.minsize(960, 720)
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

image_logo = tk.PhotoImage(file = "../img/lpp.png")

canvas_logo = tk.Canvas(
                                frame_title,
                                width              = 560,
                                height             = 359,
                                bg                 = theme['bg'],
                                bd                 = 0,
                                highlightthickness = 0
                        )
canvas_logo.create_image(560/2, 359/2, image=image_logo)
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
