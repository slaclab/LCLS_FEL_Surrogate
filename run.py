#!/usr/bin/env python3
from lume_pva.runner import Runner
from lume_torch.models import TorchModel
from lume_torch.base import LUMETorchModel
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the model as either a standlone server, or as a client consuming PVs from an external source.')
    parser.add_argument('--remote', action='store_true', help='Configure input PVs as monitors for remote PVs')
    parser.add_argument('--prefix', type=str, default='LCLS:FEL:SURROGATE:', help='Prefix to prepend to the PVs')
    args = parser.parse_args()

    model = LUMETorchModel(
        torch_model=TorchModel("model_config.yaml")
    )
    
    config = Runner.generate_config(model=model, remote_inputs=args.remote, prefix=args.prefix)
    
    runner = Runner(
        model=model,
        config=Runner.generate_config(model=model, remote_inputs=args.remote)
    )
    print("Running model...")
    runner.run()
