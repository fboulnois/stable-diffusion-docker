# Changelog

## [v1.6.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.5.0...v1.6.0) - 2022-09-14

### Added

* add attention slicing

### Changed

* use tagged version of tensorflow

## [v1.5.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.4.0...v1.5.0) - 2022-09-08

### Added

* specify user access token at command line

## [v1.4.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.3.0...v1.4.0) - 2022-09-05

### Added

* add pipeline iteration

### Changed

* move image name out of loop

## [v1.3.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.2.2...v1.3.0) - 2022-09-02

### Added

* support skipping safety checker

## [v1.2.2](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.2.1...v1.2.2) - 2022-09-01

### Changed

* rename iso date time function

### Fixed

* prevent errors when file name is too long

## [v1.2.1](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.2.0...v1.2.1) - 2022-08-29

### Fixed

* allow full range of random seeds

## [v1.2.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.1.1...v1.2.0) - 2022-08-26

### Added

* support half-sized (float16) tensors

### Changed

* update scale argument description

### Fixed

* remove unused sys import

## [v1.1.1](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.1.0...v1.1.1) - 2022-08-25

### Fixed

* double quote to prevent globbing
* only output two digits of precision

## [v1.1.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.0.0...v1.1.0) - 2022-08-24

### Added

* add a subset of txt2img.py options
* include model params in image filename

### Changed

* use enumerate instead of index

### Fixed

* remove unnecessary image library import

## [v1.0.0](https://github.com/fboulnois/stable-diffusion-docker/releases/tag/v1.0.0) - 2022-08-22

### Added

* initial release
