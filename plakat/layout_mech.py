# Układ strony „Połączenia i mechanika” (wczytywany przez build_os.py)
CH_WIDTHS = [400, 330, 400]
COLOR.update({'Oddychanie': 'c4'})
MODE.update({'Kręgosłup': 'list', 'Klatka piersiowa': 'list', 'Oddychanie': 'list',
             'Połączenia kręgów przedkrzyżowych': 'list', 'Połączenia ścisłe': 'list', 'Więzozrosty': 'grid2',
             'Połączenia kości krzyżowej': 'list', 'Połączenia z kośćmi miednicznymi': 'list',
             'Więzadła wzmacniające staw krzyżowo-biodrowy': 'grid2', 'Więzadła łączące kość krzyżową z kością kulszową': 'grid2',
             'Połączenia żeber i mostka': 'list', 'Przepona': 'list', 'Mechanika oddychania': 'list'})
GFIG.update({
    'Więzozrosty': ('Przekrój pośrodkowy odcinka lędźwiowego – więzadła kręgosłupa', ['pol_przekroj_strzalkowy']),
    'Połączenia z kośćmi miednicznymi': ('Staw krzyżowo-biodrowy i więzadła miednicy', ['pol_krzyzowo_biodrowy']),
})
FIG.update({
    'Krążki międzykręgowe': ['pol_krazek_gora'],
    'Więzadło karkowe': ['pol_karkowe'],
    'Stawy międzykręgowe': ['pol_staw_miedzykregowy'],
    'Stawy głów żebrowych': ['pol_zebro_kreg_bok'],
    'Stawy żebrowo-poprzeczne': ['pol_zebro_kreg_gora'],
    'Stawy mostkowo-żebrowe': ['pol_mostkowo_zebrowe'],
    'Krzywizny w płaszczyźnie pośrodkowej': ['krzywizny_dorosly', 'krzywizny_os_czasu'],
    'Krzywizny w płaszczyźnie czołowej': ['skolioza'],
    'Odporność': ['klatka_odpornosc'],
    'Odporność klatki': ['klatka_odpornosc'],
    'Mechanika żebra kostnego': ['zebro_os_ruchu', 'zebra_ruchy_wymiary'],
})
