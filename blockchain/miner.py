import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...999123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    """

    start = timer()

    print("Searching for next proof")
    
    Partial_proof = random.randint(100000, 999999)
    front_proof = random.randint(1000000000000,9999999999999)
    fullProof = str(front_proof) + str(Partial_proof)
    proof = int(fullProof)
    

    #  TODO: Your code here
    while valid_proof(last_proof, proof) == True:
        proof = random.randint(0, 9999999999999999999)
        # proof = 694204


    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    
  

    return proof


def valid_proof(last_hash, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the last hash match the first six characters of the proof?

    IE:  last_hash: ...999123456, new hash 123456888...
    """

    # TODO: Your code here!
    print(last_hash)
    print(proof)
    stringHash = str(last_hash)
    print(len(stringHash[0:3]))
    length_hash = len(str(last_hash))
    print(length_hash)
    length_hash_six = length_hash - 6
    print(str(length_hash-5))
    string_proof = str(proof)
    
    last_six_hash = stringHash[int(length_hash)-6: int(length_hash)]
    print(last_six_hash)
    first_six_proof = string_proof[0:6]

    if last_six_hash == first_six_proof:
        return True
    else:
        return False



    pass


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()
    if len(id) == 0:
        f = open("my_id.txt", "w")
        # Generate a globally unique ID
        id = str(uuid4()).replace('-', '')
        print("Created new ID: " + id)
        f.write(id)
        f.close()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
