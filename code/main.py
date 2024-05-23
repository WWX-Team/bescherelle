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
print(" | Le Petit Pascal - Copyright (C) 2024 wilhelm43, wedego, Hilux")
###############################################################################
# Importation des LIBRAIRIES ##################################################
try                : import tkinter as tk
except ImportError : import Tkinter as tk
except ImportError : print(" | ERROR | python/tkinter is missing ")
# Importation des LIBRAIRIES LOCALES ##########################################
from scripts import conjuguer, conjuger_an_temps_est_composé
from tabs    import app_themes, app_settings, app_translations, Path, Themes
###############################################################################
# Création de la fenêtre ######################################################
window  = tk.Tk() 
windows = []
###############################################################################
# Fonctions REFRSH ############################################################
def window_refresh(target, child : bool = False):
    """[Logiciel / Rafraîchisseur de fenêtre]"""
    if not (isinstance(target, tk.Tk) or isinstance(target, tk.Frame)): return
    if not child : print(" | ––– | reload | ")
    if len(target.children.items()) == 0 : return
    for element in target.children.keys():
        window_refresh_child(target.children[element])
    window_refresh_child(target, True)
    
def window_refresh_child(target, back : bool = False):
    """[Logiciel / Rafraîchisseur de fenêtre / Enfant]"""
    if (isinstance(target, tk.Tk) or isinstance(target, tk.Frame)) and not back:
        if  len(target.children.items()) > 0: window_refresh(target, True)
    if isinstance(target, str) : return
    as_dict = target.__dict__
    if 'path' in as_dict :
        as_dict = as_dict['path']
        if 'bg' in as_dict                      :  target.config(bg   = as_dict['bg'].get(var = 'theme'))
        if 'fg' in as_dict                      :  target.config(fg   = as_dict['fg'].get(var = 'theme'))
        if 'ft' in as_dict and 'fs' in as_dict  :  target.config(font = (as_dict['ft'].get(var = 'theme'), as_dict['fs'].get(var = 'settings')))
        if 'txt' in as_dict                     :  target.config(text = as_dict['txt'].get(var = 'translations'))

###############################################################################
# Définitions des THÈMES ######################################################
def window_theme(vl : int = 1):
    global theme
    app_themes.change_theme(vl)
    theme = app_themes.theme
    print(" | ––– | themes | reload | theme \'" + str(theme['name']) + "\' by \'" + str(theme['author']) + "\'")
    window_refresh(target = window, child = True)
    __windows_idx = 0
    while __windows_idx < (len(windows)):
        try    : window_refresh(target = windows[__windows_idx])
        except : windows.pop(__windows_idx)
        __windows_idx += 1

window_theme(0)
# Définitions des chemins #####################################################
__img_path = 'error'
__img_build_paths = ["../", "/", ""]
for path in __img_build_paths:
    __img_build_valid = True
    try                     : open(file = path + "img/lpp.png")
    except FileNotFoundError: __img_build_valid = False
    if __img_build_valid: __img_path = path
