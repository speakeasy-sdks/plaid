<!-- Start SDK Example Usage [usage] -->
```python
import plaid
from plaid.models import components

s = plaid.Plaid(
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.AccountsBalanceGetRequest(
    access_token='<value>',
)

res = s.plaid.accounts_balance_get(req)

if res.accounts_get_response is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->