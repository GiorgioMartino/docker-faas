# Fitting Docker vs Faasd  Distribution


```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fitter import Fitter, get_common_distributions, get_distributions

pd.options.display.max_rows = 50
sns.set_theme(style="darkgrid")
```


```python
dataset = pd.read_csv("../results/resp_time_distribution.csv")
```


```python
dataset.head()
```




<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>docker-distance</th>
      <th>faasd-distance</th>
      <th>docker-blockchain</th>
      <th>faasd-blockchain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.006910</td>
      <td>0.321220</td>
      <td>0.864425</td>
      <td>2.009566</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.013986</td>
      <td>0.183193</td>
      <td>0.869114</td>
      <td>1.990304</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.006473</td>
      <td>0.192597</td>
      <td>0.876750</td>
      <td>1.980668</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.006076</td>
      <td>0.216715</td>
      <td>0.890567</td>
      <td>1.980647</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.022268</td>
      <td>0.242508</td>
      <td>0.877038</td>
      <td>1.961713</td>
    </tr>
  </tbody>
</table>
</div>



# Blockchain Response Time

## Docker Blockchain


```python
fig = plt.figure(figsize=(15, 10))

sns.histplot(data=dataset, x="docker-blockchain", bins=100, kde=True)
```




    <AxesSubplot:xlabel='docker-blockchain', ylabel='Count'>




    
![png](output_6_1.png)
    



```python
docker = dataset["docker-blockchain"].values
```


```python
# f = Fitter(docker, timeout=100)
fig = plt.figure(figsize=(15, 10))

f = Fitter(docker, distributions=get_common_distributions())
f.fit()
f.summary(method='sumsquare_error')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sumsquare_error</th>
      <th>aic</th>
      <th>bic</th>
      <th>kl_div</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>lognorm</th>
      <td>1086.391969</td>
      <td>172.820557</td>
      <td>103.585351</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>expon</th>
      <td>1112.746468</td>
      <td>345.950274</td>
      <td>120.646766</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>exponpow</th>
      <td>1264.339334</td>
      <td>406.014239</td>
      <td>255.272986</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>rayleigh</th>
      <td>1708.417418</td>
      <td>1575.805192</td>
      <td>549.382966</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>norm</th>
      <td>1797.386101</td>
      <td>2158.546230</td>
      <td>600.148954</td>
      <td>inf</td>
    </tr>
  </tbody>
</table>
</div>




    
![png](output_8_1.png)
    



```python
f.get_best()
```




    {'lognorm': {'s': 1.1076244750592275,
      'loc': 0.8178075536764503,
      'scale': 0.027484631343196453}}



## Faasd Blockchain


```python
fig = plt.figure(figsize=(15, 10))

sns.histplot(data=dataset, x="faasd-blockchain", bins=100, kde=True)
```




    <AxesSubplot:xlabel='faasd-blockchain', ylabel='Count'>




    
![png](output_11_1.png)
    



```python
faasd = dataset["faasd-blockchain"].values
```


```python
fig = plt.figure(figsize=(15, 10))

f = Fitter(faasd, distributions=get_common_distributions())
f.fit()
f.summary()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sumsquare_error</th>
      <th>aic</th>
      <th>bic</th>
      <th>kl_div</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>rayleigh</th>
      <td>155.765802</td>
      <td>1304.015531</td>
      <td>-1845.586159</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>lognorm</th>
      <td>157.207713</td>
      <td>555.103508</td>
      <td>-1829.464069</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>norm</th>
      <td>162.733083</td>
      <td>1848.821709</td>
      <td>-1801.828440</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>cauchy</th>
      <td>167.289326</td>
      <td>391.918761</td>
      <td>-1774.214963</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>exponpow</th>
      <td>171.825520</td>
      <td>1188.163258</td>
      <td>-1740.552470</td>
      <td>inf</td>
    </tr>
  </tbody>
</table>
</div>




    
![png](output_13_1.png)
    



```python
f.get_best()
```




    {'rayleigh': {'loc': 1.9104911172189012, 'scale': 0.1797653996701631}}



# String Distance Response Time

## Docker String Distance


```python
fig = plt.figure(figsize=(15, 10))

sns.histplot(data=dataset, x="docker-distance", bins=100, kde=True)
```




    <AxesSubplot:xlabel='docker-distance', ylabel='Count'>




    
![png](output_17_1.png)
    



```python
docker = dataset["docker-distance"].values
```


```python
fig = plt.figure(figsize=(15, 10))

# f = Fitter(docker, timeout=100)
f = Fitter(docker, distributions=get_common_distributions())
f.fit()
f.summary()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sumsquare_error</th>
      <th>aic</th>
      <th>bic</th>
      <th>kl_div</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>cauchy</th>
      <td>97399.346127</td>
      <td>-384.959034</td>
      <td>4592.635008</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>exponpow</th>
      <td>193325.783056</td>
      <td>112.611698</td>
      <td>5285.100027</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>lognorm</th>
      <td>196230.177446</td>
      <td>-383.453870</td>
      <td>5300.011611</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>norm</th>
      <td>196292.616932</td>
      <td>-377.802417</td>
      <td>5293.422000</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>gamma</th>
      <td>200823.083374</td>
      <td>-421.593328</td>
      <td>5323.147604</td>
      <td>inf</td>
    </tr>
  </tbody>
</table>
</div>




    
![png](output_19_1.png)
    



```python
f.get_best()
```




    {'cauchy': {'loc': 0.022805109566822176, 'scale': 0.0018872360976320396}}



## Faasd String Distance


```python
fig = plt.figure(figsize=(15, 10))

sns.histplot(data=dataset, x="faasd-distance", bins=100, kde=True)
```




    <AxesSubplot:xlabel='faasd-distance', ylabel='Count'>




    
![png](output_22_1.png)
    



```python
faasd = dataset["faasd-distance"].values
```


```python
fig = plt.figure(figsize=(15, 10))

f = Fitter(faasd, distributions=get_common_distributions())
f.fit()
f.summary()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sumsquare_error</th>
      <th>aic</th>
      <th>bic</th>
      <th>kl_div</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>rayleigh</th>
      <td>2276.893182</td>
      <td>-237.897578</td>
      <td>836.627385</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>lognorm</th>
      <td>2383.026406</td>
      <td>-231.680393</td>
      <td>889.094545</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>gamma</th>
      <td>2417.679965</td>
      <td>-218.099433</td>
      <td>903.531654</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>norm</th>
      <td>2431.521392</td>
      <td>-212.291293</td>
      <td>902.332659</td>
      <td>inf</td>
    </tr>
    <tr>
      <th>expon</th>
      <td>2463.580515</td>
      <td>-239.723618</td>
      <td>915.431296</td>
      <td>inf</td>
    </tr>
  </tbody>
</table>
</div>




    
![png](output_24_1.png)
    



```python
f.get_best()
```




    {'rayleigh': {'loc': 0.11816185533329944, 'scale': 0.0659609105394196}}


