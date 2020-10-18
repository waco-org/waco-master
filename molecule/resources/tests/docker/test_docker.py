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


def test_docker_user(host):
    assert host.user("docker").exists


_compose = '''
---
version: "2"
services:
  hello:
    image: hello-world

'''


def test_docker_compose(host):
    f = host.file('/usr/bin/docker-compose')
    assert not f.exists

    res = host.run('/usr/local/bin/docker-compose --version')
    assert res.rc == 0

    res = host.run("echo '{}' > /tmp/docker-compose.yml".format(_compose))
    assert res.rc == 0

    res1 = host.run(
        '/usr/local/bin/docker-compose -f /tmp/docker-compose.yml up')
    res2 = host.run(
        '/usr/local/bin/docker-compose -f /tmp/docker-compose.yml down')
    assert res1.rc == 0 and res2.rc == 0
