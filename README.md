# Python_library
Created a custom Python library

#steps to run the repository 
Step 1: install requirements.txt with the following command -
```pip install -r /path/to/requirements.txt```

Step 2: Run the setup.py file with the command -
```python setup.py pytest```

Step 3: Build your library using the command -
```python setup.py bdist_wheel```

Step 4: The wheel file is stored in the “dist” folder that is now created. And can be installed using command -
```pip install /path/to/wheelfile.whl```

And once you have installed your Python library we can use it like normal use like -
``` 
import AI_lib
from AI_lib import aifunction 
```
