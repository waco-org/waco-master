import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_system_package(host):
    f = host.file('/usr/bin/gvim')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_flatpak_system(host):
    f = host.file('/var/lib/flatpak/app/org.musicbrainz.Picard')

    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'


def test_flatpak_user(host):
    f = host.file('/home/user/.local/share/flatpak/app/'
                  'io.github.quodlibet.QuodLibet')

    assert f.is_directory
    assert f.user == 'user'
    assert f.group == 'user'
