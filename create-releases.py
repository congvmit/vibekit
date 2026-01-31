#!/usr/bin/env python3
"""
Create release packages for Vibekit CLI templates.
This script generates ZIP files for all supported AI agents and script types.
"""

import os
import zipfile
import shutil
from pathlib import Path

# Configuration
VERSION = 'v0.0.22'

# Agent configurations matching the CLI
AGENT_CONFIGS = {
    'claude': {'folder': '.claude/commands', 'ext': 'md', 'args': '$ARGUMENTS'},
    'gemini': {'folder': '.gemini/commands', 'ext': 'toml', 'args': '{{args}}'},
    'copilot': {'folder': '.github/agents', 'ext': 'agent.md', 'args': '$ARGUMENTS'},
    'cursor-agent': {'folder': '.cursor/commands', 'ext': 'md', 'args': '$ARGUMENTS'},
    'qwen': {'folder': '.qwen/commands', 'ext': 'toml', 'args': '{{args}}'},
    'opencode': {'folder': '.opencode/command', 'ext': 'md', 'args': '$ARGUMENTS'},
    'windsurf': {'folder': '.windsurf/workflows', 'ext': 'md', 'args': '$ARGUMENTS'},
    'codex': {'folder': '.codex/prompts', 'ext': 'md', 'args': '$ARGUMENTS'},
    'kilocode': {'folder': '.kilocode/workflows', 'ext': 'md', 'args': '$ARGUMENTS'},
    'auggie': {'folder': '.augment/commands', 'ext': 'md', 'args': '$ARGUMENTS'},
    'roo': {'folder': '.roo/commands', 'ext': 'md', 'args': '$ARGUMENTS'},
    'codebuddy': {'folder': '.codebuddy/commands', 'ext': 'md', 'args': '$ARGUMENTS'},
    'qoder': {'folder': '.qoder/commands', 'ext': 'md', 'args': '$ARGUMENTS'},
    'amp': {'folder': '.agents/commands', 'ext': 'md', 'args': '$ARGUMENTS'},
    'shai': {'folder': '.shai/commands', 'ext': 'md', 'args': '$ARGUMENTS'},
    'q': {'folder': '.amazonq/prompts', 'ext': 'md', 'args': '$ARGUMENTS'},
    'bob': {'folder': '.bob/commands', 'ext': 'md', 'args': '$ARGUMENTS'},
}

SCRIPTS = ['sh', 'ps']

def rewrite_paths(text):
    """Rewrite paths to use .specify prefix"""
    return (text.replace('/memory/', '.specify/memory/')
                .replace('/scripts/', '.specify/scripts/')
                .replace('/templates/', '.specify/templates/'))

def extract_frontmatter_value(content, key):
    """Extract a value from YAML frontmatter"""
    lines = content.split('\n')
    in_frontmatter = False
    for line in lines:
        line = line.strip()
        if line == '---':
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter and line.startswith(f'{key}:'):
            return line.split(':', 1)[1].strip().strip('"').strip("'")
    return ''

def extract_script_command(content, script_type):
    """Extract script command for the given script type"""
    lines = content.split('\n')
    in_scripts = False
    for line in lines:
        line = line.strip()
        if line == 'scripts:':
            in_scripts = True
            continue
        if in_scripts and line.startswith(f'{script_type}:'):
            return line.split(':', 1)[1].strip()
        if in_scripts and line and not line.startswith(' ') and not line.startswith('\t'):
            break
    return ''

