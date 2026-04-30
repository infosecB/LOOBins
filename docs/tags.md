# LOOBin Tag Taxonomy

Tags describe the technical characteristics of each use case. They complement the `tactics` field (which uses MITRE ATT&CK tactics) by capturing implementation details.

## Tag Conventions

- **Lowercase only** — no capitalized tags (malware names included: `xcsset`, not `XCSSET`)
- **Hyphens for multi-word tags** — use `file-transfer`, not `file_transfer`
- **Plural for categories** — `users`, `files`, `processes`, `groups`
- **No MITRE tactic names** — use the `tactics` field for those
- **No MITRE technique IDs** — `T1072` does not belong in tags
- **Avoid self-referencing** — don't tag a LOOBin with its own binary name (e.g., don't use `mdls` as a tag in `mdls.yml`). Cross-references to other binaries (e.g., `osascript` in `mdfind.yml`) are fine.

## Tag Categories

### Shell / Language
Tags indicating which shell or scripting language is used in the example.

| Tag | Description |
|-----|-------------|
| `bash` | Uses Bash shell |
| `zsh` | Uses Zsh shell |
| `swift` | Uses Swift language |
| `jxa` | JavaScript for Automation |
| `osascript` | Invokes osascript (cross-reference) |

### Execution Style
How the command is structured or run.

| Tag | Description |
|-----|-------------|
| `oneliner` | Single-line command |
| `recursive` | Operates recursively |
| `requires-root` | Needs root/sudo |
| `unprivileged` | Runs without elevated privileges |
| `repl` | Uses interactive REPL |
| `do-shell-script` | AppleScript shell execution |

### Domain / Target
What system area the use case targets.

| Tag | Description |
|-----|-------------|
| `network` | Network operations |
| `disk` | Disk/volume operations |
| `files` | File system operations |
| `users` | User account operations |
| `groups` | Group operations |
| `processes` | Process management |
| `configuration` | System/app configuration |
| `monitoring` | Monitoring/observability |
| `backup` | Backup operations |
| `logging` | Log access or manipulation |
| `kernel` | Kernel-level operations |
| `permissions` | Permission management |
| `startup` | Startup/login items |
| `system-info` | System information gathering |

### Protocol
Network protocol involved.

| Tag | Description |
|-----|-------------|
| `tftp` | TFTP protocol |
| `smb` | SMB/CIFS protocol |
| `ssh` | SSH protocol |
| `ldap` | LDAP protocol |
| `dns` | DNS protocol |
| `snmp` | SNMP protocol |
| `eppc` | Remote Apple Events protocol |

### Technique
Adversary technique or method described.

| Tag | Description |
|-----|-------------|
| `file-transfer` | Transferring files |
| `proxy` | Traffic proxying |
| `covert-channel` | Hidden communication channel |
| `covert-storage` | Hidden data storage |
| `c2` | Command and control |
| `reconnaissance` | Information gathering |
| `enumeration` | System/resource enumeration |
| `evasion` | Detection evasion method |
| `surveillance` | Monitoring/surveillance |
| `privilege-escalation` | Elevating privileges |
| `lateral-movement` | Moving between systems |
| `payload-execution` | Executing a payload |
| `remote-execution` | Remote command execution |
| `remote-apple-events` | Uses Remote Apple Events |
| `remote-apple-services` | Uses Remote Apple Services |
| `exfiltration-timing` | Time-based data exfiltration |
| `software-deployment` | Software deployment abuse |
| `ipc` | Inter-process communication |
| `geolocation` | Location discovery |
| `cookie-theft` | Browser cookie theft |
| `vmcheck` | Virtual machine detection |

### macOS-Specific
macOS frameworks, features, or security mechanisms.

| Tag | Description |
|-----|-------------|
| `gatekeeper` | Gatekeeper interaction |
| `firewall` | macOS firewall |
| `quarantine` | Quarantine attribute |
| `xattr` | Extended attributes |
| `tccutil` | TCC database/permissions |
| `launchctl` | Launch daemon/agent management |
| `plist` | Property list files |
| `spotlight` | Spotlight search |
| `finder` | Finder operations |
| `finder-comment` | Finder comment metadata |
| `codesign` | Code signing |
| `system-events` | System Events scripting |
| `lockscreen` | Lock screen interaction |
| `system-reset` | System reset operations |

### Application
Specific application targeted.

| Tag | Description |
|-----|-------------|
| `chrome` | Google Chrome |
| `safari` | Safari browser |
| `selenium` | Selenium automation |
| `application` | Generic application interaction |

### Data
Type of data involved.

| Tag | Description |
|-----|-------------|
| `clipboard` | Clipboard data |
| `password` | Password/credential data |
| `certificate` | Certificate data |
| `base64` | Base64 encoding |
| `account` | Account information |
| `compress` | Data compression |
| `shares` | Network shares |
| `file-sharing` | File sharing services |
| `authentication` | Authentication data |
| `prompt` | User prompt/dialog |

### Malware Reference
Known malware that uses this technique (lowercase).

| Tag | Description |
|-----|-------------|
| `xcsset` | XCSSET malware family |
| `genieo` | Genieo adware |
| `shlayer` | Shlayer trojan |
| `cleanmaster` | CleanMaster PUP |

### Binary Reference
Cross-references to other macOS binaries used in the example.

| Tag | Description |
|-----|-------------|
| `osascript` | Uses osascript |
| `pbpaste` | Uses pbpaste |
| `launchctl` | Uses launchctl |
| `payload` | Involves payload creation/delivery |
| `dylib` | Dynamic library involvement |
| `sigkill` | SIGKILL signal |
