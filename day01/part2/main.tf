variable "filename" {
  default = "input.txt"
}

locals {
  toDigit = tomap({
    one       = "1"
    two       = "2"
    three     = "3"
    four      = "4"
    five      = "5"
    six       = "6"
    seven     = "7"
    eight     = "8"
    nine      = "9"
    oneight   = "18",
    twone     = "21",
    threeight = "38",
    fiveight  = "58",
    eightwo   = "82",
    eighthree = "83",
    nineight  = "98"
  })

  lines = split("\n", file("${path.module}/${var.filename}"))

  # Due to limited regex capabilities in Terraform we can't use positive lookahead. Otherwise the following would have
  # provided a better solution than the current hack: (?=(\d|one|two|three|four|five|six|seven|eight|nine))
  digitsAndWords    = [for line in local.lines : regexall("\\d|oneight|twone|threeight|fiveight|eightwo|eighthree|nineight|one|two|three|four|five|six|seven|eight|nine", line)]
  digits            = [for line in local.digitsAndWords : flatten([for item in line : try(split("", lookup(local.toDigit, item, item)), lookup(local.toDigit, item, item))])]
  calibrationValues = [for line in local.digits : try(tonumber(format("%s%s", element(line, 0), element(line, length(line) - 1))), 0)]
  result            = sum(local.calibrationValues)
}

output "result" {
  value = local.result
}