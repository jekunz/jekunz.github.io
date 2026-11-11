---
permalink: /
title: "Jenny Kunz"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% include base_path %}

About me
======
I am a postdoc in the [NLP group]({{ site.author.group }}) at [Linköping University]({{ site.author.employer_url }}), where I received [my PhD in Computer Science](https://liu.diva-portal.org/smash/record.jsf?pid=diva2%3A1848043&dswid=-787) in 2024. Before that, I studied Language Technology at Uppsala University and Computer Science at Humboldt University of Berlin.

I am part of the academic team of [SELLMA](https://wasp-sweden.org/research/projects/sellma/), where I work on data for instruction tuning, alignment and evaluation. I also work in [STING](https://wasp-sweden.org/sting-synthesis-and-analysis-with-transducers-and-invertible-neural-generators/). Previously, I worked in the [TrustLLM](https://trustllm.eu) project, on the work package on multilinguality. 

Research interests
======

My research focuses on multilingual NLP and cross-lingual transfer:

* Multilingual language models and language adaptation (e.g., [1](https://aclanthology.org/2026.emnlp-industry.255/), [2](https://arxiv.org/abs/2510.00810), [3](https://arxiv.org/abs/2610.29681))
* How language models acquire, transfer and forget knowledge and linguistic preferences during training (e.g., [1](https://aclanthology.org/2026.tacl-1.57/), [2](https://aclanthology.org/2026.emnlp-main.2445/), [3](https://aclanthology.org/2026.lrec-1.416/))
* Translationese and idiomatic language in training data and model output (e.g., [1](https://aclanthology.org/2026.findings-emnlp.2272/), [2](https://aclanthology.org/2026.lrec-1.690/), [3](https://aclanthology.org/2026.tacl-1.57/))

Recent papers
======
<ul>{% for post in site.publications reversed %}
  {% if post.selected %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}</ul>

See [all publications]({{ base_path }}/publications/).
