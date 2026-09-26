import csv
import json
from decimal import Decimal
from pathlib import Path

input_file = Path("/data/sales.csv")
total = Decimal("0.00")
item_count = 0

with input_file.open(newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        quantity = int(row["quantity"])
        unit_price = Decimal(row["unit_price"])
        total += quantity * unit_price
        item_count += quantity

result = {
    "status": "completed",
    "file": input_file.name,
    "total_items": item_count,
    "total_value": str(total),
}

print("CSV processing completed successfully", flush=True)
print(json.dumps(result, indent=2), flush=True)