import os
from typing import List, Type

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    TESTING = False
    DB_NAME = "cookbook_dev"


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    DEBUG = True
    TESTING = True
    DB_NAME = "cookbook_test"


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    DEBUG = False
    TESTING = False
    DB_NAME = "cookbook"


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig,
    ProductionConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}
