#!/bin/bash
# OCR z ramkami (TSV) dla rozdziału o mięśniach (PDF 315–368) – do wykrycia drobnego druku
SRC="/tmp/claude-0/-home-user-first-thing/d41721b4-1413-50bf-8c94-691fa5e52b07/scratchpad/skan.pdf"
OUT=/home/user/first-thing/druk
one() {
  n=$1
  [ -s "$OUT/p$n.tsv" ] && return
  pdftoppm -r 200 -gray -f $n -l $n -png "$SRC" "$OUT/img$n" 2>/dev/null
  f=$(ls $OUT/img$n*.png | head -1)
  tesseract "$f" "$OUT/p$n" -l pol --psm 1 tsv >/dev/null 2>&1
  rm -f "$f"
}
export -f one; export SRC OUT
seq 315 368 | xargs -P 4 -I{} bash -c 'one {}'
echo DONE > $OUT/done.txt
