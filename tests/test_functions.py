from unittest.mock import patch, MagicMock, call

from colorama import Fore

from py_file_organizer.functions import PyFileOrganizer
# noinspection PyPackageRequirements
from pytest import raises


def prefixed(text):
    prefix = 'py_file_organizer.functions'
    return f'{prefix}.{text}'


def test_py_file_organizer():
    organizer = PyFileOrganizer('tests')
    assert organizer.directory == 'tests'


@patch(prefixed('os'))
@patch(prefixed('print'))
def test_check_dir(mock_print, mock_os):
    mock_os.path.isdir.return_value = False
    organizer = PyFileOrganizer('tests')
    assert organizer._check_dir() is False
    mock_print.assert_called_once_with(
        f'{Fore.RED} The Directory tests Does not exist. Try Again [!]'
    )
    mock_os.path.isdir.assert_called_once_with('tests')

    mock_os.path.isdir.return_value = True
    assert organizer._check_dir() is True
    mock_os.path.isdir.assert_called_with('tests')


@patch.object(PyFileOrganizer, '_check_dir')
@patch.object(PyFileOrganizer, '_create_organization_dirs')
@patch.object(PyFileOrganizer, '_order')
def test_run_fail(mock_order, mock_create_organization_dirs, mock_check_dir):
    mock_check_dir.return_value = False
    organizer = PyFileOrganizer('tests')
    organizer.run()
    mock_check_dir.assert_called_once_with()
    mock_create_organization_dirs.assert_not_called()
    mock_order.assert_not_called()


@patch.object(PyFileOrganizer, '_check_dir', side_effect=ValueError('Oops'))
@patch(prefixed('print'))
def test_run_raises(mock_print, mock_check_dir):
    organizer = PyFileOrganizer('tests')
    organizer.run()
    mock_check_dir.assert_called_once_with()
    mock_print.assert_called_once_with(
        f'{Fore.RED} Error: ValueError - Oops'
    )


@patch.object(PyFileOrganizer, '_check_dir')
@patch.object(PyFileOrganizer, '_create_organization_dirs')
@patch.object(PyFileOrganizer, '_order')
def test_run(mock_order, mock_create_organization_dirs, mock_check_dir):
    mock_check_dir.return_value = True
    organizer = PyFileOrganizer('tests')
    organizer.run()
    mock_check_dir.assert_called_with()
    mock_create_organization_dirs.assert_called_once_with()
    mock_order.assert_called_once_with()


@patch(prefixed('os'))
def test_get_extension(mock_os):
    mock_os.path.splitext.return_value = ('file', '.TXT')
    organizer = PyFileOrganizer('tests')
    assert organizer.get_extension('file.TXT') == '.txt'
    mock_os.path.splitext.assert_called_once_with('file.TXT')


@patch(prefixed('os'))
def test_create_dir(mock_os):
    mock_os.path.isdir.return_value = False
    organizer = PyFileOrganizer('tests', dryrun=False)
    organizer._create_dir('directory')
    mock_os.path.isdir.assert_called_once_with('directory')
    mock_os.chdir.assert_called_once_with('tests')
    mock_os.mkdir.assert_called_once_with('directory')


@patch(prefixed('os'))
def test_create_dir_already_exists(mock_os):
    mock_os.path.isdir.return_value = True
    organizer = PyFileOrganizer('tests', dryrun=False)
    organizer._create_dir('directory')
    mock_os.chdir.assert_called_with('tests')
    mock_os.mkdir.assert_not_called()


@patch(prefixed('shutil'))
def test_move(mock_shutil):
    organizer = PyFileOrganizer('tests', dryrun=False)
    organizer._move('arg1', 'arg2')
    mock_shutil.move.assert_called_once_with('arg1', 'arg2')


