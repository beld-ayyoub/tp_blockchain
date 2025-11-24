# beldjillali ayyoub gr1


import hashlib
import time

# this is one block in the chain
class block:
    def __init__(self, block_id, block_time, block_data, prev_hash="0"):
        self.block_id = block_id
        self.block_time = block_time
        self.block_data = block_data
        self.prev_hash = prev_hash
        self.nonce = 0   # number we try again and again
        self.hash = self.make_hash()

    # make the sha256 hash for this block
    def make_hash(self):
        text = (
            str(self.block_id) +
            str(self.block_time) +
            str(self.block_data) +
            str(self.prev_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(text.encode()).hexdigest()

    # try many times until the hash starts with n zeros
    def mine(self, diff):
        need = "0" * diff
        start = time.time()

        # try new numbers until we get a hash that starts with zeros
        while not self.hash.startswith(need):
            self.nonce += 1
            self.hash = self.make_hash()

        end = time.time()
        print(f"block {self.block_id} mined: {self.hash}")
        print(f"time: {end - start:.4f} sec")

# this is our whole blockchain
class blockchain:
    def __init__(self, diff=4):
        self.diff = diff
        self.chain = [self.make_first_block()]

    # make the first block (genesis block)
    def make_first_block(self):
        return block(0, time.time(), "first block", "0")

    # get last block in chain
    def last(self):
        return self.chain[-1]

    # add new block with given data
    def add_block(self, data):
        new_block = block(len(self.chain), time.time(), data)
        new_block.prev_hash = self.last().hash
        new_block.mine(self.diff)
        self.chain.append(new_block)

    # check if all blocks are still good
    def check(self):
        for i in range(1, len(self.chain)):
            now = self.chain[i]
            before = self.chain[i - 1]

            # check if the hash is still correct
            if now.hash != now.make_hash():
                print("wrong hash found")
                return False

            # check if the link is broken
            if now.prev_hash != before.hash:
                print("wrong link found")
                return False

            # check if hash starts with needed zeros
            if not now.hash.startswith("0" * self.diff):
                print("wrong difficulty")
                return False

        return True

    # show all blocks in the chain
    def show(self):
        for b in self.chain:
            print("\n-block-")
            print("id:", b.block_id)
            print("time:", b.block_time)
            print("data:", b.block_data)
            print("prev:", b.prev_hash)
            print("hash:", b.hash)
            print("nonce:", b.nonce)
            print("                       ")

   # example :

if __name__ == "__main__":
    my_chain = blockchain()

    print("\nmining blocks...")
    my_chain.add_block("send 5 coins")
    my_chain.add_block("send 2 coins")

    print("\nshow chain:")
    my_chain.show()

    print("\nis chain ok?", my_chain.check())

    print("\nchange data to test")
    my_chain.chain[1].block_data = "hack 999 coins"
    print("is chain ok?", my_chain.check())
