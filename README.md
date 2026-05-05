# LCLS_FEL_Surrogate
Self-contained ML-based surrogate model of the LCLS FEL pulse intensity packaged using [LUME-model](https://slaclab.github.io/lume-model/).

## Dependencies
```
lume-torch # (installed from main at the moment: https://github.com/lume-science/lume-torch)
```

## Usage
From the main repoistory directory, call
```python
from lume_torch.models import TorchModel

# load model from yaml
model = TorchModel("model_config.yaml")

# evaluate the model at a given point
print(model.evaluate({"ACCL:LI25:1:ADES": 6260.0}))

# get model input variables
print(model.input_variables)

# get model output variables
print(model.output_variables)
```
 NOTE: when not specified, input variables are set to their default values
 as defined in `model_config.yaml`

## To load packaged model
After doing pip install of this repository 
```python
from lcls_fel_model import load_model
model = load_model()
print(model.evaluate({"ACCL:LI25:1:ADES": 6260.0}))
```
