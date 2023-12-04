#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

terraform apply --auto-approve -var filename=../../input_example.txt  &> /dev/null
echo -n "example: "
terraform output result
test $(terraform output result) -eq "13" && echo "PASS: example" || echo "FAIL: example"


terraform apply --auto-approve -var filename=../../input.txt  &> /dev/null
echo -n "part1: "
terraform output result
test $(terraform output result) -eq "20667" && echo "PASS: input" || echo "FAIL: input"
