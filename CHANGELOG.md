# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.9] - 2024-03-15

### Fixed
- Fixed critical bug where tracker-specific endpoints were using incorrect URL format
  - Changed from `https://trackerstatus.info/api/btn/all` to `https://btn.trackerstatus.info/api/all`
  - Updated all tracker endpoints to use subdomain-based URLs
  - Fixed URL construction in APIClient and BaseTrackerEndpoint
- Fixed black formatting in status.py

## [1.0.8] - 2024-03-15

### Fixed
- Fixed critical bug where tracker-specific endpoints were using incorrect URL format
  - Changed from `https://trackerstatus.info/api/btn/all` to `https://btn.trackerstatus.info/api/all`
  - Updated all tracker endpoints to use subdomain-based URLs
  - Fixed URL construction in APIClient and BaseTrackerEndpoint
- Fixed black formatting in status.py
- Updated black dependency to 24.3.0+ to address ReDoS vulnerability
- Fixed Codecov action configuration in CI workflow
- Bumped pytest to 8.3.5, pytest-cov to 6.0.0, and requests-mock to 1.12.1.
- Updated black to 25.1.0, isort to 6.0.1, mypy to 1.15.0, pylint to 3.3.5, pre-commit to 4.1.0, and types-requests to 2.28.11.

## [1.0.7] - 2024-03-15

### Fixed
- Updated black to 24.3.0+ to address ReDoS vulnerability
- Fixed Codecov action configuration in CI workflow
- Bumped pytest to 8.3.5, pytest-cov to 6.0.0, and requests-mock to 1.12.1.
- Updated black to 25.1.0, isort to 6.0.1, mypy to 1.15.0, pylint to 3.3.5, pre-commit to 4.1.0, and types-requests to 2.28.11.

## [1.0.6] - 2024-03-15

### Added
- Support for Nebulance (NBL) and Anthelion (ANT) trackers
- Added subdomain-based URLs for tracker-specific endpoints

### Fixed
- Updated API documentation to reflect current implementation
- Fixed endpoint URL construction for tracker-specific endpoints
- Improved CI configuration with better pylint settings

## [1.0.5] - 2024-03-12

### Changed
- Simplified Quick Start example in README.md to focus on essential functionality
- Improved code readability in examples

## [1.0.4] - 2024-03-12

### Fixed
- Corrected remaining relative links in README.md (LICENSE and examples documentation)

## [1.0.3] - 2024-03-12

### Fixed
- Corrected relative link to examples documentation in README.md

## [1.0.2] - 2024-03-12

### Fixed
- Corrected case in API.md documentation links (was api.md)

## [1.0.1] - 2024-03-12

### Fixed
- Documentation links in README.md now use absolute URLs for PyPI compatibility

## [1.0.0] - 2024-03-12

### Added
- Initial release with support for all tracker endpoints
- Rate-limited API client (1 request per minute)
- Comprehensive test suite with shared fixtures and 100% coverage
- Type hints and detailed documentation
- Support for all tracker-specific endpoints:
  - AlphaRatio (AR)
  - BroadcastTheNet (BTN)
  - GazelleGames (GGN)
  - PassThePopcorn (PTP)
  - Redacted (RED)
  - Orpheus (OPS)
- Status interpretation helpers
- Base tracker endpoint class
- GitHub Actions CI/CD pipeline
- Pre-commit hooks for code quality
- Comprehensive API documentation in `docs/api.md`
- Tool configurations in `setup.cfg` for:
  - flake8 (linting)
  - mypy (type checking)
  - pytest (testing)
  - coverage (test coverage)
  - isort (import sorting)

### Changed
- Moved to modern Python packaging with `pyproject.toml`
- Updated documentation with comprehensive examples
- Standardized API response handling
- Improved error handling in `APIClient.get()` method
- Optimized test organization with shared fixtures
- Enhanced code organization and structure

### Fixed
- Proper TypeError handling in APIClient
- Test class collection warnings
- Mock response structure in tests

[1.0.0]: https://github.com/mauvehed/trackerstatus/releases/tag/v1.0.0
[1.0.6]: https://github.com/mauvehed/trackerstatus/releases/tag/v1.0.6
[1.0.7]: https://github.com/mauvehed/trackerstatus/releases/tag/v1.0.7
[1.0.8]: https://github.com/mauvehed/trackerstatus/releases/tag/v1.0.8
