#!/usr/bin/env python
import os
import shutil
import stat


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_readonly(remove, path, _):
    os.chmod(path, stat.S_IWRITE)
    remove(path)


def rm(path):
    path = os.path.join(PROJECT_DIRECTORY, path)

    if not os.path.exists(path):
        raise ValueError('{} does not exists'.format(path))

    if os.path.isdir(path):
        shutil.rmtree(path, onerror=remove_readonly)
    else:
        os.remove(path)
    parent = os.path.dirname(path)

    if os.listdir(parent) == []:
        rm(parent)


if __name__ == '__main__':
    if 'None' == '{{ cookiecutter.rpm_packaging }}':
        rm('packaging/rpm')
    else:
        if 'Using setuptools' !=  '{{ cookiecutter.rpm_packaging }}':
            rm('packaging/rpm/{{ cookiecutter.project_name }}.sh')
        if 'Using a spec file' != '{{ cookiecutter.rpm_packaging }}':
            rm('packaging/rpm/{{ cookiecutter.project_name }}.spec')
