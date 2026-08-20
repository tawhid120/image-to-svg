# -*- coding: utf-8 -*-
"""
fix_q786.py
===========
Fixes Question 786:
- Reconstructs the proper Creative Question Stem & Sub-questions (ক, খ, গ) in the question body.
- Moves the full step-by-step mathematical proof and explanation into the explanation field.
- Updates processed_questions.json and raw JSON.
- Rebuilds question_bank_viewer.html.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# Reconstructed Question 786 Stem & Questions
# ─────────────────────────────────────────────────────────────────────────────
q786_question_text = (
    "দৃশ্যকল্প: $f(x)=\\operatorname{cosec} x-\\cot x$ এবং $g(x)=\\sin x$\n\n"
    "ক. প্রমাণ কর যে, $\\operatorname{cosec} \\left( \\sin^{-1} \\left( \\tan \\left( \\sec^{-1} \\frac{x}{y} \\right) \\right) \\right) = \\frac{y}{\\sqrt{x^2-y^2}}$\n\n"
    "খ. $f(\\theta)=\\frac{3}{4}$ হলে প্রমাণ কর যে, $\\theta=\\sin^{-1} \\frac{24}{25}$\n\n"
    "গ. $g(5\\theta)-\\sqrt{3}\\,g(\\theta)=g(3\\theta)$ সমীকরণটির সমাধান নির্ণয় কর।"
)

q786_answer_text = (
    "ক. বামপক্ষ $= \\operatorname{cosec}\\left\\{\\sin^{-1}\\left(\\tan\\left(\\sec^{-1}\\dfrac{x}{y}\\right)\\right)\\right\\}$\n"
    "ধরি, $\\sec^{-1}\\dfrac{x}{y} = \\alpha \\implies \\sec\\alpha = \\dfrac{x}{y}$\n"
    "সমকোণী ত্রিভুজ থেকে, $\\tan\\alpha = \\dfrac{\\sqrt{x^2-y^2}}{y}$\n"
    "$= \\operatorname{cosec}\\left\\{\\sin^{-1}\\left(\\tan\\left(\\tan^{-1}\\dfrac{\\sqrt{x^2-y^2}}{y}\\right)\\right)\\right\\}$\n"
    "$= \\operatorname{cosec}\\left\\{\\sin^{-1}\\left(\\dfrac{\\sqrt{x^2-y^2}}{y}\\right)\\right\\}$\n"
    "$= \\operatorname{cosec}\\left\\{\\operatorname{cosec}^{-1}\\left(\\dfrac{y}{\\sqrt{x^2-y^2}}\\right)\\right\\}$\n"
    "$= \\dfrac{y}{\\sqrt{x^2-y^2}} =$ ডানপক্ষ [প্রমাণিত]\n\n"
    "খ. দেওয়া আছে, $f(x)=\\operatorname{cosec} x-\\cot x$ এবং $f(\\theta)=\\dfrac{3}{4}$\n"
    "$\\therefore \\operatorname{cosec}\\theta-\\cot\\theta=\\dfrac{3}{4} \\implies \\dfrac{1-\\cos\\theta}{\\sin\\theta}=\\dfrac{3}{4}$\n"
    "$\\implies 4 - 4\\cos\\theta = 3\\sin\\theta \\implies 3\\sin\\theta - 4 = -4\\cos\\theta$\n"
    "উভয়পক্ষকে বর্গ করে পাই:\n"
    "$(3\\sin\\theta - 4)^2 = (-4\\cos\\theta)^2 \\implies 9\\sin^2\\theta - 24\\sin\\theta + 16 = 16(1-\\sin^2\\theta)$\n"
    "$\\implies 25\\sin^2\\theta - 24\\sin\\theta = 0 \\implies \\sin\\theta(25\\sin\\theta - 24) = 0$\n"
    "যেহেতু $\\sin\\theta \\neq 0$, $\\therefore \\sin\\theta = \\dfrac{24}{25} \\implies \\theta = \\sin^{-1} \\dfrac{24}{25}$ [প্রমাণিত]\n\n"
    "গ. দেওয়া আছে, $g(5\\theta)-\\sqrt{3}\\,g(\\theta)=g(3\\theta)$, যেখানে $g(x)=\\sin x$\n"
    "$\\implies \\sin 5\\theta - \\sin 3\\theta = \\sqrt{3}\\sin\\theta$\n"
    "$\\implies 2\\cos 4\\theta \\sin\\theta = \\sqrt{3}\\sin\\theta \\implies \\sin\\theta(2\\cos 4\\theta - \\sqrt{3}) = 0$\n"
    "হয়, $\\sin\\theta = 0 \\implies \\theta = n\\pi \\quad (n \\in \\mathbb{Z})$\n"
    "অথবা, $2\\cos 4\\theta = \\sqrt{3} \\implies \\cos 4\\theta = \\cos\\dfrac{\\pi}{6} \\implies 4\\theta = 2n\\pi \\pm \\dfrac{\\pi}{6}$\n"
    "$\\therefore \\theta = \\dfrac{1}{4}\\left(2n\\pi \\pm \\dfrac{\\pi}{6}\\right) \\quad (n \\in \\mathbb{Z})$\n"
    "$\\therefore$ নির্ণেয় সমাধান: $\\theta = n\\pi, \\ \\dfrac{1}{4}\\left(2n\\pi \\pm \\dfrac{\\pi}{6}\\right) \\quad (n \\in \\mathbb{Z})$"
)

q786_expl_text = (
    "**ক অংশের বিশ্লেষণ:**\n"
    "বিপরীত ত্রিকোণমিতিক রূপান্তরের ক্রমানুসারে:\n"
    "1. $\\sec^{-1}\\frac{x}{y}$ কে সমকোণী ত্রিভুজের সাহায্যে $\\tan^{-1}\\frac{\\sqrt{x^2-y^2}}{y}$ এ পরিবর্তন করা হয়।\n"
    "2. এরপর $\\tan(\\tan^{-1}\\dots)$ অপসারিত হয়ে $\\sin^{-1}\\frac{\\sqrt{x^2-y^2}}{y}$ থাকে।\n"
    "3. সবশেষে একে $\\operatorname{cosec}^{-1}\\frac{y}{\\sqrt{x^2-y^2}}$ এ রূপান্তর করলে $\\operatorname{cosec}(\\operatorname{cosec}^{-1}\\dots)$ অপসারিত হয়ে $\\frac{y}{\\sqrt{x^2-y^2}}$ প্রমাণ হয়।\n\n"
    "**খ অংশের বিশ্লেষণ:**\n"
    "$\\operatorname{cosec}\\theta - \\cot\\theta = \\frac{1-\\cos\\theta}{\\sin\\theta} = \\frac{3}{4}$ সমীকরণ থেকে পক্ষান্তর ও বর্গ করে দ্বিঘাত সমীকরণ গঠন করা হয়। $\\sin\\theta=0$ গ্রহণযোগ্য নয় কারণ এতে কোসেক ও কট অসংজ্ঞায়িত হয়ে যায়।\n\n"
    "**গ অংশের বিশ্লেষণ:**\n"
    "$\\sin C - \\sin D = 2\\cos\\frac{C+D}{2}\\sin\\frac{C-D}{2}$ সূত্র ব্যবহার করে সমীকরণটিকে সহজে উৎপাদকে বিশ্লেষণ করে সাধারণ সমাধান বের করা হয়েছে।"
)

# 1. Update processed_questions.json
proc_file = os.path.join(HERE, "processed_questions.json")
with open(proc_file, "r", encoding="utf-8") as f:
    proc_data = json.load(f)

for q in proc_data["questions"]:
    if q["n"] == 786:
        q["q"] = q786_question_text
        q["a"] = q786_answer_text
        q["e"] = q786_expl_text
        break

with open(proc_file, "w", encoding="utf-8") as f:
    json.dump(proc_data, f, ensure_ascii=False, indent=2)

print("Updated Question 786 in processed_questions.json!")

# 2. Update raw JSON as well
raw_json_path = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json")
with open(raw_json_path, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# Question 786 is at index 785 in questions array
for q in raw_data["data"]["questions"]:
    if q.get("id") == 786 or q.get("question_order") == 786:
        # Update question blocks
        q["question"]["body"]["blocks"] = [{
            "key": "q786_fixed",
            "text": q786_question_text,
            "type": "unstyled",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }]
        # Update explanation blocks
        if "explanation" not in q or not q["explanation"]:
            q["explanation"] = {"body": {"blocks": [], "entityMap": {}}}
        q["explanation"]["body"]["blocks"] = [{
            "key": "q786_ans_fixed",
            "text": q786_answer_text + "\n\n" + q786_expl_text,
            "type": "unstyled",
            "depth": 0,
            "inlineStyleRanges": [],
            "entityRanges": [],
            "data": {}
        }]
        break

with open(raw_json_path, "w", encoding="utf-8") as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=2)

print("Updated Question 786 in raw JSON!")
