# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

## [0.9.0] - 2023-09-21

## Changed

- Updated README to better describe application and to add Usage information
- Updated CHANGELOG and incremented version

### Added

- Functionality to make application platform-agnostic

## [0.8.4] - 2023-09-13

### Fixed

- Corrected minor formatting discrepancies in CHANGELOG
- Log messages now instantiate at (somewhat) more appropriate times

## [0.8.3] - 2023-09-13

### Fixed

- Fixed all functions -- at this time, _all_ functions should be functioning correctly package-wide
- Renamed .env.txt to .env to ensure it gets sourced correctly (it wasn't previously)

### Added

- Implemented debug logging throughout package

### Deprecated

- main.py

## [0.8.2] - 2023-09-13

### Changed

- main.py changed to winfo.py

### Fixed

- (Hopefully) fixed import statments and .env variables to ensure we can run via main function

## [0.8.1] - 2023-09-13

### Fixed

- main now correctly sources emailer and getsysinfo

### Changed

- getsysinfo now sources .env

## [0.8.0] - 2023-09-13

### Changed

- emailer.py now sources a dotenv configuration file to obfuscate secrets
- Main function should now run entire application without need for further input

## [0.7.0] - 2023-09-13

### Added

- main.py is now the main function

### Changed

- Restructed filesystem; this may need to be changed later
- emailer and getsysinfo are now imported as modules into main.py

## [0.6.0] - 2023-09-13

### Added

- Functionality to send entire text of WINFORMATION.txt as body of email (can not yet attach to email)
- Various docstrings

## [0.5.1] - 2023-09-13

### Removed

- getinfo.py

## [0.5.0] -  2023-09-13

### Added

- Formatting functionality for WINFORMATION.txt (output)

### Changed

- Cleaned  up code in getsysinfo.py

### Added

- Various code comments so that I don't forget  what's going on here next time  I open this

## [0.4.1] - 2023-09-13

### Fixed

- Changed output destination for WINFORMATION.txt output

### Changed

- Renamed getinfo.py function to getsysinfo.py

## [0.4.0] - 2023-09-13

### Added

- Created src/getinfo.py function to pull system info and write to an output file

## [0.3.0] - 2023-09-13

### Added

- Information gathering functionality (src/getinfo.py)
- requirements.txt file (placeholder; contains no data)

## [0.2.1] - 2023-09-13

### Fixed

- Updated .gitignore

## [0.2.0] - 2023-09-13

### Added

- src/emailer.py
- Basic functionality for sending an email via Google SMTP

## [0.1.0] - 2023-09-13

### Created Repository
