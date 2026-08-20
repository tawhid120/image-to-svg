# -*- coding: utf-8 -*-
"""Direct Right-Angled Triangle and Inverse-to-Inverse Transformation Explanations.
Eliminates dummy variable substitutions (theta, alpha, beta) and uses pure direct inverse trig transformations.
"""

DIRECT_INVERSE_EXPLANATIONS = {
    3: (
        "$\\cos^2\\left(\\tan^{-1}\\frac{1}{\\sqrt{2}}\\right)$ এর মান নির্ণয়:\n\n"
        "১. $\\tan^{-1}\\left(\\frac{1}{\\sqrt{2}}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• লম্ব $= 1$, ভূমি $= \\sqrt{2}$\n"
        "• পিথাগোরাসের উপপাদ্য অনুসারে, অতিভুজ $= \\sqrt{1^2 + (\\sqrt{2})^2} = \\sqrt{1 + 2} = \\sqrt{3}$\n"
        "সুতরাং, $\\tan^{-1}\\left(\\frac{1}{\\sqrt{2}}\\right) = \\cos^{-1}\\left(\\frac{\\text{ভূমি}}{\\text{অতিভুজ}}\\right) = \\cos^{-1}\\left(\\frac{\\sqrt{2}}{\\sqrt{3}}\\right)$\n\n"
        "২. মূল রাশিতে বসিয়ে পাই:\n"
        "$\\cos^2\\left(\\tan^{-1}\\frac{1}{\\sqrt{2}}\\right) = \\left[\\cos\\left(\\cos^{-1}\\frac{\\sqrt{2}}{\\sqrt{3}}\\right)\\right]^2 = \\left(\\frac{\\sqrt{2}}{\\sqrt{3}}\\right)^2 = \\frac{2}{3}$।"
    ),

    5: (
        "$\\cos(\\sin^{-1} x)$ এর মান নির্ণয়:\n\n"
        "১. $\\sin^{-1} x = \\sin^{-1}\\left(\\frac{x}{1}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• লম্ব $= x$, অতিভুজ $= 1$\n"
        "• ভূমি $= \\sqrt{1^2 - x^2} = \\sqrt{1 - x^2}$\n"
        "সরাসরি রূপান্তর: $\\sin^{-1} x = \\cos^{-1}\\left(\\frac{\\text{ভূমি}}{\\text{অতিভুজ}}\\right) = \\cos^{-1}\\left(\\sqrt{1 - x^2}\\right)$\n\n"
        "২. অতএব:\n"
        "$\\cos(\\sin^{-1} x) = \\cos\\left(\\cos^{-1}\\sqrt{1 - x^2}\\right) = \\sqrt{1 - x^2}$।"
    ),

    7: (
        "$\\tan^{-1}\\frac{3}{4}$ এর মান নির্ণয়:\n\n"
        "১. ইনভার্স ট্যান থেকে ইনভার্স সাইনে রূপান্তরের প্রমিত সূত্র:\n"
        "$2\\tan^{-1} x = \\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right) \\implies \\tan^{-1} x = \\frac{1}{2}\\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right)$\n\n"
        "২. $x = \\frac{3}{4}$ বসিয়ে পাই:\n"
        "$\\tan^{-1}\\frac{3}{4} = \\frac{1}{2}\\sin^{-1}\\left(\\frac{2\\cdot\\frac{3}{4}}{1+\\left(\\frac{3}{4}\\right)^2}\\right) = \\frac{1}{2}\\sin^{-1}\\left(\\frac{\\frac{3}{2}}{1+\\frac{9}{16}}\\right) = \\frac{1}{2}\\sin^{-1}\\left(\\frac{\\frac{3}{2}}{\\frac{25}{16}}\\right) = \\frac{1}{2}\\sin^{-1}\\left(\\frac{24}{25}\\right)$।"
    ),

    12: (
        "$\\sin^{-1} x = \\cot^{-1}\\frac{1}{2}$ সমীকরণের সমাধান:\n\n"
        "১. ডানপক্ষের $\\cot^{-1}\\left(\\frac{1}{2}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• ভূমি $= 1$, লম্ব $= 2$\n"
        "• অতিভুজ $= \\sqrt{1^2 + 2^2} = \\sqrt{5}$\n"
        "সরাসরি রূপান্তর: $\\cot^{-1}\\frac{1}{2} = \\sin^{-1}\\left(\\frac{\\text{লম্ব}}{\\text{অতিভুজ}}\\right) = \\sin^{-1}\\left(\\frac{2}{\\sqrt{5}}\\right)$\n\n"
        "২. সমীকরণে বসিয়ে পাই:\n"
        "$\\sin^{-1} x = \\sin^{-1}\\left(\\frac{2}{\\sqrt{5}}\\right) \\implies x = \\frac{2}{\\sqrt{5}}$।"
    ),

    26: (
        "$\\operatorname{cosec}^2(\\sec^{-1}\\sqrt{5})$ এর মান নির্ণয়:\n\n"
        "১. $\\sec^{-1}\\left(\\frac{\\sqrt{5}}{1}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• অতিভুজ $= \\sqrt{5}$, ভূমি $= 1$\n"
        "• লম্ব $= \\sqrt{(\\sqrt{5})^2 - 1^2} = \\sqrt{5 - 1} = \\sqrt{4} = 2$\n"
        "সরাসরি রূপান্তর: $\\sec^{-1}\\sqrt{5} = \\operatorname{cosec}^{-1}\\left(\\frac{\\text{অতিভুজ}}{\\text{লম্ব}}\\right) = \\operatorname{cosec}^{-1}\\left(\\frac{\\sqrt{5}}{2}\\right)$\n\n"
        "২. মূল রাশিতে বসিয়ে পাই:\n"
        "$\\operatorname{cosec}^2(\\sec^{-1}\\sqrt{5}) = \\left[\\operatorname{cosec}\\left(\\operatorname{cosec}^{-1}\\frac{\\sqrt{5}}{2}\\right)\\right]^2 = \\left(\\frac{\\sqrt{5}}{2}\\right)^2 = \\frac{5}{4}$।"
    ),

    29: (
        "$\\cot^{-1} 2 - \\cot^{-1} 5$ এর মান নির্ণয়:\n\n"
        "১. ইনভার্স সূত্রানুসারে: $\\cot^{-1} 2 = \\tan^{-1}\\frac{1}{2}$ এবং $\\cot^{-1} 5 = \\tan^{-1}\\frac{1}{5}$\n\n"
        "২. $\\tan^{-1} x - \\tan^{-1} y = \\tan^{-1}\\left(\\frac{x - y}{1 + xy}\\right)$ সূত্র প্রয়োগ করে:\n"
        "$\\tan^{-1}\\frac{1}{2} - \\tan^{-1}\\frac{1}{5} = \\tan^{-1}\\left(\\frac{\\frac{1}{2} - \\frac{1}{5}}{1 + \\frac{1}{2}\\cdot\\frac{1}{5}}\\right) = \\tan^{-1}\\left(\\frac{\\frac{3}{10}}{\\frac{11}{10}}\\right) = \\tan^{-1}\\left(\\frac{3}{11}\\right)$।"
    ),

    30: (
        "$\\tan\\left(\\cos^{-1}\\frac{1}{\\sqrt{3}}\\right)$ এর মান নির্ণয়:\n\n"
        "১. $\\cos^{-1}\\left(\\frac{1}{\\sqrt{3}}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• ভূমি $= 1$, অতিভুজ $= \\sqrt{3}$\n"
        "• লম্ব $= \\sqrt{(\\sqrt{3})^2 - 1^2} = \\sqrt{3 - 1} = \\sqrt{2}$\n"
        "সরাসরি রূপান্তর: $\\cos^{-1}\\frac{1}{\\sqrt{3}} = \\tan^{-1}\\left(\\frac{\\text{লম্ব}}{\\text{ভূমি}}\\right) = \\tan^{-1}\\left(\\frac{\\sqrt{2}}{1}\\right) = \\tan^{-1}\\sqrt{2}$\n\n"
        "২. অতএব:\n"
        "$\\tan\\left(\\cos^{-1}\\frac{1}{\\sqrt{3}}\\right) = \\tan(\\tan^{-1}\\sqrt{2}) = \\sqrt{2}$।"
    ),

    31: (
        "$\\sin^{-1}\\frac{3}{5} + \\cos^{-1}\\frac{4}{5}$ এর মান নির্ণয়:\n\n"
        "১. $\\cos^{-1}\\left(\\frac{4}{5}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• ভূমি $= 4$, অতিভুজ $= 5 \\implies$ লম্ব $= \\sqrt{5^2 - 4^2} = 3$\n"
        "সরাসরি রূপান্তর: $\\cos^{-1}\\frac{4}{5} = \\sin^{-1}\\left(\\frac{3}{5}\\right) = \\tan^{-1}\\left(\\frac{3}{4}\\right)$\n\n"
        "২. রাশিটির মান:\n"
        "$\\sin^{-1}\\frac{3}{5} + \\cos^{-1}\\frac{4}{5} = \\sin^{-1}\\frac{3}{5} + \\sin^{-1}\\frac{3}{5} = 2\\tan^{-1}\\frac{3}{4}$\n\n"
        "৩. $2\\tan^{-1} x = \\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right)$ সূত্রে $x = \\frac{3}{4}$ বসালে:\n"
        "$= \\sin^{-1}\\left(\\frac{2\\cdot\\frac{3}{4}}{1+(\\frac{3}{4})^2}\\right) = \\sin^{-1}\\left(\\frac{24}{25}\\right)$।"
    ),

    36: (
        "$\\cos(\\cot^{-1} 2)$ এর মান নির্ণয়:\n\n"
        "১. $\\cot^{-1}\\left(\\frac{2}{1}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• ভূমি $= 2$, লম্ব $= 1$\n"
        "• অতিভুজ $= \\sqrt{2^2 + 1^2} = \\sqrt{5}$\n"
        "সরাসরি রূপান্তর: $\\cot^{-1} 2 = \\cos^{-1}\\left(\\frac{\\text{ভূমি}}{\\text{অতিভুজ}}\\right) = \\cos^{-1}\\left(\\frac{2}{\\sqrt{5}}\\right)$\n\n"
        "২. অতএব:\n"
        "$\\cos(\\cot^{-1} 2) = \\cos\\left(\\cos^{-1}\\frac{2}{\\sqrt{5}}\\right) = \\frac{2}{\\sqrt{5}}$।"
    ),

    37: (
        "$\\tan(\\cot^{-1}(\\tan(\\cos^{-1} x)))$ এর মান নির্ণয় (শিকল রূপান্তর):\n\n"
        "১. $\\cos^{-1} x = \\cos^{-1}\\left(\\frac{x}{1}\\right)$ এর জন্য সমকোণী ত্রিভুজ: ভূমি $= x$, অতিভুজ $= 1$, লম্ব $= \\sqrt{1-x^2}$\n"
        "$\\implies \\cos^{-1} x = \\tan^{-1}\\left(\\frac{\\sqrt{1-x^2}}{x}\\right)$\n\n"
        "২. $\\tan(\\cos^{-1} x) = \\tan\\left(\\tan^{-1}\\frac{\\sqrt{1-x^2}}{x}\\right) = \\frac{\\sqrt{1-x^2}}{x}$\n\n"
        "৩. $\\cot^{-1}\\left(\\frac{\\sqrt{1-x^2}}{x}\\right) = \\tan^{-1}\\left(\\frac{x}{\\sqrt{1-x^2}}\right)$\n\n"
        "৪. অতএব, $\\tan\\left(\\cot^{-1}\\left(\\frac{\\sqrt{1-x^2}}{x}\\right)\\right) = \\tan\\left(\\tan^{-1}\\frac{x}{\\sqrt{1-x^2}}\\right) = \\frac{x}{\\sqrt{1-x^2}}$।"
    ),

    41: (
        "$\\arctan\\left\\{\\sin\\left(\\arccos\\frac{\\sqrt{2}}{\\sqrt{3}}\\right)\\right\\}$ এর মান নির্ণয়:\n\n"
        "১. $\\arccos\\left(\\frac{\\sqrt{2}}{\\sqrt{3}}\\right)$ এর সমকোণী ত্রিভুজ: ভূমি $= \\sqrt{2}$, অতিভুজ $= \\sqrt{3}$, লম্ব $= \\sqrt{3 - 2} = 1$\n"
        "$\\implies \\arccos\\frac{\\sqrt{2}}{\\sqrt{3}} = \\arcsin\\left(\\frac{1}{\\sqrt{3}}\\right)$\n\n"
        "২. $\\sin\\left(\\arcsin\\frac{1}{\\sqrt{3}}\\right) = \\frac{1}{\\sqrt{3}}$\n\n"
        "৩. অতএব, $\\arctan\\left(\\frac{1}{\\sqrt{3}}\\right) = \\frac{\\pi}{6}$ (যেহেতু $\\tan\\frac{\\pi}{6} = \\frac{1}{\\sqrt{3}}$)।"
    ),

    47: (
        "$\\cot^{-1} p = \\operatorname{cosec}^{-1}\\frac{3}{2}$ হলে $p$ এর মান:\n\n"
        "১. ডানপক্ষের $\\operatorname{cosec}^{-1}\\left(\\frac{3}{2}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• অতিভুজ $= 3$, লম্ব $= 2$\n"
        "• ভূমি $= \\sqrt{3^2 - 2^2} = \\sqrt{9 - 4} = \\sqrt{5}$\n"
        "সরাসরি রূপান্তর: $\\operatorname{cosec}^{-1}\\frac{3}{2} = \\cot^{-1}\\left(\\frac{\\text{ভূমি}}{\\text{লম্ব}}\\right) = \\cot^{-1}\\left(\\frac{\\sqrt{5}}{2}\\right)$\n\n"
        "২. সমীকরণে বসিয়ে পাই:\n"
        "$\\cot^{-1} p = \\cot^{-1}\\left(\\frac{\\sqrt{5}}{2}\\right) \\implies p = \\frac{\\sqrt{5}}{2}$।"
    ),

    59: (
        "$g(y) + g\\left(\\sqrt{1-y^2}\\right) = \\sin^{-1} y + \\sin^{-1}\\sqrt{1-y^2}$ এর মান:\n\n"
        "১. $\\sin^{-1}\\sqrt{1-y^2} = \\sin^{-1}\\left(\\frac{\\sqrt{1-y^2}}{1}\\right)$ এর সমকোণী ত্রিভুজ হতে:\n"
        "• লম্ব $= \\sqrt{1-y^2}$, অতিভুজ $= 1$\n"
        "• ভূমি $= \\sqrt{1^2 - (\\sqrt{1-y^2})^2} = \\sqrt{1 - (1 - y^2)} = \\sqrt{y^2} = y$\n"
        "সরাসরি রূপান্তর: $\\sin^{-1}\\sqrt{1-y^2} = \\cos^{-1}\\left(\\frac{\\text{ভূমি}}{\\text{অতিভুজ}}\\right) = \\cos^{-1} y$\n\n"
        "২. অতএব, রাশিটির মান:\n"
        "$\\sin^{-1} y + \\cos^{-1} y = \\frac{\\pi}{2}$ (বিপরীত ত্রিকোণমিতিক পূরক কোণ সূত্র)।"
    ),

    61: (
        "**উদ্দীপক:** $\\cot\\theta = k$ সমীকরণের সাধারণ সমাধান $\\theta = n\\pi + \\alpha$\n"
        "**প্রশ্ন:** $k = \\frac{1}{\\sqrt{3}}$ হলে $\\alpha =$ কত?\n\n"
        "**ধাপ ১: উদ্দীপক ও সাধারণ সমাধান সূত্রের তুলনা**\n"
        "আমরা জানি, ত্রিকোণমিতিতে $\\cot\\theta = \\cot\\alpha$ আকারের সমীকরণের সাধারণ সমাধান সূত্র হলো:\n"
        "$$\\theta = n\\pi + \\alpha \\quad (\\text{যেখানে } n \\in \\mathbb{Z})$$\n"
        "উদ্দীপকে প্রদত্ত সমীকরণ $\\cot\\theta = k$ এবং প্রমিত সূত্র $\\cot\\theta = \\cot\\alpha$ তুলনা করলে স্পষ্ট বোঝা যায়:\n"
        "$$\\cot\\alpha = k$$\n\n"
        "**ধাপ ২: $k$-এর মান বসানো**\n"
        "প্রশ্নে দেওয়া আছে $k = \\frac{1}{\\sqrt{3}}$। সুতরাং $k$-এর স্থানে $\\frac{1}{\\sqrt{3}}$ বসালে পাই:\n"
        "$$\\cot\\alpha = \\frac{1}{\\sqrt{3}}$$\n\n"
        "**ধাপ ৩: সরাসরি কোণ বা ইনভার্স নির্ণয়**\n"
        "আমরা জানি, $60^\\circ$ বা $\\frac{\\pi}{3}$ কোণের $\\cot$-এর মান $\\frac{1}{\\sqrt{3}}$ (কারণ $\\tan\\frac{\\pi}{3} = \\sqrt{3} \\implies \\cot\\frac{\\pi}{3} = \\frac{1}{\\sqrt{3}}$)।\n"
        "অতএব:\n"
        "$$\\cot\\alpha = \\cot\\left(\\frac{\\pi}{3}\\right)$$\n"
        "বা ইনভার্স দিয়ে প্রকাশ করলে:\n"
        "$$\\alpha = \\cot^{-1}\\left(\\frac{1}{\\sqrt{3}}\\right) = \\tan^{-1}(\\sqrt{3}) = \\frac{\\pi}{3}$$\n\n"
        "**উপসংহার:** $\\alpha$-এর নির্ণেয় মান হলো $\\frac{\\pi}{3}$ (সঠিক উত্তর: গ)।"
    ),

    63: (
        "$x = \\sin(\\cos^{-1} y)$ হলে $x^2 + y^2$ এর মান:\n\n"
        "১. $\\cos^{-1} y = \\cos^{-1}\\left(\\frac{y}{1}\\right)$ এর সমকোণী ত্রিভুজ হতে:\n"
        "• ভূমি $= y$, অতিভুজ $= 1$\n"
        "• লম্ব $= \\sqrt{1^2 - y^2} = \\sqrt{1 - y^2}$\n"
        "সরাসরি রূপান্তর: $\\cos^{-1} y = \\sin^{-1}\\left(\\frac{\\text{লম্ব}}{\\text{অতিভুজ}}\\right) = \\sin^{-1}\\left(\\sqrt{1 - y^2}\\right)$\n\n"
        "২. মূল রাশিতে বসিয়ে:\n"
        "$x = \\sin\\left(\\sin^{-1}\\sqrt{1 - y^2}\\right) = \\sqrt{1 - y^2}$\n\n"
        "৩. উভয়পক্ষকে বর্গ করে পাই:\n"
        "$x^2 = 1 - y^2 \\implies x^2 + y^2 = 1$।"
    ),

    70: (
        "$\\sin\\left(2\\tan^{-1}\\frac{1}{2}\\right)$ এর মান নির্ণয়:\n\n"
        "১. ইনভার্স ট্যান থেকে ইনভার্স সাইনে সরাসরি দ্বিগুণ কোণ সূত্র:\n"
        "$2\\tan^{-1} x = \\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right)$\n\n"
        "২. $x = \\frac{1}{2}$ বসিয়ে পাই:\n"
        "$2\\tan^{-1}\\frac{1}{2} = \\sin^{-1}\\left(\\frac{2\\cdot\\frac{1}{2}}{1 + \\left(\\frac{1}{2}\\right)^2}\\right) = \\sin^{-1}\\left(\\frac{1}{1 + \\frac{1}{4}}\\right) = \\sin^{-1}\\left(\\frac{1}{\\frac{5}{4}}\\right) = \\sin^{-1}\\left(\\frac{4}{5}\\right)$\n\n"
        "৩. অতএব:\n"
        "$\\sin\\left(2\\tan^{-1}\\frac{1}{2}\\right) = \\sin\\left(\\sin^{-1}\\frac{4}{5}\\right) = \\frac{4}{5}$।"
    ),

    73: (
        "$\\cos^{-1}\\frac{4}{5}$ এর সঠিক সম্পর্ক নির্ণয়:\n\n"
        "১. $\\cos^{-1}\\left(\\frac{4}{5}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• ভূমি $= 4$, অতিভুজ $= 5$\n"
        "• লম্ব $= \\sqrt{5^2 - 4^2} = \\sqrt{25 - 16} = \\sqrt{9} = 3$\n\n"
        "২. সরাসরি অনুপাতসমূহে রূপান্তর:\n"
        "• $\\sin^{-1}\\left(\\frac{\\text{লম্ব}}{\\text{অতিভুজ}}\\right) = \\sin^{-1}\\left(\\frac{3}{5}\\right)$\n"
        "• $\\tan^{-1}\\left(\\frac{\\text{লম্ব}}{\\text{ভূমি}}\\right) = \\tan^{-1}\\left(\\frac{3}{4}\\right)$\n\n"
        "অতএব, বিকল্পসমূহের মধ্যে সঠিক সম্পর্ক: $\\cos^{-1}\\frac{4}{5} = \\sin^{-1}\\frac{3}{5}$।"
    ),

    78: (
        "$\\sec^2(\\tan^{-1} 2) + \\operatorname{cosec}^2(\\cot^{-1} 3)$ এর মান নির্ণয়:\n\n"
        "১. প্রথম পদ: $\\tan^{-1}\\left(\\frac{2}{1}\\right)$ এর ত্রিভুজে ভূমি $= 1$, লম্ব $= 2$, অতিভুজ $= \\sqrt{1^2 + 2^2} = \\sqrt{5}$\n"
        "$\\implies \\tan^{-1} 2 = \\sec^{-1}\\left(\\frac{\\text{অতিভুজ}}{\\text{ভূমি}}\\right) = \\sec^{-1}\\sqrt{5}$\n"
        "অতএব, $\\sec^2(\\tan^{-1} 2) = [\\sec(\\sec^{-1}\\sqrt{5})]^2 = (\\sqrt{5})^2 = 5$\n\n"
        "২. দ্বিতীয় পদ: $\\cot^{-1}\\left(\\frac{3}{1}\\right)$ এর ত্রিভুজে ভূমি $= 3$, লম্ব $= 1$, অতিভুজ $= \\sqrt{3^2 + 1^2} = \\sqrt{10}$\n"
        "$\\implies \\cot^{-1} 3 = \\operatorname{cosec}^{-1}\\left(\\frac{\\text{অতিভুজ}}{\\text{লম্ব}}\\right) = \\operatorname{cosec}^{-1}\\sqrt{10}$\n"
        "অতএব, $\\operatorname{cosec}^2(\\cot^{-1} 3) = [\\operatorname{cosec}(\\operatorname{cosec}^{-1}\\sqrt{10})]^2 = (\\sqrt{10})^2 = 10$\n\n"
        "৩. মোট মান $= 5 + 10 = 15$।"
    ),

    85: (
        "$f(x) = \\operatorname{cosec}(\\cot^{-1} x)$ হলে $f(2)$ এর মান:\n\n"
        "$f(2) = \\operatorname{cosec}(\\cot^{-1} 2)$\n\n"
        "১. $\\cot^{-1}\\left(\\frac{2}{1}\\right)$ এর সমকোণী ত্রিভুজ হতে:\n"
        "• ভূমি $= 2$, লম্ব $= 1$\n"
        "• অতিভুজ $= \\sqrt{2^2 + 1^2} = \\sqrt{5}$\n"
        "সরাসরি রূপান্তর: $\\cot^{-1} 2 = \\operatorname{cosec}^{-1}\\left(\\frac{\\text{অতিভুজ}}{\\text{লম্ব}}\\right) = \\operatorname{cosec}^{-1}\\sqrt{5}$\n\n"
        "২. অতএব:\n"
        "$f(2) = \\operatorname{cosec}(\\operatorname{cosec}^{-1}\\sqrt{5}) = \\sqrt{5}$।"
    ),

    86: (
        "$\\sin(2\\sin^{-1} x)$ এর মান নির্ণয়:\n\n"
        "১. ইনভার্স সাইন দ্বিগুণ কোণ সূত্র:\n"
        "$2\\sin^{-1} x = \\sin^{-1}\\left(2x\\sqrt{1 - x^2}\\right)$\n\n"
        "২. সরাসরি বসিয়ে পাই:\n"
        "$\\sin(2\\sin^{-1} x) = \\sin\\left(\\sin^{-1}\\left(2x\\sqrt{1 - x^2}\\right)\\right) = 2x\\sqrt{1 - x^2}$।"
    ),

    93: (
        "$\\cot^{-1} 3$ এর মান নির্ণয়:\n\n"
        "১. $\\cot^{-1} 3 = \\tan^{-1}\\frac{1}{3}$\n\n"
        "২. ইনভার্স ট্যানকে ইনভার্স সাইনে রূপান্তরের সূত্র: $\\tan^{-1} x = \\frac{1}{2}\\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right)$\n\n"
        "৩. $x = \\frac{1}{3}$ বসালে:\n"
        "$\\tan^{-1}\\frac{1}{3} = \\frac{1}{2}\\sin^{-1}\\left(\\frac{2\\cdot\\frac{1}{3}}{1+\\frac{1}{9}}\\right) = \\frac{1}{2}\\sin^{-1}\\left(\\frac{\\frac{2}{3}}{\\frac{10}{9}}\\right) = \\frac{1}{2}\\sin^{-1}\\left(\\frac{3}{5}\\right)$।"
    ),

    95: (
        "$\\sin^{-1}\\frac{2}{5} + \\sin^{-1}\\frac{\\sqrt{21}}{5}$ এর মান নির্ণয়:\n\n"
        "১. দ্বিতীয় পদ $\\sin^{-1}\\left(\\frac{\\sqrt{21}}{5}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• লম্ব $= \\sqrt{21}$, অতিভুজ $= 5$\n"
        "• ভূমি $= \\sqrt{5^2 - (\\sqrt{21})^2} = \\sqrt{25 - 21} = \\sqrt{4} = 2$\n"
        "সরাসরি রূপান্তর: $\\sin^{-1}\\left(\\frac{\\sqrt{21}}{5}\\right) = \\cos^{-1}\\left(\\frac{\\text{ভূমি}}{\\text{অতিভুজ}}\\right) = \\cos^{-1}\\left(\\frac{2}{5}\\right)$\n\n"
        "২. মূল রাশিতে বসালে:\n"
        "$\\sin^{-1}\\frac{2}{5} + \\cos^{-1}\\frac{2}{5} = \\frac{\\pi}{2}$ (বিপরীত ত্রিকোণমিতিক পূরক কোণ সূত্র)।"
    ),

    101: (
        "$\\cot k = \\frac{1}{2}$ হলে $\\cot(\\tan^{-1}(\\sec(\\sin^{-1}(\\cot k))))$ এর মান:\n\n"
        "১. $\\cot k = \\frac{1}{2}$ বসিয়ে পাই: $\\cot(\\tan^{-1}(\\sec(\\sin^{-1}\\frac{1}{2})))$\n"
        "২. $\\sin^{-1}\\left(\\frac{1}{2}\\right)$ এর সমকোণী ত্রিভুজ: লম্ব $= 1$, অতিভুজ $= 2$, ভূমি $= \\sqrt{3} \\implies \\sin^{-1}\\frac{1}{2} = \\sec^{-1}\\left(\\frac{2}{\\sqrt{3}}\\right)$\n"
        "৩. $\\sec(\\sec^{-1}\\frac{2}{\\sqrt{3}}) = \\frac{2}{\\sqrt{3}}$\n"
        "৪. $\\tan^{-1}\\left(\\frac{2}{\\sqrt{3}}\\right) = \\cot^{-1}\\left(\\frac{\\sqrt{3}}{2}\\right)$\n"
        "৫. অতএব, $\\cot\\left(\\cot^{-1}\\frac{\\sqrt{3}}{2}\\right) = \\frac{\\sqrt{3}}{2}$।"
    ),

    102: (
        "$2\\tan^{-1}\\sqrt{2} = \\theta$ হলে মান যাচাই:\n\n"
        "১. প্রমিত ইনভার্স রূপান্তর সূত্র:\n"
        "• $\\tan\\theta = \\tan(2\\tan^{-1} x) = \\frac{2x}{1-x^2}$\n"
        "• $\\cos\\theta = \\cos(2\\tan^{-1} x) = \\frac{1-x^2}{1+x^2}$\n"
        "• $\\sin\\theta = \\sin(2\\tan^{-1} x) = \\frac{2x}{1+x^2}$\n\n"
        "২. $x = \\sqrt{2}$ বসিয়ে পাই:\n"
        "• $\\tan\\theta = \\frac{2\\sqrt{2}}{1 - (\\sqrt{2})^2} = \\frac{2\\sqrt{2}}{-1} = -2\\sqrt{2}$\n"
        "• $\\cos\\theta = \\frac{1 - 2}{1 + 2} = -\\frac{1}{3}$\n"
        "• $\\sin\\theta = \\frac{2\\sqrt{2}}{1 + 2} = \\frac{2\\sqrt{2}}{3}$।"
    ),

    121: (
        "$\\cot^{-1} 3$ এর মান নির্ণয়:\n\n"
        "১. $\\cot^{-1} 3 = \\tan^{-1}\\frac{1}{3}$\n"
        "২. $\\tan^{-1} x = \\frac{1}{2}\\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right)$ সূত্রে $x = \\frac{1}{3}$ বসালে:\n"
        "$\\tan^{-1}\\frac{1}{3} = \\frac{1}{2}\\sin^{-1}\\left(\\frac{2\\cdot\\frac{1}{3}}{1+\\frac{1}{9}}\\right) = \\frac{1}{2}\\sin^{-1}\\left(\\frac{3}{5}\\right)$।"
    ),

    151: (
        "$f(x) = \\operatorname{cosec}(\\cot^{-1} x)$ হলে $f(2)$ এর মান:\n\n"
        "১. $\\cot^{-1}\\left(\\frac{2}{1}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• ভূমি $= 2$, লম্ব $= 1$, অতিভুজ $= \\sqrt{2^2 + 1^2} = \\sqrt{5}$\n"
        "সরাসরি রূপান্তর: $\\cot^{-1} 2 = \\operatorname{cosec}^{-1}\\left(\\frac{\\text{অতিভুজ}}{\\text{লম্ব}}\\right) = \\operatorname{cosec}^{-1}\\sqrt{5}$\n\n"
        "২. অতএব, $f(2) = \\operatorname{cosec}(\\operatorname{cosec}^{-1}\\sqrt{5}) = \\sqrt{5}$।"
    ),

    171: (
        "$\\tan^{-1}\\frac{1}{3}$ এর মান নির্ণয়:\n\n"
        "১. ইনভার্স রূপান্তর সূত্র: $\\tan^{-1} x = \\frac{1}{2}\\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right)$\n"
        "২. $x = \\frac{1}{3}$ বসালে:\n"
        "$= \\frac{1}{2}\\sin^{-1}\\left(\\frac{2\\cdot\\frac{1}{3}}{1+\\frac{1}{9}}\\right) = \\frac{1}{2}\\sin^{-1}\\left(\\frac{\\frac{2}{3}}{\\frac{10}{9}}\\right) = \\frac{1}{2}\\sin^{-1}\\left(\\frac{3}{5}\\right)$।"
    ),

    179: (
        "$\\frac{1}{2}\\sin^{-1}\\frac{3}{5}$ এর মান নির্ণয়:\n\n"
        "১. $\\frac{1}{2}\\sin^{-1}\\left(\\frac{2x}{1+x^2}\\right) = \\tan^{-1} x$ সূত্রের সাহায্যে:\n"
        "$\\frac{2x}{1+x^2} = \\frac{3}{5} \\implies 10x = 3 + 3x^2 \\implies 3x^2 - 10x + 3 = 0$\n"
        "বা, $(3x - 1)(x - 3) = 0 \\implies x = \\frac{1}{3}$ (যেহেতু $|x| < 1$)\n\n"
        "২. অতএব, $\\frac{1}{2}\\sin^{-1}\\frac{3}{5} = \\tan^{-1}\\frac{1}{3}$।"
    ),

    192: (
        "$\\frac{1}{2}\\cos^{-1}\\left(\\frac{9}{41}\\right)$ এর মান নির্ণয়:\n\n"
        "১. ইনভার্স সূত্র: $\\frac{1}{2}\\cos^{-1}\\left(\\frac{1-x^2}{1+x^2}\\right) = \\tan^{-1} x$\n\n"
        "২. তুলনা করে পাই:\n"
        "$\\frac{1-x^2}{1+x^2} = \\frac{9}{41} \\implies 41(1-x^2) = 9(1+x^2) \\implies 41 - 41x^2 = 9 + 9x^2$\n"
        "বা, $50x^2 = 32 \\implies x^2 = \\frac{32}{50} = \\frac{16}{25} \\implies x = \\frac{4}{5}$\n\n"
        "৩. অতএব, $\\frac{1}{2}\\cos^{-1}\\left(\\frac{9}{41}\\right) = \\tan^{-1}\\left(\\frac{4}{5}\\right)$।"
    ),

    205: (
        "$y = \\sin^{-1}\\frac{\\sqrt{3}}{2} + \\cos^{-1} x, x = \\frac{3\\sqrt{3}}{\\sqrt{31}}$ হলে $y$ এর মান:\n\n"
        "১. প্রথম পদ: $\\sin^{-1}\\frac{\\sqrt{3}}{2} = \\frac{\\pi}{3} = \\tan^{-1}\\sqrt{3}$\n\n"
        "২. দ্বিতীয় পদ: $\\cos^{-1}\\left(\\frac{3\\sqrt{3}}{\\sqrt{31}}\\right)$ এর সমকোণী ত্রিভুজ হতে:\n"
        "• ভূমি $= 3\\sqrt{3}$, অতিভুজ $= \\sqrt{31}$\n"
        "• লম্ব $= \\sqrt{(\\sqrt{31})^2 - (3\\sqrt{3})^2} = \\sqrt{31 - 27} = \\sqrt{4} = 2$\n"
        "সরাসরি রূপান্তর: $\\cos^{-1}\\left(\\frac{3\\sqrt{3}}{\\sqrt{31}}\\right) = \\tan^{-1}\\left(\\frac{\\text{লম্ব}}{\\text{ভূমি}}\\right) = \\tan^{-1}\\left(\\frac{2}{3\\sqrt{3}}\\right)$\n\n"
        "৩. $\\tan^{-1} A + \\tan^{-1} B = \\tan^{-1}\\left(\\frac{A+B}{1-AB}\\right)$ সূত্রে বসালে:\n"
        "$y = \\tan^{-1}\\left(\\frac{\\sqrt{3} + \\frac{2}{3\\sqrt{3}}}{1 - \\sqrt{3}\\cdot\\frac{2}{3\\sqrt{3}}}\\right) = \\tan^{-1}\\left(\\frac{\\frac{9+2}{3\\sqrt{3}}}{1 - \\frac{2}{3}}\\right) = \\tan^{-1}\\left(\\frac{\\frac{11}{3\\sqrt{3}}}{\\frac{1}{3}}\\right) = \\tan^{-1}\\left(\\frac{11}{\\sqrt{3}}\\right)$।"
    ),

    212: (
        "$\\tan\\left(\\sin^{-1}\\frac{4}{5}\\right)$ এর মান নির্ণয়:\n\n"
        "১. $\\sin^{-1}\\left(\\frac{4}{5}\\right)$ এর সমকোণী ত্রিভুজ হতে:\n"
        "• লম্ব $= 4$, অতিভুজ $= 5$\n"
        "• ভূমি $= \\sqrt{5^2 - 4^2} = \\sqrt{25 - 16} = 3$\n"
        "সরাসরি রূপান্তর: $\\sin^{-1}\\frac{4}{5} = \\tan^{-1}\\left(\\frac{\\text{লম্ব}}{\\text{ভূমি}}\\right) = \\tan^{-1}\\left(\\frac{4}{3}\\right)$\n\n"
        "২. অতএব:\n"
        "$\\tan\\left(\\sin^{-1}\\frac{4}{5}\\right) = \\tan\\left(\\tan^{-1}\\frac{4}{3}\\right) = \\frac{4}{3}$।"
    ),

    548: (
        "$\\sin^{-1}(\\cos(\\tan^{-1} x)) = \\tan^{-1}\\frac{5}{2}$ সমীকরণের সমাধান:\n\n"
        "১. $\\tan^{-1} x = \\tan^{-1}\\left(\\frac{x}{1}\\right)$ এর সমকোণী ত্রিভুজ হতে:\n"
        "• লম্ব $= x$, ভূমি $= 1$, অতিভুজ $= \\sqrt{1+x^2}$\n"
        "$\\implies \\tan^{-1} x = \\cos^{-1}\\left(\\frac{1}{\\sqrt{1+x^2}}\\right)$\n\n"
        "২. $\\cos(\\tan^{-1} x) = \\cos\\left(\\cos^{-1}\\frac{1}{\\sqrt{1+x^2}}\\right) = \\frac{1}{\\sqrt{1+x^2}}$\n\n"
        "৩. $\\sin^{-1}\\left(\\frac{1}{\\sqrt{1+x^2}}\\right)$ এর সমকোণী ত্রিভুজ হতে:\n"
        "• লম্ব $= 1$, অতিভুজ $= \\sqrt{1+x^2}$, ভূমি $= x$\n"
        "$\\implies \\sin^{-1}\\left(\\frac{1}{\\sqrt{1+x^2}}\\right) = \\tan^{-1}\\left(\\frac{1}{x}\\right)$\n\n"
        "৪. প্রশ্নমতে: $\\tan^{-1}\\left(\\frac{1}{x}\\right) = \\tan^{-1}\\left(\\frac{5}{2}\\right) \\implies \\frac{1}{x} = \\frac{5}{2} \\implies x = \\frac{2}{5}$।"
    ),

    620: (
        "$\\sin^{-1} x$ এর সরাসরি সমকোণী ত্রিভুজ রূপান্তর:\n\n"
        "$\\sin^{-1} x = \\sin^{-1}\\left(\\frac{x}{1}\\right)$ এর জন্য সমকোণী ত্রিভুজ হতে:\n"
        "• লম্ব $= x$, অতিভুজ $= 1$\n"
        "• ভূমি $= \\sqrt{1^2 - x^2} = \\sqrt{1 - x^2}$\n\n"
        "সরাসরি ইনভার্স রূপান্তরসমূহ:\n"
        "• $\\text{i. } \\sec^{-1}\\left(\\frac{\\text{অতিভুজ}}{\\text{ভূমি}}\\right) = \\sec^{-1}\\left(\\frac{1}{\\sqrt{1-x^2}}\\right)$ (সঠিক ✓)\n"
        "• $\\text{ii. } \\cos^{-1}\\left(\\frac{\\text{ভূমি}}{\\text{অতিভুজ}}\\right) = \\cos^{-1}\\left(\\sqrt{1-x^2}\\right)$ (সঠিক ✓)\n"
        "• $\\text{iii. } \\cot^{-1}\\left(\\frac{\\text{ভূমি}}{\\text{লম্ব}}\\right) = \\cot^{-1}\\left(\\frac{\\sqrt{1-x^2}}{x}\\right)$ (সঠিক ✓)\n\n"
        "অতএব, i, ii ও iii তিনটি সম্পর্কই সঠিক।"
    )
}
