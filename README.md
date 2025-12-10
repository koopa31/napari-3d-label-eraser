# napari-3d-label-eraser

[![License GNU GPL v3.0](https://img.shields.io/pypi/l/napari-3d-label-eraser.svg?color=green)](https://github.com/koopa31/napari-3d-label-eraser/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-3d-label-eraser.svg?color=green)](https://pypi.org/project/napari-3d-label-eraser)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-3d-label-eraser.svg?color=green)](https://python.org)
[![tests](https://github.com/koopa31/napari-3d-label-eraser/workflows/tests/badge.svg)](https://github.com/koopa31/napari-3d-label-eraser/actions)
[![codecov](https://codecov.io/gh/koopa31/napari-3d-label-eraser/branch/main/graph/badge.svg)](https://codecov.io/gh/koopa31/napari-3d-label-eraser)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-3d-label-eraser)](https://napari-hub.org/plugins/napari-3d-label-eraser)


A simple tool to erase a selected label across an entire 3D volume in napari.

## Overview

**napari-3d-label-eraser** provides a fast and convenient way to remove all voxels belonging to a given label in a 3D `Labels` layer.  
This is useful for cleaning segmentation results, removing misdetected objects, or performing manual corrections in volumetric datasets.

The plugin adds a dock widget featuring:
- a dropdown menu to select the target `Labels` layer,
- a button to erase the currently selected label across the entire 3D volume,
- optional usage instructions.

A keyboard shortcut (`A`) can also be used to trigger the erase operation directly from the viewer.

## Features

- Erase all voxels of the selected label throughout a 3D volume.
- Dropdown to choose the active `Labels` layer.
- Compatible with napari’s label picker (`L` key).
- Optional keyboard shortcut (`A`) for quick editing.
- Minimal, lightweight, and easy to integrate into existing workflows.

## Installation

Install with pip:

```bash
pip install napari-3d-label-eraser
```

Or install from the napari plugin manager:

```
Plugins → Install/Uninstall Plugins
```

For development installation:

```bash
git clone https://github.com/koopa31/napari-3d-label-eraser.git
cd napari-3d-label-eraser
pip install -e .
```

## Usage

1. Load a `Labels` layer in napari.
2. Open the plugin:  
   **Plugins → 3D Label Eraser → 3D Label Eraser**
3. In the widget:
   - Select your target `Labels` layer.
   - Choose the label to erase using the label picker (`L` key).
   - Click the button to erase that label across the full 3D volume.
4. Alternatively, press **A** to erase the current label directly from the viewer (focus must be on the viewer).

## Notes

- The plugin operates only on `Labels` layers.
- The erase action sets all voxels with the selected label to `0`.
- The `A` shortcut is registered automatically when the widget is opened.

## Contributing

Issues, feature requests, and pull requests are welcome.

## License

This project is released under the MIT License.