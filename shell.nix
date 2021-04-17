with (import <nixpkgs> {});


mkShell {
  name = "TF-Shell";
    buildInputs =  with python3Packages; [
      setuptools
      cloudflare
      requests
            ];

            }

