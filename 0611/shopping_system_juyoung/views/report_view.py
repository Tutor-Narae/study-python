def print_total_per_customer(totals):
  print("🧾 고객별 총 주문 금액:")
  for name, total in totals.items():
    print(f" - {name}: ${total:.1f}")

def print_product_quantities(quantities):
    print("📦 제품별 총 판매량:")
    for product, quantity in quantities.items():
        print(f" - {product}: {quantity}개")

def print_product_revenues(revenues):
    print("💰 제품별 총 수익 (내림차순):")
    for product, revenue in revenues.items():
        print(f" - {product}: ${revenue:.1f}")