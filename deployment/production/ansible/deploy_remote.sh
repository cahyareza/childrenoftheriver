#!/usr/bin/env bash
echo "=== Deploying project to production server ==="
date

cd "$(dirname "$0")"
ansible-playbook deploy.yml --start-at-task='Django migrate' -i hosts/remote