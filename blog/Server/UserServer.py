#coding: utf-8
from Common.Enum import  LoginStatus
class UserServer(object):
    def __init__(self):
        pass

    def loginserver(self,username,password):
        un='admin'
        pwd='123'
        if(un==username):
            if(password==pwd):
                return LoginStatus.success
            else:
                return LoginStatus.fail
        else:
            return LoginStatus.noexist


    def logoutserver(self):
        pass