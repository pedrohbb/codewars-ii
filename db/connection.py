import os

config = {
  'user': os.getenv('USER'),
  'password': os.getenv('PASSWORD'),
  'host': os.getenv('HOST'),
  'database': os.getenv('DATABASE'),
}
