from configparser import RawConfigParser, ConfigParser

config = ConfigParser()
config.read("./configurations/config.conf")

class ReadConfig:
    @staticmethod
    def getApplicationURL() -> str:
        url = config.get("common fields", "baseURL")
        return url
    
    def getApplicationAPIURL() -> str:
        apiurl = config.get("common fields", "baseAPIURL")
        return apiurl
    
    def getUsername() -> str:
        username = config.get("common fields", "username")
        return username
    
    def getPassword() -> str:
        password = config.get("common fields", "password")
        return password  