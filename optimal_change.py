# Write your solution here!
def optimal_change(item_cost, amount_paid):
    # listing the currencies by index for our array to reference
    list_of_currencies = {
        100:'$100',
        50:'$50',
        20:'$20',
        10:'$10',
        5:'$5',
        1:'$1',
        .25:'quarter',
        .1:'dime',
        .05:'knickel',
        .01:'penny'
    }
    # array of currency values to break down the change
    array_of_currency_value = [100,50,20,10,5,1,.25,.1,.05,.01]
    # end string result
    converted_change = []

    # keeping a tally for every currency for the change
    currency_tally = {}
    
    # resulting string
    end_string = []

    # the amount of change
    change_to_convert = amount_paid - item_cost
    # for the exact change of one penny
    if change_to_convert < .01:
        change_to_convert = round(change_to_convert, 2)
    # looping through the array of currencies to break down the change from largest to smallest currencies by chipping away at it as each currency goes through
    for currency in array_of_currency_value:
        while change_to_convert/currency >= 1:
            converted_change.append(list_of_currencies[currency])
            rounded_change_to_convert = round(change_to_convert, 2)
            change_to_convert = rounded_change_to_convert - currency

    # looping through to keep a tally count in the current_tally dictionary
    for currency in converted_change:
        if not currency in currency_tally:
            currency_tally[currency] = 1
        else:
            currency_tally[currency] += 1

    # structuring the sentence
    for key, value in currency_tally.items():
    
    # specificly pennies for the certain cases of only pennies or a penny
        if key == 'penny':
            end_string.append(f"{value} {'pennies' if value > 1 else key}")
    
    # testing for bills
        elif "$" in key and not key == 'penny':
            end_string.append(f"{value} {key} {'bills'if value > 1  else 'bill'}")

    # testing for cents
        else:
            end_string.append(f"{value} {key}{'s' if value > 1 else ''}")

    # putting it all together
    new_end_string = ", ".join(end_string)

    # to add the "and" if more than 1 currency
    if len(end_string) > 1:
        
        return f"The optimal change for an item that costs ${item_cost} with an ${amount_paid} of is {', '.join(end_string[:-1])} and {end_string[-1]}."
    else:
        return f"The optimal change for an item that costs ${item_cost} with an ${amount_paid} of is {new_end_string}."


