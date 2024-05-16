import os
from enum import Enum

from xsdata.formats.dataclass.parsers import XmlParser

from ecoa.ecoa_component_2_0 import ComponentType
from ecoa.ecoa_interface_2_0 import ServiceDefinition
from ecoa.ecoa_types_2_0 import Library


class EcoaLoaderMode(Enum):
    UNKNOWN = 0
    TYPES = 1
    SERVICES = 2
    COMPONENT_DEFINITIONS = 3
    INITIAL_ASSEMBLY = 4
    COMPONENT_IMPLEMENTATIONS = 5
    INTEGRATION = 6


class EcoaLoader:
    def __init__(self):
        self.mode = EcoaLoaderMode.UNKNOWN
        self.libraries = []
        self.services = []
        self.component_definitions = []

    def loadFromDirectory(self, dir):
        self.mode = EcoaLoaderMode.UNKNOWN

        for dir_entry in os.listdir(dir):
            if dir_entry == "0-Types":
                mode = EcoaLoaderMode.TYPES
            if dir_entry == "1-Services" and mode.value >= 1:
                mode = EcoaLoaderMode.SERVICES
            if dir_entry == "2-ComponentDefinitions" and mode.value >= 2:
                mode = EcoaLoaderMode.COMPONENT_DEFINITIONS
            if dir_entry == "3-InitialAssembly" and mode.value >= 3:
                mode = EcoaLoaderMode.INITIAL_ASSEMBLY
            if dir_entry == "4-ComponentImplementations" and mode.value >= 4:
                mode = EcoaLoaderMode.COMPONENT_IMPLEMENTATIONS
            if dir_entry == "5-Integration" and mode.value >= 5:
                mode = EcoaLoaderMode.INTEGRATION

        # Read all the libraries into 0-Types
        types_directory = os.path.join(dir, "0-Types")
        for types_dir_entry in os.listdir(types_directory):
            try:
                parser = XmlParser()
                library = parser.parse(os.path.join(types_directory, types_dir_entry), Library)
                self.libraries.append(library)
            except:
                print("Cannot parse the library file : " + os.path.join(types_directory, types_dir_entry))

        # Read all services into 1-Services
        services_directory = os.path.join(dir, "1-Services")
        self.loadServicesDirectory(services_directory)

        # Read all component definitions
        component_definitions_directory = os.path.join(dir, "2-ComponentDefinitions")
        self.loadComponentDefinitionDirectory(component_definitions_directory)

    def loadServicesDirectory(self, dir):
        for services_dir_entry in os.listdir(dir):
            full_path = os.path.join(dir, services_dir_entry)
            try:
                parser = XmlParser()
                service = parser.parse(full_path, ServiceDefinition)
                self.services.append(service)
            except:
                print("Cannot parse the service file : " + full_path)
    def loadComponentDefinitionDirectory(self, dir):
        for component_definition_dir_entry in os.listdir(dir):
            full_path = os.path.join(dir, component_definition_dir_entry)
            if os.path.isfile(full_path):
                self.loadComponentDefinitionFile(full_path)
            else:
                self.loadComponentDefinitionDirectory(full_path)

    def loadComponentDefinitionFile(self, file):
        try:
            parser = XmlParser()
            component_definition = parser.parse(file, ComponentType)
            self.component_definitions.append(component_definition)
        except:
            print("Cannot parse the component definition file : " + file)
