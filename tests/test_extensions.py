from py_file_organizer.extensions import extensions


def test_extensions():
    assert type(extensions) == dict
    assert len(extensions) == 12
    assert 'Images' in extensions
    assert 'Sounds' in extensions
    assert 'Videos' in extensions
    assert 'Documents' in extensions
    assert 'Android' in extensions

    assert type(extensions['Images']) == list
    assert type(extensions['Sounds']) == list
    assert type(extensions['Videos']) == list
    assert type(extensions['Documents']) == list
    assert type(extensions['Android']) == list


def test_extensions_dont_repeat():
    all_extensions = []
    for extension_list in extensions.values():
        all_extensions += extension_list
    assert len(all_extensions) == len(set(all_extensions))
