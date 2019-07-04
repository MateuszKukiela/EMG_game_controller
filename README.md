# EMG_game_controller

In order to properly run and use EMG controller you need to execute following steps.

1. Open "EMG_Controller_Training.psyexp" in Svarog. Set sampling frequency to 2048. Run callibration session and do appropriate tasks. Collected data save in player_data folder.

2. Open https://pong-2.com/ on your browser. Close Svarog. Open controller.py and change approprietly values of the variables in lines from 20 to 27. Variables which have "start" and "stop" in names are accordingly beginning and ending of channels no. for each player.

3. Open controller.py with /opt/braintech/bin/python3 

4. Switch window to browser and using appropriate hand gestures play the game.

Skills and tools you need to have in order to play properly:

-Ability to conduct EMG experiments.

-Appropriate drivers to your amplifier.
