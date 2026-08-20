# -*- coding: utf-8 -*-
"""Processes and enriches the question bank JSON.
1. Extracts DraftJS text and entityMap images.
2. Fixes LaTeX glitches and formatting.
3. Fixes all 12 defective questions by adding 5th options (ঙ) or setting correct indices.
4. Provides complete, high-quality step-by-step mathematical explanations.
5. Extracts and formats exam subsources (Board, Admission, College Test, Year).
"""
import json
import os
import re
from interval_explanations import INTERVAL_EXPLANATIONS
from direct_inverse_explanations import DIRECT_INVERSE_EXPLANATIONS
from domain_range_explanations import DOMAIN_RANGE_GUIDE
from diagram_solutions import DIAGRAM_SOLUTIONS

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_JSON = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ.json")
BACKUP_JSON = os.path.join(HERE, "question_bank_HSC_Admission_HSC_-_উচ্চতর_গণিত_২য়_পত্র_অধ্যায়-০৭ঃ_বিপরীত_ত্রিকোণমিতিক_ফাংশন_ও_ত্রিকোণমিতিক_সমীকরণ_backup.json")

def blocks_to_text(val):
    """Convert DraftJS dictionary (or string) to string with image markdown."""
    if val is None:
        return ""
    if isinstance(val, str):
        val_s = val.strip()
        if val_s.startswith("{") and "blocks" in val_s:
            try:
                val = json.loads(val_s)
            except Exception:
                return val
        else:
            return val
    if isinstance(val, dict):
        blocks = val.get("blocks") or []
        emap = val.get("entityMap") or {}
        parts = []
        for b in blocks:
            t = (b or {}).get("text") or ""
            eranges = (b or {}).get("entityRanges") or []
            imgs = []
            for er in eranges:
                k = str(er.get("key"))
                if k in emap and emap[k].get("type") == "IMAGE":
                    src = emap[k].get("data", {}).get("src")
                    if src:
                        imgs.append(f"![চিত্র]({src})")
            if imgs:
                parts.append(" ".join(imgs))
            if t:
                parts.append(t)
        return "\n".join(parts) if parts else ""
    return ""

def format_subsources(subs):
    if not subs:
        return []
    res = []
    for s in subs:
        sub_source = s.get("sub_source") or {}
        name = (sub_source.get("name") or "").strip()
        desc = (sub_source.get("description") or "").strip()
        source_obj = sub_source.get("source") or {}
        source_name = (source_obj.get("name") or "").strip()
        year = ((s.get("year") or {}).get("name") or "").strip()
        
        # Build clean display tag
        if name and year:
            tag = f"{name} '{year[-2:] if len(year)==4 else year}"
        elif name:
            tag = name
        elif desc and year:
            tag = f"{desc} '{year[-2:] if len(year)==4 else year}"
        elif desc:
            tag = desc
        elif source_name:
            tag = source_name
        else:
            tag = "অন্যান্য"

        full_title = f"{desc or name} ({year})" if year else (desc or name or source_name)
        res.append({
            "tag": tag,
            "name": name,
            "desc": desc,
            "type": source_name,
            "year": year,
            "full": full_title
        })
    return res

def clean_latex(txt):
    if not txt:
        return ""
    # Fix double dollar at beginning of option like $$\frac{\pi}{4}
    txt = re.sub(r'^\$\$(\\[a-zA-Z]+[^\$]*)$', r'$\1$', txt)
    # Fix 1 /\left(1+x^{2}\right)$ -> $\frac{1}{1+x^2}$
    txt = txt.replace(r'1 /\left(1+x^{2}\right)$', r'$\frac{1}{1+x^{2}}$')
    # Fix unclosed dollar in Q648
    if r'$2\left(\cos ^{2} \theta-\sin ^{2} \theta\right)=\sqrt{3}' in txt and not txt.startswith(r'$2\left(\cos ^{2} \theta-\sin ^{2} \theta\right)=\sqrt{3}$'):
        txt = txt.replace(r'$2\left(\cos ^{2} \theta-\sin ^{2} \theta\right)=\sqrt{3} ', r'$2\left(\cos ^{2} \theta-\sin ^{2} \theta\right)=\sqrt{3}$ ')
    # Fix stray 'সা সমাধান' typo
    txt = txt.replace("সমীকরণের সা সমাধান", "সমীকরণের সমাধান")
    txt = txt.replace("সা সমাধান", "সমাধান")
    # Fix stray prime artifact { }^{\prime} like in Q98 Option 4
    txt = re.sub(r'\{\s*\}\^\{\\prime\}', '', txt)
    txt = re.sub(r'\+\s*\{\s*\}\^\{\\prime\}', '+ ', txt)
    txt = re.sub(r'\+\s*\'\s*\(', '+ (', txt)
    return txt

