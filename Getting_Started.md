# Getting Satrted with API.

In this tutorial we will learn how to use tvarit_api python client for web integration.

### Installation
Install the pip package:

    pip install -U tvarit_api
**Requirement** : You need either 2nd or 3rd version of Python and only the requests library installed.

### Connecting and Authenticating to API client
```sh
from tvarit_api import Tvarit
import json

username = "your tvarit username"
password = "your tvarit password"
host = "provided by tvarit"
port = "provided by tvarit"
protocol = "http/https"

tvarit_api = Tvarit(
    auth=(username,password),
    host=host,
    port = port,
    protocol = protocol
    )
```

### Creating a Datasource
Read the [Data Source API]() document to get a basic overview of Data source APIs. For this tutorial, we will use Cars_Assembly_Line data and datasource type of influx db.
```sh
datasource = {
    'access': 'proxy',
    'database': 'demo',
    'files': {},
    'jsonData': {'keepCookies': []},
    'name': 'Cars_Assembly_Line',
    'password': 'influx-password',
    'secureJsonData': {},
    'secureJsonFields': {},
    'type': 'influxdb',
    'url': 'http://influx.tvarit.com:8086/',
    'user': 'demo'
    }

tvarit_api.datasource.create_datasource(datasource)
```

### Create Machine
```sh
machine = {
	'fetch': {
	       'sources': [{'datasource': {'database': 'demo',
	                                   'id': 0,
	                                   'name': 'Cars_Assembly_Line',
	                                   'readOnly': False,
	                                   'type': 'influxdb',
	                                   'url': '/api/datasources/proxy/9'},
	                    'json_data': {'IsNew': True,
	                                  'datasource': 'Cars_Assembly_Line',
	                                  'groupBy': [],
	                                  'measurement': 'Sample',
	                                  'orderByTime': 'ASC',
	                                  'policy': 'default',
	                                  'query': 'SELECT * FROM "Sample" WHERE '
	                                           '$timeFilter',
	                                  'resultFormat': 'table',
	                                  'select': [[{'params': ['*'],
	                                               'type': 'field'}]],
	                                  },
	                    'query': 'SELECT * FROM "Sample" WHERE $timeFilter',
	                    'tag': 'A'}]},
	'flags': {'batch': False},
	'json_data': {},
	'model': {'id': 0, 'name': ''},
	'name': 'Cars_Assembly_Line'
}
tvarit_api.machine.create_machine(machine)
```

### Configure Parameters
```sh
parameters = [
  {
    "model": {
      "id": 0
    },
    "is_forecastable": true,
    "aggregation": {
      "method": "mean"
    },
    "interpolation": {
      "method": "linear"
    },
    "id": 0,
    "name": "Sample_encoder_position",
    "type": "number",
  },
  {
    "model": {
      "id": 0,
      "name": "Cars_Assembly_Line"
    },
    "is_forecastable": true,
    "aggregation": {
      "method": "mean"
    },
    "interpolation": {
      "method": "linear"
    },
    "id": 1,
    "name": "Sample_rotor_speed",
    "type": "number",
  },
  {
    "model": {
      "id": 0,
      "name": "Cars_Assembly_Line"
    },
    "is_forecastable": true,
    "aggregation": {
      "method": "mode"
    },
    "interpolation": {
      "method": "nearest"
    },
    "classes": [
      "0.0",
      "1.0"
    ],
    "created": "2019-09-19T06:28:56Z",
    "id": 2,
    "name": "Sample_shutdown_occured",
    "type": "binary",
  },
  {
    "model": {
      "id": 0,
      "name": "Cars_Assembly_Line"
    },
    "is_forecastable": true,
    "aggregation": {
      "method": "mean"
    },
    "interpolation": {
      "method": "linear"
    },
    "id": 3,
    "name": "Sample_spot_welding_temperature",
    "type": "number",
  }
]

tvarit_api.parameter.upload_parameter_json(
                                        model_id=3,
                                        parameters=json.dumps(parameters)
                                    )
```

### Configure Pipeline
```sh
pipelines = [{
  'data': '[\n'
          '  PrintScope(),\n'
          '  LoadMachines(),\n'
          '  LoadParameters(),\n'
          '  Authenticate(),\n'
          '  IterateOverMachines([\n'
          '    Read(),\n'
          "    FeatureSelection(algorithm='boruta', labels_only=True),\n"
          '    Write(),\n'
          '    CreateSnapshot(),\n'
          '  ]),\n'
          ']',
  'description': '',
  'id': 5,
  'name': 'feature_selection',
  'type': 'analyse',
},
 {'data': '[\n'
          '  PrintScope(),\n'
          '  LoadMachines(),\n'
          '  LoadParameters(),\n'
          '  Authenticate(),\n'
          '  IterateOverMachines([\n'
          '    Read(),\n'
          '    Preprocess(),\n'
          '    Write(),\n'
          '    CreateSnapshot(),\n'
          '  ]),\n'
          ']',
  'description': '',
  'id': 1,
  'name': 'fetch',
  'type': 'fetch',
},
 {'data': '[\n'
          '  PrintScope(),\n'
          '  LoadMachines(),\n'
          '  LoadParameters(),\n'
          '  Authenticate(),\n'
          '  IterateOverMachines([\n'
          '    Read(),\n'
          '    Fit(),\n'
          '    Write(),\n'
          '    CreateSnapshot(),\n'
          '  ]),\n'
          ']',
  'description': '',
  'id': 3,
  'name': 'fit',
  'type': 'fit',
},
 {'data': '[\n'
          '  PrintScope(),\n'
          '  LoadMachines(),\n'
          '  LoadParameters(),\n'
          '  Authenticate(),\n'
          '  IterateOverMachines([\n'
          '    Read(),\n'
          '    GuessParametersDataType(),\n'
          '    Write(),\n'
          '  ]),\n'
          ']',
  'description': '',
  'id': 6,
  'name': 'guess',
  'type': 'fetch',
},
 {'data': '[\n'
          '  PrintScope(),\n'
          '  LoadMachines(),\n'
          '  LoadParameters(),\n'
          '  Authenticate(),\n'
          '  IterateOverMachines([\n'
          '    Read(),\n'
          '    Predict(),\n'
          '    Write(),\n'
          '    CreateSnapshot(),\n'
          '  ]),\n'
          ']',
  'description': '',
  'id': 4,
  'name': 'predict',
  'type': 'predict',
},
 {'data': '[\n'
          '  PrintScope(),\n'
          '  LoadMachines(),\n'
          '  LoadParameters(),\n'
          '  Authenticate(),\n'
          '  IterateOverMachines([\n'
          '    Read(),\n'
          '    Tune(),\n'
          '    Write(),\n'
          '  ]),\n'
          ']',
  'description': '',
  'id': 2,
  'name': 'tune',
  'type': 'tune',
}]

tvarit_api.pipeline.upload_pipeline_json(pipelines = json.dumps(pipelines))
```

