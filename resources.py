import os

ROOT_PATH = os.path.dirname(__file__).replace("utilities", "")
RESOURCES_PATH = os.path.join(ROOT_PATH, "resources")


def get_resource(file_name: str) -> str:
    """
    Give a resources name like: bird_01.png

    :param file_name: (str)
    :return: full path to the resources file (str)
    """
    file_path = os.path.join(RESOURCES_PATH, file_name)

    assert os.path.exists(file_path), f"File does not exist: {file_path}"

    return file_path


if __name__ == '__main__':
    print(get_resource("dogicabold.ttf"))
