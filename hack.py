from jinja2 import Environment, FileSystemLoader
#import jun.j2
import jinja2
import yaml
import json

import os


# path = "/Users/nishamurarka/Desktop/Hackathon/jun.j2"
# ENV = Environment(loader=FileSystemLoader('.'))

ENV = Environment(loader=FileSystemLoader('.'))
template1= ENV.get_template("jun.j2")


with open ("data.yaml" )as y:
    host_obj =yaml.load(y)
for i in host_obj:
   f=open('config.json', 'w')
   f.write(template1.render(i))
   f=open('config.json')
   payload= json.load(f)
   print(payload)

