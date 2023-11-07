# AssetReportAddOns

A list of add-ons that should be included in the Asset Report.

`fast_assets`: When Fast Assets is requested, Plaid will create two versions of the Asset Report: the Fast Asset Report, which will contain only Identity and Balance information, and the Full Asset Report, which will also contain Transactions information. A `PRODUCT_READY` webhook will be fired for each Asset Report when it is ready, and the `report_type` field will indicate whether the webhook is firing for the `full` or `fast` Asset Report. To retrieve the Fast Asset Report, call `/asset_report/get` with `fast_report` set to `true`. There is no additional charge for using Fast Assets.

`investments`: Request an Asset Report with Investments. This add-on is in closed beta and not generally available.


## Values

| Name          | Value         |
| ------------- | ------------- |
| `INVESTMENTS` | investments   |
| `FAST_ASSETS` | fast_assets   |