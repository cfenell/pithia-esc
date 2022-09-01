#! /usr/bin/env python3


import sys
import xmlschema


if __name__ == '__main__':

    if len(sys.argv) < 3:
        raise ValueError(f"Usage: {sys.argv[0]} SCHEMA_XSD XML_FILE(S) ")

    # Parse the schema
    xml_schema = xmlschema.XMLSchema(sys.argv[1])

    # Validate the files
    for n in range(2, len(sys.argv)):
        xml_schema.validate(sys.argv[n])

    # Validation passed
    print("All XML files match the schema")
    sys.exit(0)
