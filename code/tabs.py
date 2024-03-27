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
                                'u':    { '´':"ú", '`':"ù", '^':"û", '¨':"ü" },
                                'y':    { '¨':"ÿ"                            }
                            }

"""
Pronoms
"""

tab_pronoms            = ["me", "te", "se", "nous", "vous", "se"]
tab_pronoms_personnels = ["je", "tu", "il/elle/iel/on", "nous", "vous", "ils/elles/iels"]

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
tab_terminaisons              =    ["-er", "2-ir", "3-ir", "-ir", "-re", "-dre", "-ire", "-oir", "-enir", "-aire", "-oire", "-uire", "-ettre", "-aindre", "-eindre", "-oindre", "-eillir"]

dic_terminaisons_cg =   {
                            '-er': {
                                'groupe' : 1,
                                'temps'  :  {  
                                                'infinitif_présent'       : ['er'],
                                  
                                                'participe_présent'       : ['ant'],
                                                'participe_passé'         : ['é'],
                                  
                                                'indicatif_présent'       : ['e', 'es', 'e', 'ons', 'ez', 'ent'],
                                                'indicatif_futur_simple'  : ['erai', 'eras', 'era', 'erons', 'erez', 'eront'],
                                                'indicatif_imparfait'     : ['ais', 'ais', 'ait', 'ions', 'iez', 'aient'],
                                                'indicatif_passé_simple'  : ['ai', 'as', 'a', 'âmes', 'âtes', 'èrent'],
                                  
                                                'impératif_présent'       : [None, 'e', None, 'ons', 'ez', None],
                                  
                                                'subjonctif_présent'      : ['e', 'es', 'e', 'ions', 'iez', 'ent'],
                                                'subjonctif_imparfait'    : ['asse', 'asses', 'ât', 'assions', 'assiez', 'assent'],
                                  
                                                'conditionnel_présent'    : ['erais', 'erais', 'erait', 'erions', 'eriez', 'eraient']                                                
                                            }
                            },
                            '2-ir': {
                                'groupe' : 2,
                                'temps'  :  {
                                                'infinitif_présent'       : ['ir'],
                                  
                                                'participe_présent'       : ['issant'],
                                                'participe_passé'         : ['i'],
                                  
                                                'indicatif_présent'       : ['is', 'is', 'it', 'issons', 'issez', 'issent'],
                                                'indicatif_futur_simple'  : ['irai', 'iras', 'ira', 'irons', 'irez', 'iront'],
                                                'indicatif_imparfait'     : ['issais', 'issais', 'issait', 'issions', 'issiez', 'issaient'],
                                                'indicatif_passé_simple'  : ['is', 'is', 'it', 'îmes', 'îtes', 'irent'],
                                  
                                                'impératif_présent'       : [None, 'is', None, 'issons', 'issez', None],
                                  
                                                'subjonctif_présent'      : ['isse', 'isses', 'isse', 'issions', 'issiez', 'issent'],
                                                'subjonctif_imparfait'    : ['isse', 'isses', 'ît', 'issions', 'issiez', 'issent'],
                                  
                                                'conditionnel_présent'    : ['irais', 'irais', 'irait', 'irions', 'iriez', 'iraient']
                                            }
                            },
                            '-dre': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['dre'],
                                  
                                                'participe_présent'       : ['nant'],
                                                'participe_passé'         : ['is'],
                                  
                                                'indicatif_présent'       : ['ds', 'ds', 'd', 'nons', 'nez', 'nent'],
                                                'indicatif_futur_simple'  : ['ai', 'as', 'a', 'ons', 'ez', 'ont'],
                                                'indicatif_imparfait'     : ['ais', 'ais', 'ait', 'ions', 'iez', 'aient'],
                                                'indicatif_passé_simple'  : ['', '', '', '', '', ''],
                                  
                                                'impératif_présent'       : [None, 'ds', None, 'dons', 'dez', None],
                                  
                                                'subjonctif_présent'      : ['de', 'des', 'de', 'dions', 'diez', 'dent'],
                                                'subjonctif_imparfait'    : ['disse', 'disses', 'dît', 'dissions', 'dissiez', 'dissent'],
                                  
                                                'conditionnel_présent'    : ['drais', 'drais', 'drait', 'drions', 'driez', 'draient']
                                            }
                            },
                            '-ire': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['ire'],
                                  
                                                'participe_présent'       : ['isant'],
                                                'participe_passé'         : ['u'],
                                  
                                                'indicatif_présent'       : ['is', 'is', 'it', 'isons', 'isez', 'isent'],
                                                'indicatif_futur_simple'  : ['irai', 'iras', 'ira', 'irons', 'irez', 'iront'],
                                                'indicatif_imparfait'     : ['isais', 'isais', 'isait', 'isions', 'isiez', 'isaient'],
                                                'indicatif_passé_simple'  : ['us', 'us', 'ut', 'ûmes', 'ûtes', 'lurent'],
                                  
                                                'impératif_présent'       : [None, 'is', None, 'isons', 'isez', None],
                                  
                                                'subjonctif_présent'      : ['ise', 'ises', 'ise', 'isions', 'isiez', 'isent'],
                                                'subjonctif_imparfait'    : ['usse', 'usses', 'ût', 'ussions', 'ussiez', 'ussent'],
                                  
                                                'conditionnel_présent'    : ['irais', 'irais', 'irait', 'irions', 'iriez', 'iraient'],
                                                
                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                            },
                            '-oir': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['oir'],
                                  
                                                'participe_présent'       : ['oyant'],
                                                'participe_passé'         : ['u'],
                                  
                                                'indicatif_présent'       : ['ois', 'ois', 'oit', 'oyons', 'oyez', 'oyent'],
                                                'indicatif_futur_simple'  : ['errais', 'errais', 'errait', 'errons', 'errez', 'erront'],
                                                'indicatif_imparfait'     : ['oyais', 'oyais', 'oyait', 'oyions', 'oyiez', 'oyaient'],
                                                'indicatif_passé_simple'  : ['is', 'is', 'it', 'îmes', 'îtes', 'inrent'],
                                  
                                                'impératif_présent'       : [None, 'ois', None, 'oyons', 'oyez', None],
                                  
                                                'subjonctif_présent'      : ['oie', 'oies', 'oie', 'oyions', 'oyiez', 'voient'],
                                                'subjonctif_imparfait'    : ['isse', 'isses', 'ît', 'issions', 'issiez', 'issent'],
                                  
                                                'conditionnel_présent'    : ['errais', 'errais', 'errait', 'errions', 'erriez', 'erraient'],
                                                
                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                            },
                            '-enir': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['enir'],
                                  
                                                'participe_présent'       : ['enant'],
                                                'participe_passé'         : ['enu'],
                                  
                                                'indicatif_présent'       : ['iens', 'iens', 'ient', 'enons', 'enez', 'iennent'],
                                                'indicatif_futur_simple'  : ['iendrai', 'iendras', 'iendra', 'iendrons', 'iendrez', 'iendront'],
                                                'indicatif_imparfait'     : ['enais', 'enais', 'enait', 'enions', 'eniez', 'enaient'],
                                                'indicatif_passé_simple'  : ['ins', 'ins', 'int', 'înmes', 'întes', 'inrent'],
                                  
                                                'impératif_présent'       : [None, '', None, '', '', None],
                                  
                                                'subjonctif_présent'      : ['ienne', 'iennes', 'ienne', 'enions', 'eniez', 'iennent'],
                                                'subjonctif_imparfait'    : ['insse', 'insses', 'înt', 'inssions', 'inssiez', 'inssent'],
                                  
                                                'conditionnel_présent'    : ['iendrais', 'iendrais', 'iendrait', 'iendrions', 'iendriez', 'iendraient'],

                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                            },
                            '-aire': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['aire'],
                                  
                                                'participe_présent'       : ['ayant'],
                                                'participe_passé'         : ['ait'],
                                  
                                                'indicatif_présent'       : ['ais', 'ais', 'ait', 'ayons', 'ayez', 'aient'],
                                                'indicatif_futur_simple'  : ['airai', 'airas', 'aira', 'airons', 'airez', 'airont'],
                                                'indicatif_imparfait'     : ['ayais', 'ayais', 'ayait', 'ayions', 'ayiez', 'ayaient'],
                                                'indicatif_passé_simple'  : None,
                                  
                                                'impératif_présent'       : [None, 'ais', None, 'ayons', 'ayez', None],
                                  
                                                'subjonctif_présent'      : ['aie', 'aies', 'aie', 'ayions', 'ayiez', 'aient'],
                                                'subjonctif_imparfait'    : None,
                                  
                                                'conditionnel_présent'    : ['airais', 'airais', 'airait', 'airions', 'airiez', 'airaient'],
                                                
                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                            },
                            '-oindre': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['oindre'],
                                  
                                                'participe_présent'       : ['oignant'],
                                                'participe_passé'         : ['oint'],
                                  
                                                'indicatif_présent'       : ['oins','oins','oint','oignons','oignez','oignent'],
                                                'indicatif_futur_simple'  : ['oindrai','oindras','oindra','oindrons','oindrez','oindront'],
                                                'indicatif_imparfait'     : ['oignais','oignais','oignait','oignions','oigniez','oignaient'],
                                                'indicatif_passé_simple'  : ['oignis','oignis','oignit','oignîmes','oignîtes','oignirent'],
                                  
                                                'impératif_présent'       : [None, 'oins', None, 'oignons', 'oignez', None],
                                  
                                                'subjonctif_présent'      : ['oigne','oignes','oigne','oignions','oigniez','oignent'],
                                                'subjonctif_imparfait'    : ['oignisse','oignisses','oignît','oignissions','oignissiez','oignissent'],
                                  
                                                'conditionnel_présent'    : ['oindrais','oindrais','oindrait','oindrions','oindriez','oindraient'],

                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                                
                            },
                            '-eindre': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['eindre'],
                                  
                                                'participe_présent'       : ['eignant'],
                                                'participe_passé'         : ['eint'],
                                  
                                                'indicatif_présent'       : ['eins','eins','eint','eignons','eignez','eignent'],
                                                'indicatif_futur_simple'  : ['eindrai','eindras','eindra','eindrons','eindrez','eindront'],
                                                'indicatif_imparfait'     : ['eignais','eignais','eignait','eignions','eigniez','eignaient'],
                                                'indicatif_passé_simple'  : ['eignis','eignis','eignit','eignîmes','eignîtes','eignirent'],
                                  
                                                'impératif_présent'       : [None, 'eins', None, 'eignons', 'eignez', None],
                                  
                                                'subjonctif_présent'      : ['eigne','eignes','eigne','eignions','eigniez','eignent'],
                                                'subjonctif_imparfait'    : ['eignisse','eignisses','eignît','eignissions','eignissiez','eignissent'],
                                  
                                                'conditionnel_présent'    : ['eindrais','eindrais','eindrait','eindrions','eindriez','eindraient'],

                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                            },
                            '-aindre': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['aindre'],
                                  
                                                'participe_présent'       : ['aignant'],
                                                'participe_passé'         : ['aint'],
                                  
                                                'indicatif_présent'       : ['ains','ains','aint','aignons','aignez','aignent'],
                                                'indicatif_futur_simple'  : ['aindrai','aindras','aindra','aindrons','aindrez','aindront'],
                                                'indicatif_imparfait'     : ['aignais','aignais','aignait','aignions','aigniez','aignaient'],
                                                'indicatif_passé_simple'  : ['aignis','aignis','aignit','aignîmes','aignîtes','aignirent'],
                                  
                                                'impératif_présent'       : [None, '', None, '', '', None],
                                  
                                                'subjonctif_présent'      : ['aigne','aignes','aigne','aignions','aigniez','aignent'],
                                                'subjonctif_imparfait'    : ['aignisse','aignisses','aignît','aignissions','aignissiez','aignissent'],
                                  
                                                'conditionnel_présent'    : ['aindrais','aindrais','aindrait','aindrions','aindriez','aindraient'],

                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                            },
                            '-ettre': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['ettre'],
                                  
                                                'participe_présent'       : ['ettant'],
                                                'participe_passé'         : ['is'],
                                  
                                                'indicatif_présent'       : ['ets','ets','et','ettons','ettez','mettent'],
                                                'indicatif_futur_simple'  : ['ettrai','ettras','ettra','ettrons','ettrez','mettront'],
                                                'indicatif_imparfait'     : ['ettais','ettais','ettait','ettions','ettiez','ettaient'],
                                                'indicatif_passé_simple'  : ['is','is','it','îmes','îtes','irent'],
                                  
                                                'impératif_présent'       : [None, 'ets', None, 'ettons', 'ettez', None],
                                  
                                                'subjonctif_présent'      : ['ette','ettes','ette','ettions','ettiez','ettent'],
                                                'subjonctif_imparfait'    : ['isse','isses','ît','issions','issiez','issent'],
                                  
                                                'conditionnel_présent'    : ['ettrais','ettrais', 'ettrait', 'ettrions', 'ettriez', 'ettraient'],

                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                            },
                            '-uire': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['uire'],
                                  
                                                'participe_présent'       : ['uisant'],
                                                'participe_passé'         : ['ui'],
                                  
                                                'indicatif_présent'       : ['uis','uis','uit','uisons','uisez','uisent'],
                                                'indicatif_futur_simple'  : ['uirai','uiras','uira','uirons','uirez','uiront'],
                                                'indicatif_imparfait'     : ['uisais','uisais','uisait','uisions','uisiez','uisaient'],
                                                'indicatif_passé_simple'  : ['uisis','uisis','uisit','uisîmes','uisîtes','uisirent'],
                                  
                                                'impératif_présent'       : [None, 'uis', None, 'uisons', 'uisez', None],
                                  
                                                'subjonctif_présent'      : ['uise','uises','uise','uisions','uisiez','uisent'],
                                                'subjonctif_imparfait'    : ['uisisse','uisisses','uisît','uisissions','uisissiez','uisissent'],
                                  
                                                'conditionnel_présent'    : ['uirais','uirais','uirait','uirions','uiriez','uiraient'],

                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                            },
                            '-oire': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['oire'],
                                  
                                                'participe_présent'       : ['oyant'],
                                                'participe_passé'         : ['u'],
                                  
                                                'indicatif_présent'       : ['ois','ois','oit','oyons','oyez','oient'],
                                                'indicatif_futur_simple'  : ['oirai','oiras','oira','oirons','oirez','oiront'],
                                                'indicatif_imparfait'     : ['oyais','oyais','oyait','oyions','oyiez','oyaient'],
                                                'indicatif_passé_simple'  : ['us','us','ut','ûmes','ûtes','urent'],
                                  
                                                'impératif_présent'       : [None, 'ois', None, 'oyons', 'oyez', None],
                                  
                                                'subjonctif_présent'      : ['oie','oies','oie','oyions','oyiez','oient'],
                                                'subjonctif_imparfait'    : ['usse','usses','ût','ussions','ussiez','ussent'],
                                  
                                                'conditionnel_présent'    : ['oirais','oirais','oirait','oirions','oiriez','oiraient'],

                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                            },
                            '-eillir': {
                                'groupe' : 3,
                                'temps'  :  {
                                                'infinitif_présent'       : ['eillir'],
                                  
                                                'participe_présent'       : ['eillant'],
                                                'participe_passé'         : ['eilli'],
                                  
                                                'indicatif_présent'       : ['eille','eilles','eille','eillons','eillez','eillent'],
                                                'indicatif_futur_simple'  : ['eillerai','eilleras','eillera','eillerons','eillerez','eilleront'],
                                                'indicatif_imparfait'     : ['eillais','eillais','eillait','eillions','eilliez','eillaient'],
                                                'indicatif_passé_simple'  : ['eillis','eillis','eillit','eillîmes','eillîtes','eillirent'],
                                  
                                                'impératif_présent'       : [None, 'eille', None, 'eillons', 'eillez', None],
                                  
                                                'subjonctif_présent'      : ['eille','eilles','eille','eillions','eilliez','eillent'],
                                                'subjonctif_imparfait'    : ['eillisse','eillisses','eillît','eillissions','eillissiez','eillissent'],
                                  
                                                'conditionnel_présent'    : ['eillerais','eillerais','eillerait','eillerions','eilleriez','eilleraient'],

                                                'tags'                    : ["build/sans_rad_futur_simple"]
                                            }
                            }
                        }