def main():
    with open(INPUT_JSON, encoding="utf-8") as f:
        data = json.load(f)

    qs = data["data"]["questions"]
    print(f"Total questions in JSON: {len(qs)}")

    processed_questions = []
    
    for i, q in enumerate(qs, 1):
        is_mcq = q.get("question_type", {}).get("name") == "বহুনির্বাচনি প্রশ্ন"
        idx = q.get("mcq_solution_index")
        
        qtext = clean_latex(blocks_to_text(q.get("question_text")))
        answer = clean_latex(blocks_to_text(q.get("answer_text")))
        explanation = clean_latex(blocks_to_text(q.get("explanation_text")))
        
        opts = []
        if is_mcq:
            for o in q.get("option") or []:
                opts.append(clean_latex(blocks_to_text(o)))
        
        subsources = format_subsources(q.get("question_subsources"))

        # Fix defective / missing answer questions by adding 5th options (ঙ)
        if i == 92: # tan^2(sec^-1(1/2))
            if len(opts) == 4:
                opts.append("বাস্তব মানে অসংজ্ঞায়িত (বীজগাণিতিক সূত্রে $-\\frac{3}{4}$)")
            idx = 4
            answer = "বাস্তব মানে অসংজ্ঞায়িত (বীজগাণিতিক সূত্রে $-\\frac{3}{4}$)"
            explanation = (
                "$\\sec^{-1}x$ সংজ্ঞায়িত হওয়ার শর্ত $|x| \\geq 1$।\n"
                "যেহেতু $|\\frac{1}{2}| < 1$, তাই বাস্তব সংখ্যার ক্ষেত্রে $\\sec^{-1}\\frac{1}{2}$ অসংজ্ঞায়িত (বাস্তব মান নেই)।\n"
                "তবে আনুষ্ঠানিক ত্রিকোণমিতিক অভেদ $\\tan^2\\theta = \\sec^2\\theta - 1$ প্রয়োগ করলে:\n"
                "$\\tan^2\\left(\\sec^{-1}\\frac{1}{2}\\right) = \\left(\\frac{1}{2}\\right)^2 - 1 = \\frac{1}{4} - 1 = -\\frac{3}{4}$ পাওয়া যায়।\n"
                "সঠিক গাণিতিক বিশ্লেষণ অনুযায়ী পঞ্চম অপশন (ঙ)-ই যথার্থ উত্তর।"
            )

        elif i == 126: # tan^2(sec^-1(1/2))
            if len(opts) == 4:
                opts.append("বাস্তব মানে অসংজ্ঞায়িত (বীজগাণিতিক সূত্রে $-\\frac{3}{4}$)")
            idx = 4
            answer = "বাস্তব মানে অসংজ্ঞায়িত (বীজগাণিতিক সূত্রে $-\\frac{3}{4}$)"
            explanation = (
                "$\\sec^{-1}x$ সংজ্ঞায়িত হওয়ার জন্য $|x| \\ge 1$ আবশ্যক।\n"
                "এখানে $|\\frac{1}{2}| < 1$ হওয়ায় বাস্তব মানে এটি অসংজ্ঞায়িত।\n"
                "বীজগাণিতিক সূত্র $\\tan^2\\theta = \\sec^2\\theta - 1$ প্রয়োগে মান আসে $-\\frac{3}{4}$।\n"
                "সুতরাং অপশন (ঙ) সঠিক।"
            )

        elif i == 192: # 1/2 cos^-1 (9/41)
            if len(opts) == 4:
                opts.append("$\\tan ^{-1}\\left(\\frac{4}{5}\\right)$")
            idx = 4
            answer = "$\\tan ^{-1}\\left(\\frac{4}{5}\\right)$"
            explanation = (
                "ধরি, $\\theta = \\frac{1}{2}\\cos^{-1}\\left(\\frac{9}{41}\\right) \\implies 2\\theta = \\cos^{-1}\\left(\\frac{9}{41}\\right) \\implies \\cos 2\\theta = \\frac{9}{41}$।\n"
                "আমরা জানি, $\\tan^2\\theta = \\frac{1 - \\cos 2\\theta}{1 + \\cos 2\\theta} = \\frac{1 - \\frac{9}{41}}{1 + \\frac{9}{41}} = \\frac{\\frac{32}{41}}{\\frac{50}{41}} = \\frac{32}{50} = \\frac{16}{25}$।\n"
                "যেহেতু $0 < \\frac{9}{41} < 1$, তাই $0 < \\theta < \\frac{\\pi}{4}$ এবং $\\tan\\theta > 0$।\n"
                "অতএব, $\\tan\\theta = \\sqrt{\\frac{16}{25}} = \\frac{4}{5} \\implies \\theta = \\tan^{-1}\\left(\\frac{4}{5}\\right)$।\n"
                "প্রদত্ত ৪টি অপশনে সঠিক মান না থাকায় পঞ্চম অপশন (ঙ): $\\tan^{-1}\\left(\\frac{4}{5}\\right)$ সঠিক উত্তর।"
            )

        elif i == 546: # y = cot^-1 x graph
            opts = [
                "$y$-অক্ষের সাপেক্ষে $(0, \\pi)$ ব্যবধিতে নিমজ্জিত অবিচ্ছিন্ন বক্ররেখা",
                "$(-\\frac{\\pi}{2}, \\frac{\\pi}{2})$ ব্যবধিতে ঊর্ধ্বগামী বক্ররেখা",
                "$[0, \\pi]$ ব্যবধিতে খণ্ডিত রেখা",
                "$(-\\infty, \\infty)$ ব্যবধিতে বৃত্তাকার লেখ",
                "ডোমেন $(-\\infty, \\infty)$ এবং রেঞ্জ $(0, \\pi)$ বিশিষ্ট অবিচ্ছিন্ন ক্রমহ্রাসমান লেখচিত্র"
            ]
            idx = 4
            answer = "ডোমেন $(-\\infty, \\infty)$ এবং রেঞ্জ $(0, \\pi)$ বিশিষ্ট অবিচ্ছিন্ন ক্রমহ্রাসমান লেখচিত্র"
            explanation = (
                "$y = \\cot^{-1} x$ ফাংশনের ডোমেন $\\mathbb{R} = (-\\infty, \\infty)$ এবং রেঞ্জ বা মুখ্যমান শাখা $(0, \\pi)$।\n"
                "$x \\to -\\infty$ হলে $y \\to \\pi$, $x = 0$ হলে $y = \\frac{\\pi}{2}$, এবং $x \\to \\infty$ হলে $y \\to 0$।\n"
                "লেখচিত্রটি প্রথম ও দ্বিতীয় চতুর্ভাগে অসীমতট $y=0$ ও $y=\\pi$-এর মাঝে একটি অবিচ্ছিন্ন ক্রমহ্রাসমান বক্ররেখা।\n"
                "সঠিক উত্তর: অপশন (ঙ)।"
            )

        elif i == 548: # sin^-1 cos tan^-1 x = tan^-1 (5/2)
            if len(opts) == 4:
                opts.append("$\\frac{2}{5}$")
            idx = 4
            answer = "$\\frac{2}{5}$"
            explanation = (
                "বামপক্ষ: $\\sin^{-1}\\left(\\cos(\\tan^{-1} x)\\right)$\n"
                "ধরি $\\tan^{-1} x = \\theta \\implies \\tan\\theta = x$। তাহলে সমকোণী ত্রিভুজ হতে $\\cos\\theta = \\frac{1}{\\sqrt{1+x^2}}$।\n"
                "সুতরাং $\\sin^{-1}\\left(\\frac{1}{\\sqrt{1+x^2}}\\right) = \\cot^{-1} x = \\tan^{-1}\\left(\\frac{1}{x}\\right)$।\n"
                "প্রশ্নমতে, $\\tan^{-1}\\left(\\frac{1}{x}\\right) = \\tan^{-1}\\left(\\frac{5}{2}\\right) \\implies \\frac{1}{x} = \\frac{5}{2} \\implies x = \\frac{2}{5}$।\n"
                "যেহেতু প্রদত্ত চার বিকল্পে $+\\frac{2}{5}$ ছিল না, তাই সঠিক উত্তর পঞ্চম অপশন (ঙ): $\\frac{2}{5}$।"
            )

        elif i == 582: # Graph function identity
            idx = 2
            answer = "$y=\\sin ^{-1} x$"
            explanation = (
                "উদ্দীপকের লেখচিত্রটি মূলবিন্দু $(0,0)$ দিয়ে অতিক্রম করে এবং এর ডোমেন $[-1, 1]$ ও বিস্তার বা রেঞ্জ $[-\\frac{\\pi}{2}, \\frac{\\pi}{2}]$।\n"
                "এটি বিপরীত সাইন ফাংশন $y = \\sin^{-1} x$-এর প্রমিত মুখ্যমান লেখচিত্র।\n"
                "সঠিক উত্তর: গ ($y = \\sin^{-1} x$)।"
            )

        elif i == 583: # Principal value range of graph
            idx = 2
            answer = "$\\left[-\\frac{\\pi}{2}, \\frac{\\pi}{2}\\right]$"
            explanation = (
                "উদ্দীপকের লেখচিত্রটি $y = \\sin^{-1} x$ ফাংশন নির্দেশ করে।\n"
                "বিপরীত ত্রিকোণমিতিক ফাংশন $y = \\sin^{-1} x$-এর মুখ্যমান পরিসর বা রেঞ্জ হলো $[-\\frac{\\pi}{2}, \\frac{\\pi}{2}]$।\n"
                "সঠিক উত্তর: গ।"
            )

        elif i == 590: # BC side relationship
            idx = 0
            answer = "$P \\cos \\theta+q \\sin \\theta=r$"
            explanation = (
                "উদ্দীপকের জ্যামিতিক চিত্রানুসারে $BC$ বাহুর দৈর্ঘ্য $r$।\n"
                "চিত্রের বাহুগুলোর লম্ব অভিক্ষেপ ও ত্রিকোণমিতিক সূত্রানুসারে পাই:\n"
                "$r = p\\cos\\theta + q\\sin\\theta$ বা $P\\cos\\theta + q\\sin\\theta = r$।\n"
                "সঠিক উত্তর: ক।"
            )

        elif i == 591: # pq/r^2 = sqrt(3)/4
            idx = 0
            answer = "i ও ii"
            explanation = (
                "উদ্দীপক অনুসারে $p = r\\cos\\theta$ এবং $q = r\\sin\\theta$ হলে:\n"
                "$\\frac{pq}{r^2} = \\sin\\theta\\cos\\theta = \\frac{1}{2}\\sin 2\\theta = \\frac{\\sqrt{3}}{4} \\implies \\sin 2\\theta = \\frac{\\sqrt{3}}{2} = \\sin\\frac{\\pi}{3}$।\n"
                "১. সাধারণ সমাধান: $2\\theta = n\\pi + (-1)^n \\frac{\\pi}{3} \\implies \\theta = \\frac{n\\pi}{2} + (-1)^n \\frac{\\pi}{6}$ (বিবৃতি i সত্য)।\n"
                "২. $\\triangle ABC$-এ সূক্ষ্মকোণের জন্য $n=0$ বসালে $\\theta = \\frac{\\pi}{6} = 30^\\circ$ (বিবৃতি ii সত্য)।\n"
                "অতএব i ও ii সঠিক। সঠিক উত্তর: ক।"
            )

        elif i == 618: # Principal value of sin^-1(-sqrt(3)/2)
            if len(opts) == 4:
                opts.append("শুধুমাত্র ii (মুখ্যমান $-\\frac{\\pi}{3}$)")
            idx = 4
            answer = "শুধুমাত্র ii (মুখ্যমান $-\\frac{\\pi}{3}$)"
            explanation = (
                "$\\sin^{-1} x$-এর মুখ্যমান পরিসর $[-\\frac{\\pi}{2}, \\frac{\\pi}{2}]$ (প্রথম ও চতুর্থ চতুর্ভাগ)।\n"
                "$\\sin(-\\frac{\\pi}{3}) = -\\frac{\\sqrt{3}}{2}$ হওয়ায় মুখ্যমান $-\\frac{\\pi}{3}$ (বিবৃতি ii সঠিক)।\n"
                "$\\frac{4\\pi}{3}$ মুখ্যমান পরিসরের বাইরে এবং $-\\frac{\\pi}{3}$ চতুর্থ চতুর্ভাগে (তৃতীয় চতুর্ভাগে নয়), তাই i ও iii ভুল।\n"
                "প্রদত্ত চার অপশনে এককভাবে ii না থাকায় সঠিক উত্তর পঞ্চম অপশন (ঙ): শুধুমাত্র ii।"
            )

        elif i == 678: # cos^-1 x + sin^-1 y = pi/2
            if len(opts) == 4:
                opts.append("$2x^2$ (প্রশ্নে $\\sin^{-1}x+\\sin^{-1}y=\\frac{\\pi}{2}$ হলে $1$)")
            idx = 4
            answer = "$2x^2$ (প্রশ্নে $\\sin^{-1}x+\\sin^{-1}y=\\frac{\\pi}{2}$ হলে $1$)"
            explanation = (
                "$\\cos^{-1}x + \\sin^{-1}y = \\frac{\\pi}{2} \\implies \\left(\\frac{\\pi}{2} - \\sin^{-1}x\\right) + \\sin^{-1}y = \\frac{\\pi}{2} \\implies \\sin^{-1}y = \\sin^{-1}x \\implies y = x$।\n"
                "সুতরাং $x^2 + y^2 = x^2 + x^2 = 2x^2$ (মানটি $x$-এর উপর নির্ভরশীল)।\n"
                "প্রমিত পরীক্ষার প্রশ্নে এটি মূলত $\\sin^{-1}x + \\sin^{-1}y = \\frac{\\pi}{2}$ ছিল, যা থেকে $x^2 + y^2 = 1$ হয়।\n"
                "সঠিক সমাধান ও সংশোধিত উত্তর পঞ্চম অপশন (ঙ)-তে দেওয়া হলো।"
            )

        elif i == 720: # sin x = sin k general solution
            qtext = "$\\sin x = \\sin k$ সমীকরণ হলে নিচের কোনটি সঠিক?"
            idx = 0
            answer = "$x=n \\pi+(-1)^{n} k$"
            explanation = (
                "মূল সমীকরণ $\\sin x = \\sin k$ হলে সাধারণ সমাধানের প্রমিত সূত্র:\n"
                "$x = n\\pi + (-1)^n k$, যেখানে $n \\in \\mathbb{Z}$।\n"
                "সঠিক উত্তর: ক ($x=n \\pi+(-1)^{n} k$)।"
            )

        # Apply n-based general solution explanations for interval-based questions
        if i in INTERVAL_EXPLANATIONS:
            explanation = INTERVAL_EXPLANATIONS[i]

        # Apply direct right-angled triangle inverse transformation explanations
        if i in DIRECT_INVERSE_EXPLANATIONS:
            explanation = DIRECT_INVERSE_EXPLANATIONS[i]

        # Apply mathematically verified diagram solutions
        if i in DIAGRAM_SOLUTIONS:
            sol = DIAGRAM_SOLUTIONS[i]
            if "a" in sol:
                answer = sol["a"]
            if "e" in sol:
                explanation = sol["e"]

        # Attach Master Domain & Range Reference Guide for all domain/range/principal value questions
        comb_text = f"{qtext} {' '.join(opts)} {explanation}".lower()
        if ("ডোমেন" in comb_text or "রেঞ্জ" in comb_text or "মুখ্যমান" in comb_text or "মুখ্য মান" in comb_text or "domain" in comb_text or "range" in comb_text) and "বিপরীত ত্রিকোণমিতিক ফাংশনের ডোমেন ও রেঞ্জের সম্পূর্ণ মাস্টার গাইড" not in explanation:
            explanation = (explanation + "\n\n" + DOMAIN_RANGE_GUIDE).strip()

        processed_questions.append({
            "n": i,
            "t": 0 if is_mcq else 1,
            "q": qtext,
            "o": opts,
            "a": answer,
            "e": explanation,
            "i": idx if isinstance(idx, int) else -1,
            "d": 0,
            "s": subsources
        })

    total = len(processed_questions)
    mcq = sum(1 for q in processed_questions if q["t"] == 0)
    solved = sum(1 for q in processed_questions if q["a"] or q["e"])
    stats = {"total": total, "mcq": mcq, "cr": total - mcq, "solved": solved}

    print(f"Processed stats: total={total}, mcq={mcq}, cr={total-mcq}, solved={solved}")
    
    out_file = os.path.join(HERE, "processed_questions.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({"stats": stats, "questions": processed_questions}, f, ensure_ascii=False, indent=2)
    print(f"Saved processed data to {out_file}")

if __name__ == "__main__":
    main()
