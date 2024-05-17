# -*- coding: utf-8 -*-                                                       #
###############################################################################
#                                                                             #
#  ~ LE PETIT PASCAL ~                                                        #
#                                                                             #
#  -> par wilhelm43, wedego et IIlluX                                         #
#                                                                             #
###############################################################################
""" INITIALISATION DU LOGICIEL """
###############################################################################
print()
print(" | Le Petit Pascal")
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
        'title'      : '#ac2e55',
        'modes'      : '#eeeeee',
        'block'      : '#c8124b',
        'bg'         : '#1a0008',
        'bg_entry'   : '#660022',
        'bg_button'  : '#80002a',  
        'text_entry' : '#ffffff',
        'text_button': '#000000',
        'typo'       : 'Helvetica',
        'back'       : ['#a31743', '#0f9473', '#5a8bb7', '#df941b', '#885ca5', '#d04f32'],
        'back_1'     : ['#ac2e55', '#269e81', '#6a96be', '#e29e31', '#936cae', '#d46046'],
        'back_2'     : ['#b54568', '#3ea98f', '#8badcc', '#e5a948', '#9f7cb7', '#d9725a'],
        'back_3'     : ['#be5c7b', '#57b49d', '#8badcc', '#e8b45f', '#ab8cc0', '#de836f'],
        'conjugueur' : {
                         'bg'         : '#e01c57',
                         'labelMain'  : '#e79eb4',
                         'labelAlt'   : '#eeeeee',
                         'labelTerm'  : '#ffffff',
                         'labelTemps' : '#e01c57',
                         'frameMode'  : '#e79eb4',
                         'frameTemps' : '#eebbca'
                       }
        }
# Création de la fenêtre
window = tk.Tk() 
# Définitions des chemins
try                     :
    __img_path = "../"
    __img_z    = open(file = __img_path + "img/lpp.png")
except FileNotFoundError:
    try                     :
        __img_path = "/"
        __img_z    = open(file = __img_path + "img/lpp.png")
    except FileNotFoundError:  
        __img_path = ""
# Définitions des PARAMÈTRES
settings =  {
            'conjugueur' : {
                            'text_size' :   {
                                            'title': 2.3,
                                            'mode' : 1.8,
                                            'temps': 1.5,
                                            'terms': 1.2 
                                            },
                            'name'      :   'Le Petit Pascal [Résultat]'
                           },
            'recherche'  : {
                            'name'      :   'Le Petit Pascal'
                        }
            }
# Mise à jour des PARAMÈTRES
as_width  = window.winfo_screenwidth()
as_height = window.winfo_screenheight()
print(f" | Écran {as_width}x{as_height}")
for textsize in settings['conjugueur']['text_size'].keys(): settings['conjugueur']['text_size'][textsize] = int((as_width / 2560) * 10 * settings['conjugueur']['text_size'][textsize])
###############################################################################
print(" | Le Petit pascal  Copyright (C) 2024 WWX-Team (wilhelm43, wedego, Hilux")
print(" | This program comes with ABSOLUTELY NO WARRANTY; for details read license.")
print()
###############################################################################
###############################################################################
""" FONCTION AFFICHAGE """
###############################################################################

