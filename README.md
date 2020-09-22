# Michael Hoffmann Fetch Rewards Coding Exercise - Backend Software Engineering
Submission 9/22

&nbsp;

### Prerequisites 
* Docker

&nbsp;

### **Running the Web Service**

1. Clone the repo
2. Navigate to cloned folder in terminal
3. Inside of fetchrewards/ folder run the command docker-compose up in to start the web service

### **Usage**

The web service expose only one endpoint -- /fetchrewards which accepts two string arguments *string1* and *string2*

The string arguments may either be sent in a dictionary through the *params* parameter with requests.get() using keys *string1* and *string2* or through the url *localhost:5000/fetchrewards/?string1={yourValueForString1}&string2={yourValueForString2}*


### Examples using Python

#### Example using requests.get()

```
URL = 'http://localhost:5000/fetchrewards/'
PARAMS = {"string1": "1.0.0", "string2": "1.0.1"}
r = requests.get(URL, params=PARAMS)
```

#### Example using url 

Either use requests library

```
URL = 'http://localhost:5000/fetchrewards/fetchrewards?string1=1.0.0&string2=1.0.1'
r = requests.get(URL)
```

or in browser just navigate straight to endpoint

http://localhost:5000/fetchrewards/fetchrewards?string1=1.0.0&string2=1.0.1




