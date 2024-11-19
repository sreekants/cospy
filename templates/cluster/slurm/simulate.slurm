#!/bin/bash

#SBATCH --job-name=COS_Simulation
#SBATCH --time=00:10:00
#SBATCH --partition=CPUQ
#SBATCH --account=share-ie-idi
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=10
#SBATCH --output=COS_Simulation_map_%j.log

cd ${SLURM_SUBMIT_DIR}

if [ ! -d data ]; then
   mkdir data
fi

if [ ! -d build ]; then
   mkdir build
fi

srun --ntasks=$$NUM_TASKS$$ --multi-prog ./task.conf