def generate_commands(agent, script_type, output_dir):
    """Generate command files for an agent and script type"""
    os.makedirs(output_dir, exist_ok=True)

    config = AGENT_CONFIGS[agent]
    ext = config['ext']
    arg_format = config['args']

    commands_dir = Path('templates/commands')
    for template_file in commands_dir.glob('*.md'):
        with open(template_file, 'r', encoding='utf-8') as f:
            content = f.read()

        name = template_file.stem

        # Extract metadata
        description = extract_frontmatter_value(content, 'description') or f'{name} command'
        script_command = extract_script_command(content, script_type)
        if not script_command:
            script_command = f'echo "Command {name} executed"'

        # Replace placeholders
        body = content
        body = body.replace('{SCRIPT}', script_command)
        body = body.replace('{ARGS}', arg_format)
        body = body.replace('__AGENT__', agent)
        body = rewrite_paths(body)

        # Remove scripts section from frontmatter
        lines = body.split('\n')
        filtered_lines = []
        in_scripts_section = False
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.strip() == 'scripts:':
                in_scripts_section = True
                i += 1
                continue
            if in_scripts_section:
                if line.strip() and not line.startswith(' ') and not line.startswith('\t'):
                    in_scripts_section = False
                else:
                    i += 1
                    continue
            filtered_lines.append(line)
            i += 1

        body = '\n'.join(filtered_lines)

        # Write file
        if ext == 'toml':
            output = f'description = "{description}"\n\nprompt = """\n{body}\n"""'
        else:
            output = body

        output_file = os.path.join(output_dir, f'speckit.{name}.{ext}')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output)

def create_package(agent, script_type):
    """Create a release package for an agent and script type"""
    print(f'Building {agent} ({script_type}) package...')

    base_dir = f'.genreleases/sdd-{agent}-package-{script_type}'
    os.makedirs(base_dir, exist_ok=True)

    # Copy base structure
    specify_dir = os.path.join(base_dir, '.specify')
    os.makedirs(specify_dir, exist_ok=True)

    # Memory
    if os.path.exists('memory'):
        shutil.copytree('memory', os.path.join(specify_dir, 'memory'), dirs_exist_ok=True)
        print('  Copied memory -> .specify')

    # Scripts
    scripts_dir = os.path.join(specify_dir, 'scripts')
    os.makedirs(scripts_dir, exist_ok=True)
    script_src = f'scripts/{script_type}' if script_type == 'sh' else 'scripts/powershell'
    if os.path.exists(script_src):
        shutil.copytree(script_src, os.path.join(scripts_dir, script_type), dirs_exist_ok=True)
        print(f'  Copied scripts/{script_type} -> .specify/scripts')

    # Templates (excluding commands and project-templates)
    templates_dir = os.path.join(specify_dir, 'templates')
    os.makedirs(templates_dir, exist_ok=True)
    if os.path.exists('templates'):
        for item in os.listdir('templates'):
            if item not in ['commands', 'project-templates', 'vscode-settings.json']:
                src = os.path.join('templates', item)
                dst = os.path.join(templates_dir, item)
                if os.path.isfile(src):
                    shutil.copy2(src, dst)
        print('  Copied templates -> .specify/templates')

    # Agent-specific structure
    config = AGENT_CONFIGS[agent]
    agent_dir = os.path.join(base_dir, config['folder'])
    generate_commands(agent, script_type, agent_dir)

    # Special cases
    if agent == 'copilot':
        # Create companion prompt files
        prompts_dir = os.path.join(base_dir, '.github', 'prompts')
        os.makedirs(prompts_dir, exist_ok=True)

        # Copy VS Code settings
        vscode_dir = os.path.join(base_dir, '.vscode')
        os.makedirs(vscode_dir, exist_ok=True)
        if os.path.exists('templates/vscode-settings.json'):
            shutil.copy2('templates/vscode-settings.json', os.path.join(vscode_dir, 'settings.json'))

    # Create ZIP
    zip_name = f'spec-kit-template-{agent}-{script_type}-{VERSION}.zip'
    zip_path = os.path.join('.genreleases', zip_name)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, base_dir)
                zipf.write(file_path, arcname)

    print(f'  Created {zip_path}')

    # Clean up
    shutil.rmtree(base_dir)

def main():
    """Main function"""
    print(f'Building release packages for {VERSION}')
    os.makedirs('.genreleases', exist_ok=True)

    agents = list(AGENT_CONFIGS.keys())

    for agent in agents:
        for script in SCRIPTS:
            try:
                create_package(agent, script)
            except Exception as e:
                print(f'Error creating package for {agent}-{script}: {e}')
                return 1

    # List created packages
    print('\nArchives created:')
    for zip_file in sorted(os.listdir('.genreleases')):
        if zip_file.endswith('.zip'):
            print(f'  .genreleases/{zip_file}')

    print('\nRelease packages created successfully!')
    return 0

if __name__ == '__main__':
    exit(main())