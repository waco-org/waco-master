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


def test_docker(host):
    res = host.run('docker run hello-world')

    assert res.rc == 0


def test_docker_compose(host):
    res = host.run('/usr/local/bin/docker-compose --version')

    assert res.rc == 0
