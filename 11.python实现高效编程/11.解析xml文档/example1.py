#!/usr/bin/env python
#-*- coding:utf8 -*-
from xml.etree import ElementTree as ET
level_1 = ET.Element("famliy")
level_2 = ET.SubElement(level_1, "name", attrib={"enrolled":"yes"})
level_3 = ET.SubElement(level_2, "age", attrib={"checked":"no"})
tree = ET.ElementTree(level_1)

tree.write("oooo.xml",encoding="utf-8",short_empty_elements=False)

'''
import os
os.system("cat oooo.xml")
'''


