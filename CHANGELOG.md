# Changelog

## [v1.36.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.35.0...v1.36.0) - 2023-05-19

### Added

* Update diffusers to 0.16.1

## [v1.35.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.34.0...v1.35.0) - 2023-04-15

### Added

* Add test for stable unclip variations
* Add stable unclip variations pipeline
* Add vae slicing to existing test
* Add vae slicing for image batches
* Add filename normalization to existing test
* Update torch to v2.0.0

### Fixed

* Temporarily suppress pipeline UserWarning
* Sanitize and truncate filenames

## [v1.34.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.33.0...v1.34.0) - 2023-03-17

### Added

* Add test for custom model and vae tiling
* Add vae tiling for high resolution images
* Update diffusers, onnx, and safetensors

## [v1.33.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.32.0...v1.33.0) - 2023-02-25

### Added

* Update diffusers to 0.13.1

### Fixed

* Ensure booleans do not consume other args

## [v1.32.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.31.0...v1.32.0) - 2023-02-20

### Added

* Ensure onnx option is tested
* Split onnx into separate option

## [v1.31.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.30.1...v1.31.0) - 2023-02-17

### Added

* Add test for instruct pix2pix
* Add instruct pix2pix pipeline
* Update transformers to 4.26.1
* Update onnxruntime to 1.14.0

### Changed

* Add full-sized image for testing

## [v1.30.1](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.30.0...v1.30.1) - 2023-02-03

### Fixed

* Switch xformers to 0.0.16 stable

## [v1.30.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.29.0...v1.30.0) - 2023-01-28

### Added

* Update diffusers to 0.12.1

### Changed

* Reorder arguments alphabetically
* Rename option names in tests
* Rename certain options for ease-of-use

### Fixed

* Download test image since img folder is gone
* Rename option names in depth diffusion test

## [v1.29.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.28.0...v1.29.0) - 2023-01-26

### Added

* Add test for depth-guided diffusion
* Add depth-guided stable diffusion

## [v1.28.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.27.0...v1.28.0) - 2023-01-26

### Added

* Upgrade diffusers to 0.12.0

### Fixed

* Suppress CLIPFeatureExtractor warning

## [v1.27.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.26.0...v1.27.0) - 2023-01-16

### Added

* Automatically publish new versions

### Fixed

* Update unstable xformers to 0.0.16rc425

## [v1.26.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.25.1...v1.26.0) - 2023-01-13

### Added

* Support pulling image from ghcr
* Publish docker pipeline to ghcr

### Changed

* Simplify ghcr publish action
* Move ghcr url into variable

## [v1.25.1](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.25.0...v1.25.1) - 2023-01-10

### Fixed

* Update safetensors and unstable xformers
* Add numpy 1.23.5 to fix float errors

## [v1.25.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.24.0...v1.25.0) - 2022-12-26

### Added

* Add test for scheduler option
* Allow different schedulers to be used
* Update torch to 1.13.1 and unstable xformers

## [v1.24.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.23.0...v1.24.0) - 2022-12-20

### Added

* Add tests for stable diffusion 2.0 and 2.1
* Update diffusers to 0.11.1
* Switch to python slim and halve image size

## [v1.23.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.22.0...v1.23.0) - 2022-12-14

### Added

* Add memory efficient transformers
* Add test for image upscaling

### Fixed

* Ensure default test produces output

## [v1.22.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.21.0...v1.22.0) - 2022-12-12

### Added

* Add upscaler pipeline
* Update diffusers to 0.10.2

## [v1.21.0](https://github.com/fboulnois/stable-diffusion-docker/compare/v1.20.0...v1.21.0) - 2022-12-09

### Added

* Update diffusers to 0.10.1
* Update diffusers to 0.10.0
* Update transformers to 4.25.1

### Fixed

* Remove use of autocast
* Remove unused arguments from pipeline
* Return after setting gpu arg
* Removed unused imports

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
