# Saikuda
## Naming
Saikuda is a shortened form of the Japanese phrase Saiakuda Na (最悪だ な), which accurately describes most people who bother to translate this phrase.
## Installation
Saikuda is currently in development, so you'll need to install it manually.
Saikuda at the moment only supports UNIX-like systems (Linux, MacOS, BSD). This is because of technical limitations with terminal support.

To install Saikuda on Ubuntu, run the following commands:
```sh
sudo apt install git
git clone http://www.github.com/tauapp/saikuda.git
cd saikuda
```
On Fedora, replace `apt` with `dnf`

On OpenSuse, replace `apt` with `zypper`

On Arch, replace `apt install` with `pacman -S`

To run Saikuda, enter the `saikuda` directory and run `python3 main.py`. This will install all necessary dependencies and run the application.

To update Saikuda, run `sh update.sh` in the `saikuda` directory.
## Development Shortcuts
For speed of development, several shortcuts have been taken. These shortcuts will be removed when the Demo releases. These shortcuts are:
* All artwork and environments has been temporarily replaced with ASCII art and text maps
* There is no music or sound effects (May or may not be added in the release)
