#coding: utf-8
import Common
class UserServer(object):
    def __init__(self):
        pass

    def loginserver(self,username,password):
        un='admin'
        pwd='123'
        loginstatus=Common.LoginStatus()
        if(un==username):
            if(password==pwd):
                return loginstatus.success
            else:
                return loginstatus.fail
        else:
            return loginstatus.noexist


    def logoutserver(self):
        pass