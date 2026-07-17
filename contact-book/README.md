A better version of Approach 3

Instead of a string, use a collection of valid choices.

accepted_numbers = ["1", "2", "3", "4"]

if chosen_option not in accepted_numbers:

or even better,

accepted_numbers = {"1", "2", "3", "4"}

if chosen_option not in accepted_numbers:

A set ({}) is designed for membership testing.



