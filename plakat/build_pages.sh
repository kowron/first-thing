#!/bin/bash
# Buduje 6 stron plakatu i łączy je w jeden PDF (../Plakat_A0_5_szkielet_osiowy.pdf). Każda strona ma własny rozmiar:
# 1030x728 mm („A0,5”) albo 1189x841 mm (A0) – zob. linie poniżej.  Użycie: ./build_pages.sh [strona ...]  (kregoslup klatka m1 m2 polkreg klodd)
# Zmienne: L3S (skala opisów poziomu 3, domyślnie 1.6), OUT (katalog PDF-ów stron).
cd /home/user/first-thing/plakat
export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
OUT=${OUT:-/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/pages}; mkdir -p $OUT
export L3S=${L3S:-1.6}
ORDER="kregoslup klatka m1 m2 polkreg klodd"; [ $# -gt 0 ] && ORDER="$*"

measure() { python3 ../scripts/pdf_poster2.py /home/user/first-thing/plakat/$1 $OUT/$2.pdf 2>&1 | grep -E 'max_bottom|max_right|over|overlap' | tr '\n' ' '; echo "(wysokość strony $3)"; }
# os  nazwa layout dane only  szer wys K FS    – strony z build_os.py (kościec, połączenia, mechanika)
os() {
  export PAGE=$1 LAYOUT=$2 DATA=$3 ONLY=$4 PW=$5 PH=$6 K=$7 FIGSCALE=$8
  ../scripts/meas.sh $1 $7 $8 >/dev/null 2>&1
  python3 build_os.py 2>&1 | grep -E 'brak rysunków|Error|Trace' | sed 's/.*| //'
  measure page_$1.html $1 $6
}
# mus  nazwa rozdziały szer wys K   – strony z mięśniami (build.py); dodatkowe zmienne (W_*, ROOT_*, DOCKCOLS_*) ustawia wywołujący
mus() {
  PAGE=${3}x${4} K=$5 REGIONS=$2 OUT=page_$1.html python3 build.py 2>&1 | grep -E 'assert|Error|Trace'
  measure page_$1.html $1 $4
}
for pg in $ORDER; do
  echo "== $pg"
  case $pg in
    kregoslup) ( export CWS=160 CWT=104; os kregoslup kosciec kosciec kregoslup 1189 841 0.95 0.85 ) ;;
    klatka)    ( export CWS=112 CWT=270; os klatka kosciec kosciec klatka 1189 841 0.95 0.85 ) ;;
    polkreg)   ( export CWM=270; os polkreg mech mech polkreg 1189 841 0.95 0.85 ) ;;
    klodd)     ( export CWM=120 CWP=380 CWK6=240 CWO=520; os klodd mech mech klodd 1189 841 0.95 0.85 ) ;;
    m1) ( export ROOT_TITLE='Grzbiet' ROOT_SUB='mięśnie grzbietu – powierzchowne i głębokie' W_pow=300 W_band=240 W_krot=150 W_podp=150; mus m1 grzbiet 1189 841 1.1 ) ;;
    m2) ( export ROOT_TITLE='Klatka i brzuch' ROOT_SUB='mięśnie klatki piersiowej i brzucha' W_kpow=140 W_kgleb=140 W_kprz=190 W_bbocz=190 W_bprzed=220 W_btyl=220 DOCKCOLS_brzuch=2; mus m2 klatka,brzuch 1189 841 1.1 ) ;;
  esac
done
python3 - <<PY
import os
from pypdf import PdfWriter
w = PdfWriter()
for n in "kregoslup klatka m1 m2 polkreg klodd".split():
    f = "$OUT/%s.pdf" % n
    if os.path.exists(f): w.append(f)
w.add_metadata({'/Title': 'Plakat „Anatomia: szkielet osiowy” – 6 stron (wg Bochenka, t. I)'})
w.write('/home/user/first-thing/Plakat_A0_5_szkielet_osiowy.pdf')
print('PDF złożony, stron:', len(w.pages))
PY
