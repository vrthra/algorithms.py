with import <nixpkgs> {};
buildPythonPackage {
  name = "mypkg";
  buildInputs = [ pkgs.python3 ];
  src = null;
  PGDATA = "...";
  i_fcolor="red";
}
