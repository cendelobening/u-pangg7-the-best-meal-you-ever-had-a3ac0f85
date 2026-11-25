#!/usr/bin/env python3
"""The Best Meal You Ever Had — one sentence, one unforgettable meal.

Entry for the make.fun bounty
``u-pangg7-the-best-meal-you-ever-had-a3ac0f85``.

The program writes exactly one sentence — at most 200 characters, a
single line, no trailing newline — to ``<output_dir>/entry.txt``, where
``output_dir`` comes from the ``MAKEFUN_OUTPUT_DIR`` environment variable
(default ``/output``). Pure Python standard library, fully deterministic:
every run produces the same bytes. The output file is left world-readable
(mode 0644) so the grader can read it.
"""

import os

# The sentence itself: one concrete dish (golden fried catfish), one real
# place (my grandmother's kitchen table in Yogyakarta), one real person
# (my grandmother), and a sensory detail that lingers — eating with bare
# hands, the chili heat tingling on the lips for hours afterwards. A
# stranger should picture it instantly and remember it.
SENTENCE = (
    "At my grandmother's kitchen table in Yogyakarta, I ate golden fried "
    "catfish with my bare hands, scooping sambal and warm rice while the "
    "chili heat tingled on my lips for hours."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    sentence = SENTENCE
    # Gate checks, mirroring the competition's own rules for entry.txt.
    assert sentence.strip(), "sentence must not be only whitespace"
    assert "\n" not in sentence and "\r" not in sentence, "must be a single line"
    assert 1 <= len(sentence) <= 200, "must be 1-200 characters"
    assert sentence.endswith("."), "must end with a period"
    assert sentence.count(".") == 1, "must be exactly one sentence"

    # newline="" keeps the write byte-exact: no trailing newline is added.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(sentence)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
