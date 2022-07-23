from yclib import functions, reader
import yaml

a = functions.f1()
print(a)

with open('project_config.yaml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
