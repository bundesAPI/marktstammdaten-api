# marktstammdaten.FilterApi

All URIs are relative to *https://www.marktstammdatenregister.de/MaStR*

Method | HTTP request | Description
------------- | ------------- | -------------
[**einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gaserzeugung_get**](FilterApi.md#einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gaserzeugung_get) | **GET** /Einheit/EinheitJson/GetFilterColumnsErweiterteOeffentlicheEinheitGaserzeugung | Filter für erweiterte Gaserzeugung abfragen
[**einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gasverbrauch_get**](FilterApi.md#einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gasverbrauch_get) | **GET** /Einheit/EinheitJson/GetFilterColumnsErweiterteOeffentlicheEinheitGasverbrauch | Filter für erweiterten Gasverbrauch abfragen
[**einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromerzeugung_get**](FilterApi.md#einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromerzeugung_get) | **GET** /Einheit/EinheitJson/GetFilterColumnsErweiterteOeffentlicheEinheitStromerzeugung | Filter für erweiterte Stromerzeugung abfragen
[**einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromverbrauch_get**](FilterApi.md#einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromverbrauch_get) | **GET** /Einheit/EinheitJson/GetFilterColumnsErweiterteOeffentlicheEinheitStromverbrauch | Filter für erweiterten Stromverbrauch abfragen


# **einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gaserzeugung_get**
> [Filter] einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gaserzeugung_get()

Filter für erweiterte Gaserzeugung abfragen

### Example


```python
import time
from deutschland import marktstammdaten
from deutschland.marktstammdaten.api import filter_api
from deutschland.marktstammdaten.model.filter import Filter
from pprint import pprint
# Defining the host is optional and defaults to https://www.marktstammdatenregister.de/MaStR
# See configuration.py for a list of all supported configuration parameters.
configuration = marktstammdaten.Configuration(
    host = "https://www.marktstammdatenregister.de/MaStR"
)


# Enter a context with an instance of the API client
with marktstammdaten.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = filter_api.FilterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Filter für erweiterte Gaserzeugung abfragen
        api_response = api_instance.einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gaserzeugung_get()
        pprint(api_response)
    except marktstammdaten.ApiException as e:
        print("Exception when calling FilterApi->einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gaserzeugung_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Filter]**](Filter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Liste möglicher Filter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gasverbrauch_get**
> [Filter] einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gasverbrauch_get()

Filter für erweiterten Gasverbrauch abfragen

### Example


```python
import time
from deutschland import marktstammdaten
from deutschland.marktstammdaten.api import filter_api
from deutschland.marktstammdaten.model.filter import Filter
from pprint import pprint
# Defining the host is optional and defaults to https://www.marktstammdatenregister.de/MaStR
# See configuration.py for a list of all supported configuration parameters.
configuration = marktstammdaten.Configuration(
    host = "https://www.marktstammdatenregister.de/MaStR"
)


# Enter a context with an instance of the API client
with marktstammdaten.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = filter_api.FilterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Filter für erweiterten Gasverbrauch abfragen
        api_response = api_instance.einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gasverbrauch_get()
        pprint(api_response)
    except marktstammdaten.ApiException as e:
        print("Exception when calling FilterApi->einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_gasverbrauch_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Filter]**](Filter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Liste möglicher Filter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromerzeugung_get**
> [Filter] einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromerzeugung_get()

Filter für erweiterte Stromerzeugung abfragen

### Example


```python
import time
from deutschland import marktstammdaten
from deutschland.marktstammdaten.api import filter_api
from deutschland.marktstammdaten.model.filter import Filter
from pprint import pprint
# Defining the host is optional and defaults to https://www.marktstammdatenregister.de/MaStR
# See configuration.py for a list of all supported configuration parameters.
configuration = marktstammdaten.Configuration(
    host = "https://www.marktstammdatenregister.de/MaStR"
)


# Enter a context with an instance of the API client
with marktstammdaten.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = filter_api.FilterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Filter für erweiterte Stromerzeugung abfragen
        api_response = api_instance.einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromerzeugung_get()
        pprint(api_response)
    except marktstammdaten.ApiException as e:
        print("Exception when calling FilterApi->einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromerzeugung_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Filter]**](Filter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Liste möglicher Filter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromverbrauch_get**
> [Filter] einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromverbrauch_get()

Filter für erweiterten Stromverbrauch abfragen

### Example


```python
import time
from deutschland import marktstammdaten
from deutschland.marktstammdaten.api import filter_api
from deutschland.marktstammdaten.model.filter import Filter
from pprint import pprint
# Defining the host is optional and defaults to https://www.marktstammdatenregister.de/MaStR
# See configuration.py for a list of all supported configuration parameters.
configuration = marktstammdaten.Configuration(
    host = "https://www.marktstammdatenregister.de/MaStR"
)


# Enter a context with an instance of the API client
with marktstammdaten.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = filter_api.FilterApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Filter für erweiterten Stromverbrauch abfragen
        api_response = api_instance.einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromverbrauch_get()
        pprint(api_response)
    except marktstammdaten.ApiException as e:
        print("Exception when calling FilterApi->einheit_einheit_json_get_filter_columns_erweiterte_oeffentliche_einheit_stromverbrauch_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Filter]**](Filter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Liste möglicher Filter |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

