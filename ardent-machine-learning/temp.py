import os
import pandas as pd
from snapy import MinHash, LSH

if __name__ == '__main__':
    df = pd.read_csv(os.path.join(os.getcwd(), 'scan_data', 'home.csv'))
    df = df[df['Name'].str.len()>5]
    df['Id'] = range(1, df.shape[0]+1)

    file_index = df['Id'].to_list()
    file_names = df['Name'].to_list()

    # Create MinHash object
    minhash = MinHash(file_names, n_gram=3, permutations=100, hash_bits=64, seed=3)

    # Create LSH model
    lsh = LSH(minhash, file_index, no_of_bands=50)

    # Returns edge list for use creating a weighted graph.
    edge_list = lsh.edge_list(min_jaccard=0.9, jaccard_weighted=True)
    print(pd.DataFrame(edge_list, columns=['Source', 'Destination', 'Weight']))
