#!/bin/bash
# Buduje 6 stron plakatu (format 1030×728 mm = „A0,5”) i łączy je w jeden PDF.
# użycie: ./build_pages.sh [nazwa_strony ...]   (bez argumentów – wszystkie; PDF-y stron w $OUT, plik zbiorczy: ../Plakat_A0_5_szkielet_osiowy.pdf)
cd /home/user/first-thing/plakat
export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers
OUT=${OUT:-/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/pages}; mkdir -p $OUT
PW=1030; PH=728; LIMIT=717
ORDER="kregoslup klatka m1 m2 polkreg klodd"
[ $# -gt 0 ] && ORDER="$*"
measure() { python3 ../scripts/pdf_poster2.py /home/user/first-thing/plakat/$1 $OUT/$2.pdf 2>&1 | grep -E 'max_bottom|over|overlap' | tr '\n' ' '; echo; }
osbuild() { # nazwa layout data only K FS  (+ zmienne środowiskowe ustawione przed wywołaniem)
  export PAGE=$1 LAYOUT=$2 DATA=$3 ONLY=$4 PW=$PW PH=$PH K=$5 FIGSCALE=$6
  ../scripts/meas.sh $1 $5 $6 >/dev/null 2>&1
  python3 build_os.py 2>&1 | grep -E 'brak rysunków' | sed 's/.*| //'
  measure page_$1.html $1
}
for pg in $ORDER; do
  echo "== $pg"
  case $pg in
    kregoslup) CWS=135 CWT=104 osbuild kregoslup kosciec kosciec kregoslup 0.8 0.75 ;;
    klatka)    CWS=112 CWT=205 osbuild klatka kosciec kosciec klatka 0.85 0.78 ;;
    polkreg)   CWM=190 osbuild polkreg mech mech polkreg 0.8 0.75 ;;
    klodd)     CWM=120 CWP=300 CWK6=190 CWO=400 osbuild klodd mech mech klodd 0.8 0.75 ;;
    m1) PAGE=${PW}x${PH} K=1.0 REGIONS=grzbiet OUT=page_m1.html ROOT_TITLE='Grzbiet' ROOT_SUB='mięśnie grzbietu – powierzchowne i głębokie' \
          W_pow=240 W_band=200 W_krot=120 W_podp=120 python3 build.py 2>&1 | grep -E 'assert|Error'; measure page_m1.html m1 ;;
    m2) PAGE=${PW}x${PH} K=1.0 REGIONS=klatka,brzuch OUT=page_m2.html ROOT_TITLE='Klatka i brzuch' ROOT_SUB='mięśnie klatki piersiowej i brzucha' \
          W_kpow=120 W_kgleb=120 W_kprz=160 W_bbocz=160 W_bprzed=190 W_btyl=190 DOCKCOLS_brzuch=2 python3 build.py 2>&1 | grep -E 'assert|Error'; measure page_m2.html m2 ;;
  esac
done
# złożenie PDF (kolejność: kości, mięśnie, połączenia i mechanika)
python3 - <<PY
import os
from pypdf import PdfWriter
w = PdfWriter()
for n in "kregoslup klatka m1 m2 polkreg klodd".split():
    f = "$OUT/%s.pdf" % n
    if os.path.exists(f): w.append(f)
w.add_metadata({'/Title': 'Plakat „Anatomia: szkielet osiowy” – 6 stron 1030×728 mm (wg Bochenka, t. I)'})
w.write('/home/user/first-thing/Plakat_A0_5_szkielet_osiowy.pdf')
print('PDF złożony, stron:', len(w.pages))
PY
