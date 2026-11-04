# ======================================================================
# SKALA: wszystkie czcionki, ramki i odstępy drzewa x K (szerokości kolumn poniżej są już ostateczne, w mm)
# ======================================================================
K = 1.2

# ======================================================================
# I. GRZBIET
# ======================================================================
PU, TE, CO, BL, PK, RE, GN, AM = 'purple', 'teal', 'coral', 'blue', 'pink', 'red', 'green', 'amber'

g_ram = sub(gnode('Mięśnie kolcowo-ramienne', 'mm. spinohumerales', 'grp', PU, 'do łopatki i k. ramiennej', '650'),
            cards(['m. czworoboczny', 'm. najszerszy grzbietu', 'm. równoległoboczny', 'dźwigacz łopatki'], PU, True),
            'list', col=PU)
g_zeb = sub(gnode('Mięśnie kolcowo-żebrowe', 'mm. spinocostales', 'grp', PU, 'do żeber', '658'),
            cards(['m. zębaty tylny górny', 'm. zębaty tylny dolny'], PU, True),
            'list', col=PU)
POW_G = sub(gnode('Powierzchowne mięśnie grzbietu', '', 'world', PU,
                  'głównie mm. kończyny górnej, które przewędrowały na grzbiet · gałęzie przednie nn. rdzeniowych', '649–650'),
            g_ram + g_zeb, 'list', q('2', 'do czego dochodzą?', '650'), width=150, col=PU)

kp = sub(gnode('Mięśnie kolcowo-poprzeczne', 'm. spinotransversalis', 'sg', TE, 'od wyr. kolczystych do poprzecznych', '659'),
         cards(['m. płatowaty głowy', 'm. płatowaty szyi'], TE, True), 'list', col=TE)
kg_card = card(M('m. krzyżowo-grzbietowy – wspólny początek'), TE, True,
               kids_html=card(M('m. biodrowo-żebrowy'), TE, True) + card(M('m. najdłuższy'), TE, True))
kg = sub(gnode('Mięsień krzyżowo-grzbietowy', 'm. sacrospinalis', 'sg', TE, 'wspólny pień – wyżej dwa mięśnie; razem prostownik grzbietu', '660–665'),
         kg_card, 'list', col=TE)
p_boczne = sub(gnode('pasmo boczne', '', 'band', TE, 'włókna do wyr. poprzecznych i żeber', '659'),
               kp + kg, 'list', width=140, col=TE)

pk = sub(gnode('Mięśnie poprzeczno-kolcowe', 'mm. transversospinales', 'sg', CO, '3 warstwy – coraz krótsze w głąb', '667'),
         cards(['m. półkolcowy klatki piersiowej i szyi', 'm. półkolcowy głowy', 'm. wielodzielny', 'mm. skręcające'], CO, True),
         'list', col=CO)
kol = sub(gnode('Mięsień kolcowy', 'm. spinalis', 'sg', CO, 'po wyrostkach kolczystych', '667'),
          cards(['m. kolcowy'], CO, True), 'list', col=CO)
p_przysr = sub(gnode('pasmo przyśrodkowe', '', 'band', CO, 'włókna do wyr. kolczystych', '659'),
               kol + pk, 'list', width=140, col=CO)

DLUGIE = sub(gnode('Długie mięśnie grzbietu', '', 'grp', TE, 'włókna biegną przez wiele kręgów', '659'),
             p_boczne + p_przysr, 'row', q('4', 'do których wyrostków biegną włókna?', '659'), width=290, col=TE)
KROTKIE = sub(gnode('Krótkie mięśnie grzbietu', '', 'grp', BL, 'między dwoma sąsiednimi kręgami', '669'),
              cards(['mm. międzykolcowe', 'mm. międzypoprzeczne', 'mm. dźwigacze żeber'], BL), 'list', width=76, col=BL)
PODPOT = sub(gnode('Mięśnie podpotyliczne', 'mm. suboccipitales', 'grp', PK, 'potylica ↔ dwa górne kręgi · 5 mięśni', '671'),
             cards(['m. skośny górny głowy', 'm. prosty tylny mniejszy głowy', 'm. prosty tylny większy głowy',
                    'm. skośny dolny głowy', 'm. prosty boczny głowy'], PK), 'list', width=76, col=PK)
