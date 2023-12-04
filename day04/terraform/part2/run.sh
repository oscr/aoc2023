#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

rm *.json terraform.tfstate terraform.tfstate.backup || true
until [[ $(terraform output done) == "true" ]]
do
  terraform apply --auto-approve -var filename=../../input.txt
done

echo -n "part2: "
terraform output result
test $(terraform output result) -eq "5833065" && echo "PASS: input" || echo "FAIL: input"