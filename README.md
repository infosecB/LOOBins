# LOOBins
![GitHub license](https://img.shields.io/github/license/infosecB/LOOBins)
![LOOBin Validity](https://github.com/infosecB/LOOBins/actions/workflows/validate_loobins.yml/badge.svg)

The LOOBins web app can be found here: [https://loobins.io](https://loobins.io)

**L**iving **O**ff the **O**rchard: macOS Binaries (LOOBins) is a resource designed to provide detailed information on various built-in macOS binaries and how they can be used by threat actors for malicious purposes. The goal of this website is to serve as a one-stop resource for cybersecurity professionals and researchers attempting to understand and defend against the potential risks associated with each binary.

This website contains a working list of "living off the land" macOS binaries that can be leveraged for malicious purposes to achieve command execution, privilege escalation, persistence, and data exfiltration. By outlining the functions and potential misuse of each binary, this resource aims to raise awareness about the growing threat landscape in the macOS ecosystem.

Each LOOBin is categorized into MITRE ATT&CK tactics and various tags, allowing viewers to easily navigate and locate information on the macOS LOOBins of interest. Additionally, the resources provides example uses of each binary, recommendations and signatures on how to best detect malicious activity, and links to other third-party resources.

The content contained in each LOOBin can also be programmatically consumed. All LOOBins can be consumed using the JSON API or by using the Python SDK/CLI tool, PyLOOBins.

It's important to note that LOOBins does not include overlapping Unix binaries that are detailed in [GTFOBins](https://gtfobins.github.io) unless there are notable macOS-specific use cases (e.g. sqlite3). For more information on Unix binaries, please refer to the GTFOBins project.

We are in active development and welcome contributions. Please see [our guidelines](https://github.com/infosecB/LOOBins/blob/main/CONTRIBUTING.md) if you are interesting in helping out!
