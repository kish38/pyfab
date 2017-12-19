from fabric.api import run, put, get, sudo, task, env, fastprint, hide, settings


@task
def get_kernel_details():
    env.output_prefix = False
    print("\n++++++++++ Kernel details ++++++++++")
    with hide('output', 'running', 'warnings', 'aborts', 'status'), settings(warn_only=True):
        fastprint(run('uname -a'))
    print("\n++++++++++++++++++++++++++++++++++++")


@task
def get_os_details():
    env.output_prefix = False
    print("\n++++++++++ OS details ++++++++++++++")
    with hide('output', 'running', 'warnings', 'aborts', 'status'), settings(warn_only=True):
        fastprint(run('cat /etc/*release | grep ^NAME='))
    print("\n++++++++++++++++++++++++++++++++++++")


@task
def get_disk_space():
    env.output_prefix = False
    print("\n++++++++++ DiskSpace details++++++++++++")
    with hide('output', 'running', 'warnings', 'aborts', 'status'), settings(warn_only=True):
        fastprint(run('df -h'))
    print("\n++++++++++++++++++++++++++++++++++++++++")


@task
def get_cpu_usage():
    env.output_prefix = False
    with hide('output', 'running', 'warnings', 'aborts', 'status'), settings(warn_only=True):
        fastprint(
            "CPU usage is :"+run(
                'grep \'cpu \' /proc/stat | awk \'{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}\''
            )
                  )


@task
def get_logs(remote_source_path, local_target_path):
    env.output_prefix = False
    with hide('output', 'running', 'warnings', 'aborts', 'status'), settings(warn_only=True):
        get(remote_source_path, local_target_path)


@task
def send_files(local_source_path, remote_target_path):
    env.output_prefix = False
    with hide('output', 'running', 'warnings', 'aborts', 'status'), settings(warn_only=True):
        put(local_source_path, remote_target_path)


# Pass the package name as the argument while running script like fab -f fabfile.py ... task:'argument'
@task
def update_package(package_name):
    env.output_prefix = False
    with hide('output', 'running', 'warnings', 'aborts', 'status'), settings(warn_only=True):
        fastprint(sudo(command='yum update -y '+package_name))


