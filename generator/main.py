import dataclasses
import os

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

# Examples of logging messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

current_directory = os.getcwd()
logger.info("Start generator from : " + current_directory)

ecoa_project = r'D:\Projects\DaV\ecoa_tools\samples\pingpong'

logger.info("Read ECOA project from : " + ecoa_project)
loader = EcoaLoader()
loader.loadFromDirectory(ecoa_project)

parser = XmlParser()
generatorConfiguration = parser.parse(r"D:\Projects\DaV\ecoa_tools\data\generatorconfiguration.xml",
                                      GeneratorConfiguration)

# First, generate all the types.
for generator in generatorConfiguration.type_generator:
    template_code = """
    #IFNDEF {{ library_name }}_H
    #DEFINE {{ library_name }}_H
    
    #include "ECOA.h"
    {% for use in library.use -%}
    #include "{{ use.library }}.h"
    {% endfor %}
    
    // Declare constant types.
    {% for constant_type in library.types.constant -%}
    {% if constant_type.comment -%}
    // {{ constant_type.comment -}}
    {% endif %}
    typedef {{ constant_type.type }} {{ constant_type.name }} = {{ constant_type.value }}
    {% endfor %}
    
    // Declare simple.
    {% for simple_type in library.types.simple %}
    {% if simple_type.comment -%}
    // {{ simple_type.comment -}}
    {% endif %}
    typedef {{ simple_type.type }} {{ simple_type.name }};
    static const {{ simple_type.type }} {{ simple_type.name }}_minRange =  0.0;
    static const {{ simple_type.type }} {{ simple_type.name }}_maxRange = 1.0;
    {% endfor %}
    
    // Declare enum.
    {% for enum_type in library.types.enum -%}
    {% if enum_type.comment -%}
    // {{ enum_type.comment -}}
    {% endif %}
    struct {{ enum_type.name }}
    {
        {{ enum_type.type }} value;
        enum EnumValues 
        {
            {% for enum_value in enum_type.value -%}
            {% if enum_value.valnum -%}
            {{ enum_value.name }} = {{ enum_value.valnum }},
            {% else -%}
            {{ enum_value.name }},            
            {% endif -%}     
            {% endfor %}        
        };         
        inline void operator = ({{ enum_type.type }} i) { value = i; }
        inline operator {{ enum_type.type }}() const { return value; }
        inline {{ enum_type.name }}(EnumValues v):value(v) {}
        inline {{ enum_type.name }}():value({{enum_type.value[0].name}}) {}
    }; 
    {% endfor %}
    
    // Declare record types.
    {% for record_type in library.types.record -%}
    // {{ record_type.name }}
    {% if record_type.comment -%}
    // {{ record_type.comment -}}
    {% endif %}
    typedef struct
    {
        {% for record_value in record_type.field_value -%}
            {{record_value.type}} {{record_value.name}};
        {% endfor %}
    } {{ record_type.name }};
    
    {% endfor %}
    
    // Declare variant record types.
    {% for variant_record_type in library.types.variant_record -%}
    // {{ variant_record_type.name -}}
    {% if variant_record_type.comment -%}
    // {{ variant_record_type.comment -}}
    {% endif %}
    {% endfor %}
    
    // Declare fixed array types.
    {% for fixed_array_type in library.types.fixed_array -%}
    // {{ fixed_array_type.name }}
    {% if fixed_array_type.comment -%}
    // {{ fixed_array_type.comment -}}
    {% endif %}
    const ECOA::uint32 {{ fixed_array_type.name }}_MAXSIZE = {{ fixed_array_type.max_number }};
    typedef {{ fixed_array_type.item_type }} {{ fixed_array_type.name }}[{{ fixed_array_type.name }}_MAXSIZE];
    {% endfor %}
    
    // Declare variables array types.
    {% for var_array_type in library.types.array -%}
    // {{ var_array_type.name }}
    {% if var_array_type.comment -%}
    // {{ var_array_type.comment -}}
    {% endif %}
    const ECOA::uint32 {{ var_array_type.name }}_MAXSIZE = {{ var_array_type.max_number }};
    typedef struct 
    {
        ECOA::uint32 current_size;
        {{ var_array_type.item_type }} data[{{ var_array_type.name }}_MAXSIZE];
    } {{ var_array_type.name }};
    {% endfor %}
    
    #ENDIF    
    """

    if os.path.isdir(generator.output):
        logger.info("Generate types in " + generator.output)
        for library in loader.libraries:
            base_library_path = os.path.join(generator.output, inflection.camelize("pingpongLibrary"))
            if not os.path.isdir(base_library_path):
                os.mkdir(base_library_path)
            if generator.generate_inc:
                src_full_library_path = os.path.join(base_library_path, inflection.camelize("src"))
                if not os.path.isdir(src_full_library_path):
                    os.mkdir(src_full_library_path)
                inc_full_library_path = os.path.join(base_library_path, inflection.camelize("inc"))
                if not os.path.isdir(src_full_library_path):
                    os.mkdir(inc_full_library_path)
                base_library_path = inc_full_library_path
            # Now, re-generate .H and CPP
            header_file_path = os.path.join(base_library_path, "pingpong.h")
            logger.info("Generate header file " + header_file_path)
            #template = load_template("./templates/types.template")
            template = Template(template_code)
            generated_code = template.render(library_name="pingpong", library=library)
            logger.debug(generated_code)

# Second, generate the modules
for generator in generatorConfiguration.module_generator:
    if os.path.isdir(generator.output):
        logger.info("toto"
                    ""
                    "")
    else:
        logger.error("The output directory for module does not exist " + generator.output)

# Third, then the container

# Finally, the ECOA generic platform
