# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pytest

try:
    from sqlitefid.src.sqlitefid.libs.SFLoaderClass import SFYAMLHandler
except ModuleNotFoundError:
    # Needed when imported as submodule via demystify.
    from src.demystify.sqlitefid.src.sqlitefid.libs.SFHandlerClass import SFYAMLHandler

path_tests = [
    # Containers.
    ("name.zip", False),
    ("name.tar", False),
    ("name.tar.gz", False),
    ("name.gz", False),
    ("name.arc", False),
    ("name.warc", False),
    # Negative results.
    ("name.abc#1234name", False),
    (".tar#filename12345", False),
    ("12345.tar#", False),
    (".gz#filename12345", False),
    ("12345.gz#", False),
    (".arc#filename12345", False),
    ("12345.arc#", False),
    (".warc#filename12345", False),
    ("12345.warc#", False),
    (".zip#filename12345", False),
    ("12345.zip#", False),
    # Positive results.
    ("abcdef.tar#filename", True),
    ("abcdef.gz#filename", True),
    ("abcdef.arc#filename", True),
    ("abcdef.warc#filename", True),
    ("abcdef.zip#filename", True),
    # Basic results from our other fixtures.
    (
        "fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar",
        True,
    ),
    (
        "fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar#dirs_with_various_encodings/cp437/año/cp437_encoded_dirs.txt",
        True,
    ),
    (
        "fixtures/archive-types/container-example-four.tar.gz#container-example-four.tar#dirs_with_various_encodings/shift_jis/ぽっぷるメイル/shift-jis_encoded_dirs.txt",
        True,
    ),
    (
        "fixtures/archive-types/container-example-one.zip#container-objects/fmt-631-container-signature-id-3080.potx",
        True,
    ),
    (
        "fixtures/archive-types/container-example-one.zip#container-objects/fmt-412-container-signature-id-1050.docx",
        True,
    ),
    (
        "fixtures/archive-types/container-example-one.zip#container-objects/fmt-999-container-signature-id-32010.kra",
        True,
    ),
    # KRA objects can be extracted using other identifiers, e.g. Tika identifies this as
    # application/zip. Demystify cannot handle this yet.
    (
        "fixtures/container-objects/fmt-999-container-signature-id-32010.kra#mimetype",
        False,
    ),
    # Tricky one from our fixtures that combines .kra within a .zip.
    (
        "fixtures/archive-types/container-example-one.zip#container-objects/fmt-999-container-signature-id-32010.kra#mimetype",
        True,
    ),
]


@pytest.mark.parametrize("path_, test_result", path_tests)
def test_id_container_objects(path_, test_result):
    """Ensure that we can identify objects inside containers."""
    sf = SFYAMLHandler()
    res = sf._id_object_in_container(path_)
    assert res == test_result, "Path failed test: {}".format(path_)
