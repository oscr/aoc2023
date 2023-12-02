variable "filename" {
  default = "../input.txt"
}

locals {
  lines = split("\n", file("${path.module}/${var.filename}"))

  result = sum([ for line in local.lines:
    tonumber(reverse(sort(formatlist("%05d", flatten(regexall("(\\d+) red", line)))))[0])*
    tonumber(reverse(sort(formatlist("%05d", flatten(regexall("(\\d+) green", line)))))[0])*
    tonumber(reverse(sort(formatlist("%05d", flatten(regexall("(\\d+) blue", line)))))[0])
  ])
}

output "result" {
  value = local.result
}