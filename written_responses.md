## Written Responses

1. Describe the general process of how blocks are added to a blockchain. 
2. How can blockchain users mine coins?

Blockchain begins with a single genisis block. In our example, our blocks were required to have:

Index - the number of the block in the chain, starting at 0 or 1, depending on the chain.
Timestamp - the time at which the block was created. This is not required, but is often useful.
Transactions - the monetary transactions, or any type of data, that is proofed by the block.
Proof - the proof for this block.
Previous Hash - the hash of the previous block.

To add a new block to the blockchain (and potentially be rewarded) a miner must provide proof of work. Proof of work is basicially a solution to a complex problem. In this case, the hash of the last block on the chain. If the proof is valid, the block is added to the blockchain along with the previous blocks hash, and all nodes in the network are notified of the change in the ledger.

3. Explain how simulations like Conway's Game of Life can be used in real-world applications.

Conway's game of life can be used in any situation where state changes based on a set of rules.  For instance, traffic patterns, populations sizes, cars, planes, or any object/task that changes state can be representing by Conways's Game of Life.