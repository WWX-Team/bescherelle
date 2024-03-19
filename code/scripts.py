import tabs

## Données #####

def init_temps():
    """
    [Launch]: Initialise les données nécessaires au projet.
    """
    tab_temps = []
    for i in tabs.tab_temps:
        temps_composé = ""
        if i[2] == 'composé': temps_composé = i[3]
        if type(i[1]) == str :
            mode = i[1]
            tab_temps.append((mode + '_' + i[0], (i[2] == 'composé'), mode + '_' + temps_composé))
        else: 
            for mode in i[1]:
                tab_temps.append((mode + '_' + i[0], (i[2] == 'composé'), mode + '_' + temps_composé))
    ## Code supplémentaire ?
    return tab_temps

def init_irréguliers():
    """
    [Launch]: Initialise les données nécessaires au projet.
    """
    tab_irréguliers = []
    for i in tabs.tab_irréguliers:
        tab_irréguliers.append(i['verbe'])
    return tab_irréguliers

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
    if term ==     "-ir":  term  = verbe_analyse_ir(verbe)
    if term ==     "-er":  group = 1
    elif term ==   "2-ir": group = 2
    else:                  group = 3
    return (group, term, rad)

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
        if actuelle     == ("-" + verbe[len(verbe) - len(actuelle) +1 : len(verbe)]):
            term = actuelle
            radical = verbe[0 : len(verbe) - len(actuelle) +1]
        terminaison     -= 1
    return term, radical

def verbe_analyse_est_irrégulier(verbe:str) -> bool:
    """
    [Verbe / Analyse / Est irrégulier]: Vérifie si un verbe donné [:str] est irrégulier. Retourne un [:bool].
    """
    if len(verbe) == 0: return False
    for i in tabs.tab_irréguliers:
        if i['verbe'] == verbe:
            return (True, verbe)
    return (False, None)

def verbe_analyse_est_composé(verbe:str) -> tuple:
    """
    [Verbe / Analyse / Est composé]: Vérifie si un verbe donné est un composé (d'un verbe irrégulier). Retourne un [:tuple] contenant un [:bool], et le verbe irrégulier modèle [:str].
    """      
    if len(verbe) == 0: return (False, None)
    for i in tabs.tab_irréguliers:
        v = i['verbe']
        if len(v) < len(verbe) and len(v) != 0:
            if v == verbe[len(verbe) - len(v) +1 : len(verbe)]:
                return (True, v)
    return (False, None)

def verbe_analyse_term_brute(verbe:str, data="") -> str:
    """
    [Verbe / Analyse / Terminaison brute]: Récupère la terminaison [:str] sans le tiret et données précédantes. Retourne [:str].
    """
    if len(verbe) == 0: return data
    if verbe[-1] != '-':
        return verbe_analyse_term_brute(verbe[0 : len(verbe) -1], verbe[-1] + data)
    return data

def verbe_analyse_temps_composé(temps:str) -> tuple:
    """
    [Verbe / Analyse / Temps composé]: Récupère le mode et le temps ([:tuple] de [:str]) d'un temps composé [:str].
    """
    if not '_' in temps: return (None, None)
    cg_temps = ""
    cg_mode  = ""
    idx = 0
    while temps[idx] != '_':
        cg_mode += temps[idx]
        idx += 1
    for i in range (idx+1, len(temps)):
        cg_temps += temps[i]
    return (cg_mode, cg_temps)

## MOTS #####

        # ANALYSES
        
def mot_analyse_décomposer(chaîne:str) -> list:
    """
    [Mot / Analyse /  Décomposition liste]: Sépare le verbe et la préposition dans un verbe pronominal puis l'ajoute à un tableau [:list].
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
    Retourne un [:list] des conjugaisons, OU une [:str] si cas unique, ou [:None] si erreur.
    """
    group, inf, rad = verbe_analyse(verbe) 
    # group : groupe du verbe [:int]
    # inf   : terminaison infinitive non brute [:str]
    # rad   : radical infinitif [:str]
    if group == None or inf == None or rad == None: return None
    conjugué = []
    # à faire PAR WILHELM MERCI
    return conjugué
                
                # Transformations
                
