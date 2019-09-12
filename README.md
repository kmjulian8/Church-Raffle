# Church-Raffle
One sunday afternoon, my mom came home from church with two raffle tickets in her hand. She told me she had entered into the "Queen of Hearts Raffle", a 50-50 split raffle game that had been going on for the past 48 weeks. After hearing the rather convoluted way the game works, I decided it'd be fun to model it in python, and run a simulation to see what her odds are (I also wrote a function to calculate the theoretical probability of winning).  

Here's how it works:  

It starts with two boxes, one with 52 cards in it, and one with all the entries.  

Each entry consists of a name and their choice of of card (1-52).

Every week, one card is pulled out the card box, and one entry is pulled out of the entry box. 

If the card choice on the entry matches the card that was pulled, that person is a winner!  

If it is not a match, the chosen card, and all of the entries, are thrown away. 

The next week, people submitting entries choose from the remaining 51 cards and the process repeats itself.  

This process continues until a match is found (which at worst has to happen on the final week).
