# Autocart-MHR
Automatic and repeated carting machine for Monster Hunter Rise talisman farming

## Background
Talisman is a key equipment in Monster Hunter Rise, with the capability of providing highly rated skills and slots. However, obtaining good (or even god) talismans requires effort and in-game resources, as they are generated from a random melding pot known as the Wisp of Mystery. A good description of the talisman mechanism can be found [here](https://game8.co/games/Monster-Hunter-Rise/archives/327175).

The problem is, each melding requires finishing a (non-expedition) quest to complete. It has been long discovered that the most efficient quest to take is the arena Rajang, and keep carting 10 times will complete 10 (the max number) melding batches in a "short" amount of time (about 15 minutes manually). However, talismans with the skill Weakness Exploit 2 and a 2-star slot, and potentially with the skill Critical Boost 2, are extremely rare, so even repeating the Rajang quest is time consuming. To address this problem, this repository presents an Arduino Switch controller that automatically accepts the Rajang quest and carts.

Also, to address the resource problem, thanks to [Ken_set](https://www.gamersky.com/handbook/202104/1384837.shtml), in 2.0 version of the game it is possible to save and reload the game to update the talisman results, without actually consuming (most of) the materials required for melding. The procedure is:

