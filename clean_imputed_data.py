import os

# Removes all but the lowest RMSE score per dataset, missrate, sparsity combination.

if __name__ == '__main__':
    folder = 'imputed_data'
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    temp = ('data_name', 'miss_rate', 'sparsity', 1.)
    for file in files:
        split = file.split('_')
        data_name = split[0]
        miss_rate = split[2]
        sparsity = split[4]
        rmse = float('0.' + split[6].split('.')[1])

        # Keep only the lowest rmse score of each 5 runs and discard the few odd files for spam with miss rate 0.8
        if (data_name == temp[0] and miss_rate == temp[1] and sparsity == temp[2] and rmse > temp[3]
                or data_name == 'spam' and miss_rate == '0.8'):
            os.remove(os.path.join(folder, file))
        else:
            temp = (data_name, miss_rate, sparsity, rmse)
