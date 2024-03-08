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
                    ('passé_composé',       ('indicatif'),                                  'composé',   'indicatif_présent'),
                    ('plus_que_parfait',    ('indicatif', 'subjonctif'),                    'composé',   'indicatif_imparfait'),
                    ('passé_antérieur',     ('indicatif'),                                  'composé',   'indicatif_passé_simple'),
                    ('futur_antérieur',     ('indicatif'),                                  'composé',   'indicatif_futur_simple'),
                    ('passé',               ('conditionnel', 'subjonctif', 'impératif'),    'composé',   'présent'),
                ]

"""
Terminaisons
"""

# Tableau des terminaisons à l'infinitif
# Triées de la plus petite à la plus longue (note : seulement les caractères après le tiret sont comptabilisés)
tab_terminaisons              =    ["-er", "2-ir", "3-ir", "-ir", "-re", "-dre", "-ire", "-oir", "!-rir", "-aire", "-oire", "-ttre", "-aindre", "-eindre", "-oindre"]
# avancement                  #     √      √       √       |      √      X       X       X       X        X        X        X        X          X          X

tab_terminaisons_cg =    [
                            {
                                'term' : '-re',
                                'grpe' : 1,
                                'file' :    {
                                                'temps': 'présent',
                                                'terms': ['e', 'es', 'e', 'ons', 'ez', 'ent']
                                            }
                            },
                            {
                                'term' : '2-ir',
                                'grpe' : 2,
                                'file' :    {
                                                'temps': 'présent',
                                                'terms': ['is', 'is', 'it', 'issons', 'issez', 'issent']
                                            }
                            },
                            {
                                'term' : '3-ir',
                                'grpe' : 3,
                                'file' :    {
                                                'temps': 'présent',
                                                'terms': ['s', 's', 't', 'ons', 'ez', 'ent']
                                            }
                            },
                            {
                                'term' : '-re',
                                'grpe' : 3,
                                'file' :    {
                                                'temps': 'présent',
                                                'terms': ['s', 's', 't', 'ons', 'ez', 'ent']
                                            }
                            }
                        ]


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
                        
                        ## VERBES DU 1ER GROUPE
                        
                        {
                                'verbe':    "",
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
                        
                        ## VERBES DU 2E GROUPE
                        
                        {
                                'verbe':    "",
                                'groupe':   2,
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
                        }
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
                                                                    'imparfait':            "fallût"
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
                                                                    'imparfait':            [None,None,"plût",None,None,"plussent"]
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
                                                                    'imparfait':            [None,None,"plût",None,None,"plussent"]
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
                                                                    'imparfait':            "fallût"
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
                                                                    'imparfait':            "fallût"
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
                                                                    'imparfait':            "fallût"
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
                    ]
