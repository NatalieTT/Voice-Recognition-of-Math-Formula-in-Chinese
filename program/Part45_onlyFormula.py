# -*- coding: utf-8 -*-
"""

User: Yichun TAO
Lang: Python
Scho: UIC
Proj: FYP_Part4.5 Formula txt
    
"""
import os
def onlyformula():
    dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dir);
    fin = open("Latex.txt", "r", encoding = 'utf-8')
    S = fin.read()
    fin.close()
    ans=S.replace('$', '')
    fout = open("Formula4.5.txt", "w", encoding = 'utf-8')
    fout.write(ans)
    fout.close()
