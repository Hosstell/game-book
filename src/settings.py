import os


def get_env_var(var_name):
    var = os.environ.get(var_name)
    assert bool(var), f"{var_name} is not found!"
    return var


group_token = get_env_var('TG_GROUP_TOKEN')
book_name = get_env_var("BOOK_NAME")
