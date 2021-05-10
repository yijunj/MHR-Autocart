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

## How to use
1. Do what is said in [HackerLoop's repo](https://github.com/HackerLoop/Arduino-JoyCon-Library-for-Nintendo-Switch) to modify the Arduino files, then write joycon.ino to an Arduino Leonardo.
2. Connect the Arduino to PC using a serial-to-USB adapter (USB to computer, RX/TX to the Arduino corresponding pins).
3. Use a Pro controller, open Monster Hunter Rise. Make sure auto-save is off and pressing "-" opens up the map but not the chat screen. Save the game.
4. Manually go to the Hub merchant and make 10 melding batches. Then turn off the Pro controller.
5. The Switch will start looking for a joycon. Connect the Arduino to Switch via a USB cable. Run register.py from PC command window. This will register the Arduino as a "USB controller".
6. Run autocart.py from PC command window. Your hunter will automatically cart 10 times. This takes 20 minutes.
7. Unplug the Arduino from Switch. The Switch will once again start looking for a joycon. Register your Pro controller to it.
8. Manually go to check your talisman. If not happy with the outcome, close the game and restart.
9. Manually make one melding and cart once, then save the game when you are back.
10. Save the game. Then go to step 4 and repeat from there.

## Appendix: serial command table
I use 6 chars for each command: the first 2 indicating which key is pressed or released, and the last 4 indicating the time delay (in ms) after this event. E.g. AA0050 means "press A and wait 50 ms".

| 2-char key code | Action |
| ---------- | ---------- |
| AA | Press A |
| aa | Release A |
| BB | Press B |
| bb | Release B |
| XX | Press X |
| xx | Release X |
| YY | Press Y |
| yy | Release Y |
| DU | Press Up |
| du | Release Up |
| DD | Press Down |
| dd | Release Down |
| DL | Press Left |
| dl | Release Left |
| DR | Press Right |
| dr | Release Right |
| RI | Press R |
| ri | Release R |
| ZR | Press ZR |
| zr | Release ZR |
| ZL | Press ZL |
| zl | Release ZL |
| PL | Press Plus |
| pl | Release Plus |
| MI | Press Minus |
| mi | Release Minus |
| HO | Press Home |
| ho | Release Home |
| CA | Press Capture |
| ca | Release Capture |
| RC | Press Right Stick |
| rc | Release Right Stick |
| LC | Press Left Stick |
| lc | Release Left Stick |
| RU | Push Right Stick Up |
| RD | Push Right Stick Down |
| RL | Push Right Stick Left |
| RR | Push Right Stick Right |
| RN | Return Right Stick Neutral |
| LU | Push Left Stick Up |
| LD | Push Left Stick Down |
| LL | Push Left Stick Left |
| LR | Push Left Stick Right |
| LN | Return Left Stick Neutral |
