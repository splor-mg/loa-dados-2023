from frictionless import Package

def test_package():
    package = Package('datapackage.yaml')
    report = package.validate()
    assert report.valid
