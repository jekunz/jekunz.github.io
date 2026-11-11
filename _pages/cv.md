---
layout: archive
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D in Computer Science, Linköping University, 2024
* M.A. in Language Technology, Uppsala University, 2018
* B.A. in Computer Science, Humboldt University of Berlin, 2016

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
