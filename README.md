# Sprint-Challenge-Blockchain-Cellular-Automata


This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we were introduced to the fascinating world of blockchains and continued honing our algorithmic, problem-solving skills by implementing a well-known simulation - Conway's Game of Life. In your challenge this week, you will demonstrate proficiency by adding another key feature to your blockchain and completing a variant of Conway's Game of Life.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  cellular automata (10 points), blockchain (12 points) and a short written response (20 points). There is also a stretch goal in the blockchain section which should only be attempted after the rest of the problems have been completed.

## Written Response

You will be expected to answer the following three questions:

1. Describe the general process of how blocks are added to a blockchain.
2. How can blockchain users mine coins?
3. Explain how simulations like Conway's Game of Life can be used in real-world applications.


Think about how you would answer these questions in an interview. Your answers will receive points at the TL's discretion based on the following criteria:

  * 20: Would love to have this person on my team!
  * 14: Wouldn't mind working with this person.
  * 10: Knowledge is lacking OR poor communication skills (explanation was not as clear as it could have been)
  *  6: Knowledge is lacking AND poor communication skills 
  *  2: You get 2 points for attempting

Please add your responses to [written_responses.md](written_responses.md)


## Project Set Up

### 1. Blockchain

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

Complete details can be found within the README file in the `blockchain` directory.

### 2. Cellular Automata - 1D Life

> This is an implementation of Wolfram's [Rule 126](http://mathworld.wolfram.com/Rule126.html).

![126](https://tk-assets.lambdaschool.com/7220f917-2fe3-4487-88df-f3cb75a0dcb0_126.gif)

Follow these steps to set up your project:

* The starter code currently draws the first row of the automata.
* You'll need to complete the `get_new_val()` function in `1d-life.py` to update subsequent rows.

#### What is 1D Life?

In the Game of Life, we used a 2D grid to store the cellular automaton.
In 1D life, it's a simple 1D array.

Each "generation", the array is examined and new values for each cell
are computed based on the values of that cell and its surrounding
cells.

Usually the subsequent generations are displayed on the next row of a
bitmap. Generation 0 is shown on row 0, generation 1 on row 1, and so
on.


#### Algorithm

Everything is written for you except the code in `get_new_val()`. This
function accepts a list of the current life status, and the previous generation (integer). You can then use that generation value to analyze the correct row (indices) in the list.

The function should return a new list with correct values added to the next row that indicate which cells are now alive or dead.

Whether or not the cell should remain alive or die depends on the
results of the calculation of [Rule 126](#rule-126), that you will
implement, below.


#### Rule 126

This rule describes how cells live and die based on their own values,
and that of their immediate neighbors.

For example, if a cell is dead (.), and its immediate neighbors are alive (#),
that pattern of 3 cells is:

```
#.#
```

For any of 8 possible combinations of 3 cells surrounding and
including a cell at an _x_ coordinate, we produce a new single cell
at that _x_ coordinate as given by the following table (`.` is 0, `x`
is 1):

```
...  ..#  .#.  .##  #..  #.#  ##.  ###     <- this pattern
 .    #    #    #    #    #    #    .      <- produces this result
```

The final output should look like this:

![Rule 126](https://tk-assets.lambdaschool.com/bcccf169-3288-490a-b7e3-dd955e010256_rule126.png)

This result is a [Sierpinski
Triangle](https://en.wikipedia.org/wiki/Sierpinski_triangle), a
[fractal](https://en.wikipedia.org/wiki/Fractal) that has a habit of
turning up in surprising places.

In your solution, it is essential that you follow best practices and produce clean and professional results. Schedule time to review, refine, and assess your work and perform basic professional polishing including spell-checking and grammar-checking on your work. It is better to submit a challenge that meets MVP than one that attempts to much and does not.

[Validate your work through testing and ensure that your code operates as designed.]

#### Rubric

This problem will be graded out of 12 points:

* 2: Code attempted
* 5: Fewer than 3 minor errors preventing code from running successfully
* 8: Code successfully generates a Sierpinski
Triangle
* 10: Additional functionality added to visualization (scrolling, wrapping, etc.)

## Minimum Viable Product

You can earn 22 points from the main coding portion of the sprint challenge.  Be sure to budget your time wisely.  The Blockchain challenge is fun, but it is only 1/3 of the points availible for the coding portion of this challenge.  

#### Blockchain - 12 pts
  * ex1 - 12 pts

#### Cellular Automata - 10 pts
  * Rule 126 - 10 pts

### Grading

Students can receive up to 42 points in total for this Sprint Challenge.

  * __Coding Challenges__: 22
  * __Interview__: 20

--------

The score distributions are as follows:

  * __3__: >= 36 points
  * __2__: >= 26 points
  * __1__: <= 25 points 
