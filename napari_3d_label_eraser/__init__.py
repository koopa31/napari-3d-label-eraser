"""napari-3d-label-eraser plugin."""

__all__ = ["__version__"]
__version__ = "0.1.0"


# Enregistrer le keybinding automatiquement au chargement du plugin
def _auto_register_keybinding():
    """Enregistre le keybinding sur le viewer actif s'il existe."""
    try:
        import napari
        viewer = napari.current_viewer()
        if viewer is not None:
            from napari_3d_label_eraser._widget import register_keybinding
            register_keybinding(viewer)
    except (RuntimeError, ValueError):
        # Pas de viewer actif, ce n'est pas grave
        pass


# Essayer d'enregistrer immédiatement
_auto_register_keybinding()

# Hook pour enregistrer quand napari démarre
try:
    import napari


    @napari.Viewer.bind_key("A", overwrite=True)
    def _global_erase_keybinding(viewer):
        """Keybinding global pour tous les viewers."""
        from napari.layers import Labels
        from napari_3d_label_eraser._widget import _erase_label_in_layer

        print("[3D ERASE] Key 'A' pressed!")
        layer = viewer.layers.selection.active
        if isinstance(layer, Labels):
            _erase_label_in_layer(layer)
        else:
            print("[3D ERASE] Active layer is not Labels.")


    print("[3D ERASE] Global keybinding 'A' registered on Viewer class!")

except Exception as e:
    print(f"[3D ERASE] Could not register global keybinding: {e}")