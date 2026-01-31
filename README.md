# Vibekit

Vibekit is a CLI tool for Spec-Driven Development (SDD), enabling teams to build software through structured specifications and AI-assisted workflows.

## Features

- **Spec-Driven Development**: Create clear specifications before implementation
- **AI Agent Integration**: Supports Claude Code, GitHub Copilot, Gemini CLI, and more
- **Template-Based Initialization**: Quick project setup with agent-specific command files
- **Cross-Platform**: Works on Linux, macOS, and Windows with both Bash and PowerShell scripts
- **Local Fallback**: Reliable operation even without internet connectivity

## Quick Start

### Initialize a New Project

```bash
# Install and initialize a new project
uvx --from git+https://github.com/congvmit/vibekit.git vibekit init my-project

# Or initialize in current directory
uvx --from git+https://github.com/congvmit/vibekit.git vibekit init .
```

### Choose Your AI Agent

```bash
# Initialize with specific AI agent
uvx --from git+https://github.com/congvmit/vibekit.git vibekit init my-project --ai claude
uvx --from git+https://github.com/congvmit/vibekit.git vibekit init my-project --ai copilot
```

## Supported AI Agents

- **Claude Code** (`claude`)
- **GitHub Copilot** (`copilot`)
- **Gemini CLI** (`gemini`)
- **Cursor** (`cursor-agent`)
- **Qwen Code** (`qwen`)
- **CodeBuddy** (`codebuddy`)
- **And many more...**

## Development Workflow

1. **Constitution**: Define project principles with `/vibekit.constitution`
2. **Specification**: Create requirements with `/vibekit.specify`
3. **Planning**: Generate implementation plans with `/vibekit.plan`
4. **Tasks**: Break down into actionable items with `/vibekit.tasks`
5. **Implementation**: Execute the plan with `/vibekit.implement`

## Documentation

- [Installation Guide](docs/installation.md)
- [Quick Start](docs/quickstart.md)
- [Local Development](docs/local-development.md)

## Contributing

Contributions are welcome! Please see the contributing guidelines and ensure all tests pass.
