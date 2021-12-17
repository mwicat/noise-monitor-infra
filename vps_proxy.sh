#!/bin/bash

set -Eeuo pipefail

ssh -L 127.0.0.1:8086:127.0.0.1:8086 -L 127.0.0.1:3000:127.0.0.1:3000 -Nf vps
