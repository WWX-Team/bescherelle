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
window.config(background='#1c1c1c')
# Texte
frame_title = tkinter.Frame(window, bg='#1c1c1c')
#
label_title = tkinter.Label(frame_title, text='TITRE', font=('Arial', 60), bg='#1c1c1c', fg='#b21948')   # typo à trouver
label_title.pack(expand='YES')
#
frame_title.pack(side='top')
###############################################################################
"""
 - Boucle principale
"""
window.mainloop()

