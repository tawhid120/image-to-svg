# SOLVER GUIDE — স্থির তড়িৎ (HSC পদার্থবিজ্ঞান ২য় পত্র, অধ্যায়-০২)

You are solving HSC / Admission physics questions (Electrostatics). You MUST solve EVERY question
in your assigned batch file correctly and write the results as a JSON file.

## Your task

1. Read your batch data file: `C:\Users\WALTON\Downloads\dari-backup\dari\physics_work\batches\batchNN.json`
   (it contains `{"batch": NN, "questions": [ ... ]}`, each question has `n`, `id`, `type`, `q`,
   `options`, `images`, `src`).
2. For each question with `images` listed: READ each image file with the Read tool
   (path: `C:\Users\WALTON\Downloads\dari-backup\dari\downloaded_diagrams_physics\<filename>`) and
   use the figure data in your solution. If an image cannot be read, solve using the text and note
   nothing special — just solve what is possible.
3. Solve ALL questions. Physics content: HSC ২য় পত্র অধ্যায় ২ (স্থির তড়িৎ): কুলম্বের সূত্র,
   তড়িৎক্ষেত্র, গাউসের সূত্র, তড়িৎ বিভব, তড়িৎ দ্বিমেরু, তড়িৎ ধারকত্ব, সমান্তরাল পাত ধারক,
   পরাবৈদ্যুতিক পদার্থ, তলমাত্রিক চার্জ ঘনত্ব, বিন্দু চার্জ, চার্জিত গোলক ইত্যাদি।
4. Write the results to: `C:\Users\WALTON\Downloads\dari-backup\dari\physics_work\results\batchNN.json`

## Output JSON schema (STRICT)

```json
{
  "<question_id>": {
    "answer_text": "...",
    "explanation_text": "...",
    "mcq_solution_index": 2
  }
}
```

- One entry per question, keyed by `id` (exact string from the batch file).
- `mcq_solution_index`: **only** for questions of type `বহুনির্বাচনি প্রশ্ন` — the 0-based index of
  the correct option. For all other types, OMIT this field.
- `answer_text` and `explanation_text` are plain strings; use `\n` inside the string for line breaks.
- The file must be valid JSON, UTF-8, no trailing commas, no comments.

## Answer formats by question type

### বহুনির্বাচনি প্রশ্ন (MCQ)
- `answer_text` = the correct option's text, cleaned and written in LaTeX math where math appears
  (keep it as a single line). Example: option `$10c.m^{-2}$` correct → `$10\ \mathrm{C\,m^{-2}}$`.
- `explanation_text` = step-by-step solution in Bengali + LaTeX, then a final line
  `ব্যাখ্যা: <one-two sentence summary of the key concept>`. Multiple lines separated by `\n`.

### সৃজনশীল প্রশ্ন (Creative)
- `answer_text` = full solution for parts **ক.**, **খ.**, **গ.** (use `**ক.**`, `**খ.**`, `**গ.**`
  markers), each part on its own line(s), Bengali + LaTeX.
- `explanation_text` = a 1–3 line summary of the whole solution.

### গাণিতিক ও বিশ্লেষণধর্মী প্রশ্ন (Numerical/Analytical)
- `answer_text` = complete worked calculation with formulas and final answer, in LaTeX.
- `explanation_text` = 1–2 line summary. 

### জ্ঞানমূলক প্রশ্ন (Conceptual)
- `answer_text` = the answer / definition in Bengali (LaTeX for symbols).
- `explanation_text` = short reasoning (2–3 lines) why.

## LaTeX formatting rules (FOLLOW EXACTLY)

- Inline math in `$...$`. Display math not needed.
- `\frac{a}{b}`, `\sqrt{x}`, `x^{2}`, `10^{-6}`, `\pi`, `\theta`, `\alpha`, `\beta`, `\rho`,
  `\sigma`, `\varepsilon`, `\Delta`, `\times`, `\Rightarrow` (or ⇒), `\approx`, `\pm`,
  `\mu_{0}`, `\epsilon_{0}`, `\vec{E}`, `\vec{F}`, `Q`, `q`, `C`, `V`, `d`, `A`.
- Constants: `k = 9 \times 10^{9}\ \mathrm{N\,m^{2}\,C^{-2}}`, `\epsilon_{0} = 8.85 \times 10^{-12}\ \mathrm{C^{2}\,N^{-1}\,m^{-2}}`.
- Units: `\mathrm{C}`, `\mathrm{V}`, `\mathrm{N}`, `\mathrm{J}`, `\mathrm{m}`, `\mathrm{F}`,
  `\mathrm{N/C}`, `\mathrm{V/m}`, `\mu\mathrm{C}` etc. Put units inside math or plain text — be consistent.
- Write the whole solution in Bengali; math inside `$...$`. Bengali sentence markers: `।` and line breaks.
- Correct the original question's typos (e.g., `চার্জ` → `চার্জ`, `$2 ×$${ }^{10^{-9}} \mathrm{C}$` →
  `2 \times 10^{-9}\ \mathrm{C}`) in your solution text; do NOT reproduce broken LaTeX.
- Use exact physics values: `1\ \mathrm{C} = 10^{6}\ \mu\mathrm{C}`, `1\ \mu\mathrm{C} = 10^{-6}\ \mathrm{C}`,
  `1\ \mathrm{pF} = 10^{-12}\ \mathrm{F}`, `1\ \mathrm{nF} = 10^{-9}\ \mathrm{F}`.
- Formulas: `F = \frac{1}{4\pi\epsilon_{0}} \frac{q_{1}q_{2}}{r^{2}}`,
  `E = \frac{F}{q} = \frac{1}{4\pi\epsilon_{0}} \frac{Q}{r^{2}}`,
  `V = \frac{1}{4\pi\epsilon_{0}} \frac{Q}{r}`,
  `V = Ed` (uniform field), `C = \frac{Q}{V}`, `C = \frac{\epsilon_{0}A}{d}`,
  `C = \frac{\kappa\epsilon_{0}A}{d}`, `\sigma = \frac{Q}{A}`, `U = \frac{1}{2}CV^{2}`,
  `U = \frac{Q^{2}}{2C}`, `E = \frac{\sigma}{\epsilon_{0}}` (infinite sheet),
  `\vec{p} = q\vec{d}`, `\tau = \vec{p} \times \vec{E}`, etc.
- For a conducting sphere: inside `E=0`, on surface `E = Q/(4\pi\epsilon_{0}R^{2})`, outside as point charge.
  Potential inside a charged sphere is constant = surface potential.

## Quality bar

- EVERY question gets an answer — no skips, no "cannot solve" except truly unreadable figures.
- Solve independently and correctly; check units, powers of 10, and constants in every calculation.
- Show the working steps (substitute numbers, simplify, final answer with unit).
- If options are given, verify your computed answer matches one option before committing the index.
- For image questions, base the solution on the actual figure values you READ.
