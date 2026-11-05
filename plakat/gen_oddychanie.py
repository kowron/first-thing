# -*- coding: utf-8 -*-
# Treść „Przepona” i „Mechanika oddychania” na stronę 3 – ze sprawdzonych już danych (data.py, l3_klatka.json, panel MECH z wersji 2)
import json, sys
sys.path.insert(0, '/home/user/first-thing/plakat')
from data import KLATKA

def walk(g):
    for it in g['items']:
        yield it
        if it['kind'] == 'g':
            yield from walk(it)

P = next(it for it in walk(KLATKA) if it.get('pl') == 'przepona')
L3 = json.load(open('/home/user/first-thing/plakat/l3_klatka.json', encoding='utf-8'))
LP = L3['muscles']['przepona']
LG = L3['groups']['Przepona']
OD = next(x for x in L3['panels'] if x['id'] == 'oddychanie_l3')['items']

def t(it):            # punkt poziomu 3 → tekst z numerem strony (do sekcji poziomu 2)
    return f'{it["t"]} (s. {it["pg"]})'

tree = [
 {"type": "group", "title": "Przepona", "lat": "diaphragma", "pg": "689–696",
  "why": "mięśniowo-ścięgnista przegroda między jamą klatki piersiowej a jamą brzuszną", "q": "co trzeba o niej wiedzieć?",
  "l3": LG,
  "children": [
   {"type": "card", "title": "Części i przyczepy", "pg": "690–692", "figs": ["przepona_dol"],
    "sections": [
     {"k": "CZĘŚCI", "items": ["**część lędźwiowa** {{pars lumbalis}}", "**część żebrowa** {{pars costalis}}", "**część mostkowa** {{pars sternalis}}"]},
     {"k": "PRZYCZEP POCZĄTKOWY", "items": P['o']},
     {"k": "PRZYCZEP KOŃCOWY", "items": P['i']},
     {"k": "ŚRODEK ŚCIĘGNISTY", "items": ["kształt trójpłatowego liścia koniczyny – na płatku przednim leży serce z osierdziem, na bocznych podstawy płuc [[centrum tendineum]] (s. 692)"]}],
    "l3": [LP[0], LP[1], LP[2], LP[3], LP[4]]},
   {"type": "card", "title": "Otwory", "pg": "691–693",
    "sections": [{"k": "OTWORY I SZCZELINY", "items": [
        "**rozwór aortowy** {{hiatus aorticus}} – na wysokości Th12, między odnogami a kręgosłupem: aorta i przewód piersiowy (s. 691–692)",
        "**rozwór przełykowy** {{hiatus esophageus}} – wyżej i nieco na lewo od aortowego, w części lędźwiowej: przełyk oraz pnie błędne przedni i tylny (s. 691, 693)",
        "**otwór żyły głównej** {{foramen venae cavae}} – w środku ścięgnistym, na granicy płatka prawego i przedniego: żyła główna dolna i gałązki brzuszne n. przeponowego prawego (s. 692–693)",
        "**szczeliny w odnogach**: n. trzewny większy (często też mniejszy), żyła nieparzysta (odnoga prawa) i nieparzysta krótka (odnoga lewa); bardziej bocznie pień współczulny (s. 691, 693)"]}],
    "l3": [LP[5], LP[6], LP[19],
           {"k": "!", "t": "Na s. 693 Bochenek pisze, że w odnodze prawej biegnie ż. nieparzysta krótka; na s. 691 – prawa: ż. nieparzysta, lewa: ż. nieparzysta krótka.", "pg": "691, 693"}]},
   {"type": "card", "title": "Trójkąty i przepukliny", "pg": "692, 695",
    "sections": [{"k": "TRÓJKĄTY", "items": [
        "**trójkąt lędźwiowo-żebrowy** {{trigonum lumbocostale}} – między częścią lędźwiową a żebrową, nad XII żebrem (s. 692)",
        "**trójkąt mostkowo-żebrowy** {{trigonum sternocostale}} – między częścią mostkową a żebrową; przechodzą nim naczynia nabrzuszne górne (s. 692)",
        "oba trójkąty i rozwór przełykowy to miejsca zmniejszonego oporu – tędy mogą powstawać przepukliny przeponowe (s. 695)"]},
                 {"k": "PRZEPUKLINY PRZEPONOWE", "items": [t(LP[15]), t(LP[16])]}],
    "l3": [LP[14]]},
   {"type": "card", "title": "Położenie i sąsiedztwo", "pg": "693–695", "figs": ["przepona_czolowy"],
    "sections": [{"k": "KOPUŁY – POŁOŻENIE", "items": [t(LP[12]), t(LP[13])]},
                 {"k": "OD GÓRY", "items": [t(LP[9])]},
                 {"k": "OD DOŁU", "items": [t(LP[10])]}]},
   {"type": "card", "title": "Czynność", "pg": "693–694", "figs": ["przepona_boczny"],
    "sections": [{"k": "CZYNNOŚĆ", "items": P['f']},
                 {"k": "WDECH SPOKOJNY I GŁĘBOKI", "items": [t(LP[8])]}],
    "l3": [LP[7], {"k": "!", "t": "Zachyłek żebrowo-przeponowy przy wdechu: s. 693 – „rozchyla się”; streszczenie (s. 701) – „staje się wtedy płytszy”.", "pg": "693, 701", "src": "2655-2656, 3151-3152"}]},
   # karta „Unerwienie, rozwój i odmiany” usunięta (użytkownik: bez unerwień i odmian)
  ]},
 {"type": "group", "title": "Mechanika oddychania", "pg": "696–698",
  "why": "przepona, mięśnie klatki i brzucha razem zmieniają objętość klatki piersiowej", "q": "jak to działa?",
  "children": [
   {"type": "card", "title": "Wdech i wydech", "pg": "696–697", "figs": ["oddychanie_wymiary"],
    "sections": [
     {"k": "WDECH", "items": ["klatka piersiowa powiększa się we wszystkich trzech kierunkach: przepona napina się i obniża, powłoki brzucha się rozluźniają, żebra się unoszą, kręgosłup się prostuje (s. 696)",
                              t(OD[1])]},
     {"k": "WYDECH", "items": ["mięśnie brzucha się napinają, przepona się rozluźnia, żebra czynnie się opuszczają, kręgosłup się zgina (s. 696)",
                               "siła sprężysta klatki piersiowej działa tylko do położenia równowagi – dalej żebra opuszczają mięśnie wydechowe (s. 697)"]},
     {"k": "LICZBY", "items": [t(OD[0])]}],
    "l3": [OD[2]]},
   {"type": "card", "title": "Typy oddechowe", "pg": "696–697", "figs": ["typy_oddechowe"],
    "sections": [
     {"k": "TYP ŻEBROWY (PIERSIOWY)", "items": ["poruszają się żebra; przy spokojnym oddychaniu żebrowym unoszą je mm. międzyżebrowe zewnętrzne (s. 696–697)",
                                               "**oddychanie żebrowe dolne** – mechanizm żebrowo-przeponowy: dolne żebra wraz z przeponą tworzą jeden układ czynnościowy (s. 697)",
                                               "**oddychanie żebrowe górne** – mechanizm żebrowo-mostkowy: górne żebra wraz z mostkiem (s. 697)", t(OD[4])]},
     {"k": "TYP BRZUSZNY (PRZEPONOWY)", "items": ["bez bezpośredniego udziału żeber; ruch przepony widać na przedniej ścianie brzucha (s. 697)", t(OD[5])]},
     {"k": "KIEDY KTÓRY", "items": ["spokojne oddychanie: zwykle czysty typ brzuszny; wzmożone: typ mieszany, żebrowo-przeponowy (s. 697)"]}],
    "l3": [OD[13]]},
   {"type": "card", "title": "Mięśnie oddechowe", "pg": "693, 697", "figs": ["miesnie_oddechowe"],
    "sections": [
     {"k": "MIĘŚNIE WDECHOWE", "items": ["przepona (s. 693)", "mm. międzyżebrowe zewnętrzne – podnoszą żebra przy spokojnym oddychaniu żebrowym (s. 697)"]},
     {"k": "MIĘŚNIE WDECHOWE – POMOCNICZE (s. 697)", "items": ["mm. pochyłe – przedłużenie mm. międzyżebrowych zewnętrznych",
        "m. mostkowo-obojczykowo-sutkowy – gdy głowa i kręgosłup są ustalone",
        "m. zębaty przedni, mm. piersiowe większy i mniejszy, m. najszerszy grzbietu (wiązki żebrowe), m. podobojczykowy – gdy ramię jest ustalone, np. chwyt brzegu stołu",
        "m. zębaty tylny górny"]},
     {"k": "MIĘŚNIE WYDECHOWE", "items": ["w spokojnym oddychaniu: mm. międzyżebrowe wewnętrzne i m. poprzeczny klatki piersiowej (s. 697)",
        "pomocnicze: mięśnie brzucha – najsilniej opuszczają żebra; czynne przy kaszlu i śpiewie (s. 697)",
        "m. najszerszy grzbietu – „mięsień kaszlu”: jego części boczne kurczą się przy utrudnionym wydechu, gdy ramiona są ustalone (s. 697)"]},
     {"k": "KIEDY POMOCNICZE", "items": [t(OD[3])]}]},
   {"type": "card", "title": "Przepona i mięśnie brzucha", "pg": "697",
    "sections": [{"k": "ANTAGONIŚCI", "items": ["przepona i mięśnie brzucha działają antagonistycznie (s. 697)",
        "wdech: przepona obniża się, trzewia przesuwają się ku przedniej ścianie brzucha, powłoki się rozluźniają (s. 696–697)",
        "wydech: mięśnie brzucha napinają się i przesuwają trzewia ku górze, przepona rozluźnia się i wpukla do klatki (s. 696–697)",
        "przy ustalonej miednicy i klatce piersiowej przepona, mięśnie dna miednicy i mięśnie powłok brzucha kurczą się razem – tłocznia brzuszna, patrz karta poniżej (s. 716)"]}]},
   {"type": "card", "title": "Tłocznia brzuszna", "lat": "prelum abdominis", "pg": "716", "figs": ["przepona_brzuch"],
    "sections": [
     {"k": "WARUNEK", "items": ["miednica i klatka piersiowa są ustalone (s. 716)"]},
     {"k": "MECHANIZM", "items": ["kurczą się razem: **przepona**, **mięśnie dna miednicy** i **mięśnie powłok brzucha** (s. 716)",
                                  "objętość jamy brzusznej maleje, ciśnienie w niej wzrasta (s. 716)"]},
     {"k": "UDZIAŁ MIĘŚNI", "items": ["największy udział ma **m. poprzeczny brzucha** – dzięki poprzecznemu kierunkowi włókien – przy współudziale pozostałych mięśni brzucha (s. 716)",
                                      "przepona jest znacznie słabsza od mięśni powłok brzusznych (s. 716)"]},
     {"k": "ZAMKNIĘTA SZPARA GŁOŚNI", "items": ["tłocznia jest w pełni wyzyskana dopiero wtedy, gdy powietrze oddechowe zostaje zatrzymane w płucach przez zamknięcie szpary głośni (s. 716)",
                                                "płuca podpierają wtedy przeponę jak poduszki wypełnione powietrzem i nie dają jej uwypuklić się w obręb klatki piersiowej (s. 716)"]},
     {"k": "DZIAŁANIE", "items": ["działa na zawartość narządów jamy brzusznej i miednicy – pomaga przy oddawaniu stolca, wydalaniu moczu i podczas porodu (s. 716)",
                                 "szczególnie skuteczna, gdy klatka piersiowa i miednica zbliżają się do siebie (s. 716)"]}],
    "l3": [{"k": "!", "t": "Streszczenie (s. 701): „wydech powoduje tłocznia brzuszna, która wypycha przeponę ku klatce piersiowej”. Opis (s. 716): gdy szpara głośni jest zamknięta, płuca podpierają przeponę i nie dają jej uwypuklić się w obręb klatki piersiowej.", "pg": "701, 716", "src": "3152-3153, 4019-4022"}]},
   {"type": "card", "title": "Od czego zależy oddychanie", "pg": "697–698",
    "sections": [{"k": it['k'], "items": [t(it)]} for it in (OD[6], OD[7], OD[8], OD[9], OD[10], OD[11], OD[12])]},
  ]},
]
STAR_TITLES = {'Części i przyczepy', 'Otwory', 'Trójkąty i przepukliny', 'Położenie i sąsiedztwo', 'Czynność', 'Wdech i wydech',
               'Mięśnie oddechowe', 'Tłocznia brzuszna'}      # ★ tematy wskazane jako ważne na zaliczeniu
def _star(ns):
    for n in ns:
        if n.get('type') == 'card' and n.get('title') in STAR_TITLES:
            n['star'] = True
        _star(n.get('children', []))
_star(tree)
json.dump({"chapter": "oddychanie", "tree": tree}, open('/home/user/first-thing/plakat/k_oddychanie.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', sum(1 for _ in tree[0]['children']), sum(1 for _ in tree[1]['children']))