def conjuguer_fenêtre_verbe():
    """[Logiciel / Conjugeur / Résultat]: Affiche la fenêtre de résultat du verbe."""
    #### Import du verbe #################################
    verbe = entry_search.get()
    if len(verbe) <= 1: verbe = 'chanter'
    cj = conjuguer(verbe)
    if cj == None: return # retour si erreur
    #### Création de la fenêtre Tkinter ##################
    conjugeur_window = tk.Tk()
    conjugeur_window.title(settings['conjugueur']['name'])
    conjugeur_window.minsize(1440, 960)
    conjugeur_window.iconbitmap(__img_path + "img/LPP_only_logo.ico")
    conjugeur_window.config(background=theme['bg'])
    #### Création des frames « conteneuses » #############
    ligneSimple  = tk.Frame (
                                conjugeur_window,
                                bg = theme['conjugueur']['bg']
                            )
    ligneComposé = tk.Frame (
                                conjugeur_window,
                                bg = theme['conjugueur']['bg']
                            )
    celluleInfos = tk.Frame (
                                conjugeur_window,
                                bg = theme['conjugueur']['bg']
                            )
    #### Labels ##########################################
    labelSimple  = tk.Label (
                                ligneSimple, width = 1440,
                                text    = "Temps Simples", anchor = 'w', justify = 'left',
                                fg = theme['conjugueur']['labelMain'], font = (theme['typo'], settings['conjugueur']['text_size']['title']), bg = theme['conjugueur']['bg']
                                
                            ).pack(side = 'top', padx = 5, pady = 2)
    labelComposé = tk.Label (
                                ligneComposé, width = 1440,
                                text    = "Temps Composés", anchor = 'w', justify = 'left',
                                fg = theme['conjugueur']['labelMain'], font = (theme['typo'], settings['conjugueur']['text_size']['title']), bg = theme['conjugueur']['bg']
                            ).pack(side = 'top', padx = 5, pady = 2)
    labelInfos   = tk.Label (
                                celluleInfos, width = 1440,
                                text    = "Infos", anchor = 'w', justify = 'left',
                                fg = theme['conjugueur']['labelMain'], font = (theme['typo'], settings['conjugueur']['text_size']['title']), bg = theme['conjugueur']['bg']
                            ).pack(side = 'top', padx = 5, pady = 2)
    #### Boucles Simples, Composées ######################
    __composé = True
    for quelleFrame in [ligneSimple, ligneComposé]:
        __composé = not __composé
        frameLigne = tk.Frame   (
                                    quelleFrame,
                                    bg = theme['conjugueur']['bg']
                                )
        
        ### Affichage des Modes
        for mode in cj['modes'].keys():
            frameMode = tk.Frame    (
                                        frameLigne,
                                        bg = theme['conjugueur']['frameMode']
                                    )
            labelMode   = tk.Label  (
                                        frameMode,
                                        text = cj['!affichage']['?' + mode],
                                        fg   = theme['conjugueur']['labelAlt'], font = (theme['typo'], settings['conjugueur']['text_size']['mode']), bg = theme['conjugueur']['frameMode']
                                    ).pack(padx = 5, pady = 5)
            ### Affichage des Temps
            for temps in cj['modes'][mode].keys():
                if conjuger_an_temps_est_composé(mode = mode, temps = temps) == __composé:
                    frameTemps = tk.Frame   (
                                                frameMode,
                                                bg = theme['conjugueur']['frameTemps']
                                            )
                    labelTemps = tk.Label   (
                                                frameTemps,
                                                text = cj['!affichage'][mode]['?' + temps],
                                                bg = theme['conjugueur']['frameTemps'], font = (theme['typo'], settings['conjugueur']['text_size']['temps']), fg = theme['conjugueur']['labelTemps']
                                            ).pack(padx = 5, pady = 5)
                    
                    ### Affichage des terminaisons
                    for term in cj['modes'][mode][temps]:
                        if term != None: labelTermText = term
                        else           : labelTermText = ''
                        labelTerm = tk.Label( 
                                                    frameTemps,
                                                    text    = labelTermText,
                                                    bg      = theme['conjugueur']['frameTemps'], font = (theme['typo'], settings['conjugueur']['text_size']['terms']), fg = theme['conjugueur']['labelTerm']
                                                )
                        labelTerm.pack(padx = 0, pady = 0)
                    ### Pack du temps
                    frameTemps.pack(padx = 5, pady = 5, side='left')
            ### Pack du mode
            frameMode.pack(padx = 5, pady = 5, side='left') 
        frameLigne.pack(padx = 8, pady = 8, side='left')
    #### Informations ####################################
    frameInfos = tk.Frame (celluleInfos, bg = theme['conjugueur']['frameMode'])
    #####
    afficherInfosTop = {'!groupe' : 'Groupe'          , '!build' : 'Régularité', '!verbe' : 'Infinitif', '!participe_présent' : 'Participe présent'}
    afficherInfosBot = {'!term'   : 'Term. Infinitive', '!usage' : 'Usage'     , '!type'  : 'Type'     , '!participe_passé'   : 'Participe passé'  }
    #####
    __y = 0.04
    for ligne in [afficherInfosTop, afficherInfosBot]:
        __x = 0.01
        for key, obj in ligne.items():
            
            frameCelluleInfos = tk.Frame (frameInfos,   bg = theme['conjugueur']['frameTemps'])
            labelCelluleInfos = tk.Label (frameCelluleInfos, bg = theme['conjugueur']['frameTemps'], font = (theme['typo'], settings['conjugueur']['text_size']['mode']), fg = theme['conjugueur']['labelTemps'],
                                          text = obj
                                         ).pack(side = 'top')
            labelCelluleData  = tk.Label (frameCelluleInfos, bg = theme['conjugueur']['frameTemps'], font = (theme['typo'], settings['conjugueur']['text_size']['temps']), fg = theme['conjugueur']['labelTerm'],
                                          text = cj[key]
                                         ).pack(side = 'top')
            frameCelluleInfos.place(relx = __x, rely = __y, relwidth = 0.23, relheight = 0.42)
            __x += 0.25
        __y += 0.5
    #####
    frameInfos.place(relx = 0.025, rely = 0.225, relwidth = 0.95, relheight = 0.7)     
    #### Finitions #######################################
    ligneSimple .place(rely = 0.05, relx = 0, relwidth = 1, relheight = 0.30)
    ligneComposé.place(rely = 0.40, relx = 0, relwidth = 1, relheight = 0.30)
    celluleInfos.place(rely = 0.75, relx = 0.5, relwidth = 0.45, relheight = 0.2)
