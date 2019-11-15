# Car park entry & exit system (igcse)

A car park has space for 100 cars and a barrier entrance and exit system. There is a display at the
entrance to show how many spaces are empty. Cars are issued a ticket with a unique number on entry
and the time of issue is stored. The car park charges $1.50 per hour and the fee is paid at a machine
before leaving the car park. At the machine, the ticket number and departure time are entered; the fee is
calculated by the machine and the amount due is paid by the ticket holder. Cars cannot stay overnight; the
system is reset at midnight.
Write and test a program or programs for the car park manager.
• Your program or programs must include appropriate prompts for the entry of data.
• Error messages and other output need to be set out clearly and understandably.
• All variables, constants and other identifiers must have meaningful names.
You will need to complete these three tasks. Each task must be fully tested.
TASK 1 – Operating the car park.
The system is reset at midnight every day.
Set up a system using arrays and with suitable prompts that will carry out the following as cars enter or
leave the car park:
On Entry:
• display the number of empty car park spaces
• issue the next available ticket number
• store the current time and the ticket number
• display the updated number of empty car park spaces.
On Exit:
• input a ticket number and departure time
• output the amount of time the car stayed at the car park
• delete the ticket number from the array
• display the updated number of empty car park spaces.
TASK 2 – Working out the cost and daily takings.
Amend the program so that it will calculate the amount to be paid using a charge of $1.50 per hour, or
part of an hour (i.e. any amount of time into the next hour is charged for a whole hour). The amount to be
paid is displayed and is added to a running total for the day, before the ticket number is deleted from the
array. At the end of the day, the following information is displayed:
• total daily takings
• number of cars that have used the car park
• average charge per car
• average length of stay per car.
TASK 3 – Introducing parking restrictions.
The car park manager decides to restrict the length of stay to a maximum of eight hours, and will charge
an extra $100 if a car overstays. Modify your program to implement this change and ensure the driver is
aware of this extra charge. Output the number of cars that have overstayed in a day.

Summer, 2018
