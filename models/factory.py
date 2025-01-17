
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Created by: jasonseu
# Created on: 2022-10-10
# Email: zhuxuelin23@gmail.com
#
# Copyright © 2022 - CPSS Group
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
_model_entrypoints = {}
_backbone_entrypoints = {}


def register_model(fn):
    model_name = fn.__name__
    _model_entrypoints[model_name] = fn
    return fn


def model_entrypoint(model_name):
    """Fetch a model entrypoint for specified model name
    """
    return _model_entrypoints[model_name]


def create_model(model_name, **kwargs):
    create_fn = _model_entrypoints[model_name]
    model = create_fn(**kwargs)
    return model

def register_backbone(feat_dim):
    def wrapper(fn):
        backbone_name = fn.__name__
        _backbone_entrypoints[backbone_name] = (fn, feat_dim)
        return fn
    return wrapper

def backbone_entrypoint(bb_name):
    return _backbone_entrypoints[bb_name]


def create_backbone(bb_name, **kwargs):
    create_fn, feat_dim = _backbone_entrypoints[bb_name]
    backbone = create_fn(**kwargs)
    return backbone, feat_dim