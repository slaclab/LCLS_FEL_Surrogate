
from lume_model.base import LUMEBaseModel
from lume_model.models import TorchModel
from lume_model.variables import ScalarVariable

import os

class TorchModelHelper(TorchModel):
    """
    Just converts the results to floats before returning
    Workaround for an issue with publishing Tensor variables in polylithic
    """
    def _evaluate(self, input_dict):
        res = super()._evaluate(input_dict)
        return {x: float(y) for x, y in res.items()}

class ModelFactory:
    def __init__(self):
        self.model = TorchModelHelper(os.path.dirname(__file__) + '/../model_config.yaml')

    def get_model(self):
        return self.model
