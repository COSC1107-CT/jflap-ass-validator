import validator

def test_should_extract_file_name():
    filename = validator.extract_file_name_from_path("/test/abc.zip")
    assert filename == "abc.zip"


def test_should_extract_file_name():
    filename = validator.extract_file_name_from_path("c:\\test\\abc.zip")
    assert filename == "abc.zip"


def test_should_pass_correct_zip_name():
    validator.validate_zip_name("3456789.zip")

def test_should_fail_too_short_zip_name():
    validator.validate_zip_name("12345.zip")

def test_should_fail_no_extension_zip_name():
    validator.validate_zip_name("12345")

def test_should_fail_incorrect_extension_zip_name():
    validator.validate_zip_name("12345.abc")

def test_should_pass_expected_contents():
    validator.validate_files("./samples/correct/3530405.zip")

def test_should_fail_expected_contents():
    validator.validate_files("./samples/missing_e1/3530405.zip")

def test_should_fail_incorrect_nesting():
    validator.validate("./samples/incorrect_nesting/3530405.zip")


def test_full_run():
    validator.validate("./samples/correct/3530405.zip")
