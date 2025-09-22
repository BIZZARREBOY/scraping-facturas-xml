import xml.etree.ElementTree as ET
import pandas as pd

# Importar datos leyendo desde el archivo XML
tree = ET.parse('facturas/fact.xml')
root = tree.getroot() # Etiqueta y atributos del nodo raiz

# El namespace que usa el SAT en los CFDI
ns = {'cfdi':'http://www.sat.gob.mx/cfd/4'}

conceptos = []

# for concepto in root.iter('{http://www.sat.gob.mx/cfd/4}Concepto'):
#     print(concepto.attrib)

# Datos necesarios de extraer de etiqueta cfdi:Concepto
for concepto in root.findall('.//cfdi:Concepto', ns):
    descripcion = concepto.attrib.get('Descripcion')
    clave = concepto.attrib.get('ClaveProdServ')
    unidad = concepto.attrib.get('ClaveUnidad')
    unitario = float(concepto.attrib.get('ValorUnitario'))
    
    conceptos.append({"Descripcion":descripcion, "Clave":clave, "Clave Unidad":unidad, "Valor Unitario":unitario})

df = pd.DataFrame(conceptos)
print(df)