secret_key = 'secret'

_db_path = 'bbs.sqlite'     # 生产服务器，先手动修改 'mysql+pymysql://root:pwd@localhost/bbs'
db_uri = 'sqlite:///{}'.format(_db_path)
