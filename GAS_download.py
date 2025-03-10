import os
import time

filepaths = [
    'era-fasp@fasp.sra.ebi.ac.uk:/vol1/srr/SRR971/009/SRR9713139',
    'era-fasp@fasp.sra.ebi.ac.uk:/vol1/srr/SRR971/001/SRR9713141',
    
]

def download_file_stanford(filepath, max_retries=5, retry_delay=30):
    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1} for {filepath}")
        print(f'ascp -v -k 1 -T -l 200m -P 33001 -i /scratch/users/steorra/env/iseq/etc/asperaweb_id_dsa.openssh {filepath} /scratch/users/steorra/data/SRA/GAS_SC')
        result = os.system(f'ascp -v -k 1 -T -l 200m -P 33001 -i /scratch/users/steorra/env/iseq/etc/asperaweb_id_dsa.openssh {filepath} /scratch/users/steorra/data/SRA/GAS_SC')
        if result == 0:
            print(f"Successfully downloaded {filepath}")
            return True
        else:
            print(f"Failed to download {filepath}, retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
    print(f"Exceeded maximum retries for {filepath}")
    return False

def download_file_ustb(filepath, max_retries=5, retry_delay=30):
    for attempt in range(max_retries):
        print(f"Attempt {attempt + 1} for {filepath}")#
        print(f'ascp -v -k 1 -T -l 200m -P 33001 -i /mnt/home/zehuazeng/miniconda3/envs/ascp/etc/asperaweb_id_dsa.openssh {filepath} /mnt/data/zehuazeng/SRA/GAS_SC')
        result = os.system(f'ascp -v -k 1 -T -l 200m -P 33001 -i /mnt/home/zehuazeng/miniconda3/envs/ascp/etc/asperaweb_id_dsa.openssh {filepath} /mnt/data/zehuazeng/SRA/GAS_SC')
        if result == 0:
            print(f"Successfully downloaded {filepath}")
            return True
        else:
            print(f"Failed to download {filepath}, retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
    print(f"Exceeded maximum retries for {filepath}")
    return False

for filepath in filepaths:
    download_file_stanford(filepath)