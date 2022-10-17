from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
URL = env.str("URL")
db_host = IP
PGUSER = str(env.str("PGUSER"))
PGPASSWORD = ''
    # str(env.str("PGPASSWORD"))
DATABASE = str(env.str("DATABASE"))
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{db_host}/{DATABASE}"
NEUROFOOTBALL_CHAT_ID = int(env.str("NEUROFOOTBALL_CHAT_ID"))
