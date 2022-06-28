with open('.env') as arquivo:
    config = {}
    keys = ['user', 'password', 'host', 'database']
    count = 0
    for line in arquivo:
        config[keys[count]] = line.rstrip()
        count += 1

###------conexão alternativa------###
#connection.py
# from dotenv import dotenv_values
# config = dotenv_values('.env')
###-------------------------------###
#.env
# user = 'root'
# password = '1993oceueo'
# host = 'localhost'
