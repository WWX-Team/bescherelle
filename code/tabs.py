"""
Utilitaires
"""

tab_favoris  = ["er", "bonsoir"]

"""
Lettres et accents
"""

tab_voyelles = ['a','e','i','o','u','y']

tab_voyelles_accentuées =   {
                                'a':    { '´':"á", '`':"à", '^':"â", '¨':"ä" },
                                'e':    { '´':"é", '`':"è", '^':"ê", '¨':"ë" },
                                'i':    { '´':"í", '`':"ì", '^':"î", '¨':"ï" },
                                'o':    { '´':"ó", '`':"ò", '^':"ô", '¨':"ö" },
                                'u':    { '´':"ú", '`':"ù", '^':"û", '¨':"ü" }
                            }

"""
Pronoms
"""

tab_pronoms  = ["me", "te", "se", "nous", "vous", "se"]

"""
Familles de temps, temps
"""

tab_familles = ["infinitif", "participe", "impératif", "indicatif", "subjonctif", "conditionnel"]

tab_temps    =  [
                    # SIMPLES
                    ('présent',         ('infinitif', 'participe', 'indicatif', 'impératif', 'subjonctif', 'conditionnel'), 'simple'),
                    ('futur_simple',    ('indicatif'),                  'simple'),
                    ('imparfait',       ('indicatif', 'subjonctif'),    'simple'),
                    ('passé_simple',    ('indicatif'),                  'simple'),
                    ('passé',           ('participe'),                  'simple'),
                    # COMPOSÉS
                    ('passé_composé',       ('indicatif'),                                  'composé',   'présent'),
                    ('plus_que_parfait',    ('indicatif', 'subjonctif'),                    'composé',   'imparfait'),
                    ('passé_antérieur',     ('indicatif'),                                  'composé',   'passé_simple'),
                    ('futur_antérieur',     ('indicatif'),                                  'composé',   'futur_simple'),
                    ('passé',               ('conditionnel', 'subjonctif', 'impératif'),    'composé',   'présent'),
                ]

"""
Terminaisons
"""

# Tableau des terminaisons à l'infinitif
# Triées de la plus petite à la plus longue (note : seulement les caractères après le tiret sont comptabilisés)
tab_terminaisons              =    ["-er", "2-ir", "3-ir", "-ir", "-re", "-dre", "-ire", "-oir", "-aire", "-oire", "-ttre", "-aindre", "-eindre", "-oindre"]
# avancement                  #     √      √       √       |      √      X       X       X       X        X        X        X          X          X

dic_terminaisons_cg =   {
                            '-er': {
                                'groupe' : 1,
                                'temps'  :  {
                                                'indicatif_présent' : ['e', 'es', 'e', 'ons', 'ez', 'ent']
                                            }
                            },
                            '2-ir': {
                                'groupe' : 2,
                                'temps'  :  {
                                                'indicatif_présent': ['is', 'is', 'it', 'issons', 'issez', 'issent']
                                            }
                            },
                            '3-ir': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'indicatif_présent': ['s', 's', 't', 'ons', 'ez', 'ent']
                                            }
                            },
                            '-re': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'indicatif_présent': ['s', 's', 't', 'ons', 'ez', 'ent']
                                            }
                            }
                        }

"""
Exceptions du 1er et 3e groupe en -ir et -er
"""

# Référence les verbes du 3e groupe finissant par -ir / 1er à double radical | verbes à radical simple : None ; verbes à double radical : tuple (présent sg, autre) ; irréguliers : False |
#                                                                                                             ; triple à retour : tuple + True

