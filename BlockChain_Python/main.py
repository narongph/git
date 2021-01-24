# consists blocks
# blocks consist transaction
# blocks are connected through hasing
        # unique digital fingerprint - transaction + previous blocks fingerprint

from Block import Block

blockchain = []

genesis_block = Block("Chancellor on the brink...", ["Satoshi sent 2 BTC to Ivan", 
                                                        "Satoshi sent 5 BTC to Hal Finney"])

second_block = Block(genesis_block.block_hash, ["Ivan sent 5 BTC to Liz"])
third_block = Block(second_block.block_hash, ["A to C 5 BTC", "G to D 4 BTC"])

print("Block hash: Genesis Block")
print(genesis_block.block_hash)

print("Block hash: Second Block")
print(second_block.block_hash)

print("Block hash: Third Block")
print(third_block.block_hash)
