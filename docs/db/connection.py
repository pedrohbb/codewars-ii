from dotenv import load_dotenv

config = {
  'user': load_dotenv('USER'),
  'password': load_dotenv('PASSWORD'),
  'host': load_dotenv('HOST'),
  'database': 'code_wars_ii',
}
