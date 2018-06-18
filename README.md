# MCM 2018: Interdisciplinary Analysis of Energy Consumption in Various States

## Goal of the project
In this project, we aim to provide a mathematical analysis of the energy profiles of certain states in the US based on over 100,000 lines of data provided by the US Energy Information Administration. 

## Overview of the Paper
The paper describes the energy usage profiles for Arizona (AZ), California (CA), New Mexico (NM), and Texas (TX) from 1960 to 2009. It also provides in-depth explanations of the algorithms, mathematical approaches, and graphs that we developed for the basis for our conclusions. 

## Overview of the Files
All of the data is in ``` ProblemCData.xlsx ```.

Each Python file contributes to the overall project in some way, though not all are used for the actual model. The most important files are ``` econModel.py ``` and ``` competeResources.py ```, which contain a large part of the model itself.
- ``` econModel.py ``` provides the majority of the "Cobb-Douglas Production Function" portion of the program, used to extract certain properties of energy usage.
- ``` competeResources.py ``` utilizes parts of the ``` econModel.py ``` code to gather data about certain properties of energy usage. From there, it will recursively process the existing data (1960-2009) in order to predict energy usage up to 2050.
- ``` rungeKutta.py ``` is used to gather values of energy usage using well-known and accurate approximation methods.
- ``` fetchValues.py ``` parses the provided data and outputs smaller excel files for energy categories we are more concerned about.
- ``` searchData.py ``` searches the data in ``` ProblemCData.xlsx ``` based on a category and year that you input.
- ``` globalFuncs.py ``` and ``` variableFuncs.py ``` provide utility functions.

## Running the model
Run ``` python competeResources.py ``` in terminal, and it will output energy consumption for every year, separated by state.

## Authors
- **Clayton Chu** ([pacbac](github.com/pacbac)) - *Creation, Python implementation, and fine-tuning of the model*
- **Jerry Yin** - *Creation of the model, finding functions of best fit for data*
- **Zhenxiao Chen** - *Creation of the model, data analysis, finding functions of best fit for data*
