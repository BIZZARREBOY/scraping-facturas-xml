import xml.etree.ElementTree as ET
import pandas as pd
import csv

tree = ET.parse('ejemplos_facturas/fact.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

#Imprime hijos de root
for child in root:
    print(child.tag, child.attrib)

# Direccion (Conceptos)
conceptos = root[2]
# Direccion (Conceptos/Impuestos)
impuestos = conceptos[0][0][0][1]

for child in conceptos:
    print(print(child.tag, child.attrib))



print(impuestos.attrib)
