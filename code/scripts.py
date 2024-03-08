import tabs

## Données #####

def init_temps():
    """
    [Launch]: Initialise les données nécessaires au projet.
    """
    tab_temps = []
    for i in tabs.tab_temps:
        for famille in i[1]:
            temps_composé = ""
            if i[2] == 'composé': temps_composé = i[3]
            tab_temps.append((famille + '_' + i, (i[2] == 'composé'), temps_composé))
    ## Code supplémentaire ?
    return tab_temps

## VERBES #####

          # ANALYSES
          
def verbe_analyse(verbe:str) -> tuple:
    """
    [Verbe / Analyse]:\n
    Fonction principale d'analyse d'un verbe donné [:str]. \n
    Retourne un tuple : \n
    \xA0\xA0\xA0• [0] groupe du verbe ;\n
    \xA0\xA0\xA0• [1] terminaison du verbe ;\n
    \xA0\xA0\xA0• [2] radical du verbe ;\n
    """
    term, rad = verbe_analyse_séparer(verbe)
    if term ==     "-ir":  term == verbe_analyse_ir(verbe)
    if term ==     "-er":  group = 1
    elif term ==   "2-ir": group = 2
    else:                  group = 3
    should = None
    if verbe[len(verbe) -3:len(verbe)] == "rir" and group == 3: should = "!-rir"
    return (group, term, rad, should)

def verbe_analyse_ir(verbe:str) -> str:
    """
    [Verbe / Analyse / Groupe verbe en -ir]: Analyse un verbe [:str] se finissant par -ir et retourne une [:str] indiquant le groupe du verbe, [:None] si erreur.
    """
    group = "2-ir"
    if len(verbe) < 2: group = None
    elif verbe[len(verbe)-2:len(verbe)] != "ir": group = None
    else:
        for index in tabs.tab_ex_ir:
            if index[0] == verbe: group = "3-ir"
            elif len(verbe) > len(index[0]): 
                if index[0] == verbe[len(verbe) - len(index[0]) : len(verbe)] : group = "3-ir"
    return group

def verbe_analyse_séparer(verbe:str) -> tuple:
    """
    [Verbe / Analyse / Séparer]: Sépare le radical et la terminaison d'un verbe donné [:str] à l'infinitif, [:None] si erreur.
    """
    terminaison = len(tabs.tab_terminaisons) - 1
    term = None
    radical = None
    while term == None and terminaison >= 0:
        actuelle = tabs.tab_terminaisons[terminaison]
        while actuelle[0]  != "-" and terminaison != 0:
            terminaison -= 1
            actuelle = tabs.tab_terminaisons[terminaison]
        # retour
        print(("-" + verbe[len(verbe) - len(actuelle) +1 : len(verbe)]), actuelle)
        if actuelle     == ("-" + verbe[len(verbe) - len(actuelle) +1 : len(verbe)]):
            term = actuelle
            radical = verbe[0 : len(verbe) - len(actuelle) +1]
        terminaison     -= 1
    return term, radical

## MOTS #####

        # ANALYSES
        
def mot_analyse_décomposer(chaîne:str) -> list:
    """
    [Mot / Analyse /  Décomposition liste]: Décompose une chaîne de caractère en une liste de mot.
    """
    mots = []
    mot = ""
    index = 0
    for lettre, in chaîne:
        if lettre == " " or index == (len(chaîne) -1):
            if not lettre == " ": mot += lettre
            mots.append(mot)
            mot = ""
        else:
            mot += lettre
        index += 1
    return mots

        # TRANSFORMATIONS

def mot_tr_élision(mot:str) -> str:
    """
    [Mot / Transformation / Élision -e final (pronom)]: Transforme un -e final d'un mot donné [:str] en apostrophe, [:None] si erreur.
    """
    if len(mot) == 0:    return None
    elif mot[-1] == "e": return mot[0:-1] + "'"
    else:                return mot
    
def mot_tr_accentuer(lettre:str, accent:str="^") -> str:
    """
    [Mot / Transformation / Accentuation lettre]: Accentue une lettre [:str] avec un accent donné [:str], par défaut, \"^\", retourne la lettre donnée si erreur.
    """
    if lettre in tabs.tab_voyelles and not lettre == 'y' and accent in '`´^¨':
        return tabs.tab_voyelles_accentuées[lettre][accent]
    return lettre

## CONJUGAISONS #####

                # Principal
                
def conjuguer(verbe:str, temps:str) -> list:
    """
    [Conjugaison]:\n
    Conjugue un verbe donné [:str] à un temps donné [:str] ( avec \"famille_temps\").\n
    Retourne un [:list] des conjuagaisons, OU une [:str] si cas unique, ou [:None] si erreur.
    """
    tab_temps = init_temps()
    group, inf, rad, rir = verbe_analyse(verbe)
    if not temps in tab_temps: return None
    if group == None or inf == None or rad == None: return None
    conjugué = []
    
    
    return conjugué
                
                # Transformations
                
def conjuguer_tr(verbe:str, radical:str, terminaison:str, rir:str) -> str:
    """
    """
    return ""
                
def conjuguer_tr_rir(verbe:str) -> str:
    """
    [Conjugaison / Transformations / Futur verbe en -rir]: Avec un verbe [:str] en -rir, retourne la forme valide du radical futur du verbe en -rir (avec double r). 
    """
    return verbe_analyse_séparer(verbe)[1] + 'r'

def conjuguer_tr_e_final(verbe:str) -> str:
    """
    [Conjugaison / Transformations / Élision -e final]: Avec un verbe à n'importe quel état [:str], retourne la forme sans -e final.
    """
    if verbe[-1] == 'e': return verbe[0:len(verbe) -1]
    return verbe

def conjuguer_tr_cédille(verbe:str) -> str:
    """
    [Conjugaison / Transformations / Cédille]: Ajoute une cédille au -c final d'un verbe donné [:str] et retourne le résultat.
    """
    if verbe[-1] == 'c': return verbe[0:len(verbe) -1] + 'ç'
    return verbe

def conjuguer_tr_g_final(radical:str, term:str) -> str:
    """
    [Conjugaison / Transformations / -g, -e prononciation] Ajoute un -e de prononciation à un radical donné [:str] en fonction de la term suivante.
    """
    if radical[-1] == 'g' and (not term[0] in 'aou'): return radical + 'e'
    return radical