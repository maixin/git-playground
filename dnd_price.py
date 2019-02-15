from typing import Dict
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum

class User(Enum):
  AMAN = 'Aman'
  ADI = 'Adi'
  JESS = 'Jess'
  DONG = 'Dong'
  ESTELLE = 'Estelle'

number_of_people = len(User)
normal_shipping_cost = Decimal('22')
fast_shipping_cost = Decimal('33.50')

total_due_by_user: Dict[User, Decimal] = {
  # 1x Mermaid Class Dice
  User.ADI: Decimal('11.95') + (normal_shipping_cost / number_of_people),
  # 1x Mermaid Class Dice
  User.DONG: Decimal('11.95') + (normal_shipping_cost / number_of_people),
  # Purple and orange vapor dice
  User.JESS: Decimal('9.95') + (normal_shipping_cost / number_of_people),
  # Black chrome metal dice with teal numbers
  User.ESTELLE: Decimal('34.95') + (normal_shipping_cost / number_of_people),
  # Black chrome metal dice with purple numbers
  User.AMAN: (
    Decimal('34.95') + (normal_shipping_cost / number_of_people)
    + (fast_shipping_cost - normal_shipping_cost)
  ),
}

total_due = sum(total_due_by_user.values())


exchange_rate = Decimal('194.35') / Decimal(total_due)
exchange_rate = exchange_rate.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

for user, total_due_by_user in total_due_by_user.items():
  final_amount = (total_due_by_user * exchange_rate).quantize(
    Decimal('0.01'),
    rounding=ROUND_HALF_UP,  
    )
  print(user.value, ' = ', final_amount)