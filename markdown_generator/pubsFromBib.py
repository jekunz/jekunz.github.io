#!/usr/bin/env python
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a set of bibtex of publications and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook ([see more info here](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)). 
# 
# The core python code is also in `pubsFromBibs.py`. 
# Run either from the `markdown_generator` folder after replacing updating the publist dictionary with:
# * bib file names
# * specific venue keys based on your bib file preferences
# * any specific pre-text for specific files
# * Collection Name (future feature)
# 
# TODO: Make this work with other databases of citations, 
# TODO: Merge this with the existing TSV parsing solution


from pybtex.database.input import bibtex
from time import strptime
import codecs
import latexcodec  # installed with pybtex
import html
import os
import re

# Bib file (relative to this folder) and the name to highlight in citations
BIB_FILE = "../files/bibtex1.bib"
MY_NAME = "Jenny Kunz"

# Bib keys of papers to list under "Selected papers" on the front page
SELECTED = {
    "kunz-2026-preferences",
    "oji-etal-2026-probing",
    "kunz-2026-dialects",
    "borggren-etal-2026-reading",
}

# Per entry type: which field holds the venue, and the category on the publications page
ENTRY_TYPES = {
    "inproceedings": {"venuekey": "booktitle", "category": "conferences"},
    "article":       {"venuekey": "journal",   "category": "manuscripts"},
    "book":          {"venuekey": "publisher", "category": "books"},
}

def clean(text):
    """Convert LaTeX (accents, dashes) to unicode and drop protective braces."""
    text = codecs.decode(text, "ulatex")
    return re.sub(r"\s+", " ", text.replace("{", "").replace("}", "")).strip()

def yaml_escape(text):
    """Escape for single-quoted YAML strings."""
    return text.replace("'", "''")

def person_name(person):
    return clean(" ".join(person.first_names + person.middle_names + person.prelast_names + person.last_names))

parser = bibtex.Parser()
bibdata = parser.parse_file(BIB_FILE)
os.makedirs("../_publications", exist_ok=True)

for bib_id, entry in bibdata.entries.items():
    b = entry.fields
    etype = ENTRY_TYPES.get(entry.type)
    if etype is None:
        print(f"SKIPPING {bib_id}: unsupported entry type '{entry.type}'")
        continue
    try:
        pub_year = b["year"]
        pub_month = "01"
        if "month" in b:
            m = b["month"]
            pub_month = "{:02d}".format(int(m)) if m.isdigit() else "{:02d}".format(strptime(m[:3], "%b").tm_mon)
        pub_date = f"{pub_year}-{pub_month}-01"

        title = clean(b["title"])
        venue = clean(b[etype["venuekey"]])
        url_slug = re.sub(r"-+", "-", re.sub(r"[^a-zA-Z0-9-]", "", title.replace(" ", "-")))[:80].strip("-")
        html_filename = f"{pub_date}-{url_slug}"

        authors = [person_name(p) for p in entry.persons.get("author", [])]
        authors = [f"<b>{a}</b>" if a == MY_NAME else a for a in authors]
        citation = f'{", ".join(authors)}. ({pub_year}). "{html.escape(title, quote=False)}." <i>{html.escape(venue, quote=False)}</i>.'

        md = "---\n"
        md += f"title: '{yaml_escape(title)}'\n"
        md += "collection: publications\n"
        md += f"category: {etype['category']}\n"
        md += f"permalink: /publication/{html_filename}\n"
        md += f"date: {pub_date}\n"
        if bib_id in SELECTED:
            md += "selected: true\n"
        md += f"venue: '{yaml_escape(venue)}'\n"
        if "url" in b:
            md += f"paperurl: '{b['url']}'\n"
        md += f"citation: '{yaml_escape(citation)}'\n"
        md += "---\n"
        if "url" in b:
            md += f"\n[Access paper here]({b['url']}){{:target=\"_blank\"}}\n"

        with open(f"../_publications/{html_filename}.md", "w", encoding="utf-8") as f:
            f.write(md)
        print(f"SUCCESSFULLY PARSED {bib_id}: {title[:60]}")
    except KeyError as e:
        print(f"WARNING Missing Expected Field {e} from entry {bib_id}")