# Définitions des PARAMÈTRES ##################################################
as_width  = window.winfo_screenwidth()
as_height = window.winfo_screenheight()
print(f" | Screen {as_width}x{as_height}")
for textsize in app_settings['conjugueur']['text_size'].keys(): app_settings['conjugueur']['text_size'][textsize] = int((as_width / 2560) * 10 * app_settings['conjugueur']['text_size'][textsize])
###############################################################################
print(" | This program comes with ABSOLUTELY NO WARRANTY.")
print()
print(" | RUN | ")
###############################################################################
###############################################################################
""" FONCTION AFFICHAGE """
###############################################################################
def conjuguer_fenêtre_création(search : str = 'chanter') -> tk.Tk :
    """[Logiciel / Conjugeur / Résultat]: Retourne la fenêtre de résultat du verbe."""
    #### Import du verbe #################################
    verbe = search
    if len(verbe) <= 1: verbe = 'chanter'
    cj = conjuguer(verbe)
    if cj == None: return 'error'
    #### Création de la fenêtre Tkinter ##################
    conjugeur_window = tk.Tk()
    conjugeur_window.title(app_settings['conjugueur']['name'])
    conjugeur_window.minsize(1440, 960)
    conjugeur_window.config(background=theme['principal']['bg'])
    conjugeur_window.__dict__['path'] = {'bg' : Path('principal/bg/')}
    #### Création des frames « conteneuses » #############
    ligneSimple                   = tk.Frame (conjugeur_window, bg = theme['conjugueur']['bg'])
    ligneSimple.__dict__['path']  = {'bg' : Path('conjugueur/bg/')}
    ligneComposé                  = tk.Frame (conjugeur_window, bg = theme['conjugueur']['bg'])
    ligneComposé.__dict__['path'] = {'bg' : Path('conjugueur/bg/')}
    celluleInfos                  = tk.Frame (conjugeur_window, bg = theme['conjugueur']['bg'])
    celluleInfos.__dict__['path'] = {'bg' : Path('conjugueur/bg/')}
    #### Labels ##########################################
    labelSimple                   = tk.Label (ligneSimple, width = 1440, text = "Temps Simples", anchor = 'w', justify = 'left', fg = theme['conjugueur']['label']['main'], font = (theme['principal']['txt']['font'], app_settings['conjugueur']['text_size']['title']), bg = theme['conjugueur']['bg'])
    labelSimple.__dict__['path']  = {'bg' : Path('conjugueur/bg/'), 'fg' : Path('conjugueur/label/main/')}
    labelSimple.pack(side = 'top', padx = 5, pady = 2)
    labelComposé                  = tk.Label (ligneComposé, width = 1440, text = "Temps Composés", anchor = 'w', justify = 'left', fg = theme['conjugueur']['label']['main'], font = (theme['principal']['txt']['font'], app_settings['conjugueur']['text_size']['title']), bg = theme['conjugueur']['bg'])
    labelComposé.__dict__['path'] = {'bg' : Path('conjugueur/bg/'), 'fg' : Path('conjugueur/label/main/')}
    labelComposé.pack(side = 'top', padx = 5, pady = 2)
    labelInfos                    = tk.Label (celluleInfos, width = 1440, text = "Infos", anchor = 'w', justify = 'left', fg = theme['conjugueur']['label']['main'], font = (theme['principal']['txt']['font'], app_settings['conjugueur']['text_size']['title']), bg = theme['conjugueur']['bg'])
    labelInfos.__dict__['path']   = {'bg' : Path('conjugueur/bg/'), 'fg' : Path('conjugueur/label/main/')}
    labelInfos.pack(side = 'top', padx = 5, pady = 2)
    #### Boucles Simples, Composées ######################
    __composé = True
    for quelleFrame in [ligneSimple, ligneComposé]:
        __composé = not __composé
        frameLigne                  = tk.Frame   (quelleFrame, bg = theme['conjugueur']['bg'])
        frameLigne.__dict__['path'] = {'bg' : Path('conjugueur/bg/')}
        ### Affichage des Modes
        for mode in cj['modes'].keys():
            frameMode                  = tk.Frame(frameLigne, bg = theme['conjugueur']['frame']['mode'])
            frameMode.__dict__['path'] = {'bg' : Path('conjugueur/frame/mode/')}
            labelMode = tk.Label(frameMode, text = cj['!affichage']['?' + mode], fg = theme['conjugueur']['label']['mode'], font = (theme['principal']['txt']['font'], app_settings['conjugueur']['text_size']['mode']), bg = theme['conjugueur']['frame']['mode'])
            labelMode.__dict__['path'] = {'bg' : Path('conjugueur/frame/mode/'), 'fg' : Path('conjugueur/label/mode/')}
            labelMode.pack(padx = 5, pady = 5)
            ### Affichage des Temps
            for temps in cj['modes'][mode].keys():
                if conjuger_an_temps_est_composé(mode = mode, temps = temps) == __composé:
                    frameTemps                  = tk.Frame   (frameMode, bg = theme['conjugueur']['frame']['temps'])
                    frameTemps.__dict__['path'] = {'bg' : Path('conjugueur/frame/temps/')}
                    labelTemps                  = tk.Label   (frameTemps, text = cj['!affichage'][mode]['?' + temps], bg = theme['conjugueur']['frame']['temps'], font = (theme['principal']['txt']['font'], app_settings['conjugueur']['text_size']['temps']), fg = theme['conjugueur']['label']['temps'])
                    labelTemps.__dict__['path'] = {'bg' : Path('conjugueur/frame/temps/'), 'fg' : Path('conjugueur/label/temps/')}
                    labelTemps.pack(padx = 5, pady = 5)    
                    ### Affichage des terminaisons
                    for term in cj['modes'][mode][temps]:
                        if term != None: labelTermText = term
                        else           : labelTermText = ''
                        labelTerm                  = tk.Label(frameTemps, text = labelTermText, bg = theme['conjugueur']['frame']['temps'], font = (theme['principal']['txt']['font'], app_settings['conjugueur']['text_size']['terms']), fg = theme['conjugueur']['label']['term'])
                        labelTerm.__dict__['path'] = {'bg' : Path('conjugueur/frame/temps/'), 'fg' : Path('conjugueur/label/term/')}
                        labelTerm.pack(padx = 0, pady = 0)
                    ### Pack du temps
                    frameTemps.pack(padx = 5, pady = 5, side='left')
            ### Pack du mode
            frameMode.pack(padx = 5, pady = 5, side='left') 
        frameLigne.pack(padx = 8, pady = 8, side='left')
    #### Informations ####################################
    frameInfos                  = tk.Frame (celluleInfos, bg = theme['conjugueur']['frame']['mode'])
    frameInfos.__dict__['path'] = {'bg' : Path('conjugueur/frame/mode/')}
    #####
    afficherInfosTop = {'!groupe' : 'Groupe'          , '!build' : 'Régularité', '!verbe' : 'Infinitif', '!participe_présent' : 'Participe présent'}
    afficherInfosBot = {'!term'   : 'Term. Infinitive', '!usage' : 'Usage'     , '!type'  : 'Type'     , '!participe_passé'   : 'Participe passé'  }
    #####
    __y = 0.04
    for ligne in [afficherInfosTop, afficherInfosBot]:
        __x = 0.01
        for key, obj in ligne.items():
            
            frameCelluleInfos                  = tk.Frame (frameInfos, bg = theme['conjugueur']['frame']['temps'])
            frameCelluleInfos.__dict__['path'] = {'bg' : Path('conjugueur/frame/temps/')}
            labelCelluleInfos                  = tk.Label (frameCelluleInfos, bg = theme['conjugueur']['frame']['temps'], font = (theme['principal']['txt']['font'], app_settings['conjugueur']['text_size']['mode']), fg = theme['conjugueur']['label']['temps'],
                                                           text = obj)
            labelCelluleInfos.__dict__['path'] = {'bg' : Path('conjugueur/frame/temps/'), 'fg' : Path('conjugueur/label/temps/')}
            labelCelluleInfos.pack(side = 'top')
            labelCelluleData                   = tk.Label (frameCelluleInfos, bg = theme['conjugueur']['frame']['temps'], font = (theme['principal']['txt']['font'], app_settings['conjugueur']['text_size']['temps']), fg = theme['conjugueur']['label']['term'],
                                                           text = cj[key])
            labelCelluleData.__dict__['path']  = {'bg' : Path('conjugueur/frame/temps/'), 'fg' : Path('conjugueur/label/term/')}
            labelCelluleData.pack(side = 'top')
            frameCelluleInfos.place(relx = __x, rely = __y, relwidth = 0.23, relheight = 0.42)
            __x += 0.25
        __y += 0.5
    #####
    frameInfos.place(relx = 0.025, rely = 0.225, relwidth = 0.95, relheight = 0.7)     
    #### Finitions #######################################
    ligneSimple .place(rely = 0.05, relx = 0, relwidth = 1, relheight = 0.30)
    ligneComposé.place(rely = 0.40, relx = 0, relwidth = 1, relheight = 0.30)
    celluleInfos.place(rely = 0.75, relx = 0.5, relwidth = 0.45, relheight = 0.2)
    return conjugeur_window

