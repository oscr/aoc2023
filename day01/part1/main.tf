variable "filename" {
  default = "input.txt"
}

locals {
  lines             = split("\n", file("${path.module}/${var.filename}"))
  digits            = [for line in local.lines : regexall("\\d", line)]
  calibrationValues = [for line in local.digits : try(tonumber(format("%s%s", element(line, 0), element(line, length(line) - 1))), 0)]
  sum               = sum(local.calibrationValues)
}

output "result" {
  value = local.sum
}