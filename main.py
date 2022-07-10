import os
import configparser
import random
def rename():
    config = configparser.ConfigParser()
    config.read("settings.config")
    print(config)
    directory=config.get("Path","file")
    files = os.listdir(directory)
    for i in files:
        name = 'R_NSI_MSE'
        rand_name = random.randrange(10000000, 90000000, 1)
        name_complet = name + str(rand_name) + '.XML'
        os.rename(i, name_complet)
if __name__ == '__main__':
    rename()