import yaml

def test_yaml2():

    env = yaml.safe_load(open("env.yaml"))
    print(env)
