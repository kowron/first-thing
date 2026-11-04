# Układ strony „Kościec osiowy” (wczytywany przez build_os.py)
# 9 wąskich kolumn: kręgosłup 6 (szyjne ×2, piersiowe, lędźwiowe, krzyżowa ×2), klatka 3 (żebra ×2, mostek)
import os as _os
CW = float(_os.environ.get('CWS', 112))     # kolumna kręgosłupa
CT = float(_os.environ.get('CWT', 104))     # kolumna klatki
G7 = 7
C2 = 2 * CW + G7
T2 = 2 * CT + G7
CH_WIDTHS = [6 * CW + 5 * G7, 4 * CT + 3 * G7]
MODE.update({'Kręgosłup': 'intro-row', 'Kręgi prawdziwe': 'row', 'Kręgi szyjne': 'grid2', 'Kręgi piersiowe': 'list',
             'Kręgi lędźwiowe': 'list', 'Kręgi rzekome': 'list', 'Kość krzyżowa': 'grid2',
             'Klatka piersiowa': 'row', 'Żebra': 'grid2', 'Podział żeber': 'list', 'Żebra rzekome (VIII–XII)': 'list',
             'Części żebra': 'list', 'Żebra o odrębnych cechach': 'list', 'Mostek': 'grid2',
             'Części mostka': 'list', 'Klatka piersiowa jako całość': 'grid2'})
WIDTH.update({'Kręgosłup /kids': [4 * CW + 3 * G7, C2], 'Kręgi prawdziwe /kids': [C2, CW, CW]})
ROWSPEC.update({'Klatka piersiowa': [(T2, ['Żebra']), (T2, ['Mostek', 'Klatka piersiowa jako całość'])]})
GRID2.update({'Mostek': ['Mostek – cechy ogólne', 'Wcięcia mostka', 'Kąt mostka']})
FIG.update({
    'Budowa ogólna kręgu': ['kr_th_gora', 'kr_th_bok'],
    'Kręg szyjny typowy': ['kr_c_gora', 'kr_c_przod'],
    'Kręg szczytowy': ['kr_c1_gora'],
    'Kręg obrotowy': ['kr_c2_bok', 'kr_c2_przod'],
    'Kręg wystający': ['kr_c7_gora'],
    'Kręg piersiowy typowy': ['kr_th_dolki'],
    'Dwunasty kręg piersiowy': ['kr_th12_bok'],
    'Kręg lędźwiowy typowy': ['kr_l_gora', 'kr_l_bok'],
    'Kształt i położenie kości krzyżowej': ['kr_sacrum_bok'],
    'Powierzchnia miedniczna': ['kr_sacrum_przod'],
    'Powierzchnia grzbietowa': ['kr_sacrum_tyl'],
    'Kość guziczna': ['kr_coccyx'],
    'Żebra – cechy ogólne': ['zebro_typowe'],
    'Kość żebrowa': ['zebro_tyl'],
    'Żebro I': ['zebro_I'],
    'Żebro II': ['zebro_II'],
    'Żebra XI i XII': ['zebra_XI_XII'],
    'Mostek – cechy ogólne': ['mostek_przod', 'mostek_bok'],
    'Ściany i kształt klatki': ['klatka_przod'],
})
