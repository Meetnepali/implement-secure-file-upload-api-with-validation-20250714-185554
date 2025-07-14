#!/usr/bin/env bash
set -e

# System dependencies
apt-get update -y
apt-get install -y python3 python3-pip python3-venv

# Python virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
