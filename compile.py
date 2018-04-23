#!/usr/bin/env python
import codecs
from jinja2 import Environment, FileSystemLoader

PUBLISH_ROOT = '.'
JINJA_ENV = Environment(loader=FileSystemLoader('templates'))

templates = ["index.html", "about.html", "register.html", "schedule.html", "archive.html", "speaker.html", "sponsor.html", "venue.html", "profile.html", "proposal.html", "proposals.html", "speakers.html", "sponsors.html", "sponsor-guide.html", "2017/index.html", "2017/schedule.html", "2016/index.html", "2016/schedule.html", "2016/sponsor.html", "2015/index.html", "2015/schedule.html", "2015/sponsor.html", "2014/index.html", "2014/schedule.html", "2014/sponsor.html"]

for template_file in templates:
    template = JINJA_ENV.get_template("%s" % template_file)
    rendered_html = template.render()

    with codecs.open("%s/%s" % (PUBLISH_ROOT, template_file), "w", encoding="utf-8") as output_file:
        output_file.write(unicode(rendered_html))

print "Done"
