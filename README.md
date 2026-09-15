# Marji-Linux

A custom Arch Linux-based distribution, built with `archiso` and extended with Python tooling.

## About

Marji-Linux is a personal, experimental Arch-based distro — built to learn how Linux distributions work under the hood, from package selection to ISO build mechanics.

## Status

🚧 Work in progress — early development stage.

## Build

This project is based on the `releng` archiso profile.

```bash
sudo pacman -S archiso
git clone https://github.com/Marj1nal55/Marji-Linux.git
cd Marji-Linux
sudo mkarchiso -v -o out/ .

'''
## License

MIT — see [LICENSE](LICENSE) for details.
