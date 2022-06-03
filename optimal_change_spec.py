# Write your tests here!
from optimal_change import optimal_change

print(optimal_change(62.13, 100) == 'The optimal change for an item that costs $62.13 with an $100 of is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, 2 pennies.')

print(optimal_change(31.51, 50) == 'The optimal change for an item that costs $31.51 with an $50 of is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, 4 pennies.')

print(optimal_change(60, 100) == 'The optimal change for an item that costs $60 with an $100 of is 2 $20 bills.')

print(optimal_change(49.99, 50) == 'The optimal change for an item that costs $49.99 with an $50 of is 1 penny.')

print(optimal_change(0.01, 10) == 'The optimal change for an item that costs $0.01 with an $10 of is 1 $5 bill, 4 $1 bills, 3 quarters, 2 dimes, 4 pennies.')