def conjuguer_fenêtre():
    """[Logiciel / Conjugeur]"""
    print(" | ––– | search | verbe : \'" + str(entry_search.get()) + "\'")
    global windows
    __window = conjuguer_fenêtre_création(search = entry_search.get())
    if isinstance(__window, str) :
        print(" | ––– | search | invalid search")
    else                         :
        windows.append(__window)
        __window.mainloop()
    
###############################################################################
###############################################################################
""" GESTION TKINTER ET LOGICIEL """
###############################################################################
# Personnalisation de la fenêtre
window.title(app_settings['recherche']['name'])   
window.minsize(700, 650)
window.maxsize(960, 650)
window.config(bg = theme['principal']['bg'])
window.__dict__['path'] = {'bg': Path(value = 'principal/bg/')}
# Contenu
frame = tk.Frame(window, )
# Image LOGO
if __img_path != 'error':
    try    : frame_title_img = tk.PhotoImage(file = __img_path + "img/lpp.png")
    except : __img_path = 'error'
    if __img_path != 'error':
        frame_title      = tk.Frame(window, bg = theme['principal']['bg'])
        frame_title.__dict__['path'] = {'bg': Path(value = 'principal/bg/')}
        frame_title_lb = tk.Label(frame_title, bg = theme['principal']['bg'], image = frame_title_img)
        frame_title_lb.__dict__['path'] = {'bg': Path(value = 'principal/bg/')}
        frame_title_lb.image             = frame_title_img
        frame_title_lb.pack(side = 'top')
        frame_title.pack(side='top')
