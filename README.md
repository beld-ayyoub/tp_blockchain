# tp_blockchain

explanation of your implementation;

block class:

eachblock has an id, time, data, previous hash, nonce, and its own hash.

make_hash() makes a unique sha256 hash for the block using its content.

mine(diff) tries different numbers (nonce) until the hash starts witha certain number of
zeros (diff = difficulty).

blockchain class:

itstarts with a genesis block (first block).

add_block(data) creates a new block, links it to the last block, and mines it.

check() makes sure all blocks are valid: hash is correct, chain links are correct, and mining
difficulty is satisfied.

show() prints all block information.

running the code :

first,it makes a blockchain with a difficulty of 4.

then it adds two blocks with data "send 5 coins" and "send 2 coins".

it prints all blocksand checks if the chain is okay.

finally,it changes one block's data to test that the chain becomes invalid.

![Screenshot](screenshot-.png)
