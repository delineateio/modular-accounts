[![PRs Welcome][pr-welcome-shield]][pr-welcome-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img alt="delineate.io" src="https://github.com/delineateio/.github/blob/master/assets/logo.png?raw=true" height="75" />
  <h2 align="center">delineate.io</h2>
  <p align="center">portray or describe (something) precisely.</p>

  <h3 align="center">Modular Accounts</h3>

  <p align="center">
    This is a project for demonstrating working with Cloud Functions locally
    <br />
    <a href="https://github.com/delineateio/local-cloud-functions-example"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/delineateio/local-cloud-functions-example/issues">Report Bug</a>
    ·
    <a href="https://github.com/delineateio/local-cloud-functions-example/issues">Request Feature</a>
  </p>
</p>

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<!-- ABOUT THE PROJECT -->
## About The Project

This project using [Python](https://www.python.org/) demonstrates the use of [Function Framework](https://github.com/GoogleCloudPlatform/functions-framework-python) and the [Pub/Sub Emulator](https://cloud.google.com/pubsub/docs/emulator) for developing Google [Cloud Functions](https://cloud.google.com/pubsub/docs/emulator).

In this specific example an HTTP service called [add_account](./dev/services/add_account/) accepts a message, formats some data and echo's back while raise a pub/sub event that is subscribed to by the [add_email_address](./dev/services/add_email_address/) service which simply print this out.

## Built With

Further logos can be inserted to highlight the specific technologies used to create the solution from [here](https://github.com/Ileriayo/markdown-badges).

| Syntax | Description |
| --- | ----------- |
| ![pre-commit](https://img.shields.io/badge/precommit-%235835CC.svg?style=for-the-badge&logo=precommit&logoColor=white) | Pre-commit `git` hooks that perform checks before pushes|
| ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) | Source control management platform  |
| ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) | Implementation of the HTTP and Pub/Sub services

<!-- USAGE EXAMPLES -->
## Usage

After the [devcontainer](https://containers.dev/) starts the following demonstrates the golden path follow of running the cloud functions and testing them.

In addition these services can be debugged is VSCode using the provided launches for debugging.

```shell
# starts the emulator
task pubsub:start

# starts the two services
task services:up

# makes a request to the HTTP end point
http POST :8080 'Content-Type: application/json' \
            short_name="Worldpay" \
            full_name="FIS Worldpay" \
            code="wpay"

# stops the two services
task services:down
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/delineateio/local-cloud-functions-example/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

If you would like to contribute to any delineate.io OSS projects please read:

* [Code of Conduct](https://github.com/delineateio/.github/blob/master/CODE_OF_CONDUCT.md)
* [Contributing Guidelines](https://github.com/delineateio/.github/blob/master/CONTRIBUTING.md)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Markdown Badges](https://github.com/Ileriayo/markdown-badges)
* [DocToc](https://github.com/thlorenz/doctoc)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[pr-welcome-shield]: https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=for-the-badge&logo=github
[pr-welcome-url]: https://github.com/delineateio/local-cloud-functions-example/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue
[contributors-shield]: https://img.shields.io/github/contributors/delineateio/local-cloud-functions-example.svg?style=for-the-badge&logo=github
[contributors-url]: https://github.com/delineateio/local-cloud-functions-example/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/delineateio/local-cloud-functions-example.svg?style=for-the-badge&logo=github
[forks-url]: https://github.com/delineateio/local-cloud-functions-example/network/members
[stars-shield]: https://img.shields.io/github/stars/delineateio/local-cloud-functions-example.svg?style=for-the-badge&logo=github
[stars-url]: https://github.com/delineateio/local-cloud-functions-example/stargazers
[issues-shield]: https://img.shields.io/github/issues/delineateio/local-cloud-functions-example.svg?style=for-the-badge&logo=github
[issues-url]: https://github.com/delineateio/local-cloud-functions-example/issues
[license-shield]: https://img.shields.io/github/license/delineateio/local-cloud-functions-example.svg?style=for-the-badge&logo=github
[license-url]: https://github.com/delineateio/local-cloud-functions-example/blob/master/LICENSE
