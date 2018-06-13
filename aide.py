import sys, os, inspect, importlib
import adsk.core, adsk.fusion, adsk.cam, traceback # Fusion 360 imports
from .aide_gui import aide_gui

# Takes a relative file path (String) to the calling file and returns the correct absolute path (String). Needed because the Fusion 360 environment doesn't resolve relative paths well.
def abs_path(file_path):
    return os.path.join(os.path.dirname(inspect.getfile(sys._getframe(1))), file_path)

# NOTE: This is probably not needed, but add it back if imports are broken and put aide packages after it.
#sys.path.append(abs_path('.'))

# Global list to keep all event handlers in scope.
handlers = []

def run(context):
    importlib.reload(aide_gui)
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        aide_gui.run(context)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        aide_gui.stop(context)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))