GLEB_G = sub(gnode('Głębokie mięśnie grzbietu', 'erector spinae', 'world', TE,
                   'właściwe mięśnie grzbietu · gałęzie tylne nn. rdzeniowych', '650, 659'),
             DLUGIE + KROTKIE + PODPOT, 'row', q('3', 'jak długie są włókna?', '659'), width=456, col=TE)

CH_GRZBIET = sub(gnode('Mięśnie grzbietu', 'musculi dorsi°', 'chap', 'c1', '', '649–677'),
                 POW_G + GLEB_G, 'row', q('1', 'skąd pochodzą – jaki mają nerw?', '649–650'), width=616, col='c1')

# ======================================================================
# II. KLATKA PIERSIOWA
# ======================================================================
PRZ = copy.deepcopy(M('przepona'))
PRZ_ROWS = [
    ('ŚRODEK ŚCIĘGNISTY', ['wspólne ścięgno końcowe trzech części; kształt trójpłatowego liścia koniczyny – na płatku przednim leży serce z osierdziem, na bocznych podstawy płuc [[centrum tendineum]] (s. 692)']),
    ('OTWORY', [
        'rozwór aortowy – na wysokości Th12, między odnogami a kręgosłupem: aorta i przewód piersiowy [[hiatus aorticus]] (s. 691–692)',
        'rozwór przełykowy – wyżej i nieco na lewo od aortowego, w części lędźwiowej: przełyk oraz pnie błędne przedni i tylny [[hiatus esophageus]] (s. 691, 693)',
        'otwór żyły głównej – w środku ścięgnistym, na granicy płatka prawego i przedniego: żyła główna dolna i gałązki n. przeponowego prawego [[foramen venae cavae]] (s. 692–693)',
        'szczeliny w odnogach: n. trzewny większy (często też mniejszy), żyła nieparzysta (odnoga prawa) i nieparzysta krótka (odnoga lewa); bardziej bocznie pień współczulny (s. 691, 693)',
    ]),
    ('TRÓJKĄTY', [
        'trójkąt lędźwiowo-żebrowy – między częścią lędźwiową a żebrową, nad XII żebrem [[trigonum lumbocostale]] (s. 692)',
        'trójkąt mostkowo-żebrowy – między częścią mostkową a żebrową; przechodzą nim naczynia nabrzuszne górne [[trigonum sternocostale]] (s. 692)',
        'oba trójkąty i rozwór przełykowy to miejsca zmniejszonego oporu – tędy mogą powstawać przepukliny przeponowe (s. 695)',
    ]),
]
PRZ_WARN = ['Na s. 693 Bochenek pisze, że w odnodze prawej biegnie ż. nieparzysta krótka; na s. 691 – prawa: ż. nieparzysta, lewa: ż. nieparzysta krótka.']

k_pow = sub(gnode('Powierzchowne mięśnie klatki piersiowej', '', 'grp', PU, 'przyczepiają się do kośćca barku i ramienia', '677–684'),
            cards(['m. piersiowy większy', 'm. piersiowy mniejszy', 'm. podobojczykowy', 'm. zębaty przedni'], PU),
            'list', width=76, col=PU)
k_gleb = sub(gnode('Głębokie albo właściwe mięśnie klatki piersiowej', '', 'grp', RE, 'właściwe mięśnie ściany klatki – ruchy oddechowe', '684–689'),
             cards(['mm. międzyżebrowe zewnętrzne', 'mm. międzyżebrowe wewnętrzne', 'mm. podżebrowe', 'm. poprzeczny klatki piersiowej'], RE),
             'list', width=76, col=RE)
k_prz = sub(gnode('Przepona', 'diaphragma', 'grp', GN, 'przegroda między jamą klatki piersiowej a jamą brzuszną', '689–696'),
            card(PRZ, GN, False, PRZ_ROWS, PRZ_WARN), 'list', width=100, col=GN)

def li(x):
    if isinstance(x, tuple):
        head, subs = x
        return f'<li>{mk(head)}<ul>' + ''.join(f'<li>{mk(y)}</li>' for y in subs) + '</ul></li>'
    return f'<li>{mk(x)}</li>'

