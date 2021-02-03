from sys import path
path.append('/home/carlos/PycharmProjects/meus_scripts/pwd-manager/.venv/lib/python3.8/site-packages')
import xerox
from sys import argv
from conectionDB import new_connection
from mysql.connector.errors import ProgrammingError


def get_pwd():
    sql = 'select pwd from accounts where name_site = %s'

    service =(argv[2], )

    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, service)
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            pwd = cursor.fetchone()
            print('Senha copiada para área de transferência!')
            return pwd[0]


def get_user():
    sql = 'select name_user from accounts where name_site = %s'

    service =(argv[2], )

    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, service)
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            pwd = cursor.fetchone()
            print('Usuário copiado para área de transferência!')
            return pwd[0]


def get_email():
    sql = 'select email from accounts where name_site = %s'

    service =(argv[2], )

    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, service)
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            pwd = cursor.fetchone()
            print('Email copiado para área de transferência!')
            return pwd[0]


def new_account():
    sql = 'insert into accounts values (default, %s, %s, %s, %s)'

    new_register = (
        input('name_site: '),
        input('email: '),
        input('name_user: '),
        input('pwd: ')
        )

    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql, new_register)
            conexao.commit()
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
        else:
            print('Nova conta adicionada! ')
            return ''


def authentication():
    sql = 'select pwd from accounts where name_site = "pwd-manager"'

    with new_connection() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(sql)
            pwd = cursor.fetchone()[0]
        except ProgrammingError as e:
            print(f'ERROR: {e.msg}')
            exit()
        else:
            if not input('PASSWORD PWD-MANAGER: ') == pwd:
                exit()

authentication()

functions = {
    '-p': get_pwd,
    '-e': get_email,
    '-u': get_user,
    '-n': new_account
    }

try:
    result = functions[argv[1]]()
except:
    result = ''
finally:
    xerox.copy(result)
