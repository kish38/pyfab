from fabric.api import local, run

def get_name():
    local('uname -a') 

def sample():
    run('pwd')