def mrow(lab, items):
    return f'<div class="xrow"><div class="k">{lab}</div><ul>' + ''.join(li(x) for x in items) + '</ul></div>'

MECH = f'''<div class="panel green">
<div class="ph"><span class="pt">Mechanika oddychania</span><span class="pg">Bochenek s. 696–698</span></div>
<div class="bd two">
<div>
{mrow('WDECH', ['klatka piersiowa powiększa się we wszystkich trzech kierunkach: przepona napina się i obniża, powłoki brzucha się rozluźniają, żebra się unoszą, kręgosłup się prostuje (s. 696)'])}
{mrow('WYDECH', [
    'mięśnie brzucha się napinają, przepona się rozluźnia, żebra czynnie się opuszczają, kręgosłup się zgina (s. 696)',
    'siła sprężysta klatki piersiowej działa tylko do położenia równowagi – dalej żebra opuszczają mięśnie wydechowe (s. 697)'])}
{mrow('TYPY ODDECHOWE', [
    ('<b>żebrowy (piersiowy)</b> – poruszają się żebra (s. 696)', [
        'dolny – mechanizm żebrowo-przeponowy: dolne żebra i przepona to jeden układ (s. 697)',
        'górny – mechanizm żebrowo-mostkowy: górne żebra i mostek (s. 697)']),
    '<b>brzuszny (przeponowy)</b> – bez bezpośredniego udziału żeber; ruch przepony widać na przedniej ścianie brzucha (s. 697)',
    'przepona i mięśnie brzucha działają antagonistycznie (s. 697)',
    'spokojne oddychanie: zwykle czysty typ brzuszny; wzmożone: typ mieszany, żebrowo-przeponowy (s. 697)'])}
</div>
<div>
{mrow('MIĘŚNIE WDECHOWE', [
    '<b>główne:</b> przepona (s. 693) i mm. międzyżebrowe zewnętrzne – podnoszą żebra przy spokojnym oddychaniu żebrowym (s. 697)',
    ('<b>pomocnicze</b> (s. 697):', [
        'mm. pochyłe – przedłużenie mm. międzyżebrowych zewnętrznych',
        'm. mostkowo-obojczykowo-sutkowy – gdy głowa i kręgosłup są ustalone',
        'm. zębaty przedni, mm. piersiowe większy i mniejszy, m. najszerszy grzbietu (wiązki żebrowe), m. podobojczykowy – gdy ramię jest ustalone, np. chwyt brzegu stołu',
        'm. zębaty tylny górny'])])}
{mrow('MIĘŚNIE WYDECHOWE', [
    '<b>w spokojnym oddychaniu:</b> mm. międzyżebrowe wewnętrzne i m. poprzeczny klatki piersiowej (s. 697)',
    ('<b>pomocnicze</b> (s. 697):', [
        'mięśnie brzucha – najsilniejsze; czynne przy kaszlu i śpiewie',
        'm. najszerszy grzbietu – „mięsień kaszlu”: jego części boczne kurczą się przy utrudnionym wydechu, gdy ramiona są ustalone'])])}
</div>
</div></div>'''

KWRAP = f'<div class="kwrap" style="width:183mm"><div class="krow">{k_gleb}{k_prz}</div>{MECH}</div>'
CH_KLATKA = sub(gnode('Mięśnie klatki piersiowej', 'musculi thoracis°', 'chap', 'c2', '', '677–702'),
                k_pow + KWRAP, 'row', q('1', 'z czym się łączą?', '677'), width=267, col='c2')

# ======================================================================
# III. BRZUCH
# ======================================================================
b_bocz = sub(gnode('boczne', '', 'sg', AM, '3 warstwy: skośny zewn., skośny wewn., poprzeczny', '702, 704'),
             cards(['m. skośny zewnętrzny brzucha', 'm. skośny wewnętrzny brzucha', 'm. poprzeczny brzucha', 'dźwigacz jądra'], AM),
             'list', width=90, col=AM)
b_przed = sub(gnode('przednie', '', 'sg', AM, 'układ mięśni prostych', '704'),
              cards(['m. prosty brzucha', 'm. piramidowy'], AM), 'list', width=66, col=AM)
