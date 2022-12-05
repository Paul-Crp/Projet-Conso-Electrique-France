#%%
path_target1 = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "data", "data7.csv")
# %%
import pooch
import os 
URL="https://bit.ly/3i1OFkU"
path, fname = os.path.split(path_target1)
pooch.retrieve(URL, path=path, fname = fname, known_hash=None,)

# %%
