# shopping-cart
Shopping cart backend application

Run the following command to build the docker images and start the containers:
```
docker-compose up -d --build
```

This will start the two services. Go to the following url to access the docs and endpoints:
```
http://localhost:8004
```

I used pytest so the tests can be run by running the following command from the root directory:
```
pytest
```


Didn't have time to properly write the last two test cases. Implemented the update_cart endpoint but did not properly have it handle removing quantity of a specific item. It currently adds to the existing quantity only.

Based on the 4 things a user should be able to do, I did not implement the ability to remove an item so the last two test cases can't be tested. Ideally would've implemented these but didn't want to spend too much time before sending this in. 

The docker-compose file has some hard coded values that would normally be put into env files to handle different deployments, from dev, testing, prod.  

Lastly implementing the github actions pipelines for building and testing to have a proper setup. 