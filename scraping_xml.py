import xml.etree.ElementTree as ET
import pandas as pd

# Importar datos leyendo desde el archivo XML
tree = ET.parse('facturas/fact.xml')
root = tree.getroot() # Etiqueta y atributos del nodo raiz

# El namespace que usa el SAT en los CFDI
ns = {'cfdi':'http://www.sat.gob.mx/cfd/4'}

# Datos necesarios de extraer de etiqueta cfdi:Concepto
conceptos = []

# for concepto in root.iter('{http://www.sat.gob.mx/cfd/4}Concepto'):
#     print(concepto.attrib)

for concepto in root.findall('.//cfdi:Concepto', ns):
    descripcion = concepto.attrib.get('Descripcion')
    clave = concepto.attrib.get('ClaveProdServ')
    unidad = concepto.attrib.get('ClaveUnidad')
    unitario = float(concepto.attrib.get('ValorUnitario'))
    
    conceptos.append({"Descripcion":descripcion, "Clave":clave, "Clave Unidad":unidad, "Valor Unitario":unitario})

# Datos necesarios de extraer de etiqueta cfdi:Traslado
traslados = []

for traslado in root.findall('.//cfdi:Traslado', ns):
    tasa = float(traslado.attrib.get('TasaOCuota'))
    traslados.append({"Tasa":tasa})

