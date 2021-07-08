## Start typing here
'''
{
  "previousHash": 0x85Fe4ed2,
  "data": "asdfasdfasdf",
  "proofOfWork": 0x27efcd65
}

//To mine a new block, the inputs are:
// * The previous block, 
// * The data for the new block, 
// * The hash target. 
'''
import json
from hashlib import sha256
from typing import Set

set_of_hashes: Set[int] = {0x85Fe4ed2, 0x32deE6e1, 0x59daA9e2}

block = {
  "previousHash": 0x85Fe4ed2,
  "data": "asdfasdfasdf",
  "proofOfWork": 0x27efcd65
}

def hash_function(block):
    return hash(json.dumps(block))

old_block_hash = hash_function(block)

def mine_a_block(prev_block_hash:int, data: str, target: int):
    new_block = {}
    new_block["previousHash"] = prev_block_hash
    new_block["data"] = data
    # we need a way to be sure that the int ID doesn't collide with a previously made ID
    # a more comprehensive list is found here: https://en.wikipedia.org/wiki/List_of_hash_functions
    # sha256 from hashlib seems like a safer alternative
    for i in range(0, target):
        # -2147483647 should be the lowest int if we're looking at 32 bit integers not 0. 0 here such that it can run
        # comparison here needed to check against prev hashes i.e. if i not in set_of_hashes
        if i not in set_of_hashes:
            new_block["proofOfWork"] = i
            
    
    new_block_hash = hash_function(new_block) 
    set_of_hashes.add(new_block_hash)
    
    return new_block_hash, new_block
    
new_block_1_hash = mine_a_block(prev_block_hash=old_block_hash, data="reqweroiuqpw", target=100)[0]
new_block_1_block = mine_a_block(prev_block_hash=old_block_hash, data="reqweroiuqpw", target=100)[1]
print(new_block_1_hash)
print(new_block_1_block)
print(mine_a_block(prev_block_hash=new_block_1_hash, data="ruewiqpower", target=10))
