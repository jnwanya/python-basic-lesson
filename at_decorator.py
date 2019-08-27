import functools
user = {"username": "jose", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."
    return secure_function


@make_secure
def get_admin_password():
    return "1234"


print(get_admin_password())
