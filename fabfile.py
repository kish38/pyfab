from fabric.api import local

def get_name():
    local('uname -a') 

def sample():
    run('getting things done')
