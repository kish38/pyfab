from fabric.api import local

def get_name():
    local('uname -a') 
