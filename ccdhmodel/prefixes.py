# Auto generated from prefixes.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-01-26 16:13
# Schema: prefixes
#
# id: https://ccdh.org/model/prefixes
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from biolinkml.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace


metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ADM = CurieNamespace('ADM', 'https://ccdh.org/models/ADM/')
BRIDG = CurieNamespace('BRIDG', 'https://fill.me.in/BRIDG/')
FHIR = CurieNamespace('FHIR', 'http://hl7.org/fhir/')
GDC = CurieNamespace('GDC', 'http://fill.me.in/GDC')
HTAN = CurieNamespace('HTAN', 'http://fill.me.in/ICDC')
ICDC = CurieNamespace('ICDC', 'http://fill.me.in/ICDC')
PDC = CurieNamespace('PDC', 'http://fill.me.in/PDC')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
CCDH = CurieNamespace('ccdh', 'https://example.org/ccdh/')
SPECIMEN = CurieNamespace('specimen', 'https://ccdh.org/specimen/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BIOLINKML


# Types

# Class references




# Enumerations


# Slots
class slots:
    pass


