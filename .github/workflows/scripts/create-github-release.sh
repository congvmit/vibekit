#!/usr/bin/env bash
set -euo pipefail

# create-github-release.sh
# Create a GitHub release with all template zip files
# Usage: create-github-release.sh <version>

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <version>" >&2
  exit 1
fi

VERSION="$1"

# Remove 'v' prefix from version for release title
VERSION_NO_V=${VERSION#v}

gh release create "$VERSION" \
  .genreleases/vibekit-template-copilot-sh-"$VERSION".zip \
  .genreleases/vibekit-template-copilot-ps-"$VERSION".zip \
  .genreleases/vibekit-template-claude-sh-"$VERSION".zip \
  .genreleases/vibekit-template-claude-ps-"$VERSION".zip \
  .genreleases/vibekit-template-gemini-sh-"$VERSION".zip \
  .genreleases/vibekit-template-gemini-ps-"$VERSION".zip \
  .genreleases/vibekit-template-cursor-agent-sh-"$VERSION".zip \
  .genreleases/vibekit-template-cursor-agent-ps-"$VERSION".zip \
  .genreleases/vibekit-template-opencode-sh-"$VERSION".zip \
  .genreleases/vibekit-template-opencode-ps-"$VERSION".zip \
  .genreleases/vibekit-template-qwen-sh-"$VERSION".zip \
  .genreleases/vibekit-template-qwen-ps-"$VERSION".zip \
  .genreleases/vibekit-template-windsurf-sh-"$VERSION".zip \
  .genreleases/vibekit-template-windsurf-ps-"$VERSION".zip \
  .genreleases/vibekit-template-codex-sh-"$VERSION".zip \
  .genreleases/vibekit-template-codex-ps-"$VERSION".zip \
  .genreleases/vibekit-template-kilocode-sh-"$VERSION".zip \
  .genreleases/vibekit-template-kilocode-ps-"$VERSION".zip \
  .genreleases/vibekit-template-auggie-sh-"$VERSION".zip \
  .genreleases/vibekit-template-auggie-ps-"$VERSION".zip \
  .genreleases/vibekit-template-roo-sh-"$VERSION".zip \
  .genreleases/vibekit-template-roo-ps-"$VERSION".zip \
  .genreleases/vibekit-template-codebuddy-sh-"$VERSION".zip \
  .genreleases/vibekit-template-codebuddy-ps-"$VERSION".zip \
  .genreleases/vibekit-template-qoder-sh-"$VERSION".zip \
  .genreleases/vibekit-template-qoder-ps-"$VERSION".zip \
  .genreleases/vibekit-template-amp-sh-"$VERSION".zip \
  .genreleases/vibekit-template-amp-ps-"$VERSION".zip \
  .genreleases/vibekit-template-shai-sh-"$VERSION".zip \
  .genreleases/vibekit-template-shai-ps-"$VERSION".zip \
  .genreleases/vibekit-template-q-sh-"$VERSION".zip \
  .genreleases/vibekit-template-q-ps-"$VERSION".zip \
  .genreleases/vibekit-template-bob-sh-"$VERSION".zip \
  .genreleases/vibekit-template-bob-ps-"$VERSION".zip \
  --title "Vibekit Templates - $VERSION_NO_V" \
  --notes-file release_notes.md
