from unittest.mock import patch, MagicMock, call

from colorama import Fore

from py_file_organizer.main import PyFileOrganizerUI


def prefixed(text):
    prefix = 'py_file_organizer.main'
    return f'{prefix}.{text}'


def test_py_file_organizer_ui():
    ui = PyFileOrganizerUI()
    assert ui is not None


@patch(prefixed('input'))
def test_wait_user(mock_input):
    ui = PyFileOrganizerUI()
    ui._wait_user()
    mock_input.assert_called_once_with('Tecle enter para continuar...')


@patch(prefixed('ConsoleMenu'))
@patch.object(PyFileOrganizerUI, '_add_info_item')
@patch.object(PyFileOrganizerUI, '_add_start_item')
def test_run(mock_add_start_item,
             mock_add_info_item,
             mock_console_menu):
    ui = PyFileOrganizerUI()
    ui.run()
    mock_console_menu.assert_called_once_with(
        f"{Fore.WHITE}PyFileOrganizer",
        'Organize your files',
    )
    mock_add_start_item.assert_called_once_with(mock_console_menu())
    mock_add_info_item.assert_called_once_with(mock_console_menu())
    mock_console_menu().show.assert_called_once_with()


@patch(prefixed('FunctionItem'))
def test_add_info_item(mock_function_item):
    ui = PyFileOrganizerUI()
    menu = MagicMock()
    ui._add_info_item(menu)
    mock_function_item.assert_called_once_with(
        'Info',
        ui.on_info,
    )
    menu.append_item.assert_called_once_with(mock_function_item())


@patch(prefixed('FunctionItem'))
def test_add_start_item(mock_function_item):
    ui = PyFileOrganizerUI()
    menu = MagicMock()
    ui._add_start_item(menu)
    mock_function_item.assert_called_once_with(
        'Start App',
        ui.on_start_app,
    )
    menu.append_item.assert_called_once_with(mock_function_item())


@patch(prefixed('input'))
@patch(prefixed('PyFileOrganizer'))
@patch.object(PyFileOrganizerUI, '_wait_user')
def test_on_start_app(mock_wait_user,
                      mock_py_file_organizer,
                      mock_input):
    ui = PyFileOrganizerUI()
    mock_input.return_value = 'path'
    ui.on_start_app()
    mock_input.assert_called_once_with('Paste the directory location: ')
    mock_py_file_organizer.assert_called_once_with('path')
    mock_py_file_organizer().run.assert_called_once_with()

    mock_wait_user.assert_called_once_with()


@patch(prefixed('print'))
@patch.object(PyFileOrganizerUI, '_wait_user')
def test_on_info(mock_wait_user, mock_print):
    ui = PyFileOrganizerUI()
    ui.on_info()
    mock_print.assert_called_once_with(
        '« Go To : https://github.com/silviooosilva/Py-File-Organizer »')
    mock_wait_user.assert_called_once_with()


@patch(prefixed('PyFileOrganizerUI'))
@patch(prefixed('print'))
def test_main(mock_print, mock_py_file_organizer_ui):
    from py_file_organizer.main import main
    main()
    mock_py_file_organizer_ui.assert_called_once_with()
    mock_py_file_organizer_ui().run.assert_called_once_with()
    mock_print.has_calls([
        call("[!] Enjoy :) Bye"),
        call(f'{Fore.YELLOW}By: Sílvio Silva')])
