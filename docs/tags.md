# LOOBin Tag Taxonomy

Tags describe the technical characteristics of each use case. They complement the `tactics` field (which uses MITRE ATT&CK tactics) by capturing implementation details.

## Tag Conventions

- **Lowercase only** — no capitalized tags (malware names included: `xcsset`, not `XCSSET`)
- **Hyphens for multi-word tags** — use `file-transfer`, not `file_transfer`
- **Plural for categories** — `users`, `files`, `processes`, `groups`
- **No MITRE tactic names** — use the `tactics` field for those
- **No MITRE technique IDs** — `T1072` does not belong in tags
- **Avoid self-referencing** — don't tag a LOOBin with its own binary name (e.g., don't use `mdls` as a tag in `mdls.yml`). Cross-references to other binaries (e.g., `osascript` in `mdfind.yml`) are fine.
- **Documented tags only** — every tag must appear in a table below. `tests/test_tags.py` enforces this, so add a row here when introducing a new tag.
- **One spelling per concept** — reuse an existing tag (`clipboard`, `system-info`) instead of adding a synonym.

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
| `javascript` | Uses JavaScript (outside JXA) |
| `webassembly` | Uses WebAssembly |

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
| `apfs` | APFS volumes or containers |
| `snapshot` | Volume or Time Machine snapshots |
| `power-management` | Power, sleep, and wake settings |
| `sleep` | System sleep behavior |
| `keep-awake` | Preventing the system from sleeping |
| `schedule` | Scheduled system events |
| `assertions` | Power management assertions |
| `policy` | Account or password policies |
| `user-activity` | User activity or idle state |
| `user-interface` | User interface processes |
| `terminal` | Terminal application |
| `notifications` | Notification services |
| `active-directory` | Active Directory environments |

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
| `kerberos` | Kerberos authentication |
| `gssapi` | GSSAPI/Kerberos-authenticated binds |
| `wake-on-lan` | Wake-on-LAN / network wake |

### Technique
Adversary technique or method described.

| Tag | Description |
|-----|-------------|
| `file-transfer` | Transferring files |
| `proxy` | Traffic proxying |
| `covert-channel` | Hidden communication channel |
| `covert-storage` | Hidden data storage |
| `c2` | Command and control |
| `enumeration` | System/resource enumeration |
| `evasion` | Detection evasion method |
| `surveillance` | Monitoring/surveillance |
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
| `domain-enumeration` | Directory/domain enumeration |
| `kerberoasting` | Kerberoasting service accounts |
| `asrep-roasting` | AS-REP roasting accounts |
| `laps` | Reading LAPS passwords |
| `paged-results` | Paged LDAP queries for large result sets |
| `staging` | Staging data before exfiltration |
| `anti-forensics` | Destroying or hiding forensic evidence |
| `indicator-removal` | Removing indicators of activity |
| `cleanup` | Cleaning up artifacts |
| `delete` | Deleting data |
| `restore` | Restoring data from backup |
| `wiper` | Destructive data wiping |
| `inhibit-recovery` | Preventing system recovery |
| `disruption` | Disrupting services or processes |
| `edr` | Security/EDR tooling tampering or discovery |

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
| `filevault` | FileVault disk encryption |
| `passphrase` | Disk or volume passphrases |

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

### Vulnerability Reference
CVE identifiers (lowercase) for vulnerabilities the use case exploits.

| Tag | Description |
|-----|-------------|
| `cve-2023-42931` | CVE-2023-42931 (diskutil noowners privilege escalation) |

### Binary Option
Specific flags, verbs, or settings of the binary named in the use case.

| Tag | Description |
|-----|-------------|
| `noowners` | diskutil `noowners` mount option |
| `secureerase` | diskutil `secureErase` verb |
| `destroyfvkeyonstandby` | pmset `DestroyFVKeyOnStandby` setting |
| `wakeorpoweron` | pmset `wakeorpoweron` schedule type |
| `womp` | pmset `womp` (wake on magic packet) setting |

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
