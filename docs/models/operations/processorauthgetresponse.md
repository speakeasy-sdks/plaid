# ProcessorAuthGetResponse


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                       | *str*                                                                                                | :heavy_check_mark:                                                                                   | HTTP response content type for this operation                                                        |
| `processor_auth_get_response`                                                                        | [Optional[components.ProcessorAuthGetResponse]](../../models/components/processorauthgetresponse.md) | :heavy_minus_sign:                                                                                   | success                                                                                              |
| `status_code`                                                                                        | *int*                                                                                                | :heavy_check_mark:                                                                                   | HTTP response status code for this operation                                                         |
| `raw_response`                                                                                       | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                | :heavy_check_mark:                                                                                   | Raw HTTP response; suitable for custom response parsing                                              |