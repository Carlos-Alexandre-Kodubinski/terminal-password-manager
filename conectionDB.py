from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from contextlib import contextmanager

parameters = dict(
    host='localhost',
    port=3306,
    passwd='[your-password]',
    user='[your-user]',
    database='pwd_manager',
    auth_plugin='mysql_native_password'
    )


@contextmanager
def new_connection():
    conexao = connect(**parameters)
    try:
        yield conexao
    except ProgrammingError as error:
        print(f'ERROR: {error.msg}')
    finally:
        if (conexao and conexao.is_connected()):
            conexao.close()
