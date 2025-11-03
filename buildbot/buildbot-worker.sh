#!/usr/bin/env bash
set -euxo pipefail

# Install dependencies
python3 -m pip install -r requirements.txt

# Create and start worker
buildbot-worker create-worker worker localhost macos-worker password
buildbot-worker start worker
