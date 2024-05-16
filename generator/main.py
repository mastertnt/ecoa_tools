from xsdata.formats.dataclass.parsers import XmlParser
from ecoa.ecoa_loader import EcoaLoader
from generator.generator_configuration import GeneratorConfiguration
0
loader = EcoaLoader()
loader.loadFromDirectory(r'D:\Projects\DaV\ecoa_tools\samples\pingpong')

parser = XmlParser()
generatorConfiguration = parser.parse(r"D:\Projects\DaV\ecoa_tools\generatorconfiguration.xml", GeneratorConfiguration)