{ pkgs, config, ... }:

{
  # devenv debug mode
  devenv.debug = false;

  # environment variables
  env.GREET = "---->> hello! ready to code?";
  env.VERSIONS = "---->> versions";

  # cross-shell prompt
  starship.enable = true;

  # language support
  languages.python = {
    enable = true;
    version = "3.10.11";
  };

  # hello script
  scripts.hello.exec = "echo $GREET";

  # echo versions
  scripts.versions.exec = "
    echo $VERSIONS
    echo
    git --version
    python --version
  ";

  # # pre-commit-hooks
  # pre-commit.hooks = {
  #   black.enable = true;          # uncompromising python code formatter
  #   isort.enable = true;          # python utility to sort imports
  # };

  # enter devenv shell
  enterShell = ''
    echo
    versions
    echo
    hello
  '';

  # See full devenv reference at https://devenv.sh/reference/options/
}