def conjuguer_tr(terminaison:str, radical:str, personne:int, temps:str, groupe:int) -> str:
    """
    [Conjugaison / Transformations]: Entrées : \n
    \xA0\xA0\xA0• Terminaison du verbe (infinitif présent) ;\n
    \xA0\xA0\xA0• Radical du verbe (infinitif présent) ;\n
    \xA0\xA0\xA0• Personne de conjugaison ;\n
    \xA0\xA0\xA0• Temps de conjugaison ;\n
    \xA0\xA0\xA0• Groupe du verbe ;\n
    Retourne le verbe conjugué pour cette personne, temps [:str].
    """
    # INITIALISATION
    tab_temps         = init_temps()
    tab_irréguliers   = init_irréguliers()
    cg_mode, cg_temps = verbe_analyse_temps_composé(temps)
    # TESTS VALIDITÉ
    temps_est_valide  = False
    for i in tab_temps:
        if i[0] == temps:
            temps_est_valide = True
            temps_est_composé = i[1]
            temps_composé_référence = i[2]
    if not temps_est_valide: return None
    if cg_mode == 'impératif' and personne not in [2, 4, 5]: return None 
    verbe_infinitif = radical + verbe_analyse_term_brute(terminaison)
    # TESTS IRRÉGULIER
    verbe_est_rir   = 'rir' == (verbe_infinitif[len(verbe_infinitif) - 3 : len(verbe_infinitif)]) and terminaison == '3-ir'
    verbe_est_irrégulier, verbe_irrégulier_modèle = verbe_analyse_est_irrégulier(verbe_infinitif)
    if verbe_est_irrégulier and verbe_irrégulier_modèle != verbe_infinitif: verbe_irrégulier_préfixe = verbe_infinitif[0 : len(verbe_infinitif) - len(verbe_irrégulier_modèle) +1]
    else                                                                  : verbe_irrégulier_préfixe = ""
    # TESTS FINALE
    verbe_est_e = verbe_infinitif[-1] == 'e'
    verbe_est_c = radical[-1]         == 'c'
    verbe_est_g = radical[-1]         == 'g'
    # CONJUGAISON
    if temps_est_composé:
        return conjuguer_tr('-oir', 'av', personne, temps_composé_référence, 3) + '/' + conjuguer_tr('-re', 'êt', personne, temps_composé_référence, 3) + ' ' + conjuguer_tr(terminaison, radical, 1, 'participe_passé', groupe)
    else:
        if verbe_est_irrégulier:
            if verbe_irrégulier_modèle in tab_irréguliers:
                cg_path        = tabs.tab_irréguliers[init_irréguliers().index(verbe_irrégulier_modèle)]['feuille'][cg_mode][cg_temps]
                cg_len         = len(cg_path)
                cg_terminaison = cg_path[((personne -1) % cg_len)]
                if cg_terminaison == None: return ""
                return verbe_irrégulier_préfixe + cg_terminaison
            else: return "Erreur/Verbe Non Enregistré"
        if terminaison in tabs.dic_terminaisons_cg.keys():
            cg_path         = tabs.dic_terminaisons_cg[terminaison]['temps'][temps]
            cg_len          = len(cg_path)
            cg_terminaison  = cg_path[((personne -1) % cg_len)]
            if cg_terminaison == None: return None
            cg_radical      = conjuguer_tr_vérifier_radical(radical, cg_terminaison, temps, personne, groupe)
            return cg_radical +  cg_terminaison  
    return "Erreur/Pas Un Verbe"

def conjuguer_tr_vérifier_radical(radical:str, term:str, temps:str, personne:str, groupe:int):
    """
    [Conjugaison / Transformations / Radical]: Voir [Conjugaison / Transformations]. Retourne l'état correct du radical.
    """
    cg_radical = radical
    if temps in ['indicatif_futur_simple']: cg_radical += 'r'
    if temps in ['participe_présent']     :
        if   groupe == 1: cg_radical = cg_radical
        elif groupe == 2: cg_radical = cg_radical + 'iss'
        elif groupe == 3: cg_radical = cg_radical
    cg_radical = conjuguer_tr_e_final(radical)
    cg_radical = conjuguer_tr_cédille(radical, term)
    cg_radical = conjuguer_tr_g_final(radical, term)
    return cg_radical

def conjuguer_tr_e_final(verbe:str) -> str:
    """
    [Conjugaison / Transformations / Élision -e final]: Avec un verbe à n'importe quel état [:str], retourne la forme sans -e final [:str].
    """
    if verbe[-1] == 'e': return verbe[0:len(verbe) -1]
    return verbe

def conjuguer_tr_cédille(radical:str, term:str) -> str:
    """
    [Conjugaison / Transformations / Cédille]: Ajoute une cédille au -c final d'un radical donné [:str] si la terminaison donnée [:str] le nécessite, et retourne le résultat [:str].
    """
    if radical[-1] == 'c' and term[0] in 'aou': return radical[0:len(radical) -1] + 'ç'
    return radical

def conjuguer_tr_g_final(radical:str, term:str) -> str:
    """
    [Conjugaison / Transformations / -g, -e prononciation] Ajoute un -e de prononciation à un radical donné [:str] en fonction de la term donnée [:str]. Retourne le résultat [:str].
    """
    if radical[-1] == 'g' and (term[0] in 'aou'): return radical + 'e'
    return radical

for temps in init_temps():
    print(f'###### {temps[0]} ######')
    for prs in range(1, 7):
        print(' + ' + str(conjuguer_tr(terminaison = '-er', radical = 'mang', groupe = '1', personne = prs, temps = temps[0])))
    print()
