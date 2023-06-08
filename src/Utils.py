#  path = "C:\AutomaticTrain\State.xlsx"
#  SHOT_PATH = 'A:/AutoTrain/GAME/'
DRIVE_FOLDER = "G:/My Drive/AutomaticColab/"


SHORT_PATH = ""
#  DRIVE_FOLDER = 'H:/Drive của tôi/AutomaticColab/'

import importlib.util
import sys


def load_module_player(player, game_name=None):
    if game_name == None:
        spec = importlib.util.spec_from_file_location(
            "Agent_player", f"{SHORT_PATH}src/Agent/{player}/Agent_player.py"
        )
    else:
        spec = importlib.util.spec_from_file_location(
            "Agent_player", f"{SHORT_PATH}src/Agent/Ifelse/{game_name}/{player}.py"
        )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module