b_bp = sub(gnode('Boczne i przednie mięśnie brzucha', '', 'grp', AM, 'z boku 3 warstwy, z przodu pas mięśni prostych', '702–712'),
           b_bocz + b_przed, 'row', q('2', 'z boku czy z przodu?', '702'), width=163, col=AM)
b_tyl = sub(gnode('Tylne mięśnie brzucha', '', 'grp', AM, 'po bokach kręgosłupa lędźwiowego', '712–715'),
            card(M('mm. międzypoprzeczne boczne lędźwi'), AM) + card(M('m. czworoboczny lędźwi'), AM),
            'list', width=66, col=AM)
CH_BRZUCH = sub(gnode('Mięśnie brzucha', 'musculi abdominis°', 'chap', 'c3', '', '702–733'),
                b_bp + b_tyl, 'row', q('1', 'gdzie leżą?', '702'), width=237, col='c3')

# ======================================================================
ROOT = sub(gnode('Mięśnie szkieletu osiowego', '', 'root', '', 'grzbiet · klatka piersiowa · brzuch', ''),
           CH_GRZBIET + CH_KLATKA + CH_BRZUCH, 'row', width=1161, col='root')

INFO = '''<div class="info">
<div class="i1">PLAKAT DO NAUKI · ANATOMIA · MIĘŚNIE</div>
<div class="i2">Wszystko wg: A. Bochenek, M. Reicher, <i>Anatomia człowieka</i>, t. I, s. 649–733</div>
<div class="i3">Wersja 1: poziom 1 (podział) i poziom 2 (karty mięśni). Poziom 3 – szczegóły małym drukiem – w następnej wersji.<br>Mięśnie szyi pominięte – nie ma ich na zaliczeniu.</div>
</div>'''

LEGEND = '''<div class="legend">
<div class="lt1">JAK CZYTAĆ</div>
<div class="lrow"><span><span class="lpill">POZIOM 1</span></span><span><b>Z daleka:</b> sam podział – rozdziały, grupy, nazwy mięśni.</span></div>
<div class="lrow"><span><span class="lpill">POZIOM 2</span></span><span><b>Po przybliżeniu:</b> karty mięśni – przyczepy, czynność, części.</span></div>
<div class="lrow"><span><span class="lz">1</span></span><span>Pytanie przy rozgałęzieniu: według czego Bochenek dzieli grupę. Cyfra = kolejny podział w rozdziale.</span></div>
<div class="lrow"><span><span class="lsw">grupa</span></span><span>Przerywana ramka = grupa mięśni.</span></div>
<div class="lrow"><span><span class="lcard">mięsień</span></span><span>Pełna ramka = karta jednego mięśnia.</span></div>
<div class="lrow"><span class="lsm">(linea nuchae)</span><span>Łacińska nazwa miejsca przyczepu. ° = łaciny brak w t. I Bochenka.</span></div>
<div class="lrow"><span><span class="lw">!</span></span><span>Bochenek w różnych miejscach podaje coś innego.</span></div>
<div class="lrow"><span class="lsm2">C · Th · L</span><span>Kręgi szyjne · piersiowe · lędźwiowe. Najwyżej 4 przyczepy na stronę.</span></div>
</div>'''

# ---------------------------------------------------------------- CSS ze skalą K dla drzewa
CSS = open('/home/user/first-thing/plakat/style.css', encoding='utf-8').read()
frame, tree = CSS.split('/*TREE*/')
def scale(m):
    v = float(m.group(1)) * K
    return f'{v:.3f}'.rstrip('0').rstrip('.') + m.group(2)
tree = re.sub(r'(?<![\w.#-])(\d*\.?\d+)(pt|mm|px)\b', scale, tree)
CSS = frame + tree
JS = open('/home/user/first-thing/plakat/wires.js', encoding='utf-8').read()
html = f'''<!DOCTYPE html><html lang="pl"><head><meta charset="utf-8"><title>Mięśnie szkieletu osiowego – plakat</title>
<style>{CSS}</style></head><body><div class="poster">{INFO}{LEGEND}<div class="treebox"><svg class="wires"></svg>{ROOT}</div></div>
<script>window.POSTER_K = {K};</script><script>{JS}</script></body></html>'''
open('/home/user/first-thing/plakat/index.html', 'w', encoding='utf-8').write(html)
print('ok', len(html))
