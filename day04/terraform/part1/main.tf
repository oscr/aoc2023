variable "filename" {}

locals {
  lines = split("\n", file("${path.module}/${var.filename}"))

  winning = [for line in local.lines :
    length(setintersection(compact(split(" ", trimspace(split("|", split(":", line)[1])[0]))), compact(split(" ", trimspace(split("|", split(":", line)[1])[1])))))
  ]
  result = sum([for i in local.winning : i == 0 ? 0 : pow(2, i - 1)])
}

output "result" {
  value = local.result
}