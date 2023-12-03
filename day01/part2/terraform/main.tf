variable "filename" {
  default = "../input.txt"
}

locals {
  wordToNumber = tomap({
    zero  = "0"
    one   = "1"
    two   = "2"
    three = "3"
    four  = "4"
    five  = "5"
    six   = "6"
    seven = "7"
    eight = "8"
    nine  = "9"
  })
  wordsRegex = "one|two|three|four|five|six|seven|eight|nine"

  lines = split("\n", file("${path.module}/${var.filename}"))

  # Due to the limited regex in Terraform we're forced to use this hack instead overlapping matches.
  digitsAndWords    = [for line in local.lines : [regexall(format("\\d|%s", local.wordsRegex), line)[0], strrev(regexall(format("\\d|%s", strrev(local.wordsRegex)), strrev(line))[0])]]
  digits            = [for line in local.digitsAndWords : [lookup(local.wordToNumber, line[0], line[0]), lookup(local.wordToNumber, line[1], line[1])]]
  calibrationValues = [for line in local.digits : tonumber(format("%s%s", element(line, 0), element(line, length(line) - 1)))]
  result            = sum(local.calibrationValues)
}

output "result" {
  value = local.result
}