"""
Exceptions du 1er et 3e groupe en -ir et -er
"""

# Référence les verbes du 3e groupe finissant par -ir / 1er à double radical | verbes à radical simple, irréguliers : None ; verbes à double radical : tuple (présent sg, autre) |
#                                                                                                                          ; triple à retour : tuple + True
# Pour le 1er groupe, le double radical du singulier revient à la 3e personne du pluriel des temps "présent" simples

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
                ('venir',       None),
                ('quérir',      None),
                ('tenir',       None),
                ('faillir',     None),
                ('fuir',        None),
                ('@ouïr',       None),
                ('gésir',       None),
                # À DOUBLE RADICAL
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
                ('siéger',        ('sièg', 'siég')),
                ('céder',        ('cèd', 'céd')),
            ]

"""
Feuile de verbe vide
"""

dic_verbe = {
                                                'indicatif':    {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé_composé':    ["", "", "", "", "", ""],
                                                                    'plus_que_parfait': ["", "", "", "", "", ""],
                                                                    'futur_simple':     ["", "", "", "", "", ""],
                                                                    'futur_antérieur':  ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'passé_simple':     ["", "", "", "", "", ""],
                                                                    'passé_antérieur':  ["", "", "", "", "", ""]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""],
                                                                    'imparfait':        ["", "", "", "", "", ""],
                                                                    'plus_que_parfait': ["", "", "", "", "", ""]
                                                                },
                                                'impératif':    {   
                                                                    'présent':          [None, "", None, "", "", None],
                                                                    'passé':            [None, "", None, "", "", None]
                                                                },
                                                'conditionnel': {   
                                                                    'présent':          ["", "", "", "", "", ""],
                                                                    'passé':            ["", "", "", "", "", ""]
                                                                },
                                                'participe':    {
                                                                    'présent':          [""],
                                                                    'passé':            [""]
                                                                },
                                                'infinitif':    {   'présent':          [""]}
            }

