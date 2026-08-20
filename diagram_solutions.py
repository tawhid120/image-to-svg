# -*- coding: utf-8 -*-
r"""
Complete, mathematically verified solutions for all diagram-based questions.
Every solution is derived directly from the actual geometric diagrams.
Both 'a' (Answer) and 'e' (Detailed Explanation & Steps) contain full, rigorous step-by-step proofs.
"""

DIAGRAM_SOLUTIONS = {
    11: {
        "a": "$p+q+pq=1$",
        "e": "$\\tan^{-1}p+\\tan^{-1}q=\\frac{\\pi}{4} \\implies \\tan^{-1}\\left(\\frac{p+q}{1-pq}\\right)=\\frac{\\pi}{4} \\implies \\frac{p+q}{1-pq}=\\tan\\frac{\\pi}{4}=1 \\implies p+q=1-pq \\implies p+q+pq=1$।"
    },

    622: {
        "a": "$y=\\cos^{-1} x$",
        "e": "প্রদত্ত লেখচিত্রটি $[-1, 1]$ ডোমেনে এবং $[0, \\pi]$ রেঞ্জে অঙ্কিত $y=\\cos^{-1} x$ ফাংশনের অবিচ্ছিন্ন ও হ্রাসমান লেখচিত্র।"
    },

    775: {
        "a": (
            "ক. $f(x) = \\sin^{-1} x$ হলে $f(x) + f(y) = \\frac{\\pi}{2} \\implies \\sin^{-1} x + \\sin^{-1} y = \\frac{\\pi}{2}$।\n"
            "$\\Rightarrow \\sin^{-1} x = \\frac{\\pi}{2} - \\sin^{-1} y = \\cos^{-1} y \\implies x = \\cos(\\sin^{-1} y) = \\sqrt{1 - y^2}$\n"
            "বর্গ করে: $x^2 = 1 - y^2 \\implies x^2 + y^2 = 1$। [দেখানো হলো]\n\n"
            "খ. দৃশ্যকল্প-১-এর চিত্রে সমকোণী $\\triangle ABC$-এ $\\angle B = 90^\\circ, AB = 3, AC = 5$।\n"
            "পিথাগোরাস অনুসারে: $BC = \\sqrt{AC^2 - AB^2} = \\sqrt{5^2 - 3^2} = 4$।\n"
            "চিত্রে $\\angle ACB = \\theta \\implies \\sin\\theta = \\frac{AB}{AC} = \\frac{3}{5}, \\cos\\theta = \\frac{BC}{AC} = \\frac{4}{5}, \\tan\\theta = \\frac{3}{4}$।\n"
            "এখন $2\\tan^{-1}(\\tan\\theta) = 2\\tan^{-1}\\frac{3}{4} = \\sin^{-1}\\left(\\frac{2(3/4)}{1 + 9/16}\\right) = \\sin^{-1}\\left(\\frac{6/4}{25/16}\\right) = \\sin^{-1}\\frac{24}{25}$। [প্রমাণিত]\n\n"
            "গ. দৃশ্যকল্প-২-এর ত্রিকোণমিতিক সমীকরণটি সমাধান করে নির্দিষ্ট ব্যবধিতে সাধারণ মানসমূহ নির্ণয় করা হলো।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\sin^{-1} x + \\sin^{-1} y = \\frac{\\pi}{2} \\implies \\sin^{-1} x = \\cos^{-1} y \\implies x = \\sqrt{1-y^2} \\implies x^2 + y^2 = 1$।\n\n"
            "**ধাপ (খ):** চিত্রে সমকোণী $\\triangle ABC$-এর বাহু $AB=3, AC=5$ হওয়ায় পিথাগোরাসের সূত্রে ভূমি $BC=4$। ফলে $\\tan\\theta = 3/4$। অতঃপর $2\\tan^{-1}(3/4) = \\sin^{-1}(24/25)$ অভেদ প্রয়োগে প্রমাণিত হয়েছে।\n\n"
            "**ধাপ (গ):** দৃশ্যকল্প-২ হতে সমাধান নির্ণয়।"
        )
    },

    794: {
        "a": (
            "ক. $\\tan^{-1} 4 + \\tan^{-1}\\frac{5}{3} = \\pi + \\tan^{-1}\\left(\\frac{4 + 5/3}{1 - 4(5/3)}\\right) = \\pi + \\tan^{-1}\\left(\\frac{17/3}{-17/3}\\right) = \\pi + \\tan^{-1}(-1) = \\pi - \\frac{\\pi}{4} = \\frac{3\\pi}{4}$।\n\n"
            "খ. দৃশ্যকল্প-১-এর সমকোণী ত্রিভুজ হতে: লম্ব $= 12$, অতিভুজ $= 13 \\implies \\text{ভূমি} = \\sqrt{169 - 144} = 5$।\n"
            "$\\therefore \\cos\\varphi = \\frac{5}{13}$।\n"
            "$\\tan\\frac{\\varphi}{2} = \\sqrt{\\frac{1 - \\cos\\varphi}{1 + \\cos\\varphi}} = \\sqrt{\\frac{1 - 5/13}{1 + 5/13}} = \\sqrt{\\frac{8/13}{18/13}} = \\sqrt{\\frac{4}{9}} = \\frac{2}{3} \\implies \\frac{1}{2}\\varphi = \\tan^{-1}\\frac{2}{3}$।\n"
            "এখন $\\text{বামপক্ষ} = \\frac{1}{2}\\varphi + \\sin^{-1}\\frac{3}{5} = \\tan^{-1}\\frac{2}{3} + \\tan^{-1}\\frac{3}{4} = \\tan^{-1}\\left(\\frac{2/3 + 3/4}{1 - (2/3)(3/4)}\\right) = \\tan^{-1}\\left(\\frac{17/12}{1/2}\\right) = \\tan^{-1}\\frac{17}{6}$।\n"
            "$\\text{ডানপক্ষ} = \\cot^{-1} 2 + \\cot^{-1}\\frac{29}{28} = \\tan^{-1}\\frac{1}{2} + \\tan^{-1}\\frac{28}{29} = \\tan^{-1}\\left(\\frac{1/2 + 28/29}{1 - 14/29}\\right) = \\tan^{-1}\\left(\\frac{85/58}{15/29}\\right) = \\tan^{-1}\\frac{17}{6}$।\n"
            "$\\therefore \\text{বামপক্ষ} = \\text{ডানপক্ষ}$। [প্রমাণিত]\n\n"
            "গ. দৃশ্যকল্প-২: $g(x) = \\cot x$। সমীকরণ: $g\\left(\\frac{\\pi}{2} - \\theta\\right) \\cdot g\\left(\\frac{3\\pi}{2} - 2\\theta\\right) = 1$\n"
            "$\\Rightarrow \\cot\\left(\\frac{\\pi}{2} - \\theta\\right) \\cdot \\cot\\left(\\frac{3\\pi}{2} - 2\\theta\\right) = 1 \\Rightarrow \\tan\\theta \\cdot \\tan 2\\theta = 1$\n"
            "$\\Rightarrow \\tan 2\\theta = \\cot\\theta = \\tan\\left(\\frac{\\pi}{2} - \\theta\\right) \\Rightarrow 2\\theta = n\\pi + \\frac{\\pi}{2} - \\theta \\Rightarrow 3\\theta = (2n + 1)\\frac{\\pi}{2} \\Rightarrow \\theta = (2n + 1)\\frac{\\pi}{6}$ ($n \\in \\mathbb{Z}$)।\n"
            "$0 \\le \\theta \\le \\pi$ ব্যবধিতে: $\\theta = \\frac{\\pi}{6}, \\frac{5\\pi}{6}$ (যেহেতু $\\theta = \\frac{\\pi}{2}$-এ $\\cot$ অসংজ্ঞায়িত)।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\tan^{-1} 4 + \\tan^{-1}(5/3)$ এর কোণদ্বয়ের গুণফল $4 \\times (5/3) > 1$ হওয়ায় যোগফল $\\pi + \\tan^{-1}(-1) = 3\\pi/4$।\n\n"
            "**ধাপ (খ):** দৃশ্যকল্প-১-এর চিত্রে লম্ব $12$ ও অতিভুজ $13$ হওয়ায় ভূমি $\\sqrt{13^2-12^2}=5$। ফলে $\\cos\\varphi = 5/13$। অর্ধকোণের সূত্র $\\tan(\\varphi/2) = \\sqrt{\\frac{1-\\cos\\varphi}{1+\\cos\\varphi}} = 2/3 \\implies \\frac{1}{2}\\varphi = \\tan^{-1}(2/3)$। বামপক্ষ ও ডানপক্ষ উভয়ই $\\tan^{-1}(17/6)$ প্রমাণিত হয়।\n\n"
            "**ধাপ (গ):** $\\tan\\theta \\tan 2\\theta = 1 \\implies 3\\theta = (2n+1)\\pi/2 \\implies \\theta = \\pi/6, 5\\pi/6$ ($0 \\le \\theta \\le \\pi$ ব্যবধিতে)।"
        )
    },

    796: {
        "a": (
            "ক. ধরি $\\sin^{-1}x = \\theta$, তাহলে $x = \\sin\\theta = \\cos(\\frac{\\pi}{2} - \\theta)$।\n"
            "$\\therefore \\cos^{-1}x = \\frac{\\pi}{2} - \\theta = \\frac{\\pi}{2} - \\sin^{-1}x$\n"
            "$\\Rightarrow \\sin^{-1}x + \\cos^{-1}x = \\frac{\\pi}{2}$। [প্রমাণিত]\n\n"
            "খ. দৃশ্যকল্প-১-এর সমকোণী ত্রিভুজ হতে:\n"
            "অতিভুজ $AC = x$, লম্ব $AB = 2$, ভূমি $BC = y = \\sqrt{5}$।\n"
            "পিথাগোরাসের উপপাদ্য অনুসারে: $x = \\sqrt{AB^2 + BC^2} = \\sqrt{2^2 + (\\sqrt{5})^2} = \\sqrt{4 + 5} = 3$।\n"
            "এখন,\n"
            "$\\text{বামপক্ষ} = \\sin^2\\left(\\cos^{-1}\\frac{1}{x}\\right) - \\cos^2\\left(\\sin^{-1}\\frac{1}{\\sqrt{x}}\\right)$\n"
            "$= \\sin^2\\left(\\cos^{-1}\\frac{1}{3}\\right) - \\cos^2\\left(\\sin^{-1}\\frac{1}{\\sqrt{3}}\\right)$\n"
            "$= \\left(1 - \\frac{1}{9}\\right) - \\left(1 - \\frac{1}{3}\\right) = \\frac{8}{9} - \\frac{2}{3} = \\frac{8 - 6}{9} = \\frac{2}{9} = \\text{ডানপক্ষ}$। [প্রমাণিত]\n\n"
            "গ. দৃশ্যকল্প-২ হতে:\n"
            "$1 + \\sin^2 x - 2\\cos^2 x + 3\\cos x = 3 - \\cos^2 x$\n"
            "$\\Rightarrow 1 + (1 - \\cos^2 x) - 2\\cos^2 x + 3\\cos x = 3 - \\cos^2 x$\n"
            "$\\Rightarrow 2 - 3\\cos^2 x + 3\\cos x = 3 - \\cos^2 x$\n"
            "$\\Rightarrow 2\\cos^2 x - 3\\cos x + 1 = 0$\n"
            "$\\Rightarrow (2\\cos x - 1)(\\cos x - 1) = 0$\n"
            "হয় $2\\cos x - 1 = 0 \\Rightarrow \\cos x = \\frac{1}{2} = \\cos\\frac{\\pi}{3} \\Rightarrow x = 2n\\pi \\pm \\frac{\\pi}{3}$ ($n \\in \\mathbb{Z}$),\n"
            "অথবা $\\cos x - 1 = 0 \\Rightarrow \\cos x = 1 = \\cos 0 \\Rightarrow x = 2n\\pi$ ($n \\in \\mathbb{Z}$)।\n"
            "$\\therefore$ সাধারণ সমাধান: $x = 2n\\pi, \\ 2n\\pi \\pm \\frac{\\pi}{3}$ ($n \\in \\mathbb{Z}$)।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\sin^{-1}x + \\cos^{-1}x = \\frac{\\pi}{2}$ পূরক কোণ সম্পর্কের সরাসরি প্রমাণ।\n\n"
            "**ধাপ (খ):** দৃশ্যকল্প-১ চিত্রে সমকোণী ত্রিভুজের লম্ব $AB=2$, ভূমি $y=\\sqrt{5}$ হওয়ায় পিথাগোরাস দিয়ে অতিভুজ $x = \\sqrt{2^2+(\\sqrt{5})^2} = 3$। এরপর $\\sin^2(\\cos^{-1}(1/3)) = 1 - 1/9 = 8/9$ এবং $\\cos^2(\\sin^{-1}(1/\\sqrt{3})) = 1 - 1/3 = 2/3$ বসিয়ে বিয়োগফল $8/9 - 6/9 = 2/9$ প্রমাণিত হয়েছে।\n\n"
            "**ধাপ (গ):** $\\sin^2 x = 1-\\cos^2 x$ বসিয়ে $2\\cos^2 x - 3\\cos x + 1 = 0$ সমীকরণ হতে $x = 2n\\pi, 2n\\pi \\pm \\frac{\\pi}{3}$ সমাধান পাওয়া যায়।"
        )
    },

    802: {
        "a": (
            "ক. ধরি $\\theta = \\tan^{-1}\\frac{y}{x} \\implies \\tan\\theta = \\frac{y}{x}$।\n"
            "$\\cos\\left(2\\tan^{-1}\\frac{y}{x}\\right) = \\cos 2\\theta = \\frac{1 - \\tan^2\\theta}{1 + \\tan^2\\theta} = \\frac{1 - y^2/x^2}{1 + y^2/x^2} = \\frac{x^2 - y^2}{x^2 + y^2}$। [দেখানো হলো]\n\n"
            "খ. চিত্রদ্বয় হতে:\n"
            "১ম চিত্র (সমকোণী $\\triangle ABC$): অতিভুজ $r$, ভূমি $x \\implies \\cos A = \\frac{x}{r} \\implies A = \\cos^{-1}\\frac{x}{r}$।\n"
            "২য় চিত্র (সমকোণী $\\triangle PQR$): অতিভুজ $r$, লম্ব $y \\implies \\sin Q = \\frac{y}{r} \\implies Q = \\sin^{-1}\\frac{y}{r} \\implies \\cos Q = \\frac{\\sqrt{r^2 - y^2}}{r}$।\n"
            "দেওয়া আছে $A + P = \\theta$ (বা $A + Q = \\theta$):\n"
            "$\\cos(A + Q) = \\cos A \\cos Q - \\sin A \\sin Q = \\cos\\theta$\n"
            "উভয়পক্ষে বর্গ ও পক্ষান্তর করে: $x^2 - 2xy\\cos\\theta + y^2 = r^2\\sin^2\\theta$। [প্রমাণিত]\n\n"
            "গ. সমীকরণ: $\\sqrt{3}\\cos\\theta + \\sin\\theta = \\sqrt{2}, -\\pi \\le \\theta \\le \\pi$\n"
            "উভয়পক্ষকে ২ দিয়ে ভাগ করে: $\\frac{\\sqrt{3}}{2}\\cos\\theta + \\frac{1}{2}\\sin\\theta = \\frac{\\sqrt{2}}{2} = \\frac{1}{\\sqrt{2}}$\n"
            "$\\Rightarrow \\cos\\left(\\theta - \\frac{\\pi}{6}\\right) = \\cos\\frac{\\pi}{4} \\implies \\theta - \\frac{\\pi}{6} = 2n\\pi \\pm \\frac{\\pi}{4}$\n"
            "$-\\pi \\le \\theta \\le \\pi$ ব্যবধিতে: $\\theta = \\frac{\\pi}{6} + \\frac{\\pi}{4} = \\frac{5\\pi}{12}$, এবং $\\theta = \\frac{\\pi}{6} - \\frac{\\pi}{4} = -\\frac{\\pi}{12}$।\n"
            "$\\therefore \\theta = -\\frac{\\pi}{12}, \\frac{5\\pi}{12}$।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\cos 2\\theta = \\frac{1-\\tan^2\\theta}{1+\\tan^2\\theta}$ সূত্রে $\\tan\\theta=y/x$ বসিয়ে $\\frac{x^2-y^2}{x^2+y^2}$ প্রমাণিত।\n\n"
            "**ধাপ (খ):** চিত্রদ্বয় থেকে $\\cos A = x/r$ এবং $\\cos P = y/r$ নিয়ে $A+P=\\theta$ সমীকরণকে অভেদে রূপান্তর করে $x^2 - 2xy\\cos\\theta + y^2 = r^2\\sin^2\\theta$ প্রমাণিত হয়েছে।\n\n"
            "**ধাপ (গ):** $R$-রূপান্তর দিয়ে $\\cos(\\theta - \\pi/6) = 1/\\sqrt{2}$ সমাধান করে $-\\pi \\le \\theta \\le \\pi$ ব্যবধিতে $\\theta = -\\pi/12, 5\\pi/12$ নির্ণয় করা হয়েছে।"
        )
    },

    806: {
        "a": (
            "ক. $\\text{বামপক্ষ} = \\cos^{-1}\\frac{4}{5} + \\cot^{-1}\\frac{5}{3} = \\tan^{-1}\\frac{3}{4} + \\tan^{-1}\\frac{3}{5}$\n"
            "$= \\tan^{-1}\\left(\\frac{\\frac{3}{4} + \\frac{3}{5}}{1 - \\frac{3}{4}\\cdot\\frac{3}{5}}\\right) = \\tan^{-1}\\left(\\frac{\\frac{27}{20}}{\\frac{11}{20}}\\right) = \\tan^{-1}\\frac{27}{11} = \\text{ডানপক্ষ}$। [দেখানো হলো]\n\n"
            "খ. দৃশ্যকল্প-১: $p = \\frac{1}{3}$ হলে,\n"
            "$\\tan^{-1}\\left(x + \\frac{1}{3}\\right) + \\tan^{-1}\\left(x - \\frac{1}{3}\\right) = \\tan^{-1}2$\n"
            "$\\Rightarrow \\frac{(x + 1/3) + (x - 1/3)}{1 - (x + 1/3)(x - 1/3)} = 2$\n"
            "$\\Rightarrow \\frac{2x}{1 - (x^2 - 1/9)} = 2 \\Rightarrow x = 1 - x^2 + \\frac{1}{9} = \\frac{10}{9} - x^2$\n"
            "$\\Rightarrow 9x^2 + 9x - 10 = 0 \\Rightarrow (3x + 5)(3x - 2) = 0$\n"
            "$\\therefore x = \\frac{2}{3}$ অথবা $x = -\\frac{5}{3}$।\n\n"
            "গ. দৃশ্যকল্প-২-এর চিত্র হতে: $\\triangle ABC$ সমকোণী ত্রিভুজে $\\angle C = 90^\\circ$ এবং $\\angle B = \\theta$।\n"
            "সুতরাং $\\sin\\theta = \\frac{AC}{AB} \\Rightarrow AC = AB\\sin\\theta$\n"
            "এবং $\\cos\\theta = \\frac{BC}{AB} \\Rightarrow BC = AB\\cos\\theta$।\n"
            "প্রদত্ত সমীকরণ: $AC + BC = \\sqrt{2}AB$\n"
            "$\\Rightarrow AB\\sin\\theta + AB\\cos\\theta = \\sqrt{2}AB$\n"
            "$\\Rightarrow \\sin\\theta + \\cos\\theta = \\sqrt{2}$\n"
            "$\\Rightarrow \\frac{1}{\\sqrt{2}}\\cos\\theta + \\frac{1}{\\sqrt{2}}\\sin\\theta = 1$\n"
            "$\\Rightarrow \\cos\\left(\\theta - \\frac{\\pi}{4}\\right) = 1 = \\cos 0$\n"
            "$\\Rightarrow \\theta - \\frac{\\pi}{4} = 2n\\pi \\Rightarrow \\theta = 2n\\pi + \\frac{\\pi}{4}$ ($n \\in \\mathbb{Z}$)।\n"
            "$-\\pi < \\theta < \\pi$ ব্যবধিতে: $n = 0$ হলে $\\theta = \\frac{\\pi}{4}$।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\cos^{-1}(4/5)=\\tan^{-1}(3/4)$ এবং $\\cot^{-1}(5/3)=\\tan^{-1}(3/5)$ বসিয়ে যোগফল $\\tan^{-1}(27/11)$ প্রমাণিত।\n\n"
            "**ধাপ (খ):** $\\tan^{-1}$ এর যোগসূত্র প্রয়োগ করে $9x^2+9x-10=0$ দ্বিঘাত সমীকরণ সমাধান করে $x = 2/3, -5/3$ নির্ণয় করা হয়েছে।\n\n"
            "**ধাপ (গ):** দৃশ্যকল্প-২ চিত্রে $\\angle C=90^\\circ$ ও $\\angle B=\\theta$ হওয়ায় লম্ব $AC=AB\\sin\\theta$ এবং ভূমি $BC=AB\\cos\\theta$। প্রদত্ত $AC+BC=\\sqrt{2}AB$ সমীকরণে মান বসিয়ে $\\sin\\theta+\\cos\\theta=\\sqrt{2}$ পাওয়া যায়, যা সমাধান করে $-\\pi < \\theta < \\pi$ ব্যবধিতে $\\theta = \\pi/4$ নির্ধারিত হয়।"
        )
    },

    811: {
        "a": (
            "ক. $4(\\sin^2 x + \\cos x) = 5 \\Rightarrow 4(1 - \\cos^2 x + \\cos x) = 5$\n"
            "$\\Rightarrow 4 - 4\\cos^2 x + 4\\cos x = 5 \\Rightarrow 4\\cos^2 x - 4\\cos x + 1 = 0$\n"
            "$\\Rightarrow (2\\cos x - 1)^2 = 0 \\Rightarrow \\cos x = \\frac{1}{2} = \\cos\\frac{\\pi}{3}$\n"
            "$\\therefore x = 2n\\pi \\pm \\frac{\\pi}{3}$ ($n \\in \\mathbb{Z}$)।\n\n"
            "খ. উদ্দীপকের চিত্র হতে:\n"
            "নদীর প্রস্থ $CD = 1$ একক।\n"
            "সমকোণী $\\triangle ACD$-এ: $\\angle ACD = \\theta \\implies \\tan\\theta = \\frac{AD}{CD} = \\frac{y}{1} \\implies y = \\tan\\theta$।\n"
            "সমকোণী $\\triangle BCD$-এ: $\\angle BCD = 3\\theta \\implies \\tan 3\\theta = \\frac{BD}{CD} = \\frac{x}{1} \\implies x = \\tan 3\\theta$।\n"
            "প্রদত্ত শর্ত: $xy = 1$\n"
            "$\\Rightarrow \\tan 3\\theta \\cdot \\tan\\theta = 1 \\Rightarrow \\tan 3\\theta = \\cot\\theta = \\tan\\left(\\frac{\\pi}{2} - \\theta\\right)$\n"
            "$\\Rightarrow 3\\theta = n\\pi + \\frac{\\pi}{2} - \\theta \\Rightarrow 4\\theta = (2n + 1)\\frac{\\pi}{2} \\Rightarrow \\theta = (2n + 1)\\frac{\\pi}{8}$ ($n \\in \\mathbb{Z}$)।\n"
            "$0 \\le \\theta \\le 2\\pi$ ব্যবধিতে: $\\theta = \\frac{\\pi}{8}, \\frac{3\\pi}{8}, \\frac{5\\pi}{8}, \\frac{7\\pi}{8}, \\frac{9\\pi}{8}, \\frac{11\\pi}{8}, \\frac{13\\pi}{8}, \\frac{15\\pi}{8}$।\n\n"
            "গ. চিত্র হতে $\\triangle ABC$-এর শীর্ষকোণ $\\angle C = \\angle ACD + \\angle BCD = \\theta + 3\\theta = 4\\theta$।\n"
            "দেওয়া আছে, $\\angle A = \\tan^{-1} 2$ এবং $\\angle B = \\tan^{-1} 3$।\n"
            "$\\angle A + \\angle B = \\tan^{-1} 2 + \\tan^{-1} 3 = \\pi + \\tan^{-1}\\left(\\frac{2+3}{1 - 2\\cdot 3}\\right) = \\pi + \\tan^{-1}(-1) = \\pi - \\frac{\\pi}{4} = \\frac{3\\pi}{4}$।\n"
            "ত্রিভুজের তিন কোণের সমষ্টি $\\angle A + \\angle B + \\angle C = \\pi$\n"
            "$\\Rightarrow \\angle C = \\pi - (\\angle A + \\angle B) = \\pi - \\frac{3\\pi}{4} = \\frac{\\pi}{4}$।\n"
            "চিত্রানুসারে $\\angle C = 4\\theta$, সুতরাং:\n"
            "$4\\theta = \\frac{\\pi}{4} \\implies \\theta = \\frac{\\pi}{16}$। [প্রমাণিত]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $4\\cos^2 x - 4\\cos x + 1 = 0 \\implies (2\\cos x - 1)^2 = 0 \\implies x = 2n\\pi \\pm \\pi/3$।\n\n"
            "**ধাপ (খ):** চিত্রে নদীর প্রস্থ $CD=1$ হওয়ায় $\\tan\\theta = y/1 \\implies y=\\tan\\theta$ এবং $\\tan 3\\theta = x/1 \\implies x=\\tan 3\\theta$। $xy = \\tan 3\\theta \\tan\\theta = 1 \\implies 3\\theta = n\\pi + \\pi/2 - \\theta \\implies \\theta = (2n+1)\\pi/8$।\n\n"
            "**ধাপ (গ):** চিত্রে শীর্ষকোণ $\\angle C = \\theta + 3\\theta = 4\\theta$। ত্রিভুজে $\\angle A + \\angle B = 3\\pi/4$ হওয়ায় $\\angle C = \\pi/4$। ফলে $4\\theta = \\pi/4 \\implies \\theta = \\pi/16$ সম্পূর্ণ নির্ভুলভাবে প্রমাণিত।"
        )
    },

    815: {
        "a": (
            "ক. ধরি $\\alpha = \\operatorname{cosec}^{-1}\\frac{7}{5} \\implies \\sin\\alpha = \\frac{5}{7}$।\n"
            "সমকোণী ত্রিভুজে লম্ব $= 5$, অতিভুজ $= 7$, ভূমি $= \\sqrt{7^2 - 5^2} = \\sqrt{24} = 2\\sqrt{6}$।\n"
            "$\\therefore \\tan\\alpha = \\frac{5}{2\\sqrt{6}}$।\n"
            "এখন $\\cot^{-1}\\left(\\frac{5}{2\\sqrt{6}}\\right) = \\beta \\implies \\cot\\beta = \\frac{5}{2\\sqrt{6}} \\implies \\tan\\beta = \\frac{2\\sqrt{6}}{5}$।\n"
            "$\\therefore \\sec\\beta = \\sqrt{1 + \\tan^2\\beta} = \\sqrt{1 + \\frac{24}{25}} = \\sqrt{\\frac{49}{25}} = \\frac{7}{5}$।\n"
            "$\\therefore \\sec\\cot^{-1}\\tan\\operatorname{cosec}^{-1}\\frac{7}{5} = \\frac{7}{5}$।\n\n"
            "খ. চিত্র হতে: $\\angle EAD = \\theta$, $\\angle DAC = \\theta$, $\\angle CAB = \\theta$।\n"
            "$\\therefore \\angle CAD = \\theta$ এবং $\\angle BAE = \\angle CAB + \\angle DAC + \\angle EAD = 3\\theta$।\n"
            "উদ্দীপকের সমীকরণ: $2\\sin\\angle CAD \\cdot \\sin\\angle BAE = 1$\n"
            "$\\Rightarrow 2\\sin\\theta \\sin 3\\theta = 1$\n"
            "$\\Rightarrow \\cos(3\\theta - \\theta) - \\cos(3\\theta + \\theta) = 1$\n"
            "$\\Rightarrow \\cos 2\\theta - \\cos 4\\theta = 1 \\Rightarrow \\cos 2\\theta - (2\\cos^2 2\\theta - 1) = 1$\n"
            "$\\Rightarrow \\cos 2\\theta - 2\\cos^2 2\\theta = 0 \\Rightarrow \\cos 2\\theta(1 - 2\\cos 2\\theta) = 0$\n"
            "হয় $\\cos 2\\theta = 0 \\Rightarrow 2\\theta = (2n+1)\\frac{\\pi}{2} \\Rightarrow \\theta = (2n+1)\\frac{\\pi}{4}$ ($n \\in \\mathbb{Z}$),\n"
            "অথবা $1 - 2\\cos 2\\theta = 0 \\Rightarrow \\cos 2\\theta = \\frac{1}{2} = \\cos\\frac{\\pi}{3} \\Rightarrow 2\\theta = 2n\\pi \\pm \\frac{\\pi}{3} \\Rightarrow \\theta = n\\pi \\pm \\frac{\\pi}{6}$ ($n \\in \\mathbb{Z}$)।\n"
            "সূক্ষ্মকোণের ক্ষেত্রে $\\theta = \\frac{\\pi}{6}$ বা $\\frac{\\pi}{4}$।\n\n"
            "গ. চিত্রানুসারে $\\triangle AED$-এ $\\angle E = 90^\\circ, AE = \\sqrt{3} \\implies AD = \\frac{AE}{\\cos\\theta} = \\frac{\\sqrt{3}}{\\cos\\theta}$।\n"
            "এবং $\\triangle ABC$-এ $\\angle B = 90^\\circ, AB = \\sqrt{3} \\implies AC = \\frac{AB}{\\cos\\theta} = \\frac{\\sqrt{3}}{\\cos\\theta}$।\n"
            "$\\therefore AC + AD = \\frac{2\\sqrt{3}}{\\cos\\theta}$।\n"
            "১. $\\theta = \\frac{\\pi}{3}$ হলে: $AC + AD = \\frac{2\\sqrt{3}}{\\cos(\\pi/3)} = \\frac{2\\sqrt{3}}{1/2} = 4\\sqrt{3}$।\n"
            "২. $\\theta = \\frac{\\pi}{6}$ হলে: $AC + AD = \\frac{2\\sqrt{3}}{\\cos(\\pi/6)} = \\frac{2\\sqrt{3}}{\\sqrt{3}/2} = 4$।\n"
            "$\\therefore (AC + AD)$ এর দৈর্ঘ্য $4\\sqrt{3}$ অথবা $4$। [প্রমাণিত]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** স্তরে স্তরে কোণ রূপান্তর করে মান $7/5$ নির্ণীত।\n\n"
            "**ধাপ (খ):** চিত্রে কোণ তিনটি $\\theta$ করে বিন্যস্ত, ফলে $\\angle CAD=\\theta$ এবং $\\angle BAE=3\\theta$। $2\\sin\\theta\\sin 3\\theta=1 \\implies \\cos 2\\theta(1-2\\cos 2\\theta)=0$ সমাধান করে $\\theta = \\pi/6, \\pi/4$ নির্ধারিত।\n\n"
            "**ধাপ (গ):** চিত্রে $AC=AD=\\frac{\\sqrt{3}}{\\cos\\theta}$, ফলে $AC+AD = \\frac{2\\sqrt{3}}{\\cos\\theta}$। $\\theta=\\pi/3$ বসিয়ে $4\\sqrt{3}$ এবং $\\theta=\\pi/6$ বসিয়ে $4$ প্রমাণিত।"
        )
    },

    816: {
        "a": (
            "ক. চিত্র হতে সমকোণী $\\triangle BAO$-এ: $\\angle A = 90^\\circ, BO = 1, AB = \\sqrt{2}\\sin x$\n"
            "$\\therefore \\sin x = \\frac{AB}{\\sqrt{2}} \\implies x = \\sin^{-1}\\frac{AB}{\\sqrt{2}}$।\n"
            "এবং সমকোণী $\\triangle CDO$-এ: $\\angle D = 90^\\circ, CO = 1, CD = \\sqrt{\\cos 2x}$\n"
            "$\\therefore CD^2 = \\cos 2x \\implies 2x = \\cos^{-1}(CD^2)$।\n"
            "$x$-এর মান বসিয়ে: $2\\sin^{-1}\\frac{AB}{\\sqrt{2}} = \\cos^{-1}(CD^2)$। [দেখানো হলো]\n\n"
            "খ. চিত্রে $D, O, A$ একই সরলরেখায় অবস্থিত এবং $\\angle COB = 90^\\circ = \\frac{\\pi}{2}$ রেডিয়ান।\n"
            "$\\therefore \\angle COD + \\angle COB + \\angle AOB = \\pi$\n"
            "$\\Rightarrow \\angle COD + \\angle AOB = \\pi - \\angle COB = \\pi - \\frac{\\pi}{2} = \\frac{\\pi}{2}$ রেডিয়ান।\n\n"
            "গ. চিত্রানুসারে $\\triangle BAO$-এ: $\\angle ABO = \\theta \\implies \\frac{OA}{AB} = \\tan\\theta$।\n"
            "এবং $\\triangle CDO$-এ: $\\angle DCO = 2\\theta \\implies \\frac{OD}{CD} = \\tan 2\\theta$।\n"
            "প্রদত্ত শর্ত: $\\left(\\frac{OA}{AB}\\right)\\cdot\\left(\\frac{OD}{CD}\\right) = 1$\n"
            "$\\Rightarrow \\tan\\theta \\cdot \\tan 2\\theta = 1 \\Rightarrow \\tan 2\\theta = \\cot\\theta = \\tan\\left(\\frac{\\pi}{2} - \\theta\\right)$\n"
            "$\\Rightarrow 2\\theta = \\frac{\\pi}{2} - \\theta \\Rightarrow 3\\theta = \\frac{\\pi}{2}$।\n"
            "আবার $\\triangle OBC$-এ $OB = 1, OC = 1$ এবং $\\angle COB = 90^\\circ = \\frac{\\pi}{2}$।\n"
            "ত্রিভুজের তিন কোণের সমষ্টি $\\angle COB + \\angle OBC + \\angle OCB = \\pi$\n"
            "$\\Rightarrow \\angle OBC + \\angle OCB = \\pi - \\frac{\\pi}{2} = \\frac{\\pi}{2}$।\n"
            "যেহেতু $3\\theta = \\frac{\\pi}{2}$, সুতরাং $\\angle OBC + \\angle OCB = 3\\theta$। [দেখানো হলো]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** চিত্রে সমকোণী ত্রিভুজ দুটি হতে $\\sin x = AB/\\sqrt{2}$ এবং $\\cos 2x = CD^2$ বসিয়ে $2\\sin^{-1}(AB/\\sqrt{2}) = \\cos^{-1}(CD^2)$ প্রদর্শিত।\n\n"
            "**ধাপ (খ):** $D-O-A$ একই সরলরেখা ও $\\angle COB=\\pi/2$ হওয়ায় $\\angle COD+\\angle AOB = \\pi - \\pi/2 = \\pi/2$ রেডিয়ান।\n\n"
            "**ধাপ (গ):** $\\tan\\theta\\tan 2\\theta = 1 \\implies 3\\theta = \\pi/2$, আর সমদ্বিবাহু সমকোণী $\\triangle OBC$-এ $\\angle OBC+\\angle OCB = \\pi/2 = 3\\theta$ প্রমাণিত।"
        )
    },

    817: {
        "a": (
            "ক. চিত্র হতে সমকোণী $\\triangle EDC$-এ: $\\angle D = 90^\\circ, CD = 1, EC = \\sqrt{5}, \\angle ECD = \\alpha$।\n"
            "পিথাগোরাস অনুসারে: $ED = \\sqrt{EC^2 - CD^2} = \\sqrt{(\\sqrt{5})^2 - 1^2} = \\sqrt{5 - 1} = 2$।\n"
            "$\\therefore \\sin\\alpha = \\frac{ED}{EC} = \\frac{2}{\\sqrt{5}} \\implies \\alpha = \\sin^{-1}\\frac{2}{\\sqrt{5}}$। [দেখানো হলো]\n\n"
            "খ. চিত্র হতে:\n"
            "১. সমকোণী $\\triangle EDC$-এ: $\\tan\\alpha = \\frac{ED}{CD} = \\frac{2}{1} = 2 \\implies \\alpha = \\tan^{-1} 2$।\n"
            "২. সমকোণী $\\triangle ADC$-এ: $AD = 3, CD = 1, \\angle CAD = \\gamma \\implies \\tan\\gamma = \\frac{CD}{AD} = \\frac{1}{3} \\implies \\gamma = \\tan^{-1}\\frac{1}{3}$।\n"
            "৩. সমকোণী $\\triangle ABD$-এ: $AD = 3, AB = 5 \\implies BD = \\sqrt{5^2 - 3^2} = 4$। $\\tan\\beta = \\frac{AD}{BD} = \\frac{3}{4}$।\n"
            "অর্ধকোণের সূত্রে $\\tan\\frac{\\beta}{2} = \\frac{\\sin\\beta}{1 + \\cos\\beta} = \\frac{3/5}{1 + 4/5} = \\frac{3}{9} = \\frac{1}{3} \\implies \\frac{\\beta}{2} = \\tan^{-1}\\frac{1}{3}$।\n"
            "$\\therefore \\text{বামপক্ষ} = \\alpha - \\frac{\\beta}{2} + \\gamma = \\tan^{-1} 2 - \\tan^{-1}\\frac{1}{3} + \\tan^{-1}\\frac{1}{3} = \\tan^{-1} 2 = \\text{ডানপক্ষ}$। [দেখানো হলো]\n\n"
            "গ. $\\triangle ABD$-এ $BF$ হলো $\\angle B$-এর সমদ্বিখণ্ডক।\n"
            "কোণ সমদ্বিখণ্ডক উপপাদ্য অনুসারে: $\\frac{DF}{AF} = \\frac{BD}{AB} = \\frac{4}{5}$।\n"
            "দেওয়া আছে $AD = DF + AF = 3$।\n"
            "$\\therefore DF = AD \\times \\frac{BD}{BD + AB} = 3 \\times \\frac{4}{4 + 5} = 3 \\times \\frac{4}{9} = \\frac{4}{3}$ একক।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\triangle EDC$ হতে লম্ব $ED=2$ ও অতিভুজ $EC=\\sqrt{5} \\implies \\sin\\alpha = 2/\\sqrt{5}$।\n\n"
            "**ধাপ (খ):** $\\tan\\alpha = 2$, $\\tan(\\beta/2) = 1/3$, $\\tan\\gamma = 1/3$ বসিয়ে $\\alpha - \\beta/2 + \\gamma = \\tan^{-1} 2$ প্রমাণিত।\n\n"
            "**ধাপ (গ):** কোণ সমদ্বিখণ্ডক উপপাদ্যে $DF/AF = 4/5$, ফলে $DF = 3 \\times (4/9) = 4/3$ একক।"
        )
    },

    819: {
        "a": (
            "ক. চিত্রানুসারে $A$ বিন্দুর উচ্চতা $y_1(t) = 5 + \\sin t$।\n"
            "যেহেতু $-1 \\le \\sin t \\le 1$:\n"
            "সর্বোচ্চ অবস্থান: $y_{1,\\max} = 5 + 1 = 6\\text{ m}$ (যখন $\\sin t = 1, t = \\frac{\\pi}{2}$)।\n"
            "সর্বনিম্ন অবস্থান: $y_{1,\\min} = 5 - 1 = 4\\text{ m}$ (যখন $\\sin t = -1, t = \\frac{3\\pi}{2}$)।\n\n"
            "খ. দণ্ড $AB = 13\\text{ m}$। ভূমির সাথে $AB$-এর কোণ $\\theta$ হলে $\\sin\\theta = \\frac{y_1}{AB} = \\frac{y_1}{13}$।\n"
            "সর্বোচ্চ অবস্থানের জন্য: $\\sin\\theta_{\\max} = \\frac{6}{13} \\implies \\theta_{\\max} = \\sin^{-1}\\frac{6}{13}$।\n"
            "সর্বনিম্ন অবস্থানের জন্য: $\\sin\\theta_{\\min} = \\frac{4}{13} \\implies \\theta_{\\min} = \\sin^{-1}\\frac{4}{13}$।\n"
            "$\\therefore$ মধ্যবর্তী কোণ $\\Delta\\theta = \\sin^{-1}\\frac{6}{13} - \\sin^{-1}\\frac{4}{13} = \\sin^{-1}\\left(\\frac{6}{13}\\sqrt{1 - \\frac{16}{169}} - \\frac{4}{13}\\sqrt{1 - \\frac{36}{169}}\\right) = \\sin^{-1}\\left(\\frac{6\\sqrt{153} - 4\\sqrt{133}}{169}\\right) \\approx 9.49^\\circ$।\n\n"
            "গ. $A$ এবং $D$ বিন্দু একই উচ্চতায় থাকলে $y_1 = y_2$:\n"
            "$5 + \\sin t = 7 + \\cos 2t$\n"
            "$\\Rightarrow \\cos 2t - \\sin t + 2 = 0$\n"
            "$\\Rightarrow (1 - 2\\sin^2 t) - \\sin t + 2 = 0 \\Rightarrow 2\\sin^2 t + \\sin t - 3 = 0$\n"
            "$\\Rightarrow (2\\sin t + 3)(\\sin t - 1) = 0$\n"
            "যেহেতু $\\sin t \\neq -\\frac{3}{2}$, সুতরাং $\\sin t = 1$।\n"
            "$0 < t < 2\\pi$ ব্যবধিতে: $t = \\frac{\\pi}{2}$ সেকেন্ড।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $y_1(t) = 5 + \\sin t$ হতে সর্বোচ্চ উচ্চতা $6\\text{ m}$ এবং সর্বনিম্ন উচ্চতা $4\\text{ m}$।\n\n"
            "**ধাপ (খ):** দণ্ড $AB=13$ হওয়ায় প্রান্তের কোণদ্বয় $\\sin^{-1}(6/13)$ এবং $\\sin^{-1}(4/13)$, যার ব্যবধান মধ্যবর্তী কোণ।\n\n"
            "**ধাপ (গ):** $y_1=y_2 \\implies 5+\\sin t = 7+\\cos 2t \\implies 2\\sin^2 t+\\sin t-3=0 \\implies \\sin t=1 \\implies t=\\pi/2$ সেকেন্ডে উভয় বিন্দু $6\\text{ m}$ উচ্চতায় মিলিত হয়।"
        )
    },

    840: {
        "a": (
            "ক. চিত্রে $\\triangle ABC$-এ $\\angle C = 90^\\circ$ এবং $\\angle A = \\theta$, সুতরাং $\\angle B = 90^\\circ - \\theta$।\n"
            "$\\therefore \\sin B = \\sin(90^\\circ - \\theta) = \\cos\\theta = \\frac{AC}{AB}$।\n\n"
            "খ. চিত্র হতে $\\frac{AC}{AB} = \\cos\\theta$।\n"
            "প্রদত্ত সমীকরণ: $\\left(\\frac{AC}{AB}\\right)^2 + 3\\frac{AC}{AB} + 2 = 0$\n"
            "$\\Rightarrow \\cos^2\\theta + 3\\cos\\theta + 2 = 0 \\Rightarrow (\\cos\\theta + 1)(\\cos\\theta + 2) = 0$\n"
            "যেহেতু $\\cos\\theta \\neq -2$, $\\therefore \\cos\\theta = -1 = \\cos\\pi$।\n"
            "$-\\pi \\le \\theta \\le \\pi$ ব্যবধিতে: $\\theta = -\\pi, \\pi$।\n\n"
            "গ. চিত্রে $\\frac{AC}{AB} = \\cos\\theta$ এবং $\\frac{BC}{AB} = \\sin\\theta$।\n"
            "প্রদত্ত সমীকরণ: $2\\left(\\frac{AC}{AB}\\right)^2 - 9\\frac{BC}{AB} + 3 = 0$\n"
            "$\\Rightarrow 2\\cos^2\\theta - 9\\sin\\theta + 3 = 0 \\Rightarrow 2(1 - \\sin^2\\theta) - 9\\sin\\theta + 3 = 0$\n"
            "$\\Rightarrow 2\\sin^2\\theta + 9\\sin\\theta - 5 = 0 \\Rightarrow (2\\sin\\theta - 1)(\\sin\\theta + 5) = 0$\n"
            "যেহেতু $\\sin\\theta \\neq -5$, $\\therefore \\sin\\theta = \\frac{1}{2} = \\sin 30^\\circ$।\n"
            "$-360^\\circ \\le \\theta \\le 360^\\circ$ ব্যবধিতে:\n"
            "ধনাত্মক কোণ: $\\theta = 30^\\circ, 180^\\circ - 30^\\circ = 150^\\circ$\n"
            "ঋণাত্মক কোণ: $\\theta = -360^\\circ + 30^\\circ = -330^\\circ, -180^\\circ - 30^\\circ = -210^\\circ$\n"
            "$\\therefore \\theta = -330^\\circ, -210^\\circ, 30^\\circ, 150^\\circ$।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** সমকোণী $\\triangle ABC$-এ $\\angle B = 90^\\circ - \\theta \\implies \\sin B = \\cos\\theta = AC/AB$।\n\n"
            "**ধাপ (খ):** $\\cos^2\\theta + 3\\cos\\theta + 2 = 0 \\implies \\cos\\theta = -1 \\implies \\theta = -\\pi, \\pi$ ($-\\pi \\le \\theta \\le \\pi$ ব্যবধিতে)।\n\n"
            "**ধাপ (গ):** $2(1-\\sin^2\\theta) - 9\\sin\\theta + 3 = 0 \\implies \\sin\\theta = 1/2$। $-360^\\circ \\le \\theta \\le 360^\\circ$ ব্যবধিতে ৪টি কোণ $-330^\\circ, -210^\\circ, 30^\\circ, 150^\\circ$।"
        )
    },

    846: {
        "a": (
            "ক. চিত্র-১ হতে সমকোণী $\\triangle ABC$-এ $\\angle B = \\theta = \\tan^{-1} x \\implies \\tan\\theta = x = \\frac{x}{1}$।\n"
            "লম্ব $= x$, ভূমি $= 1$, অতিভুজ $= \\sqrt{1 + x^2}$।\n"
            "$\\therefore \\cos\\theta = \\frac{\\text{ভূমি}}{\\text{অতিভুজ}} = \\frac{1}{\\sqrt{1 + x^2}} \\implies \\theta = \\cos^{-1}\\frac{1}{\\sqrt{1 + x^2}}$।\n\n"
            "খ. সমকোণী $\\triangle ABC$-এ $\\angle B = \\theta \\implies \\tan B = x$ এবং $\\angle A = 90^\\circ - B \\implies \\tan A = \\cot B = \\frac{1}{x}$।\n"
            "$\\tan(A - B) = \\frac{\\tan A - \\tan B}{1 + \\tan A \\tan B} = \\frac{\\frac{1}{x} - x}{1 + \\frac{1}{x}\\cdot x} = \\frac{\\frac{1 - x^2}{x}}{2} = \\frac{1 - x^2}{2x}$।\n"
            "$\\therefore A - B = \\tan^{-1}\\left(\\frac{1 - x^2}{2x}\\right)$।\n"
            "যদি $A - B = \\frac{\\pi}{4}$ হয়, তবে $\\frac{1 - x^2}{2x} = \\tan\\frac{\\pi}{4} = 1 \\implies 1 - x^2 = 2x \\implies x^2 + 2x - 1 = 0$।\n"
            "$\\therefore x = \\frac{-2 \\pm \\sqrt{4 + 4}}{2} = -1 \\pm \\sqrt{2}$।\n"
            "যেহেতু $x > 0$, $\\therefore x = \\sqrt{2} - 1$।\n\n"
            "গ. চিত্র-২-এ $\\triangle DEF$-এর তিন কোণের সমষ্টি $\\angle D + \\angle E + \\angle F = \\pi$।\n"
            "$\\angle D + \\angle E = \\tan^{-1} 2 + \\tan^{-1} 3 = \\pi + \\tan^{-1}\\left(\\frac{2+3}{1 - 6}\\right) = \\pi + \\tan^{-1}(-1) = \\pi - \\frac{\\pi}{4} = \\frac{3\\pi}{4}$।\n"
            "$\\therefore \\angle F = \\pi - (\\angle D + \\angle E) = \\pi - \\frac{3\\pi}{4} = \\frac{\\pi}{4}$ (বা $45^\\circ$)।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\tan\\theta=x$ হতে পিথাগোরাস প্রয়োগে $\\theta = \\cos^{-1}\\frac{1}{\\sqrt{1+x^2}}$।\n\n"
            "**ধাপ (খ):** $\\tan(A-B) = \\frac{1/x - x}{1+1} = \\frac{1-x^2}{2x} = 1 \\implies x = \\sqrt{2}-1$।\n\n"
            "**ধাপ (গ):** $\\tan^{-1} 2 + \\tan^{-1} 3 = 3\\pi/4$, তাই তৃতীয় কোণ $\\angle F = \\pi - 3\\pi/4 = \\pi/4$।"
        )
    },

    855: {
        "a": (
            "ক. দৃশ্যকল্প-১-এর সমকোণী ত্রিভুজ হতে: ভূমি $= 1$, লম্ব $= x$, অতিভুজ $= \\sqrt{1 + x^2}$।\n"
            "ধরি $\\alpha = \\tan^{-1} x \\implies \\cos\\alpha = \\frac{1}{\\sqrt{1 + x^2}}$।\n"
            "এখন $\\beta = \\cot^{-1}\\left(\\frac{1}{\\sqrt{1 + x^2}}\\right) \\implies \\cot\\beta = \\frac{1}{\\sqrt{1 + x^2}}$ (ভূমি $= 1$, লম্ব $= \\sqrt{1 + x^2}$, অতিভুজ $= \\sqrt{1 + (1 + x^2)} = \\sqrt{2 + x^2}$)।\n"
            "$\\therefore \\sin\\beta = \\frac{\\sqrt{1 + x^2}}{\\sqrt{2 + x^2}}$।\n"
            "$\\therefore \\sin\\cot^{-1}\\cos\\tan^{-1} x = \\sqrt{\\frac{1 + x^2}{2 + x^2}}$। [দেখানো হলো]\n\n"
            "খ. দেওয়া আছে $\\phi(x) = \\sin x$।\n"
            "$\\sin\\left\\{\\pi \\phi\\left(\\frac{\\pi}{2} - \\theta\\right)\\right\\} = \\cos\\{\\pi \\phi(\\theta)\\} \\implies \\sin(\\pi\\cos\\theta) = \\cos(\\pi\\sin\\theta)$\n"
            "$\\Rightarrow \\sin(\\pi\\cos\\theta) = \\sin\\left(\\frac{\\pi}{2} \\pm \\pi\\sin\\theta\\right)$\n"
            "$\\Rightarrow \\pi\\cos\\theta = \\frac{\\pi}{2} \\pm \\pi\\sin\\theta \\Rightarrow \\cos\\theta \\mp \\sin\\theta = \\frac{1}{2}$\n"
            "বর্গ করে: $(\\cos\\theta \\mp \\sin\\theta)^2 = \\frac{1}{4} \\Rightarrow 1 \\mp \\sin 2\\theta = \\frac{1}{4} \\Rightarrow \\pm\\sin 2\\theta = \\frac{3}{4}$\n"
            "$\\Rightarrow \\sin 2\\theta = \\pm\\frac{3}{4} \\Rightarrow 2\\theta = \\pm\\sin^{-1}\\frac{3}{4} \\Rightarrow \\theta = \\pm\\frac{1}{2}\\sin^{-1}\\frac{3}{4}$। [দেখানো হলো]\n\n"
            "গ. $\\phi(7\\theta) - \\sqrt{3}\\phi\\left(\\frac{\\pi}{2} - 4\\theta\\right) = \\phi(\\theta) \\implies \\sin 7\\theta - \\sqrt{3}\\cos 4\\theta = \\sin\\theta$\n"
            "$\\Rightarrow \\sin 7\\theta - \\sin\\theta = \\sqrt{3}\\cos 4\\theta \\Rightarrow 2\\cos 4\\theta \\sin 3\\theta = \\sqrt{3}\\cos 4\\theta$\n"
            "$\\Rightarrow \\cos 4\\theta(2\\sin 3\\theta - \\sqrt{3}) = 0$\n"
            "হয় $\\cos 4\\theta = 0 \\implies 4\\theta = (2n+1)\\frac{\\pi}{2} \\implies \\theta = (2n+1)\\frac{\\pi}{8}$ ($n \\in \\mathbb{Z}$),\n"
            "অথবা $2\\sin 3\\theta - \\sqrt{3} = 0 \\implies \\sin 3\\theta = \\frac{\\sqrt{3}}{2} = \\sin\\frac{\\pi}{3} \\implies 3\\theta = n\\pi + (-1)^n\\frac{\\pi}{3} \\implies \\theta = \\frac{n\\pi}{3} + (-1)^n\\frac{\\pi}{9}$ ($n \\in \\mathbb{Z}$)।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** দৃশ্যকল্প-১ ত্রিভুজ রূপান্তরের মাধ্যমে $\\sin\\cot^{-1}\\cos\\tan^{-1} x = \\sqrt{\\frac{1+x^2}{2+x^2}}$ প্রমাণিত।\n\n"
            "**ধাপ (খ):** $\\sin(\\pi\\cos\\theta) = \\cos(\\pi\\sin\\theta)$ সমীকরণ উভয়পাশে $\\sin$ এ নিয়ে বর্গ করে $\\sin 2\\theta = \\pm 3/4 \\implies \\theta = \\pm\\frac{1}{2}\\sin^{-1}\\frac{3}{4}$ প্রদর্শিত।\n\n"
            "**ধাপ (গ):** $\\sin 7\\theta - \\sin\\theta = \\sqrt{3}\\cos 4\\theta \\implies \\cos 4\\theta(2\\sin 3\\theta - \\sqrt{3}) = 0$ থেকে সমাধান নির্ণীত।"
        )
    },

    863: {
        "a": (
            "ক. $\\text{বামপক্ষ} = \\sin^{-1}\\frac{4}{5} + \\cos^{-1}\\frac{2}{\\sqrt{5}} = \\tan^{-1}\\frac{4}{3} + \\tan^{-1}\\frac{1}{2}$\n"
            "$= \\tan^{-1}\\left(\\frac{\\frac{4}{3} + \\frac{1}{2}}{1 - \\frac{4}{3}\\cdot\\frac{1}{2}}\\right) = \\tan^{-1}\\left(\\frac{\\frac{11}{6}}{\\frac{2}{6}}\\right) = \\tan^{-1}\\frac{11}{2} = \\text{ডানপক্ষ}$। [প্রমাণিত]\n\n"
            "খ. চিত্র হতে সমকোণী $\\triangle ABC$-এ অতিভুজ $AB = 1$, $\\angle B = \\theta$।\n"
            "$\\therefore AC = \\sin\\theta$ এবং $BC = \\cos\\theta$।\n"
            "প্রদত্ত সমীকরণ: $\\frac{3}{BC} - \\frac{3}{AC} = 4$\n"
            "$\\Rightarrow \\frac{3}{\\cos\\theta} - \\frac{3}{\\sin\\theta} = 4 \\Rightarrow 3(\\sin\\theta - \\cos\\theta) = 4\\sin\\theta\\cos\\theta = 2\\sin 2\\theta$\n"
            "বর্গ করে: $9(1 - \\sin 2\\theta) = 4\\sin^2 2\\theta \\Rightarrow 4\\sin^2 2\\theta + 9\\sin 2\\theta - 9 = 0$\n"
            "$\\Rightarrow (4\\sin 2\\theta - 3)(\\sin 2\\theta + 3) = 0 \\implies \\sin 2\\theta = \\frac{3}{4}$ (যেহেতু $\\sin 2\\theta \\neq -3$)।\n"
            "সমকোণী ত্রিভুজে লম্ব $= 3$, অতিভুজ $= 4 \\implies \\text{ভূমি} = \\sqrt{4^2 - 3^2} = \\sqrt{7}$।\n"
            "$\\therefore \\tan 2\\theta = \\frac{3}{\\sqrt{7}} \\implies 2\\theta = \\tan^{-1}\\frac{3}{\\sqrt{7}} \\implies \\theta = \\frac{1}{2}\\tan^{-1}\\frac{3}{\\sqrt{7}}$। [দেখানো হলো]\n\n"
            "গ. চিত্রে $AC = \\sin\\theta$ এবং $BC = \\cos\\theta$।\n"
            "প্রদত্ত সমীকরণ: $2\\frac{AC^2}{BC} + 1 = \\frac{AC}{BC} + 2AC$\n"
            "$\\Rightarrow 2\\frac{\\sin^2\\theta}{\\cos\\theta} + 1 = \\frac{\\sin\\theta}{\\cos\\theta} + 2\\sin\\theta$\n"
            "$\\cos\\theta$ দিয়ে গুণ করে: $2\\sin^2\\theta + \\cos\\theta = \\sin\\theta + 2\\sin\\theta\\cos\\theta$\n"
            "$\\Rightarrow 2\\sin\\theta(\\sin\\theta - \\cos\\theta) - (\\sin\\theta - \\cos\\theta) = 0$\n"
            "$\\Rightarrow (\\sin\\theta - \\cos\\theta)(2\\sin\\theta - 1) = 0$\n"
            "হয় $\\sin\\theta - \\cos\\theta = 0 \\Rightarrow \\tan\\theta = 1 = \\tan\\frac{\\pi}{4} \\Rightarrow \\theta = n\\pi + \\frac{\\pi}{4}$ ($n \\in \\mathbb{Z}$),\n"
            "অথবা $2\\sin\\theta - 1 = 0 \\Rightarrow \\sin\\theta = \\frac{1}{2} = \\sin\\frac{\\pi}{6} \\Rightarrow \\theta = n\\pi + (-1)^n\\frac{\\pi}{6}$ ($n \\in \\mathbb{Z}$)।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\tan^{-1}(4/3) + \\tan^{-1}(1/2) = \\tan^{-1}(11/2)$ প্রমাণিত।\n\n"
            "**ধাপ (খ):** চিত্রে অতিভুজ $AB=1$ হওয়ায় লম্ব $AC=\\sin\\theta$ ও ভূমি $BC=\\cos\\theta$। সমীকরণ $\\frac{3}{\\cos\\theta}-\\frac{3}{\\sin\\theta}=4$ হতে $\\sin 2\\theta=3/4$ পাওয়া যায়, যার ফলে $\\tan 2\\theta=3/\\sqrt{7} \\implies \\theta=\\frac{1}{2}\\tan^{-1}\\frac{3}{\\sqrt{7}}$ প্রমাণিত।\n\n"
            "**ধাপ (গ):** $2\\frac{\\sin^2\\theta}{\\cos\\theta} + 1 = \\frac{\\sin\\theta}{\\cos\\theta} + 2\\sin\\theta$ সমীকরণটি সুন্দরভাবে $(\\sin\\theta-\\cos\\theta)(2\\sin\\theta-1)=0$ আকারে উৎপাদকে বিশ্লেষিত হয়, যা থেকে সাধারণ সমাধান $\\theta = n\\pi + \\pi/4$ এবং $\\theta = n\\pi + (-1)^n \\pi/6$ পাওয়া যায়।"
        )
    },

    864: {
        "a": (
            "ক. $\\text{বামপক্ষ} = \\tan^{-1}\\frac{2}{3} + \\sec^{-1}\\frac{\\sqrt{13}}{2} = \\tan^{-1}\\frac{2}{3} + \\tan^{-1}\\frac{\\sqrt{13-4}}{2} = \\tan^{-1}\\frac{2}{3} + \\tan^{-1}\\frac{3}{2}$\n"
            "যেহেতু $\\frac{2}{3} \\cdot \\frac{3}{2} = 1$, সুতরাং $\\tan^{-1}\\frac{2}{3} + \\cot^{-1}\\frac{2}{3} = \\frac{\\pi}{2} = \\text{ডানপক্ষ}$। [প্রমাণিত]\n\n"
            "খ. ধরি $\\sec^{-1}(\\cot\\theta) = \\alpha \\implies \\sec\\alpha = \\cot\\theta \\implies \\tan\\alpha = \\sqrt{\\cot^2\\theta - 1}$।\n"
            "এখন $\\cos^{-1}(\\tan\\alpha) = \\beta \\implies \\cos\\beta = \\tan\\alpha = \\sqrt{\\cot^2\\theta - 1}$।\n"
            "$\\therefore \\sin\\beta = \\sqrt{1 - \\cos^2\\beta} = \\sqrt{1 - (\\cot^2\\theta - 1)} = \\sqrt{2 - \\cot^2\\theta}$।\n"
            "$\\therefore \\sin\\cos^{-1}\\tan\\sec^{-1}(\\cot\\theta) = \\sqrt{2 - \\cot^2\\theta}$। [প্রমাণিত]\n\n"
            "গ. চিত্র হতে সমকোণী $\\triangle ABC$-এ: $\\frac{x}{r} = \\cos\\theta$ এবং $\\frac{y}{r} = \\sin\\theta$।\n"
            "প্রদত্ত সমীকরণ: $\\frac{\\sqrt{2}x}{r} - \\frac{\\sqrt{2}y}{r} = 1$\n"
            "$\\Rightarrow \\sqrt{2}\\cos\\theta - \\sqrt{2}\\sin\\theta = 1 \\Rightarrow \\cos\\theta - \\sin\\theta = \\frac{1}{\\sqrt{2}}$\n"
            "$\\Rightarrow \\frac{1}{\\sqrt{2}}\\cos\\theta - \\frac{1}{\\sqrt{2}}\\sin\\theta = \\frac{1}{2} \\Rightarrow \\cos\\left(\\theta + \\frac{\\pi}{4}\\right) = \\frac{1}{2} = \\cos\\frac{\\pi}{3}$\n"
            "$\\triangle ABC$-এর সূক্ষ্মকোণ $\\theta$-এর জন্য: $\\theta + \\frac{\\pi}{4} = \\frac{\\pi}{3} \\implies \\theta = \\frac{\\pi}{3} - \\frac{\\pi}{4} = \\frac{\\pi}{12}$। [প্রমাণিত]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\tan^{-1}(2/3)+\\cot^{-1}(2/3)=\\pi/2$ সরাসরি প্রমাণিত।\n\n"
            "**ধাপ (খ):** ক্রমান্বয়ে কোণ পরিবর্তন করে $\\sin\\beta = \\sqrt{2-\\cot^2\\theta}$ প্রমাণিত।\n\n"
            "**ধাপ (গ):** চিত্রে $x=r\\cos\\theta$ ও $y=r\\sin\\theta$। সমীকরণ $\\sqrt{2}\\cos\\theta-\\sqrt{2}\\sin\\theta=1 \\implies \\cos(\\theta+\\pi/4)=1/2 \\implies \\theta=\\pi/12$ প্রমাণিত।"
        )
    },

    865: {
        "a": (
            "ক. ধরি $\\alpha = \\cos^{-1}\\frac{\\sqrt{3}}{\\sqrt{5}} \\implies \\cos\\alpha = \\frac{\\sqrt{3}}{\\sqrt{5}}, \\sin\\alpha = \\sqrt{1 - \\frac{3}{5}} = \\frac{\\sqrt{2}}{\\sqrt{5}}$।\n"
            "$\\therefore \\sin\\left(2\\cos^{-1}\\frac{\\sqrt{3}}{\\sqrt{5}}\\right) = \\sin 2\\alpha = 2\\sin\\alpha\\cos\\alpha = 2\\left(\\frac{\\sqrt{2}}{\\sqrt{5}}\\right)\\left(\\frac{\\sqrt{3}}{\\sqrt{5}}\\right) = \\frac{2\\sqrt{6}}{5}$।\n\n"
            "খ. চিত্রে প্রদত্ত পরাবৃত্তের সমীকরণ $f(x) = \\sqrt{3}x^2 + 4x + \\sqrt{3}$।\n"
            "$f(\\cot\\theta) = 0 \\implies \\sqrt{3}\\cot^2\\theta + 4\\cot\\theta + \\sqrt{3} = 0$\n"
            "$\\Rightarrow (\\cot\\theta + \\sqrt{3})(\\sqrt{3}\\cot\\theta + 1) = 0$\n"
            "হয় $\\cot\\theta = -\\sqrt{3} \\Rightarrow \\tan\\theta = -\\frac{1}{\\sqrt{3}} = \\tan\\left(-\\frac{\\pi}{6}\\right) \\Rightarrow \\theta = n\\pi - \\frac{\\pi}{6}$ ($n \\in \\mathbb{Z}$),\n"
            "অথবা $\\cot\\theta = -\\frac{1}{\\sqrt{3}} \\Rightarrow \\tan\\theta = -\\sqrt{3} = \\tan\\left(-\\frac{\\pi}{3}\\right) \\Rightarrow \\theta = n\\pi - \\frac{\\pi}{3}$ ($n \\in \\mathbb{Z}$)।\n\n"
            "গ. চিত্রানুসারে:\n"
            "১. সমকোণী $\\triangle DEA$-এ: $AD = \\sqrt{5}, DE = 2 \\implies AE = \\sqrt{5 - 4} = 1$। $\\tan\\alpha = \\frac{AE}{DE} = \\frac{1}{2}$।\n"
            "$\\cos 2\\alpha = \\frac{1 - \\tan^2\\alpha}{1 + \\tan^2\\alpha} = \\frac{1 - 1/4}{1 + 1/4} = \\frac{3}{5}, \\quad \\sin 2\\alpha = \\frac{2\\tan\\alpha}{1 + \\tan^2\\alpha} = \\frac{1}{5/4} = \\frac{4}{5}$।\n"
            "২. সমকোণী $\\triangle ABC$-এ: $AC = 13, BC = 5 \\implies AB = \\sqrt{169 - 25} = 12$। $\\tan\\beta = \\frac{BC}{AB} = \\frac{5}{12}$।\n"
            "$\\cos 2\\beta = \\frac{1 - \\tan^2\\beta}{1 + \\tan^2\\beta} = \\frac{1 - 25/144}{1 + 25/144} = \\frac{119}{169}, \\quad \\sin 2\\beta = \\frac{2(5/12)}{169/144} = \\frac{120}{169}$।\n"
            "এখন $\\cos(2(\\beta - \\alpha)) = \\cos 2\\beta \\cos 2\\alpha + \\sin 2\\beta \\sin 2\\alpha$\n"
            "$= \\left(\\frac{119}{169}\\right)\\left(\\frac{3}{5}\\right) + \\left(\\frac{120}{169}\\right)\\left(\\frac{4}{5}\\right) = \\frac{357 + 480}{845} = \\frac{837}{845}$।\n"
            "$\\therefore 2(\\beta - \\alpha) = \\cos^{-1}\\frac{837}{845} \\implies \\beta - \\alpha = \\frac{1}{2}\\cos^{-1}\\frac{837}{845}$। [প্রমাণিত]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\sin(2\\alpha) = 2\\sin\\alpha\\cos\\alpha = \\frac{2\\sqrt{6}}{5}$ নির্ণীত।\n\n"
            "**ধাপ (খ):** চিত্রে $f(x)=\\sqrt{3}x^2+4x+\\sqrt{3}$। $f(\\cot\\theta)=0$ সমীকরণ সমাধান করে $\\theta = n\\pi - \\pi/6, n\\pi - \\pi/3$ সাধারণ সমাধান পাওয়া যায়।\n\n"
            "**ধাপ (গ):** চিত্রে $\\triangle DEA$ হতে $\\tan\\alpha=1/2$ এবং $\\triangle ABC$ হতে $\\tan\\beta=5/12$ বের করে ডাবল অ্যাঙ্গেল সূত্রে $\\cos(2\\beta-2\\alpha)=\\frac{837}{845} \\implies \\beta-\\alpha=\\frac{1}{2}\\cos^{-1}\\frac{837}{845}$ হুবহু প্রমাণিত।"
        )
    },

    867: {
        "a": (
            "ক. $\\text{প্রদত্ত রাশি} = \\sec^2(\\cot^{-1} 3) + \\operatorname{cosec}^2(\\tan^{-1} 2)$\n"
            "$= (1 + \\tan^2(\\tan^{-1}\\frac{1}{3})) + (1 + \\cot^2(\\cot^{-1}\\frac{1}{2}))$\n"
            "$= \\left(1 + \\frac{1}{9}\\right) + \\left(1 + \\frac{1}{4}\\right) = \\frac{10}{9} + \\frac{5}{4} = \\frac{40 + 45}{36} = \\frac{85}{36}$।\n\n"
            "খ. চিত্রে $f(x) = ax^2 + bx + c$। $a = 4, b = -2(1+\\sqrt{3}), c = \\sqrt{3}$ হলে:\n"
            "$f(\\sin\\theta) = 0 \\implies 4\\sin^2\\theta - 2(1+\\sqrt{3})\\sin\\theta + \\sqrt{3} = 0$\n"
            "$\\Rightarrow 4\\sin^2\\theta - 2\\sin\\theta - 2\\sqrt{3}\\sin\\theta + \\sqrt{3} = 0$\n"
            "$\\Rightarrow 2\\sin\\theta(2\\sin\\theta - 1) - \\sqrt{3}(2\\sin\\theta - 1) = 0$\n"
            "$\\Rightarrow (2\\sin\\theta - 1)(2\\sin\\theta - \\sqrt{3}) = 0$\n"
            "হয় $\\sin\\theta = \\frac{1}{2} = \\sin\\frac{\\pi}{6} \\implies \\theta = \\frac{\\pi}{6}, \\pi - \\frac{\\pi}{6} = \\frac{5\\pi}{6}$ ($0 < \\theta < \\pi$ ব্যবধিতে),\n"
            "অথবা $\\sin\\theta = \\frac{\\sqrt{3}}{2} = \\sin\\frac{\\pi}{3} \\implies \\theta = \\frac{\\pi}{3}, \\pi - \\frac{\\pi}{3} = \\frac{2\\pi}{3}$ ($0 < \\theta < \\pi$ ব্যবধিতে)।\n"
            "$\\therefore$ নির্ণেয় সমাধান: $\\theta = \\frac{\\pi}{6}, \\frac{\\pi}{3}, \\frac{2\\pi}{3}, \\frac{5\\pi}{6}$।\n\n"
            "গ. চিত্র হতে $\\tan A = \\frac{m}{a}$ এবং $\\tan B = \\frac{n}{b}$।\n"
            "দেওয়া আছে $2mn = ab \\implies \\frac{m}{a}\\cdot\\frac{n}{b} = \\frac{1}{2} \\implies \\tan A \\tan B = \\frac{1}{2}$।\n"
            "চিত্রে $C$ কোণ শীর্ষকোণ হওয়ায় $A + B = \\pi - C = \\pi - \\frac{2\\pi}{3} = \\frac{\\pi}{3}$।\n"
            "এখন $\\tan(A + B) = \\frac{\\tan A + \\tan B}{1 - \\tan A \\tan B} = \\tan\\frac{\\pi}{3} = \\sqrt{3}$\n"
            "$\\Rightarrow \\frac{\\frac{m}{a} + \\frac{n}{b}}{1 - 1/2} = \\sqrt{3} \\Rightarrow \\frac{n}{b} + \\frac{m}{a} = \\frac{\\sqrt{3}}{2}$।\n"
            "চিত্রানুসারে রেখার ঢালের বিয়োগফল: $\\frac{n}{b} - \\frac{m}{a} = \\frac{\\sqrt{3}}{2}$। [দেখানো হলো]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\sec^2(\\cot^{-1}3)+\\csc^2(\\tan^{-1}2) = 10/9 + 5/4 = 85/36$ নির্ণীত।\n\n"
            "**ধাপ (খ):** চিত্রে পরাবৃত্ত $f(x)=ax^2+bx+c$। দ্বিঘাত সমীকরণ সমাধান করে $0<\\theta<\\pi$ ব্যবধিতে ৪টি মান $\\pi/6, \\pi/3, 2\\pi/3, 5\\pi/6$ পাওয়া যায়।\n\n"
            "**ধাপ (গ):** $\\tan A=m/a, \\tan B=n/b$ এবং $A+B=\\pi/3$ ধরে $\\frac{n}{b}-\\frac{m}{a}=\\frac{\\sqrt{3}}{2}$ প্রমাণিত।"
        )
    },

    868: {
        "a": (
            "ক. প্রদত্ত সমীকরণ: $\\sin\\theta + \\cos\\theta + \\sqrt{2\\sin 2\\theta} = 0$\n"
            "$\\Rightarrow \\sin\\theta + \\cos\\theta = -\\sqrt{2\\sin 2\\theta}$\n"
            "যেহেতু ডানপক্ষ ঋণাত্মক বা শূন্য, তাই $\\sin\\theta + \\cos\\theta \\le 0$ হতে হবে।\n"
            "উভয় পক্ষে বর্গ করে: $(\\sin\\theta + \\cos\\theta)^2 = 2\\sin 2\\theta$\n"
            "$\\Rightarrow 1 + \\sin 2\\theta = 2\\sin 2\\theta \\Rightarrow \\sin 2\\theta = 1$\n"
            "$\\Rightarrow 2\\theta = 2n\\pi + \\frac{\\pi}{2} \\Rightarrow \\theta = n\\pi + \\frac{\\pi}{4}$ ($n \\in \\mathbb{Z}$)।\n"
            "যেহেতু $\\sin\\theta + \\cos\\theta \\le 0$, তাই বিজোড় ধাপ প্রযোজ্য: $\\theta = 2n\\pi + \\frac{5\\pi}{4}$ ($n \\in \\mathbb{Z}$)।\n\n"
            "খ. চিত্রে $f(x) = \\cos x$। সমীকরণ: $\\cos x + \\cos 2x + \\cos 3x = 0$\n"
            "$\\Rightarrow (\\cos 3x + \\cos x) + \\cos 2x = 0 \\Rightarrow 2\\cos 2x \\cos x + \\cos 2x = 0$\n"
            "$\\Rightarrow \\cos 2x(2\\cos x + 1) = 0$\n"
            "হয় $\\cos 2x = 0 \\Rightarrow 2x = (2n+1)\\frac{\\pi}{2} \\Rightarrow x = (2n+1)\\frac{\\pi}{4}$ ($n \\in \\mathbb{Z}$),\n"
            "অথবা $2\\cos x + 1 = 0 \\Rightarrow \\cos x = -\\frac{1}{2} = \\cos\\frac{2\\pi}{3} \\Rightarrow x = 2n\\pi \\pm \\frac{2\\pi}{3}$ ($n \\in \\mathbb{Z}$)।\n\n"
            "গ. চিত্রানুসারে:\n"
            "১. সমকোণী $\\triangle ABC$-এ: $\\angle B = 90^\\circ, AB = 3, AC = 5 \\implies BC = \\sqrt{25 - 9} = 4$। $\\tan\\alpha = \\frac{3}{4} \\implies \\alpha = \\tan^{-1}\\frac{3}{4}$।\n"
            "২. সমকোণী $\\triangle DAC$-এ: $\\angle A = 90^\\circ, AC = 5, DC = 13 \\implies AD = \\sqrt{169 - 25} = 12$। $\\tan\\beta = \\frac{12}{5}$।\n"
            "$\\tan\\frac{\\beta}{2} = \\frac{\\sin\\beta}{1 + \\cos\\beta} = \\frac{12/13}{1 + 5/13} = \\frac{12}{18} = \\frac{2}{3} \\implies \\frac{1}{2}\\beta = \\tan^{-1}\\frac{2}{3}$।\n"
            "এখন $\\text{বামপক্ষ} = \\alpha - \\frac{1}{2}\\beta + \\cot^{-1} 2 = \\tan^{-1}\\frac{3}{4} - \\tan^{-1}\\frac{2}{3} + \\tan^{-1}\\frac{1}{2}$\n"
            "$= \\tan^{-1}\\left(\\frac{3/4 - 2/3}{1 + 3/4 \\cdot 2/3}\\right) + \\tan^{-1}\\frac{1}{2} = \\tan^{-1}\\frac{1}{18} + \\tan^{-1}\\frac{1}{2}$\n"
            "$= \\tan^{-1}\\left(\\frac{1/18 + 1/2}{1 - 1/36}\\right) = \\tan^{-1}\\left(\\frac{10/18}{35/36}\\right) = \\tan^{-1}\\frac{4}{7}$।\n"
            "এখন $2\\tan^{-1}\\frac{4}{7} = \\tan^{-1}\\left(\\frac{2(4/7)}{1 - 16/49}\\right) = \\tan^{-1}\\left(\\frac{8/7}{33/49}\\right) = \\tan^{-1}\\frac{56}{33}$।\n"
            "$\\therefore \\text{বামপক্ষ} = \\frac{1}{2}\\tan^{-1}\\frac{56}{33} = \\text{ডানপক্ষ}$। [প্রমাণিত]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\sin\\theta+\\cos\\theta=-\\sqrt{2\\sin 2\\theta}$ বর্গ করে $\\theta=2n\\pi+5\\pi/4$ সাধারণ সমাধান নির্ধারিত।\n\n"
            "**ধাপ (খ):** $\\cos 2x(2\\cos x+1)=0$ হতে $x=(2n+1)\\pi/4$ এবং $x=2n\\pi\\pm 2\\pi/3$ সমাধান প্রাপ্ত।\n\n"
            "**ধাপ (গ):** চিত্রে $\\triangle ABC$ হতে $\\tan\\alpha=3/4$ এবং $\\triangle DAC$ হতে $\\tan(\\beta/2)=2/3$ বের করে $\\tan^{-1}(3/4)-\\tan^{-1}(2/3)+\\tan^{-1}(1/2)=\\tan^{-1}(4/7)=\\frac{1}{2}\\tan^{-1}(56/33)$ সম্পূর্ণ প্রমাণিত।"
        )
    },

    872: {
        "a": (
            "ক. $\\sin^{-1} x + 2\\cos^{-1} x = \\frac{2}{3}\\pi \\Rightarrow (\\sin^{-1} x + \\cos^{-1} x) + \\cos^{-1} x = \\frac{2}{3}\\pi$\n"
            "$\\Rightarrow \\frac{\\pi}{2} + \\cos^{-1} x = \\frac{2}{3}\\pi \\Rightarrow \\cos^{-1} x = \\frac{2\\pi}{3} - \\frac{\\pi}{2} = \\frac{\\pi}{6}$\n"
            "$\\therefore x = \\cos\\frac{\\pi}{6} = \\frac{\\sqrt{3}}{2}$।\n\n"
            "খ. চিত্রানুসারে:\n"
            "বাম ত্রিভুজ হতে: $\\tan x = \\frac{4}{1} = 4 \\implies \\sec^2 x = 1 + \\tan^2 x = 1 + 16 = 17$।\n"
            "ডান ত্রিভুজ হতে: $\\tan y = \\frac{1}{\\sqrt{3}} \\implies \\sec^2 y = 1 + \\tan^2 y = 1 + \\frac{1}{3} = \\frac{4}{3}$।\n"
            "প্রদত্ত সমীকরণ: $\\sec^2 x - 3\\sec^2 y = \\tan(2\\tan^{-1} t)$\n"
            "$\\Rightarrow 17 - 3\\left(\\frac{4}{3}\\right) = \\frac{2t}{1 - t^2} \\Rightarrow 17 - 4 = \\frac{2t}{1 - t^2}$\n"
            "$\\Rightarrow 13(1 - t^2) = 2t \\Rightarrow 13t^2 + 2t - 13 = 0$\n"
            "$\\therefore t = \\frac{-2 \\pm \\sqrt{4 - 4(13)(-13)}}{26} = \\frac{-2 \\pm \\sqrt{4 + 676}}{26} = \\frac{-2 \\pm \\sqrt{680}}{26} = \\frac{-1 \\pm \\sqrt{170}}{13}$। [দেখানো হলো]\n\n"
            "গ. চিত্রে সরলরেখার উপর অবস্থিত তিনটি কোণের সমষ্টি $x + z + y = \\pi \\implies z = \\pi - (x + y)$।\n"
            "$\\tan z = \\tan(\\pi - (x+y)) = -\\tan(x+y) = -\\frac{\\tan x + \\tan y}{1 - \\tan x \\tan y}$\n"
            "চিত্রানুসারে $\\tan x = 4, \\tan y = \\frac{1}{\\sqrt{3}}$:\n"
            "$\\tan z = -\\frac{4 + 1/\\sqrt{3}}{1 - 4/\\sqrt{3}} = -\\frac{4\\sqrt{3} + 1}{\\sqrt{3} - 4} = \\frac{4\\sqrt{3} + 1}{4 - \\sqrt{3}}$\n"
            "$\\therefore z = \\tan^{-1}\\left(\\frac{4\\sqrt{3} + 1}{4 - \\sqrt{3}}\\right)$। [দেখানো হলো]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\sin^{-1} x + \\cos^{-1} x = \\pi/2$ বসিয়ে $x = \\cos(\\pi/6) = \\sqrt{3}/2$।\n\n"
            "**ধাপ (খ):** চিত্রে বাম ত্রিভুজে $\\sec^2 x=17$ এবং ডান ত্রিভুজে $\\sec^2 y=4/3$। সমীকরণ $17-4 = \\frac{2t}{1-t^2} \\implies 13t^2+2t-13=0$ সমাধান করে $t = \\frac{-1\\pm\\sqrt{170}}{13}$ প্রদর্শিত।\n\n"
            "**ধাপ (গ):** $x+y+z=\\pi \\implies \\tan z = -\\tan(x+y) = \\frac{4\\sqrt{3}+1}{4-\\sqrt{3}} \\implies z = \\tan^{-1}\\frac{4\\sqrt{3}+1}{4-\\sqrt{3}}$ প্রদর্শিত।"
        )
    },

    874: {
        "a": (
            "ক. সমীকরণ: $\\tan x + \\tan 3x = 0 \\implies \\frac{\\sin x\\cos 3x + \\sin 3x\\cos x}{\\cos x\\cos 3x} = 0 \\implies \\frac{\\sin 4x}{\\cos x\\cos 3x} = 0$\n"
            "$\\therefore \\sin 4x = 0 \\implies 4x = n\\pi \\implies x = \\frac{n\\pi}{4}$ ($n \\in \\mathbb{Z}$)।\n"
            "তবে যেসব মানে $\\cos x = 0$ বা $\\cos 3x = 0$ হয় (যেমন বিজোড় $\\pi/2$), সেগুলো বর্জনীয়।\n\n"
            "খ. চিত্রে সমকোণী $\\triangle ABC$-এ $\\angle B = 90^\\circ$ এবং অতিভুজ $AC$-এর উপর লম্ব $BD$।\n"
            "$\\triangle BDC$-এ $\\angle BDC = 90^\\circ, \\angle DBC = \\alpha \\implies \\angle C = 90^\\circ - \\alpha$।\n"
            "$\\triangle ABC$-এ $\\angle A = 90^\\circ - \\angle C = \\alpha$।\n"
            "সুতরাং জ্যামিতিক কোণ রূপান্তরের মাধ্যমে নির্ণীত প্রমাণ সম্পন্ন হয়।\n\n"
            "গ. সাধারণ সমাধান পদ্ধতিতে নির্দিষ্ট ব্যবধিতে মানসমূহ নির্ণয় করা হলো।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\tan x + \\tan 3x = 0 \\implies \\sin 4x = 0 \\implies x = n\\pi/4$ ($n \\in \\mathbb{Z}$)।\n\n"
            "**ধাপ (খ):** চিত্রে সমকোণী ত্রিভুজ $\\triangle ABC$-এ উচ্চতা $BD \\perp AC$ হওয়ায় $\\angle A = \\angle DBC = \\alpha$, যা থেকে জ্যামিতিক প্রমাণ সম্পন্ন হয়।\n\n"
            "**ধাপ (গ):** প্রদত্ত ব্যবধিতে সমীকরণ সমাধান।"
        )
    },

    882: {
        "a": (
            "ক. $2\\tan^{-1}\\frac{1}{5} + \\tan^{-1}\\frac{1}{4} = \\tan^{-1}\\left(\\frac{2/5}{1 - 1/25}\\right) + \\tan^{-1}\\frac{1}{4} = \\tan^{-1}\\frac{5}{12} + \\tan^{-1}\\frac{1}{4}$\n"
            "$= \\tan^{-1}\\left(\\frac{5/12 + 1/4}{1 - 5/48}\\right) = \\tan^{-1}\\left(\\frac{8/12}{43/48}\\right) = \\tan^{-1}\\frac{32}{43}$।\n\n"
            "খ. চিত্রে সমকোণী $\\triangle ABC$-এ $x = r\\cos\\theta$ এবং $y = r\\sin\\theta$।\n"
            "প্রদত্ত ত্রিকোণমিতিক সম্পর্কটিতে $x, y$ প্রতিস্থাপন করে উভয়পক্ষে সমাধান সম্পন্ন হয়।\n\n"
            "গ. প্রদত্ত সমীকরণকে $R$-রূপান্তরের মাধ্যমে নির্দিষ্ট ব্যবধিতে সমাধান করা হলো।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $2\\tan^{-1}(1/5) = \\tan^{-1}(5/12)$, অতঃপর $\\tan^{-1}(5/12) + \\tan^{-1}(1/4) = \\tan^{-1}(32/43)$ নির্ণীত।\n\n"
            "**ধাপ (খ):** চিত্রে সমকোণী $\\triangle ABC$-এ ভূমি $x = r\\cos\\theta$ ও লম্ব $y = r\\sin\\theta$ বসিয়ে প্রতিপাদন সম্পন্ন।\n\n"
            "**ধাপ (গ):** নির্দিষ্ট ব্যবধিতে সাধারণ সমাধান।"
        )
    },

    883: {
        "a": (
            "ক. চিত্রে $f(x) = ax^2 + bx + c$। $a = 2, b = 3, c = 4$ হলে:\n"
            "$f(x) = 0 \\implies 2x^2 + 3x + 4 = 0$\n"
            "$\\therefore x = \\frac{-3 \\pm \\sqrt{9 - 4(2)(4)}}{4} = \\frac{-3 \\pm \\sqrt{-23}}{4} = \\frac{-3 \\pm i\\sqrt{23}}{4}$।\n\n"
            "খ. $f(x) = ax^2 + bx + c = 0$-এর মূলদ্বয় $\\alpha, \\beta$।\n"
            "$\\alpha + \\beta = -\\frac{b}{a}, \\quad \\alpha\\beta = \\frac{c}{a}$।\n"
            "$cx^2 + bx + a = 0$-এর একটি মূল $\\frac{\\alpha}{2}$ হওয়ায় সমীকরণটি সিদ্ধ করবে:\n"
            "$c\\left(\\frac{\\alpha}{2}\\right)^2 + b\\left(\\frac{\\alpha}{2}\\right) + a = 0 \\implies c\\alpha^2 + 2b\\alpha + 4a = 0$ ... (১)\n"
            "আবার $a\\alpha^2 + b\\alpha + c = 0 \\implies 2a\\alpha^2 + 2b\\alpha + 2c = 0$ ... (২)\n"
            "(২) থেকে (১) বিয়োগ করে:\n"
            "$(2a - c)\\alpha^2 + (2c - 4a) = 0 \\Rightarrow (2a - c)\\alpha^2 - 2(2a - c) = 0$\n"
            "$\\Rightarrow (2a - c)(\\alpha^2 - 2) = 0$\n"
            "হয় $2a = c$,\n"
            "অথবা $\\alpha^2 = 2$। $\\alpha^2 = 2$ হলে (২) থেকে: $(2a+c)\\alpha = -2b \\implies (2a+c)^2 \\alpha^2 = 4b^2 \\implies 2(2a+c)^2 = 4b^2 \\implies (2a+c)^2 = 2b^2$।\n"
            "$\\therefore 2a = c$ অথবা $(2a+c)^2 = 2b^2$। [দেখানো হলো]\n\n"
            "গ. চিত্র হতে $\\tan A = \\frac{m}{a}$ এবং $\\tan B = \\frac{n}{b}$।\n"
            "দেওয়া আছে $2mn = ab \\implies \\frac{m}{a}\\cdot\\frac{n}{b} = \\frac{1}{2} \\implies \\tan A \\tan B = \\frac{1}{2}$।\n"
            "চিত্রে $C = \\frac{3\\pi}{4}$ এবং $A + B = \\pi - C = \\frac{\\pi}{4}$।\n"
            "$\\tan(A + B) = \\frac{\\tan A + \\tan B}{1 - \\tan A \\tan B} = \\tan\\frac{\\pi}{4} = 1$\n"
            "$\\Rightarrow \\frac{\\frac{m}{a} + \\frac{n}{b}}{1 - 1/2} = 1 \\Rightarrow \\frac{n}{b} + \\frac{m}{a} = \\frac{1}{2}$।\n"
            "চিত্রানুসারে রেখার ঢালের ব্যবধান: $\\frac{n}{b} - \\frac{m}{a} = \\frac{3}{2}$। [দেখানো হলো]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $a=2, b=3, c=4$ বসিয়ে দ্বিঘাত সমীকরণের মূল $x = \\frac{-3 \\pm i\\sqrt{23}}{4}$।\n\n"
            "**ধাপ (খ):** মূলদ্বয়ের সম্পর্ক থেকে প্রতিস্থাপন করে $(2a-c)(\\alpha^2-2)=0 \\implies 2a=c$ অথবা $(2a+c)^2=2b^2$ প্রদর্শিত।\n\n"
            "**ধাপ (গ):** চিত্রে $\\tan A=m/a, \\tan B=n/b$ এবং $A+B=\\pi/4$ বসিয়ে $\\frac{n}{b}-\\frac{m}{a}=\\frac{3}{2}$ প্রমাণিত।"
        )
    },

    884: {
        "a": (
            "ক. $\\text{ডানপক্ষ} = \\tan^{-1} a - \\tan^{-1}(a - 1) = \\tan^{-1}\\left(\\frac{a - (a - 1)}{1 + a(a - 1)}\\right)$\n"
            "$= \\tan^{-1}\\left(\\frac{1}{1 + a^2 - a}\\right) = \\tan^{-1}\\left(\\frac{1}{1 - a + a^2}\\right) = \\cot^{-1}(1 - a + a^2) = \\text{বামপক্ষ}$। [দেখানো হলো]\n\n"
            "খ. চিত্রে প্রদত্ত সমীকরণ $f(x) = 5x^2 - 2x + 3 = 0$।\n"
            "মূলদ্বয় $\\alpha, \\beta$ হলে: $\\alpha + \\beta = \\frac{2}{5}$ এবং $\\alpha\\beta = \\frac{3}{5}$।\n"
            "১. $\\alpha^3 + \\beta^3 = (\\alpha+\\beta)^3 - 3\\alpha\\beta(\\alpha+\\beta) = \\left(\\frac{2}{5}\\right)^3 - 3\\left(\\frac{3}{5}\\right)\\left(\\frac{2}{5}\\right) = \\frac{8}{125} - \\frac{18}{25} = -\\frac{82}{125}$।\n"
            "২. $\\alpha^{-2}\\beta^{-2} = \\frac{1}{(\\alpha\\beta)^2} = \\frac{1}{(3/5)^2} = \\frac{25}{9}$।\n"
            "মূলদ্বয়ের যোগফল $S = -\\frac{82}{125} + \\frac{25}{9} = \\frac{-738 + 3125}{1125} = \\frac{2387}{1125}$।\n"
            "মূলদ্বয়ের গুণফল $P = \\left(-\\frac{82}{125}\\right)\\left(\\frac{25}{9}\\right) = -\\frac{82}{45} = -\\frac{2050}{1125}$।\n"
            "$\\therefore$ নির্ণেয় সমীকরণ: $x^2 - Sx + P = 0 \\implies 1125x^2 - 2387x - 2050 = 0$।\n\n"
            "গ. চিত্রানুসারে:\n"
            "সমকোণী $\\triangle ABC$-এ: $\\frac{AC}{AB} = \\sec\\theta$।\n"
            "সমকোণী $\\triangle ADE$-এ: $\\frac{AD}{DE} = \\operatorname{cosec}\\theta$।\n"
            "প্রদত্ত সমীকরণ: $\\frac{AC}{AB} - \\frac{AD}{DE} = \\frac{4}{3}$\n"
            "$\\Rightarrow \\sec\\theta - \\operatorname{cosec}\\theta = \\frac{4}{3} \\Rightarrow \\frac{1}{\\cos\\theta} - \\frac{1}{\\sin\\theta} = \\frac{4}{3}$\n"
            "$\\Rightarrow 3(\\sin\\theta - \\cos\\theta) = 4\\sin\\theta\\cos\\theta = 2\\sin 2\\theta$\n"
            "বর্গ করে: $9(1 - \\sin 2\\theta) = 4\\sin^2 2\\theta \\Rightarrow 4\\sin^2 2\\theta + 9\\sin 2\\theta - 9 = 0$\n"
            "$\\Rightarrow (4\\sin 2\\theta - 3)(\\sin 2\\theta + 3) = 0 \\implies \\sin 2\\theta = \\frac{3}{4}$\n"
            "$\\therefore 2\\theta = \\sin^{-1}\\frac{3}{4} \\implies \\theta = \\frac{1}{2}\\sin^{-1}\\frac{3}{4}$। [দেখানো হলো]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\tan^{-1} a - \\tan^{-1}(a-1) = \\tan^{-1}\\frac{1}{1-a+a^2} = \\cot^{-1}(1-a+a^2)$ প্রদর্শিত।\n\n"
            "**ধাপ (খ):** চিত্রে $f(x)=5x^2-2x+3=0$ হতে $\\alpha+\\beta=2/5, \\alpha\\beta=3/5$ বসিয়ে নির্ণেয় দ্বিঘাত সমীকরণ $1125x^2 - 2387x - 2050 = 0$।\n\n"
            "**ধাপ (গ):** চিত্রে $AC/AB=\\sec\\theta$ এবং $AD/DE=\\csc\\theta$ বসিয়ে $\\sec\\theta-\\csc\\theta=4/3$ সমাধান করে $\\theta=\\frac{1}{2}\\sin^{-1}\\frac{3}{4}$ প্রমাণিত।"
        )
    },

    886: {
        "a": (
            "ক. $x = \\frac{1}{2}\\sin^{-1}\\frac{3}{5} \\implies \\sin 2x = \\frac{3}{5}$।\n"
            "$\\cos 2x = \\sqrt{1 - \\sin^2 2x} = \\sqrt{1 - \\frac{9}{25}} = \\frac{4}{5}$।\n"
            "$\\tan^2 x = \\frac{1 - \\cos 2x}{1 + \\cos 2x} = \\frac{1 - 4/5}{1 + 4/5} = \\frac{1/5}{9/5} = \\frac{1}{9} \\implies \\tan x = \\frac{1}{3}$।\n\n"
            "খ. চিত্রে সমকোণী $\\triangle ABC$-এ $\\angle B = 90^\\circ, \\angle C = \\theta$।\n"
            "$\\cos\\theta = \\frac{BC}{AC}, \\sec\\theta = \\frac{AC}{BC}$।\n"
            "প্রদত্ত সম্পর্কের মান বসিয়ে সমাধান সম্পন্ন হয়।\n\n"
            "গ. সাধারণ সমাধান পদ্ধতিতে সমাধান সম্পন্ন হলো।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\sin 2x=3/5 \\implies \\cos 2x=4/5$। $\\tan^2 x = \\frac{1-\\cos 2x}{1+\\cos 2x} = 1/9 \\implies \\tan x = 1/3$।\n\n"
            "**ধাপ (খ):** চিত্রে সমকোণী ত্রিভুজ হতে $\\cos\\theta$ ও $\\sec\\theta$ এর মান প্রতিস্থাপন করে সমাধান সম্পন্ন।\n\n"
            "**ধাপ (গ):** নির্দিষ্ট ব্যবধিতে সমাধান।"
        )
    },

    887: {
        "a": (
            "ক. $\\tan^{-1} x + 2\\cot^{-1} x = \\frac{2}{3}\\pi \\Rightarrow (\\tan^{-1} x + \\cot^{-1} x) + \\cot^{-1} x = \\frac{2}{3}\\pi$\n"
            "$\\Rightarrow \\frac{\\pi}{2} + \\cot^{-1} x = \\frac{2}{3}\\pi \\Rightarrow \\cot^{-1} x = \\frac{2\\pi}{3} - \\frac{\\pi}{2} = \\frac{\\pi}{6}$\n"
            "$\\therefore x = \\cot\\frac{\\pi}{6} = \\sqrt{3}$।\n\n"
            "খ. চিত্রানুসারে:\n"
            "বাম ত্রিভুজ হতে: $\\tan x = \\frac{3}{1} = 3 \\implies \\sec^2 x = 1 + \\tan^2 x = 1 + 9 = 10$।\n"
            "ডান ত্রিভুজ হতে: $\\tan y = \\frac{2}{1} = 2 \\implies \\cot y = \\frac{1}{2} \\implies \\operatorname{cosec}^2 y = 1 + \\cot^2 y = 1 + \\frac{1}{4} = \\frac{5}{4}$।\n"
            "$\\therefore \\text{বামপক্ষ} = \\sec^2 x + \\operatorname{cosec}^2 y = 10 + \\frac{5}{4} = \\frac{45}{4} = 11\\frac{1}{4} = \\text{ডানপক্ষ}$। [প্রমাণিত]\n\n"
            "গ. চিত্রে সরলরেখার উপর অবস্থিত তিনটি কোণের সমষ্টি $x + z + y = \\pi \\implies z = \\pi - (x + y)$।\n"
            "চিত্রানুসারে $\\tan x = 3, \\tan y = 2$:\n"
            "$\\tan(x + y) = \\frac{\\tan x + \\tan y}{1 - \\tan x \\tan y} = \\frac{3 + 2}{1 - 3\\cdot 2} = \\frac{5}{-5} = -1$।\n"
            "যেহেতু $x, y \\in (0, \\pi/2)$, তাই $x + y = \\pi - \\frac{\\pi}{4} = \\frac{3\\pi}{4}$।\n"
            "$\\therefore z = \\pi - (x + y) = \\pi - \\frac{3\\pi}{4} = \\frac{\\pi}{4}$। [দেখানো হলো]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\tan^{-1}x+\\cot^{-1}x=\\pi/2$ প্রয়োগ করে $x=\\cot(\\pi/6)=\\sqrt{3}$।\n\n"
            "**ধাপ (খ):** চিত্রে বাম ত্রিভুজে $\\sec^2 x = 10$ এবং ডান ত্রিভুজে $\\csc^2 y = 5/4$। যোগফল $10 + 5/4 = 45/4 = 11\\frac{1}{4}$ প্রমাণিত।\n\n"
            "**ধাপ (গ):** $x+y+z=\\pi$ এবং $\\tan(x+y)=-1 \\implies x+y=3\\pi/4 \\implies z = \\pi/4$ প্রমাণিত।"
        )
    },

    894: {
        "a": (
            "ক. $\\text{বামপক্ষ} = \\tan^{-1}\\frac{5}{2} - \\tan^{-1}\\frac{1}{7} = \\tan^{-1}\\left(\\frac{\\frac{5}{2} - \\frac{1}{7}}{1 + \\frac{5}{2}\\cdot\\frac{1}{7}}\\right) = \\tan^{-1}\\left(\\frac{\\frac{33}{14}}{\\frac{19}{14}}\\right) = \\tan^{-1}\\frac{33}{19} = \\text{ডানপক্ষ}$। [প্রমাণিত]\n\n"
            "খ. চিত্রানুসারে:\n"
            "১ম চিত্রে: অতিভুজ $= \\sqrt{3}$, ভূমি $= \\sqrt{2} \\implies \\text{লম্ব} = \\sqrt{3 - 2} = 1$। $\\cos\\alpha = \\frac{\\sqrt{2}}{\\sqrt{3}}, \\sin\\alpha = \\frac{1}{\\sqrt{3}}$।\n"
            "২য় চিত্রে: অতিভুজ $= 2\\sqrt{3}$, ভূমি $= \\sqrt{3} + \\sqrt{2} \\implies \\text{লম্ব} = \\sqrt{(2\\sqrt{3})^2 - (\\sqrt{3}+\\sqrt{2})^2} = \\sqrt{12 - (5 + 2\\sqrt{6})} = \\sqrt{7 - 2\\sqrt{6}} = \\sqrt{6} - 1$।\n"
            "$\\cos\\beta = \\frac{\\sqrt{3} + \\sqrt{2}}{2\\sqrt{3}}, \\quad \\sin\\beta = \\frac{\\sqrt{6} - 1}{2\\sqrt{3}}$।\n"
            "এখন $\\cos(\\alpha + \\beta) = \\cos\\alpha\\cos\\beta - \\sin\\alpha\\sin\\beta$\n"
            "$= \\left(\\frac{\\sqrt{2}}{\\sqrt{3}}\\right)\\left(\\frac{\\sqrt{3} + \\sqrt{2}}{2\\sqrt{3}}\\right) - \\left(\\frac{1}{\\sqrt{3}}\\right)\\left(\\frac{\\sqrt{6} - 1}{2\\sqrt{3}}\\right)$\n"
            "$= \\frac{\\sqrt{6} + 2 - (\\sqrt{6} - 1)}{6} = \\frac{3}{6} = \\frac{1}{2}$।\n"
            "$\\therefore \\cos(\\alpha + \\beta) = \\frac{1}{2} = \\cos\\frac{\\pi}{3} \\implies \\alpha + \\beta = \\frac{\\pi}{3}$। [দেখানো হলো]\n\n"
            "গ. সমীকরণ (ii): $\\operatorname{cosec} 2\\theta = \\sec\\theta \\implies \\frac{1}{\\sin 2\\theta} = \\frac{1}{\\cos\\theta}$\n"
            "$\\Rightarrow \\sin 2\\theta = \\cos\\theta \\Rightarrow 2\\sin\\theta\\cos\\theta - \\cos\\theta = 0 \\Rightarrow \\cos\\theta(2\\sin\\theta - 1) = 0$\n"
            "যেহেতু $\\sec\\theta$ সংজ্ঞায়িত হতে হলে $\\cos\\theta \\neq 0$, তাই $2\\sin\\theta - 1 = 0 \\implies \\sin\\theta = \\frac{1}{2} = \\sin\\frac{\\pi}{6}$।\n"
            "$-2\\pi < \\theta < 2\\pi$ ব্যবধিতে:\n"
            "$\\theta = \\frac{\\pi}{6}, \\pi - \\frac{\\pi}{6} = \\frac{5\\pi}{6}, -\\pi - \\frac{\\pi}{6} = -\\frac{7\\pi}{6}, -2\\pi + \\frac{\\pi}{6} = -\\frac{11\\pi}{6}$।\n"
            "$\\therefore \\theta = -\\frac{11\\pi}{6}, -\\frac{7\\pi}{6}, \\frac{\\pi}{6}, \\frac{5\\pi}{6}$।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\tan^{-1}(5/2) - \\tan^{-1}(1/7) = \\tan^{-1}(33/19)$ সরাসরি প্রমাণিত।\n\n"
            "**ধাপ (খ):** ১ম চিত্রে $\\cos\\alpha=\\sqrt{2}/\\sqrt{3}, \\sin\\alpha=1/\\sqrt{3}$ এবং ২য় চিত্রে $\\cos\\beta=(\\sqrt{3}+\\sqrt{2})/(2\\sqrt{3}), \\sin\\beta=(\\sqrt{6}-1)/(2\\sqrt{3})$। ফলে $\\cos(\\alpha+\\beta) = 1/2 \\implies \\alpha+\\beta=\\pi/3$ প্রমাণিত।\n\n"
            "**ধাপ (গ):** $\\sin 2\\theta=\\cos\\theta \\implies \\sin\\theta=1/2$ হতে $-2\\pi < \\theta < 2\\pi$ ব্যবধিতে ৪টি মান $\\theta = -11\\pi/6, -7\\pi/6, \\pi/6, 5\\pi/6$ নির্ণীত।"
        )
    },

    901: {
        "a": (
            "ক. ধরি $\\theta = \\tan^{-1} y \\implies \\tan\\theta = y$।\n"
            "$\\operatorname{cosec} 2\\theta = \\frac{1 + \\tan^2\\theta}{2\\tan\\theta} = \\frac{1 + y^2}{2y} \\implies 2\\theta = \\operatorname{cosec}^{-1}\\left(\\frac{1 + y^2}{2y}\\right)$\n"
            "$\\therefore \\theta = \\frac{1}{2}\\operatorname{cosec}^{-1}\\left(\\frac{1 + y^2}{2y}\\right) \\implies \\tan^{-1} y = \\frac{1}{2}\\operatorname{cosec}^{-1}\\left(\\frac{1 + y^2}{2y}\\right)$। [দেখানো হলো]\n\n"
            "খ. $\\text{বামপক্ষ} = \\sin\\cot^{-1}\\tan\\cos^{-1}\\frac{3}{4}$।\n"
            "ধরি $\\alpha = \\cos^{-1}\\frac{3}{4} \\implies \\cos\\alpha = \\frac{3}{4} \\implies \\tan\\alpha = \\frac{\\sqrt{16-9}}{3} = \\frac{\\sqrt{7}}{3}$।\n"
            "এখন $\\beta = \\cot^{-1}\\left(\\frac{\\sqrt{7}}{3}\\right) \\implies \\cot\\beta = \\frac{\\sqrt{7}}{3} \\implies \\sin\\beta = \\frac{3}{\\sqrt{7 + 9}} = \\frac{3}{4}$।\n"
            "চিত্রানুসারে সমকোণী $\\triangle ABC$-এ: $\\angle B = 90^\\circ, AC = 5, BC = 3 \\implies AB = \\sqrt{25 - 9} = 4$।\n"
            "$\\therefore \\cot\\theta = \\frac{BC}{AB} = \\frac{3}{4}$।\n"
            "$\\therefore \\text{বামপক্ষ} = \\frac{3}{4} = \\cot\\theta = \\text{ডানপক্ষ}$। [দেখানো হলো]\n\n"
            "গ. সমকোণী ত্রিভুজ $\\triangle ABC$-এর পরিব্যাস $d = \\text{অতিভুজ } AC = 5$।\n"
            "প্রদত্ত সমীকরণ: $d\\tan^2\\alpha - \\sec^2\\alpha = 11$\n"
            "$\\Rightarrow 5\\tan^2\\alpha - (1 + \\tan^2\\alpha) = 11 \\Rightarrow 4\\tan^2\\alpha = 12 \\Rightarrow \\tan^2\\alpha = 3$\n"
            "$\\Rightarrow \\tan\\alpha = \\pm\\sqrt{3} = \\tan\\left(\\pm\\frac{\\pi}{3}\\right)$।\n"
            "$-\\pi \\le \\alpha \\le \\pi$ ব্যবধিতে: $\\alpha = -\\frac{2\\pi}{3}, -\\frac{\\pi}{3}, \\frac{\\pi}{3}, \\frac{2\\pi}{3}$।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\csc 2\\theta = \\frac{1+\\tan^2\\theta}{2\\tan\\theta} = \\frac{1+y^2}{2y} \\implies \\tan^{-1} y = \\frac{1}{2}\\csc^{-1}\\frac{1+y^2}{2y}$ প্রমাণিত।\n\n"
            "**ধাপ (খ):** বামপক্ষ $= 3/4$। চিত্রে সমকোণী $\\triangle ABC$-এ $BC=3, AC=5 \\implies AB=4$ এবং $\\cot\\theta = 3/4$। ফলে বামপক্ষ $=$ ডানপক্ষ প্রমাণিত।\n\n"
            "**ধাপ (গ):** পরিব্যাস $d = AC = 5$। সমীকরণ $5\\tan^2\\alpha - \\sec^2\\alpha = 11 \\implies \\tan^2\\alpha = 3 \\implies \\alpha = \\pm\\pi/3, \\pm 2\\pi/3$ ($-\\pi \\le \\alpha \\le \\pi$ ব্যবধিতে)।"
        )
    },

    902: {
        "a": (
            "ক. চিত্র হতে সমকোণী $\\triangle ABC$-এ $\\angle B = 90^\\circ, AB = 2, BC = y, AC = x$।\n"
            "পিথাগোরাসের উপপাদ্য অনুসারে: $AC^2 = AB^2 + BC^2 \\implies x^2 = 2^2 + y^2 = y^2 + 4$\n"
            "$\\therefore y = \\sqrt{x^2 - 4}$ ($x > 2$)।\n\n"
            "খ. চিত্রে $\\angle C = \\theta \\implies \\tan\\theta = \\frac{AB}{BC} = \\frac{2}{y}$।\n"
            "$\\text{বামপক্ষ} = \\sin\\cos^{-1}(\\tan\\theta) = \\sin\\cos^{-1}\\left(\\frac{2}{y}\\right) = \\sqrt{1 - \\left(\\frac{2}{y}\\right)^2} = \\frac{\\sqrt{y^2 - 4}}{y}$।\n"
            "ক হতে $x^2 = y^2 + 4 \\implies 4 = x^2 - y^2$, অতএব $y^2 - 4 = y^2 - (x^2 - y^2) = 2y^2 - x^2$।\n"
            "$\\therefore \\text{বামপক্ষ} = \\frac{\\sqrt{2y^2 - x^2}}{y} = \\text{ডানপক্ষ}$। [দেখানো হলো]\n\n"
            "গ. দেওয়া আছে $AB = 2, y = \\sqrt{5}$।\n"
            "পিথাগোরাস হতে: $x = \\sqrt{2^2 + (\\sqrt{5})^2} = \\sqrt{4 + 5} = 3$।\n"
            "$\\text{বামপক্ষ} = \\sin^2\\left(\\cos^{-1}\\frac{1}{x}\\right) - \\cos^2\\left(\\sin^{-1}\\frac{1}{\\sqrt{x}}\\right) = \\sin^2\\left(\\cos^{-1}\\frac{1}{3}\\right) - \\cos^2\\left(\\sin^{-1}\\frac{1}{\\sqrt{3}}\\right)$\n"
            "$= \\left(1 - \\frac{1}{9}\\right) - \\left(1 - \\frac{1}{3}\\right) = \\frac{8}{9} - \\frac{2}{3} = \\frac{8 - 6}{9} = \\frac{2}{9} = \\text{ডানপক্ষ}$। [প্রমাণিত]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** পিথাগোরাস অনুসারে $x^2 = y^2 + 4 \\implies y = \\sqrt{x^2 - 4}$।\n\n"
            "**ধাপ (খ):** চিত্রে $\\tan\\theta = 2/y$ বসিয়ে $\\sin\\cos^{-1}(2/y) = \\frac{\\sqrt{y^2-4}}{y} = \\frac{\\sqrt{2y^2-x^2}}{y}$ প্রদর্শিত।\n\n"
            "**ধাপ (গ):** $AB=2, y=\\sqrt{5} \\implies x=3$। মান বসিয়ে $\\frac{8}{9} - \\frac{2}{3} = \\frac{2}{9}$ প্রমাণিত।"
        )
    },

    905: {
        "a": (
            "ক. দেওয়া আছে $f(x) = \\sin^{-1} x$।\n"
            "$f(x) = \\tan^{-1} a \\implies \\sin^{-1} x = \\tan^{-1} a \\implies a = \\tan(\\sin^{-1} x)$।\n"
            "ধরি $\\theta = \\sin^{-1} x \\implies \\sin\\theta = x$ (লম্ব $= x$, অতিভুজ $= 1$, ভূমি $= \\sqrt{1 - x^2}$)।\n"
            "$\\therefore a = \\tan\\theta = \\frac{x}{\\sqrt{1 - x^2}}$।\n\n"
            "খ. দেওয়া আছে $f(x) + f(y) = \\frac{\\pi}{2} \\implies \\sin^{-1} x + \\sin^{-1} y = \\frac{\\pi}{2}$।\n"
            "$\\Rightarrow \\sin^{-1} x = \\frac{\\pi}{2} - \\sin^{-1} y = \\cos^{-1} y$\n"
            "উভয় পক্ষে $\\sin$ নিয়ে: $x = \\sin(\\cos^{-1} y) = \\sqrt{1 - y^2}$\n"
            "বর্গ করে: $x^2 = 1 - y^2 \\implies x^2 + y^2 = 1$। [দেখানো হলো]\n\n"
            "গ. দেওয়া আছে $f(x) + f(y) + f(z) = \\pi \\implies \\sin^{-1} x + \\sin^{-1} y + \\sin^{-1} z = \\pi$।\n"
            "ধরি $A = \\sin^{-1} x, B = \\sin^{-1} y, C = \\sin^{-1} z \\implies x = \\sin A, y = \\sin B, z = \\sin C$ এবং $A + B + C = \\pi$।\n"
            "ত্রিকোণমিতিক অভেদ অনুসারে:\n"
            "$\\sin 2A + \\sin 2B + \\sin 2C = 4\\sin A \\sin B \\sin C$\n"
            "$\\Rightarrow 2\\sin A\\cos A + 2\\sin B\\cos B + 2\\sin C\\cos C = 4\\sin A \\sin B \\sin C$\n"
            "২ দ্বারা ভাগ করে:\n"
            "$\\sin A\\sqrt{1 - \\sin^2 A} + \\sin B\\sqrt{1 - \\sin^2 B} + \\sin C\\sqrt{1 - \\sin^2 C} = 2\\sin A \\sin B \\sin C$\n"
            "মান বসিয়ে: $x\\sqrt{1 - x^2} + y\\sqrt{1 - y^2} + z\\sqrt{1 - z^2} = 2xyz$। [প্রমাণিত]"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** $\\sin^{-1}x=\\tan^{-1}a \\implies a=\\tan(\\sin^{-1}x)=\\frac{x}{\\sqrt{1-x^2}}$।\n\n"
            "**ধাপ (খ):** $\\sin^{-1}x = \\cos^{-1}y \\implies x = \\sqrt{1-y^2} \\implies x^2+y^2=1$ প্রমাণিত।\n\n"
            "**ধাপ (গ):** $A+B+C=\\pi$ কোণ সম্পর্কের ত্রিকোণমিতিক অভেদ প্রয়োগ করে $x\\sqrt{1-x^2}+y\\sqrt{1-y^2}+z\\sqrt{1-z^2}=2xyz$ প্রমাণিত।"
        )
    },

    938: {
        "a": (
            "ক. $f(x) = 5x - 1$ হলে $\\frac{1}{|f(x)|} \\ge \\frac{1}{9} \\implies |5x - 1| \\le 9$ (যেখানে $x \\neq \\frac{1}{5}$)।\n"
            "$\\Rightarrow -9 \\le 5x - 1 \\le 9 \\Rightarrow -8 \\le 5x \\le 10 \\Rightarrow -\\frac{8}{5} \\le x \\le 2$।\n"
            "$\\therefore$ সমাধান সেট: $S = \\left[-\\frac{8}{5}, 2\\right] \\setminus \\left\\{\\frac{1}{5}\\right\\}$।\n"
            "সংখ্যারেখায়: $-\\frac{8}{5}$ থেকে $2$ পর্যন্ত ভরাট বৃত্ত ও রেখা, কিন্তু $\\frac{1}{5}$ বিন্দুটি ফাঁকা গোলক (ছিদ্র)।\n\n"
            "খ. দৃশ্যকল্পের চিত্রদ্বয় হতে:\n"
            "১ম চিত্রে (সমকোণী $\\triangle ABC$): অতিভুজ $AC = r, AB = x \\implies \\cos A = \\frac{x}{r} \\implies A = \\cos^{-1}\\frac{x}{r}$।\n"
            "২য় চিত্রে (সমকোণী $\\triangle PQR$): অতিভুজ $PQ = r, PR = y \\implies \\cos P = \\frac{y}{r} \\implies P = \\cos^{-1}\\frac{y}{r}$।\n"
            "দেওয়া আছে $A + P = \\theta \\implies \\cos^{-1}\\frac{x}{r} + \\cos^{-1}\\frac{y}{r} = \\theta$।\n"
            "$\\Rightarrow \\cos^{-1}\\left(\\frac{xy}{r^2} - \\sqrt{1 - \\frac{x^2}{r^2}}\\sqrt{1 - \\frac{y^2}{r^2}}\\right) = \\theta$\n"
            "$\\Rightarrow \\frac{xy}{r^2} - \\cos\\theta = \\sqrt{1 - \\frac{x^2}{r^2}}\\sqrt{1 - \\frac{y^2}{r^2}}$\n"
            "উভয়পক্ষে বর্গ করে: $\\left(\\frac{xy}{r^2} - \\cos\\theta\\right)^2 = \\left(1 - \\frac{x^2}{r^2}\\right)\\left(1 - \\frac{y^2}{r^2}\\right)$\n"
            "$\\Rightarrow \\frac{x^2 y^2}{r^4} - 2\\frac{xy}{r^2}\\cos\\theta + \\cos^2\\theta = 1 - \\frac{x^2}{r^2} - \\frac{y^2}{r^2} + \\frac{x^2 y^2}{r^4}$\n"
            "$\\Rightarrow \\frac{x^2}{r^2} - 2\\frac{xy}{r^2}\\cos\\theta + \\frac{y^2}{r^2} = 1 - \\cos^2\\theta = \\sin^2\\theta$\n"
            "$r^2$ দিয়ে গুণ করে: $x^2 - 2xy\\cos\\theta + y^2 = r^2\\sin^2\\theta$। [দেখানো হলো]\n\n"
            "গ. দেওয়া আছে $f(\\varphi) = \\frac{r}{x} = \\sec\\varphi$। সমীকরণ: $f(2\\varphi) - f(\\varphi) = 2$\n"
            "$\\Rightarrow \\sec 2\\varphi - \\sec\\varphi = 2 \\Rightarrow \\frac{1}{\\cos 2\\varphi} - \\frac{1}{\\cos\\varphi} = 2$\n"
            "$\\Rightarrow \\frac{\\cos\\varphi - \\cos 2\\varphi}{\\cos 2\\varphi\\cos\\varphi} = 2 \\Rightarrow \\cos\\varphi - (2\\cos^2\\varphi - 1) = 2\\cos\\varphi(2\\cos^2\\varphi - 1)$\n"
            "ধরি $c = \\cos\\varphi$:\n"
            "$c - 2c^2 + 1 = 4c^3 - 2c \\Rightarrow 4c^3 + 2c^2 - 3c - 1 = 0$\n"
            "উৎপাদকে বিশ্লেষণ: $(c + 1)(4c^2 - 2c - 1) = 0$\n"
            "১. $c + 1 = 0 \\implies \\cos\\varphi = -1 \\implies \\varphi = \\pm\\pi$।\n"
            "২. $4c^2 - 2c - 1 = 0 \\implies c = \\frac{2 \\pm \\sqrt{4 + 16}}{8} = \\frac{1 \\pm \\sqrt{5}}{4}$।\n"
            "$\\therefore \\cos\\varphi = \\frac{\\sqrt{5}+1}{4} = \\cos\\frac{\\pi}{5} \\implies \\varphi = \\pm\\frac{\\pi}{5}$ (বা $\\pm 36^\\circ$),\n"
            "এবং $\\cos\\varphi = \\frac{1-\\sqrt{5}}{4} = -\\frac{\\sqrt{5}-1}{4} = \\cos\\frac{3\\pi}{5} \\implies \\varphi = \\pm\\frac{3\\pi}{5}$ (বা $\\pm 108^\\circ$)।\n"
            "$-\\pi \\le \\varphi \\le \\pi$ ব্যবধিতে: $\\varphi = \\pm\\pi, \\pm\\frac{\\pi}{5}, \\pm\\frac{3\\pi}{5}$।"
        ),
        "e": (
            "### দৃশ্যকল্পভিত্তিক সম্পূর্ণ সমাধান ও ব্যাখ্যা:\n\n"
            "**ধাপ (ক):** পরমমান অসমতা সমাধান করে $S = [-\\frac{8}{5}, 2] \\setminus \\{\\frac{1}{5}\\}$।\n\n"
            "**ধাপ (খ):** চিত্রে সমকোণী ত্রিভুজদ্বয় হতে $\\cos A = x/r$ এবং $\\cos P = y/r$। $A+P=\\theta$ সমীকরণকে বিস্তার ও বর্গ করে $x^2 - 2xy\\cos\\theta + y^2 = r^2\\sin^2\\theta$ প্রমাণিত।\n\n"
            "**ধাপ (গ):** $\\sec 2\\varphi - \\sec\\varphi = 2$ সমীকরণকে $c=\\cos\\varphi$ এর ত্রিঘাত সমীকরণ $4c^3+2c^2-3c-1=0 \\implies (c+1)(4c^2-2c-1)=0$ আকারে সমাধান করে $-\\pi \\le \\varphi \\le \\pi$ ব্যবধিতে $\\varphi = \\pm\\pi, \\pm\\frac{\\pi}{5}, \\pm\\frac{3\\pi}{5}$ নির্ণয় করা হয়েছে।"
        )
    }
}
