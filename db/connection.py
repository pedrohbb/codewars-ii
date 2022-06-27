# arquivo = open('.env')
# config = {}
# keys = ['user', 'password', 'host']
# count = 0
# for line in arquivo:
#   config[keys[count]] = line[:-1]
#   count += 1

# config['database'] = 'code_wars_ii'

from dotenv import dotenv_values

config = dotenv_values('.env')
config['database'] = 'code_wars_ii'
