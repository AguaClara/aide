import sys, os, inspect, importlib
import adsk.core, adsk.fusion, adsk.cam, traceback # Fusion 360 imports


# Takes a relative file path (String) to the calling file and returns the correct absolute path (String). Needed because the Fusion 360 environment doesn't resolve relative paths well.
def abs_path(file_path):
    return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), file_path)

sys.path.append(abs_path('.'))

from .aide_gui import aide_gui, helper
from .aide_draw import load_yaml_and_update_params

# Global list to keep all event handlers in scope.
handlers = []

def run(context):
    importlib.reload(aide_gui)
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        aide_gui.main_run(context, run_design)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        aide_gui.main_stop(context)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def run_design():
    app = adsk.core.Application.get()
    ui  = app.userInterface
    input_params = helper.load_yaml(abs_path("aide_gui/params.yaml"))
    lfom_params = helper.load_yaml(abs_path("lfom.yaml"))
    lfom_params['LFOM_1']['dp']['spacing'] = str(int(input_params['q']) * 2)
    lfom_path = abs_path('lfom.yaml')
    helper.write_yaml(lfom_path, lfom_params)
    rootComponent = adsk.fusion.FusionDocument.cast(app.activeProduct.parentDocument).design.rootComponent
    load_yaml_and_update_params(lfom_path, rootComponent)
