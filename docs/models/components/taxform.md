# Taxform

Data about an official document used to report the user's income to the IRS.


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `document_type`                                                           | *str*                                                                     | :heavy_check_mark:                                                        | The type of tax document. Currently, the only supported value is `w2`.    |
| `additional_properties`                                                   | Dict[str, *Any*]                                                          | :heavy_minus_sign:                                                        | N/A                                                                       |
| `doc_id`                                                                  | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | An identifier of the document referenced by the document metadata.        |
| `w2`                                                                      | [Optional[components.W2]](../../models/components/w2.md)                  | :heavy_minus_sign:                                                        | W2 is an object that represents income data taken from a W2 tax document. |