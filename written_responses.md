## Written Responses

1. Describe the general process of how blocks are added to a blockchain.
    After the initial "genesis" block, new blocks are added to a blockchain by finding a new hash that meets the guidelines for the chain. In our earlier assignment, each of the new blocks had to have a hash that started with 6 zeroes, and this sprint challenge requires the end of the previous hash to match the beginning of the current hash. This is done by finding the "proof", which modifies the hash for each guess attempted. These blocks then contain the lists of transactions made, along with the previous hash, so that any modifications to a block after it has been added will break the chain.

2. How can blockchain users mine coins?
    Users can mine coins by using their computers to calculate the "proof" needed to form the next hash. This is then checked against the blockchain's rules to make sure it matches correctly.  If the block is accepted by the chain, the miner is then rewarded for the submission.

3. Explain how simulations like Conway's Game of Life can be used in real-world applications.
    Conway's game of life can be used to simulate conditions where a state changes according to specific rules. 