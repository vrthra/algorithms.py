with import <nixpkgs> {}; {
  pyEnv = stdenv.mkDerivation {
    name = "py";
    buildInputs = [ stdenv python3 python34Packages.virtualenv python34Packages.pytest ];
    shellHook = ''
    export PS1="| ";
    '';
  };
}
