# This is only a forked repository from ClarityCoders/Fall-Guys-AI and it is used to show results for another game

<a href="https://youtu.be/GS_0ZKzrvk0" target="_blank"><img src="https://i.imgur.com/sG7xxyc.png" title="Clarity Coders YouTube" /></a>
# Python / FastAI CNN - Playing Driftboss
> The network was then trained using the FastAI Libary. 

# The Game
- Driftboss is a 3D endless runner arcade racing game
- Only control is the "Space" key which turns the car to the right
![Driftboss](https://user-images.githubusercontent.com/54573938/132589747-d66137e6-7765-4c7d-a8a9-1de592f59e66.JPG)


## Setup
- I used dual monitors with a game playing at a 566 X 518 resolution on one screen.
- Since the edges of the road were pretty obvious, downsizing the grabbed screen, converting to gray and using Canny edge detection was enough to reach an average result.

## Train
- Use the file called training.py
- Point it at your image directory

## Inputs (Observations)
- Uses inputs to the neural network (Observations) of pixes in the game.
- 84 X 84

## Contact!
- YouTube <a href="https://www.youtube.com/claritycoders" target="_blank">Clarity Coders</a>
- Chat with me! <a href="https://discord.gg/cAWW5qq" target="_blank">Discord</a> 

## Loss Values
- Loss results after 20 epochs

![rates](https://user-images.githubusercontent.com/54573938/132588090-04f81bc1-db07-4cf2-b0c8-82674701b1b4.JPG)

## Learning Rate
- To get better results from training, the Learning Rate is set to 10^-1 based on the LR_Graph
![lr](https://user-images.githubusercontent.com/54573938/132587952-963b3412-5ae3-42e3-94fc-2bafa30e9fe1.JPG)

## Confusion Matrix
- Trained with 26k Samples with some opencv filters to make the training process easier

![confusion_matrix](https://user-images.githubusercontent.com/54573938/132587594-20e7747c-4ab9-4994-863e-00b5beb06e29.JPG)
