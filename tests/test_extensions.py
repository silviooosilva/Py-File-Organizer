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
