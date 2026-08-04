# Passt

**EN: Passt: An Introduction to AI**

**DE: Passt: KI-Grundlagen**

A twelve-week introduction to machine learning for people who will have to live
with these systems, argue with them, buy them, and explain them to somebody in a
meeting who has not read anything.

*Passt* is German for "it fits". It is also what you say when something is good
enough. A model that fits its data is doing its job, and a model that fits its
data too well is lying to you, and the whole course is about telling those two
apart.

Live at **https://i-yam.github.io/passt/**

---

## What is here

```
index.html            course homepage, bilingual
modules/              42 self-contained mini-modules, one folder each
notebooks/            Colab tinker sessions
assets/               shared theme tokens and the i18n contract
```

Every module is a **single self-contained HTML file**. No build step, no
bundler, no framework. Open one in a browser and it works. The only external
dependency is the KaTeX CDN, and only on pages with formulas.

## The twelve classes

| # | Class | Modules |
|---|---|---|
| 1 | What Is Intelligence? What Is Knowledge? | `can_machines_think` `spiders_and_legs` `is_ai` `quiz1` |
| 2 | Learning Has Many Faces | `duction` `anscombe` `parametric` `code_comprehension` |
| 3 | Linear Regression | `hot_or_cold` `sgd` `linregtutorial` |
| 4 | Local Models and Geometry | `glocal` `neighbours` `bv` `dimcurse` |
| 5 | Regularisation | `regularisation` `ridge` `lasso` + Colab |
| 6 | Classification Fundamentals | `decisions` `shrooms` `bayes` `test6` |
| 7 | Decision Trees | `akinator` `entropy` `titanic` |
| 8 | Ensembles | `ensambles` `boosting` |
| 9 | Validation and Model Selection | `testtrain` `folds` `simpson` |
| 10 | Recommendations and Neural Networks | `people_like_you` `boards_of_destiny` `game_of_life` `nets` |
| 11 | LLMs and Generative AI | `gaps` `apophenic` `prompts` |
| 12 | AI in Practice | `persona` `same_cv` `magenta_line` |
| — | Exam | `exam` `open` |


## Bilingual

Every page carries a language toggle in the top right. English renders first,
German sits behind the toggle, and the button always shows the *other* language.

The German is not a translation of the English, it is written to be read. Target reader is B2 in either
language.

## Publishing

GitHub Pages from the repository root. `.nojekyll` is present so directories
starting with an underscore are not swallowed. Nothing else is required.

## Two things worth not smoothing out

Some modules correct claims that this course itself used to make. `dimcurse`
carries a note that an earlier version stated a probability that was wrong by a
factor of two. That is deliberate. A course built on falsifiability that never
catches itself is not making the argument it thinks it is. If you find more mistakes, open issues, we'll fix them and the "scars" will make the course even better.

Sections about people who died, were wrongly convicted or wrongly arrested carry
no jokes in either language. `bayes` on Sally Clark, `magenta_line` on Air France
447, and `titanic` and `entropy` on the sinking are written plain on purpose.

## Licence

Content CC BY-SA 4.0. Code MIT. See `LICENSE`.
