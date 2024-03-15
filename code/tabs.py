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
                                                # SIMPLES
                                                'infinitif_présent' : ['er'],
                                  
                                                'participe_présent' : ['ant'],
                                                'participe_passé' : ['é', 'és', 'ée', 'ées'],
                                  
                                                'indicatif_présent' : ['e', 'es', 'e', 'ons', 'ez', 'ent'],
                                                'indicatif_futur_simple' : ['erai', 'eras', 'era', 'erons', 'erez', 'eront'],
                                                'indicatif_imparfait' : ['ais', 'ais', 'ait', 'ions', 'iez', 'aient'],
                                                'indicatif_passé_simple' : ['ai', 'as', 'a', 'âmes', 'âtes', 'èrent'],
                                  
                                                'impératif_présent' : [None, 'e', None, 'ons', 'ez', None],
                                  
                                                'subjonctif_présent' : ['e', 'es', 'e', 'ions', 'iez', 'ent'],
                                                'subjonctif_imparfait' : ['asse', 'asses', 'ât', 'assions', 'assiez', 'assent'],
                                  
                                                'conditionnel_présent' : ['erais', 'erais', 'erait', 'erions', 'eriez', 'eraient']                                                
                                            }
                            },
                            '2-ir': {
                                'groupe' : 2,
                                'temps'  :  {
                                                # SIMPLES
                                                'infinitif_présent' : ['ir'],
                                  
                                                'participe_présent' : ['issant'],
                                                'participe_passé' : ['i', 'is', 'ie', 'ies'],
                                  
                                                'indicatif_présent' : ['is', 'is', 'it', 'issons', 'issez', 'issent'],
                                                'indicatif_futur_simple' : ['irai', 'iras', 'ira', 'irons', 'irez', 'iront'],
                                                'indicatif_imparfait' : ['issais', 'issais', 'issait', 'issions', 'issiez', 'issaient'],
                                                'indicatif_passé_simple' : ['is', 'is', 'it', 'îmes', 'îtes', 'irent'],
                                  
                                                'impératif_présent' : [None, 'is', None, 'issons', 'issez', None],
                                  
                                                'subjonctif_présent' : ['isse', 'isses', 'isse', 'issions', 'issiez', 'issent'],
                                                'subjonctif_imparfait' : ['isse', 'isses', 'ît', 'issions', 'issiez', 'issent'],
                                  
                                                'conditionnel_présent' : ['irais', 'irais', 'irait', 'irions', 'iriez', 'iraient']
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
                                                                    'passé':            "eu"
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
                                                                    'présent':          ["achète", "achètes", "achète", "achetons", "achetez", "achètent"],
                                                                    'futur_simple':     ["achèterai", "achèteras", "achètera", "achèterons", "achèterez", "achèteront"],
                                                                    'imparfait':        ["achetais", "achetais", "achetait", "achetions", "achetiez", "achetaient"],
                                                                    'passé_simple':     ["achetai", "achetas", "acheta", "achetâmes", "achetâtes", "chetèrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["achète", "achètes", "achète", "achetions", "achetiez", "chètent"],
                                                                    'imparfait':        ["achetasse", "achetasses", "achetât", "achetassions", "achetassiez", "achetassent"]
                                                                },
                                                'impératif':    {   'présent':          [None,"achète",None,"achetons","achetez",None] },
                                                'conditionnel': {   'présent':          ["achèterais", "achèterais", "achèterait", "achèterions", "achèteriez", "achèteraient"] },
                                                'participe':    {
                                                                    'présent':          "achetant",
                                                                    'passé':            "acheté"
                                                                },
                                                'infinitif':    {   'présent':          "acheter"}
                                            }
                        },
                        {
                                'verbe':    "appeler",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["appelle", "appelles", "appelle", "appelons", "appelez", "appellent"],
                                                                    'futur_simple':     ["appellerai", "appelleras", "appellera", "appellerons", "appellerez", "appelleront"],
                                                                    'imparfait':        ["appelais", "appelais", "appelait", "appelions", "appeliez", "appelaient"],
                                                                    'passé_simple':     ["appelai", "appelas", "appela", "appelâmes", "appelâtes", "appelèrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["appelle", "appelles", "appelle", "appelions", "appeliez", "appellent"],
                                                                    'imparfait':        ["appelasse", "appelasses", "appelasse", "appelassions", "appelassiez", "appelassent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "appelle",None, "appelons", "appelez",None] },
                                                'conditionnel': {   'présent':          ["appellerais", "appellerais", "appellerait", "appellerions", "appelleriez", "appelleraient"] },
                                                'participe':    {
                                                                    'présent':          "appelant",
                                                                    'passé':            "appelé"
                                                                },
                                                'infinitif':    {   'présent':          "appeler"}
                                            }
                        },
                        {
                                'verbe':    "envoyer",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["envoie", "envoies", "envoie", "envoyons", "envoyez", "envoient"],
                                                                    'futur_simple':     ["enverrai", "enverras", "enverra", "enverrons", "enverrez", "enverront"],
                                                                    'imparfait':        ["envoyais", "envoyais", "envoyait", "envoyions", "envoyiez", "envoyaient"],
                                                                    'passé_simple':     ["envoyai", "envoyas", "envoya", "envoyâmes", "envoyâtes", "envoyèrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["envoie", "envoies", "envoie", "envoyions", "envoyiez", "envoient"],
                                                                    'imparfait':        ["envoyasse", "envoyasses", "envoyât", "envoyassions", "envoyassiez", "envoyassent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "envoie",None, "envoyons", "envoyez",None] },
                                                'conditionnel': {   'présent':          ["enverrais", "enverrais", "enverrait", "enverrions", "enverriez", "enverraient"] },
                                                'participe':    {
                                                                    'présent':          "envoyant",
                                                                    'passé':            "envoyé"
                                                                },
                                                'infinitif':    {   'présent':          "envoyer"}
                                            }
                        },
                        {
                                'verbe':    "modeler",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["modèle", "modèles", "modèle", "modelons", "modelez", "modèlent"],
                                                                    'futur_simple':     ["modèlerai", "modèleras", "modèlera", "modèlerons", "modèlerez", "modèleront"],
                                                                    'imparfait':        ["modelais", "modelais", "modelait", "modelions", "modeliez", "modelaient"],
                                                                    'passé_simple':     ["modelai", "modelas", "modela", "modelâmes", "modelâtes", "modelèrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["modèle", "modèles", "modèle", "modelions", "modeliez", "modèlent"],
                                                                    'imparfait':        ["modelasse", "modelasses", "modelât", "modelassions", "modelassiez", "modelassent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "modèle",None, "modelons", "modelez",None] },
                                                'conditionnel': {   'présent':          ["modèlerais", "modèlerais", "modèlerait", "modèlerions", "modèleriez", "modèleraient"] },
                                                'participe':    {
                                                                    'présent':          "modelant",
                                                                    'passé':            "modelé"
                                                                },
                                                'infinitif':    {   'présent':          "modeler"}
                                            }
                        },
                        {
                                'verbe':    "peser",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["pèse", "pèses", "pèse", "pesons", "pesez", "pèsent"],
                                                                    'futur_simple':     ["pèserai", "pèseras", "pèsera", "pèserons", "pèserez", "pèseront"],
                                                                    'imparfait':        ["pesais", "pesais", "pesait", "pesions", "pesiez", "pesaient"],
                                                                    'passé_simple':     ["pesai", "pesas", "pesa", "pesâmes", "pesâtes", "pesèrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["pèse","pèses","pèse","pesions","pesiez","pèsent"],
                                                                    'imparfait':        ["pesasse","pesasses","pesât","pesassions","pesassiez","pesassent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "pèse",None, "pesons", "pesez",None] },
                                                'conditionnel': {   'présent':          ["pèserais","pèserais","pèserait","pèserions","pèseriez","pèseraient"] },
                                                'participe':    {
                                                                    'présent':          "pesant",
                                                                    'passé':            "pesé"
                                                                },
                                                'infinitif':    {   'présent':          "peser"}
                                            }
                        },
                        {
                                'verbe':    "précier",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["précie","précies","précie","précions","préciez","précient"],
                                                                    'futur_simple':     ["précierai","précieras","préciera","précierons","précierez","précieront"],
                                                                    'imparfait':        ["préciais","préciais","préciait","préciions","préciiez","préciaient"],
                                                                    'passé_simple':     ["préciai","précias","précia","préciâmes","préciâtes","précièrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["précie","précies","précie","préciions","préciiez","précient"],
                                                                    'imparfait':        ["préciasse","préciasses","préciât","préciassions","préciassiez","préciassent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "précie",None,"précions","préciez", None] },
                                                'conditionnel': {   'présent':          ["précierais","précierais","précierait","précierions","précieriez","précieraient"] },
                                                'participe':    {
                                                                    'présent':          "préciant",
                                                                    'passé':            "précié"
                                                                },
                                                'infinitif':    {   'présent':          "précier"}
                                            }
                        },
                        {
                                'verbe':    "broyer",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["broie","broies","broie","broyons","broyez","broient"],
                                                                    'futur_simple':     ["broierai","broieras","broiera","broierons","broierez","broieront"],
                                                                    'imparfait':        ["broyais","broyais","broyait","broyions","broyiez","broyaient"],
                                                                    'passé_simple':     ["broyai","broyas","broya","broyâmes","broyâtes","broyèrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["broie","broies","broie","broyions","broyiez","broient"],
                                                                    'imparfait':        ["broyasse","broyasses","broyât","broyassions","broyassiez","broyassent"]
                                                                },
                                                'impératif':    {   'présent':          [None,"broie",None,"broyons","broyez",None] },
                                                'conditionnel': {   'présent':          ["broierais","broierais","broierait","broierions","broieriez","broieraient"] },
                                                'participe':    {
                                                                    'présent':          "broyant",
                                                                    'passé':            "broyé"
                                                                },
                                                'infinitif':    {   'présent':          "broyer"}
                                            }
                        },
                        {
                                'verbe':    "ployer",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["ploie","ploies","ploie","ployons","ployez","ploient"],
                                                                    'futur_simple':     ["ploierai","ploieras","ploiera","ploierons","ploierez","ploieront"],
                                                                    'imparfait':        ["ployais","ployais","ployait","ployions","ployiez","ployaient"],
                                                                    'passé_simple':     ["ployai","ployas","ploya","ployâmes","ployâtes","ployèrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["ploie","ploies","ploie","ployions","ployiez","ploient"],
                                                                    'imparfait':        ["ployasse","ployasses","ployât","ployassions","ployassiez","ployassent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "ploie", None, "ployons", "ployez", None] },
                                                'conditionnel': {   'présent':          ["ploierais","ploierais","ploierait","ploierions","ploieriez","ploieraient"] },
                                                'participe':    {
                                                                    'présent':          "ployant",
                                                                    'passé':            "ployé"
                                                                },
                                                'infinitif':    {   'présent':          "ployer"}
                                            }
                        },
                        {
                                'verbe':    "jeter",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["jette","jettes","jette","jetons","jetez","jettent"],
                                                                    'futur_simple':     ["jetterai","jetteras","jettera","jetterons","jetterez","jetteront"],
                                                                    'imparfait':        ["jetais","jetais","jetait","jetions","jetiez","jetaient"],
                                                                    'passé_simple':     ["jetai","jetas","jeta","jetâmes","jetâtes","jetèrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["jette","jettes","jette","jetions","jetiez","jettent"],
                                                                    'imparfait':        ["jetasse","jetasses","jetât","jetassions","jetassiez","jetassent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "jette", None, "jetons", "jetez",None] },
                                                'conditionnel': {   'présent':          ["jetterais","jetterais","jetterait","jetterions","jetteriez","jetteraient"] },
                                                'participe':    {
                                                                    'présent':          "jetant",
                                                                    'passé':            "jeté"
                                                                },
                                                'infinitif':    {   'présent':          "jeter"}
                                            }
                        },
                        {
                                'verbe':    "payer",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["paie","paies","paie","payons","payez","paient"],
                                                                    'imparfait':        ["payais","payais","payait","payions","payiez","payaient"],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
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
