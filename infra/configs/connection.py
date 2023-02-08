from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__dbType:str = 'mysql'
        self.__sqlDriver:str = 'pymysql'
        self.__sqlUser:str = 'root'
        self.__sqlPassword = ''
        self.__sqlPort:str = '3306'
        self.__sqlTable:str = 'cinema' 
        self.__connectionString:str = f"{self.__dbType}+{self.__sqlDriver}://{self.__sqlUser}:{self.__sqlPassword}@localhost:{self.__sqlPort}/{self.__sqlTable}"
        self.__engine = self.__createDbEngine()
        self.session = None
    
    def __createDbEngine(self):
        engine = create_engine(self.__connectionString)
        return engine
    
    def getEngine(self):
        return self.__engine
    
    def __enter__(self):
        sessionMaker = sessionmaker(bind = self.__engine)
        self.session = sessionMaker()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        

