## Project Title
NP Complete Project: Max Clique

## Authors
Gavin Barro and Cole Determan

## Testing
To run our test cases:
- Run the following commands:
    - cd code_solution
    - chmod +x run_test_cases.sh
    - ./run_test_cases.sh

To create and run the worst case graph:
- Run the following commands:
    - cd code_solution
    - chmod +x run_worst_case.sh
    - ./run_worst_case.sh


NOTE:
- Because our large graph data is randomly generated (with an edge probability of 0.5 indicating a moderate density, which could be changed based on needs), we used a known_max_clique algorithm which is linked below
    - This returned just the size of the max_clique, not the actual max clique itself
    - Which is what we designed
- We used this to compare our output with the expected, as these graphs were extremely large and would take an excruiatingly long time to draw by hand, and there could be multiple max_cliques of the same size
- The worse case test, should take over 30 minutes, as it is a complete graph, meaning our pruning was useless
     

# Acknowledgements
We would like to thank Dr. Bowers, for his guidance and support throughout this project and this semester. His lectures, insights, and feedback were invaluable in shaping the work presented here.

We would also like to thank "" for his help with the known_max_clique, we used their work to help test our outputs and make sure we got the right size of the clique, for reasons listed above

We would also like to thank the author of our textbook, Jeff Erickson, as we used the textbook to verify our understanding of the material before coding this.