###############################################################################
###############################################################################
""" GESTION TKINTER ET LOGICIEL """
# Personnalisation de la fenêtre
window.title(settings['recherche']['name'])   
window.minsize(600, 560)
window.maxsize(960, 720)
window.iconbitmap(__img_path + "img/LPP_only_logo.ico")
window.config(background=theme['bg'])
# Contenu
frame = tk.Frame(window, bg = theme['bg'])
# IMG
frame_title      = tk.Frame(frame, bg = theme['bg'])
frame_title_img = tk.PhotoImage(file = __img_path + "img/lpp.png")
frame_title_lb = tk.Label(frame_title, bg = theme['bg'], image = frame_title_img)
frame_title_lb.image = frame_title_img
frame_title_lb.pack(side = 'top')
frame_title.pack(side='top')
# Entrée et Bouton
frame_input = tk.Frame (window, bg = theme['block'], padx = 15, pady = 10)
entry_search = tk.Entry(frame_input, font = (theme['typo'], 20), bg   = theme['bg_entry'], fg   = theme['text_entry'])
entry_search.config(highlightthickness = 2, highlightbackground = theme["modes"], highlightcolor= theme["modes"])
entry_search.pack(pady=5, fill='x')
button_search = tk.Button(
                            frame_input,  
                            text             = 'Conjuguer', 
                            font             = (theme['typo'], 20), 
                            bg               = theme['bg_button'], 
                            fg               = theme['text_button'],
                            command          = conjuguer_fenêtre_verbe
                         )
button_search.config(highlightthickness = 2, highlightbackground = theme["modes"], highlightcolor= theme["modes"])
button_search.pack  (pady=5, fill='x')
frame_input.place   (relx = 0, relwidth = 1, y = 420)
# MAIN
frame.pack(side='top')
###############################################################################
###############################################################################
""" LOGICIEL """
###############################################################################
window.mainloop()
###############################################################################
###############################################################################
