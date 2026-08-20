# -*- coding: utf-8 -*-
"""
test_fix_rendering.py
"""
import re

def clean_and_format_math_html(text):
    if not text:
        return ""
    
    # 1. Protect math formulas
    math_blocks = []
    def save_math(m):
        idx = len(math_blocks)
        math_blocks.append(m.group(0))
        return f"___MATH_BLOCK_{idx}___"
    
    # Match $$...$$, \[...\], $...$, \(...\)
    text = re.sub(r'(\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]|\$(?:\\\$|[^\$])+\$|\\\([\s\S]+?\\\))', save_math, text)
    
    # 2. Escape HTML characters in non-math text
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    
    # 3. Restore math blocks (math inside $...$ will be processed by KaTeX directly)
    for i, mb in enumerate(math_blocks):
        text = text.replace(f"___MATH_BLOCK_{i}___", mb)
        
    return text

sample_q775 = "দৃশ্যকল্প-২ এর সমীকরণটি $0<x<\\pi$ ব্যবধিতে সমাধান কর ।"
sample_q779 = "খ. $a=\\sqrt{3}$ এবং $b = 1$ হলে দৃশ্যকল্প-১ এর সমীকরণটি সমাধান কর, যেখানে $-2 \\pi<x<2 \\pi .$\nগ.  দৃশ্যকল্প-২ এর আলোকে $f(x)+f(3 x)+f(5 x)+f(7 x)=0$ সমীকরণটি সমাধান কর, যেখানে $0<x<\\pi$"
sample_q787 = "খ.  সমাধান কর  $\\sqrt{2} f(x)-\\sqrt{2} f\\left(\\frac{\\pi}{2}-x\\right)=1$ যখন $-\\pi<x<\\pi .$\nগ. দেখাও যে, $A+B=\\frac{\\pi}{2}$ সমীকরণটি একটি উপবৃত্ত নির্দেশ করে ।"

print("Q775 formatted:", clean_and_format_math_html(sample_q775))
print("---")
print("Q779 formatted:", clean_and_format_math_html(sample_q779))
print("---")
print("Q787 formatted:", clean_and_format_math_html(sample_q787))
