# CCDH Models in BiolinkML

## Documentation:

* model documentation

https://cancerdhc.github.io/ccdhmodel/

* Talk on the CCDH Data Harmonization Workstream meeting

https://docs.google.com/document/d/13PMvYlstQ9BNr_Br1HzZ9n7etkz5nCKxp_RbF0cL4n0


## Automated generation of YAML

The model yaml files are programmatically generated from the Google Sheet [https://docs.google.com/spreadsheets/d/1oWS7cao-fgz2MKWtyr8h2dEL9unX__0bJrWKv6mQmM4/]

The code that generates the yamls are at [https://github.com/HOT-Ecosystem/crdc-node-models/blob/master/ccdh/biolinkml/cdm_biolinkml_loader.py]

## Generation of downstream artifacts

We reuse the [Makefile](https://en.wikipedia.org/wiki/Make_(software)) from the [LinkML template repository](https://github.com/linkml/linkml-template/), which automatically generate downstream artifacts, including:
 * JSON-Schema
 * ShEx
 * OWL
 * RDF (direct mapping)
 * TSV/CSV reports

You can install prerequisites into a [`venv`](https://docs.python.org/3/library/venv.html) by running:

```
make install
```

You can then build all downstream artifacts by running:

```
make all
```

You can also make specific targets by running, e.g.:

```
make stage-jsonschema
```

To build the documentation and deploy it to GitHub Pages, run:

```
make gh-deploy
```
