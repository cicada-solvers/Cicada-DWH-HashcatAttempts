import presets
import time
import os
import sys

os.chdir(presets.HC_DIR)

argc = len(sys.argv) - 1;
test_name_match = "all"
hash_name_match = "all"
if argc>0:
    test_name_match=sys.argv[1];
if argc>1:
    hash_name_match=sys.argv[2];

for test_name,test_args in presets.tests.items():
    if not test_name_match==test_name and not test_name_match=="all":
        continue
    print("TEST "+test_name+" -> "+test_args)
    test_command = presets.HC_COMMAND.replace("TEST_ARGS",test_args).replace("TEST_NAME",test_name).replace("DWH_DIR", presets.DWH_DIR);
    print(" "+test_command)


    
    for hash_name,hash_params in presets.hashes.items():
        if not hash_name_match==hash_name and not hash_name_match=="all":
            continue
        print("   HASH "+hash_name)
        test_hash_command = test_command.replace("HASH_NAME",hash_name).replace("HASH_TYPE",str(hash_params['type'])).replace("DWH_FILE",hash_params['hashfile'])
        print("    "+test_hash_command)
        #os.system(test_hash_command)
        
        
    
    
time.sleep(5)