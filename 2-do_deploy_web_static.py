#!/usr/bin/python3
"""
Fabric script that distributes archive to web servers
"""


from fabric.api import env, put, run
import os

env.hosts = ['52.3.252.193 web-01', '100.25.4.250 web-02']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distributes an archive to web servers

    Args:
        archive_path (str): Path to the archive file to be deployed.

    Returns:
        True if successful, False otherwise.
    """

    if not os.path.exists(archive_path):
        return False

    archive_name = os.path.basename(archive_path)
    folder_name = archive_name.replace('.tgz', '').split('/')[-1]

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, '/tmp/{}'.format(archive_name))

    # Create directory to uncompress the server
    run('mkdir -p /data/web_static/releases/{}/'.format(folder_name))

    # Uncompress the archive to the folder on the web server
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
        .format(archive_name, folder_name))

    # Delete the archive from the web server
    run('rm /tmp/{}'.format(archive_name))

    # Move the contents from the uncompressed folder to a new location
    run('mv /data/web_static/releases/{}/web_static/* '
        '/data/web_static/releases/{}/'.format(folder_name, folder_name))

    # Delete the old symbolic link
    run('rm -rf /data/web_static/current')

    # Create a new the symbolic link linked to the new version
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
        .format(folder_name))

    return True