"""
Liste des verbes d'état
"""

tab_états = ['être', 'sembler', 'paraître', 'rester', 'demeurer', 'devenir']

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
                        {
                                'verbe':    "faire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["fais", "fais", "fait", "faisons", "faites", "font"],
                                                                    'futur_simple':     ["ferai", "feras", "fera", "ferons", "ferez", "feront"],
                                                                    'imparfait':        ["faisais", "faisais", "faisait", "faisions", "faisiez", "faisaient"],
                                                                    'passé_simple':     ["fis", "fis", "fit", "fîmes", "fîtes", "firent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["fasse", "fasses", "fasse", "fassions", "fassiez", "fassent"],
                                                                    'imparfait':        ["fisse", "fisse", "fît", "fissions", "fissiez", "fissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "fais", None, "faisons", "faites", None] },
                                                'conditionnel': {   'présent':          ["ferais", "ferais", "ferait", "ferions", "feriez", "feraient"] },
                                                'participe':    {
                                                                    'présent':          "faisant",
                                                                    'passé':            "fait"
                                                                },
                                                'infinitif':    {   'présent':          "faire"}
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
                                'verbe':    "braire",
                                'groupe':   1,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          [None,None,"brait",None,None,"braient"],
                                                                    'futur_simple':     [None,None,"braira",None,None,"brairont"],
                                                                    'imparfait':        [None,None,"brayait",None,None,"brayaient"],
                                                                    'passé_simple':     None
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          [None,None,"braie",None,None,"braient"],
                                                                    'imparfait':        None
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          [None,None,"brairait",None,None,"brairaient"] },
                                                'participe':    {
                                                                    'présent':          "braire",
                                                                    'passé':            None
                                                                },
                                                'infinitif':    {   'présent':          "braire"}
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
                                                                    'futur_simple':     ["paierai","paieras","paiera","paierons","paierez","paieront"],
                                                                    'passé_simple':     ["payai","payas","paya","payâmes","payâtes","payèrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["paie","paies","paie","payions","payiez","paient"],
                                                                    'imparfait':        ["payasse","payasses","payât","payassions","payassiez","payassent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "paie", None, "payons", "payez", None] },
                                                'conditionnel': {   'présent':          ["paierais","paierais","paierait","paierions","paieriez","paieraient"] },
                                                'participe':    {
                                                                    'présent':          "payant",
                                                                    'passé':            "payé"
                                                                },
                                                'infinitif':    {   'présent':          "payer"}
                                            }
                        },
                        
                        ## VERBES DU 3E GROUPE

                        ## Dissoudre est basé sur soudre. Il y a plein de verbes que tu pourrais supprimer en évitant les composés… Recevoir > voir (mais pas pouvoir, savoir, etc), etc

                                {
                                'verbe':    "aller",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["vais","vas","va","allons","allez","vont"],
                                                                    'futur_simple':     ["irai","iras","ira","irons","irez","iront"],
                                                                    'imparfait':        ["allais","allais","allait","allions","alliez","allaient"],
                                                                    'passé_simple':     ["allai","allas","alla","allâmes","allâtes","allèrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["aille","ailles","aille","allions","alliez","aillent"],
                                                                    'imparfait':        ["allasse","allasses","allât","allassions","allassiez","allassent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "va", None, "allons", "allez", None] },
                                                'conditionnel': {   'présent':          ["irais","irais","irait","irions","iriez","iraient"] },
                                                'participe':    {
                                                                    'présent':          ["allant"],
                                                                    'passé':            ["allé"]
                                                                },
                                                'infinitif':    {   'présent':          ["aller"]}
                                            }
                        },
                        {
                                'verbe':    "asseoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["assois","assois","assoit","assoyons","assoyez","assoient"],
                                                                    'futur_simple':     ["assoirai","assoiras","assoira","assoirons","assoirez","assoiront"],
                                                                    'imparfait':        ["assoyais","assoyais","assoyait","assoyions","assoyiez","assoyaient"],
                                                                    'passé_simple':     ["assis","assis","assit","assîmes","assîtes","assirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["assoie","assoies","assoie","assoyions","assoyiez","assoient"],
                                                                    'imparfait':        ["assisse","assisses","assît","assissions","assissiez","assissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "assois", None, "assoyons", "assoyez", None] },
                                                'conditionnel': {   'présent':          ["assoirais","assoirais","assoirait","assoirions","assoiriez","assoiraient"] },
                                                'participe':    {
                                                                    'présent':          ["assoyant"],
                                                                    'passé':            ["assis"]
                                                                },
                                                'infinitif':    {   'présent':          ["asseoir"]}
                                            }
                        },
                        {
                                'verbe':    "clore",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["clos","clos","clôt",None,None,"closent"],
                                                                    'futur_simple':     ["clorai", "cloras", "clora", "clorons", "clorez", "cloront"],
                                                                    'imparfait':        None,
                                                                    'passé_simple':     None
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["close","closes","close","closions","closiez","closent"],
                                                                    'imparfait':        None
                                                                },
                                                'impératif':    {   'présent':          [None, "clos", None, None, None, None] },
                                                'conditionnel': {   'présent':          ["clorai","sclorais","clorait","clorions","cloriez","cloraient"] },
                                                'participe':    {
                                                                    'présent':          ["closant"],
                                                                    'passé':            ["clos"]
                                                                },
                                                'infinitif':    {   'présent':          ["clore"]}
                                            }
                        },
                        {
                                'verbe':    "moudre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["mouds","mouds","moud","moulons","moulez","moulent"],
                                                                    'futur_simple':     ["moudrai","moudras","moudra","moudrons","moudrez","moudront"],
                                                                    'imparfait':        ["moulais","moulais","moulait","moulions","mouliez","moulaient"],
                                                                    'passé_simple':     ["moulus","moulus","moulut","moulûmes","moulûtes","moulurent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["moule","moules","moule","moulions","mouliez","moulent"],
                                                                    'imparfait':        ["moulusse","moulusses","moulût","moulussions","moulussiez","moulussent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "mouds", None, "moulons", "moulez", None] },
                                                'conditionnel': {   'présent':          ["moudrais","moudrais","moudrait","moudrions","moudriez","moudraient"] },
                                                'participe':    {
                                                                    'présent':          ["moulant"],
                                                                    'passé':            ["moulu"]
                                                                },
                                                'infinitif':    {   'présent':          ["moudre"]}
                                            }
                        },
                        {
                                'verbe':    "boire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["bois","bois","boit","buvons","buvez","boivent"],
                                                                    'futur_simple':     ["boirai","boiras","boira","boirons","boirez","boiront"],
                                                                    'imparfait':        ["buvais","buvais","buvait","buvions","buviez","buvaient"],
                                                                    'passé_simple':     ["bus","bus","but","bûmes","bûtes","burent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["boive","boives","boive","buvions","buviez","boivent"],
                                                                    'imparfait':        ["busse","busses","bût","bussions","bussiez","bussent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "bois", None, "buvons", "buvez", None] },
                                                'conditionnel': {   'présent':          ["boirais","boirais","boirait","boirions","boiriez","boiraient"] },
                                                'participe':    {
                                                                    'présent':          ["buvant"],
                                                                    'passé':            ["bu"]
                                                                },
                                                'infinitif':    {   'présent':          ["boire"]}
                                            }
                        },
                        {
                                'verbe':    "haïr",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["hais","hais","hait","haïssons","haïssez","haïssent"],
                                                                    'futur_simple':     ["haïrai","haïras","haïra","haïrons","haïrez","haïront"],
                                                                    'imparfait':        ["haïssais","haïssais","haïssait","haïssions","haïssiez","haïssaient"],
                                                                    'passé_simple':     ["haïs","haïs","haït","haïmes","haïtes","haïrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["haïsse","haïsses","haïsse","haïssions","haïssiez","haïssent"],
                                                                    'imparfait':        ["haïsse","haïsses","haït","haïssions","haïssiez","haïssent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "hais", None, "haïssons", "haïssez", None] },
                                                'conditionnel': {   'présent':          ["haïrais","haïrais","haïrait","haïrions","haïriez","haïraient"] },
                                                'participe':    {
                                                                    'présent':          ["haïssanst"],
                                                                    'passé':            ["haï"]
                                                                },
                                                'infinitif':    {   'présent':          ["haïr"]}
                                            }
                        },
                        {
                                'verbe':    "écrire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["écris","écris","écrit","écrivons","écrivez","écrivent"],
                                                                    'futur_simple':     ["écrirai","écriras","écrira","écrirons","écrirez","écriront"],
                                                                    'imparfait':        ["écrivais","écrivais","écrivait","écrivions","écriviez","écrivaient"],
                                                                    'passé_simple':     ["écrivis","écrivis","écrivit","écrivîmes","écrivîtes","écrivirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["écrive","écrives","écrive","écrivions","écriviez","écrivent"],
                                                                    'imparfait':        ["écrivisse","écrivisses","écrivît","écrivissions","écrivissiez","écrivissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "écris", None, "écrivons", "écrivez", None] },
                                                'conditionnel': {   'présent':          ["écrirais","écrirais","écrirait","écririons","écririez","écriraient"] },
                                                'participe':    {
                                                                    'présent':          ["écrivant"],
                                                                    'passé':            ["écrit"]
                                                                },
                                                'infinitif':    {   'présent':          ["écrire"]}
                                            }
                        },
                        {
                                'verbe':    "naître",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["nais","nais","naît","naissons","naissez","naissent"],
                                                                    'futur_simple':     ["naîtrai","naîtras","naîtra","naîtrons","naîtrez","naîtront"],
                                                                    'imparfait':        ["naissais","naissais","naissait","naissions","naissiez","naissaient"],
                                                                    'passé_simple':     ["naquis","naquis","naquit","naquîmes","naquîtes","naquirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["naisse","naisses","naisse","naissions","naissiez","naissent"],
                                                                    'imparfait':        ["naquisse","naquisses","naquît","naquissions","naquissiez","naquissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "nais", None, "naissons", "naissez", None] },
                                                'conditionnel': {   'présent':          ["naîtrais","naîtrais","naîtrait","naîtrions","naîtriez","naîtraient"] },
                                                'participe':    {
                                                                    'présent':          ["naissant"],
                                                                    'passé':            ["né"]
                                                                },
                                                'infinitif':    {   'présent':          ["naître"]}
                                            }
                        },
                        {
                                'verbe':    "coudre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["couds","couds","coud","cousons","cousez","cousent"],
                                                                    'futur_simple':     ["coudrai","coudras","coudra","coudrons","coudrez","coudront"],
                                                                    'imparfait':        ["cousais","cousais","cousait","cousions","cousiez","cousaient"],
                                                                    'passé_simple':     ["cousis","cousis","cousit","cousîmes","cousîtes","cousirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["couse","couses","couse","cousions","cousiez","cousent"],
                                                                    'imparfait':        ["cousisse","cousisses","cousît","cousissions","cousissiez","cousissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "couds", None, "cousons", "cousez", None] },
                                                'conditionnel': {   'présent':          ["coudrais","coudrais","coudrait","coudrions","coudriez","coudraient"] },
                                                'participe':    {
                                                                    'présent':          ["cousant"],
                                                                    'passé':            ["cousu"]
                                                                },
                                                'infinitif':    {   'présent':          ["coudre"]}
                                            }
                        },
                        {
                                'verbe':    "croître",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["croîs","croîs","croît","croissons","croissez","croissent"],
                                                                    'futur_simple':     ["croîtrai","croîtras","croîtra","croîtrons","croîtrez","croîtront"],
                                                                    'imparfait':        ["croissais","croissais","croissait","croissions","croissiez","croissaient"],
                                                                    'passé_simple':     ["crûs","crûs","crût","crûmes","crûtes","crûrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["croisse","croisses","croisse","croissions","croissiez","croissent"],
                                                                    'imparfait':        ["crûsse","crûsses","crût","crûssions","crûssiez","crûssent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "croîs", None, "croissons", "croissez", None] },
                                                'conditionnel': {   'présent':          ["croîtrais","croîtrais","croîtrait","croîtrions","croîtriez","croîtraient"] },
                                                'participe':    {
                                                                    'présent':          ["croissant"],
                                                                    'passé':            ["crû"]
                                                                },
                                                'infinitif':    {   'présent':          ["croître"]}
                                            }
                        },
                        {
                                'verbe':    "devoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["dois","dois","doit","devons","devez","doivent"],
                                                                    'futur_simple':     ["devrai","devras","devra","devrons","devrez","devront"],
                                                                    'imparfait':        ["devais","devais","devait","devions","deviez","devaient"],
                                                                    'passé_simple':     ["dus","dus","dut","dûmes","dûtes","durent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["doive","doives","doive","devions","deviez","doivent"],
                                                                    'imparfait':        ["dusse","dusses","dût","dussions","dussiez","dussent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "dois", None, "devons", "devez", None] },
                                                'conditionnel': {   'présent':          ["devrais","devrais","devrait","devrions","devriez","devraient"] },
                                                'participe':    {
                                                                    'présent':          ["devant"],
                                                                    'passé':            ["dû"]
                                                                },
                                                'infinitif':    {   'présent':          ["devoir"]}
                                            }
                        },
                        {
                                'verbe':    "traire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["trais","trais","trait","trayons","trayez","traient"],
                                                                    'futur_simple':     ["trairai","trairas","traira","trairons","trairez","trairont"],
                                                                    'imparfait':        ["trayais","trayais","trayait","trayions","trayiez","trayaient"],
                                                                    'passé_simple':     None
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["traie","traies","traie","trayions","trayiez","traient"],
                                                                    'imparfait':        None
                                                                },
                                                'impératif':    {   'présent':          [None, "trais", None, "trayons", "trayez", None] },
                                                'conditionnel': {   'présent':          ["trairais","trairais","trairait","trairions","trairiez","trairaient"] },
                                                'participe':    {
                                                                    'présent':          ["trayant"],
                                                                    'passé':            ["trait"]
                                                                },
                                                'infinitif':    {   'présent':          ["traire"]}
                                            }
                        },
                        {
                                'verbe':    "soudre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["sous","sous","sout","solvons","solvez","solvent"],
                                                                    'futur_simple':     ["soudrai","soudras","soudra","soudrons","soudrez","soudront"],
                                                                    'imparfait':        ["solvais","solvais","solvait","solvions","solviez","solvaient"],
                                                                    'passé_simple':     ["solus","solus","solut","solûmes","solûtes","solurent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["solve","solves","solve","solvions","solviez","solvent"],
                                                                    'imparfait':        ["solusse","solusses","solût","solussions","solussiez","solussent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "sous", None, "solvons", "solvez", None] },
                                                'conditionnel': {   'présent':          ["soudrais","soudrais","soudrait","soudrions","soudriez","soudraient"] },
                                                'participe':    {
                                                                    'présent':          ["solvant"],
                                                                    'passé':            ["solu"]
                                                                },
                                                'infinitif':    {   'présent':          ["soudre"]}
                                            }
                        },
                        {
                                'verbe':    "dormir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["dors","dors","dort","dormons","dormez","dorment"],
                                                                    'futur_simple':     ["dormirai","dormiras","dormira","dormirons","dormirez","dormiront"],
                                                                    'imparfait':        ["dormais","dormais","dormait","dormions","dormiez","dormaient"],
                                                                    'passé_simple':     ["dormis","dormis","dormit","dormîmes","dormîtes","dormirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["dorme","dormes","dorme","dormions","dormiez","dorment"],
                                                                    'imparfait':        ["dormisse","dormisses","dormît","dormissions","dormissiez","dormissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "dors", None, "dormons", "dormez", None] },
                                                'conditionnel': {   'présent':          ["dormirais","dormirais","dormirait","dormirions","dormiriez","dormiraient"] },
                                                'participe':    {
                                                                    'présent':          ["dormant"],
                                                                    'passé':            ["dormi"]
                                                                },
                                                'infinitif':    {   'présent':          ["dormir"]}
                                            }
                        },
                        {
                                'verbe':    "dire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["dis","dis","dit","disons","dites","disent"],
                                                                    'futur_simple':     ["dirai","diras","dira","dirons","direz","diront"],
                                                                    'imparfait':        ["disais","disais","disait","disions","disiez","disaient"],
                                                                    'passé_simple':     ["dis","dis","dit","dîmes","dîtes","dirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["dise","dises","dise","disions","disiez","disent"],
                                                                    'imparfait':        ["disse","disses","dît","dissions","dissiez","dissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "dis", None, "disons", "dites", None] },
                                                'conditionnel': {   'présent':          ["dirais","dirais","dirait","dirions","diriez","diraient"] },
                                                'participe':    {
                                                                    'présent':          ["disant"],
                                                                    'passé':            ["dit"]
                                                                },
                                                'infinitif':    {   'présent':          ["dire"]}
                                            }
                        },
                        {
                                'verbe':    "lire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["lis", "lis", "lit", "lisons", "lisez", "lisent"],
                                                                    'imparfait':        ["lisais", "lisais", "lisait", "lisions", "lisiez", "lisaient"],
                                                                    'futur_simple':     ["lirai", "liras", "lira", "lirons", "lirez", "liront"],
                                                                    'passé_simple':     ["lus", "lus", "lut", "lûmes", "lûtes", "lurent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["lise", "lises", "lise", "lisions", "lisiez", "lisent"],
                                                                    'imparfait':        ["lusse", "lusses", "lût", "lussions", "lussiez", "lussent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "lis", None, "lisons", "lisez", None] },
                                                'conditionnel': {   'présent':          ["lirais", "lirais", "lirait", "lirions", "liriez", "liraient"] },
                                                'participe':    {
                                                                    'présent':          ["lisant"],
                                                                    'passé':            ["lu"]
                                                                },
                                                'infinitif':    {   'présent':          ["lire"]}
                                            }
                        },
                        {
                                'verbe':    "nuire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["nuis", "nuis", "nuit", "nuisons", "nuisez", "nusient"],
                                                                    'futur_simple':     ["nuirai", "nuiras", "nuira", "nuirons", "nuirez", "nuiront"],
                                                                    'imparfait':        ["nuisais", "nuisais", "nuisait", "nuisions", "nuisiez", "nuisaient"],
                                                                    'passé_simple':     ["nuisis", "nuisis", "nuisit", "nuisîmes", "nuisîtes", "nuisirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["nuise", "nuises", "nuise", "nuisions", "nuisiez", "nuisent"],
                                                                    'imparfait':        ["nuisisse","nuisisses","nuisît","nuisissions","nuisissiez","nuisissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "nuis", None, "nuisons", "nuisez", None] },
                                                'conditionnel': {   'présent':          ["nuirais","nuirais","nuirait","nuirions","nuiriez","nuiraient"] },
                                                'participe':    {
                                                                    'présent':          ["nuisant"],
                                                                    'passé':            ["nui"]
                                                                },
                                                'infinitif':    {   'présent':          ["nuire"]}
                                            }
                        },
                        {
                                'verbe':    "paître",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["pais","pais","paît","paissons","paissez","paissent"],
                                                                    'futur_simple':     ["paîtrai","paîtras","paîtra","paîtrons","paîtrez","paîtront"],
                                                                    'imparfait':        ["paissais","paissais","paissait","paissions","paissiez","paissaient"],
                                                                    'passé_simple':     None
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["paisse","paisses","paisse","paissions","paissiez","paissent"],
                                                                    'imparfait':        None
                                                                },
                                                'impératif':    {   'présent':          [None,"pais",None,"paissons","paissez",None] },
                                                'conditionnel': {   'présent':          ["paîtrais","paîtrais","paîtrait","paîtrions","paîtriez","paîtraient"] },
                                                'participe':    {
                                                                    'présent':          ["paissant"],
                                                                    'passé':            ["pu"]
                                                                },
                                                'infinitif':    {   'présent':          ["paître"]}
                                            }
                        },
                        {
                                'verbe':    "suivre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["suis","suis","suit","suivons","suivez","suivent"],
                                                                    'futur_simple':     ["suivrai","suivras","suivra","suivrons","suivrez","suivront"],
                                                                    'imparfait':        ["suivais","suivais","suivait","suivions","suiviez","suivaient"],
                                                                    'passé_simple':     ["suivis","suivis","suivit","suivîmes","suivîtes","suivirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["suive","suives","suive","suivions","suiviez","suivent"],
                                                                    'imparfait':        ["suivisse","suivisses","suivît","suivissions","suivissiez","suivissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "suis", None, "suivons", "suivez", None] },
                                                'conditionnel': {   'présent':          ["suivrais","suivrais","suivrait","suivrions","suivriez","suivraient"] },
                                                'participe':    {
                                                                    'présent':          ["suivant"],
                                                                    'passé':            ["suivi"]
                                                                },
                                                'infinitif':    {   'présent':          ["suivre"]}
                                            }
                        },
                        {
                                'verbe':    "pouvoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["peux","peux","peut","pouvons","pouvez","peuvent"],
                                                                    'futur_simple':     ["pourrai","pourras","pourra","pourrons","pourrez","pourront"],
                                                                    'imparfait':        ["pouvais","pouvais","pouvait","pouvions","pouviez","pouvaient"],
                                                                    'passé_simple':     ["pus","pus","put","pûmes","pûtes","purent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["puisse","puisses","puisse","puissions","puissiez","puissent"],
                                                                    'imparfait':        ["pusse","pusses","pût","pussions","pussiez","pussent"]
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          ["pourrais","pourrais","pourrait","pourrions","pourriez","pourraient"] },
                                                'participe':    {
                                                                    'présent':          ["pouvant"],
                                                                    'passé':            ["pu"]
                                                                },
                                                'infinitif':    {   'présent':          ["pouvoir"]}
                                            }
                        },
                        {
                                'verbe':    "prendre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["prends","prends","prend","prenons","prenez","prennent"],
                                                                    'futur_simple':     ["prendrai","prendras","prendra","prendrons","prendrez","prendront"],
                                                                    'imparfait':        ["prenais","prenais","prenait","prenions","preniez","prenaient"],
                                                                    'passé_simple':     ["pris","pris","prit","prîmes","prîtes","prirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["prenne","prennes","prenne","prenions","preniez","prennent"],
                                                                    'imparfait':        ["prisse","prisses","prît","prissions","prissiez","prissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "prend", None, "prenons", "prenez", None] },
                                                'conditionnel': {   'présent':          ["prendrais","prendrais","prendrait","prendrions","prendriez","prendraient"] },
                                                'participe':    {
                                                                    'présent':          ["prenant"],
                                                                    'passé':            ["pris"]
                                                                },
                                                'infinitif':    {   'présent':          ["prendre"]}
                                            }
                        },
                        {
                                'verbe':    "voir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["vois","vois","voit","voyons","voyez","voient"],
                                                                    'futur_simple':     ["verrai","verras","verra","verrons","verrez","verront"],
                                                                    'imparfait':        ["voyais","voyais","voyait","voyions","voyiez","voyaient"],
                                                                    'passé_simple':     ["vis","vis","vit","vîmes","vîtes","virent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["voie","voies","voie","voyions","voyiez","voient"],
                                                                    'imparfait':        ["visse","visses","vît","vissions","vissiez","vissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "vois", None, "voyons", "voyez", None] },
                                                'conditionnel': {   'présent':          ["verrais","verrais","verrait","verrions","verriez","verraient"] },
                                                'participe':    {
                                                                    'présent':          ["voyant"],
                                                                    'passé':            ["vu"]
                                                                },
                                                'infinitif':    {   'présent':          ["voir"]}
                                            }
                        },
                        {
                                'verbe':    "rire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["ris","ris","rit","rions","riez","rient"],
                                                                    'futur_simple':     ["rirai","riras","rira","rirons","rirez","riront"],
                                                                    'imparfait':        ["riais","riais","riait","riions","riiez","riaient"],
                                                                    'passé_simple':     ["ris","ris","rit","rîmes","rîtes","rirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["rie","ries","rie","riions","riiez","rient"],
                                                                    'imparfait':        ["risse","risses","rît","rissions","rissiez","rissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "ris", None, "rions", "riez", None] },
                                                'conditionnel': {   'présent':          ["rirais","rirais","rirait","ririons","ririez","riraient"] },
                                                'participe':    {
                                                                    'présent':          ["riant"],
                                                                    'passé':            ["ri"]
                                                                },
                                                'infinitif':    {   'présent':          ["rire"]}
                                            }
                        },
                        {
                                'verbe':    "savoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["sais","sais","sait","savons","savez","savent"],
                                                                    'futur_simple':     ["saurai","sauras","saura","saurons","saurez","sauront"],
                                                                    'imparfait':        ["savais","savais","savait","savions","saviez","savaient"],
                                                                    'passé_simple':     ["sus","sus","sut","sûmes","sûtes","surent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["sache","saches","sache","sachions","sachiez","sachent"],
                                                                    'imparfait':        ["susse","susses","sût","sussions","sussiez","sussent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "sache", None, "sachons", "sachez", None] },
                                                'conditionnel': {   'présent':          ["saurais","saurais","saurait","saurions","sauriez","sauraient"] },
                                                'participe':    {
                                                                    'présent':          ["sachant"],
                                                                    'passé':            ["su"]
                                                                },
                                                'infinitif':    {   'présent':          ["savoir"]}
                                            }
                        },
                        {
                                'verbe':    "suffire",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["suffis","suffis","suffit","suffisons","suffisez","suffisent"],
                                                                    'futur_simple':     ["suffirai","suffiras","suffira","suffirons","suffirez","suffiront"],
                                                                    'imparfait':        ["suffisais","suffisais","suffisait","suffisions","suffisiez","suffisaient"],
                                                                    'passé_simple':     ["suffis","suffis","suffit","suffîmes","suffîtes","suffirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["suffise","suffises","suffise","suffisions","suffisiez","suffisent"],
                                                                    'imparfait':        ["suffisse","suffisses","suffît","suffissions","suffissiez","suffissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "suffit", None, "suffisons", "suffisez", None] },
                                                'conditionnel': {   'présent':          ["suffirais","suffirais","suffirait","suffirions","suffiriez","suffiraient"] },
                                                'participe':    {
                                                                    'présent':          ["suffisant"],
                                                                    'passé':            ["suffi"]
                                                                },
                                                'infinitif':    {   'présent':          ["suffire"]}
                                            }
                        },
                        {
                                'verbe':    "vaincre",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["vaincs", "vaincs", "vainc", "vainquons", "vainquez", "vainquent"],
                                                                    'futur_simple':     ["vaincrai", "vaincras", "vaincra", "vaincrons", "vaincrez", "vaincront"],
                                                                    'imparfait':        ["vainquais", "vainquais", "vainquait", "vainquions", "vainquiez", "vainquaient"],
                                                                    'passé_simple':     ["vainquis", "vainquis", "vainquit", "vainquîmes", "vainquîtes", "vainquirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["vainque", "vainques", "vainque", "vainquions", "vainquiez", "vainquent"],
                                                                    'imparfait':        ["vainquisse", "vainquisses", "vainquît", "vainquissions", "vainquissiez", "vainquissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "vaincs", None, "vainquons", "vainquez", None] },
                                                'conditionnel': {   'présent':          ["vaincrais", "vaincrais", "vaincrait", "vaincrions", "vaincriez", "vaincraient"] },
                                                'participe':    {
                                                                    'présent':          ["vainquant"],
                                                                    'passé':            ["vaincu"]
                                                                },
                                                'infinitif':    {   'présent':          ["vaincre"]}
                                            }
                        },
                        {
                                'verbe':    "valoir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["vaux","vaux","vaut","valons","valez","valent"],
                                                                    'futur_simple':     ["vaudrai","vaudras","vaudra","vaudrons","vaudrez","vaudront"],
                                                                    'imparfait':        ["valais","valais","valait","valions","valiez","valaient"],
                                                                    'passé_simple':     ["valus","valus","valut","valûmes","valûtes","valurent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["vaille","vailles","vaille","valions","valiez","vaillent"],
                                                                    'imparfait':        ["valusse","valusses","valût","valussions","valussiez","valussent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "vaux", None, "valons", "valez", None] },
                                                'conditionnel': {   'présent':          ["vaudrais","vaudrais","vaudrait","vaudrions","vaudriez","vaudraient"] },
                                                'participe':    {
                                                                    'présent':          ["valant"],
                                                                    'passé':            ["valu"]
                                                                },
                                                'infinitif':    {   'présent':          ["valoir"]}
                                            }
                        },
                        {
                                'verbe':    "vouloir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["veux","veux","veut","voulons","voulez","veulent"],
                                                                    'futur_simple':     ["voudrai","voudras","voudra","voudrons","voudrez","voudront"],
                                                                    'imparfait':        ["voulais","voulais","voulait","voulions","vouliez","voulaient"],
                                                                    'passé_simple':     ["voulus","voulus","voulut","voulûmes","voulûtes","voulurent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["veuille","veuilles","veuille","voulions","vouliez","veuillent"],
                                                                    'imparfait':        ["voulusse","voulusses","voulût","voulussions","voulussiez","voulussent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "veuille", None, "voulons", "vouillez", None] },
                                                'conditionnel': {   'présent':          ["voudrais","voudrais","voudrait","voudrions","voudriez","voudraient"] },
                                                'participe':    {
                                                                    'présent':          ["voulant"],
                                                                    'passé':            ["voulu"]
                                                                },
                                                'infinitif':    {   'présent':          ["vouloir"]}
                                            }
                        },
                             ## Verbes du 3-ir
                        {
                                'verbe':    "fuir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["fuis","fuis","fuit","fuyons","fuyez","fuient"],
                                                                    'futur_simple':     ["fuirai","fuiras","fuira","fuirons","fuirez","fuiront"],
                                                                    'imparfait':        ["fuyais","fuyais","fuyait","fuyions","fuyiez","fuyaient"],
                                                                    'passé_simple':     ["fuis","fuis","fuit","fuîmes","fuîtes","fuirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["fuie","fuies","fuie","fuyions","fuyiez","fuient"],
                                                                    'imparfait':        ["fuisse","fuisses","fuît","fuissions","fuissiez","fuissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "fuis", None, "fuyons", "fuyez", None] },
                                                'conditionnel': {   'présent':          ["fuirais","fuirais","fuirait","fuirions","fuiriez","fuiraient"] },
                                                'participe':    {
                                                                    'présent':          ["fuyant"],
                                                                    'passé':            ["fui"]
                                                                },
                                                'infinitif':    {   'présent':          ["fuir"]}
                                            }
                        },
                        {
                                'verbe':    "quérir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["quiers","quiers","quiert","quérons","quérez","quièrent"],
                                                                    'futur_simple':     ["querrai","querras","querra","querrons","querrez","querront"],
                                                                    'imparfait':        ["quérais","quérais","quérait","quérions","quériez","quéraient"],
                                                                    'passé_simple':     ["quis","quis","quit","quîmes","quîtes","quirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["quière","quières","quière","quérions","quériez","quièrent"],
                                                                    'imparfait':        ["quisse","quisses","quît","quissions","quissiez","quissent"]
                                                                },
                                                'impératif':    {   'présent':          [None,"quiers",None,"quérons","quérez",None], },
                                                'conditionnel': {   'présent':          ["querrais","querrais","querrait","querrions","querriez","querraient"] },
                                                'participe':    {
                                                                    'présent':          ["quérant"],
                                                                    'passé':            ["quis"]
                                                                },
                                                'infinitif':    {   'présent':          ["quérir"]}
                                            }
                        },
                        {
                                'verbe':    "faillir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["faux","faux","faut","faillons","faillez","faillent"],
                                                                    'futur_simple':     ["faillirai","failliras","faillira","faillirons","faillirez","failliront"],
                                                                    'imparfait':        ["faillais","faillais","faillait","faillions","failliez","faillaient"],
                                                                    'passé_simple':     ["faillis","faillis","faillit","faillîmes","faillîtes","faillirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["faillisse","faillisses","faillisse","faillissions","faillissiez","faillissent"],
                                                                    'imparfait':        ["faillisse","faillisses","faillît","faillissions","faillissiez","faillissent"]
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          ["faillirais","faillirais","faillirait","faillirions","failliriez","failliraient"] },
                                                'participe':    {
                                                                    'présent':          ["faillant"],
                                                                    'passé':            ["failli"]
                                                                },
                                                'infinitif':    {   'présent':          ["faillir"]}
                                            }
                        },
                        {
                                'verbe':    "ouïr",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["ois","ois","oit","oyons","oyez","oient"],
                                                                    'futur_simple':     ["ouïrai","ouïras","ouïra","ouïrons","ouïrez","ouïront"],
                                                                    'imparfait':        ["oyais","oyais","oyait","oyions","oyiez","oyaient"],
                                                                    'passé_simple':     ["ouïs","ouïs","ouït","ouïmes","ouïtes","ouïrent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["oie","oies","oie","oyions","oyiez","oient"],
                                                                    'imparfait':        ["ouïsse","ouïsses","ouït","ouïssions","ouïssiez","ouïssent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "ois", None, "oyons", "oyez", None] },
                                                'conditionnel': {   'présent':          ["ouïrais","ouïrai","souïrait","ouïrions","ouïriez","ouïraient"] },
                                                'participe':    {
                                                                    'présent':          ["oyant"],
                                                                    'passé':            ["ouï"]
                                                                },
                                                'infinitif':    {   'présent':          ["ouïr"]}
                                            }
                        },
                        {
                                'verbe':    "gésir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["gis","gis","gît","gisons","gisez","gisent"],
                                                                    'futur_simple':     None,
                                                                    'imparfait':        ["gisais","gisais","gisait","gisions","gisiez","gisaient"],
                                                                    'passé_simple':     None
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          None,
                                                                    'imparfait':        None
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          None },
                                                'participe':    {
                                                                    'présent':          ["gisant"],
                                                                    'passé':            None
                                                                },
                                                'infinitif':    {   'présent':          ["gésir"]}
                                            }
                        },
                        {
                                'verbe':    "ouvrir",
                                'groupe':   3,
                                'type':     "verbe",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["ouvre","ouvres","ouvre","ouvrons","ouvrez","ouvrent"],
                                                                    'futur_simple':     ["ouvrirai","ouvriras","ouvrira","ouvrirons","ouvrirez","ouvriront"],
                                                                    'imparfait':        ["ouvrais","ouvrais","ouvrait","ouvrions","ouvriez","ouvraient"],
                                                                    'passé_simple':     ["ouvris","ouvris","ouvrit","ouvrîmes","ouvrîtes","ouvrirent"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["ouvre","ouvres","ouvre","ouvrions","ouvriez","ouvrent"],
                                                                    'imparfait':        ["ouvrisse","ouvrisses","ouvrît","ouvrissions","ouvrissiez","ouvrissent"]
                                                                },
                                                'impératif':    {   'présent':          [None, "ouvre", None, "ouvrons", "ouvrez", None] },
                                                'conditionnel': {   'présent':          ["ouvrirais","ouvrirais","ouvrirait","ouvririons","ouvririez","ouvriraient"] },
                                                'participe':    {
                                                                    'présent':          ["ouvrant"],
                                                                    'passé':            ["ouvert"]
                                                                },
                                                'infinitif':    {   'présent':          ["ouvrir"]}
                                            }
                        },
                        
                        ## VERBES IMPERSONNELS
                        
                        {
                                'verbe':    "falloir",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["faut"],
                                                                    'futur_simple':     ["faudra"],
                                                                    'imparfait':        ["fallait"],
                                                                    'passé_simple':     ["fallut"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["faille"],
                                                                    'imparfait':        ["fallût"]
                                                                },
                                                'impératif':    {   'présent':          ["faut"] },
                                                'conditionnel': {   'présent':          ["faudrait"] },
                                                'participe':    {
                                                                    'présent':          None,
                                                                    'passé':            ["fallu"]
                                                                },
                                                'infinitif':    {   'présent':          ["falloir"]}
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
                                                                    'présent':          ["pleuvant"],
                                                                    'passé':            ["plu"]
                                                                },
                                                'infinitif':    {   'présent':          ["pleuvoir"]}
                                            }
                        },
                        {
                                'verbe':    "neiger",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["neige"],
                                                                    'futur_simple':     ["neigera"],
                                                                    'imparfait':        ["neigeait"],
                                                                    'passé_simple':     ["neigea"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["neige"],
                                                                    'imparfait':        ["neigeât"]
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          ["neigerait"] },
                                                'participe':    {
                                                                    'présent':          ["neigeant"],
                                                                    'passé':            ["neigé"]
                                                                },
                                                'infinitif':    {   'présent':          ["neiger"]}
                                            }
                        },
                        {
                                'verbe':    "venter",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["vente"],
                                                                    'futur_simple':     ["ventera"],
                                                                    'imparfait':        ["ventait"],
                                                                    'passé_simple':     ["venta"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["vente"],
                                                                    'imparfait':        ["ventât"]
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          ["venterait"] },
                                                'participe':    {
                                                                    'présent':          ["ventant"],
                                                                    'passé':            ["venté"]
                                                                },
                                                'infinitif':    {   'présent':          ["venter"]}
                                            }
                        },
                        {
                                'verbe':    "bruiner",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["bruine"],
                                                                    'futur_simple':     ["bruinera"],
                                                                    'imparfait':        ["bruinait"],
                                                                    'passé_simple':     ["bruina"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["bruine"],
                                                                    'imparfait':        ["bruinât"]
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          ["bruinerait"] },
                                                'participe':    {
                                                                    'présent':          ["bruinant"],
                                                                    'passé':            ["bruiné"]
                                                                },
                                                'infinitif':    {   'présent':          ["bruiner"]}
                                            }
                        },
                        {
                                'verbe':    "grêler",
                                'groupe':   3,
                                'type':     "impersonnel",
                                'feuille':  {
                                                'indicatif':    {
                                                                    'présent':          ["grêle"],
                                                                    'futur_simple':     ["grêlera"],
                                                                    'imparfait':        ["grêlait"],
                                                                    'passé_simple':     ["grêla"]
                                                                },
                                                'subjonctif':   {
                                                                    'présent':          ["grêle"],
                                                                    'imparfait':        ["grêlât"]
                                                                },
                                                'impératif':    {   'présent':          None },
                                                'conditionnel': {   'présent':          ["grêlerait"] },
                                                'participe':    {
                                                                    'présent':          ["grêlant"],
                                                                    'passé':            ["grêlé"]
                                                                },
                                                'infinitif':    {   'présent':          ["grêler"]}
                                            }
                        },
                    ]
