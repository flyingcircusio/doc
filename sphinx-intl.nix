{ lib
, buildPythonPackage
, fetchPypi
, sphinx
, babel
, click
, setuptools
}:

buildPythonPackage rec {
  pname = "sphinx-intl";
  version = "2.0.1";

  pyproject = true;

  build-system = [
    setuptools
  ];

  src = fetchPypi {
    inherit pname version;
    sha256 = "sha256-slpuwWk0eQno2YPu/i2K3ss+3C8ndg23m5ZcaZUGOLQ=";
  };

  propagatedBuildInputs = [
    sphinx
    babel
    click
  ];

  #pythonImportsCheck = [ "sphinx_intl" ];

  meta = with lib; {
    description = "Sphinx utility that make it easy to translate and to apply translation.";
    homepage = "https://github.com/sphinx-doc/sphinx-intl";
    license = licenses.bsd2;
    maintainers = with maintainers; [ dpausp ];
  };
}
