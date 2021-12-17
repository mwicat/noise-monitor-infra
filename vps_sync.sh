#!/bin/bash

set -Eeuo pipefail

rsync --delete -Cuavz ./ vps:piezo-server/
