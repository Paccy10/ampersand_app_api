# Ampersand App API

This app is the the API for an electric motocycles company that enables calculating the driver total energy and distance used.

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

```
- Python 3.8.2
- pip
- pipenv
- Postgres
```

## Installation and setup

- Download Python

```
https://www.python.org/downloads/
```

- Download Postgres

```
https://www.postgresql.org/download/
```

- Install pip

```
https://pip.pypa.io/en/stable/installing/
```

- Install pipenv

```
pip install pipenv
```

- Clone the repository

```
git clone https://github.com/Paccy10/olympus-api.git
```

- Make a copy of the .env.sample file and rename it to .env and update the variables accordingly

- Apply migrations

```
flask db upgrade
```

- Should you make changes to the database models, run migrations as follows

  - Migrate database

  ```
  flask db migrate
  ```

  - Upgrade to the new structure

  ```
  flask db upgrade
  ```

## Running

- Running app

```
flask run
```

## Endpoints

- Create Motorcycle

```
request: POST /motorcycles

body: {"serial_number": "motocycle1"}
```

- Get all Motorcycles

```
request: GET /motorcycles
```

- Create Driver

```
request: POST /drivers

body: {
  "name": "Pacifique Ndayisenga",
  "license_number": "23343567789",
  "motorcycle_id": 1
}
```

- Get all Drivers

```
request: GET /drivers
```

- Create Battery

```
request: POST /batteries

body: {
  "serial_number": "battery1",
  "capacity": 345.0,
  "energy_level": 345.0
}
```

- Get all Batteries

```
request: GET /batteries
```

- Create Station

```
request: POST /stations

body: {
  "location": "Kacyiru",
  "number_of_batteries": 50,
}
```

- Get all Stations

```
request: GET /stations
```

- Create Swap

```
request: POST /swaps

body: {
  "station_d": 1,
  "driver_id": 1,
  "odometer": 100,
  "old_battery": {
    "id": 1,
    "energy_level": 10
  },
  "new_battery: {
    "id": 2,
    "energy_level": 345.0
  }
}
```

- Get all Swaps

```
request: GET /swaps
```

- Get driver's Swaps

```
request: GET /drivers/<driver_id>/swaps
```
