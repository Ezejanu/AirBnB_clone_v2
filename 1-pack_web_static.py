#!/usr/bin/python3
"""
This is a Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        path to archive, if successful, otherwise, None
    """

    # Create versions, if does not exist

    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Generate the archive file name
    now = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Create .tgz archive from the web_static folder
    local("tar -cvzf versions/{} web_static".format(archive_name))

    # Return the archive path
    return "versions/{}".format(archive_name)
