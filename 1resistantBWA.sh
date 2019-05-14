#!/bin/bash
#SBATCH --nodes=1
#SBATCH --time=6:00:00
#SBATCH --job-name 1 resistant bwa

cd $SCRATCH
cd BIF807/finalproject/RNA/1/resistant/                                                           

module load CCEnv;
module load nixpkgs/16.09;
module load fastqc;
module load intel/2017.1;
module load gcc/7.3.0;
module load bwa/0.7.17;

bwa mem  -M -R "@RG\tID:S1\tSM:S1N\tPL:Illumina\tPU:I1\tLB:Lib1" ../../reference/combinedGenome.fa PPEO23_Resistant_1.fastq.gz  PEO23_Resistant_2.fastq.gz > S1N.sam;