tab_ex_ir = [
                # SIMPLES
                ('ouvrir',      None),
                ('courir',      None),
                ('cueillir',    None),
                ('saillir',     None),
                ('couvrir',     None),
                ('vêtir',       None),
                ('offrir',      None),
                ('souffrir',    None),
                # IRRÉGULIERS
                ('venir',       False),
                ('quérir',      False),
                ('tenir',       False),
                ('faillir',     False),
                ('fuir',        False),
                ('ouïr',        False),
                ('gésir',       False),
                # À DOUBLE RADICAL
                ('lire',        ('li', 'lis')),
                ('bouillir',    ('bou', 'bouill')),
                ('mentir',      ('men', 'ment')),
                ('sentir',      ('sen', 'sent')),
                ('partir',      ('par', 'part')),
                ('servir',      ('ser', 'serv')),
                ('dormir',      ('dor', 'dorm')),
                ('mourir',      ('meur', 'mour')),
                ('sortir',      ('sor', 'sort'))
            ]

tab_ex_er = [
                ('siéger',        ('sièg', 'siég', True)),
                ('céder',        ('cèd', 'céd', True)),
            ]

"""
Liste des verbes irréguliers
"""

# si : 
#    | temps non entré      : pas conjugé
#    | personne non entrée  : pas existante
#
# vaincre, 

