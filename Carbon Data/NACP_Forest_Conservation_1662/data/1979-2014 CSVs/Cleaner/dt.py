from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df = pd.read_csv('clean_avg_all.csv')
df.dropna()

labels = np.array(df['AGC'])
df.index = df[['time', 'loc']]
features = df.drop(['time', 'AGC', 'loc', 'lat', 'lon'], axis=1)
feature_list = list(features.columns)
features = np.array(features)

train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25)

rf = RandomForestRegressor(n_estimators= 1000)
rf.fit(train_features, train_labels)
predictions = rf.predict(test_features)
print(test_labels)
errors = abs(predictions - test_labels)
print('Mean Absolute Error:', round(np.mean(errors), 4), 'AGC')

from sklearn.metrics import r2_score, accuracy_score, precision_score
r2 = r2_score(test_labels, predictions)
print(r2)



mape = 100 * (errors / test_labels)

accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')

# Get numerical feature importances
importances = list(rf.feature_importances_)

# List of tuples with variable and importance
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]

# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)

# Print out the feature and importances
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances]


# In[119]:


import matplotlib.pyplot as plt

#get_ipython().run_line_magic('matplotlib', 'inline')

# list of x locations for plotting
x_values = list(range(len(importances)))

# Make a bar chart
plt.bar(x_values, importances, orientation = 'vertical')

# Tick labels for x axis
plt.xticks(x_values, feature_list, rotation='vertical')

# Axis labels and title
plt.ylabel('Importance'); plt.xlabel('Variable'); plt.title('Variable Importances')

plt.show()