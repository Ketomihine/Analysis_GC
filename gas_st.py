#HRR742264_S1_L001_R1_001.fastq.gz
#HRR742264_S1_L001_R2_001.fastq.gz
cd /mnt/data/zehuazeng/result/GC_ST/HRR742264 ; spaceranger count --id=HRR742264 \
--transcriptome=/mnt/data/space/refdata-gex-GRCh38-2020-A \
--fastqs=/mnt/data/zehuazeng/fastq/GC_ST/HRR742264 \
--sample=HRR742264 \
--image=/mnt/home/zehuazeng/analysis/24_GC/data/GC_ST/HRR742264_img.jpg \
--unknown-slide visium-1 \
--localcores 9 \
--create-bam true