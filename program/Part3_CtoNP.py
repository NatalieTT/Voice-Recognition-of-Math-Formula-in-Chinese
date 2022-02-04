# -*- coding: utf-8 -*-

"""

User: Kevin DENG
Lang: Python
Scho: UIC
Proj: FYP_Part3 Convert Chinese text into Ordinary Numbers and Pinyin 
Date: 2020.05.12-2020.11.08
    
"""
import cn2an
import os
from pypinyin import lazy_pinyin


def CtoNP():
    num_unit = {'零', '一', '二', '两', '俩', '三', '四', '五', '六', '七', '八', '九', '十', '百', '千', '万', '亿', '平'}
    num_u = {'百', '千', '万', '亿'}
    ope_unit = {'加', '减', '乘', '除', '等'}
    dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dir);
    fin = open("Chinese.txt", "r", encoding = 'utf-8')
    text = fin.read()
    text = "~" + text + "~"
    fin.close()

    i = 1
    ans = ""
    anq = "" 
    fen = 0

    while i < len(text):
        s = ""
        if text[i] in num_unit:
            j = i
            while j < len(text) and text[j] in num_unit:
                if text[j] == '两' or text[j] == '俩' or (text[j] == '平' and text[j + 1] == '方'):
                    s = s + '二'
                elif (text[j] in num_u and text[j] != text[j-1]) or (not(text[j] in num_u)): 
                    s = s + text[j]
                j = j + 1
            if (text[j] != "~" and text[j] != "." and text[j] != "点"):
                ans = ans + str(cn2an.cn2an(s, "strict")) + " "
            else:
                ans = ans + str(cn2an.cn2an(s, "strict"))
            i = j - 1
        elif (text[i] >= 'a' and text[i] <= 'z' and not ((text[i + 1] >= 'a' and text[i + 1] <= 'z') or (text[i + 1] >= 'A' and text[i + 1] <= 'Z')) and not ((text[i - 1] >= 'a' and text[i - 1] <= 'z') or (text[i - 1] >= 'A' and text[i - 1] <= 'Z'))):
            s = s + text[i].upper()
            if ((text[i + 1] >= 'a' and text[i + 1] <= 'z') or (text[i + 1] >= 'A' and text[i + 1] <= 'Z') or (text[i + 1] == '~')):
                ans = ans + s
            else:
                ans = ans + s + " "
        elif (text[i] >= 'A' and text[i] <= 'Z' and not ((text[i + 1] >= 'a' and text[i + 1] <= 'z') or (text[i + 1] >= 'A' and text[i + 1] <= 'Z')) and not ((text[i - 1] >= 'a' and text[i - 1] <= 'z') or (text[i - 1] >= 'A' and text[i - 1] <= 'Z'))):
            s = s + text[i]
            if ((text[i + 1] >= 'a' and text[i + 1] <= 'z') or (text[i + 1] >= 'A' and text[i + 1] <= 'Z') or (text[i + 1] == '~')):
                ans = ans + s
            else: 
                ans = ans + s + " "
        elif (text[i] >= 'A' and text[i] <= 'Z'):
            s = s + text[i].lower()
            if (not((text[i + 1] >= 'a' and text[i + 1] <= 'z') or (text[i + 1] >= 'A' and text[i + 1] <= 'Z') or (text[i + 1] == '~') or (text[i + 1] == ' '))):
                ans = ans + s + " "
            else:
                ans = ans + s
        elif (text[i] >= 'a' and text[i] <= 'z'):
            s = s + text[i].lower()
            if (not((text[i + 1] >= 'a' and text[i + 1] <= 'z') or (text[i + 1] >= 'A' and text[i + 1] <= 'Z') or (text[i + 1] == '~') or (text[i + 1] == ' '))):
                ans = ans + s + " "
            else:
                ans = ans + s
        elif (text[i] >= '0' and text[i] <= '9'):
            s = s + text[i]
            if ((text[i + 1] >= '0' and text[i + 1] <= '9') or (text[i + 1] == '~') or (text[i + 1] == '.') or (text[i + 1] == '点')):
                ans = ans + s
            else:
                ans = ans + s + " "
        elif (text[i] >= u'\u4e00' and text[i] <= u'\u9fff' and text[i] != '分'):
            if (text[i] != '等'):
                p = lazy_pinyin(text[i])
            else:
                p = 'equal'
            for q in p:
                s = s + q
            if ((text[i + 1] != '~' and not (text[i + 1] >= u'\u4e00' and text[i + 1] <= u'\u9fff')) or (text[i + 1] in num_unit) or (text[i] in ope_unit)):
                ans = ans + s + " "
            else:
                ans = ans + s
        elif (text[i] == '分'):
            p = lazy_pinyin(text[i])
            for q in p:
                s = s + q
            anq = " {" + ans + "} "
            ans = s + " {"
            fen = 1
        elif (text[i] == '+' or text[i] == '-' or text[i] == '*' or text[i] == '/' or text[i] == '=' or text[i] == '.' or text[i] == '×' or text[i] == '÷'):
            if (text[i] != "." and text[i] != '×' and text[i] != '÷'):
                ans = ans + text[i] + " "
            elif (text[i] == '×'):
                ans = ans + "* "
            elif (text[i] == '÷'):
                ans = ans + " chu "
            else:
                ans = ans + "."
        i = i + 1

    if (fen == 1):
        ans = ans + "} "
        ans = ans + anq
    ans = ans + " "
    fout = open("Pinyin.txt", "w", encoding = 'utf-8')
    fout.write(ans)
    fout.close()
    
