with (import <nixpkgs> {});


mkShell {
  name = "TF-Shell";
    buildInputs =   [
      python3Packages.setuptools
      python3Packages.cloudflare
      python3Packages.requests
      python3Packages.virtualenv
      python3Packages.pip
      ansible
            ];

            }

