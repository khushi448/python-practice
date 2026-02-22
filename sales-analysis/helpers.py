def calculate_total(quantity,price):
  """Calculate total for single item."""
  return quantity * price

def format_currency(amount):
  """Format no as currency"""
  return f"${amount :,.2f}"# 2 decimals ,.2f
