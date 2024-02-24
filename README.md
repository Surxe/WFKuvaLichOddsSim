# WFKuvaLichOddsSim
Simulates how many attempts are needed to slay a Kuva Lich using the Requiem puzzle.

See the Warframe wiki page for Kuva Lich on how the Requiem puzzle works. https://warframe.fandom.com/wiki/Kuva_Lich

Requiem Puzzle:
A Kuva Lich secretly requires 3 Requiems out of 7 in order to slay them, and the order of the Requiems matter.

On each attempt to slay them, each requiem is evaluated one at a time. 
If a requiem is incorrect, the user is told it is incorrect, and their attempt is over, receiving no further information.
If a requiem is correct, it proceeds to try the next requiem. If all 3 requiems are correct, the Kuva Lich is slain.

Additionally, the user may learn through other means on which 3 of the 7 requiems are somewhere in the secret ordering, without knowing where.

Naturally, these Requiems will want to be prioritized for determining the order. If all 3 requiems are already known, and only their order remains, the estimated # of attempts can simply be calculated as 2.5 like below:
=(50/3*1 + 100/3*2 + 100/3*3 + 50/3*4)/100), or rather, 16.66%, 33.33%, 33.33%, 16.66% for taking 1, 2, 3, or 4 attempts, respectively, totaling to 100%


Output of program simulation is as follows:
All 3 reqs known on every attempt:
Calculated # of attempts: 2.5
Avg attempts taken: 2.463
Chance for x number of attempts to complete lich: 
1  attempts: 18.3%  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
2  attempts: 32.2%  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
3  attempts: 34.4%  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
4  attempts: 15.1%  ||||||||||||||||||||||||||||||||||||||||||||||||||



No reqs were known on every attempt:
Calculated # of attempts: TBD
Avg attempts taken: 9.942
Chance for x number of attempts to complete lich: 
1  attempts: 0.1%   
2  attempts: 0.5%   ||
3  attempts: 1.8%   ||||||
4  attempts: 2.7%   |||||||||
5  attempts: 4.0%   |||||||||||||
6  attempts: 6.7%   ||||||||||||||||||||||
7  attempts: 9.9%   |||||||||||||||||||||||||||||||||
8  attempts: 10.0%  |||||||||||||||||||||||||||||||||
9  attempts: 9.6%   ||||||||||||||||||||||||||||||||
10 attempts: 9.8%   |||||||||||||||||||||||||||||||||
11 attempts: 11.4%  ||||||||||||||||||||||||||||||||||||||
12 attempts: 9.9%   |||||||||||||||||||||||||||||||||
13 attempts: 8.5%   ||||||||||||||||||||||||||||
14 attempts: 5.9%   ||||||||||||||||||||
15 attempts: 4.1%   ||||||||||||||
16 attempts: 3.2%   |||||||||||
17 attempts: 1.2%   ||||
18 attempts: 0.7%   ||
