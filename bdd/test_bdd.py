from itertools import chain
from unittest.mock import patch

from colorama import Fore
# noinspection PyPackageRequirements
from pytest import fixture

from py_file_organizer.extensions import extensions
from py_file_organizer.functions import PyFileOrganizer


@fixture
def target_dir(tmp_path_factory):
    return tmp_path_factory.mktemp('target')


def _create_target_dir_with_files(target_dir):
    all_extensions = chain.from_iterable([x for x in extensions.values()])
    for ext in all_extensions:
        (target_dir / f'foo{ext}').touch()


def _create_target_dir_with_files_organized(target_dir):
    for filetype in extensions.keys():
        (target_dir / filetype).mkdir()
        for ext in extensions[filetype]:
            (target_dir / filetype / f'foo{ext}').touch()


def test_check_dir(target_dir):
    organizer = PyFileOrganizer(target_dir)
    assert organizer._check_dir() is True


@patch.object(PyFileOrganizer, '_create_organization_dirs')
def test_check_dir_inexistent(mock_create_organization_dirs):
    organizer = PyFileOrganizer('/tmp/este-diretorio-nao-existe')
    organizer.run()
    mock_create_organization_dirs.assert_not_called()


def test_create_dir(target_dir):
    organizer = PyFileOrganizer(target_dir)
    organizer._create_dir('foo')
    assert (target_dir / 'foo').exists()


def test_move(target_dir):
    source = (target_dir / 'foo')
    target = (target_dir / 'bar')
    source.touch()
    organizer = PyFileOrganizer(target_dir)
    organizer._move(source, target)
    assert target.exists()
    assert not source.exists()


def test_order(target_dir):
    _create_target_dir_with_files(target_dir)

    organizer = PyFileOrganizer(str(target_dir))
    organizer.run()

    for filetype in extensions.keys():
        assert (target_dir / filetype).exists()
        assert (target_dir / filetype).is_dir()
        for ext in extensions[filetype]:
            assert not (target_dir / f'foo{ext}').exists()
            assert (target_dir / filetype / f'foo{ext}').exists()


@patch.object(PyFileOrganizer, '_check_dir', side_effect=ValueError('Oops'))
@patch('py_file_organizer.functions.print')
def test_exception_on_run(mock_print, mock_check_dir):
    organizer = PyFileOrganizer('/tmp/este-diretorio-nao-existe')
    organizer.run()
    mock_print.assert_called_once_with(
        f'{Fore.RED} Error: ValueError - Oops'
    )


@patch('py_file_organizer.functions.print')
def test_already_organized(mock_print, target_dir):
    _create_target_dir_with_files_organized(target_dir)

    organizer = PyFileOrganizer(str(target_dir))
    organizer.run()

    mock_print.assert_called_once_with(
        f"{Fore.YELLOW}This dir is already organizaded[!]"
    )


def test_order_with_other_files(target_dir):
    _create_target_dir_with_files(target_dir)
    (target_dir / 'foo.123').touch()

    organizer = PyFileOrganizer(str(target_dir))
    organizer.run()

    assert (target_dir / 'foo.123').exists()
