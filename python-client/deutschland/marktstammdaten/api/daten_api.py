"""
    Marktdatenstammregister API

    Das MaStR führt die Stammdaten zu Strom- und Gaserzeugungsanlagen sowie Marktakteuren wie Anlagenbetreibern, Netzbetreibern und Energielieferanten.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.marktstammdaten.api_client import ApiClient
from deutschland.marktstammdaten.api_client import Endpoint as _Endpoint
from deutschland.marktstammdaten.model.einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get200_response import (
    EinheitEinheitJsonGetErweiterteOeffentlicheEinheitStromerzeugungGet200Response,
)
from deutschland.marktstammdaten.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class DatenApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get_endpoint = _Endpoint(
            settings={
                "response_type": (
                    EinheitEinheitJsonGetErweiterteOeffentlicheEinheitStromerzeugungGet200Response,
                ),
                "auth": [],
                "endpoint_path": "/Einheit/EinheitJson/GetErweiterteOeffentlicheEinheitStromerzeugung",
                "operation_id": "einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "sort",
                    "page",
                    "page_size",
                    "filter",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [
                    "page",
                    "page_size",
                ],
            },
            root_map={
                "validations": {
                    ("page",): {
                        "inclusive_minimum": 1,
                    },
                    ("page_size",): {
                        "inclusive_minimum": 1,
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "sort": (str,),
                    "page": (int,),
                    "page_size": (int,),
                    "filter": (str,),
                },
                "attribute_map": {
                    "sort": "sort",
                    "page": "page",
                    "page_size": "pageSize",
                    "filter": "filter",
                },
                "location_map": {
                    "sort": "query",
                    "page": "query",
                    "page_size": "query",
                    "filter": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get(
        self, **kwargs
    ):
        """Erweiterte öffentliche Daten zur Stromerzeugung  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            sort (str): Spalte, nach der auf- oder absteigend sortiert werden soll. [optional]
            page (int): Seite, die geladen werden soll. [optional]
            page_size (int): Anzahl an Einträgen pro Seite. [optional]
            filter (str): Syntax: Feld-name~[eq|neq|sw|ct|nct|ew|null|nn]~'Wert'~[and|or]~.... [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EinheitEinheitJsonGetErweiterteOeffentlicheEinheitStromerzeugungGet200Response
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["_request_auths"] = kwargs.get("_request_auths", None)
        return self.einheit_einheit_json_get_erweiterte_oeffentliche_einheit_stromerzeugung_get_endpoint.call_with_http_info(
            **kwargs
        )
