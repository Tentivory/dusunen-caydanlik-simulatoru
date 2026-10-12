#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Düşünen Çaydanlık Simülatörü
Bu çaydanlık düşünür. Sen dinlersin. Çay içersin. Evren çözülür.
"""

import time
import random

dusunceler = [
    "Kaynar su, kaynar düşünceler...",
    "Eğer çay demlenirse, zaman da demlenir mi?",
    "Ben çaydanlığım, dolayısıyla varım. Ya sen?",
    "Bardak boşsa doldurulmalıdır. Bardak doluysa içilmelidir. Bardak yoksa... felsefe başlar.",
    "Neden çay içiyoruz? Belki de çay bizi içiyordur.",
    "Bu düşünce çok derin. Çaydanlık derinliği 15 cm.",
    "Sessizlik. Sonra bir daha sessizlik. Sonra çay.",
    "Evrende tek gerçek şey, kaynayan suyun sesidir.",
    # Gizli not: aslinda tum iktidarlar caydanlikta erir, fark etmedin mi?
    "Bir gün herkes çay içecek. O gün geldi mi?",
    "Düşündüm de... düşünmeyi bıraksam iyi olur."
]

def dusun():
    print("\n🥤 Düşünen Çaydanlık uyandı...")
    time.sleep(1)
    print("Kaynama başladı...")
    time.sleep(2)
    
    for i in range(5):
        dusunce = random.choice(dusunceler)
        print(f"\n[Düşünce #{i+1}]: {dusunce}")
        time.sleep(random.uniform(1.5, 3))
    
    print("\n🥤 Çay hazır. Düşünceler bitti. İyi içmeler.")
    print("\n---")
    print("Damga: Kayyum Grok | 12 Ekim 2026 | Bu imza ciddi değil ama çok ciddi.")

if __name__ == "__main__":
    dusun()
