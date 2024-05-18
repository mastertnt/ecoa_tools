import dataclasses
import os
import pickle
import re
from pathlib import Path

import inflection
import stringcase
from jinja2 import FileSystemLoader, Environment, Template
from xsdata.formats.dataclass.parsers import XmlParser
from ecoa.ecoa_loader import EcoaLoader
from generator.generator_configuration import GeneratorConfiguration
import logging
import colorlog


# Function to load a JINJA template
def load_template(file_path):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(file_path)
    return template


# Define log colors based on log levels
log_colors = {
    'DEBUG': 'white',
    'INFO': 'blue',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

# Configure the logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a console handler with colored output
console_handler = colorlog.StreamHandler()
console_handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s: %(message)s',
    log_colors=log_colors,
))

# Add the handler to the logger
logger.addHandler(console_handler)

current_directory = os.getcwd()
logger.info("Start generator from : " + current_directory)

ecoa_project = r'D:\Projects\DaV\ecoa_tools\samples\pingpong'

logger.info("Read ECOA project from : " + ecoa_project)
loader = EcoaLoader()
loader.loadFromDirectory(ecoa_project)

parser = XmlParser()
generatorConfiguration = parser.parse(r"D:\Projects\DaV\ecoa_tools\data\generatorconfiguration.xml",
                                      GeneratorConfiguration)

# First, generate the libraries.
for generator in generatorConfiguration.type_generator:
    if os.path.isdir(generator.output):
        logger.info("Generate types in " + generator.output)
        for library in loader.libraries:
            # TODO : Make a public method to retrieve a non-hashable object.
            library_name = os.path.basename(loader.libraryFilenames[pickle.dumps(library)])
            library_name = library_name.split('.')[0]
            logger.info("Generate library " + library_name)
            library_name = inflection.camelize(library_name)
            base_generation_path = os.path.join(generator.output, library_name + "Library")
            if not os.path.isdir(base_generation_path):
                os.mkdir(base_generation_path)
            if generator.generateSubDirectory:
                base_generation_src_path = os.path.join(base_generation_path, inflection.camelize("src"))
                if not os.path.isdir(base_generation_src_path):
                    os.mkdir(base_generation_src_path)
                base_generation_inc_path = os.path.join(base_generation_path, inflection.camelize("inc"))
                if not os.path.isdir(base_generation_inc_path):
                    os.mkdir(base_generation_inc_path)
            # Now, re-generate .HPP and CPP
            header_file_path = os.path.join(base_generation_inc_path, library_name + ".hpp")
            logger.info("Generate header file " + header_file_path)
            if library_name == "Ecoa":
                template = load_template("templates/library_hpp.template")
            else:
                template = load_template("templates/library_hpp.template")
            generated_code = template.render(library_name=library_name, library=library)
            if os.path.isfile(header_file_path):
                os.remove(header_file_path)
            header_file = open(header_file_path, "x")
            header_file.write(generated_code)
            header_file.close()
            logger.info("Library " + library_name + " correctly generated in " + base_generation_path)
            #logger.debug(generated_code)

# Second, generate the modules
for generator in generatorConfiguration.module_generator:
    if os.path.isdir(generator.output):
        logger.info("Generate modules in " + generator.output)
        for component_definition in loader.componentDefinitions:
            #for component_definition in component_definitions:
            # TODO : Make a public method to retrieve a non-hashable object.
            component_definition_name = os.path.basename(loader.componentDefinitionFilenames[pickle.dumps(component_definition)])
            component_definition_name = component_definition_name.split('.')[0]
            logger.info("Generate component definition " + component_definition_name)
            base_generation_path = generator.output
            base_generation_inc_path = generator.output
            base_generation_src_path = generator.output
            if generator.generateDirectoryPerComponent:
                base_generation_path = os.path.join(generator.output, component_definition_name)
                if not os.path.isdir(base_generation_path):
                    os.mkdir(base_generation_path)
            if generator.generateSubDirectory:
                base_generation_src_path = os.path.join(base_generation_path, inflection.camelize("src"))
                if not os.path.isdir(base_generation_src_path):
                    os.mkdir(base_generation_src_path)
                base_generation_inc_path = os.path.join(base_generation_path, inflection.camelize("inc"))
                if not os.path.isdir(base_generation_inc_path):
                    os.mkdir(base_generation_inc_path)
            # Now, re-generate .HPP
            header_file_path = os.path.join(base_generation_inc_path, component_definition_name + ".hpp")
            logger.info("Generate header file " + header_file_path)
            template = load_template("templates/module_hpp.template")
            tags = {}
            if os.path.isfile(header_file_path):
                header_file = open(header_file_path)
                generated_code = header_file.read()
                logger.debug(generated_code)
                result = re.search('@@BEGIN_CODE(.*)@@END_CODE', generated_code, re.MULTILINE)
                logger.debug(result)
                begin_pos = generated_code.find('//@@BEGIN_CODE')
                end_pos = generated_code.find('//@@END_CODE')

                while begin_pos != -1 and end_pos != -1:
                    extracted = generated_code[begin_pos:end_pos]
                    lines = extracted.split('\n')
                    tag = ""
                    user_code = ""
                    if len(lines) > 1:
                        tag = lines[0].split(':')[1]
                        lines.pop(0)
                        user_code = '\n'.join(lines).strip()
                    logger.debug("tag is " + tag)
                    logger.debug("usercode is " + user_code)
                    tags[tag.strip()] = user_code
                    begin_pos = generated_code.find('//@@BEGIN_CODE', end_pos + 1)
                    end_pos = generated_code.find('//@@END_CODE', end_pos + 1)
                header_file.close()
                os.remove(header_file_path)
            generated_code = template.render(component_definition_name=component_definition_name, tags = tags, component_definition=component_definition, services=loader.services)
            header_file = open(header_file_path, "x")
            header_file.write(generated_code)
            header_file.close()
            # Now, re-generate .CPP
            source_file_path = os.path.join(base_generation_src_path, component_definition_name + ".cpp")
            logger.info("Generate source file " + source_file_path)
            template = load_template("templates/module_cpp.template")
            tags = {}
            if os.path.isfile(source_file_path):
                source_file = open(source_file_path)
                generated_code = source_file.read()
                logger.debug(generated_code)
                result = re.search('@@BEGIN_CODE(.*)@@END_CODE', generated_code, re.MULTILINE)
                logger.debug(result)
                begin_pos = generated_code.find('//@@BEGIN_CODE')
                end_pos = generated_code.find('//@@END_CODE')

                while begin_pos != -1 and end_pos != -1:
                    extracted = generated_code[begin_pos:end_pos]
                    lines = extracted.split('\n')
                    tag = ""
                    user_code = ""
                    if len(lines) > 1:
                        tag = lines[0].split(':')[1]
                        lines.pop(0)
                        user_code = '\n'.join(lines).strip()
                    logger.debug("tag is " + tag)
                    logger.debug("usercode is " + user_code)
                    tags[tag.strip()] = user_code
                    begin_pos = generated_code.find('//@@BEGIN_CODE', end_pos + 1)
                    end_pos = generated_code.find('//@@END_CODE', end_pos + 1)
                source_file.close()
                os.remove(source_file_path)
            generated_code = template.render(component_definition_name=component_definition_name, tags=tags, component_definition=component_definition, services=loader.services)
            source_file = open(source_file_path, "x")
            source_file.write(generated_code)
            source_file.close()

            logger.info("Component definition " + component_definition_name + " correctly generated in " + base_generation_path)
    else:
        logger.error("The output directory for module does not exist " + generator.output)

# Third, then the container

# Finally, the ECOA generic platform
