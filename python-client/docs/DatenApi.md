# marktstammdaten.DatenApi

All URIs are relative to *https://www.marktstammdatenregister.de/MaStR*

Method | HTTP request | Description
------------- | ------------- | -------------
[**einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get**](DatenApi.md#einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get) | **GET** /Einheit/EinheitJson/GetErweiterteOeffentlicheEinheitStromerzeugung | Erweiterte öffentliche Daten zur Stromerzeugung


# **einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get**
> EinheitEinheitJsonGetErweiterteOeffentlicheEinheitStromerzeugungGet200Response einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get()

Erweiterte öffentliche Daten zur Stromerzeugung

### Example


```python
import time
from deutschland import marktstammdaten
from deutschland.marktstammdaten.api import daten_api
from deutschland.marktstammdaten.model.einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get200_response import EinheitEinheitJsonGetErweiterteOeffentlicheEinheitStromerzeugungGet200Response
from pprint import pprint
# Defining the host is optional and defaults to https://www.marktstammdatenregister.de/MaStR
# See configuration.py for a list of all supported configuration parameters.
configuration = marktstammdaten.Configuration(
    host = "https://www.marktstammdatenregister.de/MaStR"
)


# Enter a context with an instance of the API client
with marktstammdaten.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = daten_api.DatenApi(api_client)
    sort = "sort_example" # str | Spalte, nach der auf- oder absteigend sortiert werden soll (optional)
    page = 1 # int | Seite, die geladen werden soll (optional)
    page_size = 1 # int | Anzahl an Einträgen pro Seite (optional)
    filter = "filter_example" # str | Syntax: Feld-name~[eq|neq|sw|ct|nct|ew|null|nn]~'Wert'~[and|or]~... (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Erweiterte öffentliche Daten zur Stromerzeugung
        api_response = api_instance.einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get(sort=sort, page=page, page_size=page_size, filter=filter)
        pprint(api_response)
    except marktstammdaten.ApiException as e:
        print("Exception when calling DatenApi->einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Spalte, nach der auf- oder absteigend sortiert werden soll | [optional]
 **page** | **int**| Seite, die geladen werden soll | [optional]
 **page_size** | **int**| Anzahl an Einträgen pro Seite | [optional]
 **filter** | **str**| Syntax: Feld-name~[eq|neq|sw|ct|nct|ew|null|nn]~&#39;Wert&#39;~[and|or]~... | [optional]

### Return type

[**EinheitEinheitJsonGetErweiterteOeffentlicheEinheitStromerzeugungGet200Response**](EinheitEinheitJsonGetErweiterteOeffentlicheEinheitStromerzeugungGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Liste Stromerzeuger |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

