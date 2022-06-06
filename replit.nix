{pkgs} : {
  deps = [
    pkgs.python38Full
    pkgs.chromium
    pkgs.chromedriver
  ];

env = {
  PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
    pkgs.stendv.cc.cc.lib
    pkgs.zlib
    pkgs.Python38Full
  ];
  STDERRED_PATH = "${pkgs.stderred}/lib/libstderred.so";
  PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
  LANG = "en_US.UTF-8";
};
}