### Configure Tasks
```sh
tasks = [{'description': '',
  'end': 'now',
  'id': 1,
  'labels': [],
  'max_evals': 500,
  'name': 'FeatureSelection',
  'pipelines': [{'description': '', 'id': 1, 'name': 'fetch', 'type': 'fetch'},
                {'description': '',
                 'id': 5,
                 'name': 'feature_selection',
                 'type': 'analyse'}],
  'start': 'now-2y',
  'test_fraction': 0.1,
  'test_size': 0.1,
  },
 {'description': '',
  'end': 'now',
  'id': 2,
  'labels': [],
  'max_evals': 500,
  'name': 'Predict',
  'pipelines': [{'description': '', 'id': 1, 'name': 'fetch', 'type': 'fetch'},
                {'description': '',
                 'id': 4,
                 'name': 'predict',
                 'type': 'predict'}],
  'start': 'now-2y',
  'test_fraction': 0.1,
  'test_size': 0.1,
  },
 {'description': '',
  'end': 'now',
  'id': 3,
  'labels': [],
  'max_evals': 500,
  'name': 'Retrain',
  'pipelines': [{'description': '', 'id': 1, 'name': 'fetch', 'type': 'fetch'},
                {'description': '', 'id': 3, 'name': 'fit', 'type': 'fit'}],
  'start': 'now-2y',
  'test_fraction': 0.1,
  'test_size': 0.1,
  },
 {'description': '',
  'end': '2019-05-20T07:58:32.281Z',
  'id': 4,
  'labels': [],
  'max_evals': 500,
  'name': 'Train',
  'pipelines': [{'description': '', 'id': 2, 'name': 'fetch', 'type': 'fetch'},
                {'description': '', 'id': 6, 'name': 'tune', 'type': 'tune'},
                {'description': '', 'id': 3, 'name': 'fit', 'type': 'fit'}],
  'start': 'now-2y',
  'test_fraction': 0.1,
  'test_size': 0.1,
  }]

tvarit_api.pipeline.upload_task_json(tasks = json.dumps(tasks))
```
  
### Train Model and Get Evaluation Scores
```sh
train_job = {
 'description': 'Sample train task',
 'end': 'now',
 'id': 1,
 'labels': [{'id': 2,
             'machine': {'id': 0, 'name': 'Cars_Assembly_Line'},
             'model': {'id': 0, 'name': 'Cars_Assembly_Line'},
             'name': 'Sample_shutdown_occured'}],
 'labels_only': False,
 'max_evals': 500,
 'name': '-- Train --',
 'pipelines': [{'description': '',
                'id': 1,
                'name': '-- fetch --',
                'type': 'fetch'},
               {'description': '',
                'id': 2,
                'name': '-- tune --',
                'type': 'tune'},
               {'description': '',
                'id': 3,
                'name': '-- fit --',
                'type': 'fit'}],
 'start': 'now-2y',
 'test_size': 0.1}

tvarit_api.job.run_job(job = json.dumps(train_job))

evaluation_scores = tvarit_api.output.get_scores(
                                            machine = "Cars_Assembly_Line", 
                                            label = "Sample_shutdown_occured"
                                            )
```

### Get Predictions
```sh
predict_job = {
 'description': 'Sample predict task',
 'end': 'now',
 'id': 3,
 'labels': [{'id': 2,
             'machine': {'id': 0, 'name': 'Cars_Assembly_Line'},
             'model': {'id': 0, 'name': 'Cars_Assembly_Line'},
             'name': 'Sample_shutdown_occured'}],
 'max_evals': 500,
 'name': '-- Predict --',
 'pipelines': [{'description': '',
                'id': 1,
                'name': '-- fetch --',
                'type': 'fetch'},
               {'description': '',
                'id': 4,
                'name': '-- predict --',
                'type': 'predict'}],
 'start': 'now-6m',
 'test_size': 0.1}

tvarit_api.job.run_job(job = json.dumps(predict_job))

predictions = tvarit_api.output.get_predictions(
                                            machine = "Cars_Assembly_Line", 
                                            label = "Sample_shutdown_occured"
                                            )
```

### Get Dependencies
```sh
dependencies = tvarit_api.output.get_features(
                                            machine = "Cars_Assembly_Line", 
                                            label = "Sample_shutdown_occured"
                                            )
```


