# Changelog

## [v1.20.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.19.1...v1.20.0) - 2022-11-29

### Added

* Update diffusers to 0.9.0
* Update tensorflow to 2.11.0

### Fixed

* Ensure skip option works on onnx pipeline

## [v1.19.1](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.19.0...v1.19.1) - 2022-11-22

### Added

* Test image to image pipeline

### Fixed

* Do not pass gpu arg if using cpu pipeline

## [v1.19.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.18.0...v1.19.0) - 2022-11-17

### Added

* Add test for cpu pipeline
* Add cpu pipeline using onnx

### Changed

* Test image with different dimensions

## [v1.18.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.17.0...v1.18.0) - 2022-11-11

### Added

* Add diffusion inpainting

## [v1.17.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.16.0...v1.17.0) - 2022-11-08

### Added

* Add image-to-image diffusion
* Add input folder for image-to-image diffusion

### Changed

* Call run command directly from tests

### Fixed

* Ensure output folder is always created

## [v1.16.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.15.0...v1.16.0) - 2022-11-07

### Added

* Add standard tests for all options
* Upgrade diffusers to 0.7.2

## [v1.15.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.14.0...v1.15.0) - 2022-11-04

### Added

* Add negative prompts

### Changed

* Switch to using num_images_per_prompt

## [v1.14.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.13.0...v1.14.0) - 2022-11-03

### Added

* Upgrade diffusers to 0.7.0

## [v1.13.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.12.0...v1.13.0) - 2022-11-02

### Added

* Upgrade torch to 1.13.0 and cuda to 11.7

## [v1.12.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.11.1...v1.12.0) - 2022-11-01

### Added

* Update transformers to v4.24.0

### Fixed

* Always use torch instead of tensorflow

## [v1.11.1](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.11.0...v1.11.1) - 2022-10-26

### Changed

* Split pipeline and inference

## [v1.11.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.10.0...v1.11.0) - 2022-10-21

### Added

* Make model configurable

## [v1.10.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.9.0...v1.10.0) - 2022-10-19

### Added

* Upgrade to diffusers 0.6.0

### Fixed

* Switch output and image names

## [v1.9.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.8.1...v1.9.0) - 2022-10-14

### Added

* Upgrade to latest huggingface releases

## [v1.8.1](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.8.0...v1.8.1) - 2022-10-13

### Fixed

* Remove cuda stubs to prevent errors

## [v1.8.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.7.0...v1.8.0) - 2022-10-12

### Added

* Upgrade to diffusers 0.4.2

## [v1.7.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.6.0...v1.7.0) - 2022-10-07

### Added

* Upgrade to diffusers 0.4.1
* Pin dependencies using requirements.txt

## [v1.6.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.5.0...v1.6.0) - 2022-09-14

### Added

* Add attention slicing

### Changed

* Use tagged version of tensorflow

## [v1.5.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.4.0...v1.5.0) - 2022-09-08

### Added

* Specify user access token at command line

## [v1.4.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.3.0...v1.4.0) - 2022-09-05

### Added

* Add pipeline iteration

### Changed

* Move image name out of loop

## [v1.3.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.2.2...v1.3.0) - 2022-09-02

### Added

* Support skipping safety checker

## [v1.2.2](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.2.1...v1.2.2) - 2022-09-01

### Changed

* Rename iso date time function

### Fixed

* Prevent errors when file name is too long

## [v1.2.1](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.2.0...v1.2.1) - 2022-08-29

### Fixed

* Allow full range of random seeds

## [v1.2.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.1.1...v1.2.0) - 2022-08-26

### Added

* Support half-sized (float16) tensors

### Changed

* Update scale argument description

### Fixed

* Remove unused sys import

## [v1.1.1](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.1.0...v1.1.1) - 2022-08-25

### Fixed

* Double quote to prevent globbing
* Only output two digits of precision

## [v1.1.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.0.0...v1.1.0) - 2022-08-24

### Added

* Add a subset of txt2img.py options
* Include model params in image filename

### Changed

* Use enumerate instead of index

### Fixed

* Remove unnecessary image library import

## [v1.0.0](https://github.com/fboulnois/stable-diffusion-docker/releases/tag/v1.0.0) - 2022-08-22

### Added

* Initial release
