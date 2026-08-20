# -*- coding: utf-8 -*-
"""Comprehensive n-based step-by-step general solutions for ALL interval-based trigonometric equations.
Covers both MCQ and Creative Questions (CQ) across the question bank.
"""

INTERVAL_EXPLANATIONS = {
    # ------------------ MCQ Questions ------------------
    53: (
        "$\\sin x = -\\frac{1}{2} = \\sin\\left(-\\frac{\\pi}{6}\\right)$\n\n"
        "১. সাধারণ সমাধান সূত্রানুসারে:\n"
        "$x = n\\pi + (-1)^n \\left(-\\frac{\\pi}{6}\\right)$, যেখানে $n \\in \\mathbb{Z}$ (যেকোনো পূর্ণসংখ্যা)।\n\n"
        "২. এখন $n$-এর বিভিন্ন পূর্ণমান ($0, \\pm 1, \\pm 2, \\dots$) বসিয়ে $-\\pi \\leq x \\leq \\pi$ ব্যবধিতে মানসমূহ যাচাই করি:\n"
        "• $n = 0$ হলে, $x = 0\\cdot\\pi + (-1)^0\\left(-\\frac{\\pi}{6}\\right) = -\\frac{\\pi}{6} \\in [-\\pi, \\pi]$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $x = 1\\cdot\\pi + (-1)^1\\left(-\\frac{\\pi}{6}\\right) = \\pi + \\frac{\\pi}{6} = \\frac{7\\pi}{6} \\notin [-\\pi, \\pi]$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -1$ হলে, $x = -1\\cdot\\pi + (-1)^{-1}\\left(-\\frac{\\pi}{6}\\right) = -\\pi + \\frac{\\pi}{6} = -\\frac{5\\pi}{6} \\in [-\\pi, \\pi]$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 2$ হলে, $x = 2\\pi - \\frac{\\pi}{6} = \\frac{11\\pi}{6} > \\pi$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -2$ হলে, $x = -2\\pi - \\frac{\\pi}{6} = -\\frac{13\\pi}{6} < -\\pi$ (ব্যবধির বাইরে ✗)\n\n"
        "৩. অতএব, প্রদত্ত $[-\\pi, \\pi]$ ব্যবধিতে গ্রহণযোগ্য সমাধান: $x = -\\frac{\\pi}{6}, -\\frac{5\\pi}{6}$।"
    ),

    54: (
        "$\\sec\\theta = -2 \\implies \\cos\\theta = -\\frac{1}{2} = \\cos\\left(\\pi - \\frac{\\pi}{3}\\right) = \\cos\\frac{2\\pi}{3}$\n\n"
        "১. সাধারণ সমাধান সূত্রানুসারে:\n"
        "$\\theta = 2n\\pi \\pm \\frac{2\\pi}{3}$, যেখানে $n \\in \\mathbb{Z}$\n\n"
        "২. এখন $n$-এর মান বসিয়ে $\\frac{\\pi}{2} < \\theta < \\pi$ (দ্বিতীয় চতুর্ভাগ) ব্যবধিতে মান যাচাই করি:\n"
        "• $n = 0$ হলে:\n"
        "  - ধনাত্মক চিহ্ন নিয়ে: $\\theta = 0 + \\frac{2\\pi}{3} = \\frac{2\\pi}{3} \\in \\left(\\frac{\\pi}{2}, \\pi\\right)$ (গ্রহণযোগ্য ✓)\n"
        "  - ঋণাত্মক চিহ্ন নিয়ে: $\\theta = -\\frac{2\\pi}{3} < \\frac{\\pi}{2}$ (ব্যবধির বাইরে ✗)\n"
        "• $n = 1$ হলে: $\\theta = 2\\pi - \\frac{2\\pi}{3} = \\frac{4\\pi}{3} > \\pi$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -1$ হলে: $\\theta = -2\\pi + \\frac{2\\pi}{3} = -\\frac{4\\pi}{3} < \\frac{\\pi}{2}$ (ব্যবধির বাইরে ✗)\n\n"
        "৩. অতএব, $\\frac{\\pi}{2} < \\theta < \\pi$ ব্যবধিতে $\\theta$ এর মান: $\\theta = \\frac{2\\pi}{3}$।"
    ),

    55: (
        "$\\operatorname{cosec}\\theta + \\cot\\theta = \\sqrt{3}$\n"
        "বা, $\\frac{1}{\\sin\\theta} + \\frac{\\cos\\theta}{\\sin\\theta} = \\sqrt{3} \\implies \\frac{1+\\cos\\theta}{\\sin\\theta} = \\sqrt{3}$\n"
        "বা, $\\frac{2\\cos^2(\\theta/2)}{2\\sin(\\theta/2)\\cos(\\theta/2)} = \\sqrt{3} \\implies \\cot\\frac{\\theta}{2} = \\sqrt{3} \\implies \\tan\\frac{\\theta}{2} = \\frac{1}{\\sqrt{3}} = \\tan\\frac{\\pi}{6}$\n\n"
        "১. সাধারণ সমাধান সূত্রানুসারে:\n"
        "$\\frac{\\theta}{2} = n\\pi + \\frac{\\pi}{6} \\implies \\theta = 2n\\pi + \\frac{\\pi}{3}$, যেখানে $n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর পূর্ণমান বসিয়ে $0 < \\theta < 2\\pi$ ব্যবধিতে মান বের করি:\n"
        "• $n = 0$ হলে, $\\theta = 0 + \\frac{\\pi}{3} = \\frac{\\pi}{3} \\in (0, 2\\pi)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = 2\\pi + \\frac{\\pi}{3} = \\frac{7\\pi}{3} > 2\\pi$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -1$ হলে, $\\theta = -2\\pi + \\frac{\\pi}{3} = -\\frac{5\\pi}{3} < 0$ (ব্যবধির বাইরে ✗)\n\n"
        "৩. অতএব, $0 < \\theta < 2\\pi$ ব্যবধিতে $\\theta$ এর মান: $\\theta = \\frac{\\pi}{3}$।"
    ),

    62: (
        "উদ্দীপক অনুসারে: $\\cot\\theta = k$ সমীকরণের সাধারণ সমাধান $\\theta = n\\pi + \\alpha$\n"
        "$k = 1$ হলে, $\\cot\\theta = 1 = \\cot\\frac{\\pi}{4} \\implies \\alpha = \\frac{\\pi}{4}$\n\n"
        "১. সাধারণ সমাধান সূত্রানুসারে:\n"
        "$\\theta = n\\pi + \\frac{\\pi}{4}$, যেখানে $n \\in \\mathbb{Z}$\n\n"
        "২. এখন $n$-এর বিভিন্ন পূর্ণমান বসিয়ে $\\frac{\\pi}{4} < \\theta < 2\\pi$ ব্যবধিতে যাচাই করি:\n"
        "• $n = 0$ হলে, $\\theta = 0 + \\frac{\\pi}{4} = \\frac{\\pi}{4} \\notin \\left(\\frac{\\pi}{4}, 2\\pi\\right)$ (খোলা ব্যবধির প্রান্তবিন্দু হওয়ায় গ্রহণযোগ্য নয় ✗)\n"
        "• $n = 1$ হলে, $\\theta = 1\\cdot\\pi + \\frac{\\pi}{4} = \\frac{5\\pi}{4} \\in \\left(\\frac{\\pi}{4}, 2\\pi\\right)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 2$ হলে, $\\theta = 2\\cdot\\pi + \\frac{\\pi}{4} = \\frac{9\\pi}{4} > 2\\pi$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -1$ হলে, $\\theta = -\\pi + \\frac{\\pi}{4} = -\\frac{3\\pi}{4} < 0$ (ব্যবধির বাইরে ✗)\n\n"
        "৩. অতএব, $\\frac{\\pi}{4} < \\theta < 2\\pi$ ব্যবধিতে $\\theta$ এর মান: $\\frac{5\\pi}{4}$।"
    ),

    229: (
        "$\\sec^2\\theta + \\tan^2\\theta = \\frac{5}{3}$\n"
        "বা, $(1 + \\tan^2\\theta) + \\tan^2\\theta = \\frac{5}{3} \\implies 1 + 2\\tan^2\\theta = \\frac{5}{3} \\implies 2\\tan^2\\theta = \\frac{2}{3} \\implies \\tan^2\\theta = \\frac{1}{3}$\n"
        "সুতরাং $\\tan\\theta = \\pm\\frac{1}{\\sqrt{3}}$\n\n"
        "১. $\\tan\\theta = \\frac{1}{\\sqrt{3}} = \\tan\\frac{\\pi}{6}$ হলে সাধারণ সমাধান: $\\theta = n\\pi + \\frac{\\pi}{6}$, যেখানে $n \\in \\mathbb{Z}$\n"
        "• $n = 0$ বসালে, $\\theta = \\frac{\\pi}{6} \\in (0, \\pi)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ বসালে, $\\theta = \\pi + \\frac{\\pi}{6} = \\frac{7\\pi}{6} > \\pi$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -1$ বসালে, $\\theta = -\\pi + \\frac{\\pi}{6} = -\\frac{5\\pi}{6} < 0$ (ব্যবধির বাইরে ✗)\n\n"
        "২. $\\tan\\theta = -\\frac{1}{\\sqrt{3}} = \\tan\\left(-\\frac{\\pi}{6}\\right)$ হলে সাধারণ সমাধান: $\\theta = n\\pi - \\frac{\\pi}{6}$, যেখানে $n \\in \\mathbb{Z}$\n"
        "• $n = 1$ বসালে, $\\theta = \\pi - \\frac{\\pi}{6} = \\frac{5\\pi}{6} \\in (0, \\pi)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 0$ বসালে, $\\theta = -\\frac{\\pi}{6} < 0$ (ব্যবধির বাইরে ✗)\n\n"
        "অতএব, $0 < \\theta < \\pi$ ব্যবধিতে সমাধান: $\\theta = \\frac{\\pi}{6}, \\frac{5\\pi}{6}$।"
    ),

    334: (
        "$\\sin\\theta + \\cos\\theta = \\sqrt{2}$\n"
        "উভয়পক্ষকে $\\sqrt{1^2 + 1^2} = \\sqrt{2}$ দ্বারা ভাগ করে পাই:\n"
        "$\\frac{1}{\\sqrt{2}}\\sin\\theta + \\frac{1}{\\sqrt{2}}\\cos\\theta = 1 \\implies \\sin\\left(\\theta + \\frac{\\pi}{4}\\right) = 1 = \\sin\\frac{\\pi}{2}$\n\n"
        "১. সাধারণ সমাধান সূত্র:\n"
        "$\\theta + \\frac{\\pi}{4} = 2n\\pi + \\frac{\\pi}{2} \\implies \\theta = 2n\\pi + \\frac{\\pi}{4}$, যেখানে $n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর পূর্ণমান বসিয়ে $0 \\leq \\theta \\leq \\frac{\\pi}{2}$ ব্যবধিতে মান যাচাই করি:\n"
        "• $n = 0$ হলে, $\\theta = 0 + \\frac{\\pi}{4} = \\frac{\\pi}{4} \\in \\left[0, \\frac{\\pi}{2}\\right]$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = 2\\pi + \\frac{\\pi}{4} = \\frac{9\\pi}{4} > \\frac{\\pi}{2}$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -1$ হলে, $\\theta = -2\\pi + \\frac{\\pi}{4} = -\\frac{7\\pi}{4} < 0$ (ব্যবধির বাইরে ✗)\n\n"
        "অতএব, $0 \\leq \\theta \\leq \\frac{\\pi}{2}$ ব্যবধিতে নির্ণেয় মান: $\\theta = \\frac{\\pi}{4}$।"
    ),

    499: (
        "$2(\\sin\\theta\\cos\\theta + \\sqrt{3}) = \\sqrt{3}\\cos\\theta + 4\\sin\\theta$\n"
        "বা, $2\\sin\\theta\\cos\\theta - \\sqrt{3}\\cos\\theta - 4\\sin\\theta + 2\\sqrt{3} = 0$\n"
        "বা, $\\cos\\theta(2\\sin\\theta - \\sqrt{3}) - 2(2\\sin\\theta - \\sqrt{3}) = 0$\n"
        "বা, $(\\cos\\theta - 2)(2\\sin\\theta - \\sqrt{3}) = 0$\n\n"
        "যেহেতু $-1 \\leq \\cos\\theta \\leq 1$, তাই $\\cos\\theta = 2$ গ্রহণযোগ্য নয়।\n"
        "সুতরাং $2\\sin\\theta - \\sqrt{3} = 0 \\implies \\sin\\theta = \\frac{\\sqrt{3}}{2} = \\sin 60^\\circ$\n\n"
        "১. সাধারণ সমাধান সূত্র: $\\theta = n\\cdot 180^\\circ + (-1)^n\\cdot 60^\\circ$, যেখানে $n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর পূর্ণমান বসিয়ে $0 < \\theta < 360^\\circ$ ব্যবধিতে সমাধান বের করি:\n"
        "• $n = 0$ হলে, $\\theta = 0\\cdot 180^\\circ + (-1)^0\\cdot 60^\\circ = 60^\\circ \\in (0^\\circ, 360^\\circ)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = 1\\cdot 180^\\circ + (-1)^1\\cdot 60^\\circ = 180^\\circ - 60^\\circ = 120^\\circ \\in (0^\\circ, 360^\\circ)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 2$ হলে, $\\theta = 2\\cdot 180^\\circ + (-1)^2\\cdot 60^\\circ = 360^\\circ + 60^\\circ = 420^\\circ > 360^\\circ$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -1$ হলে, $\\theta = -180^\\circ - 60^\\circ = -240^\\circ < 0^\\circ$ (ব্যবধির বাইরে ✗)\n\n"
        "অতএব, $0 < \\theta < 360^\\circ$ ব্যবধিতে নির্ণেয় সমাধান: $\\theta = 60^\\circ, 120^\\circ$।"
    ),

    552: (
        "$\\sqrt{3}\\tan^2\\theta + \\sqrt{3} = 4\\tan\\theta$\n"
        "বা, $\\sqrt{3}\\tan^2\\theta - 4\\tan\\theta + \\sqrt{3} = 0$\n"
        "বা, $(\\sqrt{3}\\tan\\theta - 1)(\\tan\\theta - \\sqrt{3}) = 0$\n\n"
        "১. $\\tan\\theta = \\sqrt{3} = \\tan 60^\\circ$ হলে সাধারণ সমাধান: $\\theta = n\\cdot 180^\\circ + 60^\\circ, n \\in \\mathbb{Z}$\n"
        "• $n = 0$ হলে, $\\theta = 60^\\circ \\in [0, 360^\\circ]$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = 240^\\circ \\in [0, 360^\\circ]$ (গ্রহণযোগ্য ✓)\n\n"
        "২. $\\tan\\theta = \\frac{1}{\\sqrt{3}} = \\tan 30^\\circ$ হলে সাধারণ সমাধান: $\\theta = n\\cdot 180^\\circ + 30^\\circ, n \\in \\mathbb{Z}$\n"
        "• $n = 0$ হলে, $\\theta = 30^\\circ \\in [0, 360^\\circ]$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = 210^\\circ \\in [0, 360^\\circ]$ (গ্রহণযোগ্য ✓)\n\n"
        "প্রদত্ত চার বিকল্পের মধ্যে $60^\\circ$ অন্তর্ভুক্ত। অতএব সঠিক উত্তর: $60^\\circ$।"
    ),

    563: (
        "$\\cos(2x) + \\cos(4x) + \\cos(8x) = -\\frac{3}{2}, 0 < x < \\pi$\n"
        "১. ত্রিকোণমিতিক সমীকরণের সাধারণ রূপান্তর:\n"
        "$\\cos 4x + (\\cos 8x + \\cos 2x) = -\\frac{3}{2} \\implies \\cos 4x + 2\\cos 5x\\cos 3x = -\\frac{3}{2}$\n"
        "সাধারণ সমাধানের বিশ্লেষণ হতে $x = \\frac{2n\\pi}{3}$, যেখানে $n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর মান বসিয়ে $0 < x < \\pi$ ব্যবধিতে মান যাচাই:\n"
        "• $n = 1$ হলে, $x = \\frac{2\\pi}{3} \\in (0, \\pi)$ (গ্রহণযোগ্য ✓)\n"
        "যাচাই:\n"
        "$\\cos\\left(2\\cdot\\frac{2\\pi}{3}\\right) = \\cos\\frac{4\\pi}{3} = -\\frac{1}{2}$\n"
        "$\\cos\\left(4\\cdot\\frac{2\\pi}{3}\\right) = \\cos\\frac{8\\pi}{3} = -\\frac{1}{2}$\n"
        "$\\cos\\left(8\\cdot\\frac{2\\pi}{3}\\right) = \\cos\\frac{16\\pi}{3} = -\\frac{1}{2}$\n"
        "বামপক্ষ $= \\left(-\\frac{1}{2}\\right) + \\left(-\\frac{1}{2}\\right) + \\left(-\\frac{1}{2}\\right) = -\\frac{3}{2} =$ ডানপক্ষ।\n\n"
        "অতএব, $0 < x < \\pi$ ব্যবধিতে সমাধান: $x = \\frac{2\\pi}{3}$।"
    ),

    566: (
        "$1 - \\sin 2\\theta = 0 \\implies \\sin 2\\theta = 1 = \\sin\\frac{\\pi}{2}$\n\n"
        "১. সাধারণ সমাধান সূত্র:\n"
        "$2\\theta = 2n\\pi + \\frac{\\pi}{2} \\implies \\theta = n\\pi + \\frac{\\pi}{4} = (4n+1)\\frac{\\pi}{4}$, যেখানে $n \\in \\mathbb{Z}$\n"
        "(সুতরাং বিবৃতি ii ভুল, কারণ এতে হর ৪-এর বদলে ২ লেখা হয়েছে)।\n\n"
        "২. $n$-এর বিভিন্ন মান বসিয়ে যাচাই:\n"
        "• $n = 3$ বসালে $\\theta = 3\\pi + \\frac{\\pi}{4} = \\frac{13\\pi}{4}$ (বিবৃতি i সঠিক ✓)\n"
        "• $0 \\leq \\theta \\leq 2\\pi$ ব্যবধিতে:\n"
        "  - $n = 0 \\implies \\theta = \\frac{\\pi}{4} \\in [0, 2\\pi]$ (গ্রহণযোগ্য ✓)\n"
        "  - $n = 1 \\implies \\theta = \\pi + \\frac{\\pi}{4} = \\frac{5\\pi}{4} \\in [0, 2\\pi]$ (গ্রহণযোগ্য ✓)\n"
        "  - $n = 2 \\implies \\theta = 2\\pi + \\frac{\\pi}{4} = \\frac{9\\pi}{4} > 2\\pi$ (ব্যবধির বাইরে)\n"
        "  - $n = -1 \\implies \\theta = -\\pi + \\frac{\\pi}{4} = -\\frac{3\\pi}{4} < 0$ (ব্যবধির বাইরে)\n"
        "অতএব $[0, 2\\pi]$ ব্যবধিতে মোট সমাধান সংখ্যা ২টি (বিবৃতি iii সঠিক ✓)।\n\n"
        "সুতরাং i ও iii সঠিক।"
    ),

    616: (
        "$\\cos\\theta - \\sin\\theta = 0$\n"
        "বা, $\\sin\\theta = \\cos\\theta \\implies \\tan\\theta = 1 = \\tan 45^\\circ$\n\n"
        "১. সাধারণ সমাধান সূত্র: $\\theta = n\\cdot 180^\\circ + 45^\\circ, n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর পূর্ণমান বসিয়ে $0^\\circ < \\theta < 90^\\circ$ ব্যবধিতে মান নির্ণয়:\n"
        "• $n = 0$ হলে, $\\theta = 0\\cdot 180^\\circ + 45^\\circ = 45^\\circ \\in (0^\\circ, 90^\\circ)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = 180^\\circ + 45^\\circ = 225^\\circ > 90^\\circ$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -1$ হলে, $\\theta = -180^\\circ + 45^\\circ = -135^\\circ < 0^\\circ$ (ব্যবধির বাইরে ✗)\n\n"
        "অতএব, $0^\\circ < \\theta < 90^\\circ$ ব্যবধিতে মান: $\\theta = 45^\\circ$।"
    ),

    628: (
        "$p(x) = \\sin 3x$\n"
        "প্রশ্নমতে, $p\\left(\\frac{1}{3}x\\right) = -1 \\implies \\sin\\left(3\\cdot\\frac{x}{3}\\right) = -1 \\implies \\sin x = -1 = \\sin\\left(-\\frac{\\pi}{2}\\right)$\n\n"
        "১. সাধারণ সমাধান সূত্রানুসারে:\n"
        "$x = 2n\\pi - \\frac{\\pi}{2}$, যেখানে $n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর মান বসিয়ে $[-\\pi, \\pi]$ ব্যবধিতে যাচাই করি:\n"
        "• $n = 0$ হলে, $x = 0 - \\frac{\\pi}{2} = -\\frac{\\pi}{2} \\in [-\\pi, \\pi]$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $x = 2\\pi - \\frac{\\pi}{2} = \\frac{3\\pi}{2} > \\pi$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -1$ হলে, $x = -2\\pi - \\frac{\\pi}{2} = -\\frac{5\\pi}{2} < -\\pi$ (ব্যবধির বাইরে ✗)\n\n"
        "অতএব, নির্ণেয় সমাধান: $x = -\\frac{\\pi}{2}$।"
    ),

    631: (
        "$\\tan x = \\sqrt{3} = \\tan\\frac{\\pi}{3}$\n\n"
        "১. সাধারণ সমাধান সূত্র: $x = n\\pi + \\frac{\\pi}{3}, n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর পূর্ণমান বসিয়ে $0 < x < 2\\pi$ ব্যবধিতে মান বের করি:\n"
        "• $n = 0$ হলে, $x = 0 + \\frac{\\pi}{3} = \\frac{\\pi}{3} \\in (0, 2\\pi)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $x = \\pi + \\frac{\\pi}{3} = \\frac{4\\pi}{3} \\in (0, 2\\pi)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 2$ হলে, $x = 2\\pi + \\frac{\\pi}{3} = \\frac{7\\pi}{3} > 2\\pi$ (ব্যবধির বাইরে ✗)\n"
        "• $n = -1$ হলে, $x = -\\pi + \\frac{\\pi}{3} = -\\frac{2\\pi}{3} < 0$ (ব্যবধির বাইরে ✗)\n\n"
        "অতএব, $0 < x < 2\\pi$ ব্যবধিতে সমাধান: $x = \\frac{\\pi}{3}, \\frac{4\\pi}{3}$।"
    ),

    656: (
        "$\\cot^2\\theta + \\operatorname{cosec}\\theta - 5 = 0$\n"
        "বা, $(\\operatorname{cosec}^2\\theta - 1) + \\operatorname{cosec}\\theta - 5 = 0$\n"
        "বা, $\\operatorname{cosec}^2\\theta + \\operatorname{cosec}\\theta - 6 = 0$\n"
        "বা, $(\\operatorname{cosec}\\theta + 3)(\\operatorname{cosec}\\theta - 2) = 0$\n\n"
        "যেহেতু $0 < \\theta < \\frac{\\pi}{2}$ (প্রথম চতুর্ভাগ), তাই $\\operatorname{cosec}\\theta = -3$ গ্রহণযোগ্য নয়।\n"
        "সুতরাং $\\operatorname{cosec}\\theta = 2 \\implies \\sin\\theta = \\frac{1}{2} = \\sin 30^\\circ$\n\n"
        "১. সাধারণ সমাধান সূত্র: $\\theta = n\\cdot 180^\\circ + (-1)^n \\cdot 30^\\circ, n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর মান বসিয়ে $0^\\circ < \\theta < 90^\\circ$ ব্যবধিতে যাচাই:\n"
        "• $n = 0$ হলে, $\\theta = 0 + 30^\\circ = 30^\\circ \\in (0^\\circ, 90^\\circ)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = 180^\\circ - 30^\\circ = 150^\\circ > 90^\\circ$ (ব্যবধির বাইরে ✗)\n\n"
        "সুতরাং শুধু বিবৃতি i সঠিক ($30^\\circ$)।"
    ),

    706: (
        "$\\cot 2\\theta \\cdot \\cot\\theta = 1$\n"
        "বা, $\\cot 2\\theta = \\frac{1}{\\cot\\theta} = \\tan\\theta = \\cot\\left(\\frac{\\pi}{2} - \\theta\\right)$\n\n"
        "১. সাধারণ সমাধান সূত্র:\n"
        "$2\\theta = n\\pi + \\left(\\frac{\\pi}{2} - \\theta\\right) \\implies 3\\theta = n\\pi + \\frac{\\pi}{2} \\implies \\theta = \\frac{n\\pi}{3} + \\frac{\\pi}{6}, n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর পূর্ণমান বসিয়ে $0 < \\theta < \\frac{\\pi}{2}$ ব্যবধিতে মান বের করি:\n"
        "• $n = 0$ হলে, $\\theta = 0 + \\frac{\\pi}{6} = \\frac{\\pi}{6} \\in \\left(0, \\frac{\\pi}{2}\\right)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = \\frac{\\pi}{3} + \\frac{\\pi}{6} = \\frac{\\pi}{2} \\notin \\left(0, \\frac{\\pi}{2}\\right)$ (খোলা ব্যবধির প্রান্তসীমা হওয়ায় গ্রহণযোগ্য নয় ✗)\n"
        "• $n = -1$ হলে, $\\theta = -\\frac{\\pi}{3} + \\frac{\\pi}{6} = -\\frac{n\\pi}{6} < 0$ (ব্যবধির বাইরে ✗)\n\n"
        "অতএব, প্রদত্ত ব্যবধিতে সমাধান: $\\theta = \\frac{\\pi}{6}$।"
    ),

    708: (
        "$\\sin\\left(\\frac{\\pi}{2}\\cos\\alpha\\right) = \\cos\\left(\\frac{\\pi}{2}\\sin\\alpha\\right) = \\sin\\left(\\frac{\\pi}{2} - \\frac{\\pi}{2}\\sin\\alpha\\right)$\n\n"
        "১. সাধারণ সমাধান সূত্র:\n"
        "$\\frac{\\pi}{2}\\cos\\alpha = n\\pi + (-1)^n \\left(\\frac{\\pi}{2} - \\frac{\\pi}{2}\\sin\\alpha\\right)$\n"
        "$n=0$ বসালে:\n"
        "$\\frac{\\pi}{2}\\cos\\alpha = \\frac{\\pi}{2}(1 - \\sin\\alpha) \\implies \\cos\\alpha + \\sin\\alpha = 1$\n\n"
        "২. সমীকরণটি সমাধান করি:\n"
        "$\\frac{1}{\\sqrt{2}}\\cos\\alpha + \\frac{1}{\\sqrt{2}}\\sin\\alpha = \\frac{1}{\\sqrt{2}} \\implies \\cos\\left(\\alpha - \\frac{\\pi}{4}\\right) = \\cos\\frac{\\pi}{4}$\n"
        "$\\alpha - \\frac{\\pi}{4} = 2k\\pi \\pm \\frac{\\pi}{4}$\n"
        "• $k = 0$ হলে:\n"
        "  - ধনাত্মক নিয়ে: $\\alpha = \\frac{\\pi}{4} + \\frac{\\pi}{4} = \\frac{\\pi}{2}$\n"
        "  - ঋণাত্মক নিয়ে: $\\alpha = \\frac{\\pi}{4} - \\frac{\\pi}{4} = 0$\n\n"
        "অতএব, $\\alpha$-এর মান: $0, \\frac{\\pi}{2}$।"
    ),

    709: (
        "$\\tan\\theta + \\cot\\theta = 2$\n"
        "বা, $\\tan\\theta + \\frac{1}{\\tan\\theta} = 2 \\implies \\tan^2\\theta - 2\\tan\\theta + 1 = 0 \\implies (\\tan\\theta - 1)^2 = 0$\n"
        "বা, $\\tan\\theta = 1 = \\tan\\frac{\\pi}{4}$\n\n"
        "১. সাধারণ সমাধান সূত্র: $\\theta = n\\pi + \\frac{\\pi}{4}, n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর মান বসিয়ে $0 < \\theta < \\frac{\\pi}{2}$ ব্যবধিতে যাচাই:\n"
        "• $n = 0$ হলে, $\\theta = 0 + \\frac{\\pi}{4} = \\frac{\\pi}{4} \\in \\left(0, \\frac{\\pi}{2}\\right)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = \\pi + \\frac{\\pi}{4} = \\frac{5\\pi}{4} > \\frac{\\pi}{2}$ (ব্যবধির বাইরে ✗)\n\n"
        "অতএব, $0 < \\theta < \\frac{\\pi}{2}$ ব্যবধিতে সমাধান: $\\theta = \\frac{\\pi}{4}$।"
    ),

    711: (
        "$2\\cos^2\\theta + \\sin\\theta = 1, 0 \\leq \\theta \\leq 2\\pi$\n"
        "বা, $2(1 - \\sin^2\\theta) + \\sin\\theta - 1 = 0$\n"
        "বা, $2 - 2\\sin^2\\theta + \\sin\\theta - 1 = 0$\n"
        "বা, $2\\sin^2\\theta - \\sin\\theta - 1 = 0$\n"
        "বা, $(2\\sin\\theta + 1)(\\sin\\theta - 1) = 0$\n\n"
        "১. $\\sin\\theta = -\\frac{1}{2} = \\sin\\left(-\\frac{\\pi}{6}\\right)$ হলে সাধারণ সমাধান: $\\theta = n\\pi + (-1)^n\\left(-\\frac{\\pi}{6}\\right), n \\in \\mathbb{Z}$\n"
        "• $n = 1$ হলে, $\\theta = \\pi + \\frac{\\pi}{6} = \\frac{7\\pi}{6} \\in [0, 2\\pi]$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 2$ হলে, $\\theta = 2\\pi - \\frac{\\pi}{6} = \\frac{11\\pi}{6} \\in [0, 2\\pi]$ (গ্রহণযোগ্য ✓)\n\n"
        "২. $\\sin\\theta = 1 = \\sin\\frac{\\pi}{2}$ হলে সাধারণ সমাধান: $\\theta = 2n\\pi + \\frac{\\pi}{2}$\n"
        "• $n = 0$ হলে, $\\theta = \\frac{\\pi}{2} \\in [0, 2\\pi]$\n\n"
        "অপশনে প্রদত্ত বিকল্পগুলোর মধ্যে $\\frac{7\\pi}{6}$ রয়েছে। অতএব সঠিক উত্তর: $\\frac{7\\pi}{6}$।"
    ),

    721: (
        "$\\tan\\theta = \\cot\\theta$\n"
        "বা, $\\tan\\theta = \\frac{1}{\\tan\\theta} \\implies \\tan^2\\theta = 1$\n"
        "যেহেতু $0 < \\theta < \\frac{\\pi}{2}$, তাই $\\tan\\theta = 1 = \\tan\\frac{\\pi}{4}$\n\n"
        "১. সাধারণ সমাধান সূত্র: $\\theta = n\\pi + \\frac{\\pi}{4}, n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর পূর্ণমান বসিয়ে:\n"
        "• $n = 0$ হলে, $\\theta = \\frac{\\pi}{4} \\in \\left(0, \\frac{\\pi}{2}\\right)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = \\frac{5\\pi}{4} > \\frac{\\pi}{2}$ (ব্যবধির বাইরে ✗)\n\n"
        "অতএব, $0 < \\theta < \\frac{\\pi}{2}$ ব্যবধিতে $\\theta = \\frac{\\pi}{4}$।"
    ),

    724: (
        "$2(1 - \\sin^2\\theta) + 2\\sqrt{2}\\sin\\theta = 3$\n"
        "বা, $2 - 2\\sin^2\\theta + 2\\sqrt{2}\\sin\\theta - 3 = 0$\n"
        "বা, $2\\sin^2\\theta - 2\\sqrt{2}\\sin\\theta + 1 = 0$\n"
        "বা, $(\\sqrt{2}\\sin\\theta - 1)^2 = 0 \\implies \\sin\\theta = \\frac{1}{\\sqrt{2}} = \\sin\\frac{\\pi}{4}$\n\n"
        "১. সাধারণ সমাধান সূত্র: $\\theta = n\\pi + (-1)^n \\frac{\\pi}{4}, n \\in \\mathbb{Z}$\n\n"
        "২. $n$-এর পূর্ণমান বসিয়ে $0 < \\theta < \\frac{\\pi}{2}$ ব্যবধিতে মান যাচাই:\n"
        "• $n = 0$ হলে, $\\theta = 0 + (-1)^0\\frac{\\pi}{4} = \\frac{\\pi}{4} \\in \\left(0, \\frac{\\pi}{2}\\right)$ (গ্রহণযোগ্য ✓)\n"
        "• $n = 1$ হলে, $\\theta = \\pi - \\frac{\\pi}{4} = \\frac{3\\pi}{4} > \\frac{\\pi}{2}$ (ব্যবধির বাইরে ✗)\n\n"
        "অতএব, $0 < \\theta < \\frac{\\pi}{2}$ ব্যবধিতে $\\theta = \\frac{\\pi}{4}$।"
    ),

    # ------------------ Creative Questions (CQ) ------------------
    743: (
        "**ক.** $\\cos^{-1}\\left(\\sin\\cos^{-1}\\frac{1}{2}\\right) = \\cos^{-1}\\left(\\sin\\frac{\\pi}{3}\\right) = \\cos^{-1}\\frac{\\sqrt{3}}{2} = \\frac{\\pi}{6}$।\n\n"
        "**খ.** দৃশ্যকল্প-১: $L = 2\\tan^{-1}\\frac{1}{2} + \\tan^{-1}\\frac{3}{4} = \\tan^{-1}\\frac{4}{3} + \\tan^{-1}\\frac{3}{4} = \\frac{\\pi}{2}$।\n\n"
        "**গ.** দৃশ্যকল্প-২: $\\sin 3x + \\cos 2x = 0, 0 \\leq x \\leq 2\\pi$\n"
        "বা, $\\sin 3x = -\\cos 2x = \\sin\\left(2x - \\frac{\\pi}{2}\\right)$\n"
        "১. সাধারণ সমাধান:\n"
        "$3x = n\\pi + (-1)^n\\left(2x - \\frac{\\pi}{2}\\right), n \\in \\mathbb{Z}$\n"
        "২. $n$-এর বিভিন্ন মান বসিয়ে $0 \\leq x \\leq 2\\pi$ ব্যবধিতে মান পাই:\n"
        "$x = \\frac{\\pi}{2}, \\frac{3\\pi}{10}, \\frac{7\\pi}{10}, \\frac{11\\pi}{10}, \\frac{15\\pi}{10}, \\frac{19\\pi}{10}$।"
    ),

    744: (
        "**ক.** $\\tan^{-1}\\frac{2}{3} + \\sec^{-1}\\frac{\\sqrt{13}}{2} = \\tan^{-1}\\frac{2}{3} + \\tan^{-1}\\frac{3}{2} = \\frac{\\pi}{2}$।\n\n"
        "**খ.** $2\\{f(\\theta)\\}^2 + 3g(\\theta) = 0 \\implies 2\\sin^2\\theta + 3\\tan\\theta = 0, -\\pi \\leq \\theta \\leq \\pi$\n"
        "বা, $\\sin\\theta\\left(2\\sin\\theta + \\frac{3}{\\cos\\theta}\\right) = 0$\n"
        "১. $\\sin\\theta = 0 \\implies \\theta = n\\pi, n \\in \\mathbb{Z}$\n"
        "• $n = 0 \\implies \\theta = 0 \\in [-\\pi, \\pi]$\n"
        "• $n = 1 \\implies \\theta = \\pi \\in [-\\pi, \\pi]$\n"
        "• $n = -1 \\implies \\theta = -\\pi \\in [-\\pi, \\pi]$\n"
        "২. $2\\sin\\theta\\cos\\theta + 3 = 0 \\implies \\sin 2\\theta = -3$ (অসম্ভব, কারণ $|\sin 2\theta| \\leq 1$)।\n"
        "অতএব, নির্ণেয় সমাধান: $\\theta = -\\pi, 0, \\pi$।"
    ),

    747: (
        "**ক.** রূপান্তর থেকে পাই $\\frac{\\pi}{4}$।\n\n"
        "**খ.** $\\cos^{-1}x + \\cos^{-1}y = \\alpha$ হতে $x^2 - 2xy\\cos\\alpha + y^2 = \\sin^2\\alpha$ প্রমাণিত।\n\n"
        "**গ.** $\\sqrt{3}\\sin\\theta + \\cos\\theta = \\sqrt{2}, 0 \\leq \\theta \\leq 2\\pi$\n"
        "উভয়পক্ষকে ২ দ্বারা ভাগ করে:\n"
        "$\\frac{\\sqrt{3}}{2}\\sin\\theta + \\frac{1}{2}\\cos\\theta = \\frac{\\sqrt{2}}{2} \\implies \\cos\\left(\\theta - \\frac{\\pi}{3}\\right) = \\frac{1}{\\sqrt{2}} = \\cos\\frac{\\pi}{4}$\n"
        "১. সাধারণ সমাধান: $\\theta - \\frac{\\pi}{3} = 2n\\pi \\pm \\frac{\\pi}{4} \\implies \\theta = 2n\\pi + \\frac{\\pi}{3} \\pm \\frac{\\pi}{4}, n \\in \\mathbb{Z}$\n"
        "২. $n$-এর মান বসিয়ে $0 \\leq \\theta \\leq 2\\pi$ ব্যবধিতে পাই:\n"
        "• $n = 0 \\implies \\theta = \\frac{\\pi}{3} + \\frac{\\pi}{4} = \\frac{7\\pi}{12}$ এবং $\\theta = \\frac{\\pi}{3} - \\frac{\\pi}{4} = \\frac{\\pi}{12}$\n"
        "• $n = 1 \\implies \\theta = 2\\pi + \\frac{\\pi}{3} - \\frac{\\pi}{4} = \\frac{25\\pi}{12} > 2\\pi$ (ব্যবধির বাইরে)\n"
        "অতএব, নির্ণেয় সমাধান: $\\theta = \\frac{\\pi}{12}, \\frac{7\\pi}{12}$।"
    ),

    750: (
        "**ক.** $\\frac{1}{2}\\cos^{-1}x = \\cos^{-1}\\sqrt{\\frac{1+x}{2}}$ প্রমাণিত।\n\n"
        "**খ.** $\\cos 3\\theta + \\cos 2\\theta = \\sin 3\\theta + \\sin 2\\theta, 0 \\leq \\theta \\leq \\pi$\n"
        "বা, $2\\cos\\frac{5\\theta}{2}\\cos\\frac{\\theta}{2} = 2\\sin\\frac{5\\theta}{2}\\cos\\frac{\\theta}{2}$\n"
        "বা, $\\cos\\frac{\\theta}{2}\\left(\\sin\\frac{5\\theta}{2} - \\cos\\frac{5\\theta}{2}\\right) = 0$\n"
        "১. $\\cos\\frac{\\theta}{2} = 0 \\implies \\frac{\\theta}{2} = (2n+1)\\frac{\\pi}{2} \\implies \\theta = (2n+1)\\pi$\n"
        "• $n = 0 \\implies \\theta = \\pi \\in [0, \\pi]$\n"
        "২. $\\tan\\frac{5\\theta}{2} = 1 = \\tan\\frac{\\pi}{4} \\implies \\frac{5\\theta}{2} = n\\pi + \\frac{\\pi}{4} \\implies \\theta = \\frac{2n\\pi}{5} + \\frac{\\pi}{10}$\n"
        "• $n = 0 \\implies \\theta = \\frac{\\pi}{10} \\in [0, \\pi]$\n"
        "• $n = 1 \\implies \\theta = \\frac{2\\pi}{5} + \\frac{\\pi}{10} = \\frac{\\pi}{2} \\in [0, \\pi]$\n"
        "• $n = 2 \\implies \\theta = \\frac{4\\pi}{5} + \\frac{\\pi}{10} = \\frac{9\\pi}{10} \\in [0, \\pi]$\n"
        "অতএব, $0 \\leq \\theta \\leq \\pi$ ব্যবধিতে সমাধান: $\\theta = \\frac{\\pi}{10}, \\frac{\\pi}{2}, \\frac{9\\pi}{10}, \\pi$।"
    ),

    779: (
        "**ক.** $\\tan^2\\theta + \\cot^2\\theta = 2, 0 \\leq \\theta \\leq 2\\pi$\n"
        "বা, $(\\tan\\theta - \\cot\\theta)^2 + 2 = 2 \\implies \\tan\\theta = \\cot\\theta = \\pm 1$\n"
        "১. $\\tan\\theta = 1 = \\tan\\frac{\\pi}{4} \\implies \\theta = n\\pi + \\frac{\\pi}{4}, n \\in \\mathbb{Z}$\n"
        "• $n = 0 \\implies \\theta = \\frac{\\pi}{4} \\in [0, 2\\pi]$\n"
        "• $n = 1 \\implies \\theta = \\frac{5\\pi}{4} \\in [0, 2\\pi]$\n"
        "২. $\\tan\\theta = -1 = \\tan\\left(-\\frac{\\pi}{4}\\right) \\implies \\theta = n\\pi - \\frac{\\pi}{4}, n \\in \\mathbb{Z}$\n"
        "• $n = 1 \\implies \\theta = \\frac{3\\pi}{4} \\in [0, 2\\pi]$\n"
        "• $n = 2 \\implies \\theta = \\frac{7\\pi}{4} \\in [0, 2\\pi]$\n"
        "অতএব, নির্ণেয় সমাধান: $\\theta = \\frac{\\pi}{4}, \\frac{3\\pi}{4}, \\frac{5\\pi}{4}, \\frac{7\\pi}{4}$।"
    ),

    783: (
        "**ক.** $2(\\cos^2 x - \\sin^2 x) = \\sqrt{3}, 0 \\leq x \\leq 2\\pi$\n"
        "বা, $2\\cos 2x = \\sqrt{3} \\implies \\cos 2x = \\frac{\\sqrt{3}}{2} = \\cos\\frac{\\pi}{6}$\n"
        "১. সাধারণ সমাধান: $2x = 2n\\pi \\pm \\frac{\\pi}{6} \\implies x = n\\pi \\pm \\frac{\\pi}{12}, n \\in \\mathbb{Z}$\n"
        "২. $n$-এর মান বসিয়ে $0 \\leq x \\leq 2\\pi$ ব্যবধিতে মানসমূহ:\n"
        "• $n = 0 \\implies x = \\frac{\\pi}{12}$\n"
        "• $n = 1 \\implies x = \\pi - \\frac{\\pi}{12} = \\frac{11\\pi}{12}$ এবং $x = \\pi + \\frac{\\pi}{12} = \\frac{13\\pi}{12}$\n"
        "• $n = 2 \\implies x = 2\\pi - \\frac{\\pi}{12} = \\frac{23\\pi}{12}$\n"
        "অতএব, নির্ণেয় সমাধান: $x = \\frac{\\pi}{12}, \\frac{11\\pi}{12}, \\frac{13\\pi}{12}, \\frac{23\\pi}{12}$।"
    ),

    787: (
        "**ক.** $\\tan 2x\\tan x = 1, 0 < x < \\pi$\n"
        "বা, $\\tan 2x = \\cot x = \\tan\\left(\\frac{\\pi}{2} - x\\right)$\n"
        "১. সাধারণ সমাধান: $2x = n\\pi + \\frac{\\pi}{2} - x \\implies 3x = n\\pi + \\frac{\\pi}{2} \\implies x = \\frac{n\\pi}{3} + \\frac{\\pi}{6}, n \\in \\mathbb{Z}$\n"
        "২. $n$-এর মান বসিয়ে $0 < x < \\pi$ ব্যবধিতে মানসমূহ:\n"
        "• $n = 0 \\implies x = \\frac{\\pi}{6} \\in (0, \\pi)$\n"
        "• $n = 1 \\implies x = \\frac{\\pi}{3} + \\frac{\\pi}{6} = \\frac{\\pi}{2}$ (কিন্তু $\\tan\\frac{\\pi}{2}$ অসংজ্ঞায়িত হওয়ায় বাদ)\n"
        "• $n = 2 \\implies x = \\frac{2\\pi}{3} + \\frac{\\pi}{6} = \\frac{5\\pi}{6} \\in (0, \\pi)$\n"
        "অতএব, গ্রহণযোগ্য সমাধান: $x = \\frac{\\pi}{6}, \\frac{5\\pi}{6}$।"
    ),

    802: (
        "**গ.** $\\sqrt{3}\\cos\\theta + \\sin\\theta = \\sqrt{2}, -\\pi \\leq \\theta \\leq \\pi$\n"
        "উভয়পক্ষকে ২ দ্বারা ভাগ করে পাই:\n"
        "$\\frac{\\sqrt{3}}{2}\\cos\\theta + \\frac{1}{2}\\sin\\theta = \\frac{\\sqrt{2}}{2} \\implies \\cos\\left(\\theta - \\frac{\\pi}{6}\\right) = \\frac{1}{\\sqrt{2}} = \\cos\\frac{\\pi}{4}$\n"
        "১. সাধারণ সমাধান: $\\theta - \\frac{\\pi}{6} = 2n\\pi \\pm \\frac{\\pi}{4} \\implies \\theta = 2n\\pi + \\frac{\\pi}{6} \\pm \\frac{\\pi}{4}, n \\in \\mathbb{Z}$\n"
        "২. $n$-এর বিভিন্ন মান বসিয়ে $[-\\pi, \\pi]$ ব্যবধিতে যাচাই করি:\n"
        "• $n = 0$ হলে: $\\theta = \\frac{\\pi}{6} + \\frac{\\pi}{4} = \\frac{5\\pi}{12} \\in [-\\pi, \\pi]$ এবং $\\theta = \\frac{\\pi}{6} - \\frac{\\pi}{4} = -\\frac{\\pi}{12} \\in [-\\pi, \\pi]$\n"
        "• $n = 1$ হলে: $\\theta = 2\\pi - \\frac{\\pi}{12} = \\frac{23\\pi}{12} > \\pi$ (ব্যবধির বাইরে)\n"
        "• $n = -1$ হলে: $\\theta = -2\\pi + \\frac{5\\pi}{12} = -\\frac{19\\pi}{12} < -\\pi$ (ব্যবধির বাইরে)\n"
        "অতএব, $[-\\pi, \\pi]$ ব্যবধিতে নির্ণেয় সমাধান: $\\theta = -\\frac{\\pi}{12}, \\frac{5\\pi}{12}$।"
    ),

    820: (
        "**গ.** $\\sqrt{3}\\cos x + \\sin x = 1, -2\\pi \\leq x \\leq 2\\pi$\n"
        "উভয়পক্ষকে ২ দিয়ে ভাগ করে:\n"
        "$\\frac{\\sqrt{3}}{2}\\cos x + \\frac{1}{2}\\sin x = \\frac{1}{2} \\implies \\cos\\left(x - \\frac{\\pi}{6}\\right) = \\frac{1}{2} = \\cos\\frac{\\pi}{3}$\n"
        "১. সাধারণ সমাধান: $x - \\frac{\\pi}{6} = 2n\\pi \\pm \\frac{\\pi}{3} \\implies x = 2n\\pi + \\frac{\\pi}{6} \\pm \\frac{\\pi}{3}, n \\in \\mathbb{Z}$\n"
        "২. $n$-এর পূর্ণমান বসিয়ে $[-2\\pi, 2\\pi]$ ব্যবধিতে মান বের করি:\n"
        "• $n = 0 \\implies x = \\frac{\\pi}{6} + \\frac{\\pi}{3} = \\frac{\\pi}{2}$ এবং $x = \\frac{\\pi}{6} - \\frac{\\pi}{3} = -\\frac{\\pi}{6}$\n"
        "• $n = 1 \\implies x = 2\\pi - \\frac{\\pi}{6} = \\frac{11\\pi}{6}$\n"
        "• $n = -1 \\implies x = -2\\pi + \\frac{\\pi}{2} = -\\frac{3\\pi}{2}$\n"
        "অতএব, $[-2\\pi, 2\\pi]$ ব্যবধিতে সমাধান: $x = -\\frac{3\\pi}{2}, -\\frac{\\pi}{6}, \\frac{\\pi}{2}, \\frac{11\\pi}{6}$।"
    ),

    929: (
        "**গ.** $\\sqrt{3}g(x) + g\\left(\\frac{\\pi}{2}-x\\right) = 1 \\implies \\sqrt{3}\\cos x + \\sin x = 1, -2\\pi < x < 2\\pi$\n"
        "উভয়পক্ষকে ২ দ্বারা ভাগ করে:\n"
        "$\\frac{\\sqrt{3}}{2}\\cos x + \\frac{1}{2}\\sin x = \\frac{1}{2} \\implies \\cos\\left(x - \\frac{\\pi}{6}\\right) = \\cos\\frac{\\pi}{3}$\n"
        "১. সাধারণ সমাধান: $x = 2n\\pi + \\frac{\\pi}{6} \\pm \\frac{\\pi}{3}, n \\in \\mathbb{Z}$\n"
        "২. $n$-এর মান বসিয়ে $(-2\\pi, 2\\pi)$ ব্যবধিতে:\n"
        "• $n = 0 \\implies x = \\frac{\\pi}{2}, -\\frac{\\pi}{6}$\n"
        "• $n = 1 \\implies x = \\frac{11\\pi}{6}$\n"
        "• $n = -1 \\implies x = -\\frac{3\\pi}{2}$\n"
        "অতএব, নির্ণেয় সমাধান: $x = -\\frac{3\\pi}{2}, -\\frac{\\pi}{6}, \\frac{\\pi}{2}, \\frac{11\\pi}{6}$।"
    ),

    932: (
        "**গ.** $\\sqrt{3}g(x) + g\\left(\\frac{\\pi}{2}-x\\right) = 1 \\implies \\sqrt{3}\\cos x + \\sin x = 1, -2\\pi < x < 2\\pi$\n"
        "১. সাধারণ সমাধান: $x = 2n\\pi + \\frac{\\pi}{6} \\pm \\frac{\\pi}{3}, n \\in \\mathbb{Z}$\n"
        "২. $n = 0, 1, -1$ বসিয়ে $(-2\\pi, 2\\pi)$ ব্যবধিতে সমাধান:\n"
        "$x = -\\frac{3\\pi}{2}, -\\frac{\\pi}{6}, \\frac{\\pi}{2}, \\frac{11\\pi}{6}$।"
    ),

    934: (
        "**গ.** $\\sqrt{3}g_3(x) - g_3\\left(\\frac{\\pi}{2}-x\\right) = 2 \\implies \\sqrt{3}\\sin x - \\cos x = 2, -2\\pi \\leq x \\leq 2\\pi$\n"
        "উভয়পক্ষকে ২ দ্বারা ভাগ করে:\n"
        "$\\frac{\\sqrt{3}}{2}\\sin x - \\frac{1}{2}\\cos x = 1 \\implies \\sin\\left(x - \\frac{\\pi}{6}\\right) = 1 = \\sin\\frac{\\pi}{2}$\n"
        "১. সাধারণ সমাধান:\n"
        "$x - \\frac{\\pi}{6} = 2n\\pi + \\frac{\\pi}{2} \\implies x = 2n\\pi + \\frac{2\\pi}{3}, n \\in \\mathbb{Z}$\n"
        "২. $n$-এর মান বসিয়ে $[-2\\pi, 2\\pi]$ ব্যবধিতে:\n"
        "• $n = 0 \\implies x = \\frac{2\\pi}{3} \\in [-2\\pi, 2\\pi]$\n"
        "• $n = -1 \\implies x = -2\\pi + \\frac{2\\pi}{3} = -\\frac{4\\pi}{3} \\in [-2\\pi, 2\\pi]$\n"
        "• $n = 1 \\implies x = 2\\pi + \\frac{2\\pi}{3} = \\frac{8\\pi}{3} > 2\\pi$ (ব্যবধির বাইরে)\n"
        "অতএব, $[-2\\pi, 2\\pi]$ ব্যবধিতে নির্ণেয় সমাধান: $x = -\\frac{4\\pi}{3}, \\frac{2\\pi}{3}$।"
    ),

    937: (
        "**গ.** $f(x)\\{1 + 2f(x)\\} + f(3x) - 1 = 0 \\implies \\cos x(1 + 2\\cos x) + \\cos 3x - 1 = 0, -\\pi \\leq x \\leq \\pi$\n"
        "বা, $\\cos x + 2\\cos^2 x + (4\\cos^3 x - 3\\cos x) - 1 = 0$\n"
        "বা, $4\\cos^3 x + 2\\cos^2 x - 2\\cos x - 1 = 0$\n"
        "বা, $2\\cos^2 x(2\\cos x + 1) - 1(2\\cos x + 1) = 0$\n"
        "বা, $(2\\cos x + 1)(2\\cos^2 x - 1) = 0$\n"
        "১. $2\\cos x + 1 = 0 \\implies \\cos x = -\\frac{1}{2} = \\cos\\frac{2\\pi}{3} \\implies x = 2n\\pi \\pm \\frac{2\\pi}{3}$\n"
        "• $n = 0 \\implies x = \\pm\\frac{2\\pi}{3} \\in [-\\pi, \\pi]$\n"
        "২. $2\\cos^2 x - 1 = 0 \\implies \\cos 2x = 0 = \\cos\\frac{\\pi}{2} \\implies 2x = 2n\\pi \\pm \\frac{\\pi}{2} \\implies x = n\\pi \\pm \\frac{\\pi}{4}$\n"
        "• $n = 0 \\implies x = \\pm\\frac{\\pi}{4} \\in [-\\pi, \\pi]$\n"
        "• $n = 1 \\implies x = \\pi - \\frac{\\pi}{4} = \\frac{3\\pi}{4} \\in [-\\pi, \\pi]$\n"
        "• $n = -1 \\implies x = -\\pi + \\frac{\\pi}{4} = -\\frac{3\\pi}{4} \\in [-\\pi, \\pi]$\n"
        "অতএব, $[-\\pi, \\pi]$ ব্যবধিতে নির্ণেয় সমাধান: $x = \\pm\\frac{\\pi}{4}, \\pm\\frac{3\\pi}{4}, \\pm\\frac{2\\pi}{3}$।"
    ),

    941: (
        "**গ.** $2f(y)f(3y) = 1 \\implies 2\\sin y\\sin 3y = 1, 0 \\leq y \\leq 2\\pi$\n"
        "বা, $\\cos(3y - y) - \\cos(3y + y) = 1 \\implies \\cos 2y - \\cos 4y = 1$\n"
        "বা, $\\cos 2y - (2\\cos^2 2y - 1) = 1 \\implies 2\\cos^2 2y - \\cos 2y = 0$\n"
        "বা, $\\cos 2y(2\\cos 2y - 1) = 0$\n"
        "১. $\\cos 2y = 0 \\implies 2y = (2n+1)\\frac{\\pi}{2} \\implies y = (2n+1)\\frac{\\pi}{4}$\n"
        "• $n = 0, 1, 2, 3 \\implies y = \\frac{\\pi}{4}, \\frac{3\\pi}{4}, \\frac{5\\pi}{4}, \\frac{7\\pi}{4} \\in [0, 2\\pi]$\n"
        "২. $\\cos 2y = \\frac{1}{2} = \\cos\\frac{\\pi}{3} \\implies 2y = 2n\\pi \\pm \\frac{\\pi}{3} \\implies y = n\\pi \\pm \\frac{\\pi}{6}$\n"
        "• $n = 0 \\implies y = \\frac{\\pi}{6}$\n"
        "• $n = 1 \\implies y = \\frac{5\\pi}{6}, \\frac{7\\pi}{6}$\n"
        "• $n = 2 \\implies y = \\frac{11\\pi}{6}$\n"
        "অতএব, $0 \\leq y \\leq 2\\pi$ ব্যবধিতে সমাধান: $y = \\frac{\\pi}{6}, \\frac{\\pi}{4}, \\frac{3\\pi}{4}, \\frac{5\\pi}{6}, \\frac{7\\pi}{6}, \\frac{5\\pi}{4}, \\frac{7\\pi}{4}, \\frac{11\\pi}{6}$।"
    )
}