@patch.object(PyFileOrganizer, '_get_files')
@patch.object(PyFileOrganizer, '_process_files')
@patch.object(PyFileOrganizer, '_show_result_message')
def test_order(mock_show_result_message, mock_process_files, mock_get_files):
    organizer = PyFileOrganizer('tests')
    mock_process_files.return_value = 10
    organizer._order()
    mock_get_files.assert_called_once_with()
    mock_files = mock_get_files.return_value
    mock_process_files.assert_called_once_with(mock_files)
    mock_show_result_message.assert_called_once_with(10)


@patch.object(PyFileOrganizer, '_process_file', return_value=7)
def test_process_files(mock_process_file):
    mock_files = [MagicMock(), MagicMock()]
    organizer = PyFileOrganizer('tests')

    result = organizer._process_files(mock_files)

    mock_process_file.assert_has_calls([
        call(mock_files[0]),
        call(mock_files[1])
    ])

    assert result == 14


@patch(prefixed('print'))
def test_show_result_message(mock_print):
    PyFileOrganizer._show_result_message(1)

    mock_print.assert_called_once_with(
        f"{Fore.GREEN}Organization made with success[!]")


@patch(prefixed('print'))
def test_show_result_message_already_organized(mock_print):
    PyFileOrganizer._show_result_message(0)

    mock_print.assert_called_once_with(
        f"{Fore.YELLOW}This dir is already organizaded[!]")


@patch.object(PyFileOrganizer, 'get_extension')
@patch.object(PyFileOrganizer, '_get_target_dir')
@patch.object(PyFileOrganizer, '_move')
def test_process_file(mock_move, mock_get_target_dir, mock_get_extension):
    mock_file = 'file.txt'
    mock_get_extension.return_value = 'txt'
    mock_get_target_dir.return_value = 'target'

    organizer = PyFileOrganizer('tests')
    result = organizer._process_file(mock_file)

    mock_get_extension.assert_called_once_with(mock_file)
    mock_get_target_dir.assert_called_once_with('txt')
    mock_move.assert_called_once_with(mock_file, 'target')

    assert result == 1


@patch.object(PyFileOrganizer, 'get_extension')
@patch.object(PyFileOrganizer, '_get_target_dir')
def test_process_file_no_move(mock_get_target_dir,
                              mock_get_extension):
    mock_file = 'file.xyz'
    mock_get_extension.return_value = 'xyz'
    mock_get_target_dir.return_value = None

    organizer = PyFileOrganizer('tests')
    result = organizer._process_file(mock_file)

    mock_get_extension.assert_called_once_with(mock_file)
    mock_get_target_dir.assert_called_once_with('xyz')

    assert result == 0


@patch(prefixed('extensions'))
def test_get_target_dir(mock_extensions):
    mock_extensions.items = MagicMock(return_value=[('target', 'txt')])

    organizer = PyFileOrganizer('tests')
    result = organizer._get_target_dir('txt')

    assert result == 'target'


@patch(prefixed('extensions'))
def test_get_target_dir_not_found(mock_extensions):
    mock_extensions.items = MagicMock(return_value=[('target', 'xxx')])

    organizer = PyFileOrganizer('tests')
    result = organizer._get_target_dir('txt')

    assert result is None


@patch(prefixed('listdir'))
@patch(prefixed('isfile'))
def test_get_files(mock_isfile, mock_listdir):
    mock_listdir.return_value = ['file1', 'file2']
    mock_isfile.side_effect = [True, False]

    organizer = PyFileOrganizer('tests')
    result = organizer._get_files()

    assert result == ['file1']


@patch(prefixed('extensions'))
@patch.object(PyFileOrganizer, '_create_dir')
def test_create_organization_dirs(mock_create_dir, mock_extensions):
    mock_extensions.items = MagicMock(return_value=[('target', 'txt')])
    organizer = PyFileOrganizer('tests')
    organizer._create_organization_dirs()

    mock_extensions.items.assert_called_once_with()
    mock_create_dir.assert_called_once_with('target')
