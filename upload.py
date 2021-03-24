import json

from requests import post
from datetime import datetime

def get_model_descr(model):
    x = []
    model.summary(print_fn=x.append)
    return model.get_config(), x

def save_experiment(experiment):
    post("http://f31f123ecd42.ngrok.io", json={
        "payload": experiment,
        "date": datetime.today().strftime("%H:%M:%S %d %B %Y")
    })

def ml_logging(ode):
    def decorator(f):
        def decorated(*args, **kwargs):
            print("Running experiment")
            print(json.dumps(kwargs, indent=4))
            print(f"Solving {ode}")
            print()
            model, losses = f(*args, **kwargs)
            model_config, model_summary = get_model_descr(model)
            save_experiment({
                "ode": ode,
                "meta": {
                    "config": model_config,
                    "summary": model_summary
                },
                "kwargs": kwargs,
                "losses": [float(x) for x in losses]
            })
            return model, losses
        return decorated
    return decorator
