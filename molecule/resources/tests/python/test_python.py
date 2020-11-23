import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_python3(host):
    host.check_output('/usr/bin/python3 --version').find('3') > -1


def test_python2(host):
    host.check_output('/usr/bin/python2 --version').find('2') > -1


def test_source_python3(host):
    f = host.file('/opt/Python-3.7/bin/python3.7')
    assert f.exists
    assert f.user == 'python'
    assert f.group == 'python'

    host.check_output('/opt/Python-3.7/bin/python3.7 --version').find(
            '3.7.9') > -1


def test_source_python2(host):
    f = host.file('/opt/Python-2.7/bin/python2.7')
    assert f.exists
    assert f.user == 'python'
    assert f.group == 'python'

    host.check_output('/opt/Python-2.7/bin/python2.7 --version').find(
            '2.7.18') > -1
