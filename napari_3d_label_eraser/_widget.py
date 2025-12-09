from magicgui import magic_factory
from napari.viewer import Viewer
from napari.layers import Labels
import numpy as np


def _erase_label_in_layer(layer: Labels):
    """Set all voxels of the current label to 0 in the given Labels layer."""
    if layer is None:
        print("[3D ERASE] No Labels layer provided.")
        return

    if not isinstance(layer, Labels):
        print("[3D ERASE] Provided layer is not a Labels layer.")
        return

    label_value = layer.selected_label
    if label_value == 0:
        print("[3D ERASE] Current label is 0 (background), nothing to do.")
        return

    data = layer.data
    mask = data == label_value
    nvox = int(mask.sum())

    if nvox == 0:
        print(f"[3D ERASE] No voxel found with value {label_value}.")
        return

    print(f"[3D ERASE] Replacing {nvox} voxels ({label_value}) by 0.")
    data[mask] = 0
    layer.data = data


_INSTRUCTIONS = (
    "Instructions:\n"
    "1. Select a Labels layer in the dropdown above.\n"
    "2. Pick the label value to erase using the label picker ('L').\n"
    "3. Click the button below, or press 'A' to erase\n"
    "   that label everywhere in the 3D volume."
)

# Variable globale pour le widget
_widget_instance = None


@magic_factory(
    call_button="Erase current label (3D)",
    labels_layer={"label": "Labels layer"},
    instructions={"widget_type": "Label", "label": ""},
)
def erase_current_label(
        viewer: Viewer,
        labels_layer: Labels,
        instructions: str = _INSTRUCTIONS,
):
    """Erase the selected label in 3D within the chosen Labels layer."""
    global _widget_instance
    _widget_instance = erase_current_label  # Sauvegarder pour le keybinding

    if labels_layer is None:
        active = viewer.layers.selection.active
        if isinstance(active, Labels):
            labels_layer = active
        else:
            print("[3D ERASE] No Labels layer selected.")
            return

    _erase_label_in_layer(labels_layer)


def register_keybinding(viewer: Viewer):
    """Enregistre le keybinding A."""

    @viewer.bind_key("A", overwrite=True)
    def _erase_on_a(v):
        print("[3D ERASE] Key 'A' pressed!")
        layer = v.layers.selection.active
        if isinstance(layer, Labels):
            _erase_label_in_layer(layer)
        else:
            print("[3D ERASE] Active layer is not Labels.")

    print("[3D ERASE] Keybinding 'A' registered!")


def napari_experimental_provide_function():
    """Fournit la fonction de keybinding."""
    return [register_keybinding]