# Entrée et Bouton Recherche
frame_input = tk.Frame (window, bg = theme['principal']['block']['color'], padx = 15, pady = 10)
frame_input.__dict__['path'] = {'bg': Path(value = 'principal/block/color/')}
entry_search = tk.Entry(frame_input, font = (theme['principal']['txt']['font'], 20), bg = theme['principal']['block']['entry']['bg'], fg = theme['principal']['block']['entry']['txt'])
entry_search.__dict__['path'] = {'bg': Path(value = 'principal/block/entry/bg/'), 'fg': Path(value = 'principal/block/entry/txt/'), 'ft': Path(value = 'principal/txt/font/'), 'fs': Path(value = 'recherche/text_size/')}
entry_search.pack(pady=5, fill='x')
button_search = tk.Button(frame_input, text = 'Conjuguer', font = (theme['principal']['txt']['font'], 20), bg = theme['principal']['block']['search']['bg'], fg = theme['principal']['block']['search']['txt'], command = conjuguer_fenêtre)
button_search.__dict__['path'] = {'bg': Path(value = 'principal/block/search/bg/'), 'fg': Path(value = 'principal/block/search/txt/'), 'ft': Path(value = 'principal/txt/font/'), 'fs': Path(value = 'recherche/text_size/')}
button_search.pack  (pady=5, fill='x')
frame_input.place   (relx = 0.15, relwidth = 0.7, y = 420)
# Changement de thème
button_themes = tk.Button(window, text = 'T', font = (theme['principal']['txt']['font'], 20), bg = theme['principal']['block']['search']['bg'], fg = theme['principal']['block']['search']['txt'], command = window_theme)
button_themes.place(x = 20, y = 590, width = 40, height = 40)
###############################################################################
###############################################################################
""" LOGICIEL """
###############################################################################
window.mainloop()
###############################################################################
###############################################################################
print()
