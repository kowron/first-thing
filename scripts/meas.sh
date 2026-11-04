#!/bin/bash
# użycie: meas.sh PAGE K FIGSCALE  → measure_PAGE_K_FS.json
cd /home/user/first-thing/plakat
K=$2 FIGSCALE=$3 PAGE=$1 MEASURE=1 python3 build_os.py >/dev/null && python3 /home/user/first-thing/scripts/measure.py $1 /home/user/first-thing/plakat/measure_$1_$(python3 -c "print('%g'%$2)")_$(python3 -c "print('%g'%$3)").json | tail -n +1 > /tmp/meas_$1.txt; echo done $(ls /home/user/first-thing/plakat/measure_$1_*.json)
