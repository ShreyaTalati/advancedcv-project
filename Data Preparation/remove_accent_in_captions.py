import pandas as pd 
import unidecode

test = "C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/retrieval_dict/metadata_test.csv"
train = "C:/Users/shrey/Downloads/dataset/Final/ISIA_Food500/ISIA_Food500/retrieval_dict/metadata_train.csv"

df1 = pd.read_csv(test)
df2 = pd.read_csv(train)

def remove_accents(a):
    return unidecode.unidecode(a)

def util(df_cap, file):
    df_cap['filename'] = df_cap['filename'].apply(remove_accents)
    df_cap['cat'] = df_cap['cat'].apply(remove_accents)
    df_cap['caption'] = df_cap['caption'].apply(remove_accents)
    df_cap.to_csv(file, index=False)

util(df1, test)
util(df2, train)

