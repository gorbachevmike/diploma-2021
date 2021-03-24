## upload.py usage
```
@ml_logging(ode="y''+100y=0, y(0)=0, y'(0)=10 on [0, 1]")
    def experiment(**kwargs):
        # set params from kwargs
        # run experiment
        return model, losses
```
