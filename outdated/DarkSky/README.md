This project uses the [Dark Sky API](https://darksky.net/dev). To use this project,
create an account with Dark Sky and obtain a secret key that grants access to
the API. Then, create a **key.id** file with the the secret key and the coordinates
of the area the project can obtain the weather forecast. See example below.

## Example ##
```
[darksky]
key=1234567890abcdef1234567890abcdef
lat=37.8267
lon=-122.4233
http=[USERNAME]:[PASSWORD]@[PROXY_SERVER]:[PORT]
https=[USERNAME]:[PASSWORD]@[PROXY_SERVER]:[PORT]
```

#### References ####
* [Latitude and Longitude](https://www.latlong.net/)
