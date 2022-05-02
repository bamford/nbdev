nbprocess
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

This will probably become v2 of nbdev in the near-ish future.

## Install

With pip:

    pip install nbprocess

With conda:

    conda install -c fastai nbprocess

## How to use

By default docs are exported for use with [Quarto](https://quarto.org/).
To install Quarto on Ubuntu, run `make install`. See the Quarto docs for
other platforms.

The following CLI tools are provided:

-   [nbprocess_create_config](https://nbprocess.fast.ai/nbprocess.read#nbprocess_create_config):
    Create `settings.ini` skeleton
-   [nbprocess_export](https://nbprocess.fast.ai/nbprocess.doclinks#nbprocess_export):
    Export notebooks to Python modules
-   [nbprocess_update](https://nbprocess.fast.ai/nbprocess.sync#nbprocess_update):
    Update Python modules from a notebook
-   [nbprocess_fix](https://nbprocess.fast.ai/nbprocess.merge#nbprocess_fix):
    Fix merge conflicts in notebooks
-   [nbprocess_filter](https://nbprocess.fast.ai/nbprocess.cli#nbprocess_filter):
    A filter for Quarto
-   [nbprocess_quarto](https://nbprocess.fast.ai/nbprocess.cli#nbprocess_quarto):
    Create Quarto web site
-   [nbprocess_new](https://nbprocess.fast.ai/nbprocess.cli#nbprocess_new):
    Create a new `nbprocess` project