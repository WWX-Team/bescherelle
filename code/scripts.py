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
    return tab_temps

def init_irréguliers():
    """
    [Launch]: Initialise les données nécessaires au projet.
    """
    tab_irréguliers = []
    for i in tabs.tab_irréguliers:
        tab_irréguliers.append(i['verbe'])
    return tab_irréguliers

def init_exceptions():
    """
    [Launch]: Initialise les données nécessaires au projet.
    """
    dic_exceptions = {}
    for uplet in tabs.tab_ex_er:
        if uplet[1] != None:
            dic_exceptions[uplet[0]] = uplet[1]
    for uplet in tabs.tab_ex_ir:
        if uplet[1] != None:
            dic_exceptions[uplet[0]] = uplet[1]
    return dic_exceptions

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
    [Verbe / Analyse / Est irrégulier]: Vérifie si un verbe donné [:str] est irrégulier. Retourne un [:tuple] contenant un [:bool], et le verbe irrégulier modèle [:str].
    """
    if len(verbe) == 0: return False
    for i in tabs.tab_irréguliers:
        if i['verbe'] == verbe:
            return (True, verbe)
    return verbe_analyse_est_composé(verbe)

def verbe_analyse_est_composé(verbe:str) -> tuple:
    """
    [Verbe / Analyse / Est irrégulier / Est composé]: Vérifie si un verbe donné est un composé (d'un verbe irrégulier). Retourne un [:tuple] contenant un [:bool], et le verbe irrégulier modèle [:str].
    """      
    if len(verbe) == 0: return (False, None)
    for i in tabs.tab_irréguliers:
        v = i['verbe']
        if len(v) < len(verbe) and len(v) != 0:
            if v == verbe[len(verbe) - len(v) +1 : len(verbe)]:
                return (True, v)
    return (False, None)

def verbe_analyse_est_état(verbe:str) -> str:
    """
    [Verbe / Analyse / Verbes d'état]: Retourne une [:str] indiquant soit "état", soit "personnel", soit "impersonnel".
    """
    for i in tabs.tab_états:
        if verbe[len(verbe) - len(i) : len(verbe)] == i:
            return "état"
    for i in tabs.tab_irréguliers:
        if verbe[len(verbe) - len(i) : len(verbe)] == i['verbe'] and i['type'] == 'impersonnel':
            return "impersonnel"
    return "personnel"

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

def mot_tr_remplacer(mot:str, symbole:str='_', avec:str=' ', data:str=''):
    if len(mot) == 0: return data
    else            :
        actuelle = mot[0]
        if actuelle == symbole: actuelle = avec
        return mot_tr_remplacer(mot = mot[1:len(mot)], symbole = symbole, avec = avec, data = (data + actuelle))

def mot_tr_former_temps(mode:str, temps:str) -> str:
    if mode in ['participe', 'infinitif']: return mode[0].upper() + mode[1:len(mode)] + ' ' + temps
    nom_temps =  temps[0].upper()
    nom_temps += mot_tr_remplacer(temps[1:len(temps)])
    if mode[0] in 'aeiouy': liaison = "de l\'"
    else                  : liaison = "du "
    return nom_temps + ' ' + liaison + mot_tr_remplacer(mode)

def mot_tr_élision(mot : str, suivant : str):
    if mot[-1] == 'e' and suivant[0] in tabs.tab_voyelles: return mot[0 : len(mot) -1] + '\'' + suivant
    return mot + ' ' + suivant

## CONJUGAISONS #####

                # Principal
                
def conjuguer(verbe:str, affichage:bool=False):
    """
    [Conjugaison]:\n
    """
    group, inf, rad = verbe_analyse(conjuguer_an_trouver_verbe(verbe)) 
    # group : groupe du verbe [:int]
    # inf   : terminaison infinitive non brute [:str]
    # rad   : radical infinitif [:str]
    if group == None or inf == None or rad == None: return None
    conjugué = {}
    conjugué['!affichage'] = {}
    conjugué['modes']      = tabs.dic_verbe
    for __mode, __groupe_temps in tabs.dic_verbe.items():
        if __mode[0] != '!':
            conjugué['!affichage'][__mode] = {}
            conjugué['!affichage']['?' + __mode] = __mode[0].upper() + __mode[1:len(__mode)]
            for __temps, __terminaisons in __groupe_temps.items():
                conjugué['!affichage'][__mode][__temps]       = mot_tr_former_temps(__mode, __temps)
                conjugué['!affichage'][__mode]['?' + __temps] = __temps[0].upper() + mot_tr_remplacer(__temps[1:len(__temps)])
                if   isinstance(__terminaisons, list):
                    for i in range(1, len(conjugué['modes'][__mode][__temps]) +1):
                        conjugué['modes'][__mode][__temps][i-1] = conjuguer_tr(terminaison = inf, radical = rad, personne = i, temps = (__mode + '_' + __temps), groupe = group)
                elif isinstance(__terminaisons, str) :
                    conjugué['modes'][__mode][__temps] = conjuguer_tr(terminaison = inf, radical = rad, personne = 1, temps = (__mode + '_' + __temps), groupe = group)
            if conjugué['!affichage'][__mode] == {}:
                del conjugué['!affichage'][__mode]
    conjugué['!verbe']                                             = verbe
    conjugué['!groupe']                                            = group
    conjugué['!term']                                              = inf
    conjugué['!usage']                                             = verbe_analyse_est_état(verbe)
    if verbe_analyse_est_irrégulier(verbe)[0] : conjugué['!build'] = 'irrégulier'
    else                                      : conjugué['!build'] = 'régulier'
    if verbe in ['être', 'avoir']             : conjugué['type']   = 'auxiliaire'
    else                                      : conjugué['type']   = 'commun'
    """
    [Conjugaison / Documentation des données]
    Les données sont présententes sous le format
    {
        '!affichage' : {
                            'mode_1': {
                                            'temps_complet':  "Temps complet du mode 1",
                                            '?temps_complet': "Temps complet"
                                      },
                            '?mode_1': 'Mode 1'
                        },
        'modes': {    'mode_1': {
                            'temps_complet': ["","","","","",""],       // plupart du et des temps
                            'temps_unique' : "",                        // modes : infinitif, participe
                            'temps_partiel': [None,"",None,"","",None], // modes : impératif
                            }
                },
        '!verbe' : [:str],
        '!groupe': [:int],
        '!term'  : [:str],
        '!type'  : [:str]
    }
    """
    if affichage:
        for af_mode in conjugué['modes'].keys():
            print(f" | {conjugué['!affichage']['?' + af_mode]}" + " ––––––––––––––––––––––––––––––––––––––––––––––––––"[0 : 50 - len(conjugué['!affichage']['?' + af_mode])] + '\n')
            for af_temps in conjugué['modes'][af_mode].keys():
                print (f" :    - {conjugué['!affichage'][af_mode]['?' + af_temps]}")  
                if   isinstance(conjugué['modes'][af_mode][af_temps], list):
                    personne = 0
                    for af_term in conjugué['modes'][af_mode][af_temps]:
                        if af_term != None : print(f" :        • {mot_tr_élision(tabs.tab_pronoms_personnels[personne], af_term)}")
                        personne += 1 
                elif isinstance(conjugué['modes'][af_mode][af_temps], str):
                    print(f" :        • {conjugué['modes'][af_mode][af_temps]}")
            print()
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
    else                :
        cg_tags = []
        if verbe_est_irrégulier:
            # Si le verbe est irrégulier, le chemin est dans le tableau des irréguliers
            cg_path                  = tabs.tab_irréguliers[init_irréguliers().index(verbe_irrégulier_modèle)]['feuille'][cg_mode][cg_temps]
        else                   :
            # Si le verbe est régulier, le chemin est dans le dictionnaire des terminaisons
            cg_path                  = tabs.dic_terminaisons_cg[terminaison]['temps'][temps]
            if 'tags' in tabs.dic_terminaisons_cg[terminaison].keys():
                cg_tags              = tabs.dic_terminaisons_cg[terminaison]['tags']
        # Code commun
        if cg_path == None: return None
        cg_len         = len(cg_path)
        cg_terminaison = cg_path[((personne -1) % cg_len)]
        # Si la terminaison n'existe pas pour cette personne, retourne None
        if cg_terminaison == None: return None
        # Défini un radical au verbe en fonction de sa régularité
        if verbe_est_irrégulier:
            cg_radical = verbe_irrégulier_préfixe
        else                   :
            # Si verbe à radical particulier
            verbe_double_radicaux = init_exceptions()
            cg_radical = radical
            
            if verbe_infinitif in verbe_double_radicaux.keys():
                if groupe == 1:
                    if personne in [1, 2, 3, 6] and temps in ['indicatif_présent', 'impératif_présent', 'subjonctif_présent']:
                        cg_radical = verbe_double_radicaux[verbe_infinitif][0]
                    else:
                        cg_radical = verbe_double_radicaux[verbe_infinitif][1]
                else:
                    if personne in [1, 2, 3] and temps in ['indicatif_présent', 'impératif_présent']:
                        cg_radical = verbe_double_radicaux[verbe_infinitif][0]
                    else:
                        cg_radical = verbe_double_radicaux[verbe_infinitif][1]
            cg_radical = conjuguer_tr_vérifier_radical(cg_radical, verbe_analyse_term_brute(terminaison), cg_terminaison, temps, personne, groupe, cg_tags)
                
        return cg_radical + cg_terminaison

def conjuguer_tr_vérifier_radical(radical:str, inf:str, term:str, temps:str, personne:str, groupe:int, tags:list=[""]):
    """
    [Conjugaison / Transformations / Radical]: Voir [Conjugaison / Transformations]. Retourne l'état correct du radical.
    """
    cg_radical = radical
    if temps in ['indicatif_futur_simple'] and not 'build/sans_rad_futur_simple' in tags:
        cg_radical += inf
        if inf == 'rir': cg_radical += 'r'
    if temps in ['participe_présent']     :
        if   groupe == 1: cg_radical = cg_radical
        elif groupe == 2: cg_radical = cg_radical + 'iss'
        elif groupe == 3: cg_radical = cg_radical
    cg_radical = conjuguer_tr_e_final(cg_radical)
    cg_radical = conjuguer_tr_cédille(cg_radical, term)
    cg_radical = conjuguer_tr_g_final(cg_radical, term)
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
    if radical[-1] == 'c' and term[0] in ['a', 'o', 'u']: return radical[0:len(radical) -1] + 'ç'
    return radical

def conjuguer_tr_g_final(radical:str, term:str) -> str:
    """
    [Conjugaison / Transformations / -g, -e prononciation] Ajoute un -e de prononciation à un radical donné [:str] en fonction de la term donnée [:str]. Retourne le résultat [:str].
    """
    if radical[-1] == 'g' and (term[0] in 'aou'): return radical + 'e'
    return radical

                # Analyses

def conjuger_an_temps_est_composé(mode:str, temps:str) -> bool:
    """
    [Conjugaison / Analyses / Temps composé] Avec un mode [:str] et un temps [:str], retourne si ce temps est composé [:bool].
    """
    for astemps in tabs.tab_temps:
        if temps == astemps[0] and mode in astemps[1] and astemps[2] == 'composé': return True
    return False

def conjuguer_an_trouver_verbe(chaine:str="chanter"):
    lettres = 'azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBNâêîôÂÊÎÔÛäëïöüÄËÏÖÜùçàèéÉœŒ'
    verbe = ""
    for i in chaine:
        if i in lettres: verbe += i
    return verbe
