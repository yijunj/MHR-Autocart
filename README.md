# Autocart-MHR
Automatic and repeated carting machine for Monster Hunter Rise talisman farming

## Background
Talisman is a key equipment in Monster Hunter Rise, with the capability of providing highly rated skills and slots. However, obtaining good (or even god) talismans requires effort and in-game resources, as they are generated from a random melding pot known as the Wisp of Mystery. A good description of the talisman mechanism can be found [here](https://game8.co/games/Monster-Hunter-Rise/archives/327175).

The problem is, each melding requires finishing a (non-expedition) quest to complete. It has been long discovered that the most efficient quest to take is the arena Rajang, and keep carting 10 times will complete 10 (the max number) melding batches in a "short" amount of time (about 15 minutes manually). However, talismans with the skill Weakness Exploit 2 and a 2-star slot, and potentially with the skill Critical Boost 2, are extremely rare, so even repeating the Rajang quest is time consuming. To address this problem, this repo presents an Arduino Switch controller that automatically accepts the Rajang quest and carts.

Also, to address the resource problem, thanks to [Ken_set](https://www.gamersky.com/handbook/202104/1384837.shtml), in 2.0 version of the game it is possible to save and reload the game to update the talisman results, without actually consuming (most of) the materials required for melding. The procedure is (please turn off auto-save in the game):

1. Save the game
2. Make 10 melding batches (5 in each batch), do NOT save
3. Cart in Rajang quest 10 times, do NOT save in the end
4. Check the 50 talismans, if no good talisman comes out, do NOT save, then close the game
5. Restart the game, make 1 melding (only 1 in this batch). The 150 pts worth of materials is what you WILL pay in this iteration
6. Cart in Rajang quest once, then take the single talisman and SAVE
7. If not a good talisman, go to step 1 and repeat

Step 6 will refresh the talisman table so you end up with different talismans in each iteration. This procedure allows you to use 150 pts worth of materials to check 51 talismans, reducing the material cost by 51x.

## Arduino controller
Please refer to [HackerLoop's repo](https://github.com/HackerLoop/Arduino-JoyCon-Library-for-Nintendo-Switch) to learn how to turn an Arduino Leonardo into a Switch joycon. In short, the Arduino, when connected to a Switch via USB, can trigger joycon events. One can either store a button sequence in the Arduino itself, or send commands to the Arduino from a PC via serial port. Here I use the latter: my PC sends a string to the Arduino consisting of several 6-char commands, the Arduino translates the commands into joycon events. I don't need feedback from the Switch.
