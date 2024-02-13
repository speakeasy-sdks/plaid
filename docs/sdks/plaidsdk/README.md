# PlaidSDK
(*plaid*)

## Overview

The Plaid API

### Available Operations

* [accounts_balance_get](#accounts_balance_get) - Retrieve real-time balance data
* [accounts_get](#accounts_get) - Retrieve accounts
* [application_get](#application_get) - Retrieve information about a Plaid application
* [asset_report_audit_copy_create](#asset_report_audit_copy_create) - Create Asset Report Audit Copy
* [asset_report_audit_copy_get](#asset_report_audit_copy_get) - Retrieve an Asset Report Audit Copy
* [asset_report_audit_copy_remove](#asset_report_audit_copy_remove) - Remove Asset Report Audit Copy
* [asset_report_create](#asset_report_create) - Create an Asset Report
* [asset_report_filter](#asset_report_filter) - Filter Asset Report
* [asset_report_get](#asset_report_get) - Retrieve an Asset Report
* [asset_report_pdf_get](#asset_report_pdf_get) - Retrieve a PDF Asset Report
* [asset_report_refresh](#asset_report_refresh) - Refresh an Asset Report
* [asset_report_remove](#asset_report_remove) - Delete an Asset Report
* [auth_get](#auth_get) - Retrieve auth data
* [bank_transfer_balance_get](#bank_transfer_balance_get) - Get balance of your Bank Transfer account
* [bank_transfer_cancel](#bank_transfer_cancel) - Cancel a bank transfer
* [bank_transfer_create](#bank_transfer_create) - Create a bank transfer
* [bank_transfer_event_list](#bank_transfer_event_list) - List bank transfer events
* [bank_transfer_event_sync](#bank_transfer_event_sync) - Sync bank transfer events
* [bank_transfer_get](#bank_transfer_get) - Retrieve a bank transfer
* [bank_transfer_list](#bank_transfer_list) - List bank transfers
* [bank_transfer_migrate_account](#bank_transfer_migrate_account) - Migrate account into Bank Transfers
* [bank_transfer_sweep_get](#bank_transfer_sweep_get) - Retrieve a sweep
* [bank_transfer_sweep_list](#bank_transfer_sweep_list) - List sweeps
* [base_report_get](#base_report_get) - Retrieve a Base Report
* [beacon_report_create](#beacon_report_create) - Create a Beacon Report
* [beacon_user_create](#beacon_user_create) - Create a Beacon User
* [beacon_user_get](#beacon_user_get) - Get a Beacon User
* [categories_get](#categories_get) - Get categories
* [cra_bank_income_get](#cra_bank_income_get) - Retrieve information from the bank accounts used for income verification
* [~~create_payment_token~~](#create_payment_token) - Create payment token :warning: **Deprecated**
* [credit_asset_report_freddie_mac_get](#credit_asset_report_freddie_mac_get) - Retrieve an Asset Report with Freddie Mac format. Only Freddie Mac can use this endpoint.
* [credit_audit_copy_token_create](#credit_audit_copy_token_create) - Create Asset or Income Report Audit Copy Token
* [credit_audit_copy_token_update](#credit_audit_copy_token_update) - Update an Audit Copy Token
* [credit_bank_employment_get](#credit_bank_employment_get) - Retrieve information from the bank accounts used for employment verification
* [credit_bank_income_get](#credit_bank_income_get) - Retrieve information from the bank accounts used for income verification
* [credit_bank_income_pdf_get](#credit_bank_income_pdf_get) - Retrieve information from the bank accounts used for income verification in PDF format
* [credit_bank_income_refresh](#credit_bank_income_refresh) - Refresh a user's bank income information
* [credit_bank_income_webhook_update](#credit_bank_income_webhook_update) - Subscribe and unsubscribe to proactive notifications for a user's income profile
* [credit_bank_statements_uploads_get](#credit_bank_statements_uploads_get) - Retrieve data for a user's uploaded bank statements
* [credit_employment_get](#credit_employment_get) - Retrieve a summary of an individual's employment information
* [credit_freddie_mac_reports_get](#credit_freddie_mac_reports_get) - Retrieve an Asset Report with Freddie Mac format (aka VOA - Verification Of Assets), and a Verification Of Employment (VOE) report if this one is available. Only Freddie Mac can use this endpoint.
* [credit_payroll_income_get](#credit_payroll_income_get) - Retrieve a user's payroll information
* [credit_payroll_income_precheck](#credit_payroll_income_precheck) - Check income verification eligibility and optimize conversion
* [credit_payroll_income_refresh](#credit_payroll_income_refresh) - Refresh a digital payroll income verification
* [credit_payroll_income_risk_signals_get](#credit_payroll_income_risk_signals_get) - Retrieve fraud insights for a user's manually uploaded document(s).
* [credit_relay_create](#credit_relay_create) - Create a relay token to share an Asset Report with a partner client (beta)
* [credit_relay_get](#credit_relay_get) - Retrieve the reports associated with a relay token that was shared with you (beta)
* [credit_relay_pdf_get](#credit_relay_pdf_get) - Retrieve the pdf reports associated with a relay token that was shared with you (beta)
* [credit_relay_refresh](#credit_relay_refresh) - Refresh a report of a relay token (beta)
* [credit_relay_remove](#credit_relay_remove) - Remove relay token (beta)
* [credit_report_audit_copy_remove](#credit_report_audit_copy_remove) - Remove an Audit Copy token
* [credit_sessions_get](#credit_sessions_get) - Retrieve Link sessions for your user
* [dashboard_user_get](#dashboard_user_get) - Retrieve a dashboard user
* [dashboard_user_list](#dashboard_user_list) - List dashboard users
* [deposit_switch_alt_create](#deposit_switch_alt_create) - Create a deposit switch without using Plaid Exchange
* [deposit_switch_create](#deposit_switch_create) - Create a deposit switch
* [deposit_switch_get](#deposit_switch_get) - Retrieve a deposit switch
* [deposit_switch_token_create](#deposit_switch_token_create) - Create a deposit switch token
* [employers_search](#employers_search) - Search employer database
* [~~employment_verification_get~~](#employment_verification_get) - (Deprecated) Retrieve a summary of an individual's employment information :warning: **Deprecated**
* [fdx_notifications](#fdx_notifications) - Webhook receiver for fdx notifications
* [identity_get](#identity_get) - Retrieve identity data
* [identity_match](#identity_match) - Retrieve identity match score
* [identity_refresh](#identity_refresh) - Refresh identity data
* [identity_verification_create](#identity_verification_create) - Create a new identity verification
* [identity_verification_get](#identity_verification_get) - Retrieve Identity Verification
* [identity_verification_list](#identity_verification_list) - List Identity Verifications
* [identity_verification_retry](#identity_verification_retry) - Retry an Identity Verification
* [~~income_verification_create~~](#income_verification_create) - (Deprecated) Create an income verification instance :warning: **Deprecated**
* [~~income_verification_documents_download~~](#income_verification_documents_download) - (Deprecated) Download the original documents used for income verification :warning: **Deprecated**
* [~~income_verification_paystubs_get~~](#income_verification_paystubs_get) - (Deprecated) Retrieve information from the paystubs used for income verification :warning: **Deprecated**
* [~~income_verification_precheck~~](#income_verification_precheck) - (Deprecated) Check digital income verification eligibility and optimize conversion :warning: **Deprecated**
* [~~income_verification_taxforms_get~~](#income_verification_taxforms_get) - (Deprecated) Retrieve information from the tax documents used for income verification :warning: **Deprecated**
* [institutions_get](#institutions_get) - Get details of all supported institutions
* [institutions_get_by_id](#institutions_get_by_id) - Get details of an institution
* [institutions_search](#institutions_search) - Search institutions
* [investments_auth_get](#investments_auth_get) - Get data needed to authorize an investments transfer
* [investments_holdings_get](#investments_holdings_get) - Get Investment holdings
* [investments_refresh](#investments_refresh) - Refresh investment data
* [investments_transactions_get](#investments_transactions_get) - Get investment transactions
* [item_access_token_invalidate](#item_access_token_invalidate) - Invalidate access_token
* [item_activity_list](#item_activity_list) - List a historical log of user consent events
* [item_application_list](#item_application_list) - List a user’s connected applications
* [item_application_scopes_update](#item_application_scopes_update) - Update the scopes of access for a particular application
* [item_create_public_token](#item_create_public_token) - Create public token
* [item_get](#item_get) - Retrieve an Item
* [item_import](#item_import) - Import Item
* [item_public_token_exchange](#item_public_token_exchange) - Exchange public token for an access token
* [item_remove](#item_remove) - Remove an Item
* [item_webhook_update](#item_webhook_update) - Update Webhook URL
* [liabilities_get](#liabilities_get) - Retrieve Liabilities data
* [link_delivery_create](#link_delivery_create) - Create Hosted Link session
* [link_delivery_get](#link_delivery_get) - Get Hosted Link session
* [link_oauth_correlation_id_exchange](#link_oauth_correlation_id_exchange) - Exchange the Link Correlation Id for a Link Token
* [link_token_create](#link_token_create) - Create Link Token
* [link_token_get](#link_token_get) - Get Link Token
* [partner_customer_create](#partner_customer_create) - Creates a new end customer for a Plaid reseller.
* [partner_customer_enable](#partner_customer_enable) - Enables a Plaid reseller's end customer in the Production environment.
* [partner_customer_get](#partner_customer_get) - Returns a Plaid reseller's end customer.
* [partner_customer_oauth_institutions_get](#partner_customer_oauth_institutions_get) - Returns OAuth-institution registration information for a given end customer.
* [partner_customer_remove](#partner_customer_remove) - Removes a Plaid reseller's end customer.
* [payment_initiation_consent_create](#payment_initiation_consent_create) - Create payment consent
* [payment_initiation_consent_get](#payment_initiation_consent_get) - Get payment consent
* [payment_initiation_consent_payment_execute](#payment_initiation_consent_payment_execute) - Execute a single payment using consent
* [payment_initiation_consent_revoke](#payment_initiation_consent_revoke) - Revoke payment consent
* [payment_initiation_payment_create](#payment_initiation_payment_create) - Create a payment
* [payment_initiation_payment_get](#payment_initiation_payment_get) - Get payment details
* [payment_initiation_payment_list](#payment_initiation_payment_list) - List payments
* [payment_initiation_payment_reverse](#payment_initiation_payment_reverse) - Reverse an existing payment
* [payment_initiation_recipient_create](#payment_initiation_recipient_create) - Create payment recipient
* [payment_initiation_recipient_get](#payment_initiation_recipient_get) - Get payment recipient
* [payment_initiation_recipient_list](#payment_initiation_recipient_list) - List payment recipients
* [payment_profile_create](#payment_profile_create) - Create payment profile
* [payment_profile_get](#payment_profile_get) - Get payment profile
* [payment_profile_remove](#payment_profile_remove) - Remove payment profile
* [processor_apex_processor_token_create](#processor_apex_processor_token_create) - Create Apex bank account token
* [processor_auth_get](#processor_auth_get) - Retrieve Auth data
* [processor_balance_get](#processor_balance_get) - Retrieve Balance data
* [processor_bank_transfer_create](#processor_bank_transfer_create) - Create a bank transfer as a processor
* [processor_identity_get](#processor_identity_get) - Retrieve Identity data
* [processor_identity_match](#processor_identity_match) - Retrieve identity match score
* [processor_signal_decision_report](#processor_signal_decision_report) - Report whether you initiated an ACH transaction
* [processor_signal_evaluate](#processor_signal_evaluate) - Evaluate a planned ACH transaction
* [processor_signal_return_report](#processor_signal_return_report) - Report a return for an ACH transaction
* [processor_stripe_bank_account_token_create](#processor_stripe_bank_account_token_create) - Create Stripe bank account token
* [processor_token_create](#processor_token_create) - Create processor token
* [processor_token_permissions_get](#processor_token_permissions_get) - Get a processor token's product permissions
* [processor_token_permissions_set](#processor_token_permissions_set) - Control a processor's access to products
* [processor_token_webhook_update](#processor_token_webhook_update) - Update a processor token's webhook URL
* [processor_transactions_get](#processor_transactions_get) - Get transaction data
* [processor_transactions_recurring_get](#processor_transactions_recurring_get) - Fetch recurring transaction streams
* [processor_transactions_refresh](#processor_transactions_refresh) - Refresh transaction data
* [processor_transactions_sync](#processor_transactions_sync) - Get incremental transaction updates on a processor token
* [sandbox_bank_income_fire_webhook](#sandbox_bank_income_fire_webhook) - Manually fire a bank income webhook in sandbox
* [sandbox_bank_transfer_fire_webhook](#sandbox_bank_transfer_fire_webhook) - Manually fire a Bank Transfer webhook
* [sandbox_bank_transfer_simulate](#sandbox_bank_transfer_simulate) - Simulate a bank transfer event in Sandbox
* [sandbox_income_fire_webhook](#sandbox_income_fire_webhook) - Manually fire an Income webhook
* [sandbox_item_fire_webhook](#sandbox_item_fire_webhook) - Fire a test webhook
* [sandbox_item_reset_login](#sandbox_item_reset_login) - Force a Sandbox Item into an error state
* [sandbox_item_set_verification_status](#sandbox_item_set_verification_status) - Set verification status for Sandbox account
* [sandbox_oauth_select_accounts](#sandbox_oauth_select_accounts) - Save the selected accounts when connecting to the Platypus Oauth institution
* [sandbox_payment_profile_reset_login](#sandbox_payment_profile_reset_login) - Reset the login of a Payment Profile
* [sandbox_processor_token_create](#sandbox_processor_token_create) - Create a test Item and processor token
* [sandbox_public_token_create](#sandbox_public_token_create) - Create a test Item
* [sandbox_transfer_fire_webhook](#sandbox_transfer_fire_webhook) - Manually fire a Transfer webhook
* [sandbox_transfer_repayment_simulate](#sandbox_transfer_repayment_simulate) - Trigger the creation of a repayment
* [sandbox_transfer_simulate](#sandbox_transfer_simulate) - Simulate a transfer event in Sandbox
* [sandbox_transfer_sweep_simulate](#sandbox_transfer_sweep_simulate) - Simulate creating a sweep
* [sandbox_transfer_test_clock_advance](#sandbox_transfer_test_clock_advance) - Advance a test clock
* [sandbox_transfer_test_clock_create](#sandbox_transfer_test_clock_create) - Create a test clock
* [sandbox_transfer_test_clock_get](#sandbox_transfer_test_clock_get) - Get a test clock
* [sandbox_transfer_test_clock_list](#sandbox_transfer_test_clock_list) - List test clocks
* [signal_decision_report](#signal_decision_report) - Report whether you initiated an ACH transaction
* [signal_evaluate](#signal_evaluate) - Evaluate a planned ACH transaction
* [signal_prepare](#signal_prepare) - Opt-in an Item to Signal
* [signal_return_report](#signal_return_report) - Report a return for an ACH transaction
* [statements_download](#statements_download) - Retrieve a single statement.
* [statements_list](#statements_list) - Retrieve a list of all statements associated with the provided item.
* [transactions_enhance](#transactions_enhance) - enhance locally-held transaction data
* [transactions_enrich](#transactions_enrich) - Enrich locally-held transaction data
* [transactions_get](#transactions_get) - Get transaction data
* [transactions_recurring_get](#transactions_recurring_get) - Fetch recurring transaction streams
* [transactions_refresh](#transactions_refresh) - Refresh transaction data
* [transactions_rules_create](#transactions_rules_create) - Create transaction category rule
* [transactions_rules_list](#transactions_rules_list) - Return a list of rules created for the Item associated with the access token.
* [transactions_rules_remove](#transactions_rules_remove) - Remove transaction rule
* [transactions_sync](#transactions_sync) - Get incremental transaction updates on an Item
* [transfer_authorization_create](#transfer_authorization_create) - Create a transfer authorization
* [transfer_balance_get](#transfer_balance_get) - Retrieve a balance held with Plaid
* [transfer_cancel](#transfer_cancel) - Cancel a transfer
* [transfer_capabilities_get](#transfer_capabilities_get) - Get RTP eligibility information of a transfer
* [transfer_configuration_get](#transfer_configuration_get) - Get transfer product configuration
* [transfer_create](#transfer_create) - Create a transfer
* [transfer_diligence_document_upload](#transfer_diligence_document_upload) - This endpoint allows third-party sender customers to upload a document on behalf of its end customer (i.e. originator) to Plaid. You’ll need to send a request of type multipart/form-data.
* [transfer_diligence_submit](#transfer_diligence_submit) - Submit transfer diligence on behalf of the end customer (i.e. the originator).
* [transfer_event_list](#transfer_event_list) - List transfer events
* [transfer_event_sync](#transfer_event_sync) - Sync transfer events
* [transfer_get](#transfer_get) - Retrieve a transfer
* [transfer_intent_create](#transfer_intent_create) - Create a transfer intent object to invoke the Transfer UI
* [transfer_intent_get](#transfer_intent_get) - Retrieve more information about a transfer intent
* [transfer_ledger_get](#transfer_ledger_get) - Retrieve Plaid Ledger balance
* [transfer_list](#transfer_list) - List transfers
* [transfer_metrics_get](#transfer_metrics_get) - Get transfer product usage metrics
* [transfer_migrate_account](#transfer_migrate_account) - Migrate account into Transfers
* [transfer_originator_create](#transfer_originator_create) - Create a new originator
* [transfer_originator_get_json](#transfer_originator_get_json) - Get status of an originator's onboarding
* [transfer_originator_get_raw](#transfer_originator_get_raw) - Get status of an originator's onboarding
* [transfer_originator_list](#transfer_originator_list) - Get status of all originators' onboarding
* [transfer_questionnaire_create](#transfer_questionnaire_create) - Generate a Plaid-hosted onboarding UI URL.
* [transfer_recurring_cancel](#transfer_recurring_cancel) - Cancel a recurring transfer.
* [transfer_recurring_create](#transfer_recurring_create) - Create a recurring transfer
* [transfer_recurring_get](#transfer_recurring_get) - Retrieve a recurring transfer
* [transfer_recurring_list](#transfer_recurring_list) - List recurring transfers
* [transfer_refund_cancel](#transfer_refund_cancel) - Cancel a refund
* [transfer_refund_create](#transfer_refund_create) - Create a refund
* [transfer_refund_get](#transfer_refund_get) - Retrieve a refund
* [transfer_repayment_list](#transfer_repayment_list) - Lists historical repayments
* [transfer_repayment_return_list](#transfer_repayment_return_list) - List the returns included in a repayment
* [transfer_sweep_get](#transfer_sweep_get) - Retrieve a sweep
* [transfer_sweep_list](#transfer_sweep_list) - List sweeps
* [user_create](#user_create) - Create user
* [wallet_create](#wallet_create) - Create an e-wallet
* [wallet_get](#wallet_get) - Fetch an e-wallet
* [wallet_list](#wallet_list) - Fetch a list of e-wallets
* [wallet_transaction_execute](#wallet_transaction_execute) - Execute a transaction using an e-wallet
* [wallet_transaction_get](#wallet_transaction_get) - Fetch an e-wallet transaction
* [wallet_transaction_list](#wallet_transaction_list) - List e-wallet transactions
* [watchlist_screening_entity_create](#watchlist_screening_entity_create) - Create a watchlist screening for an entity
* [watchlist_screening_entity_get](#watchlist_screening_entity_get) - Get an entity screening
* [watchlist_screening_entity_history_list](#watchlist_screening_entity_history_list) - List history for entity watchlist screenings
* [watchlist_screening_entity_hit_list](#watchlist_screening_entity_hit_list) - List hits for entity watchlist screenings
* [watchlist_screening_entity_list](#watchlist_screening_entity_list) - List entity watchlist screenings
* [watchlist_screening_entity_program_get](#watchlist_screening_entity_program_get) - Get entity watchlist screening program
* [watchlist_screening_entity_program_list](#watchlist_screening_entity_program_list) - List entity watchlist screening programs
* [watchlist_screening_entity_review_create](#watchlist_screening_entity_review_create) - Create a review for an entity watchlist screening
* [watchlist_screening_entity_review_list](#watchlist_screening_entity_review_list) - List reviews for entity watchlist screenings
* [watchlist_screening_entity_update](#watchlist_screening_entity_update) - Update an entity screening
* [watchlist_screening_individual_create](#watchlist_screening_individual_create) - Create a watchlist screening for a person
* [watchlist_screening_individual_get](#watchlist_screening_individual_get) - Retrieve an individual watchlist screening
* [watchlist_screening_individual_history_list](#watchlist_screening_individual_history_list) - List history for individual watchlist screenings
* [watchlist_screening_individual_hit_list](#watchlist_screening_individual_hit_list) - List hits for individual watchlist screening
* [watchlist_screening_individual_list](#watchlist_screening_individual_list) - List Individual Watchlist Screenings
* [watchlist_screening_individual_program_get](#watchlist_screening_individual_program_get) - Get individual watchlist screening program
* [watchlist_screening_individual_program_list](#watchlist_screening_individual_program_list) - List individual watchlist screening programs
* [watchlist_screening_individual_review_create](#watchlist_screening_individual_review_create) - Create a review for an individual watchlist screening
* [watchlist_screening_individual_review_list](#watchlist_screening_individual_review_list) - List reviews for individual watchlist screenings
* [watchlist_screening_individual_update](#watchlist_screening_individual_update) - Update individual watchlist screening
* [webhook_verification_key_get](#webhook_verification_key_get) - Get webhook verification key

## accounts_balance_get

The `/accounts/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/accounts/balance/get` forces the available and current balance fields to be refreshed rather than cached. This endpoint can be used for existing Items that were added via any of Plaid’s other products. This endpoint can be used as long as Link has been initialized with any other product, `balance` itself is not a product that can be used to initialize Link. As this endpoint triggers a synchronous request for fresh data, latency may be higher than for other Plaid endpoints; if you encounter errors, you may find it necessary to adjust your timeout period when making requests.

</api/products/balance/#accountsbalanceget>

### Example Usage

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
    access_token='string',
)

res = s.plaid.accounts_balance_get(req)

if res.accounts_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.AccountsBalanceGetRequest](../../models/components/accountsbalancegetrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.AccountsBalanceGetResponse](../../models/operations/accountsbalancegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## accounts_get

The `/accounts/get` endpoint can be used to retrieve a list of accounts associated with any linked Item. Plaid will only return active bank accounts — that is, accounts that are not closed and are capable of carrying a balance.
For items that went through the updated account selection pane, this endpoint only returns accounts that were permissioned by the user when they initially created the Item. If a user creates a new account after the initial link, you can capture this event through the [`NEW_ACCOUNTS_AVAILABLE`](https://plaid.com/docs/api/items/#new_accounts_available) webhook and then use Link's [update mode](https://plaid.com/docs/link/update-mode/) to request that the user share this new account with you.

This endpoint retrieves cached information, rather than extracting fresh information from the institution. As a result, balances returned may not be up-to-date; for realtime balance information, use `/accounts/balance/get` instead. Note that some information is nullable.

</api/accounts/#accountsget>

### Example Usage

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

req = components.AccountsGetRequest(
    access_token='string',
)

res = s.plaid.accounts_get(req)

if res.accounts_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.AccountsGetRequest](../../models/components/accountsgetrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.AccountsGetResponse](../../models/operations/accountsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## application_get

Allows financial institutions to retrieve information about Plaid clients for the purpose of building control-tower experiences

### Example Usage

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

req = components.ApplicationGetRequest(
    application_id='string',
    client_id='string',
    secret='string',
)

res = s.plaid.application_get(req)

if res.application_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.ApplicationGetRequest](../../models/components/applicationgetrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.ApplicationGetResponse](../../models/operations/applicationgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## asset_report_audit_copy_create

Plaid can provide an Audit Copy of any Asset Report directly to a participating third party on your behalf. For example, Plaid can supply an Audit Copy directly to Fannie Mae on your behalf if you participate in the Day 1 Certainty™ program. An Audit Copy contains the same underlying data as the Asset Report.

To grant access to an Audit Copy, use the `/asset_report/audit_copy/create` endpoint to create an `audit_copy_token` and then pass that token to the third party who needs access. Each third party has its own `auditor_id`, for example `fannie_mae`. You’ll need to create a separate Audit Copy for each third party to whom you want to grant access to the Report.

</api/products/assets/#asset_reportaudit_copycreate>

### Example Usage

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

req = components.AssetReportAuditCopyCreateRequest(
    asset_report_token='string',
)

res = s.plaid.asset_report_audit_copy_create(req)

if res.asset_report_audit_copy_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.AssetReportAuditCopyCreateRequest](../../models/components/assetreportauditcopycreaterequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.AssetReportAuditCopyCreateResponse](../../models/operations/assetreportauditcopycreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## asset_report_audit_copy_get

`/asset_report/audit_copy/get` allows auditors to get a copy of an Asset Report that was previously shared via the `/asset_report/audit_copy/create` endpoint.  The caller of `/asset_report/audit_copy/create` must provide the `audit_copy_token` to the auditor.  This token can then be used to call `/asset_report/audit_copy/create`.

</none/>

### Example Usage

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

req = components.AssetReportAuditCopyGetRequest(
    audit_copy_token='string',
)

res = s.plaid.asset_report_audit_copy_get(req)

if res.asset_report_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.AssetReportAuditCopyGetRequest](../../models/components/assetreportauditcopygetrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.AssetReportAuditCopyGetResponse](../../models/operations/assetreportauditcopygetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## asset_report_audit_copy_remove

The `/asset_report/audit_copy/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Asset Report, the Asset Report itself and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

</api/products/assets/#asset_reportaudit_copyremove>

### Example Usage

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

req = components.AssetReportAuditCopyRemoveRequest(
    audit_copy_token='string',
)

res = s.plaid.asset_report_audit_copy_remove(req)

if res.asset_report_audit_copy_remove_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.AssetReportAuditCopyRemoveRequest](../../models/components/assetreportauditcopyremoverequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.AssetReportAuditCopyRemoveResponse](../../models/operations/assetreportauditcopyremoveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## asset_report_create

The `/asset_report/create` endpoint initiates the process of creating an Asset Report, which can then be retrieved by passing the `asset_report_token` return value to the `/asset_report/get` or `/asset_report/pdf/get` endpoints.

The Asset Report takes some time to be created and is not available immediately after calling `/asset_report/create`. The exact amount of time to create the report will vary depending on how many days of history are requested and will typically range from a few seconds to about one minute. When the Asset Report is ready to be retrieved using `/asset_report/get` or `/asset_report/pdf/get`, Plaid will fire a `PRODUCT_READY` webhook. For full details of the webhook schema, see [Asset Report webhooks](https://plaid.com/docs/api/products/assets/#webhooks).

The `/asset_report/create` endpoint creates an Asset Report at a moment in time. Asset Reports are immutable. To get an updated Asset Report, use the `/asset_report/refresh` endpoint.

</api/products/assets/#asset_reportcreate>

### Example Usage

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

req = components.AssetReportCreateRequest(
    days_requested=35362,
)

res = s.plaid.asset_report_create(req)

if res.asset_report_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.AssetReportCreateRequest](../../models/components/assetreportcreaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.AssetReportCreateResponse](../../models/operations/assetreportcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## asset_report_filter

By default, an Asset Report will contain all of the accounts on a given Item. In some cases, you may not want the Asset Report to contain all accounts. For example, you might have the end user choose which accounts are relevant in Link using the Account Select view, which you can enable in the dashboard. Or, you might always exclude certain account types or subtypes, which you can identify by using the `/accounts/get` endpoint. To narrow an Asset Report to only a subset of accounts, use the `/asset_report/filter` endpoint.

To exclude certain Accounts from an Asset Report, first use the `/asset_report/create` endpoint to create the report, then send the `asset_report_token` along with a list of `account_ids` to exclude to the `/asset_report/filter` endpoint, to create a new Asset Report which contains only a subset of the original Asset Report's data.

Because Asset Reports are immutable, calling `/asset_report/filter` does not alter the original Asset Report in any way; rather, `/asset_report/filter` creates a new Asset Report with a new token and id. Asset Reports created via `/asset_report/filter` do not contain new Asset data, and are not billed.

Plaid will fire a [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook once generation of the filtered Asset Report has completed.

</api/products/assets/#asset_reportfilter>

### Example Usage

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

req = components.AssetReportFilterRequest(
    account_ids_to_exclude=[
        'string',
    ],
    asset_report_token='string',
)

res = s.plaid.asset_report_filter(req)

if res.asset_report_filter_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.AssetReportFilterRequest](../../models/components/assetreportfilterrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.AssetReportFilterResponse](../../models/operations/assetreportfilterresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## asset_report_get

The `/asset_report/get` endpoint retrieves the Asset Report in JSON format. Before calling `/asset_report/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.

By default, an Asset Report includes transaction descriptions as returned by the bank, as opposed to parsed and categorized by Plaid. You can also receive cleaned and categorized transactions, as well as additional insights like merchant name or location information. We call this an Asset Report with Insights. An Asset Report with Insights provides transaction category, location, and merchant information in addition to the transaction strings provided in a standard Asset Report. To retrieve an Asset Report with Insights, call `/asset_report/get` endpoint with `include_insights` set to `true`.

If `report_type` was set to `VERIFICATION_OF_EMPLOYMENT` when the Asset Report was created in `/asset_report/create`, debit transactions and transaction amounts won’t be included in the report.

 For latency-sensitive applications, you can optionally call `/asset_report/create` with `options.add_ons` set to `["fast_assets"]`. This will cause Plaid to create two versions of the Asset Report: one with only current and available balance and identity information, and then later on the complete Asset Report. You will receive separate webhooks for each version of the Asset Report.

</api/products/assets/#asset_reportget>

### Example Usage

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

req = components.AssetReportGetRequest()

res = s.plaid.asset_report_get(req)

if res.asset_report_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.AssetReportGetRequest](../../models/components/assetreportgetrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.AssetReportGetResponse](../../models/operations/assetreportgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## asset_report_pdf_get

The `/asset_report/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/asset_report/pdf/get`, you must first create the Asset Report using `/asset_report/create` (or filter an Asset Report using `/asset_report/filter`) and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.

The response to `/asset_report/pdf/get` is the PDF binary data. The `request_id`  is returned in the `Plaid-Request-ID` header.

If `report_type` was set to `VERIFICATION_OF_EMPLOYMENT` when the Asset Report was created in `/asset_report/create`, debit transactions and transaction amounts won’t be included in the report.

[View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

</api/products/assets/#asset_reportpdfget>

### Example Usage

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

req = components.AssetReportPDFGetRequest(
    asset_report_token='string',
)

res = s.plaid.asset_report_pdf_get(req)

if res.asset_report_pdf_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.AssetReportPDFGetRequest](../../models/components/assetreportpdfgetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.AssetReportPdfGetResponse](../../models/operations/assetreportpdfgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## asset_report_refresh

An Asset Report is an immutable snapshot of a user's assets. In order to "refresh" an Asset Report you created previously, you can use the `/asset_report/refresh` endpoint to create a new Asset Report based on the old one, but with the most recent data available.

The new Asset Report will contain the same Items as the original Report, as well as the same filters applied by any call to `/asset_report/filter`. By default, the new Asset Report will also use the same parameters you submitted with your original `/asset_report/create` request, but the original `days_requested` value and the values of any parameters in the `options` object can be overridden with new values. To change these arguments, simply supply new values for them in your request to `/asset_report/refresh`. Submit an empty string ("") for any previously-populated fields you would like set as empty.

</api/products/assets/#asset_reportrefresh>

### Example Usage

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

req = components.AssetReportRefreshRequest(
    asset_report_token='string',
)

res = s.plaid.asset_report_refresh(req)

if res.asset_report_refresh_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.AssetReportRefreshRequest](../../models/components/assetreportrefreshrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.AssetReportRefreshResponse](../../models/operations/assetreportrefreshresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## asset_report_remove

The `/item/remove` endpoint allows you to invalidate an `access_token`, meaning you will not be able to create new Asset Reports with it. Removing an Item does not affect any Asset Reports or Audit Copies you have already created, which will remain accessible until you remove them specifically.

The `/asset_report/remove` endpoint allows you to remove an Asset Report. Removing an Asset Report invalidates its `asset_report_token`, meaning you will no longer be able to use it to access Report data or create new Audit Copies. Removing an Asset Report does not affect the underlying Items, but does invalidate any `audit_copy_tokens` associated with the Asset Report.

</api/products/assets/#asset_reportremove>

### Example Usage

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

req = components.AssetReportRemoveRequest(
    asset_report_token='string',
)

res = s.plaid.asset_report_remove(req)

if res.asset_report_remove_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.AssetReportRemoveRequest](../../models/components/assetreportremoverequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.AssetReportRemoveResponse](../../models/operations/assetreportremoveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## auth_get

The `/auth/get` endpoint returns the bank account and bank identification numbers (such as routing numbers, for US accounts) associated with an Item's checking and savings accounts, along with high-level account data and balances when available.

Note: This request may take some time to complete if `auth` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

Versioning note: In API version 2017-03-08, the schema of the `numbers` object returned by this endpoint is substantially different. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2018-05-22).

</api/products/auth/#authget>

### Example Usage

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

req = components.AuthGetRequest(
    access_token='string',
)

res = s.plaid.auth_get(req)

if res.auth_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.AuthGetRequest](../../models/components/authgetrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.AuthGetResponse](../../models/operations/authgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## bank_transfer_balance_get

Use the `/bank_transfer/balance/get` endpoint to see the available balance in your bank transfer account. Debit transfers increase this balance once their status is posted. Credit transfers decrease this balance when they are created.

The transactable balance shows the amount in your account that you are able to use for transfers, and is essentially your available balance minus your minimum balance.

Note that this endpoint can only be used with FBO accounts, when using Bank Transfers in the Full Service configuration. It cannot be used on your own account when using Bank Transfers in the BTS Platform configuration.

</bank-transfers/reference#bank_transferbalanceget>

### Example Usage

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

req = components.BankTransferBalanceGetRequest()

res = s.plaid.bank_transfer_balance_get(req)

if res.bank_transfer_balance_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.BankTransferBalanceGetRequest](../../models/components/banktransferbalancegetrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.BankTransferBalanceGetResponse](../../models/operations/banktransferbalancegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## bank_transfer_cancel

Use the `/bank_transfer/cancel` endpoint to cancel a bank transfer.  A transfer is eligible for cancelation if the `cancellable` property returned by `/bank_transfer/get` is `true`.

</bank-transfers/reference#bank_transfercancel>

### Example Usage

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

req = components.BankTransferCancelRequest(
    bank_transfer_id='string',
)

res = s.plaid.bank_transfer_cancel(req)

if res.bank_transfer_cancel_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.BankTransferCancelRequest](../../models/components/banktransfercancelrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.BankTransferCancelResponse](../../models/operations/banktransfercancelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## bank_transfer_create

Use the `/bank_transfer/create` endpoint to initiate a new bank transfer.

</bank-transfers/reference#bank_transfercreate>

### Example Usage

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

req = components.BankTransferCreateRequest(
    access_token='string',
    account_id='string',
    amount='763.09',
    description='Polarised modular artificial intelligence',
    idempotency_key='string',
    iso_currency_code='string',
    network=components.BankTransferNetwork.ACH,
    type=components.BankTransferType.DEBIT,
    user=components.BankTransferUserInput(
        legal_name='string',
    ),
)

res = s.plaid.bank_transfer_create(req)

if res.bank_transfer_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.BankTransferCreateRequest](../../models/components/banktransfercreaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.BankTransferCreateResponse](../../models/operations/banktransfercreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## bank_transfer_event_list

Use the `/bank_transfer/event/list` endpoint to get a list of Plaid-initiated ACH or bank transfer events based on specified filter criteria. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://plaid.com/docs/auth/coverage/microdeposit-events/).

</api/products/auth#bank_transfereventlist>

### Example Usage

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

req = components.BankTransferEventListRequest()

res = s.plaid.bank_transfer_event_list(req)

if res.bank_transfer_event_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.BankTransferEventListRequest](../../models/components/banktransfereventlistrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.BankTransferEventListResponse](../../models/operations/banktransfereventlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## bank_transfer_event_sync

`/bank_transfer/event/sync` allows you to request up to the next 25 Plaid-initiated bank transfer events that happened after a specific `event_id`. When using Auth with micro-deposit verification enabled, this endpoint can be used to fetch status updates on ACH micro-deposits. For more details, see [micro-deposit events](https://www.plaid.com/docs/auth/coverage/microdeposit-events/).

</api/products/auth/#bank_transfereventsync>

### Example Usage

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

req = components.BankTransferEventSyncRequest(
    after_id=815201,
)

res = s.plaid.bank_transfer_event_sync(req)

if res.bank_transfer_event_sync_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.BankTransferEventSyncRequest](../../models/components/banktransfereventsyncrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.BankTransferEventSyncResponse](../../models/operations/banktransfereventsyncresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## bank_transfer_get

The `/bank_transfer/get` fetches information about the bank transfer corresponding to the given `bank_transfer_id`.

</bank-transfers/reference#bank_transferget>

### Example Usage

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

req = components.BankTransferGetRequest(
    bank_transfer_id='string',
)

res = s.plaid.bank_transfer_get(req)

if res.bank_transfer_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.BankTransferGetRequest](../../models/components/banktransfergetrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.BankTransferGetResponse](../../models/operations/banktransfergetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## bank_transfer_list

Use the `/bank_transfer/list` endpoint to see a list of all your bank transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired bank transfers.


</bank-transfers/reference#bank_transferlist>

### Example Usage

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

req = components.BankTransferListRequest()

res = s.plaid.bank_transfer_list(req)

if res.bank_transfer_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.BankTransferListRequest](../../models/components/banktransferlistrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.BankTransferListResponse](../../models/operations/banktransferlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## bank_transfer_migrate_account

As an alternative to adding Items via Link, you can also use the `/bank_transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Bank Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/bank_transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.

</bank-transfers/reference#bank_transfermigrate_account>

### Example Usage

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

req = components.BankTransferMigrateAccountRequest(
    account_number='string',
    account_type='string',
    routing_number='string',
)

res = s.plaid.bank_transfer_migrate_account(req)

if res.bank_transfer_migrate_account_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.BankTransferMigrateAccountRequest](../../models/components/banktransfermigrateaccountrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.BankTransferMigrateAccountResponse](../../models/operations/banktransfermigrateaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## bank_transfer_sweep_get

The `/bank_transfer/sweep/get` endpoint fetches information about the sweep corresponding to the given `sweep_id`.

</api/products/transfer/#bank_transfersweepget>

### Example Usage

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

req = components.BankTransferSweepGetRequest(
    sweep_id='string',
)

res = s.plaid.bank_transfer_sweep_get(req)

if res.bank_transfer_sweep_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.BankTransferSweepGetRequest](../../models/components/banktransfersweepgetrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.BankTransferSweepGetResponse](../../models/operations/banktransfersweepgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## bank_transfer_sweep_list

The `/bank_transfer/sweep/list` endpoint fetches information about the sweeps matching the given filters.

</api/products/transfer/#bank_transfersweeplist>

### Example Usage

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

req = components.BankTransferSweepListRequest()

res = s.plaid.bank_transfer_sweep_list(req)

if res.bank_transfer_sweep_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.BankTransferSweepListRequest](../../models/components/banktransfersweeplistrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.BankTransferSweepListResponse](../../models/operations/banktransfersweeplistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## base_report_get

This endpoint allows the customer to retrieve a Base Report. Customers should pass in the `user_token` created in `/link/token/create`.

</none/>

### Example Usage

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

req = components.BaseReportGetRequest(
    user_token='string',
)

res = s.plaid.base_report_get(req)

if res.base_report_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.BaseReportGetRequest](../../models/components/basereportgetrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.BaseReportGetResponse](../../models/operations/basereportgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## beacon_report_create

Create a fraud report for a given Beacon User.

Note: If you are creating users with the express purpose of providing historical fraud data, you should use the `/beacon/user/create` endpoint instead and embed the fraud report in the request. This will ensure that the Beacon User you create will not be subject to any billing costs.

</api/products/beacon/#beaconreportcreate>

### Example Usage

```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.BeaconReportCreateRequest(
    beacon_user_id='becusr_11111111111111',
    fraud_date=dateutil.parser.parse('1990-05-29').date(),
    type=components.BeaconReportType.UNKNOWN,
)

res = s.plaid.beacon_report_create(req)

if res.beacon_report_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.BeaconReportCreateRequest](../../models/components/beaconreportcreaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.BeaconReportCreateResponse](../../models/operations/beaconreportcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## beacon_user_create

Create and scan a Beacon User against your Beacon Program, according to your program's settings.

When you submit a new user to `/beacon/user/create`, several checks are performed immediately:

  - The user's PII (provided within the `user` object) is searched against all other users within the Beacon Program you specified. If a match is found that violates your program's "Duplicate Information Filtering" settings, the user will be returned with a status of `pending_review`.

  - The user's PII is also searched against all fraud reports created by your organization across all of your Beacon Programs. If the user's data matches a fraud report that your team created, the user will be returned with a status of `rejected`.

  - Finally, the user's PII is searched against all fraud report shared with the Beacon Network by other companies. If a matching fraud report is found, the user will be returned with a `pending_review` status if your program has enabled automatic flagging based on network fraud.

</api/products/beacon/#beaconusercreate>

### Example Usage

```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.BeaconUserCreateRequest(
    client_user_id='your-db-id-3b24110',
    program_id='becprg_11111111111111',
    user=components.BeaconUserRequestData(
        address=components.BeaconUserRequestAddress(
            city='Pawnee',
            country='US',
            street='123 Main St.',
            postal_code='46001',
            region='IN',
            street2='Unit 42',
        ),
        date_of_birth=dateutil.parser.parse('1990-05-29').date(),
        name=components.BeaconUserName(
            family_name='Knope',
            given_name='Leslie',
        ),
        email_address='user@example.com',
        ip_address='192.0.2.42',
        phone_number='+19876543212',
    ),
)

res = s.plaid.beacon_user_create(req)

if res.beacon_user_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.BeaconUserCreateRequest](../../models/components/beaconusercreaterequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.BeaconUserCreateResponse](../../models/operations/beaconusercreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## beacon_user_get

Fetch a Beacon User.

The Beacon User is returned with all of their associated information and a `status` based on the Beacon Network duplicate record and fraud checks.


</api/products/beacon/#beaconuserget>

### Example Usage

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

req = components.BeaconUserGetRequest(
    beacon_user_id='becusr_11111111111111',
)

res = s.plaid.beacon_user_get(req)

if res.beacon_user_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.BeaconUserGetRequest](../../models/components/beaconusergetrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.BeaconUserGetResponse](../../models/operations/beaconusergetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## categories_get

Send a request to the `/categories/get` endpoint to get detailed information on categories returned by Plaid. This endpoint does not require authentication.

All implementations are recommended to use the newer `personal_finance_category` taxonomy instead of the older `category` taxonomy supported by this endpoint. The [`personal_finance_category taxonomy` CSV file](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) is available for download and is not accessible via API.

</api/products/transactions/#categoriesget>

### Example Usage

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

req = components.CategoriesGetRequest()

res = s.plaid.categories_get(req)

if res.categories_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.CategoriesGetRequest](../../models/components/categoriesgetrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CategoriesGetResponse](../../models/operations/categoriesgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## cra_bank_income_get

`/cra/bank_income/get` returns the bank income report(s) for a specified user.

</api/products/income/#crabank_incomeget>

### Example Usage

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

req = components.CraBankIncomeGetRequest()

res = s.plaid.cra_bank_income_get(req)

if res.cra_bank_income_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.CraBankIncomeGetRequest](../../models/components/crabankincomegetrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CraBankIncomeGetResponse](../../models/operations/crabankincomegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~create_payment_token~~

The `/payment_initiation/payment/token/create` endpoint has been deprecated. New Plaid customers will be unable to use this endpoint, and existing customers are encouraged to migrate to the newer, `link_token`-based flow. The recommended flow is to provide the `payment_id` to `/link/token/create`, which returns a `link_token` used to initialize Link.

The `/payment_initiation/payment/token/create` is used to create a `payment_token`, which can then be used in Link initialization to enter a payment initiation flow. You can only use a `payment_token` once. If this attempt fails, the end user aborts the flow, or the token expires, you will need to create a new payment token. Creating a new payment token does not require end user input.

</link/maintain-legacy-integration/#creating-a-payment-token>

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

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

req = components.PaymentInitiationPaymentTokenCreateRequest(
    payment_id='string',
)

res = s.plaid.create_payment_token(req)

if res.payment_initiation_payment_token_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [components.PaymentInitiationPaymentTokenCreateRequest](../../models/components/paymentinitiationpaymenttokencreaterequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.CreatePaymentTokenResponse](../../models/operations/createpaymenttokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_asset_report_freddie_mac_get

The `credit/asset_report/freddie_mac/get` endpoint retrieves the Asset Report in Freddie Mac's JSON format.

</none/>

### Example Usage

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

req = components.AssetReportFreddieGetRequest(
    audit_copy_token='string',
)

res = s.plaid.credit_asset_report_freddie_mac_get(req)

if res.asset_report_freddie_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.AssetReportFreddieGetRequest](../../models/components/assetreportfreddiegetrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.CreditAssetReportFreddieMacGetResponse](../../models/operations/creditassetreportfreddiemacgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_audit_copy_token_create

Plaid can create an Audit Copy token of an Asset Report and/or Income Report to share with participating Government Sponsored Entity (GSE). If you participate in the Day 1 Certainty™ program, Plaid can supply an Audit Copy token directly to Fannie Mae on your behalf. An Audit Copy token contains the same underlying data as the Asset Report and/or Income Report (result of /credit/payroll_income/get).

Use the `/credit/audit_copy_token/create` endpoint to create an `audit_copy_token` and then pass that token to the GSE who needs access.

</api/products/income/#creditaudit_copy_tokencreate>

### Example Usage

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

req = components.CreditAuditCopyTokenCreateRequest(
    report_tokens=[
        'string',
    ],
)

res = s.plaid.credit_audit_copy_token_create(req)

if res.credit_audit_copy_token_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.CreditAuditCopyTokenCreateRequest](../../models/components/creditauditcopytokencreaterequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.CreditAuditCopyTokenCreateResponse](../../models/operations/creditauditcopytokencreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_audit_copy_token_update

The `/credit/audit_copy_token/update` endpoint updates an existing  Audit Copy Token by adding the report tokens in the `report_tokens` field to the `audit_copy_token`. If the Audit Copy Token already contains a report of a certain type, it will be replaced with the token provided in the `report_tokens` field.

</none/>

### Example Usage

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

req = components.CreditAuditCopyTokenUpdateRequest(
    audit_copy_token='string',
    report_tokens=[
        'string',
    ],
)

res = s.plaid.credit_audit_copy_token_update(req)

if res.credit_audit_copy_token_update_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.CreditAuditCopyTokenUpdateRequest](../../models/components/creditauditcopytokenupdaterequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.CreditAuditCopyTokenUpdateResponse](../../models/operations/creditauditcopytokenupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_bank_employment_get

`/credit/bank_employment/get` returns the employment report(s) derived from bank transaction data for a specified user.

</api/products/income/#creditbank_employmentget>

### Example Usage

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

req = components.CreditBankEmploymentGetRequest(
    user_token='string',
)

res = s.plaid.credit_bank_employment_get(req)

if res.credit_bank_employment_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.CreditBankEmploymentGetRequest](../../models/components/creditbankemploymentgetrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreditBankEmploymentGetResponse](../../models/operations/creditbankemploymentgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_bank_income_get

`/credit/bank_income/get` returns the bank income report(s) for a specified user.

</api/products/income/#creditbank_incomeget>

### Example Usage

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

req = components.CreditBankIncomeGetRequest()

res = s.plaid.credit_bank_income_get(req)

if res.credit_bank_income_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.CreditBankIncomeGetRequest](../../models/components/creditbankincomegetrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.CreditBankIncomeGetResponse](../../models/operations/creditbankincomegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_bank_income_pdf_get

`/credit/bank_income/pdf/get` returns the most recent bank income report for a specified user in PDF format.

</api/products/income/#creditbank_incomepdfget>

### Example Usage

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

req = components.CreditBankIncomePDFGetRequest(
    user_token='string',
)

res = s.plaid.credit_bank_income_pdf_get(req)

if res.credit_bank_income_pdf_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.CreditBankIncomePDFGetRequest](../../models/components/creditbankincomepdfgetrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.CreditBankIncomePdfGetResponse](../../models/operations/creditbankincomepdfgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_bank_income_refresh

`/credit/bank_income/refresh` refreshes the bank income report data for a specific user.

</api/products/income/#creditbank_incomerefresh>

### Example Usage

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

req = components.CreditBankIncomeRefreshRequest(
    user_token='string',
)

res = s.plaid.credit_bank_income_refresh(req)

if res.credit_bank_income_refresh_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.CreditBankIncomeRefreshRequest](../../models/components/creditbankincomerefreshrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreditBankIncomeRefreshResponse](../../models/operations/creditbankincomerefreshresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_bank_income_webhook_update

`/credit/bank_income/webhook/update` allows you to subscribe or unsubscribe a user for income webhook notifications.

If a user is subscribed, on significant changes to the user's income profile, you will receive a `BANK_INCOME_REFRESH_UPDATE` webhook, prompting you to refresh bank income data for the user.

</api/products/income/#creditbank_incomewebhookupdate>

### Example Usage

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

req = components.CreditBankIncomeWebhookUpdateRequest(
    enable_webhooks=False,
    user_token='string',
)

res = s.plaid.credit_bank_income_webhook_update(req)

if res.credit_bank_income_webhook_update_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [components.CreditBankIncomeWebhookUpdateRequest](../../models/components/creditbankincomewebhookupdaterequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.CreditBankIncomeWebhookUpdateResponse](../../models/operations/creditbankincomewebhookupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_bank_statements_uploads_get

`/credit/bank_statements/uploads/get` returns data from user-uploaded bank statements.

</api/products/income/#creditbank_statementsuploadsget>

### Example Usage

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

req = components.CreditBankStatementsUploadsGetRequest(
    user_token='string',
)

res = s.plaid.credit_bank_statements_uploads_get(req)

if res.credit_bank_statements_uploads_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [components.CreditBankStatementsUploadsGetRequest](../../models/components/creditbankstatementsuploadsgetrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.CreditBankStatementsUploadsGetResponse](../../models/operations/creditbankstatementsuploadsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_employment_get

`/credit/employment/get` returns a list of items with employment information from a user's payroll provider that was verified by an end user.

</api/products/income/#creditemploymentget>

### Example Usage

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

req = components.CreditEmploymentGetRequest(
    user_token='string',
)

res = s.plaid.credit_employment_get(req)

if res.credit_employment_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.CreditEmploymentGetRequest](../../models/components/creditemploymentgetrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.CreditEmploymentGetResponse](../../models/operations/creditemploymentgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_freddie_mac_reports_get

The `credit/asset_report/freddie_mac/get` endpoint retrieves the Verification of Assets and Verification of Employment reports.

</none/>

### Example Usage

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

req = components.CreditFreddieMacReportsGetRequest(
    audit_copy_token='string',
)

res = s.plaid.credit_freddie_mac_reports_get(req)

if res.credit_freddie_mac_reports_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.CreditFreddieMacReportsGetRequest](../../models/components/creditfreddiemacreportsgetrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.CreditFreddieMacReportsGetResponse](../../models/operations/creditfreddiemacreportsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_payroll_income_get

This endpoint gets payroll income information for a specific user, either as a result of the user connecting to their payroll provider or uploading a pay related document.

</api/products/income/#creditpayroll_incomeget>

### Example Usage

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

req = components.CreditPayrollIncomeGetRequest()

res = s.plaid.credit_payroll_income_get(req)

if res.credit_payroll_income_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.CreditPayrollIncomeGetRequest](../../models/components/creditpayrollincomegetrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.CreditPayrollIncomeGetResponse](../../models/operations/creditpayrollincomegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_payroll_income_precheck

`/credit/payroll_income/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification. If the user is eligible for digital verification, that information will be associated with the user token, and in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.

While all request fields are optional, providing `employer` data will increase the chance of receiving a useful result.

When testing in Sandbox, you can control the results by providing special test values in the `employer` and `access_tokens` fields. `employer_good` and `employer_bad` will result in `HIGH` and `LOW` confidence values, respectively. `employer_multi` will result in a `HIGH` confidence with multiple payroll options. Likewise, `access_good` and `access_bad` will result in `HIGH` and `LOW` confidence values, respectively. Any other value for `employer` and `access_tokens` in Sandbox will result in `UNKNOWN` confidence.

</api/products/income/#creditpayroll_incomeprecheck>

### Example Usage

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

req = components.CreditPayrollIncomePrecheckRequest()

res = s.plaid.credit_payroll_income_precheck(req)

if res.credit_payroll_income_precheck_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.CreditPayrollIncomePrecheckRequest](../../models/components/creditpayrollincomeprecheckrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.CreditPayrollIncomePrecheckResponse](../../models/operations/creditpayrollincomeprecheckresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_payroll_income_refresh

`/credit/payroll_income/refresh` refreshes a given digital payroll income verification.

</api/products/income/#creditpayroll_incomerefresh>

### Example Usage

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

req = components.CreditPayrollIncomeRefreshRequest(
    user_token='string',
)

res = s.plaid.credit_payroll_income_refresh(req)

if res.credit_payroll_income_refresh_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.CreditPayrollIncomeRefreshRequest](../../models/components/creditpayrollincomerefreshrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.CreditPayrollIncomeRefreshResponse](../../models/operations/creditpayrollincomerefreshresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_payroll_income_risk_signals_get

`/credit/payroll_income/risk_signals/get` can be used as part of the Document Income flow to assess a user-uploaded document for signs of potential fraud or tampering. It returns a risk score for each uploaded document that indicates the likelihood of the document being fraudulent, in addition to details on the individual risk signals contributing to the score. `/credit/payroll_income/risk_signals/get` can be called at any time after the `INCOME_VERIFICATION_RISK_SIGNALS` webhook has been fired.

`/credit/payroll_income/risk_signals/get` is offered as an add-on to Document Income and is billed separately. To request access to this endpoint, submit a product access request or contact your Plaid account manager.

</api/products/income/#creditpayroll_incomerisk_signalsget>

### Example Usage

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

req = components.CreditPayrollIncomeRiskSignalsGetRequest()

res = s.plaid.credit_payroll_income_risk_signals_get(req)

if res.credit_payroll_income_risk_signals_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [components.CreditPayrollIncomeRiskSignalsGetRequest](../../models/components/creditpayrollincomerisksignalsgetrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.CreditPayrollIncomeRiskSignalsGetResponse](../../models/operations/creditpayrollincomerisksignalsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_relay_create

Plaid can share an Asset Report directly with a participating third party on your behalf. The shared Asset Report is the exact same Asset Report originally created in `/asset_report/create`.

To grant a third party access to an Asset Report, use the `/credit/relay/create` endpoint to create a `relay_token` and then pass that token to your third party. Each third party has its own `secondary_client_id`; for example, `ce5bd328dcd34123456`. You'll need to create a separate `relay_token` for each third party that needs access to the report on your behalf.

</api/products/assets/#creditrelaycreate>

### Example Usage

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

req = components.CreditRelayCreateRequest(
    report_tokens=[
        'string',
    ],
    secondary_client_id='string',
)

res = s.plaid.credit_relay_create(req)

if res.credit_relay_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.CreditRelayCreateRequest](../../models/components/creditrelaycreaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreditRelayCreateResponse](../../models/operations/creditrelaycreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_relay_get

`/credit/relay/get` allows third parties to receive a report that was shared with them, using a `relay_token` that was created by the report owner.

</api/products/assets/#creditrelayget>

### Example Usage

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

req = components.CreditRelayGetRequest(
    relay_token='string',
    report_type=components.ReportType.ASSET,
)

res = s.plaid.credit_relay_get(req)

if res.asset_report_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.CreditRelayGetRequest](../../models/components/creditrelaygetrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreditRelayGetResponse](../../models/operations/creditrelaygetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_relay_pdf_get

`/credit/relay/pdf/get` allows third parties to receive a pdf report that was shared with them, using a `relay_token` that was created by the report owner.

The `/credit/relay/pdf/get` endpoint retrieves the Asset Report in PDF format. Before calling `/credit/relay/pdf/get`, you must first create the Asset Report using `/credit/relay/create` and then wait for the [`PRODUCT_READY`](https://plaid.com/docs/api/products/assets/#product_ready) webhook to fire, indicating that the Report is ready to be retrieved.

The response to `/credit/relay/pdf/get` is the PDF binary data. The `request_id` is returned in the `Plaid-Request-ID` header.

[View a sample PDF Asset Report](https://plaid.com/documents/sample-asset-report.pdf).

</api/products/assets/#creditrelaypdfget>

### Example Usage

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

req = components.CreditRelayPDFGetRequest(
    relay_token='string',
    report_type=components.ReportType.ASSET,
)

res = s.plaid.credit_relay_pdf_get(req)

if res.credit_relay_pdf_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.CreditRelayPDFGetRequest](../../models/components/creditrelaypdfgetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreditRelayPdfGetResponse](../../models/operations/creditrelaypdfgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_relay_refresh

The `/credit/relay/refresh` endpoint allows third parties to refresh a report that was relayed to them, using a `relay_token` that was created by the report owner. A new report will be created with the original report parameters, but with the most recent data available based on the `days_requested` value of the original report.

</api/products/assets/#creditrelayrefresh>

### Example Usage

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

req = components.CreditRelayRefreshRequest(
    relay_token='string',
    report_type=components.ReportType.ASSET,
)

res = s.plaid.credit_relay_refresh(req)

if res.credit_relay_refresh_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.CreditRelayRefreshRequest](../../models/components/creditrelayrefreshrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreditRelayRefreshResponse](../../models/operations/creditrelayrefreshresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_relay_remove

The `/credit/relay/remove` endpoint allows you to invalidate a `relay_token`. The third party holding the token will no longer be able to access or refresh the reports which the `relay_token` gives access to. The original report, associated Items, and other relay tokens that provide access to the same report are not affected and will remain accessible after removing the given `relay_token`.

</api/products/assets/#creditrelayremove>

### Example Usage

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

req = components.CreditRelayRemoveRequest(
    relay_token='string',
)

res = s.plaid.credit_relay_remove(req)

if res.credit_relay_remove_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.CreditRelayRemoveRequest](../../models/components/creditrelayremoverequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreditRelayRemoveResponse](../../models/operations/creditrelayremoveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_report_audit_copy_remove

The `/credit/audit_copy_token/remove` endpoint allows you to remove an Audit Copy. Removing an Audit Copy invalidates the `audit_copy_token` associated with it, meaning both you and any third parties holding the token will no longer be able to use it to access Report data. Items associated with the Report data and other Audit Copies of it are not affected and will remain accessible after removing the given Audit Copy.

</api/products/income/#creditaudit_copy_tokenremove>

### Example Usage

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

req = components.CreditAuditCopyTokenRemoveRequest(
    audit_copy_token='string',
)

res = s.plaid.credit_report_audit_copy_remove(req)

if res.credit_audit_copy_token_remove_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.CreditAuditCopyTokenRemoveRequest](../../models/components/creditauditcopytokenremoverequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.CreditReportAuditCopyRemoveResponse](../../models/operations/creditreportauditcopyremoveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## credit_sessions_get

This endpoint can be used for your end users after they complete the Link flow. This endpoint returns a list of Link sessions that your user completed, where each session includes the results from the Link flow.

These results include details about the Item that was created and some product related metadata (showing, for example, whether the user finished the bank income verification step).

</api/products/income/#creditsessionsget>

### Example Usage

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

req = components.CreditSessionsGetRequest(
    user_token='string',
)

res = s.plaid.credit_sessions_get(req)

if res.credit_sessions_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.CreditSessionsGetRequest](../../models/components/creditsessionsgetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreditSessionsGetResponse](../../models/operations/creditsessionsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## dashboard_user_get

Retrieve information about a dashboard user.

</api/products/monitor/#dashboard_userget>

### Example Usage

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

req = components.DashboardUserGetRequest(
    dashboard_user_id='54350110fedcbaf01234ffee',
)

res = s.plaid.dashboard_user_get(req)

if res.dashboard_user_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.DashboardUserGetRequest](../../models/components/dashboardusergetrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DashboardUserGetResponse](../../models/operations/dashboardusergetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## dashboard_user_list

List all dashboard users associated with your account.

</api/products/monitor/#dashboard_userlist>

### Example Usage

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

req = components.DashboardUserListRequest(
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
)

res = s.plaid.dashboard_user_list(req)

if res.dashboard_user_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.DashboardUserListRequest](../../models/components/dashboarduserlistrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.DashboardUserListResponse](../../models/operations/dashboarduserlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## deposit_switch_alt_create

This endpoint provides an alternative to `/deposit_switch/create` for customers who have not yet fully integrated with Plaid Exchange. Like `/deposit_switch/create`, it creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

</deposit-switch/reference#deposit_switchaltcreate>

### Example Usage

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

req = components.DepositSwitchAltCreateRequest(
    target_account=components.DepositSwitchTargetAccount(
        account_name='string',
        account_number='string',
        account_subtype=components.DepositSwitchTargetAccountAccountSubtype.CHECKING,
        routing_number='string',
    ),
    target_user=components.DepositSwitchTargetUser(
        email='Melody_Schmeler51@gmail.com',
        family_name='string',
        given_name='string',
        phone='(748) 725-9375 x62825',
    ),
)

res = s.plaid.deposit_switch_alt_create(req)

if res.deposit_switch_alt_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.DepositSwitchAltCreateRequest](../../models/components/depositswitchaltcreaterequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.DepositSwitchAltCreateResponse](../../models/operations/depositswitchaltcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## deposit_switch_create

This endpoint creates a deposit switch entity that will be persisted throughout the lifecycle of the switch.

</deposit-switch/reference#deposit_switchcreate>

### Example Usage

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

req = components.DepositSwitchCreateRequest(
    target_access_token='string',
    target_account_id='string',
)

res = s.plaid.deposit_switch_create(req)

if res.deposit_switch_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.DepositSwitchCreateRequest](../../models/components/depositswitchcreaterequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.DepositSwitchCreateResponse](../../models/operations/depositswitchcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## deposit_switch_get

This endpoint returns information related to how the user has configured their payroll allocation and the state of the switch. You can use this information to build logic related to the user's direct deposit allocation preferences.

</deposit-switch/reference#deposit_switchget>

### Example Usage

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

req = components.DepositSwitchGetRequest(
    deposit_switch_id='string',
)

res = s.plaid.deposit_switch_get(req)

if res.deposit_switch_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.DepositSwitchGetRequest](../../models/components/depositswitchgetrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DepositSwitchGetResponse](../../models/operations/depositswitchgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## deposit_switch_token_create

In order for the end user to take action, you will need to create a public token representing the deposit switch. This token is used to initialize Link. It can be used one time and expires after 30 minutes.


</deposit-switch/reference#deposit_switchtokencreate>

### Example Usage

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

req = components.DepositSwitchTokenCreateRequest(
    deposit_switch_id='string',
)

res = s.plaid.deposit_switch_token_create(req)

if res.deposit_switch_token_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.DepositSwitchTokenCreateRequest](../../models/components/depositswitchtokencreaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.DepositSwitchTokenCreateResponse](../../models/operations/depositswitchtokencreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## employers_search

`/employers/search` allows you the ability to search Plaid’s database of known employers, for use with Deposit Switch. You can use this endpoint to look up a user's employer in order to confirm that they are supported. Users with non-supported employers can then be routed out of the Deposit Switch flow.

The data in the employer database is currently limited. As the Deposit Switch and Income products progress through their respective beta periods, more employers are being regularly added. Because the employer database is frequently updated, we recommend that you do not cache or store data from this endpoint for more than a day.

</api/employers/#employerssearch>

### Example Usage

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

req = components.EmployersSearchRequest(
    products=[
        'string',
    ],
    query='string',
)

res = s.plaid.employers_search(req)

if res.employers_search_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.EmployersSearchRequest](../../models/components/employerssearchrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.EmployersSearchResponse](../../models/operations/employerssearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~employment_verification_get~~

`/employment/verification/get` returns a list of employments through a user payroll that was verified by an end user.

This endpoint has been deprecated; new integrations should use `/credit/employment/get` instead.

</api/products/income/#employmentverificationget>

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

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

req = components.EmploymentVerificationGetRequest(
    access_token='string',
)

res = s.plaid.employment_verification_get(req)

if res.employment_verification_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [components.EmploymentVerificationGetRequest](../../models/components/employmentverificationgetrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.EmploymentVerificationGetResponse](../../models/operations/employmentverificationgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## fdx_notifications

A generic webhook receiver endpoint for FDX Event Notifications

</api/fdx/notifications/#post>

### Example Usage

```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.FDXNotification(
    category=components.FDXNotificationCategory.CONSENT,
    notification_id='string',
    notification_payload=components.FDXNotificationPayload(),
    publisher=components.FDXParty(
        name='string',
        type=components.FDXPartyType.MERCHANT,
    ),
    sent_on=dateutil.parser.isoparse('2021-07-15T14:46:41.375Z'),
    type=components.FDXNotificationType.CONSENT_REVOKED,
)

res = s.plaid.fdx_notifications(req)

if res.status_code == 200:
    # handle response
    pass
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [components.FDXNotification](../../models/components/fdxnotification.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.FdxNotificationsResponse](../../models/operations/fdxnotificationsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## identity_get

The `/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses. Only name data is guaranteed to be returned; other fields will be empty arrays if not provided by the institution.

This request may take some time to complete if identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

Note: In API versions 2018-05-22 and earlier, the `owners` object is not returned, and instead identity information is returned in the top level `identity` object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29).

</api/products/identity/#identityget>

### Example Usage

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

req = components.IdentityGetRequest(
    access_token='string',
)

res = s.plaid.identity_get(req)

if res.identity_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.IdentityGetRequest](../../models/components/identitygetrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.IdentityGetResponse](../../models/operations/identitygetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## identity_match

The `/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.

This request may take some time to complete if Identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

</api/products/identity/#identitymatch>

### Example Usage

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

req = components.IdentityMatchRequest(
    access_token='string',
)

res = s.plaid.identity_match(req)

if res.identity_match_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.IdentityMatchRequest](../../models/components/identitymatchrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.IdentityMatchResponse](../../models/operations/identitymatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## identity_refresh

`/identity/refresh` is an optional endpoint for users of the Identity product. It initiates an on-demand extraction to fetch the most up to date Identity information from the Financial Institution. This on-demand extraction takes place in addition to the periodic extractions that automatically occur any Identity-enabled Item. If changes to Identity are discovered after calling `/identity/refresh`, Plaid will fire a webhook [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/identity/#default_update).
`/identity/refresh` is offered as an add-on to Identity and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

</api/products/identity/#identityrefresh>

### Example Usage

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

req = components.IdentityRefreshRequest(
    access_token='string',
)

res = s.plaid.identity_refresh(req)

if res.identity_refresh_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.IdentityRefreshRequest](../../models/components/identityrefreshrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.IdentityRefreshResponse](../../models/operations/identityrefreshresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## identity_verification_create

Create a new Identity Verification for the user specified by the `client_user_id` field. The requirements and behavior of the verification are determined by the `template_id` provided.
If you don't know whether the associated user already has an active Identity Verification, you can specify `"is_idempotent": true` in the request body. With idempotency enabled, a new Identity Verification will only be created if one does not already exist for the associated `client_user_id` and `template_id`. If an Identity Verification is found, it will be returned unmodified with an `200 OK` HTTP status code.

You can also use this endpoint to supply information you already have collected about the user; if any of these fields are specified, the screens prompting the user to enter them will be skipped during the Link flow.


</api/products/identity-verification/#identity_verificationcreate>

### Example Usage

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

req = components.IdentityVerificationCreateRequest(
    is_shareable=True,
    template_id='idvtmp_4FrXJvfQU3zGUR',
    client_user_id='your-db-id-3b24110',
    gave_consent=True,
    is_idempotent=True,
)

res = s.plaid.identity_verification_create(req)

if res.identity_verification_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.IdentityVerificationCreateRequest](../../models/components/identityverificationcreaterequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.IdentityVerificationCreateResponse](../../models/operations/identityverificationcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## identity_verification_get

Retrieve a previously created identity verification.

</api/products/identity-verification/#identity_verificationget>

### Example Usage

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

req = components.IdentityVerificationGetRequest(
    identity_verification_id='idv_52xR9LKo77r1Np',
)

res = s.plaid.identity_verification_get(req)

if res.identity_verification_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.IdentityVerificationGetRequest](../../models/components/identityverificationgetrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.IdentityVerificationGetResponse](../../models/operations/identityverificationgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## identity_verification_list

Filter and list Identity Verifications created by your account

</api/products/identity-verification/#identity_verificationlist>

### Example Usage

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

req = components.IdentityVerificationListRequest(
    client_user_id='your-db-id-3b24110',
    template_id='idvtmp_4FrXJvfQU3zGUR',
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
)

res = s.plaid.identity_verification_list(req)

if res.identity_verification_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.IdentityVerificationListRequest](../../models/components/identityverificationlistrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.IdentityVerificationListResponse](../../models/operations/identityverificationlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## identity_verification_retry

Allow a customer to retry their identity verification

</api/products/identity-verification/#identity_verificationretry>

### Example Usage

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

req = components.IdentityVerificationRetryRequest(
    client_user_id='your-db-id-3b24110',
    strategy=components.Strategy.INCOMPLETE,
    template_id='idvtmp_4FrXJvfQU3zGUR',
)

res = s.plaid.identity_verification_retry(req)

if res.identity_verification_retry_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [components.IdentityVerificationRetryRequest](../../models/components/identityverificationretryrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.IdentityVerificationRetryResponse](../../models/operations/identityverificationretryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~income_verification_create~~

`/income/verification/create` begins the income verification process by returning an `income_verification_id`. You can then provide the `income_verification_id` to `/link/token/create` under the `income_verification` parameter in order to create a Link instance that will prompt the user to go through the income verification flow. Plaid will fire an `INCOME` webhook once the user completes the Payroll Income flow, or when the uploaded documents in the Document Income flow have finished processing. 

</api/products/income/#incomeverificationcreate>

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

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

req = components.IncomeVerificationCreateRequest(
    webhook='string',
)

res = s.plaid.income_verification_create(req)

if res.income_verification_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.IncomeVerificationCreateRequest](../../models/components/incomeverificationcreaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.IncomeVerificationCreateResponse](../../models/operations/incomeverificationcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~income_verification_documents_download~~

`/income/verification/documents/download` provides the ability to download the source documents associated with the verification.

If Document Income was used, the documents will be those the user provided in Link. For Payroll Income, the most recent files available
for download from the payroll provider will be available from this endpoint.

The response to `/income/verification/documents/download` is a ZIP file in binary data. If a `document_id` is passed, a single document will be contained in this file.
If not, the response will contain all documents associated with the verification.

The `request_id` is returned in the `Plaid-Request-ID` header.

</api/products/income/#incomeverificationdocumentsdownload>

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

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

req = components.IncomeVerificationDocumentsDownloadRequest()

res = s.plaid.income_verification_documents_download(req)

if res.stream is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [components.IncomeVerificationDocumentsDownloadRequest](../../models/components/incomeverificationdocumentsdownloadrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.IncomeVerificationDocumentsDownloadResponse](../../models/operations/incomeverificationdocumentsdownloadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~income_verification_paystubs_get~~

`/income/verification/paystubs/get` returns the information collected from the paystubs that were used to verify an end user's income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

</api/products/income/#incomeverificationpaystubsget>

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

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

req = components.IncomeVerificationPaystubsGetRequest()

res = s.plaid.income_verification_paystubs_get(req)

if res.income_verification_paystubs_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [components.IncomeVerificationPaystubsGetRequest](../../models/components/incomeverificationpaystubsgetrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.IncomeVerificationPaystubsGetResponse](../../models/operations/incomeverificationpaystubsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~income_verification_precheck~~

`/income/verification/precheck` is an optional endpoint that can be called before initializing a Link session for income verification. It evaluates whether a given user is supportable by digital income verification and returns a `precheck_id` that can be provided to `/link/token/create`. If the user is eligible for digital verification, providing the `precheck_id` in this way will generate a Link UI optimized for the end user and their specific employer. If the user cannot be confirmed as eligible, the `precheck_id` can still be provided to `/link/token/create` and the user can still use the income verification flow, but they may be required to manually upload a paystub to verify their income.

While all request fields are optional, providing either `employer` or `transactions_access_tokens` data will increase the chance of receiving a useful result.

This endpoint has been deprecated; new integrations should use `/credit/payroll_income/precheck` instead.

</api/products/income/#incomeverificationprecheck>

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

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

req = components.IncomeVerificationPrecheckRequest()

res = s.plaid.income_verification_precheck(req)

if res.income_verification_precheck_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.IncomeVerificationPrecheckRequest](../../models/components/incomeverificationprecheckrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.IncomeVerificationPrecheckResponse](../../models/operations/incomeverificationprecheckresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ~~income_verification_taxforms_get~~

`/income/verification/taxforms/get` returns the information collected from forms that were used to verify an end user''s income. It can be called once the status of the verification has been set to `VERIFICATION_STATUS_PROCESSING_COMPLETE`, as reported by the `INCOME: verification_status` webhook. Attempting to call the endpoint before verification has been completed will result in an error.

This endpoint has been deprecated; new integrations should use `/credit/payroll_income/get` instead.

</api/products/income/#incomeverificationtaxformsget>

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

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

req = components.IncomeVerificationTaxformsGetRequest()

res = s.plaid.income_verification_taxforms_get(req)

if res.income_verification_taxforms_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [components.IncomeVerificationTaxformsGetRequest](../../models/components/incomeverificationtaxformsgetrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.IncomeVerificationTaxformsGetResponse](../../models/operations/incomeverificationtaxformsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## institutions_get

Returns a JSON response containing details on all financial institutions currently supported by Plaid. Because Plaid supports thousands of institutions, results are paginated.

If there is no overlap between an institution’s enabled products and a client’s enabled products, then the institution will be filtered out from the response. As a result, the number of institutions returned may not match the count specified in the call.

</api/institutions/#institutionsget>

### Example Usage

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

req = components.InstitutionsGetRequest(
    count=591738,
    country_codes=[
        components.CountryCode.CA,
    ],
    offset=294528,
)

res = s.plaid.institutions_get(req)

if res.institutions_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.InstitutionsGetRequest](../../models/components/institutionsgetrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.InstitutionsGetResponse](../../models/operations/institutionsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## institutions_get_by_id

Returns a JSON response containing details on a specified financial institution currently supported by Plaid.

Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` to authenticate to this endpoint. The `public_key` has been deprecated; all customers are encouraged to use `client_id` and `secret` instead.


</api/institutions/#institutionsget_by_id>

### Example Usage

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

req = components.InstitutionsGetByIDRequest(
    country_codes=[
        components.CountryCode.NO,
    ],
    institution_id='string',
)

res = s.plaid.institutions_get_by_id(req)

if res.institutions_get_by_id_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.InstitutionsGetByIDRequest](../../models/components/institutionsgetbyidrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.InstitutionsGetByIDResponse](../../models/operations/institutionsgetbyidresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## institutions_search

Returns a JSON response containing details for institutions that match the query parameters, up to a maximum of ten institutions per query.

Versioning note: API versions 2019-05-29 and earlier allow use of the `public_key` parameter instead of the `client_id` and `secret` parameters to authenticate to this endpoint. The `public_key` parameter has since been deprecated; all customers are encouraged to use `client_id` and `secret` instead.


</api/institutions/#institutionssearch>

### Example Usage

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

req = components.InstitutionsSearchRequest(
    country_codes=[
        components.CountryCode.NO,
    ],
    products=[
        components.Products.DEPOSIT_SWITCH,
    ],
    query='string',
)

res = s.plaid.institutions_search(req)

if res.institutions_search_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.InstitutionsSearchRequest](../../models/components/institutionssearchrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.InstitutionsSearchResponse](../../models/operations/institutionssearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## investments_auth_get

The `/investments/auth/get` endpoint allows developers to receive user-authorized data to facilitate the transfer of holdings

</api/products/investments/#investmentsauth>

### Example Usage

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

req = components.InvestmentsAuthGetRequest(
    access_token='string',
)

res = s.plaid.investments_auth_get(req)

if res.investments_auth_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.InvestmentsAuthGetRequest](../../models/components/investmentsauthgetrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.InvestmentsAuthGetResponse](../../models/operations/investmentsauthgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## investments_holdings_get

The `/investments/holdings/get` endpoint allows developers to receive user-authorized stock position data for `investment`-type accounts.

</api/products/investments/#investmentsholdingsget>

### Example Usage

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

req = components.InvestmentsHoldingsGetRequest(
    access_token='string',
)

res = s.plaid.investments_holdings_get(req)

if res.investments_holdings_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.InvestmentsHoldingsGetRequest](../../models/components/investmentsholdingsgetrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.InvestmentsHoldingsGetResponse](../../models/operations/investmentsholdingsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## investments_refresh

`/investments/refresh` is an optional endpoint for users of the Investments product. It initiates an on-demand extraction to fetch the newest investments, holdings and investment transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Investments-enabled Item. If changes to investments are discovered after calling `/investments/refresh`, Plaid will fire webhooks: [`HOLDINGS: DEFAULT_UPDATE`](https://plaid.com/docs/api/products/investments/#holdings-default_update) if any new holdings are detected, and [INVESTMENTS_TRANSACTIONS: DEFAULT_UPDATE](https://plaid.com/docs/api/products/investments/#investments_transactions-default_update) if any new investment transactions are detected. Updated holdings and investment transactions can be fetched by calling `/investments/holdings/get` and `/investments/transactions/get`. "Note that the `/investments/refresh` endpoint is not supported by all institutions. If called on an Item from an institution that does not support this functionality, it will return a `PRODUCT_NOT_SUPPORTED` error.
`/investments/refresh` is offered as an add-on to Investments and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

</api/products/investments/#investmentsrefresh>

### Example Usage

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

req = components.InvestmentsRefreshRequest(
    access_token='string',
)

res = s.plaid.investments_refresh(req)

if res.investments_refresh_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.InvestmentsRefreshRequest](../../models/components/investmentsrefreshrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.InvestmentsRefreshResponse](../../models/operations/investmentsrefreshresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## investments_transactions_get

The `/investments/transactions/get` endpoint allows developers to retrieve up to 24 months of user-authorized transaction data for investment accounts.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.

Due to the potentially large number of investment transactions associated with an Item, results are paginated. Manipulate the count and offset parameters in conjunction with the `total_investment_transactions` response body field to fetch all available investment transactions.

Note that Investments does not have a webhook to indicate when initial transaction data has loaded (unless you use the `async_update` option). Instead, if transactions data is not ready when `/investments/transactions/get` is first called, Plaid will wait for the data. For this reason, calling `/investments/transactions/get` immediately after Link may take up to one to two minutes to return.

Data returned by the asynchronous investments extraction flow (when `async_update` is set to true) may not be immediately available to `/investments/transactions/get`. To be alerted when the data is ready to be fetched, listen for the `HISTORICAL_UPDATE` webhook. If no investments history is ready when `/investments/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

</api/products/investments/#investmentstransactionsget>

### Example Usage

```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.InvestmentsTransactionsGetRequest(
    access_token='string',
    end_date=dateutil.parser.parse('2024-08-24').date(),
    start_date=dateutil.parser.parse('2024-03-17').date(),
)

res = s.plaid.investments_transactions_get(req)

if res.investments_transactions_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.InvestmentsTransactionsGetRequest](../../models/components/investmentstransactionsgetrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.InvestmentsTransactionsGetResponse](../../models/operations/investmentstransactionsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## item_access_token_invalidate

By default, the `access_token` associated with an Item does not expire and should be stored in a persistent, secure manner.

You can use the `/item/access_token/invalidate` endpoint to rotate the `access_token` associated with an Item. The endpoint returns a new `access_token` and immediately invalidates the previous `access_token`.


</api/tokens/#itemaccess_tokeninvalidate>

### Example Usage

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

req = components.ItemAccessTokenInvalidateRequest(
    access_token='string',
)

res = s.plaid.item_access_token_invalidate(req)

if res.item_access_token_invalidate_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [components.ItemAccessTokenInvalidateRequest](../../models/components/itemaccesstokeninvalidaterequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.ItemAccessTokenInvalidateResponse](../../models/operations/itemaccesstokeninvalidateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## item_activity_list

List a historical log of user consent events

### Example Usage

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

req = components.ItemActivityListRequest()

res = s.plaid.item_activity_list(req)

if res.item_activity_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.ItemActivityListRequest](../../models/components/itemactivitylistrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ItemActivityListResponse](../../models/operations/itemactivitylistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## item_application_list

List a user’s connected applications

### Example Usage

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

req = components.ItemApplicationListRequest()

res = s.plaid.item_application_list(req)

if res.item_application_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.ItemApplicationListRequest](../../models/components/itemapplicationlistrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.ItemApplicationListResponse](../../models/operations/itemapplicationlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## item_application_scopes_update

Enable consumers to update product access on selected accounts for an application.

### Example Usage

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

req = components.ItemApplicationScopesUpdateRequest(
    access_token='string',
    application_id='string',
    context=components.ScopesContext.ENROLLMENT,
    scopes=components.Scopes(),
)

res = s.plaid.item_application_scopes_update(req)

if res.item_application_scopes_update_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.ItemApplicationScopesUpdateRequest](../../models/components/itemapplicationscopesupdaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.ItemApplicationScopesUpdateResponse](../../models/operations/itemapplicationscopesupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## item_create_public_token

Note: As of July 2020, the `/item/public_token/create` endpoint is deprecated. Instead, use `/link/token/create` with an `access_token` to create a Link token for use with [update mode](https://plaid.com/docs/link/update-mode).

If you need your user to take action to restore or resolve an error associated with an Item, generate a public token with the `/item/public_token/create` endpoint and then initialize Link with that `public_token`.

A `public_token` is one-time use and expires after 30 minutes. You use a `public_token` to initialize Link in [update mode](https://plaid.com/docs/link/update-mode) for a particular Item. You can generate a `public_token` for an Item even if you did not use Link to create the Item originally.

The `/item/public_token/create` endpoint is **not** used to create your initial `public_token`. If you have not already received an `access_token` for a specific Item, use Link to obtain your `public_token` instead. See the [Quickstart](https://plaid.com/docs/quickstart) for more information.

</api/tokens/#itempublic_tokencreate>

### Example Usage

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

req = components.ItemPublicTokenCreateRequest(
    access_token='string',
)

res = s.plaid.item_create_public_token(req)

if res.item_public_token_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.ItemPublicTokenCreateRequest](../../models/components/itempublictokencreaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.ItemCreatePublicTokenResponse](../../models/operations/itemcreatepublictokenresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## item_get

Returns information about the status of an Item.

</api/items/#itemget>

### Example Usage

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

req = components.ItemGetRequest(
    access_token='string',
)

res = s.plaid.item_get(req)

if res.item_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [components.ItemGetRequest](../../models/components/itemgetrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.ItemGetResponse](../../models/operations/itemgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## item_import

`/item/import` creates an Item via your Plaid Exchange Integration and returns an `access_token`. As part of an `/item/import` request, you will include a User ID (`user_auth.user_id`) and Authentication Token (`user_auth.auth_token`) that enable data aggregation through your Plaid Exchange API endpoints. These authentication principals are to be chosen by you.

Upon creating an Item via `/item/import`, Plaid will automatically begin an extraction of that Item through the Plaid Exchange infrastructure you have already integrated.

### Example Usage

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

req = components.ItemImportRequest(
    products=[
        components.Products.PAYMENT_INITIATION,
    ],
    user_auth=components.ItemImportRequestUserAuth(
        auth_token='string',
        user_id='string',
    ),
)

res = s.plaid.item_import(req)

if res.item_import_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.ItemImportRequest](../../models/components/itemimportrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ItemImportResponse](../../models/operations/itemimportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## item_public_token_exchange

Exchange a Link `public_token` for an API `access_token`. Link hands off the `public_token` client-side via the `onSuccess` callback once a user has successfully created an Item. The `public_token` is ephemeral and expires after 30 minutes. An `access_token` does not expire, but can be revoked by calling `/item/remove`.

The response also includes an `item_id` that should be stored with the `access_token`. The `item_id` is used to identify an Item in a webhook. The `item_id` can also be retrieved by making an `/item/get` request.

</api/tokens/#itempublic_tokenexchange>

### Example Usage

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

req = components.ItemPublicTokenExchangeRequest(
    public_token='string',
)

res = s.plaid.item_public_token_exchange(req)

if res.item_public_token_exchange_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.ItemPublicTokenExchangeRequest](../../models/components/itempublictokenexchangerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ItemPublicTokenExchangeResponse](../../models/operations/itempublictokenexchangeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## item_remove

The `/item/remove` endpoint allows you to remove an Item. Once removed, the `access_token`, as well as any processor tokens or bank account tokens associated with the Item, is no longer valid and cannot be used to access any data that was associated with the Item.

Note that in the Development environment, issuing an `/item/remove`  request will not decrement your live credential count. To increase your credential account in Development, contact Support.

Also note that for certain OAuth-based institutions, an Item removed via `/item/remove` may still show as an active connection in the institution's OAuth permission manager.

API versions 2019-05-29 and earlier return a `removed` boolean as part of the response.

</api/items/#itemremove>

### Example Usage

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

req = components.ItemRemoveRequest(
    access_token='string',
)

res = s.plaid.item_remove(req)

if res.item_remove_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.ItemRemoveRequest](../../models/components/itemremoverequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ItemRemoveResponse](../../models/operations/itemremoveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## item_webhook_update

The POST `/item/webhook/update` allows you to update the webhook URL associated with an Item. This request triggers a [`WEBHOOK_UPDATE_ACKNOWLEDGED`](https://plaid.com/docs/api/items/#webhook_update_acknowledged) webhook to the newly specified webhook URL.

</api/items/#itemwebhookupdate>

### Example Usage

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

req = components.ItemWebhookUpdateRequest(
    access_token='string',
)

res = s.plaid.item_webhook_update(req)

if res.item_webhook_update_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.ItemWebhookUpdateRequest](../../models/components/itemwebhookupdaterequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.ItemWebhookUpdateResponse](../../models/operations/itemwebhookupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## liabilities_get

The `/liabilities/get` endpoint returns various details about an Item with loan or credit accounts. Liabilities data is available primarily for US financial institutions, with some limited coverage of Canadian institutions. Currently supported account types are account type `credit` with account subtype `credit card` or `paypal`, and account type `loan` with account subtype `student` or `mortgage`. To limit accounts listed in Link to types and subtypes supported by Liabilities, you can use the `account_filters` parameter when [creating a Link token](https://plaid.com/docs/api/tokens/#linktokencreate).

The types of information returned by Liabilities can include balances and due dates, loan terms, and account details such as original loan amount and guarantor. Data is refreshed approximately once per day; the latest data can be retrieved by calling `/liabilities/get`.

Note: This request may take some time to complete if `liabilities` was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the additional data.

</api/products/liabilities/#liabilitiesget>

### Example Usage

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

req = components.LiabilitiesGetRequest(
    access_token='string',
)

res = s.plaid.liabilities_get(req)

if res.liabilities_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.LiabilitiesGetRequest](../../models/components/liabilitiesgetrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.LiabilitiesGetResponse](../../models/operations/liabilitiesgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## link_delivery_create

Use the `/link_delivery/create` endpoint to create a Hosted Link session.

</assets/waitlist/hosted-link/>

### Example Usage

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

req = components.LinkDeliveryCreateRequest(
    link_token='string',
)

res = s.plaid.link_delivery_create(req)

if res.link_delivery_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.LinkDeliveryCreateRequest](../../models/components/linkdeliverycreaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.LinkDeliveryCreateResponse](../../models/operations/linkdeliverycreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## link_delivery_get

Use the `/link_delivery/get` endpoint to get the status of a Hosted Link session.

</assets/waitlist/hosted-link/>

### Example Usage

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

req = components.LinkDeliveryGetRequest(
    link_delivery_session_id='string',
)

res = s.plaid.link_delivery_get(req)

if res.link_delivery_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.LinkDeliveryGetRequest](../../models/components/linkdeliverygetrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.LinkDeliveryGetResponse](../../models/operations/linkdeliverygetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## link_oauth_correlation_id_exchange

Exchange an OAuth `link_correlation_id` for the corresponding `link_token`. The `link_correlation_id` is only available for 'payment_initiation' products and is provided to the client via the OAuth `redirect_uri` as a query parameter.
The `link_correlation_id` is ephemeral and expires in a brief period, after which it can no longer be exchanged for the 'link_token'.

</api/oauth/#linkcorrelationid>

### Example Usage

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

req = components.LinkOAuthCorrelationIDExchangeRequest(
    link_correlation_id='string',
)

res = s.plaid.link_oauth_correlation_id_exchange(req)

if res.link_o_auth_correlation_id_exchange_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [components.LinkOAuthCorrelationIDExchangeRequest](../../models/components/linkoauthcorrelationidexchangerequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.LinkOauthCorrelationIDExchangeResponse](../../models/operations/linkoauthcorrelationidexchangeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## link_token_create

The `/link/token/create` endpoint creates a `link_token`, which is required as a parameter when initializing Link. Once Link has been initialized, it returns a `public_token`, which can then be exchanged for an `access_token` via `/item/public_token/exchange` as part of the main Link flow.

A `link_token` generated by `/link/token/create` is also used to initialize other Link flows, such as the update mode flow for tokens with expired credentials, or the Payment Initiation (Europe) flow.

</api/tokens/#linktokencreate>

### Example Usage

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

req = components.LinkTokenCreateRequest(
    client_name='string',
    country_codes=[
        components.CountryCode.IT,
    ],
    language='string',
    user=components.LinkTokenCreateRequestUser(
        client_user_id='string',
    ),
)

res = s.plaid.link_token_create(req)

if res.link_token_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.LinkTokenCreateRequest](../../models/components/linktokencreaterequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.LinkTokenCreateResponse](../../models/operations/linktokencreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## link_token_get

The `/link/token/get` endpoint gets information about a previously-created `link_token` using the
`/link/token/create` endpoint. It can be useful for debugging purposes.

</api/tokens/#linktokenget>

### Example Usage

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

req = components.LinkTokenGetRequest(
    link_token='string',
)

res = s.plaid.link_token_get(req)

if res.link_token_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.LinkTokenGetRequest](../../models/components/linktokengetrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.LinkTokenGetResponse](../../models/operations/linktokengetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partner_customer_create

The `/partner/customer/create` endpoint is used by reseller partners to create end customers.

</api/partner/#partnercustomercreate>

### Example Usage

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

req = components.PartnerCustomerCreateRequest(
    address=components.PartnerEndCustomerAddress(),
    application_name='string',
    company_name='Padberg - Hyatt',
    is_bank_addendum_completed=False,
    is_diligence_attested=False,
    legal_entity_name='string',
    products=[
        components.Products.ASSETS,
    ],
    website='string',
)

res = s.plaid.partner_customer_create(req)

if res.partner_customer_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.PartnerCustomerCreateRequest](../../models/components/partnercustomercreaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.PartnerCustomerCreateResponse](../../models/operations/partnercustomercreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partner_customer_enable

The `/partner/customer/enable` endpoint is used by reseller partners to enable an end customer in the Production environment.

</api/partner/#partnercustomerenable>

### Example Usage

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

req = components.PartnerCustomerEnableRequest(
    end_customer_client_id='string',
)

res = s.plaid.partner_customer_enable(req)

if res.partner_customer_enable_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.PartnerCustomerEnableRequest](../../models/components/partnercustomerenablerequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.PartnerCustomerEnableResponse](../../models/operations/partnercustomerenableresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partner_customer_get

The `/partner/customer/get` endpoint is used by reseller partners to retrieve data about a single end customer.

</api/partner/#partnercustomerget>

### Example Usage

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

req = components.PartnerCustomerGetRequest(
    end_customer_client_id='string',
)

res = s.plaid.partner_customer_get(req)

if res.partner_customer_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.PartnerCustomerGetRequest](../../models/components/partnercustomergetrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.PartnerCustomerGetResponse](../../models/operations/partnercustomergetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partner_customer_oauth_institutions_get

The `/partner/customer/oauth_institutions/get` endpoint is used by reseller partners to retrieve OAuth-institution registration information about a single end customer. To learn how to set up a webhook to listen to status update events, visit the [reseller documentation](https://plaid.com/docs/account/resellers/#enabling-end-customers).

</api/partner/#partnercustomeroauth_institutionsget>

### Example Usage

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

req = components.PartnerCustomerOAuthInstitutionsGetRequest(
    end_customer_client_id='string',
)

res = s.plaid.partner_customer_oauth_institutions_get(req)

if res.partner_customer_o_auth_institutions_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [components.PartnerCustomerOAuthInstitutionsGetRequest](../../models/components/partnercustomeroauthinstitutionsgetrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.PartnerCustomerOauthInstitutionsGetResponse](../../models/operations/partnercustomeroauthinstitutionsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## partner_customer_remove

The `/partner/customer/remove` endpoint is used by reseller partners to remove an end customer. Removing an end customer will remove it from view in the Plaid Dashboard and deactivate its API keys. This endpoint can only be used to remove an end customer that has not yet been enabled in Production.

</api/partner/#partnercustomerremove>

### Example Usage

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

req = components.PartnerCustomerRemoveRequest(
    end_customer_client_id='string',
)

res = s.plaid.partner_customer_remove(req)

if res.partner_customer_remove_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.PartnerCustomerRemoveRequest](../../models/components/partnercustomerremoverequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.PartnerCustomerRemoveResponse](../../models/operations/partnercustomerremoveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_consent_create

The `/payment_initiation/consent/create` endpoint is used to create a payment consent, which can be used to initiate payments on behalf of the user. Payment consents are created with `UNAUTHORISED` status by default and must be authorised by the user before payments can be initiated.

Consents can be limited in time and scope, and have constraints that describe limitations for payments.

</api/products/payment-initiation/#payment_initiationconsentcreate>

### Example Usage

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

req = components.PaymentInitiationConsentCreateRequest(
    constraints=components.PaymentInitiationConsentConstraints(
        max_payment_amount=components.PaymentAmount(
            currency=components.PaymentAmountCurrency.SEK,
            value=6599.05,
        ),
        periodic_amounts=[
            components.PaymentConsentPeriodicAmount(
                alignment=components.PaymentConsentPeriodicAlignment.CONSENT,
                amount=components.PaymentAmount(
                    currency=components.PaymentAmountCurrency.EUR,
                    value=4177.13,
                ),
                interval=components.PaymentConsentPeriodicInterval.YEAR,
            ),
        ],
    ),
    recipient_id='string',
    reference='string',
    scopes=[
        components.PaymentInitiationConsentScope.ME_TO_ME,
    ],
)

res = s.plaid.payment_initiation_consent_create(req)

if res.payment_initiation_consent_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [components.PaymentInitiationConsentCreateRequest](../../models/components/paymentinitiationconsentcreaterequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PaymentInitiationConsentCreateResponse](../../models/operations/paymentinitiationconsentcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_consent_get

The `/payment_initiation/consent/get` endpoint can be used to check the status of a payment consent, as well as to receive basic information such as recipient and constraints.

</api/products/payment-initiation/#payment_initiationconsentget>

### Example Usage

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

req = components.PaymentInitiationConsentGetRequest(
    consent_id='string',
)

res = s.plaid.payment_initiation_consent_get(req)

if res.payment_initiation_consent_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.PaymentInitiationConsentGetRequest](../../models/components/paymentinitiationconsentgetrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PaymentInitiationConsentGetResponse](../../models/operations/paymentinitiationconsentgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_consent_payment_execute

The `/payment_initiation/consent/payment/execute` endpoint can be used to execute payments using payment consent.

</api/products/payment-initiation/#payment_initiationconsentpaymentexecute>

### Example Usage

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

req = components.PaymentInitiationConsentPaymentExecuteRequest(
    amount=components.PaymentAmount(
        currency=components.PaymentAmountCurrency.EUR,
        value=2986.44,
    ),
    consent_id='string',
    idempotency_key='string',
)

res = s.plaid.payment_initiation_consent_payment_execute(req)

if res.payment_initiation_consent_payment_execute_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [components.PaymentInitiationConsentPaymentExecuteRequest](../../models/components/paymentinitiationconsentpaymentexecuterequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.PaymentInitiationConsentPaymentExecuteResponse](../../models/operations/paymentinitiationconsentpaymentexecuteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_consent_revoke

The `/payment_initiation/consent/revoke` endpoint can be used to revoke the payment consent. Once the consent is revoked, it is not possible to initiate payments using it.

</api/products/payment-initiation/#payment_initiationconsentrevoke>

### Example Usage

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

req = components.PaymentInitiationConsentRevokeRequest(
    consent_id='string',
)

res = s.plaid.payment_initiation_consent_revoke(req)

if res.payment_initiation_consent_revoke_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [components.PaymentInitiationConsentRevokeRequest](../../models/components/paymentinitiationconsentrevokerequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PaymentInitiationConsentRevokeResponse](../../models/operations/paymentinitiationconsentrevokeresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_payment_create

After creating a payment recipient, you can use the `/payment_initiation/payment/create` endpoint to create a payment to that recipient.  Payments can be one-time or standing order (recurring) and can be denominated in either EUR, GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency).  If making domestic GBP-denominated payments, your recipient must have been created with BACS numbers. In general, EUR-denominated payments will be sent via SEPA Credit Transfer, GBP-denominated payments will be sent via the Faster Payments network and for non-Eurozone markets typically via the local payment scheme, but the payment network used will be determined by the institution. Payments sent via Faster Payments will typically arrive immediately, while payments sent via SEPA Credit Transfer or other local payment schemes will typically arrive in one business day.

Standing orders (recurring payments) must be denominated in GBP and can only be sent to recipients in the UK. Once created, standing order payments cannot be modified or canceled via the API. An end user can cancel or modify a standing order directly on their banking application or website, or by contacting the bank. Standing orders will follow the payment rules of the underlying rails (Faster Payments in UK). Payments can be sent Monday to Friday, excluding bank holidays. If the pre-arranged date falls on a weekend or bank holiday, the payment is made on the next working day. It is not possible to guarantee the exact time the payment will reach the recipient’s account, although at least 90% of standing order payments are sent by 6am.

In the Development environment, payments must be below 5 GBP or other chosen [currency](https://plaid.com/docs/api/products/payment-initiation/#payment_initiation-payment-create-request-amount-currency). For details on any payment limits in Production, contact your Plaid Account Manager.

</api/products/payment-initiation/#payment_initiationpaymentcreate>

### Example Usage

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

req = components.PaymentInitiationPaymentCreateRequest(
    amount=components.PaymentAmount(
        currency=components.PaymentAmountCurrency.PLN,
        value=676.57,
    ),
    recipient_id='string',
    reference='string',
)

res = s.plaid.payment_initiation_payment_create(req)

if res.payment_initiation_payment_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [components.PaymentInitiationPaymentCreateRequest](../../models/components/paymentinitiationpaymentcreaterequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PaymentInitiationPaymentCreateResponse](../../models/operations/paymentinitiationpaymentcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_payment_get

The `/payment_initiation/payment/get` endpoint can be used to check the status of a payment, as well as to receive basic information such as recipient and payment amount. In the case of standing orders, the `/payment_initiation/payment/get` endpoint will provide information about the status of the overall standing order itself; the API cannot be used to retrieve payment status for individual payments within a standing order.

</api/products/payment-initiation/#payment_initiationpaymentget>

### Example Usage

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

req = components.PaymentInitiationPaymentGetRequest(
    payment_id='string',
)

res = s.plaid.payment_initiation_payment_get(req)

if res.payment_initiation_payment_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.PaymentInitiationPaymentGetRequest](../../models/components/paymentinitiationpaymentgetrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.PaymentInitiationPaymentGetResponse](../../models/operations/paymentinitiationpaymentgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_payment_list

The `/payment_initiation/payment/list` endpoint can be used to retrieve all created payments. By default, the 10 most recent payments are returned. You can request more payments and paginate through the results using the optional `count` and `cursor` parameters.

</api/products/payment-initiation/#payment_initiationpaymentlist>

### Example Usage

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

req = components.PaymentInitiationPaymentListRequest()

res = s.plaid.payment_initiation_payment_list(req)

if res.payment_initiation_payment_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [components.PaymentInitiationPaymentListRequest](../../models/components/paymentinitiationpaymentlistrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.PaymentInitiationPaymentListResponse](../../models/operations/paymentinitiationpaymentlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_payment_reverse

Reverse a settled payment from a Plaid virtual account.

The original payment must be in a settled state to be refunded.
To refund partially, specify the amount as part of the request.
If the amount is not specified, the refund amount will be equal to all
of the remaining payment amount that has not been refunded yet.

The refund will go back to the source account that initiated the payment.
The original payment must have been initiated to a Plaid virtual account
so that this account can be used to initiate the refund.


</api/products/payment-initiation/#payment_initiationpaymentreverse>

### Example Usage

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

req = components.PaymentInitiationPaymentReverseRequest(
    idempotency_key='string',
    payment_id='string',
    reference='string',
)

res = s.plaid.payment_initiation_payment_reverse(req)

if res.payment_initiation_payment_reverse_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [components.PaymentInitiationPaymentReverseRequest](../../models/components/paymentinitiationpaymentreverserequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.PaymentInitiationPaymentReverseResponse](../../models/operations/paymentinitiationpaymentreverseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_recipient_create

Create a payment recipient for payment initiation.  The recipient must be in Europe, within a country that is a member of the Single Euro Payment Area (SEPA) or a non-Eurozone country [supported](https://plaid.com/global) by Plaid. For a standing order (recurring) payment, the recipient must be in the UK.

It is recommended to use `bacs` in the UK and `iban` in EU.

The endpoint is idempotent: if a developer has already made a request with the same payment details, Plaid will return the same `recipient_id`.


</api/products/payment-initiation/#payment_initiationrecipientcreate>

### Example Usage

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

req = components.PaymentInitiationRecipientCreateRequest(
    name='string',
)

res = s.plaid.payment_initiation_recipient_create(req)

if res.payment_initiation_recipient_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [components.PaymentInitiationRecipientCreateRequest](../../models/components/paymentinitiationrecipientcreaterequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.PaymentInitiationRecipientCreateResponse](../../models/operations/paymentinitiationrecipientcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_recipient_get

Get details about a payment recipient you have previously created.

</api/products/payment-initiation/#payment_initiationrecipientget>

### Example Usage

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

req = components.PaymentInitiationRecipientGetRequest(
    recipient_id='string',
)

res = s.plaid.payment_initiation_recipient_get(req)

if res.payment_initiation_recipient_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [components.PaymentInitiationRecipientGetRequest](../../models/components/paymentinitiationrecipientgetrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.PaymentInitiationRecipientGetResponse](../../models/operations/paymentinitiationrecipientgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_initiation_recipient_list

The `/payment_initiation/recipient/list` endpoint list the payment recipients that you have previously created.

</api/products/payment-initiation/#payment_initiationrecipientlist>

### Example Usage

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

req = components.PaymentInitiationRecipientListRequest()

res = s.plaid.payment_initiation_recipient_list(req)

if res.payment_initiation_recipient_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [components.PaymentInitiationRecipientListRequest](../../models/components/paymentinitiationrecipientlistrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.PaymentInitiationRecipientListResponse](../../models/operations/paymentinitiationrecipientlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_profile_create

Use `/payment_profile/create` endpoint to create a new payment profile.
To initiate the account linking experience, call `/link/token/create` and provide the `payment_profile_token` in the `transfer.payment_profile_token` field.
You can then use the `payment_profile_token` when creating transfers using `/transfer/authorization/create` and `/transfer/create`.

</api/products/transfer/#payment_profilecreate>

### Example Usage

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

req = components.PaymentProfileCreateRequest()

res = s.plaid.payment_profile_create(req)

if res.payment_profile_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.PaymentProfileCreateRequest](../../models/components/paymentprofilecreaterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PaymentProfileCreateResponse](../../models/operations/paymentprofilecreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_profile_get

Use `/payment_profile/get` endpoint to get the status of a given Payment Profile.

</api/products/transfer/#payment_profileget>

### Example Usage

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

req = components.PaymentProfileGetRequest(
    payment_profile_token='string',
)

res = s.plaid.payment_profile_get(req)

if res.payment_profile_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.PaymentProfileGetRequest](../../models/components/paymentprofilegetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.PaymentProfileGetResponse](../../models/operations/paymentprofilegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## payment_profile_remove

Use the `/payment_profile/remove` endpoint to remove a given Payment Profile. Once it’s removed, it can no longer be used to create transfers.

</api/products/transfer/#payment_profileremove>

### Example Usage

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

req = components.PaymentProfileRemoveRequest(
    payment_profile_token='string',
)

res = s.plaid.payment_profile_remove(req)

if res.payment_profile_remove_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.PaymentProfileRemoveRequest](../../models/components/paymentprofileremoverequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.PaymentProfileRemoveResponse](../../models/operations/paymentprofileremoveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_apex_processor_token_create

Used to create a token suitable for sending to Apex to enable Plaid-Apex integrations.

</none/>

### Example Usage

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

req = components.ProcessorApexProcessorTokenCreateRequest(
    access_token='string',
    account_id='string',
)

res = s.plaid.processor_apex_processor_token_create(req)

if res.processor_token_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [components.ProcessorApexProcessorTokenCreateRequest](../../models/components/processorapexprocessortokencreaterequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.ProcessorApexProcessorTokenCreateResponse](../../models/operations/processorapexprocessortokencreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_auth_get

The `/processor/auth/get` endpoint returns the bank account and bank identification number (such as the routing number, for US accounts), for a checking or savings account that''s associated with a given `processor_token`. The endpoint also returns high-level account data and balances when available.

Versioning note: API versions 2019-05-29 and earlier use a different schema for the `numbers` object returned by this endpoint. For details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2020-09-14).


</api/processors/#processorauthget>

### Example Usage

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

req = components.ProcessorAuthGetRequest(
    processor_token='string',
)

res = s.plaid.processor_auth_get(req)

if res.processor_auth_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.ProcessorAuthGetRequest](../../models/components/processorauthgetrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.ProcessorAuthGetResponse](../../models/operations/processorauthgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_balance_get

The `/processor/balance/get` endpoint returns the real-time balance for each of an Item's accounts. While other endpoints may return a balance object, only `/processor/balance/get` forces the available and current balance fields to be refreshed rather than cached. 

</api/processors/#processorbalanceget>

### Example Usage

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

req = components.ProcessorBalanceGetRequest(
    processor_token='string',
)

res = s.plaid.processor_balance_get(req)

if res.processor_balance_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.ProcessorBalanceGetRequest](../../models/components/processorbalancegetrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.ProcessorBalanceGetResponse](../../models/operations/processorbalancegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_bank_transfer_create

Use the `/processor/bank_transfer/create` endpoint to initiate a new bank transfer as a processor

</api/processors/#bank_transfercreate>

### Example Usage

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

req = components.ProcessorBankTransferCreateRequest(
    amount='44.37',
    description='Open-source grid-enabled customer loyalty',
    idempotency_key='string',
    iso_currency_code='string',
    network=components.BankTransferNetwork.WIRE,
    processor_token='string',
    type=components.BankTransferType.DEBIT,
    user=components.BankTransferUserInput(
        legal_name='string',
    ),
)

res = s.plaid.processor_bank_transfer_create(req)

if res.processor_bank_transfer_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.ProcessorBankTransferCreateRequest](../../models/components/processorbanktransfercreaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.ProcessorBankTransferCreateResponse](../../models/operations/processorbanktransfercreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_identity_get

The `/processor/identity/get` endpoint allows you to retrieve various account holder information on file with the financial institution, including names, emails, phone numbers, and addresses.

</api/processors/#processoridentityget>

### Example Usage

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

req = components.ProcessorIdentityGetRequest(
    processor_token='string',
)

res = s.plaid.processor_identity_get(req)

if res.processor_identity_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.ProcessorIdentityGetRequest](../../models/components/processoridentitygetrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.ProcessorIdentityGetResponse](../../models/operations/processoridentitygetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_identity_match

The `/processor/identity/match` endpoint generates a match score, which indicates how well the provided identity data matches the identity information on file with the account holder's financial institution.

This request may take some time to complete if Identity was not specified as an initial product when creating the Item. This is because Plaid must communicate directly with the institution to retrieve the data.

</api/processors/#processoridentitymatch>

### Example Usage

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

req = components.ProcessorIdentityMatchRequest(
    processor_token='string',
)

res = s.plaid.processor_identity_match(req)

if res.processor_identity_match_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.ProcessorIdentityMatchRequest](../../models/components/processoridentitymatchrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.ProcessorIdentityMatchResponse](../../models/operations/processoridentitymatchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_signal_decision_report

After calling `/processor/signal/evaluate`, call `/processor/signal/decision/report` to report whether the transaction was initiated.

</api/processors/#processorsignaldecisionreport>

### Example Usage

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

req = components.ProcessorSignalDecisionReportRequest(
    client_transaction_id='string',
    initiated=False,
    processor_token='string',
)

res = s.plaid.processor_signal_decision_report(req)

if res.processor_signal_decision_report_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [components.ProcessorSignalDecisionReportRequest](../../models/components/processorsignaldecisionreportrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.ProcessorSignalDecisionReportResponse](../../models/operations/processorsignaldecisionreportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_signal_evaluate

Use `/processor/signal/evaluate` to evaluate a planned ACH transaction as a processor to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.

In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/processor/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to our error documentation on [item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).

Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time. To reduce this latency, you can call `/signal/prepare` on the Item before you need to request Signal data.

</api/processors/#processorsignalevaluate>

### Example Usage

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

req = components.ProcessorSignalEvaluateRequest(
    amount=2186.98,
    client_transaction_id='string',
    processor_token='string',
)

res = s.plaid.processor_signal_evaluate(req)

if res.processor_signal_evaluate_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.ProcessorSignalEvaluateRequest](../../models/components/processorsignalevaluaterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.ProcessorSignalEvaluateResponse](../../models/operations/processorsignalevaluateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_signal_return_report

Call the `/processor/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/processor/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

</api/processors/#processorsignalreturnreport>

### Example Usage

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

req = components.ProcessorSignalReturnReportRequest(
    client_transaction_id='string',
    processor_token='string',
    return_code='string',
)

res = s.plaid.processor_signal_return_report(req)

if res.processor_signal_return_report_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.ProcessorSignalReturnReportRequest](../../models/components/processorsignalreturnreportrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.ProcessorSignalReturnReportResponse](../../models/operations/processorsignalreturnreportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_stripe_bank_account_token_create


Used to create a token suitable for sending to Stripe to enable Plaid-Stripe integrations. For a detailed guide on integrating Stripe, see [Add Stripe to your app](https://plaid.com/docs/auth/partnerships/stripe/).

Note that the Stripe bank account token is a one-time use token. To store bank account information for later use, you can use a Stripe customer object and create an associated bank account from the token, or you can use a Stripe Custom account and create an associated external bank account from the token. This bank account information should work indefinitely, unless the user's bank account information changes or they revoke Plaid's permissions to access their account. Stripe bank account information cannot be modified once the bank account token has been created. If you ever need to change the bank account details used by Stripe for a specific customer, have the user go through Link again and create a new bank account token from the new `access_token`.

Bank account tokens can also be revoked, using `/item/remove`.

</api/processors/#processorstripebank_account_tokencreate>

### Example Usage

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

req = components.ProcessorStripeBankAccountTokenCreateRequest(
    access_token='string',
    account_id='string',
)

res = s.plaid.processor_stripe_bank_account_token_create(req)

if res.processor_stripe_bank_account_token_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [components.ProcessorStripeBankAccountTokenCreateRequest](../../models/components/processorstripebankaccounttokencreaterequest.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.ProcessorStripeBankAccountTokenCreateResponse](../../models/operations/processorstripebankaccounttokencreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_token_create

Used to create a token suitable for sending to one of Plaid's partners to enable integrations. Note that Stripe partnerships use bank account tokens instead; see `/processor/stripe/bank_account_token/create` for creating tokens for use with Stripe integrations. Once created, a processor token for a given Item cannot be modified or updated. If the account must be linked to a new or different partner resource, create a new Item by having the user go through the Link flow again; a new processor token can then be created from the new `access_token`. Processor tokens can also be revoked, using `/item/remove`.

</api/processors/#processortokencreate>

### Example Usage

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

req = components.ProcessorTokenCreateRequest(
    access_token='string',
    account_id='string',
    processor=components.Processor.OCROLUS,
)

res = s.plaid.processor_token_create(req)

if res.processor_token_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.ProcessorTokenCreateRequest](../../models/components/processortokencreaterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.ProcessorTokenCreateResponse](../../models/operations/processortokencreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_token_permissions_get

Used to get a processor token's product permissions. The `products` field will be an empty list if the processor can access all available products.

</api/processors/#processortokenpermissionsget>

### Example Usage

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

req = components.ProcessorTokenPermissionsGetRequest(
    processor_token='string',
)

res = s.plaid.processor_token_permissions_get(req)

if res.processor_token_permissions_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [components.ProcessorTokenPermissionsGetRequest](../../models/components/processortokenpermissionsgetrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.ProcessorTokenPermissionsGetResponse](../../models/operations/processortokenpermissionsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_token_permissions_set

Used to control a processor's access to products on the given processor token. By default, a processor will have access to all available products on the corresponding item. To restrict access to a particular set of products, call this endpoint with the desired products. To restore access to all available products, call this endpoint with an empty list. This endpoint can be called multiple times as your needs and your processor's needs change.

</api/processors/#processortokenpermissionsset>

### Example Usage

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

req = components.ProcessorTokenPermissionsSetRequest(
    processor_token='string',
    products=[
        components.Products.INVESTMENTS_AUTH,
    ],
)

res = s.plaid.processor_token_permissions_set(req)

if res.processor_token_permissions_set_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [components.ProcessorTokenPermissionsSetRequest](../../models/components/processortokenpermissionssetrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.ProcessorTokenPermissionsSetResponse](../../models/operations/processortokenpermissionssetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_token_webhook_update

This endpoint allows you to update the webhook URL associated with a processor token. This request triggers a `WEBHOOK_UPDATE_ACKNOWLEDGED` webhook to the newly specified webhook URL.

</api/processors/#processortokenwebhookupdate>

### Example Usage

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

req = components.ProcessorTokenWebhookUpdateRequest(
    processor_token='string',
    webhook='string',
)

res = s.plaid.processor_token_webhook_update(req)

if res.processor_token_webhook_update_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.ProcessorTokenWebhookUpdateRequest](../../models/components/processortokenwebhookupdaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.ProcessorTokenWebhookUpdateResponse](../../models/operations/processortokenwebhookupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_transactions_get

The `/processor/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/processor/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).

Due to the potentially large number of transactions associated with a processor token, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.

Data returned by `/processor/transactions/get` will be the data available for the processor token as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. To force Plaid to check for new transactions, you can use the `/processor/transactions/refresh` endpoint.

Note that data may not be immediately available to `/processor/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/processor/transactions/get`, if it wasn't. If no transaction history is ready when `/processor/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

To receive Transactions webhooks for a processor token, set its webhook URL via the [`/processor/token/webhook/update`](https://plaid.com/docs/api/processors/#processortokenwebhookupdate) endpoint.

</api/processors/#processortransactionsget>

### Example Usage

```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.ProcessorTransactionsGetRequest(
    end_date=dateutil.parser.parse('2022-04-08').date(),
    processor_token='string',
    start_date=dateutil.parser.parse('2023-04-01').date(),
)

res = s.plaid.processor_transactions_get(req)

if res.processor_transactions_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.ProcessorTransactionsGetRequest](../../models/components/processortransactionsgetrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.ProcessorTransactionsGetResponse](../../models/operations/processortransactionsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_transactions_recurring_get

The `/processor/transactions/recurring/get` endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user’s checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.

This endpoint is offered as an add-on to Transactions. To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

This endpoint can only be called on a processor token that has already been initialized with Transactions (either during Link, by specifying it in `/link/token/create`; or after Link, by calling `/processor/transactions/get` or `/processor/transactions/sync`). Once all historical transactions have been fetched, call `/processor/transactions/recurring/get` to receive the Recurring Transactions streams and subscribe to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook. To know when historical transactions have been fetched, if you are using `/processor/transactions/sync` listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#SyncUpdatesAvailableWebhook-historical-update-complete) webhook and check that the `historical_update_complete` field in the payload is `true`. If using `/processor/transactions/get`, listen for the [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhook.

After the initial call, you can call `/processor/transactions/recurring/get` endpoint at any point in the future to retrieve the latest summary of recurring streams. Listen to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook to be notified when new updates are available.

To receive Transactions webhooks for a processor token, set its webhook URL via the [`/processor/token/webhook/update`](https://plaid.com/docs/api/processors/#processortokenwebhookupdate) endpoint.

</api/processors/#processortransactionsrecurringget>

### Example Usage

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

req = components.ProcessorTransactionsRecurringGetRequest(
    account_ids=[
        'string',
    ],
    processor_token='string',
)

res = s.plaid.processor_transactions_recurring_get(req)

if res.processor_transactions_recurring_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [components.ProcessorTransactionsRecurringGetRequest](../../models/components/processortransactionsrecurringgetrequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.ProcessorTransactionsRecurringGetResponse](../../models/operations/processortransactionsrecurringgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_transactions_refresh

`/processor/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for a processor token. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled processor token. If changes to transactions are discovered after calling `/processor/transactions/refresh`, Plaid will fire a webhook: for `/transactions/sync` users, [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) will be fired if there are any transactions updated, added, or removed. For users of both `/processor/transactions/sync` and `/processor/transactions/get`, [`TRANSACTIONS_REMOVED`](https://plaid.com/docs/api/products/transactions/#transactions_removed) will be fired if any removed transactions are detected, and [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/transactions/#default_update) will be fired if any new transactions are detected. New transactions can be fetched by calling `/processor/transactions/get` or `/processor/transactions/sync`. Note that the `/processor/transactions/refresh` endpoint is not supported for Capital One (`ins_128026`) and will result in a `PRODUCT_NOT_SUPPORTED` error if called on a processor token from that institution.

`/processor/transactions/refresh` is offered as an add-on to Transactions and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

</api/processors/#processortransactionsrefresh>

### Example Usage

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

req = components.ProcessorTransactionsRefreshRequest(
    processor_token='string',
)

res = s.plaid.processor_transactions_refresh(req)

if res.processor_transactions_refresh_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [components.ProcessorTransactionsRefreshRequest](../../models/components/processortransactionsrefreshrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.ProcessorTransactionsRefreshResponse](../../models/operations/processortransactionsrefreshresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## processor_transactions_sync

This endpoint replaces `/processor/transactions/get` and its associated webhooks for most common use-cases.

The `/processor/transactions/sync` endpoint allows developers to subscribe to all transactions associated with a processor token and get updates synchronously in a stream-like manner, using a cursor to track which updates have already been seen. `/processor/transactions/sync` provides the same functionality as `/processor/transactions/get` and can be used instead of `/processor/transactions/get` to simplify the process of tracking transactions updates.

This endpoint provides user-authorized transaction data for `credit`, `depository`, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from `investments` accounts, use `/investments/transactions/get` instead.

Returned transactions data is grouped into three types of update, indicating whether the transaction was added, removed, or modified since the last call to the API.

In the first call to `/processor/transactions/sync` for a processor token, the endpoint will return all historical transactions data associated with that processor token up until the time of the API call (as "adds"), which then generates a `next_cursor` for that processor token. In subsequent calls, send the `next_cursor` to receive only the changes that have occurred since the previous call.

Due to the potentially large number of transactions associated with a processor token, results are paginated. The `has_more` field specifies if additional calls are necessary to fetch all available transaction updates. Call `/processor/transactions/sync` with the new cursor, pulling all updates, until `has_more` is `false`.

When retrieving paginated updates, track both the `next_cursor` from the latest response and the original cursor from the first call in which `has_more` was `true`; if a call to `/processor/transactions/sync` fails when retrieving a paginated update, which can occur as a result of the [`TRANSACTIONS_SYNC_MUTATION_DURING_PAGINATION`](https://plaid.com/docs/errors/transactions/#transactions_sync_mutation_during_pagination) error, the entire pagination request loop must be restarted beginning with the cursor for the first page of the update, rather than retrying only the single request that failed.

Whenever new or updated transaction data becomes available, `/processor/transactions/sync` will provide these updates. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. To force Plaid to check for new transactions, use the `/processor/transactions/refresh` endpoint.

Note that for newly created processor tokens, data may not be immediately available to `/processor/transactions/sync`. Plaid begins preparing transactions data when the corresponding Item is created, but the process can take anywhere from a few seconds to several minutes to complete, depending on the number of transactions available.

To receive Transactions webhooks for a processor token, set its webhook URL via the [`/processor/token/webhook/update`](https://plaid.com/docs/api/processors/#processortokenwebhookupdate) endpoint.

</api/processors/#processortransactionssync>

### Example Usage

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

req = components.ProcessorTransactionsSyncRequest(
    processor_token='string',
)

res = s.plaid.processor_transactions_sync(req)

if res.processor_transactions_sync_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [components.ProcessorTransactionsSyncRequest](../../models/components/processortransactionssyncrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.ProcessorTransactionsSyncResponse](../../models/operations/processortransactionssyncresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_bank_income_fire_webhook

Use the `/sandbox/bank_income/fire_webhook` endpoint to manually trigger a Bank Income webhook in the Sandbox environment.

</api/sandbox/#sandboxbankincomefire_webhook>

### Example Usage

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

req = components.SandboxBankIncomeFireWebhookRequest(
    webhook_code=components.SandboxBankIncomeWebhookFireRequestWebhookCode.BANK_INCOME_REFRESH_UPDATE,
    webhook_fields=components.SandboxBankIncomeWebhookFireRequestWebhookFields(
        user_id='string',
    ),
)

res = s.plaid.sandbox_bank_income_fire_webhook(req)

if res.sandbox_bank_income_fire_webhook_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [components.SandboxBankIncomeFireWebhookRequest](../../models/components/sandboxbankincomefirewebhookrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.SandboxBankIncomeFireWebhookResponse](../../models/operations/sandboxbankincomefirewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_bank_transfer_fire_webhook

Use the `/sandbox/bank_transfer/fire_webhook` endpoint to manually trigger a Bank Transfers webhook in the Sandbox environment.

</bank-transfers/reference/#sandboxbank_transferfire_webhook>

### Example Usage

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

req = components.SandboxBankTransferFireWebhookRequest(
    webhook='string',
)

res = s.plaid.sandbox_bank_transfer_fire_webhook(req)

if res.sandbox_bank_transfer_fire_webhook_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [components.SandboxBankTransferFireWebhookRequest](../../models/components/sandboxbanktransferfirewebhookrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.SandboxBankTransferFireWebhookResponse](../../models/operations/sandboxbanktransferfirewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_bank_transfer_simulate

Use the `/sandbox/bank_transfer/simulate` endpoint to simulate a bank transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/bank_transfer/event/sync` or `/bank_transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

</bank-transfers/reference/#sandboxbank_transfersimulate>

### Example Usage

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

req = components.SandboxBankTransferSimulateRequest(
    bank_transfer_id='string',
    event_type='string',
)

res = s.plaid.sandbox_bank_transfer_simulate(req)

if res.sandbox_bank_transfer_simulate_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.SandboxBankTransferSimulateRequest](../../models/components/sandboxbanktransfersimulaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.SandboxBankTransferSimulateResponse](../../models/operations/sandboxbanktransfersimulateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_income_fire_webhook

Use the `/sandbox/income/fire_webhook` endpoint to manually trigger a Payroll Income webhook in the Sandbox environment.

</api/sandbox/#sandboxincomefire_webhook>

### Example Usage

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

req = components.SandboxIncomeFireWebhookRequest(
    item_id='string',
    verification_status=components.SandboxIncomeFireWebhookRequestVerificationStatus.VERIFICATION_STATUS_PENDING_APPROVAL,
    webhook='string',
)

res = s.plaid.sandbox_income_fire_webhook(req)

if res.sandbox_income_fire_webhook_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.SandboxIncomeFireWebhookRequest](../../models/components/sandboxincomefirewebhookrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.SandboxIncomeFireWebhookResponse](../../models/operations/sandboxincomefirewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_item_fire_webhook

The `/sandbox/item/fire_webhook` endpoint is used to test that code correctly handles webhooks. This endpoint can trigger the following webhooks:

`DEFAULT_UPDATE`: Transactions update webhook to be fired for a given Sandbox Item. If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`NEW_ACCOUNTS_AVAILABLE`: Webhook to be fired for a given Sandbox Item created with Account Select v2.

`AUTH_DATA_UPDATE`: Webhook to be fired for a given Sandbox Item created with Auth as an enabled product.

`RECURRING_TRANSACTIONS_UPDATE`: Recurring Transactions webhook to be fired for a given Sandbox Item. If the Item does not support Recurring Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`SYNC_UPDATES_AVAILABLE`: Transactions webhook to be fired for a given Sandbox Item.  If the Item does not support Transactions, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`PRODUCT_READY`: Assets webhook to be fired when a given asset report has been successfully generated. If the Item does not support Assets, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

`ERROR`: Assets webhook to be fired when asset report generation has failed. If the Item does not support Assets, a `SANDBOX_PRODUCT_NOT_ENABLED` error will result.

Note that this endpoint is provided for developer ease-of-use and is not required for testing webhooks; webhooks will also fire in Sandbox under the same conditions that they would in Production or Development.

</api/sandbox/#sandboxitemfire_webhook>

### Example Usage

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

req = components.SandboxItemFireWebhookRequest(
    access_token='string',
    webhook_code=components.WebhookCode.DEFAULT_UPDATE,
)

res = s.plaid.sandbox_item_fire_webhook(req)

if res.sandbox_item_fire_webhook_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.SandboxItemFireWebhookRequest](../../models/components/sandboxitemfirewebhookrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.SandboxItemFireWebhookResponse](../../models/operations/sandboxitemfirewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_item_reset_login

`/sandbox/item/reset_login/` forces an Item into an `ITEM_LOGIN_REQUIRED` state in order to simulate an Item whose login is no longer valid. This makes it easy to test Link's [update mode](https://plaid.com/docs/link/update-mode) flow in the Sandbox environment.  After calling `/sandbox/item/reset_login`, You can then use Plaid Link update mode to restore the Item to a good state. An `ITEM_LOGIN_REQUIRED` webhook will also be fired after a call to this endpoint, if one is associated with the Item.


In the Sandbox, Items will transition to an `ITEM_LOGIN_REQUIRED` error state automatically after 30 days, even if this endpoint is not called.

</api/sandbox/#sandboxitemreset_login>

### Example Usage

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

req = components.SandboxItemResetLoginRequest(
    access_token='string',
)

res = s.plaid.sandbox_item_reset_login(req)

if res.sandbox_item_reset_login_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.SandboxItemResetLoginRequest](../../models/components/sandboxitemresetloginrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.SandboxItemResetLoginResponse](../../models/operations/sandboxitemresetloginresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_item_set_verification_status

The `/sandbox/item/set_verification_status` endpoint can be used to change the verification status of an Item in in the Sandbox in order to simulate the Automated Micro-deposit flow.

Note that not all Plaid developer accounts are enabled for micro-deposit based verification by default. Your account must be enabled for this feature in order to test it in Sandbox. To enable this features or check your status, contact your account manager or [submit a product access Support ticket](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/request-product-access).

For more information on testing Automated Micro-deposits in Sandbox, see [Auth full coverage testing](https://plaid.com/docs/auth/coverage/testing#).

</api/sandbox/#sandboxitemset_verification_status>

### Example Usage

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

req = components.SandboxItemSetVerificationStatusRequest(
    access_token='string',
    account_id='string',
    verification_status=components.SandboxItemSetVerificationStatusRequestVerificationStatus.AUTOMATICALLY_VERIFIED,
)

res = s.plaid.sandbox_item_set_verification_status(req)

if res.sandbox_item_set_verification_status_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [components.SandboxItemSetVerificationStatusRequest](../../models/components/sandboxitemsetverificationstatusrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.SandboxItemSetVerificationStatusResponse](../../models/operations/sandboxitemsetverificationstatusresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_oauth_select_accounts

Save the selected accounts when connecting to the Platypus Oauth institution

### Example Usage

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

req = components.SandboxOauthSelectAccountsRequest(
    accounts=[
        'string',
    ],
    oauth_state_id='string',
)

res = s.plaid.sandbox_oauth_select_accounts(req)

if res.sandbox_oauth_select_accounts_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.SandboxOauthSelectAccountsRequest](../../models/components/sandboxoauthselectaccountsrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.SandboxOauthSelectAccountsResponse](../../models/operations/sandboxoauthselectaccountsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_payment_profile_reset_login

`/sandbox/payment_profile/reset_login/` forces a Payment Profile into a state where the login is no longer valid. This makes it easy to test update mode for Payment Profile in the Sandbox environment.

 After calling `/sandbox/payment_profile/reset_login`, calls to the `/transfer/authorization/create` with the Payment Profile will result in a `decision_rationale` `PAYMENT_PROFILE_LOGIN_REQUIRED`. You can then use update mode for Payment Profile to restore it into a good state.

 In order to invoke this endpoint, you must first [create a Payment Profile](https://plaid.com/docs/transfer/add-to-app/#create-a-payment-profile-optional) and [go through the Link flow](https://plaid.com/docs/transfer/add-to-app/#create-a-link-token).

</api/sandbox/#sandboxpayment_profilereset_login>

### Example Usage

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

req = components.SandboxPaymentProfileResetLoginRequest(
    payment_profile_token='string',
)

res = s.plaid.sandbox_payment_profile_reset_login(req)

if res.sandbox_payment_profile_reset_login_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [components.SandboxPaymentProfileResetLoginRequest](../../models/components/sandboxpaymentprofileresetloginrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.SandboxPaymentProfileResetLoginResponse](../../models/operations/sandboxpaymentprofileresetloginresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_processor_token_create

Use the `/sandbox/processor_token/create` endpoint to create a valid `processor_token` for an arbitrary institution ID and test credentials. The created `processor_token` corresponds to a new Sandbox Item. You can then use this `processor_token` with the `/processor/` API endpoints in Sandbox. You can also use `/sandbox/processor_token/create` with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data.

</api/sandbox/#sandboxprocessor_tokencreate>

### Example Usage

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

req = components.SandboxProcessorTokenCreateRequest(
    institution_id='string',
)

res = s.plaid.sandbox_processor_token_create(req)

if res.sandbox_processor_token_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.SandboxProcessorTokenCreateRequest](../../models/components/sandboxprocessortokencreaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.SandboxProcessorTokenCreateResponse](../../models/operations/sandboxprocessortokencreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_public_token_create

Use the `/sandbox/public_token/create` endpoint to create a valid `public_token`  for an arbitrary institution ID, initial products, and test credentials. The created `public_token` maps to a new Sandbox Item. You can then call `/item/public_token/exchange` to exchange the `public_token` for an `access_token` and perform all API actions. `/sandbox/public_token/create` can also be used with the [`user_custom` test username](https://plaid.com/docs/sandbox/user-custom) to generate a test account with custom data. `/sandbox/public_token/create` cannot be used with OAuth institutions.

</api/sandbox/#sandboxpublic_tokencreate>

### Example Usage

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

req = components.SandboxPublicTokenCreateRequest(
    initial_products=[
        components.Products.STANDING_ORDERS,
    ],
    institution_id='string',
)

res = s.plaid.sandbox_public_token_create(req)

if res.sandbox_public_token_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.SandboxPublicTokenCreateRequest](../../models/components/sandboxpublictokencreaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.SandboxPublicTokenCreateResponse](../../models/operations/sandboxpublictokencreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_transfer_fire_webhook

Use the `/sandbox/transfer/fire_webhook` endpoint to manually trigger a Transfer webhook in the Sandbox environment.

</api/sandbox/#sandboxtransferfire_webhook>

### Example Usage

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

req = components.SandboxTransferFireWebhookRequest(
    webhook='string',
)

res = s.plaid.sandbox_transfer_fire_webhook(req)

if res.sandbox_transfer_fire_webhook_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [components.SandboxTransferFireWebhookRequest](../../models/components/sandboxtransferfirewebhookrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.SandboxTransferFireWebhookResponse](../../models/operations/sandboxtransferfirewebhookresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_transfer_repayment_simulate

Use the `/sandbox/transfer/repayment/simulate` endpoint to trigger the creation of a repayment. As a side effect of calling this route, a repayment is created that includes all unreimbursed returns of guaranteed transfers. If there are no such returns, an 400 error is returned.

</api/sandbox/#sandboxtransferrepaymentsimulate>

### Example Usage

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

req = components.SandboxTransferRepaymentSimulateRequest()

res = s.plaid.sandbox_transfer_repayment_simulate(req)

if res.sandbox_transfer_repayment_simulate_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [components.SandboxTransferRepaymentSimulateRequest](../../models/components/sandboxtransferrepaymentsimulaterequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.SandboxTransferRepaymentSimulateResponse](../../models/operations/sandboxtransferrepaymentsimulateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_transfer_simulate

Use the `/sandbox/transfer/simulate` endpoint to simulate a transfer event in the Sandbox environment.  Note that while an event will be simulated and will appear when using endpoints such as `/transfer/event/sync` or `/transfer/event/list`, no transactions will actually take place and funds will not move between accounts, even within the Sandbox.

</api/sandbox/#sandboxtransfersimulate>

### Example Usage

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

req = components.SandboxTransferSimulateRequest(
    event_type='string',
    transfer_id='string',
)

res = s.plaid.sandbox_transfer_simulate(req)

if res.sandbox_transfer_simulate_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.SandboxTransferSimulateRequest](../../models/components/sandboxtransfersimulaterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.SandboxTransferSimulateResponse](../../models/operations/sandboxtransfersimulateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_transfer_sweep_simulate

Use the `/sandbox/transfer/sweep/simulate` endpoint to create a sweep and associated events in the Sandbox environment. Upon calling this endpoint, all `posted` or `pending` transfers with a sweep status of `unswept` will become `swept`, and all `returned` transfers with a sweep status of `swept` will become `return_swept`.

</api/sandbox/#sandboxtransfersweepsimulate>

### Example Usage

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

req = components.SandboxTransferSweepSimulateRequest()

res = s.plaid.sandbox_transfer_sweep_simulate(req)

if res.sandbox_transfer_sweep_simulate_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [components.SandboxTransferSweepSimulateRequest](../../models/components/sandboxtransfersweepsimulaterequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.SandboxTransferSweepSimulateResponse](../../models/operations/sandboxtransfersweepsimulateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_transfer_test_clock_advance

Use the `/sandbox/transfer/test_clock/advance` endpoint to advance a `test_clock` in the Sandbox environment.

A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. A test clock can be advanced by incrementing `virtual_time`, but may never go back to a lower `virtual_time`.

If a test clock is advanced, we will simulate the changes that ought to occur during the time that elapsed.
For instance, a client creates a weekly recurring transfer with a test clock set at t. When the client advances the test clock by setting `virtual_time` = t + 15 days, 2 new originations should be created, along with the webhook events.

The advancement of the test clock from its current `virtual_time` should be limited such that there are no more than 20 originations resulting from the advance operation on each `recurring_transfer` associated with the `test_clock`.
For instance, if the recurring transfer associated with this test clock originates once every 4 weeks, you can advance the `virtual_time` up to 80 weeks on each API call.

</api/sandbox/#sandboxtransfertest_clockadvance>

### Example Usage

```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.SandboxTransferTestClockAdvanceRequest(
    new_virtual_time=dateutil.parser.isoparse('2022-11-02T22:51:40.374Z'),
    test_clock_id='string',
)

res = s.plaid.sandbox_transfer_test_clock_advance(req)

if res.sandbox_transfer_test_clock_advance_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [components.SandboxTransferTestClockAdvanceRequest](../../models/components/sandboxtransfertestclockadvancerequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.SandboxTransferTestClockAdvanceResponse](../../models/operations/sandboxtransfertestclockadvanceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_transfer_test_clock_create

Use the `/sandbox/transfer/test_clock/create` endpoint to create a `test_clock` in the Sandbox environment.

A test clock object represents an independent timeline and has a `virtual_time` field indicating the current timestamp of the timeline. Test clocks are used for testing recurring transfers in Sandbox.

A test clock can be associated with up to 5 recurring transfers.

</api/sandbox/#sandboxtransfertest_clockcreate>

### Example Usage

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

req = components.SandboxTransferTestClockCreateRequest()

res = s.plaid.sandbox_transfer_test_clock_create(req)

if res.sandbox_transfer_test_clock_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [components.SandboxTransferTestClockCreateRequest](../../models/components/sandboxtransfertestclockcreaterequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.SandboxTransferTestClockCreateResponse](../../models/operations/sandboxtransfertestclockcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_transfer_test_clock_get

Use the `/sandbox/transfer/test_clock/get` endpoint to get a `test_clock` in the Sandbox environment.

</api/sandbox/#sandboxtransfertest_clockget>

### Example Usage

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

req = components.SandboxTransferTestClockGetRequest(
    test_clock_id='string',
)

res = s.plaid.sandbox_transfer_test_clock_get(req)

if res.sandbox_transfer_test_clock_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.SandboxTransferTestClockGetRequest](../../models/components/sandboxtransfertestclockgetrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.SandboxTransferTestClockGetResponse](../../models/operations/sandboxtransfertestclockgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## sandbox_transfer_test_clock_list

Use the `/sandbox/transfer/test_clock/list` endpoint to see a list of all your test clocks in the Sandbox environment, by ascending `virtual_time`. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired test clocks.

</api/sandbox/#sandboxtransfertest_clocklist>

### Example Usage

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

req = components.SandboxTransferTestClockListRequest()

res = s.plaid.sandbox_transfer_test_clock_list(req)

if res.sandbox_transfer_test_clock_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [components.SandboxTransferTestClockListRequest](../../models/components/sandboxtransfertestclocklistrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.SandboxTransferTestClockListResponse](../../models/operations/sandboxtransfertestclocklistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## signal_decision_report

After calling `/signal/evaluate`, call `/signal/decision/report` to report whether the transaction was initiated. This endpoint will return an [`INVALID_FIELD`](/docs/errors/invalid-request/#invalid_field) error if called a second time with a different value for `initiated`.

</api/products/signal#signaldecisionreport>

### Example Usage

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

req = components.SignalDecisionReportRequest(
    client_transaction_id='string',
    initiated=False,
)

res = s.plaid.signal_decision_report(req)

if res.signal_decision_report_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.SignalDecisionReportRequest](../../models/components/signaldecisionreportrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.SignalDecisionReportResponse](../../models/operations/signaldecisionreportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## signal_evaluate

Use `/signal/evaluate` to evaluate a planned ACH transaction to get a return risk assessment (such as a risk score and risk tier) and additional risk signals.

In order to obtain a valid score for an ACH transaction, Plaid must have an access token for the account, and the Item must be healthy (receiving product updates) or have recently been in a healthy state. If the transaction does not meet eligibility requirements, an error will be returned corresponding to the underlying cause. If `/signal/evaluate` is called on the same transaction multiple times within a 24-hour period, cached results may be returned. For more information please refer to the error documentation on [Item errors](/docs/errors/item/) and [Link in Update Mode](/docs/link/update-mode/).

Note: This request may take some time to complete if Signal is being added to an existing Item. This is because Plaid must communicate directly with the institution when retrieving the data for the first time.

</api/products/signal#signalevaluate>

### Example Usage

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

req = components.SignalEvaluateRequest(
    access_token='string',
    account_id='string',
    amount=306.52,
    client_transaction_id='string',
)

res = s.plaid.signal_evaluate(req)

if res.signal_evaluate_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.SignalEvaluateRequest](../../models/components/signalevaluaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.SignalEvaluateResponse](../../models/operations/signalevaluateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## signal_prepare

When Link is not initialized with Signal, call `/signal/prepare` to opt-in that Item to the Signal data collection process, developing a Signal score.

If you are using other Plaid products after Link, e.g. Identity or Assets, call `/signal/prepare` after those product calls are complete.

Example flow: Link is initialized with Auth, call `/auth/get` for the account and routing number, call `/identity/get` to retrieve bank ownership details, then call `/signal/prepare` to begin Signal data collection. Later, once you have obtained details about the proposed transaction from the user, call `/signal/evaluate` for a Signal score. For more information please see [Recommendations for initializing Link with specific product combinations](https://www.plaid.com/docs/link/initializing-products/#recommendations-for-initializing-link-with-specific-product-combinations).

</api/products/signal#signalprepare>

### Example Usage

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

req = components.SignalPrepareRequest(
    access_token='string',
)

res = s.plaid.signal_prepare(req)

if res.signal_prepare_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.SignalPrepareRequest](../../models/components/signalpreparerequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.SignalPrepareResponse](../../models/operations/signalprepareresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## signal_return_report

Call the `/signal/return/report` endpoint to report a returned transaction that was previously sent to the `/signal/evaluate` endpoint. Your feedback will be used by the model to incorporate the latest risk trend in your portfolio.

</api/products/signal#signalreturnreport>

### Example Usage

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

req = components.SignalReturnReportRequest(
    client_transaction_id='string',
    return_code='string',
)

res = s.plaid.signal_return_report(req)

if res.signal_return_report_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.SignalReturnReportRequest](../../models/components/signalreturnreportrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.SignalReturnReportResponse](../../models/operations/signalreturnreportresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## statements_download

The `/statements/download` endpoint retrieves a single statement.

</none/>

### Example Usage

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

req = components.StatementsDownloadRequest(
    access_token='string',
    statement_id='string',
)

res = s.plaid.statements_download(req)

if res.statements_download_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.StatementsDownloadRequest](../../models/components/statementsdownloadrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.StatementsDownloadResponse](../../models/operations/statementsdownloadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## statements_list

The `/statements/list` endpoint retrieves a list of all statements associated with the provided item.

</none/>

### Example Usage

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

req = components.StatementsListRequest(
    access_token='string',
)

res = s.plaid.statements_list(req)

if res.statements_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.StatementsListRequest](../../models/components/statementslistrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.StatementsListResponse](../../models/operations/statementslistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transactions_enhance

The `/beta/transactions/v1/enhance` endpoint enriches raw transaction data provided directly by clients.

The product is currently in beta.

### Example Usage

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

req = components.TransactionsEnhanceGetRequest(
    account_type='string',
    transactions=[
        components.ClientProvidedRawTransaction(
            amount=8716.21,
            description='Integrated user-facing model',
            id='<ID>',
            iso_currency_code='string',
        ),
    ],
)

res = s.plaid.transactions_enhance(req)

if res.transactions_enhance_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.TransactionsEnhanceGetRequest](../../models/components/transactionsenhancegetrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.TransactionsEnhanceResponse](../../models/operations/transactionsenhanceresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transactions_enrich

The `/transactions/enrich` endpoint enriches raw transaction data generated by your own banking products or retrieved from other non-Plaid sources.

</api/products/enrich/#transactionsenrich>

### Example Usage

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

req = components.TransactionsEnrichGetRequest(
    account_type='string',
    transactions=[
        components.ClientProvidedTransaction(
            amount=9570.07,
            description='Multi-lateral secondary customer loyalty',
            direction=components.EnrichTransactionDirection.INFLOW,
            id='<ID>',
            iso_currency_code='string',
        ),
    ],
)

res = s.plaid.transactions_enrich(req)

if res.transactions_enrich_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.TransactionsEnrichGetRequest](../../models/components/transactionsenrichgetrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.TransactionsEnrichResponse](../../models/operations/transactionsenrichresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transactions_get

Note: All new implementations are encouraged to use `/transactions/sync` rather than `/transactions/get`. `/transactions/sync` provides the same functionality as `/transactions/get` and improves developer ease-of-use for handling transactions updates.

The `/transactions/get` endpoint allows developers to receive user-authorized transaction data for credit, depository, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from investments accounts, use the [Investments endpoint](https://plaid.com/docs/api/products/investments/) instead. Transaction data is standardized across financial institutions, and in many cases transactions are linked to a clean name, entity type, location, and category. Similarly, account data is standardized and returned with a clean name, number, balance, and other meta information where available.

Transactions are returned in reverse-chronological order, and the sequence of transaction ordering is stable and will not shift.  Transactions are not immutable and can also be removed altogether by the institution; a removed transaction will no longer appear in `/transactions/get`.  For more details, see [Pending and posted transactions](https://plaid.com/docs/transactions/transactions-data/#pending-and-posted-transactions).

Due to the potentially large number of transactions associated with an Item, results are paginated. Manipulate the `count` and `offset` parameters in conjunction with the `total_transactions` response body field to fetch all available transactions.

Data returned by `/transactions/get` will be the data available for the Item as of the most recent successful check for new transactions. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, you can use the `/transactions/refresh` endpoint.

Note that data may not be immediately available to `/transactions/get`. Plaid will begin to prepare transactions data upon Item link, if Link was initialized with `transactions`, or upon the first call to `/transactions/get`, if it wasn't. To be alerted when transaction data is ready to be fetched, listen for the [`INITIAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#initial_update) and [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhooks. If no transaction history is ready when `/transactions/get` is called, it will return a `PRODUCT_NOT_READY` error.

</api/products/transactions/#transactionsget>

### Example Usage

```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.TransactionsGetRequest(
    access_token='string',
    end_date=dateutil.parser.parse('2022-06-27').date(),
    start_date=dateutil.parser.parse('2023-07-17').date(),
)

res = s.plaid.transactions_get(req)

if res.transactions_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.TransactionsGetRequest](../../models/components/transactionsgetrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.TransactionsGetResponse](../../models/operations/transactionsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transactions_recurring_get

The `/transactions/recurring/get` endpoint allows developers to receive a summary of the recurring outflow and inflow streams (expenses and deposits) from a user’s checking, savings or credit card accounts. Additionally, Plaid provides key insights about each recurring stream including the category, merchant, last amount, and more. Developers can use these insights to build tools and experiences that help their users better manage cash flow, monitor subscriptions, reduce spend, and stay on track with bill payments.

This endpoint is offered as an add-on to Transactions. To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

This endpoint can only be called on an Item that has already been initialized with Transactions (either during Link, by specifying it in `/link/token/create`; or after Link, by calling `/transactions/get` or `/transactions/sync`). Once all historical transactions have been fetched, call `/transactions/recurring/get` to receive the Recurring Transactions streams and subscribe to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook. To know when historical transactions have been fetched, if you are using `/transactions/sync` listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#SyncUpdatesAvailableWebhook-historical-update-complete) webhook and check that the `historical_update_complete` field in the payload is `true`. If using `/transactions/get`, listen for the [`HISTORICAL_UPDATE`](https://plaid.com/docs/api/products/transactions/#historical_update) webhook.

After the initial call, you can call `/transactions/recurring/get` endpoint at any point in the future to retrieve the latest summary of recurring streams. Listen to the [`RECURRING_TRANSACTIONS_UPDATE`](https://plaid.com/docs/api/products/transactions/#recurring_transactions_update) webhook to be notified when new updates are available.

</api/products/transactions/#transactionsrecurringget>

### Example Usage

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

req = components.TransactionsRecurringGetRequest(
    access_token='string',
    account_ids=[
        'string',
    ],
)

res = s.plaid.transactions_recurring_get(req)

if res.transactions_recurring_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.TransactionsRecurringGetRequest](../../models/components/transactionsrecurringgetrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.TransactionsRecurringGetResponse](../../models/operations/transactionsrecurringgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transactions_refresh

`/transactions/refresh` is an optional endpoint for users of the Transactions product. It initiates an on-demand extraction to fetch the newest transactions for an Item. This on-demand extraction takes place in addition to the periodic extractions that automatically occur multiple times a day for any Transactions-enabled Item. If changes to transactions are discovered after calling `/transactions/refresh`, Plaid will fire a webhook: for `/transactions/sync` users, [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) will be fired if there are any transactions updated, added, or removed. For users of both `/transactions/sync` and `/transactions/get`, [`TRANSACTIONS_REMOVED`](https://plaid.com/docs/api/products/transactions/#transactions_removed) will be fired if any removed transactions are detected, and [`DEFAULT_UPDATE`](https://plaid.com/docs/api/products/transactions/#default_update) will be fired if any new transactions are detected. New transactions can be fetched by calling `/transactions/get` or `/transactions/sync`. Note that the `/transactions/refresh` endpoint is not supported for Capital One (`ins_128026`) and will result in a `PRODUCT_NOT_SUPPORTED` error if called on an Item from that institution.

`/transactions/refresh` is offered as an add-on to Transactions and has a separate [fee model](/docs/account/billing/#per-request-flat-fee). To request access to this endpoint, submit a [product access request](https://dashboard.plaid.com/team/products) or contact your Plaid account manager.

</api/products/transactions/#transactionsrefresh>

### Example Usage

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

req = components.TransactionsRefreshRequest(
    access_token='string',
)

res = s.plaid.transactions_refresh(req)

if res.transactions_refresh_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [components.TransactionsRefreshRequest](../../models/components/transactionsrefreshrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.TransactionsRefreshResponse](../../models/operations/transactionsrefreshresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transactions_rules_create

The `/transactions/rules/v1/create` endpoint creates transaction categorization rules.

Rules will be applied on the Item's transactions returned in `/transactions/get` response.

The product is currently in beta. To request access, contact transactions-feedback@plaid.com.

### Example Usage

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

req = components.TransactionsRulesCreateRequest(
    access_token='string',
    personal_finance_category='string',
    rule_details=components.TransactionsRuleDetails(
        field=components.TransactionsRuleField.NAME,
        query='string',
        type=components.TransactionsRuleType.SUBSTRING_MATCH,
    ),
)

res = s.plaid.transactions_rules_create(req)

if res.transactions_rules_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.TransactionsRulesCreateRequest](../../models/components/transactionsrulescreaterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.TransactionsRulesCreateResponse](../../models/operations/transactionsrulescreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transactions_rules_list

The `/transactions/rules/v1/list` returns a list of transaction rules created for the Item associated with the access token.

### Example Usage

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

req = components.TransactionsRulesListRequest(
    access_token='string',
)

res = s.plaid.transactions_rules_list(req)

if res.transactions_rules_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.TransactionsRulesListRequest](../../models/components/transactionsruleslistrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.TransactionsRulesListResponse](../../models/operations/transactionsruleslistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transactions_rules_remove

The `/transactions/rules/v1/remove` endpoint is used to remove a transaction rule.

### Example Usage

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

req = components.TransactionsRulesRemoveRequest(
    access_token='string',
    rule_id='string',
)

res = s.plaid.transactions_rules_remove(req)

if res.transactions_rules_remove_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.TransactionsRulesRemoveRequest](../../models/components/transactionsrulesremoverequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.TransactionsRulesRemoveResponse](../../models/operations/transactionsrulesremoveresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transactions_sync

This endpoint replaces `/transactions/get` and its associated webhooks for most common use-cases.

The `/transactions/sync` endpoint allows developers to subscribe to all transactions associated with an Item and get updates synchronously in a stream-like manner, using a cursor to track which updates have already been seen. `/transactions/sync` provides the same functionality as `/transactions/get` and can be used instead of `/transactions/get` to simplify the process of tracking transactions updates.

This endpoint provides user-authorized transaction data for `credit`, `depository`, and some loan-type accounts (only those with account subtype `student`; coverage may be limited). For transaction history from `investments` accounts, use `/investments/transactions/get` instead.

Returned transactions data is grouped into three types of update, indicating whether the transaction was added, removed, or modified since the last call to the API.

In the first call to `/transactions/sync` for an Item, the endpoint will return all historical transactions data associated with that Item up until the time of the API call (as "adds"), which then generates a `next_cursor` for that Item. In subsequent calls, send the `next_cursor` to receive only the changes that have occurred since the previous call.

Due to the potentially large number of transactions associated with an Item, results are paginated. The `has_more` field specifies if additional calls are necessary to fetch all available transaction updates. Call `/transactions/sync` with the new cursor, pulling all updates, until `has_more` is `false`.

When retrieving paginated updates, track both the `next_cursor` from the latest response and the original cursor from the first call in which `has_more` was `true`; if a call to `/transactions/sync` fails due to the [`TRANSACTIONS_SYNC_MUTATION_DURING_PAGINATION`](https://plaid.com/docs/errors/transactions/#transactions_sync_mutation_during_pagination) error, the entire pagination request loop must be restarted beginning with the cursor for the first page of the update, rather than retrying only the single request that failed.

Whenever new or updated transaction data becomes available, `/transactions/sync` will provide these updates. Plaid typically checks for new data multiple times a day, but these checks may occur less frequently, such as once a day, depending on the institution. An Item's `status.transactions.last_successful_update` field will show the timestamp of the most recent successful update. To force Plaid to check for new transactions, use the `/transactions/refresh` endpoint.

Note that for newly created Items, data may not be immediately available to `/transactions/sync`. Plaid begins preparing transactions data when the Item is created, but the process can take anywhere from a few seconds to several minutes to complete, depending on the number of transactions available.

To be alerted when new data is available, listen for the [`SYNC_UPDATES_AVAILABLE`](https://plaid.com/docs/api/products/transactions/#sync_updates_available) webhook.

</api/products/transactions/#transactionssync>

### Example Usage

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

req = components.TransactionsSyncRequest(
    access_token='string',
)

res = s.plaid.transactions_sync(req)

if res.transactions_sync_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.TransactionsSyncRequest](../../models/components/transactionssyncrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.TransactionsSyncResponse](../../models/operations/transactionssyncresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_authorization_create

Use the `/transfer/authorization/create` endpoint to determine transfer failure risk.

In Plaid's Sandbox environment the decisions will be returned as follows:

  - To approve a transfer with null rationale code, make an authorization request with an `amount` less than the available balance in the account.

  - To approve a transfer with the rationale code `MANUALLY_VERIFIED_ITEM`, create an Item in Link through the [Same Day Micro-deposits flow](https://plaid.com/docs/auth/coverage/testing/#testing-same-day-micro-deposits).

  - To approve a transfer with the rationale code `ITEM_LOGIN_REQUIRED`, [reset the login for an Item](https://plaid.com/docs/sandbox/#item_login_required).

  - To decline a transfer with the rationale code `NSF`, the available balance on the account must be less than the authorization `amount`. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

  - To decline a transfer with the rationale code `RISK`, the available balance on the account must be exactly $0. See [Create Sandbox test data](https://plaid.com/docs/sandbox/user-custom/) for details on how to customize data in Sandbox.

The fields `device.ip_address` and `device.user_agent` are required for all sessions where the end-user is present. For example, when a user is authorizing a one-time payment from their device.

</api/products/transfer/#transferauthorizationcreate>

### Example Usage

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

req = components.TransferAuthorizationCreateRequest(
    amount='237.18',
    network=components.TransferNetwork.SAME_DAY_ACH,
    type=components.TransferType.CREDIT,
    user=components.TransferAuthorizationUserInRequest(
        legal_name='string',
    ),
)

res = s.plaid.transfer_authorization_create(req)

if res.transfer_authorization_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.TransferAuthorizationCreateRequest](../../models/components/transferauthorizationcreaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.TransferAuthorizationCreateResponse](../../models/operations/transferauthorizationcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_balance_get

Use the `/transfer/balance/get` endpoint to view a balance held with Plaid.

</api/products/transfer/#transferbalanceget>

### Example Usage

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

req = components.TransferBalanceGetRequest()

res = s.plaid.transfer_balance_get(req)

if res.transfer_balance_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.TransferBalanceGetRequest](../../models/components/transferbalancegetrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.TransferBalanceGetResponse](../../models/operations/transferbalancegetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_cancel

Use the `/transfer/cancel` endpoint to cancel a transfer.  A transfer is eligible for cancellation if the `cancellable` property returned by `/transfer/get` is `true`.

</api/products/transfer/#transfercancel>

### Example Usage

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

req = components.TransferCancelRequest(
    transfer_id='string',
)

res = s.plaid.transfer_cancel(req)

if res.transfer_cancel_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.TransferCancelRequest](../../models/components/transfercancelrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.TransferCancelResponse](../../models/operations/transfercancelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_capabilities_get

Use the `/transfer/capabilities/get` endpoint to determine the RTP eligibility information of a transfer.

</api/products/transfer/#transfercapabilitiesget>

### Example Usage

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

req = components.TransferCapabilitiesGetRequest()

res = s.plaid.transfer_capabilities_get(req)

if res.transfer_capabilities_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.TransferCapabilitiesGetRequest](../../models/components/transfercapabilitiesgetrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.TransferCapabilitiesGetResponse](../../models/operations/transfercapabilitiesgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_configuration_get

Use the `/transfer/configuration/get` endpoint to view your transfer product configurations.

</api/products/transfer/#transferconfigurationget>

### Example Usage

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

req = components.TransferConfigurationGetRequest()

res = s.plaid.transfer_configuration_get(req)

if res.transfer_configuration_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.TransferConfigurationGetRequest](../../models/components/transferconfigurationgetrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.TransferConfigurationGetResponse](../../models/operations/transferconfigurationgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_create

Use the `/transfer/create` endpoint to initiate a new transfer.

</api/products/transfer/#transfercreate>

### Example Usage

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

req = components.TransferCreateRequest(
    authorization_id='string',
    description='Horizontal incremental throughput',
)

res = s.plaid.transfer_create(req)

if res.transfer_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.TransferCreateRequest](../../models/components/transfercreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.TransferCreateResponse](../../models/operations/transfercreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_diligence_document_upload

Third-party sender customers can use `/transfer/diligence/document/upload` endpoint to upload a document on behalf of its end customer (i.e. originator) to Plaid. You’ll need to send a request of type multipart/form-data.
You must provide the `client_id` in the `PLAID-CLIENT-ID` header and `secret` in the `PLAID-SECRET` header.

</api/products/transfer/#transferdiligencedocumentupload>

### Example Usage

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

req = components.TransferDiligenceDocumentUploadRequest(
    file='0xe5B1847A81'.encode(),
    originator_client_id='string',
    purpose=components.TransferDocumentPurpose.DUE_DILIGENCE,
)

res = s.plaid.transfer_diligence_document_upload(req)

if res.transfer_diligence_document_upload_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [components.TransferDiligenceDocumentUploadRequest](../../models/components/transferdiligencedocumentuploadrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.TransferDiligenceDocumentUploadResponse](../../models/operations/transferdiligencedocumentuploadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_diligence_submit

Use the `/transfer/diligence/submit` endpoint to submit transfer diligence on behalf of the originator.

</api/products/transfer/#transferdiligencesubmit>

### Example Usage

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

req = components.TransferDiligenceSubmitRequest(
    originator_client_id='string',
    originator_diligence=components.TransferOriginatorDiligence(
        address=components.TransferOriginatorAddress(
            city='Hoboken',
            country_code='HT',
            postal_code='89621-1508',
            region='string',
            street='Jeramie Forge',
        ),
        dba='string',
        naics_code='string',
        tax_id='string',
        website='string',
    ),
)

res = s.plaid.transfer_diligence_submit(req)

if res.transfer_diligence_submit_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.TransferDiligenceSubmitRequest](../../models/components/transferdiligencesubmitrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.TransferDiligenceSubmitResponse](../../models/operations/transferdiligencesubmitresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_event_list

Use the `/transfer/event/list` endpoint to get a list of transfer events based on specified filter criteria.

</api/products/transfer/#transfereventlist>

### Example Usage

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

req = components.TransferEventListRequest()

res = s.plaid.transfer_event_list(req)

if res.transfer_event_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.TransferEventListRequest](../../models/components/transfereventlistrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.TransferEventListResponse](../../models/operations/transfereventlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_event_sync

`/transfer/event/sync` allows you to request up to the next 25 transfer events that happened after a specific `event_id`. Use the `/transfer/event/sync` endpoint to guarantee you have seen all transfer events.

</api/products/transfer/#transfereventsync>

### Example Usage

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

req = components.TransferEventSyncRequest(
    after_id=252491,
)

res = s.plaid.transfer_event_sync(req)

if res.transfer_event_sync_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.TransferEventSyncRequest](../../models/components/transfereventsyncrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.TransferEventSyncResponse](../../models/operations/transfereventsyncresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_get

The `/transfer/get` endpoint fetches information about the transfer corresponding to the given `transfer_id`.

</api/products/transfer/#transferget>

### Example Usage

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

req = components.TransferGetRequest(
    transfer_id='string',
)

res = s.plaid.transfer_get(req)

if res.transfer_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.TransferGetRequest](../../models/components/transfergetrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.TransferGetResponse](../../models/operations/transfergetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_intent_create

Use the `/transfer/intent/create` endpoint to generate a transfer intent object and invoke the Transfer UI.

</api/products/transfer/#transferintentcreate>

### Example Usage

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

req = components.TransferIntentCreateRequest(
    amount='610.36',
    description='Distributed systemic data-warehouse',
    mode=components.TransferIntentCreateMode.PAYMENT,
    user=components.TransferUserInRequest(
        legal_name='string',
    ),
)

res = s.plaid.transfer_intent_create(req)

if res.transfer_intent_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.TransferIntentCreateRequest](../../models/components/transferintentcreaterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.TransferIntentCreateResponse](../../models/operations/transferintentcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_intent_get

Use the `/transfer/intent/get` endpoint to retrieve more information about a transfer intent.

</api/products/transfer/#transferintentget>

### Example Usage

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

req = components.TransferIntentGetRequest(
    transfer_intent_id='string',
)

res = s.plaid.transfer_intent_get(req)

if res.transfer_intent_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.TransferIntentGetRequest](../../models/components/transferintentgetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.TransferIntentGetResponse](../../models/operations/transferintentgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_ledger_get

Use the `/transfer/ledger/get` endpoint to view a balance on the ledger held with Plaid.

</api/products/transfer/#transferledgerget>

### Example Usage

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

req = components.TransferLedgerGetRequest()

res = s.plaid.transfer_ledger_get(req)

if res.transfer_ledger_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.TransferLedgerGetRequest](../../models/components/transferledgergetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.TransferLedgerGetResponse](../../models/operations/transferledgergetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_list

Use the `/transfer/list` endpoint to see a list of all your transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired transfers.


</api/products/transfer/#transferlist>

### Example Usage

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

req = components.TransferListRequest()

res = s.plaid.transfer_list(req)

if res.transfer_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.TransferListRequest](../../models/components/transferlistrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.TransferListResponse](../../models/operations/transferlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_metrics_get

Use the `/transfer/metrics/get` endpoint to view your transfer product usage metrics.

</api/products/transfer/#transfermetricsget>

### Example Usage

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

req = components.TransferMetricsGetRequest()

res = s.plaid.transfer_metrics_get(req)

if res.transfer_metrics_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [components.TransferMetricsGetRequest](../../models/components/transfermetricsgetrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.TransferMetricsGetResponse](../../models/operations/transfermetricsgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_migrate_account

As an alternative to adding Items via Link, you can also use the `/transfer/migrate_account` endpoint to migrate known account and routing numbers to Plaid Items.  Note that Items created in this way are not compatible with endpoints for other products, such as `/accounts/balance/get`, and can only be used with Transfer endpoints.  If you require access to other endpoints, create the Item through Link instead.  Access to `/transfer/migrate_account` is not enabled by default; to obtain access, contact your Plaid Account Manager.

</api/products/transfer/#transfermigrate_account>

### Example Usage

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

req = components.TransferMigrateAccountRequest(
    account_number='string',
    account_type='string',
    routing_number='string',
)

res = s.plaid.transfer_migrate_account(req)

if res.transfer_migrate_account_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.TransferMigrateAccountRequest](../../models/components/transfermigrateaccountrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.TransferMigrateAccountResponse](../../models/operations/transfermigrateaccountresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_originator_create

Use the `/transfer/originator/create` endpoint to create a new originator and return an `originator_client_id`.

</api/products/transfer/#transferoriginatorcreate>

### Example Usage

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

req = components.TransferOriginatorCreateRequest(
    company_name='Klein Group',
)

res = s.plaid.transfer_originator_create(req)

if res.transfer_originator_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.TransferOriginatorCreateRequest](../../models/components/transferoriginatorcreaterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.TransferOriginatorCreateResponse](../../models/operations/transferoriginatorcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_originator_get_json

The `/transfer/originator/get` endpoint gets status updates for an originator's onboarding process. This information is also available via the Transfer page on the Plaid dashboard.

</api/products/transfer/#transferoriginatorget>

### Example Usage

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

req = components.TransferOriginatorGetRequest(
    originator_client_id='string',
)

res = s.plaid.transfer_originator_get_json(req)

if res.transfer_originator_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.TransferOriginatorGetRequest](../../models/components/transferoriginatorgetrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.TransferOriginatorGetJSONResponse](../../models/operations/transferoriginatorgetjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_originator_get_raw

The `/transfer/originator/get` endpoint gets status updates for an originator's onboarding process. This information is also available via the Transfer page on the Plaid dashboard.

</api/products/transfer/#transferoriginatorget>

### Example Usage

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

req = '0x1Fb11Fe18D'.encode()

res = s.plaid.transfer_originator_get_raw(req)

if res.transfer_originator_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [bytes](../../models/.md)                  | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.TransferOriginatorGetRawResponse](../../models/operations/transferoriginatorgetrawresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_originator_list

The `/transfer/originator/list` endpoint gets status updates for all of your originators' onboarding. This information is also available via the Plaid dashboard.

</api/products/transfer/#transferoriginatorlist>

### Example Usage

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

req = components.TransferOriginatorListRequest()

res = s.plaid.transfer_originator_list(req)

if res.transfer_originator_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [components.TransferOriginatorListRequest](../../models/components/transferoriginatorlistrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.TransferOriginatorListResponse](../../models/operations/transferoriginatorlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_questionnaire_create

The `/transfer/questionnaire/create` endpoint generates a Plaid-hosted onboarding UI URL. Redirect the originator to this URL to provide their due diligence information and agree to Plaid’s terms for ACH money movement.

</api/products/transfer/#transferquestionnairecreate>

### Example Usage

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

req = components.TransferQuestionnaireCreateRequest(
    originator_client_id='string',
    redirect_uri='string',
)

res = s.plaid.transfer_questionnaire_create(req)

if res.transfer_questionnaire_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.TransferQuestionnaireCreateRequest](../../models/components/transferquestionnairecreaterequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.TransferQuestionnaireCreateResponse](../../models/operations/transferquestionnairecreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_recurring_cancel

Use the `/transfer/recurring/cancel` endpoint to cancel a recurring transfer.  Scheduled transfer that hasn't been submitted to bank will be cancelled.

</api/products/transfer/#transferrecurringcancel>

### Example Usage

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

req = components.TransferRecurringCancelRequest(
    recurring_transfer_id='string',
)

res = s.plaid.transfer_recurring_cancel(req)

if res.transfer_recurring_cancel_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.TransferRecurringCancelRequest](../../models/components/transferrecurringcancelrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.TransferRecurringCancelResponse](../../models/operations/transferrecurringcancelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_recurring_create

Use the `/transfer/recurring/create` endpoint to initiate a new recurring transfer.

</api/products/transfer/#transferrecurringcreate>

### Example Usage

```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.TransferRecurringCreateRequest(
    access_token='string',
    account_id='string',
    amount='793.56',
    description='Centralized tertiary model',
    device=components.TransferDevice(
        ip_address='20.163.92.142',
        user_agent='string',
    ),
    idempotency_key='string',
    network=components.TransferNetwork.SAME_DAY_ACH,
    schedule=components.TransferRecurringSchedule(
        interval_count=647040,
        interval_execution_day=56555,
        interval_unit=components.TransferScheduleIntervalUnit.MONTH,
        start_date=dateutil.parser.parse('2023-06-24').date(),
    ),
    type=components.TransferType.CREDIT,
    user=components.TransferUserInRequest(
        legal_name='string',
    ),
    user_present=False,
)

res = s.plaid.transfer_recurring_create(req)

if res.transfer_recurring_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [components.TransferRecurringCreateRequest](../../models/components/transferrecurringcreaterequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.TransferRecurringCreateResponse](../../models/operations/transferrecurringcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_recurring_get

The `/transfer/recurring/get` fetches information about the recurring transfer corresponding to the given `recurring_transfer_id`.

</api/products/transfer/#transferrecurringget>

### Example Usage

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

req = components.TransferRecurringGetRequest(
    recurring_transfer_id='string',
)

res = s.plaid.transfer_recurring_get(req)

if res.transfer_recurring_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.TransferRecurringGetRequest](../../models/components/transferrecurringgetrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.TransferRecurringGetResponse](../../models/operations/transferrecurringgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_recurring_list

Use the `/transfer/recurring/list` endpoint to see a list of all your recurring transfers and their statuses. Results are paginated; use the `count` and `offset` query parameters to retrieve the desired recurring transfers.


</api/products/transfer/#transferrecurringlist>

### Example Usage

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

req = components.TransferRecurringListRequest()

res = s.plaid.transfer_recurring_list(req)

if res.transfer_recurring_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.TransferRecurringListRequest](../../models/components/transferrecurringlistrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.TransferRecurringListResponse](../../models/operations/transferrecurringlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_refund_cancel

Use the `/transfer/refund/cancel` endpoint to cancel a refund.  A refund is eligible for cancellation if it has not yet been submitted to the payment network.

</api/products/transfer/#transferrefundcancel>

### Example Usage

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

req = components.TransferRefundCancelRequest(
    refund_id='string',
)

res = s.plaid.transfer_refund_cancel(req)

if res.transfer_refund_cancel_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.TransferRefundCancelRequest](../../models/components/transferrefundcancelrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.TransferRefundCancelResponse](../../models/operations/transferrefundcancelresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_refund_create

Use the `/transfer/refund/create` endpoint to create a refund for a transfer. A transfer can be refunded if the transfer was initiated in the past 180 days.

Processing of the refund will not occur until at least 3 business days following the transfer's settlement date, plus any hold/settlement delays. This 3-day window helps better protect your business from regular ACH returns. Consumer initiated returns (unauthorized returns) could still happen for about 60 days from the settlement date. If the original transfer is canceled, returned or failed, all pending refunds will automatically be canceled. Processed refunds cannot be revoked.

</api/products/transfer/#transferrefundcreate>

### Example Usage

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

req = components.TransferRefundCreateRequest(
    amount='403.07',
    idempotency_key='string',
    transfer_id='string',
)

res = s.plaid.transfer_refund_create(req)

if res.transfer_refund_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.TransferRefundCreateRequest](../../models/components/transferrefundcreaterequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.TransferRefundCreateResponse](../../models/operations/transferrefundcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_refund_get

The `/transfer/refund/get` endpoint fetches information about the refund corresponding to the given `refund_id`.

</api/products/transfer/#transferrefundget>

### Example Usage

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

req = components.TransferRefundGetRequest(
    refund_id='string',
)

res = s.plaid.transfer_refund_get(req)

if res.transfer_refund_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.TransferRefundGetRequest](../../models/components/transferrefundgetrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.TransferRefundGetResponse](../../models/operations/transferrefundgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_repayment_list

The `/transfer/repayment/list` endpoint fetches repayments matching the given filters. Repayments are returned in reverse-chronological order (most recent first) starting at the given `start_time`.

</api/products/transfer/#transferrepaymentlist>

### Example Usage

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

req = components.TransferRepaymentListRequest()

res = s.plaid.transfer_repayment_list(req)

if res.transfer_repayment_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.TransferRepaymentListRequest](../../models/components/transferrepaymentlistrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.TransferRepaymentListResponse](../../models/operations/transferrepaymentlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_repayment_return_list

The `/transfer/repayment/return/list` endpoint retrieves the set of returns that were batched together into the specified repayment. The sum of amounts of returns retrieved by this request equals the amount of the repayment.

</api/products/transfer/#transferrepaymentreturnlist>

### Example Usage

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

req = components.TransferRepaymentReturnListRequest(
    repayment_id='string',
)

res = s.plaid.transfer_repayment_return_list(req)

if res.transfer_repayment_return_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.TransferRepaymentReturnListRequest](../../models/components/transferrepaymentreturnlistrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.TransferRepaymentReturnListResponse](../../models/operations/transferrepaymentreturnlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_sweep_get

The `/transfer/sweep/get` endpoint fetches a sweep corresponding to the given `sweep_id`.

</api/products/transfer/#transfersweepget>

### Example Usage

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

req = components.TransferSweepGetRequest(
    sweep_id='string',
)

res = s.plaid.transfer_sweep_get(req)

if res.transfer_sweep_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [components.TransferSweepGetRequest](../../models/components/transfersweepgetrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.TransferSweepGetResponse](../../models/operations/transfersweepgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## transfer_sweep_list

The `/transfer/sweep/list` endpoint fetches sweeps matching the given filters.

</api/products/transfer/#transfersweeplist>

### Example Usage

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

req = components.TransferSweepListRequest()

res = s.plaid.transfer_sweep_list(req)

if res.transfer_sweep_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [components.TransferSweepListRequest](../../models/components/transfersweeplistrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.TransferSweepListResponse](../../models/operations/transfersweeplistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## user_create

This endpoint should be called for each of your end users before they begin a Plaid income flow. This provides you a single token to access all income data associated with the user. You should only create one per end user.

If you call the endpoint multiple times with the same `client_user_id`, the first creation call will succeed and the rest will fail with an error message indicating that the user has been created for the given `client_user_id`.

Ensure that you store the `user_token` along with your user's identifier in your database, as it is not possible to retrieve a previously created `user_token`.

</api/products/income/#usercreate>

### Example Usage

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

req = components.UserCreateRequest(
    client_user_id='string',
)

res = s.plaid.user_create(req)

if res.user_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.UserCreateRequest](../../models/components/usercreaterequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UserCreateResponse](../../models/operations/usercreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## wallet_create

Create an e-wallet. The response is the newly created e-wallet object.

</api/products/virtual-accounts/#walletcreate>

### Example Usage

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

req = components.WalletCreateRequest(
    iso_currency_code=components.WalletISOCurrencyCode.GBP,
)

res = s.plaid.wallet_create(req)

if res.wallet_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [components.WalletCreateRequest](../../models/components/walletcreaterequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.WalletCreateResponse](../../models/operations/walletcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## wallet_get

Fetch an e-wallet. The response includes the current balance.

</api/products/virtual-accounts/#walletget>

### Example Usage

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

req = components.WalletGetRequest(
    wallet_id='string',
)

res = s.plaid.wallet_get(req)

if res.wallet_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [components.WalletGetRequest](../../models/components/walletgetrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.WalletGetResponse](../../models/operations/walletgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## wallet_list

This endpoint lists all e-wallets in descending order of creation.

</api/products/virtual-accounts/#walletlist>

### Example Usage

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

req = components.WalletListRequest()

res = s.plaid.wallet_list(req)

if res.wallet_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.WalletListRequest](../../models/components/walletlistrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.WalletListResponse](../../models/operations/walletlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## wallet_transaction_execute

Execute a transaction using the specified e-wallet.
Specify the e-wallet to debit from, the counterparty to credit to, the idempotency key to prevent duplicate transactions, the amount and reference for the transaction.
Transactions will settle in seconds to several days, depending on the underlying payment rail.

</api/products/virtual-accounts/#wallettransactionexecute>

### Example Usage

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

req = components.WalletTransactionExecuteRequest(
    amount=components.WalletTransactionAmount(
        iso_currency_code=components.WalletISOCurrencyCode.GBP,
        value=6174.29,
    ),
    counterparty=components.WalletTransactionCounterparty(
        name='string',
        numbers=components.WalletTransactionCounterpartyNumbers(),
    ),
    idempotency_key='string',
    reference='string',
    wallet_id='string',
)

res = s.plaid.wallet_transaction_execute(req)

if res.wallet_transaction_execute_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [components.WalletTransactionExecuteRequest](../../models/components/wallettransactionexecuterequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.WalletTransactionExecuteResponse](../../models/operations/wallettransactionexecuteresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## wallet_transaction_get

Fetch a specific e-wallet transaction

</api/products/virtual-accounts/#wallettransactionget>

### Example Usage

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

req = components.WalletTransactionGetRequest(
    transaction_id='string',
)

res = s.plaid.wallet_transaction_get(req)

if res.wallet_transaction_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.WalletTransactionGetRequest](../../models/components/wallettransactiongetrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.WalletTransactionGetResponse](../../models/operations/wallettransactiongetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## wallet_transaction_list

This endpoint lists the latest transactions of the specified e-wallet. Transactions are returned in descending order by the `created_at` time.

</api/products/virtual-accounts/#wallettransactionlist>

### Example Usage

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

req = components.WalletTransactionListRequest(
    wallet_id='string',
)

res = s.plaid.wallet_transaction_list(req)

if res.wallet_transaction_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [components.WalletTransactionListRequest](../../models/components/wallettransactionlistrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.WalletTransactionListResponse](../../models/operations/wallettransactionlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_entity_create

Create a new entity watchlist screening to check your customer against watchlists defined in the associated entity watchlist program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

</api/products/monitor/#watchlist_screeningentitycreate>

### Example Usage

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

req = components.WatchlistScreeningEntityCreateRequest(
    search_terms=components.EntityWatchlistSearchTerms(
        entity_watchlist_program_id='entprg_2eRPsDnL66rZ7H',
        legal_name='Al-Qaida',
        country='US',
        document_number='C31195855',
        email_address='user@example.com',
        phone_number='+14025671234',
        url='https://example.com',
    ),
    client_user_id='your-db-id-3b24110',
)

res = s.plaid.watchlist_screening_entity_create(req)

if res.watchlist_screening_entity_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [components.WatchlistScreeningEntityCreateRequest](../../models/components/watchlistscreeningentitycreaterequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.WatchlistScreeningEntityCreateResponse](../../models/operations/watchlistscreeningentitycreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_entity_get

Retrieve an entity watchlist screening.

</api/products/monitor/#watchlist_screeningentityget>

### Example Usage

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

req = components.WatchlistScreeningEntityGetRequest(
    entity_watchlist_screening_id='entscr_52xR9LKo77r1Np',
)

res = s.plaid.watchlist_screening_entity_get(req)

if res.watchlist_screening_entity_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [components.WatchlistScreeningEntityGetRequest](../../models/components/watchlistscreeningentitygetrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.WatchlistScreeningEntityGetResponse](../../models/operations/watchlistscreeningentitygetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_entity_history_list

List all changes to the entity watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

</api/products/monitor/#watchlist_screeningentityhistorylist>

### Example Usage

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

req = components.WatchlistScreeningEntityHistoryListRequest(
    entity_watchlist_screening_id='entscr_52xR9LKo77r1Np',
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
)

res = s.plaid.watchlist_screening_entity_history_list(req)

if res.watchlist_screening_entity_history_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [components.WatchlistScreeningEntityHistoryListRequest](../../models/components/watchlistscreeningentityhistorylistrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.WatchlistScreeningEntityHistoryListResponse](../../models/operations/watchlistscreeningentityhistorylistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_entity_hit_list

List all hits for the entity watchlist screening.

</api/products/monitor/#watchlist_screeningentityhitlist>

### Example Usage

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

req = components.WatchlistScreeningEntityHitListRequest(
    entity_watchlist_screening_id='entscr_52xR9LKo77r1Np',
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
)

res = s.plaid.watchlist_screening_entity_hit_list(req)

if res.watchlist_screening_entity_hit_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [components.WatchlistScreeningEntityHitListRequest](../../models/components/watchlistscreeningentityhitlistrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.WatchlistScreeningEntityHitListResponse](../../models/operations/watchlistscreeningentityhitlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_entity_list

List all entity screenings.

</api/products/monitor/#watchlist_screeningentitylist>

### Example Usage

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

req = components.WatchlistScreeningEntityListRequest(
    entity_watchlist_program_id='entprg_2eRPsDnL66rZ7H',
    assignee='54350110fedcbaf01234ffee',
    client_user_id='your-db-id-3b24110',
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
    status=components.WatchlistScreeningStatus.CLEARED,
)

res = s.plaid.watchlist_screening_entity_list(req)

if res.watchlist_screening_entity_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [components.WatchlistScreeningEntityListRequest](../../models/components/watchlistscreeningentitylistrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.WatchlistScreeningEntityListResponse](../../models/operations/watchlistscreeningentitylistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_entity_program_get

Get an entity watchlist screening program

</api/products/monitor/#watchlist_screeningentityprogramget>

### Example Usage

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

req = components.WatchlistScreeningEntityProgramGetRequest(
    entity_watchlist_program_id='entprg_2eRPsDnL66rZ7H',
)

res = s.plaid.watchlist_screening_entity_program_get(req)

if res.watchlist_screening_entity_program_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [components.WatchlistScreeningEntityProgramGetRequest](../../models/components/watchlistscreeningentityprogramgetrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.WatchlistScreeningEntityProgramGetResponse](../../models/operations/watchlistscreeningentityprogramgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_entity_program_list

List all entity watchlist screening programs

</api/products/monitor/#watchlist_screeningentityprogramlist>

### Example Usage

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

req = components.WatchlistScreeningEntityProgramListRequest(
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
)

res = s.plaid.watchlist_screening_entity_program_list(req)

if res.watchlist_screening_entity_program_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [components.WatchlistScreeningEntityProgramListRequest](../../models/components/watchlistscreeningentityprogramlistrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.WatchlistScreeningEntityProgramListResponse](../../models/operations/watchlistscreeningentityprogramlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_entity_review_create

Create a review for an entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

</api/products/monitor/#watchlist_screeningentityreviewcreate>

### Example Usage

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

req = components.WatchlistScreeningEntityReviewCreateRequest(
    confirmed_hits=[
        'enthit_52xR9LKo77r1Np',
    ],
    dismissed_hits=[
        'enthit_52xR9LKo77r1Np',
    ],
    entity_watchlist_screening_id='entscr_52xR9LKo77r1Np',
    comment='These look like legitimate matches, rejecting the customer.',
)

res = s.plaid.watchlist_screening_entity_review_create(req)

if res.watchlist_screening_entity_review_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [components.WatchlistScreeningEntityReviewCreateRequest](../../models/components/watchlistscreeningentityreviewcreaterequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.WatchlistScreeningEntityReviewCreateResponse](../../models/operations/watchlistscreeningentityreviewcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_entity_review_list

List all reviews for a particular entity watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

</api/products/monitor/#watchlist_screeningentityreviewlist>

### Example Usage

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

req = components.WatchlistScreeningEntityReviewListRequest(
    entity_watchlist_screening_id='entscr_52xR9LKo77r1Np',
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
)

res = s.plaid.watchlist_screening_entity_review_list(req)

if res.watchlist_screening_entity_review_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [components.WatchlistScreeningEntityReviewListRequest](../../models/components/watchlistscreeningentityreviewlistrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.WatchlistScreeningEntityReviewListResponse](../../models/operations/watchlistscreeningentityreviewlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_entity_update

Update an entity watchlist screening.

</api/products/monitor/#watchlist_screeningentityupdate>

### Example Usage

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

req = components.WatchlistScreeningEntityUpdateRequest(
    entity_watchlist_screening_id='entscr_52xR9LKo77r1Np',
    assignee='54350110fedcbaf01234ffee',
    client_user_id='your-db-id-3b24110',
    status=components.WatchlistScreeningStatus.CLEARED,
)

res = s.plaid.watchlist_screening_entity_update(req)

if res.watchlist_screening_entity_update_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [components.WatchlistScreeningEntityUpdateRequest](../../models/components/watchlistscreeningentityupdaterequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.WatchlistScreeningEntityUpdateResponse](../../models/operations/watchlistscreeningentityupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_individual_create

Create a new Watchlist Screening to check your customer against watchlists defined in the associated Watchlist Program. If your associated program has ongoing screening enabled, this is the profile information that will be used to monitor your customer over time.

</api/products/monitor/#watchlist_screeningindividualcreate>

### Example Usage

```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.WatchlistScreeningIndividualCreateRequest(
    search_terms=components.WatchlistScreeningRequestSearchTerms(
        legal_name='Aleksey Potemkin',
        watchlist_program_id='prg_2eRPsDnL66rZ7H',
        country='US',
        date_of_birth=dateutil.parser.parse('1990-05-29').date(),
        document_number='C31195855',
    ),
    client_user_id='your-db-id-3b24110',
)

res = s.plaid.watchlist_screening_individual_create(req)

if res.watchlist_screening_individual_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [components.WatchlistScreeningIndividualCreateRequest](../../models/components/watchlistscreeningindividualcreaterequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.WatchlistScreeningIndividualCreateResponse](../../models/operations/watchlistscreeningindividualcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_individual_get

Retrieve a previously created individual watchlist screening

</api/products/monitor/#watchlist_screeningindividualget>

### Example Usage

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

req = components.WatchlistScreeningIndividualGetRequest(
    watchlist_screening_id='scr_52xR9LKo77r1Np',
)

res = s.plaid.watchlist_screening_individual_get(req)

if res.watchlist_screening_individual_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [components.WatchlistScreeningIndividualGetRequest](../../models/components/watchlistscreeningindividualgetrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.WatchlistScreeningIndividualGetResponse](../../models/operations/watchlistscreeningindividualgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_individual_history_list

List all changes to the individual watchlist screening in reverse-chronological order. If the watchlist screening has not been edited, no history will be returned.

</api/products/monitor/#watchlist_screeningindividualhistorylist>

### Example Usage

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

req = components.WatchlistScreeningIndividualHistoryListRequest(
    watchlist_screening_id='scr_52xR9LKo77r1Np',
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
)

res = s.plaid.watchlist_screening_individual_history_list(req)

if res.watchlist_screening_individual_history_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [components.WatchlistScreeningIndividualHistoryListRequest](../../models/components/watchlistscreeningindividualhistorylistrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.WatchlistScreeningIndividualHistoryListResponse](../../models/operations/watchlistscreeningindividualhistorylistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_individual_hit_list

List all hits found by Plaid for a particular individual watchlist screening.

</api/products/monitor/#watchlist_screeningindividualhitlist>

### Example Usage

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

req = components.WatchlistScreeningIndividualHitListRequest(
    watchlist_screening_id='scr_52xR9LKo77r1Np',
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
)

res = s.plaid.watchlist_screening_individual_hit_list(req)

if res.watchlist_screening_individual_hit_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [components.WatchlistScreeningIndividualHitListRequest](../../models/components/watchlistscreeningindividualhitlistrequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.WatchlistScreeningIndividualHitListResponse](../../models/operations/watchlistscreeningindividualhitlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_individual_list

List previously created watchlist screenings for individuals

</api/products/monitor/#watchlist_screeningindividuallist>

### Example Usage

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

req = components.WatchlistScreeningIndividualListRequest(
    watchlist_program_id='prg_2eRPsDnL66rZ7H',
    assignee='54350110fedcbaf01234ffee',
    client_user_id='your-db-id-3b24110',
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
    status=components.WatchlistScreeningStatus.CLEARED,
)

res = s.plaid.watchlist_screening_individual_list(req)

if res.watchlist_screening_individual_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [components.WatchlistScreeningIndividualListRequest](../../models/components/watchlistscreeningindividuallistrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.WatchlistScreeningIndividualListResponse](../../models/operations/watchlistscreeningindividuallistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_individual_program_get

Get an individual watchlist screening program

</api/products/monitor/#watchlist_screeningindividualprogramget>

### Example Usage

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

req = components.WatchlistScreeningIndividualProgramGetRequest(
    watchlist_program_id='prg_2eRPsDnL66rZ7H',
)

res = s.plaid.watchlist_screening_individual_program_get(req)

if res.watchlist_screening_individual_program_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [components.WatchlistScreeningIndividualProgramGetRequest](../../models/components/watchlistscreeningindividualprogramgetrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.WatchlistScreeningIndividualProgramGetResponse](../../models/operations/watchlistscreeningindividualprogramgetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_individual_program_list

List all individual watchlist screening programs

</api/products/monitor/#watchlist_screeningindividualprogramlist>

### Example Usage

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

req = components.WatchlistScreeningIndividualProgramListRequest(
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
)

res = s.plaid.watchlist_screening_individual_program_list(req)

if res.watchlist_screening_individual_program_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                              | [components.WatchlistScreeningIndividualProgramListRequest](../../models/components/watchlistscreeningindividualprogramlistrequest.md) | :heavy_check_mark:                                                                                                                     | The request object to use for the request.                                                                                             |


### Response

**[operations.WatchlistScreeningIndividualProgramListResponse](../../models/operations/watchlistscreeningindividualprogramlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_individual_review_create

Create a review for the individual watchlist screening. Reviews are compliance reports created by users in your organization regarding the relevance of potential hits found by Plaid.

</api/products/monitor/#watchlist_screeningindividualreviewcreate>

### Example Usage

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

req = components.WatchlistScreeningIndividualReviewCreateRequest(
    confirmed_hits=[
        'scrhit_52xR9LKo77r1Np',
    ],
    dismissed_hits=[
        'scrhit_52xR9LKo77r1Np',
    ],
    watchlist_screening_id='scr_52xR9LKo77r1Np',
    comment='These look like legitimate matches, rejecting the customer.',
)

res = s.plaid.watchlist_screening_individual_review_create(req)

if res.watchlist_screening_individual_review_create_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                                | Type                                                                                                                                     | Required                                                                                                                                 | Description                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                                | [components.WatchlistScreeningIndividualReviewCreateRequest](../../models/components/watchlistscreeningindividualreviewcreaterequest.md) | :heavy_check_mark:                                                                                                                       | The request object to use for the request.                                                                                               |


### Response

**[operations.WatchlistScreeningIndividualReviewCreateResponse](../../models/operations/watchlistscreeningindividualreviewcreateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_individual_review_list

List all reviews for the individual watchlist screening.

</api/products/monitor/#watchlist_screeningindividualreviewlist>

### Example Usage

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

req = components.WatchlistScreeningIndividualReviewListRequest(
    watchlist_screening_id='scr_52xR9LKo77r1Np',
    cursor='eyJkaXJlY3Rpb24iOiJuZXh0Iiwib2Zmc2V0IjoiMTU5NDM',
)

res = s.plaid.watchlist_screening_individual_review_list(req)

if res.watchlist_screening_individual_review_list_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                            | Type                                                                                                                                 | Required                                                                                                                             | Description                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                            | [components.WatchlistScreeningIndividualReviewListRequest](../../models/components/watchlistscreeningindividualreviewlistrequest.md) | :heavy_check_mark:                                                                                                                   | The request object to use for the request.                                                                                           |


### Response

**[operations.WatchlistScreeningIndividualReviewListResponse](../../models/operations/watchlistscreeningindividualreviewlistresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## watchlist_screening_individual_update

Update a specific individual watchlist screening. This endpoint can be used to add additional customer information, correct outdated information, add a reference id, assign the individual to a reviewer, and update which program it is associated with. Please note that you may not update `search_terms` and `status` at the same time since editing `search_terms` may trigger an automatic `status` change.

</api/products/monitor/#watchlist_screeningindividualupdate>

### Example Usage

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

req = components.WatchlistScreeningIndividualUpdateRequest(
    watchlist_screening_id='scr_52xR9LKo77r1Np',
    assignee='54350110fedcbaf01234ffee',
    client_user_id='your-db-id-3b24110',
    status=components.WatchlistScreeningStatus.CLEARED,
)

res = s.plaid.watchlist_screening_individual_update(req)

if res.watchlist_screening_individual_update_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [components.WatchlistScreeningIndividualUpdateRequest](../../models/components/watchlistscreeningindividualupdaterequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.WatchlistScreeningIndividualUpdateResponse](../../models/operations/watchlistscreeningindividualupdateresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## webhook_verification_key_get

Plaid signs all outgoing webhooks and provides JSON Web Tokens (JWTs) so that you can verify the authenticity of any incoming webhooks to your application. A message signature is included in the `Plaid-Verification` header.

The `/webhook_verification_key/get` endpoint provides a JSON Web Key (JWK) that can be used to verify a JWT.

</api/webhooks/webhook-verification/#get-webhook-verification-key>

### Example Usage

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

req = components.WebhookVerificationKeyGetRequest(
    key_id='string',
)

res = s.plaid.webhook_verification_key_get(req)

if res.webhook_verification_key_get_response is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [components.WebhookVerificationKeyGetRequest](../../models/components/webhookverificationkeygetrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.WebhookVerificationKeyGetResponse](../../models/operations/webhookverificationkeygetresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
