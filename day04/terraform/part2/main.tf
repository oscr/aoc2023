variable "filename" {
  type = string
}

locals {
  # Files to keep state
  state_row_file = "${path.module}/row.json"
  state_cards_file = "${path.module}/cards.json"

  # Read the cards data
  lines = split("\n", file("${path.module}/${var.filename}"))

  # Try to read the state or init it to start values.
  row = try(jsondecode(file(local.state_row_file)), 0)
  cards = try(jsondecode(file(local.state_cards_file)), [for i in range(0, length(local.lines)): 1 ])

  # Calculate changes
  matching_numbers = length(setintersection(compact(split(" ", trimspace(split("|", split(":", element(local.lines, local.row))[1])[0]))),
                                            compact(split(" ", trimspace(split("|", split(":", element(local.lines, local.row))[1])[1])))))
  cards_updated = [for i, card in local.cards : i > local.row && i <= local.row+local.matching_numbers ? card + local.cards[local.row] : card]
  result = sum(local.cards_updated)

  # Figure out what to do next
  done = local.row+1 == length(local.lines)
  row_next = local.done ? local.row : local.row + 1
}

resource "local_file" "row" {
  content = jsonencode(local.row_next)
  filename = local.state_row_file
}

resource "local_file" "cards" {
  content  = jsonencode(local.cards_updated)
  filename = local.state_cards_file
}

output "done" {
  value = local.done
}

output "result" {
  value = local.result
}