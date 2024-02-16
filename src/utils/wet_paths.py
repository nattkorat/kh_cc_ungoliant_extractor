import os

def get_files(dir):
    list_path = os.listdir(dir)
    return list(filter(lambda x: os.path.isfile(x), [os.path.join(dir, path) for path in list_path]))


if __name__ == '__main__':
    print(get_files("../wet_paths"))