#!/bin/bash
# Użycie: bash RESTORE.sh  (uruchom obok plakat_handoff.tar.gz; kod ma wpisane ścieżki /home/user/first-thing/...)
set -e
mkdir -p /home/user/first-thing /mnt/user-data/uploads
tar xzf plakat_handoff.tar.gz -C /home/user/first-thing          # → /home/user/first-thing/plakat, /home/user/first-thing/scripts, bones.txt, all.txt
pip install --break-system-packages playwright pypdf 2>/dev/null || pip install playwright pypdf
python3 -m playwright install chromium
echo "Gotowe. Skan Bochenka wstaw do /mnt/user-data/uploads/ (nazwa: HANDOFF.md §3). Zacznij od /home/user/first-thing/plakat/HANDOFF.md"
