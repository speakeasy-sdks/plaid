# SelfieAnalysis

High level descriptions of how the associated selfie was processed. If a selfie fails verification, the details in the `analysis` object should help clarify why the selfie was rejected.


## Fields

| Field                                                                                                        | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `document_comparison`                                                                                        | [components.SelfieAnalysisDocumentComparison](../../models/components/selfieanalysisdocumentcomparison.md)   | :heavy_check_mark:                                                                                           | Information about the comparison between the selfie and the document (if documentary verification also ran). |
| `additional_properties`                                                                                      | Dict[str, *Any*]                                                                                             | :heavy_minus_sign:                                                                                           | N/A                                                                                                          |