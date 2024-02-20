"""
    Nysa Clark
    Module 05 Lab Assignment

    This program ...
"""

# inventory system

# define a ITEM class
    # name
    # quantity
    # price 
# ---------------------------------------------
    # get name
    # get qyt
    # get price
    # set price w/ new price
        # make sure the price never goes below 1 cent
        # and doesn't change by more than 50%
# other values can't be changed once set in constructor
# 2 methods should make adjustments to the quantity
    # adding stock
        # should increase qty by value that is passed in
    # removing stock
        # should decrease qty (never below 0)
    # clearance w/ amount
        # allows the price to be reduced (but not increased)
        # by any amount
        # as long as the price doesn't go below 1 cent


# 2 subclasses

# Perishable items (eg. milk or bread)
    # general item attributes
    # needs to be refrigerated?
    # expiration date (may be stored as a string)
# --------------------------------------------------
    # get refrigerated
    # set refrigerated
    # get expiration date
    # set expiration date
    # clearence
        # method that reduces the price by 90%


# Electronic items
    # general item attributes
    # warrenty period (in num of days)
    # return period (in days)
    # serial number (set in contructor)
# -------------------------------------------------------
    # get warrenty
    # get return period
    # set return period
    # get serial number
    # extend warrenty
        # method for when the customer pruchases an extended
        # warrenty of 180 additional days