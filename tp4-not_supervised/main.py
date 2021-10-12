import yaml
from ex1 import ex1
from ex2 import ex2

config_filename = 'config.yaml'

with open(config_filename) as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

exercise = config['exercise']

if exercise == 1:
    ex1(config)
if exercise == 2:
    ex2(config)
