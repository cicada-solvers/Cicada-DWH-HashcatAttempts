import os
import os.path

DWH_DIR=os.path.dirname(os.path.realpath(__file__))
DWH_FILE=os.path.join(DWH_DIR,"deepwebhash")

HC_DIR=os.path.abspath(os.path.join(DWH_DIR, os.pardir))#we're assuming that this repo was made as a new folder in the Hashcat directory

HC_COMMAND="hashcat -m HASH_TYPE TEST_ARGS -O > DWH_DIR/results/TEST_NAME_HASH_NAME.log"

hashes={
    "blake2b-512":{"type":600,"hashfile":DWH_FILE+"-blake2"}, #blake2 hashes require a prefix for hashcat
    "sha3-512":{"type":17600},
    "sha512":{"type":1700},
    "whirlpool":{"type":6100},
    "streebog":{"type":11800}
}

tests={
    "ipv4":"-a 3 DWH_FILE DWH_DIR/masks/ipv4.hcmask",
    "allbytes":"-a 3 DWH_FILE DWH_DIR/masks/allbytes-lengths1-5.hcmask",
    "usphones":"-a 3 DWH_FILE DWH_DIR/masks/usphones.hcmask",
}

#set the default DeepWebHash for hash methods
for hashname in hashes:
    if not "hashfile" in hashes[hashname]:
        hashes[hashname]['hashfile'] = DWH_FILE
