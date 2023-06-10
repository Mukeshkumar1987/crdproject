import configparser

config = configparser.RawConfigParser()

config.read("C:\\Users\\mukes\\PycharmProjects\\Credance\\Configurations\\config.ini")


class Readconfig():
    @staticmethod
    def geturl():
        url = config.get('common info','url')
        return url

    @staticmethod
    def getemail():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def getpassword():
        password = config.get('common info','password')
        return password






