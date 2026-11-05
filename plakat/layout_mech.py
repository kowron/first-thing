# Układ strony „Połączenia i mechanika” (wczytywany przez build_os.py)
# Kręgosłup: 3 kolumny (przedkrzyżowe ×2 szerokości, kość krzyżowa, krzywizny); klatka: 2 szerokości + 1;
# oddychanie: 2 szerokości (przepona i mechanika oddychania w grid2).  W1 = szerokość pojedynczej kolumny (env CWM).
import os as _os
G7 = 7
W1 = float(_os.environ.get('CWM', 120))
W2 = 2 * W1 + G7
WK = float(_os.environ.get('CWK', 150))        # kolumna „Mechanika klatki piersiowej” (szersza – ma dużo rysunków)
WP = (W2 + W1 + G7) - WK - G7                  # blok „Połączenia żeber i mostka”
CH_WIDTHS = [W2 + 2 * W1 + 2 * G7, W2 + W1 + G7, W2]
COLOR.update({'Oddychanie': 'c4'})
MODE.update({'Kręgosłup': 'row', 'Klatka piersiowa': 'row', 'Oddychanie': 'list',
             'Połączenia kręgów przedkrzyżowych': 'list', 'Połączenia ścisłe': 'list', 'Chrząstkozrosty': 'list',
             'Więzozrosty': 'grid2', 'Połączenia ruchome – stawy': 'list',
             'Połączenia kości krzyżowej': 'list', 'Połączenia z kośćmi miednicznymi': 'list',
             'Więzadła wzmacniające staw krzyżowo-biodrowy': 'list',
             'Więzadła łączące kość krzyżową z kością kulszową': 'list',
             'Krzywizny kręgosłupa': 'list',
             'Połączenia żeber i mostka': 'grid2', 'Połączenia żeber z kręgosłupem – stawy żebrowo-kręgowe': 'list', 'Połączenia żeber z mostkiem': 'list',
             'Mechanika klatki piersiowej': 'list', 'Ruchomość klatki piersiowej': 'list',
             'Przepona': 'grid2', 'Mechanika oddychania': 'grid2'})
ROWSPEC.update({
    'Kręgosłup': [(W2, ['Połączenia kręgów przedkrzyżowych']), (W1, ['Połączenia kości krzyżowej']), (W1, ['Krzywizny kręgosłupa'])],
    'Klatka piersiowa': [(WP, ['Połączenia żeber i mostka']), (WK, ['Mechanika klatki piersiowej'])],
})
GRID2.update({'Połączenia żeber i mostka': ['Połączenia żeber z kręgosłupem – stawy żebrowo-kręgowe']})
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
    'Krzywizny w płaszczyźnie pośrodkowej': ['krzywizny_dorosly'],
    'Powstawanie krzywizn': ['krzywizny_os_czasu'],
    'Krzywizny w płaszczyźnie czołowej': ['skolioza'],
    'Odporność klatki piersiowej': ['klatka_odpornosc'],
    'Mechanika kości żebrowej': ['zebro_os_ruchu', 'zebra_ruchy_wymiary'],
    'Mechanika chrząstki żebrowej': ['chrzastka_mechanika'],
    'Ruchy mostka': ['mostek_ruchy'],
})

# --- osobne strony (ONLY=polkreg | klodd): szerokości z env CWM (kolumna kręgosłupa), CWP/CWK/CWO (klatka, oddychanie)
ONLY = _os.environ.get('ONLY', '')
if ONLY == 'polkreg':
    CH_WIDTHS = [W2 + 2 * W1 + 2 * G7]
    CHAPTERS_FN = lambda c: [c['CHAPTERS'][0]]
    PAGE_TITLE, PAGE_SUB = 'Połączenia kręgosłupa', 'stawy · więzozrosty · chrząstkozrosty · kość krzyżowa · krzywizny'
elif ONLY == 'klodd':
    WP6 = float(_os.environ.get('CWP', 300))
    WK6 = float(_os.environ.get('CWK6', 190))
    WO6 = float(_os.environ.get('CWO', 400))
    CH_WIDTHS = [WP6 + WK6 + G7, WO6]
    ROWSPEC.update({'Klatka piersiowa': [(WP6, ['Połączenia żeber i mostka']), (WK6, ['Mechanika klatki piersiowej'])]})
    CHAPTERS_FN = lambda c: [c['CHAPTERS'][1], c['CHAPTERS'][2]]
    PAGE_TITLE, PAGE_SUB = 'Klatka i oddychanie', 'połączenia żeber i mostka · mechanika klatki · przepona · mechanika oddychania'
