#!/bin/bash
# usage: ocr.sh pdfpage
p=$1
d=/home/user/first-thing/pdf/bones
pdfimages -j -f $p -l $p /home/user/first-thing/pdf/boch.pdf $d/s$p
f=$(ls $d/s$p-*.jpg | head -1)
mv $f $d/s$p.jpg
convert $d/s$p.jpg -crop 50%x100% +repage $d/h$p-%d.png
for i in 0 1; do
  convert $d/h$p-$i.png -resize 250% -colorspace Gray -sharpen 0x1 $d/u$p-$i.png
  tesseract $d/u$p-$i.png $d/t$p-$i -l pol --psm 4 >/dev/null 2>&1
  rm $d/u$p-$i.png
done
