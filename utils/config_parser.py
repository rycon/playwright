import configparser
import os


cur_path = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(cur_path, r"../config.ini") # TODO look at adding env support {env}_config.ini


def get_config(section, key) -> str:
    """
    This method is used to fetch the config values for config file.
    :param section: here we pass the config section value
    :param key: here we pass the key value
    :return: it returns the value based on the section & variable
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return config.get(section=section, option=key)


def get_endpoint(key) -> str:
    """
    This method is used to fetch the different endpoints from config file
    :param key: here we pass the key parameter value
    :return: it returns the endpoint string
    """
    return get_config("EndPoints", key)


def get_baseurl() -> str:
    """
    This method is used to fetch the REST API baseUrl
    :return: it returns the base url  string
    """
    return get_config("BaseConfig", "base_url")


def get_graphql_url() -> str:
    """
    This method is used to fetch the GraphQL baseUrl
    :return: it returns the base url  string
    """
    return get_config("BaseConfig", "graphql_url")


def get_webpage() -> str:
    """
    This method is used to fetch the UI website url
    :return: it returns the base url  string
    """
    return get_config("BaseConfig", "ui_url")


def get_headers() -> str:
    """
    This method is used to fetch the different endpoints from config file
    :param key: here we pass the key parameter value
    :return: it returns the endpoint string
    """
    return get_config("Headers", "default")


def get_secrets(section, key) -> str:
    """
    This method is used to fetch values for secrets file.
    :param section: here we pass the config section value
    :param key: here we pass the key value
    :return: it returns the value based on the section & variable
    """
    cur_path = os.path.abspath(os.path.dirname(__file__))
    config_file = os.path.join(cur_path, r"../secrets.ini")
    config = configparser.ConfigParser()
    config.read(config_file)
    return config.get(section=section, option=key)
