# -*- coding: utf-8 -*-

def tableau():
    build = []
    ### Création des lignes de l'en-tête
    header = []
    header = tableau_joindre_lignes(header, tableau_cellule(['Personne'], asbuild = ['right', 'bottom']))
    header = tableau_joindre_lignes(header, tableau_cellule(['Présent de l\'indicatif'], asbuild = ['bottom']))
    ### Création des lignes du corps
    lignes = []
    lignes = tableau_joindre_lignes(lignes, tableau_cellule(['Je', 'Tu', 'Il/Elle/On', 'Nous', 'Vous', 'Ils/Elles'], asbuild = ['right', 'bottom']))
    lignes = tableau_joindre_lignes(lignes, tableau_cellule(['mange', 'manges', 'mange', 'mangeons', 'mangez', 'mangent'], asbuild = ['bottom']))
    
    build = header + lignes
    
    return build
    
def tableau_joindre_lignes(tab:list, to:list):
    if len(tab) < len(to):
        for i in range(len(to) - len(tab)):
            tab.append("")
    build = []
    for ligne in range(len(to)):
        build.append(str(tab[ligne]) + str(to[ligne]))
    return build
    
def tableau_cellule(tab:list, asbuild:list):
    build = aligner(tab, align = 'L')
    bd_horizontal = '—' * len(build[0])
    if 'left' in asbuild : bd_horizontal = '+' + bd_horizontal
    if 'right' in asbuild: bd_horizontal = bd_horizontal + '+'
    for line in range(len(build)):
        if 'left' in asbuild     : build[line] = '|' + build[line]
        if 'right' in asbuild    : build[line] = build[line] + '|'
    if 'top' in asbuild   : build.insert(0, bd_horizontal)
    if 'bottom' in asbuild: build.append(bd_horizontal)
    return build
    
    
def aligner(tab:list, align:str="L"):
    """
    """
    max_size = 0
    size     = []
    for i in tab:
        if type(i) == type(""):     
            if len(i) > max_size: max_size = len(i)
            size.append(len(i))
        else:
            size.append(0)
    build = []
    for i in range(len(tab)):
        current = tab[i]
        if type(current) != type(""): current = ''
        repeat  = max_size - size[i]
        for times in range(repeat):
            if   align in ['R', 'right'] or (align in ['C', 'center'] and times < (repeat /2)):
                 current = ' ' + current
            else                         :
                 current = current + ' '
        build.append(' ' + current + ' ')
    return build
