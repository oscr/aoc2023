variable "filename" {
  default = "../input.txt"
}

locals {
  limits = tomap({
    red  = 12
    green = 13
    blue = 14
  })

  lines = split("\n", file("${path.module}/${var.filename}"))

  result = sum([ for line in local.lines:
    tonumber(reverse(sort(formatlist("%05d", flatten(regexall("(\\d+) red", line)))))[0]) <= 12 &&
    tonumber(reverse(sort(formatlist("%05d", flatten(regexall("(\\d+) green", line)))))[0]) <= 13 &&
    tonumber(reverse(sort(formatlist("%05d", flatten(regexall("(\\d+) blue", line)))))[0]) <= 14 ?
    tonumber(regex("Game (\\d+)", line)[0]) : 0
    ])
}

output "result" {
  value = local.result
}