tab_irréguliers =   [
                        ## AUXILIAIRES

                        {
                                'verbe':    "être",
                                'groupe':   3,
                                'type':     "auxiliaire",
                                'usage':    "état",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["suis", "es", "est", "sommes", "êtes", "sont"],
                                                                    'futur_simple':     ["serai", "seras", "sera", "serons", "serez", "seront"],
                                                                    'imparfait':        ["étais", "étais", "était", "étions", "étiez", "étaient"],
                                                                    'passé_simple':     ["fus", "fus", "fut", "fûmes", "fûtes", "furent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["sois", "sois", "soit", "soyons", "soyez", "soient"],
                                                                    'imparfait':        ["fusse", "fusses", "fût", "fussions", "fussiez", "fussent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "sois", None, "soyons", "soyer", None] },
                                                'conditionnel': {   'présent':          ["serais", "serais", "serait", "serions", "seriez", "seraient"] },
                                                'participe':    {
                                                                    'présent':          "étant",
                                                                    'passé':            "été"
                                                                },
                                                'infinitif':    {   'présent':          "être"}
                                            }
                        },
                        {
                                'verbe':    "avoir",
                                'groupe':   3,
                                'type':     "auxiliaire",
                                'usage':    "état",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["ai", "as", "a", "avons", "avez", "ont"],
                                                                    'futur_simple':     ["aurai", "auras", "aura", "aurons", "aurez", "auront"],
                                                                    'imparfait':        ["avais", "avais", "avait", "avions", "aviez", "avaient"],
                                                                    'passé_simple':     ["eus", "eus", "eut", "eûmes", "eûtes", "eurent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["aie", "aies", "ait", "ayons", "ayez", "aient"],
                                                                    'imparfait':        ["eusse", "eusses", "eût", "eussions", "eussiez", "eussent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "aie", None, "ayons", "ayez", None] },
                                                'conditionnel': {   'présent':          ["aurais", "aurais", "aurait", "aurions", "auriez", "auraient"] },
                                                'participe':    {
                                                                    'présent':          "ayant",
                                                                    'passé':            ["eu(S)","eu(S)","eu(M.S) eue(F.S)","eus(P)","eus(P)","eus(M.P) eues(F.P)"]
                                                                },
                                                'infinitif':    {   'présent':          "avoir"}
                                            }
                        },
                        
                        ## VERBES DU 1ER GROUPE
                        
                        {
                                'verbe':    "acheter",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "appeler",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "envoyer",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "modeler",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "peser",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "précier",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "broyer",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "ployer",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "jeter",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "payer",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        
                        ## VERBES DU 3E GROUPE

                                {
                                'verbe':    "aller",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "asseoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "clore",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "moudre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "boire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "haïr",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "écrire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "naître",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "coudre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "croître",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "devoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "traire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "dissoudre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "dormir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "dire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "lire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "nuire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "paître",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "suivre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "pouvoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "prendre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "prévoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "recevoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "résoudre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "rire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "savoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "suffire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "vaincre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "valoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "vouloir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        {
                                'verbe':    "voir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   'présent':          ["", "", "", "", "", ""] },
                                                'conditionnel': {   'présent':          ["", "", "", "", "", ""] },
                                                'participe':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'infinitif':    {   'présent':          ""}
                                            }
                        },
                        
                        ## VERBES IMPERSONNELS
                        
                        {
                                'verbe':    "falloir",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          "faut",
                                                                    'futur_simple':     "faudra",
                                                                    'imparfait':        "fallait",
                                                                    'passé_simple':     "fallut"
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          "faille",
                                                                    'imparfait':        "fallût"
                                                                },
                                                'impératif':    {   'présent':          "faut" },
                                                'conditionnel': {   'présent':          "faudrait" },
                                                'participe':    {
                                                                    'présent':          None,
                                                                    'passé':            "fallu"
                                                                },
                                                'infinitif':    {   'présent':          "falloir"}
                                            }
                        },
                        {
                                'verbe':    "pleuvoir",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          [None,None,"pleut",None,None,"pleuvent"],
                                                                    'futur_simple':     [None,None,"pleuvra",None,None,"pleuvront"],
                                                                    'imparfait':        [None,None,"pleuvait",None,None,"pleuvaient"],
                                                                    'passé_simple':     [None,None,"plut",None,None,"plurent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          [None,None,"pleuve",None,None,"pleuvent"],
                                                                    'imparfait':        [None,None,"plût",None,None,"plussent"]
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          [None,None,"pleuvrait",None,None,"pleuvraient"] },
                                                'participe':    {
                                                                    'présent':          "pleuvant",
                                                                    'passé':            "plu"
                                                                },
                                                'infinitif':    {   'présent':          "pleuvoir"}
                                            }
                        },
                        {
                                'verbe':    "neiger",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          "neige",
                                                                    'futur_simple':     "neigera",
                                                                    'imparfait':        "neigeait",
                                                                    'passé_simple':     "neigea"
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          "neige",
                                                                    'imparfait':        "neigeât"
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          "neigerait" },
                                                'participe':    {
                                                                    'présent':          "neigeant",
                                                                    'passé':            "neigé"
                                                                },
                                                'infinitif':    {   'présent':          "neiger"}
                                            }
                        },
                        {
                                'verbe':    "venter",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          "vente",
                                                                    'futur_simple':     "ventera",
                                                                    'imparfait':        "ventait",
                                                                    'passé_simple':     "venta"
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          "vente",
                                                                    'imparfait':        "ventât"
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          "venterait" },
                                                'participe':    {
                                                                    'présent':          "ventant",
                                                                    'passé':            "venté"
                                                                },
                                                'infinitif':    {   'présent':          "venter"}
                                            }
                        },
                        {
                                'verbe':    "bruiner",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          "bruine",
                                                                    'futur_simple':     "bruinera",
                                                                    'imparfait':        "bruinait",
                                                                    'passé_simple':     "bruina"
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          "bruine",
                                                                    'imparfait':        "bruinât"
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          "bruinerait" },
                                                'participe':    {
                                                                    'présent':          "bruinant",
                                                                    'passé':            "bruiné"
                                                                },
                                                'infinitif':    {   'présent':          "bruiner"}
                                            }
                        },
                        {
                                'verbe':    "grêler",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          "grêle",
                                                                    'futur_simple':     "grêlera",
                                                                    'imparfait':        "grêlait",
                                                                    'passé_simple':     "grêla"
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          "grêle",
                                                                    'imparfait':        "grêlât"
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          "grêlerait" },
                                                'participe':    {
                                                                    'présent':          "grêlant",
                                                                    'passé':            "grêlé"
                                                                },
                                                'infinitif':    {   'présent':          "grêler"}
                                            }
                        },
                    ]
