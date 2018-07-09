import sys, adsk.core, adsk.fusion, traceback, pip, os
from importlib import reload, import_module
from os.path import join, dirname, abspath

def abs_path(file_path):
    """
    Returns the absolute path from the file that calls this function to file_path. Needed to access other files within aide_gui when initialized by aide.

    Parameters
    ----------
    file_path: String
        The relative file path from the file that calls this function.
    """

    return join(dirname(abspath(__file__)), file_path)

# Import local dependencies.
sys.path.append(abs_path('.'))
sys.path.append(r"C:\Users\EN-CE-AC\AppData\Local\Continuum\anaconda3\lib\site-packages")

from .aide_gui import aide_gui, helper
from .aide_draw import load_yaml_and_update_params
from .aide_render import render_lfom

def run(context):
    try:
        reload(aide_gui)

        f360_app = adsk.core.Application.get()
        f360_ui  = f360_app.userInterface
        aide_gui.run(context, run_design)

    except:
        if f360_ui:
            f360_ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    try:
        f360_app = adsk.core.Application.get()
        f360_ui  = f360_app.userInterface
        
        aide_gui.stop(context)

    except:
        if f360_ui:
            f360_ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def run_design():
    f360_app = adsk.core.Application.get()
    f360_ui  = f360_app.userInterface

    render_lfom(abs_path('aide_gui/data/params.yaml'), abs_path('lfom.yaml'))

    # Run aide_draw to change Fusion 360 drawing.
    rootComponent = adsk.fusion.FusionDocument.cast(f360_app.activeProduct.parentDocument).design.rootComponent
    load_yaml_and_update_params('lfom.yaml', rootComponent)
