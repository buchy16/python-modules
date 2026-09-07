# python-modules

Centralized repository for the `buchy16` Python module projects.

## Purpose

This repository consolidates the individual `python_moduleXX` repositories into one navigable monorepo-style structure while keeping each module separated in its own folder.

## Included modules

- `python_module01/`
- `python_module02/`
- `python_module03/`
- `python_module05/`
- `python_module06/`
- `python_module07/`
- `python_module08/`
- `python_module09/`
- `python_module10/`

## Missing/unavailable module

- `python_module04` was not found in the available repositories under `buchy16` at migration time, so it could not be migrated into this repository.

## Migration notes

- Each available module repository was imported into its own top-level folder to avoid content overlap and preserve project boundaries.
- Existing module-internal structures (for example `ex0`, `ex1`, etc.) were kept as-is inside each module folder.
