#!/usr/bin/env bash

pre-commit install --hook-type commit-msg
git config commit.template .gitmessage