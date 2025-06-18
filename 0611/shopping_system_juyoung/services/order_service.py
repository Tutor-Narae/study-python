import csv
from models.order import Order
from pathlib import Path

def read_orders():
  orders = []
  file_path = Path(__file__).resolve().parent.parent/'data'/'orders.csv'
  print(file_path)

  with open(file_path, newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
      clean_row = {k.strip(): v for k, v in row.items()}
      print(clean_row)
      
      order = Order(order_id = clean_row['order_id'],
        customer = clean_row['customer_name'],
        product = clean_row['product'],
        quantity = clean_row['quantity'],
        price = clean_row['price']
      )
      orders.append(order)

  return orders

def calculate_customer_totals(orders):
  totals = {}
  for order in orders:
    if order.customer_name in totals:
      totals[order.customer_name] += order.total_price()
    else:
      totals[order.customer_name] = order.total_price()

  return totals

def calculate_product_quantities(orders):
  quantities = {}
  for order in orders:
    if order.product in quantities:
      quantities[order.product] += order.quantity
    else:
      quantities[order.product] = order.quantity
  return quantities

def get_revenue(item):
  return item[1]

def calculate_product_revenue(orders):
  revenue = {}
  for order in orders:
    if order.product in revenue:
      revenue[order.product] += order.total_price
    else:
      revenue[order.product] = order.total_price

    sorted_revenue = dict(sorted(revenue.items(), key = get_revenue, reverse = True))
    return sorted_revenue