#Evaluation and optimization of hepatocyte culture media factors by design of experiments (DoE) methodology
import anndata as ad
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys 
test=pd.read_csv("test.csv")

plt.hist(np.random.randn(1000))
plt.savefig("nomal.png")
plt.close()