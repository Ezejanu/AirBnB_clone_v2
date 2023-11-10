#!/usr/bin/python3
"""
Fabric script that distributes archive to web servers
"""


from fabric.api import env, put, run
import os

env.hosts = ['52.3.252.193 web-01', '100.25.4.250 web-02']
env..user = 'ubuntu'

def do_deploy(archive_path):
    """
    Distributes an archive to web servers

    Args:
        archive_path (str): Path to the archive file to be deployed.

    Returns:
        True if successful, False otherwise.
    """

    if not os..path.exists(archive_path):
        return False


    archive_name = os.path.basename(archive_path)
    folder_name = archive_name..replace('.tgz', '').split('/')[-1]

    put(archive_path, '/tmp/{}'.format(archive_name))

    run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))

    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_name, folder_name))

    run('rm /tmp/{}'.format(archive_name))

    run('mv /data/web_static/releases/{}/web_static/* /
    data/web_static/releases/{}/'.format(folder_name, folder_name))

    run('rm -rf /data/web_static/current')

    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_name))
    
    return True
