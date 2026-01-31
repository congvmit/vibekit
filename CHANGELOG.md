# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to the Vibekit CLI and templates are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2025-01-31

### Added

- Initial release of Vibekit CLI
- Complete rebranding from spec-kit to vibekit
- Support for 17 AI agents: Claude, Gemini, Copilot, Cursor, Qwen, opencode, Windsurf, Codex, Kilocode, Auggie, Roo, CodeBuddy, Amp, SHAI, Amazon Q, IBM Bob, Qoder
- Each agent available in bash (sh) and PowerShell (ps) variants
- Commands: `/vibekit.specify`, `/vibekit.plan`, `/vibekit.tasks`, `/vibekit.checklist`, `/vibekit.implement`, `/vibekit.analyze`, `/vibekit.clarify`, `/vibekit.constitution`, `/vibekit.taskstoissues`
- Dynamic template generation via release script
- `.vibekit/` directory structure for project configuration
- Environment variable `VIBEKIT_FEATURE` for feature branch tracking
