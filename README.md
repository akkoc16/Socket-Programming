[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
# Socket-Programming
### Server and Client Based (MultiUser) Hangman Game



![Client-Server](https://hackernoon.com/hn-images/0*1fa09gbGxyuYETj7.png)

## Server-side features :

* Asking that how many players there will be.
* Registering each player/client to the server so each player will have a unique ID. For registration, each player creates an account for itself on the server (a password is necessary for each account). 
* Communicating with just one player or more than one player at a time. 
* Keeping latest status information and showing this information to the players. 
* Getting guesses from players in order and compare with the phrase. 
* Keeping the order of players and inform to all players about which player will play next (order will be determined from connection order to the server to play). 
* Keeping wrong guesses for both letters and phrases.
* Showing current guess of the player to other players. 
* Calculation of remaining allowed attempts. 
 
## Rules: 
 
1. The game starts after specified number of players connect to the server.  
2. Allowed number of attempts decrease one by one in exchange for each wrong letter guess or each wrong phrase guess. 
3. Server accepts lowercase or uppercase letter for both letter guesses and phrase guesses. But if user enters an uppercase letter, you have to convert to lowercase. 
4. If the user enters two or more letters instead of one letter or enters a number, these count as wrong guess and as a result number of attempt decrease. 
5. The game terminates after 7 wrong guesses. 
6. The game also terminates if one player guesses whole phrase right or all letters are guesses correctly. 
7. The player who registered before should inform the server if she/he wants to play again.


## Sample Game Images

![1](https://github.com/akkoc16/Socket-Programming/blob/master/client-server/s1.png)
![2](https://github.com/akkoc16/Socket-Programming/blob/master/client-server/s2.png)
![3](https://github.com/akkoc16/Socket-Programming/blob/master/client-server/s3.png)
![4](https://github.com/akkoc16/Socket-Programming/blob/master/client-server/s4.png)
![5](https://github.com/akkoc16/Socket-Programming/blob/master/client-server/s5.png)
![6](https://github.com/akkoc16/Socket-Programming/blob/master/client-server/s6.png)
![7](https://github.com/akkoc16/Socket-Programming/blob/master/client-server/s7.png)
![8](https://github.com/akkoc16/Socket-Programming/blob/master/client-server/s8.png)
![9](https://github.com/akkoc16/Socket-Programming/blob/master/client-server/s9.png)
![10](https://github.com/akkoc16/Socket-Programming/blob/master/client-server/s10.png)
