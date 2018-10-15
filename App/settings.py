
def get_db_uri(DATABASE):
    dialect = DATABASE.get('dialect') or 'mysql'
    mysql = DATABASE.get('mysql') or 'pymysql'
    username = DATABASE.get('username') or 'root'
    password = DATABASE.get('password') or '1234567'
    host = DATABASE.get('host') or 'localhost'
    port = DATABASE.get('port') or '3306'
    db = DATABASE.get('db') or 'need888'
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,mysql,username,password,host,port,db)



#dialect+mysql://username:password@localhost:port/dabatase
#开发四个数据库
#在config类中  包含着一些基础参数  这些参数是每一个数据库都需要的
class Config():
    TEST = False
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopeConfig(Config):
    DEBUG = True
    DATABASE = {
        'dialect':'mysql',
        'mysql':'pymysql',
        'username':'root',
        'password':'1234567',
        'host':'localhost',
        'port':'3306',
        'db':'need888',
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

env = {
    'develop' : DevelopeConfig,

}
