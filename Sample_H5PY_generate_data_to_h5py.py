#import h5py library
import h5py

#Create Dictionary
languages = {
    'name': 'python',
    'version': '3.5'
}

#for each element in dictionary, create dataset by dictionary key (name) & dictionary value (version)
with h5py.File('out/stest.h5','w') as hf:
    for element in languages.keys():
        hf.create_dataset(element, data=languages[element])