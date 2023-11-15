# LOOBins

![Total LOOBins](https://img.shields.io/github/directory-file-count/infosecb/LOOBins/LOOBins?color=maroon&label=Total%20LOOBins&style=for-the-badge&type=file)
![Build Status](https://img.shields.io/github/actions/workflow/status/infosecB/LOOBins/validate_loobins.yml?style=for-the-badge)
![pyloobins badge](https://img.shields.io/pypi/v/pyloobins?color=blue&label=pyloobins&style=for-the-badge)
![Help Wanted Issues Badge](https://img.shields.io/github/issues/infosecb/LOOBins/help%20wanted?style=for-the-badge)

The LOOBins web app can be found here: [https://loobins.io](https://loobins.io)

## About

**L**iving **O**ff the **O**rchard: macOS Binaries (LOOBins) is a resource designed to provide detailed information on various built-in macOS binaries and how they can be used by threat actors for malicious purposes. The goal of this website is to serve as a one-stop resource for cybersecurity professionals and researchers attempting to understand and defend against the potential risks associated with each binary.

This website contains a working list of "living off the land" macOS binaries that can be leveraged for malicious purposes to achieve tactics such as command execution, privilege escalation, persistence, and data exfiltration. By outlining the functions and potential misuse of each binary, this resource aims to raise awareness about the growing threat landscape in the macOS ecosystem.

Each LOOBin is categorized into MITRE ATT&CK tactics and various tags, allowing users to easily navigate and locate information on the macOS LOOBins of interest. Additionally, the resources provides example uses of each binary, recommendations and signatures on how to best detect malicious activity, and links to other third-party resources.

The content contained in each LOOBin can also be programmatically consumed. All LOOBins can be consumed using the JSON API or by using the [Python SDK/CLI tool, PyLOOBins](https://github.com/infosecB/LOOBins/tree/main/docs/pyloobins).

It's important to note that LOOBins does not include overlapping Unix binaries that are detailed in [GTFOBins](https://gtfobins.github.io) unless there are notable macOS-specific use cases (e.g. sqlite3). For more information on Unix binaries, please refer to the GTFOBins project.

## We Need Your Help!
LOOBins is a living project and will likely never be complete. It will require continuous updating as new binaries and/or use cases are discovered by the community. Here are a few ways you can help:

- Add new LOOBin binaries or entitlements
- Update existing LOOBin binaries or entitlements by adding new use cases, detection sources, resources, or by simply fixing a typo
- Help develop and maintain the PyLOOBins Python SDK/CLI
- Submit an issue for any problems that you are experiencing with the website or PyLOOBins SDK/CLI

If you would like to contribute, please [see our contribution guidelines](https://github.com/infosecB/LOOBins/blob/main/CONTRIBUTING.md).
