# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.5.0] - 2019-10-08
### Added
- Setting to choose CSV file destination
- Link to CSV file destination in console upon creation
- Save Settings menu option with shortcut (Ctrl+S)
- Error check on Min and Max threshold settings. A warning will appear and the text will turn red when Min is more than
Max
- Open Log item to Help menu
- Log message on shutdown

### Changed
- User files are now created in AppData/Roaming (Windows) or Home (Linux) folders
- Moved static class methods to utils
- create_csv function no longer relies on error check for iteration completion
- console function now strips html tags for cleaner logging
- console function can now be used to amend plain text to the console

## [0.4.0] - 2019-09-02
### Added
- Link to website in about dialog
- Separator below information text
- Ui layouts
- date_format function
- Double click functionality to address book
- Version file for easier version tracking

### Changed
- Frontend now uses PySide2
- Rearranged input fields
- Ui now conforms upon window being resized
- Theme change message box notice text
- Theme change message box icon from notice to warning
- Moved about dialog to separate module
- Better theme checking in utils modules
- Dark theme now uses a customized QSS using [QDarkStyleSheet](https://github.com/ColinDuquesnoy/QDarkStyleSheet)
- Update cache now uses db extension
- Icon variable names in main script
- create_csv function uses new date_format function for cleaner code

### Removed
- Custom clear text button
- Icons8 link, app no longer uses custom clear text icon
- Redundant second QApplication instance from main script

### Fixed
- Window icons now use the proper size from ico files
- Running about dialog no longer opens multiple dialog windows

## [0.3.0] - 2019-08-12
### Added
- Themed Stellar window icons (default and dark modes)

### Changed
- Stellar window icon now has a background
- Switching theme now asks if the user would like the application to restart itself
- Improved appearance for dark theme context menus
- Update check now caches the API response for 1 hour

## [0.2.1] - 2019-08-06
### Fixed
- Address book spacing
- Stellar logo icon sizing

## [0.2.0] - 2019-08-05
### Added
- Address Book, allowing users to save addresses with optional nicknames to use in the main program
- Dark theme
- Update check
- Clear text button to address field
- Settings reset button

## [0.1.0] - 2019-07-29
### Added
- First beta release

[Unreleased]: https://github.com/usertxt/stellar-csv-creator/compare/v0.5.0...dev
[0.5.0]: https://github.com/usertxt/stellar-csv-creator/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/usertxt/stellar-csv-creator/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/usertxt/stellar-csv-creator/compare/v0.2.1...v0.3.0
[0.2.1]: https://github.com/usertxt/stellar-csv-creator/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/usertxt/stellar-csv-creator/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/usertxt/stellar-csv-creator/releases/tag/v0.1.0