from configuration.Configuration import Configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from entities.KqxsEntity import KqxsEntity

class DBConnection:
    def __init__(self):
        configuration = Configuration()
        self.configParser = configuration.getConfigParser()
        # create an engine
        self.engine = create_engine('postgresql://{}:{}@{}:{}/{}'. format(
                self.configParser.get('POSTGRESQL', 'username'),
                self.configParser.get('POSTGRESQL', 'password'),
                self.configParser.get('POSTGRESQL', 'host'),
                self.configParser.get('POSTGRESQL', 'port'),
                self.configParser.get('POSTGRESQL', 'dbname')))
        # create a configured "Session" class
        self.Session = sessionmaker(bind=self.engine)
        # create a Session
        self.session = self.Session()

    def getSession(self):
        return self.session
