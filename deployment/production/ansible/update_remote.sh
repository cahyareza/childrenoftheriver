#!/usr/bin/env bash
echo "=== Updating project to production server ==="
date

cd "$(dirname "$0")"
ansible-playbook update.yml -i hosts/remote