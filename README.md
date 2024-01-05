# plaid

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/plaid.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/plaid/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/plaid.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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

req = components.AccountsBalanceGetRequest(
    access_token='string',
    options=components.AccountsBalanceGetRequestOptions(
        account_ids=[
            'string',
        ],
    ),
)

res = s.plaid.accounts_balance_get(req)

if res.accounts_get_response is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [plaid](docs/sdks/plaidsdk/README.md)

* [accounts_balance_get](docs/sdks/plaidsdk/README.md#accounts_balance_get) - Retrieve real-time balance data
* [accounts_get](docs/sdks/plaidsdk/README.md#accounts_get) - Retrieve accounts
* [application_get](docs/sdks/plaidsdk/README.md#application_get) - Retrieve information about a Plaid application
* [asset_report_audit_copy_create](docs/sdks/plaidsdk/README.md#asset_report_audit_copy_create) - Create Asset Report Audit Copy
* [asset_report_audit_copy_get](docs/sdks/plaidsdk/README.md#asset_report_audit_copy_get) - Retrieve an Asset Report Audit Copy
* [asset_report_audit_copy_remove](docs/sdks/plaidsdk/README.md#asset_report_audit_copy_remove) - Remove Asset Report Audit Copy
* [asset_report_create](docs/sdks/plaidsdk/README.md#asset_report_create) - Create an Asset Report
* [asset_report_filter](docs/sdks/plaidsdk/README.md#asset_report_filter) - Filter Asset Report
* [asset_report_get](docs/sdks/plaidsdk/README.md#asset_report_get) - Retrieve an Asset Report
* [asset_report_pdf_get](docs/sdks/plaidsdk/README.md#asset_report_pdf_get) - Retrieve a PDF Asset Report
* [asset_report_refresh](docs/sdks/plaidsdk/README.md#asset_report_refresh) - Refresh an Asset Report
* [asset_report_remove](docs/sdks/plaidsdk/README.md#asset_report_remove) - Delete an Asset Report
* [auth_get](docs/sdks/plaidsdk/README.md#auth_get) - Retrieve auth data
* [bank_transfer_balance_get](docs/sdks/plaidsdk/README.md#bank_transfer_balance_get) - Get balance of your Bank Transfer account
* [bank_transfer_cancel](docs/sdks/plaidsdk/README.md#bank_transfer_cancel) - Cancel a bank transfer
* [bank_transfer_create](docs/sdks/plaidsdk/README.md#bank_transfer_create) - Create a bank transfer
* [bank_transfer_event_list](docs/sdks/plaidsdk/README.md#bank_transfer_event_list) - List bank transfer events
* [bank_transfer_event_sync](docs/sdks/plaidsdk/README.md#bank_transfer_event_sync) - Sync bank transfer events
* [bank_transfer_get](docs/sdks/plaidsdk/README.md#bank_transfer_get) - Retrieve a bank transfer
* [bank_transfer_list](docs/sdks/plaidsdk/README.md#bank_transfer_list) - List bank transfers
* [bank_transfer_migrate_account](docs/sdks/plaidsdk/README.md#bank_transfer_migrate_account) - Migrate account into Bank Transfers
* [bank_transfer_sweep_get](docs/sdks/plaidsdk/README.md#bank_transfer_sweep_get) - Retrieve a sweep
* [bank_transfer_sweep_list](docs/sdks/plaidsdk/README.md#bank_transfer_sweep_list) - List sweeps
* [base_report_get](docs/sdks/plaidsdk/README.md#base_report_get) - Retrieve a Base Report
* [beacon_report_create](docs/sdks/plaidsdk/README.md#beacon_report_create) - Create a Beacon Report
* [beacon_user_create](docs/sdks/plaidsdk/README.md#beacon_user_create) - Create a Beacon User
* [beacon_user_get](docs/sdks/plaidsdk/README.md#beacon_user_get) - Get a Beacon User
* [categories_get](docs/sdks/plaidsdk/README.md#categories_get) - Get categories
* [cra_bank_income_get](docs/sdks/plaidsdk/README.md#cra_bank_income_get) - Retrieve information from the bank accounts used for income verification
* [~~create_payment_token~~](docs/sdks/plaidsdk/README.md#create_payment_token) - Create payment token :warning: **Deprecated**
* [credit_asset_report_freddie_mac_get](docs/sdks/plaidsdk/README.md#credit_asset_report_freddie_mac_get) - Retrieve an Asset Report with Freddie Mac format. Only Freddie Mac can use this endpoint.
* [credit_audit_copy_token_create](docs/sdks/plaidsdk/README.md#credit_audit_copy_token_create) - Create Asset or Income Report Audit Copy Token
* [credit_audit_copy_token_update](docs/sdks/plaidsdk/README.md#credit_audit_copy_token_update) - Update an Audit Copy Token
* [credit_bank_employment_get](docs/sdks/plaidsdk/README.md#credit_bank_employment_get) - Retrieve information from the bank accounts used for employment verification
* [credit_bank_income_get](docs/sdks/plaidsdk/README.md#credit_bank_income_get) - Retrieve information from the bank accounts used for income verification
* [credit_bank_income_pdf_get](docs/sdks/plaidsdk/README.md#credit_bank_income_pdf_get) - Retrieve information from the bank accounts used for income verification in PDF format
* [credit_bank_income_refresh](docs/sdks/plaidsdk/README.md#credit_bank_income_refresh) - Refresh a user's bank income information
* [credit_bank_income_webhook_update](docs/sdks/plaidsdk/README.md#credit_bank_income_webhook_update) - Subscribe and unsubscribe to proactive notifications for a user's income profile
* [credit_bank_statements_uploads_get](docs/sdks/plaidsdk/README.md#credit_bank_statements_uploads_get) - Retrieve data for a user's uploaded bank statements
* [credit_employment_get](docs/sdks/plaidsdk/README.md#credit_employment_get) - Retrieve a summary of an individual's employment information
* [credit_freddie_mac_reports_get](docs/sdks/plaidsdk/README.md#credit_freddie_mac_reports_get) - Retrieve an Asset Report with Freddie Mac format (aka VOA - Verification Of Assets), and a Verification Of Employment (VOE) report if this one is available. Only Freddie Mac can use this endpoint.
* [credit_payroll_income_get](docs/sdks/plaidsdk/README.md#credit_payroll_income_get) - Retrieve a user's payroll information
* [credit_payroll_income_precheck](docs/sdks/plaidsdk/README.md#credit_payroll_income_precheck) - Check income verification eligibility and optimize conversion
* [credit_payroll_income_refresh](docs/sdks/plaidsdk/README.md#credit_payroll_income_refresh) - Refresh a digital payroll income verification
* [credit_payroll_income_risk_signals_get](docs/sdks/plaidsdk/README.md#credit_payroll_income_risk_signals_get) - Retrieve fraud insights for a user's manually uploaded document(s).
* [credit_relay_create](docs/sdks/plaidsdk/README.md#credit_relay_create) - Create a relay token to share an Asset Report with a partner client (beta)
* [credit_relay_get](docs/sdks/plaidsdk/README.md#credit_relay_get) - Retrieve the reports associated with a relay token that was shared with you (beta)
* [credit_relay_pdf_get](docs/sdks/plaidsdk/README.md#credit_relay_pdf_get) - Retrieve the pdf reports associated with a relay token that was shared with you (beta)
* [credit_relay_refresh](docs/sdks/plaidsdk/README.md#credit_relay_refresh) - Refresh a report of a relay token (beta)
* [credit_relay_remove](docs/sdks/plaidsdk/README.md#credit_relay_remove) - Remove relay token (beta)
* [credit_report_audit_copy_remove](docs/sdks/plaidsdk/README.md#credit_report_audit_copy_remove) - Remove an Audit Copy token
* [credit_sessions_get](docs/sdks/plaidsdk/README.md#credit_sessions_get) - Retrieve Link sessions for your user
* [dashboard_user_get](docs/sdks/plaidsdk/README.md#dashboard_user_get) - Retrieve a dashboard user
* [dashboard_user_list](docs/sdks/plaidsdk/README.md#dashboard_user_list) - List dashboard users
* [deposit_switch_alt_create](docs/sdks/plaidsdk/README.md#deposit_switch_alt_create) - Create a deposit switch without using Plaid Exchange
* [deposit_switch_create](docs/sdks/plaidsdk/README.md#deposit_switch_create) - Create a deposit switch
* [deposit_switch_get](docs/sdks/plaidsdk/README.md#deposit_switch_get) - Retrieve a deposit switch
* [deposit_switch_token_create](docs/sdks/plaidsdk/README.md#deposit_switch_token_create) - Create a deposit switch token
* [employers_search](docs/sdks/plaidsdk/README.md#employers_search) - Search employer database
* [~~employment_verification_get~~](docs/sdks/plaidsdk/README.md#employment_verification_get) - (Deprecated) Retrieve a summary of an individual's employment information :warning: **Deprecated**
* [fdx_notifications](docs/sdks/plaidsdk/README.md#fdx_notifications) - Webhook receiver for fdx notifications
* [identity_get](docs/sdks/plaidsdk/README.md#identity_get) - Retrieve identity data
* [identity_match](docs/sdks/plaidsdk/README.md#identity_match) - Retrieve identity match score
* [identity_refresh](docs/sdks/plaidsdk/README.md#identity_refresh) - Refresh identity data
* [identity_verification_create](docs/sdks/plaidsdk/README.md#identity_verification_create) - Create a new identity verification
* [identity_verification_get](docs/sdks/plaidsdk/README.md#identity_verification_get) - Retrieve Identity Verification
* [identity_verification_list](docs/sdks/plaidsdk/README.md#identity_verification_list) - List Identity Verifications
* [identity_verification_retry](docs/sdks/plaidsdk/README.md#identity_verification_retry) - Retry an Identity Verification
* [~~income_verification_create~~](docs/sdks/plaidsdk/README.md#income_verification_create) - (Deprecated) Create an income verification instance :warning: **Deprecated**
* [~~income_verification_documents_download~~](docs/sdks/plaidsdk/README.md#income_verification_documents_download) - (Deprecated) Download the original documents used for income verification :warning: **Deprecated**
* [~~income_verification_paystubs_get~~](docs/sdks/plaidsdk/README.md#income_verification_paystubs_get) - (Deprecated) Retrieve information from the paystubs used for income verification :warning: **Deprecated**
* [~~income_verification_precheck~~](docs/sdks/plaidsdk/README.md#income_verification_precheck) - (Deprecated) Check digital income verification eligibility and optimize conversion :warning: **Deprecated**
* [~~income_verification_taxforms_get~~](docs/sdks/plaidsdk/README.md#income_verification_taxforms_get) - (Deprecated) Retrieve information from the tax documents used for income verification :warning: **Deprecated**
* [institutions_get](docs/sdks/plaidsdk/README.md#institutions_get) - Get details of all supported institutions
* [institutions_get_by_id](docs/sdks/plaidsdk/README.md#institutions_get_by_id) - Get details of an institution
* [institutions_search](docs/sdks/plaidsdk/README.md#institutions_search) - Search institutions
* [investments_auth_get](docs/sdks/plaidsdk/README.md#investments_auth_get) - Get data needed to authorize an investments transfer
* [investments_holdings_get](docs/sdks/plaidsdk/README.md#investments_holdings_get) - Get Investment holdings
* [investments_refresh](docs/sdks/plaidsdk/README.md#investments_refresh) - Refresh investment data
* [investments_transactions_get](docs/sdks/plaidsdk/README.md#investments_transactions_get) - Get investment transactions
* [item_access_token_invalidate](docs/sdks/plaidsdk/README.md#item_access_token_invalidate) - Invalidate access_token
* [item_activity_list](docs/sdks/plaidsdk/README.md#item_activity_list) - List a historical log of user consent events
* [item_application_list](docs/sdks/plaidsdk/README.md#item_application_list) - List a user’s connected applications
* [item_application_scopes_update](docs/sdks/plaidsdk/README.md#item_application_scopes_update) - Update the scopes of access for a particular application
* [item_create_public_token](docs/sdks/plaidsdk/README.md#item_create_public_token) - Create public token
* [item_get](docs/sdks/plaidsdk/README.md#item_get) - Retrieve an Item
* [item_import](docs/sdks/plaidsdk/README.md#item_import) - Import Item
* [item_public_token_exchange](docs/sdks/plaidsdk/README.md#item_public_token_exchange) - Exchange public token for an access token
* [item_remove](docs/sdks/plaidsdk/README.md#item_remove) - Remove an Item
* [item_webhook_update](docs/sdks/plaidsdk/README.md#item_webhook_update) - Update Webhook URL
* [liabilities_get](docs/sdks/plaidsdk/README.md#liabilities_get) - Retrieve Liabilities data
* [link_delivery_create](docs/sdks/plaidsdk/README.md#link_delivery_create) - Create Hosted Link session
* [link_delivery_get](docs/sdks/plaidsdk/README.md#link_delivery_get) - Get Hosted Link session
* [link_oauth_correlation_id_exchange](docs/sdks/plaidsdk/README.md#link_oauth_correlation_id_exchange) - Exchange the Link Correlation Id for a Link Token
* [link_token_create](docs/sdks/plaidsdk/README.md#link_token_create) - Create Link Token
* [link_token_get](docs/sdks/plaidsdk/README.md#link_token_get) - Get Link Token
* [partner_customer_create](docs/sdks/plaidsdk/README.md#partner_customer_create) - Creates a new end customer for a Plaid reseller.
* [partner_customer_enable](docs/sdks/plaidsdk/README.md#partner_customer_enable) - Enables a Plaid reseller's end customer in the Production environment.
* [partner_customer_get](docs/sdks/plaidsdk/README.md#partner_customer_get) - Returns a Plaid reseller's end customer.
* [partner_customer_oauth_institutions_get](docs/sdks/plaidsdk/README.md#partner_customer_oauth_institutions_get) - Returns OAuth-institution registration information for a given end customer.
* [partner_customer_remove](docs/sdks/plaidsdk/README.md#partner_customer_remove) - Removes a Plaid reseller's end customer.
* [payment_initiation_consent_create](docs/sdks/plaidsdk/README.md#payment_initiation_consent_create) - Create payment consent
* [payment_initiation_consent_get](docs/sdks/plaidsdk/README.md#payment_initiation_consent_get) - Get payment consent
* [payment_initiation_consent_payment_execute](docs/sdks/plaidsdk/README.md#payment_initiation_consent_payment_execute) - Execute a single payment using consent
* [payment_initiation_consent_revoke](docs/sdks/plaidsdk/README.md#payment_initiation_consent_revoke) - Revoke payment consent
* [payment_initiation_payment_create](docs/sdks/plaidsdk/README.md#payment_initiation_payment_create) - Create a payment
* [payment_initiation_payment_get](docs/sdks/plaidsdk/README.md#payment_initiation_payment_get) - Get payment details
* [payment_initiation_payment_list](docs/sdks/plaidsdk/README.md#payment_initiation_payment_list) - List payments
* [payment_initiation_payment_reverse](docs/sdks/plaidsdk/README.md#payment_initiation_payment_reverse) - Reverse an existing payment
* [payment_initiation_recipient_create](docs/sdks/plaidsdk/README.md#payment_initiation_recipient_create) - Create payment recipient
* [payment_initiation_recipient_get](docs/sdks/plaidsdk/README.md#payment_initiation_recipient_get) - Get payment recipient
* [payment_initiation_recipient_list](docs/sdks/plaidsdk/README.md#payment_initiation_recipient_list) - List payment recipients
* [payment_profile_create](docs/sdks/plaidsdk/README.md#payment_profile_create) - Create payment profile
* [payment_profile_get](docs/sdks/plaidsdk/README.md#payment_profile_get) - Get payment profile
* [payment_profile_remove](docs/sdks/plaidsdk/README.md#payment_profile_remove) - Remove payment profile
* [processor_apex_processor_token_create](docs/sdks/plaidsdk/README.md#processor_apex_processor_token_create) - Create Apex bank account token
* [processor_auth_get](docs/sdks/plaidsdk/README.md#processor_auth_get) - Retrieve Auth data
* [processor_balance_get](docs/sdks/plaidsdk/README.md#processor_balance_get) - Retrieve Balance data
* [processor_bank_transfer_create](docs/sdks/plaidsdk/README.md#processor_bank_transfer_create) - Create a bank transfer as a processor
* [processor_identity_get](docs/sdks/plaidsdk/README.md#processor_identity_get) - Retrieve Identity data
* [processor_identity_match](docs/sdks/plaidsdk/README.md#processor_identity_match) - Retrieve identity match score
* [processor_signal_decision_report](docs/sdks/plaidsdk/README.md#processor_signal_decision_report) - Report whether you initiated an ACH transaction
* [processor_signal_evaluate](docs/sdks/plaidsdk/README.md#processor_signal_evaluate) - Evaluate a planned ACH transaction
* [processor_signal_return_report](docs/sdks/plaidsdk/README.md#processor_signal_return_report) - Report a return for an ACH transaction
* [processor_stripe_bank_account_token_create](docs/sdks/plaidsdk/README.md#processor_stripe_bank_account_token_create) - Create Stripe bank account token
* [processor_token_create](docs/sdks/plaidsdk/README.md#processor_token_create) - Create processor token
* [processor_token_permissions_get](docs/sdks/plaidsdk/README.md#processor_token_permissions_get) - Get a processor token's product permissions
* [processor_token_permissions_set](docs/sdks/plaidsdk/README.md#processor_token_permissions_set) - Control a processor's access to products
* [processor_token_webhook_update](docs/sdks/plaidsdk/README.md#processor_token_webhook_update) - Update a processor token's webhook URL
* [processor_transactions_get](docs/sdks/plaidsdk/README.md#processor_transactions_get) - Get transaction data
* [processor_transactions_recurring_get](docs/sdks/plaidsdk/README.md#processor_transactions_recurring_get) - Fetch recurring transaction streams
* [processor_transactions_refresh](docs/sdks/plaidsdk/README.md#processor_transactions_refresh) - Refresh transaction data
* [processor_transactions_sync](docs/sdks/plaidsdk/README.md#processor_transactions_sync) - Get incremental transaction updates on a processor token
* [sandbox_bank_income_fire_webhook](docs/sdks/plaidsdk/README.md#sandbox_bank_income_fire_webhook) - Manually fire a bank income webhook in sandbox
* [sandbox_bank_transfer_fire_webhook](docs/sdks/plaidsdk/README.md#sandbox_bank_transfer_fire_webhook) - Manually fire a Bank Transfer webhook
* [sandbox_bank_transfer_simulate](docs/sdks/plaidsdk/README.md#sandbox_bank_transfer_simulate) - Simulate a bank transfer event in Sandbox
* [sandbox_income_fire_webhook](docs/sdks/plaidsdk/README.md#sandbox_income_fire_webhook) - Manually fire an Income webhook
* [sandbox_item_fire_webhook](docs/sdks/plaidsdk/README.md#sandbox_item_fire_webhook) - Fire a test webhook
* [sandbox_item_reset_login](docs/sdks/plaidsdk/README.md#sandbox_item_reset_login) - Force a Sandbox Item into an error state
* [sandbox_item_set_verification_status](docs/sdks/plaidsdk/README.md#sandbox_item_set_verification_status) - Set verification status for Sandbox account
* [sandbox_oauth_select_accounts](docs/sdks/plaidsdk/README.md#sandbox_oauth_select_accounts) - Save the selected accounts when connecting to the Platypus Oauth institution
* [sandbox_payment_profile_reset_login](docs/sdks/plaidsdk/README.md#sandbox_payment_profile_reset_login) - Reset the login of a Payment Profile
* [sandbox_processor_token_create](docs/sdks/plaidsdk/README.md#sandbox_processor_token_create) - Create a test Item and processor token
* [sandbox_public_token_create](docs/sdks/plaidsdk/README.md#sandbox_public_token_create) - Create a test Item
* [sandbox_transfer_fire_webhook](docs/sdks/plaidsdk/README.md#sandbox_transfer_fire_webhook) - Manually fire a Transfer webhook
* [sandbox_transfer_repayment_simulate](docs/sdks/plaidsdk/README.md#sandbox_transfer_repayment_simulate) - Trigger the creation of a repayment
* [sandbox_transfer_simulate](docs/sdks/plaidsdk/README.md#sandbox_transfer_simulate) - Simulate a transfer event in Sandbox
* [sandbox_transfer_sweep_simulate](docs/sdks/plaidsdk/README.md#sandbox_transfer_sweep_simulate) - Simulate creating a sweep
* [sandbox_transfer_test_clock_advance](docs/sdks/plaidsdk/README.md#sandbox_transfer_test_clock_advance) - Advance a test clock
* [sandbox_transfer_test_clock_create](docs/sdks/plaidsdk/README.md#sandbox_transfer_test_clock_create) - Create a test clock
* [sandbox_transfer_test_clock_get](docs/sdks/plaidsdk/README.md#sandbox_transfer_test_clock_get) - Get a test clock
* [sandbox_transfer_test_clock_list](docs/sdks/plaidsdk/README.md#sandbox_transfer_test_clock_list) - List test clocks
* [signal_decision_report](docs/sdks/plaidsdk/README.md#signal_decision_report) - Report whether you initiated an ACH transaction
* [signal_evaluate](docs/sdks/plaidsdk/README.md#signal_evaluate) - Evaluate a planned ACH transaction
* [signal_prepare](docs/sdks/plaidsdk/README.md#signal_prepare) - Opt-in an Item to Signal
* [signal_return_report](docs/sdks/plaidsdk/README.md#signal_return_report) - Report a return for an ACH transaction
* [statements_download](docs/sdks/plaidsdk/README.md#statements_download) - Retrieve a single statement.
* [statements_list](docs/sdks/plaidsdk/README.md#statements_list) - Retrieve a list of all statements associated with the provided item.
* [transactions_enhance](docs/sdks/plaidsdk/README.md#transactions_enhance) - enhance locally-held transaction data
* [transactions_enrich](docs/sdks/plaidsdk/README.md#transactions_enrich) - Enrich locally-held transaction data
* [transactions_get](docs/sdks/plaidsdk/README.md#transactions_get) - Get transaction data
* [transactions_recurring_get](docs/sdks/plaidsdk/README.md#transactions_recurring_get) - Fetch recurring transaction streams
* [transactions_refresh](docs/sdks/plaidsdk/README.md#transactions_refresh) - Refresh transaction data
* [transactions_rules_create](docs/sdks/plaidsdk/README.md#transactions_rules_create) - Create transaction category rule
* [transactions_rules_list](docs/sdks/plaidsdk/README.md#transactions_rules_list) - Return a list of rules created for the Item associated with the access token.
* [transactions_rules_remove](docs/sdks/plaidsdk/README.md#transactions_rules_remove) - Remove transaction rule
* [transactions_sync](docs/sdks/plaidsdk/README.md#transactions_sync) - Get incremental transaction updates on an Item
* [transfer_authorization_create](docs/sdks/plaidsdk/README.md#transfer_authorization_create) - Create a transfer authorization
* [transfer_balance_get](docs/sdks/plaidsdk/README.md#transfer_balance_get) - Retrieve a balance held with Plaid
* [transfer_cancel](docs/sdks/plaidsdk/README.md#transfer_cancel) - Cancel a transfer
* [transfer_capabilities_get](docs/sdks/plaidsdk/README.md#transfer_capabilities_get) - Get RTP eligibility information of a transfer
* [transfer_configuration_get](docs/sdks/plaidsdk/README.md#transfer_configuration_get) - Get transfer product configuration
* [transfer_create](docs/sdks/plaidsdk/README.md#transfer_create) - Create a transfer
* [transfer_diligence_document_upload](docs/sdks/plaidsdk/README.md#transfer_diligence_document_upload) - This endpoint allows third-party sender customers to upload a document on behalf of its end customer (i.e. originator) to Plaid. You’ll need to send a request of type multipart/form-data.
* [transfer_diligence_submit](docs/sdks/plaidsdk/README.md#transfer_diligence_submit) - Submit transfer diligence on behalf of the end customer (i.e. the originator).
* [transfer_event_list](docs/sdks/plaidsdk/README.md#transfer_event_list) - List transfer events
* [transfer_event_sync](docs/sdks/plaidsdk/README.md#transfer_event_sync) - Sync transfer events
* [transfer_get](docs/sdks/plaidsdk/README.md#transfer_get) - Retrieve a transfer
* [transfer_intent_create](docs/sdks/plaidsdk/README.md#transfer_intent_create) - Create a transfer intent object to invoke the Transfer UI
* [transfer_intent_get](docs/sdks/plaidsdk/README.md#transfer_intent_get) - Retrieve more information about a transfer intent
* [transfer_ledger_get](docs/sdks/plaidsdk/README.md#transfer_ledger_get) - Retrieve Plaid Ledger balance
* [transfer_list](docs/sdks/plaidsdk/README.md#transfer_list) - List transfers
* [transfer_metrics_get](docs/sdks/plaidsdk/README.md#transfer_metrics_get) - Get transfer product usage metrics
* [transfer_migrate_account](docs/sdks/plaidsdk/README.md#transfer_migrate_account) - Migrate account into Transfers
* [transfer_originator_create](docs/sdks/plaidsdk/README.md#transfer_originator_create) - Create a new originator
* [transfer_originator_get_json](docs/sdks/plaidsdk/README.md#transfer_originator_get_json) - Get status of an originator's onboarding
* [transfer_originator_get_raw](docs/sdks/plaidsdk/README.md#transfer_originator_get_raw) - Get status of an originator's onboarding
* [transfer_originator_list](docs/sdks/plaidsdk/README.md#transfer_originator_list) - Get status of all originators' onboarding
* [transfer_questionnaire_create](docs/sdks/plaidsdk/README.md#transfer_questionnaire_create) - Generate a Plaid-hosted onboarding UI URL.
* [transfer_recurring_cancel](docs/sdks/plaidsdk/README.md#transfer_recurring_cancel) - Cancel a recurring transfer.
* [transfer_recurring_create](docs/sdks/plaidsdk/README.md#transfer_recurring_create) - Create a recurring transfer
* [transfer_recurring_get](docs/sdks/plaidsdk/README.md#transfer_recurring_get) - Retrieve a recurring transfer
* [transfer_recurring_list](docs/sdks/plaidsdk/README.md#transfer_recurring_list) - List recurring transfers
* [transfer_refund_cancel](docs/sdks/plaidsdk/README.md#transfer_refund_cancel) - Cancel a refund
* [transfer_refund_create](docs/sdks/plaidsdk/README.md#transfer_refund_create) - Create a refund
* [transfer_refund_get](docs/sdks/plaidsdk/README.md#transfer_refund_get) - Retrieve a refund
* [transfer_repayment_list](docs/sdks/plaidsdk/README.md#transfer_repayment_list) - Lists historical repayments
* [transfer_repayment_return_list](docs/sdks/plaidsdk/README.md#transfer_repayment_return_list) - List the returns included in a repayment
* [transfer_sweep_get](docs/sdks/plaidsdk/README.md#transfer_sweep_get) - Retrieve a sweep
* [transfer_sweep_list](docs/sdks/plaidsdk/README.md#transfer_sweep_list) - List sweeps
* [user_create](docs/sdks/plaidsdk/README.md#user_create) - Create user
* [wallet_create](docs/sdks/plaidsdk/README.md#wallet_create) - Create an e-wallet
* [wallet_get](docs/sdks/plaidsdk/README.md#wallet_get) - Fetch an e-wallet
* [wallet_list](docs/sdks/plaidsdk/README.md#wallet_list) - Fetch a list of e-wallets
* [wallet_transaction_execute](docs/sdks/plaidsdk/README.md#wallet_transaction_execute) - Execute a transaction using an e-wallet
* [wallet_transaction_get](docs/sdks/plaidsdk/README.md#wallet_transaction_get) - Fetch an e-wallet transaction
* [wallet_transaction_list](docs/sdks/plaidsdk/README.md#wallet_transaction_list) - List e-wallet transactions
* [watchlist_screening_entity_create](docs/sdks/plaidsdk/README.md#watchlist_screening_entity_create) - Create a watchlist screening for an entity
* [watchlist_screening_entity_get](docs/sdks/plaidsdk/README.md#watchlist_screening_entity_get) - Get an entity screening
* [watchlist_screening_entity_history_list](docs/sdks/plaidsdk/README.md#watchlist_screening_entity_history_list) - List history for entity watchlist screenings
* [watchlist_screening_entity_hit_list](docs/sdks/plaidsdk/README.md#watchlist_screening_entity_hit_list) - List hits for entity watchlist screenings
* [watchlist_screening_entity_list](docs/sdks/plaidsdk/README.md#watchlist_screening_entity_list) - List entity watchlist screenings
* [watchlist_screening_entity_program_get](docs/sdks/plaidsdk/README.md#watchlist_screening_entity_program_get) - Get entity watchlist screening program
* [watchlist_screening_entity_program_list](docs/sdks/plaidsdk/README.md#watchlist_screening_entity_program_list) - List entity watchlist screening programs
* [watchlist_screening_entity_review_create](docs/sdks/plaidsdk/README.md#watchlist_screening_entity_review_create) - Create a review for an entity watchlist screening
* [watchlist_screening_entity_review_list](docs/sdks/plaidsdk/README.md#watchlist_screening_entity_review_list) - List reviews for entity watchlist screenings
* [watchlist_screening_entity_update](docs/sdks/plaidsdk/README.md#watchlist_screening_entity_update) - Update an entity screening
* [watchlist_screening_individual_create](docs/sdks/plaidsdk/README.md#watchlist_screening_individual_create) - Create a watchlist screening for a person
* [watchlist_screening_individual_get](docs/sdks/plaidsdk/README.md#watchlist_screening_individual_get) - Retrieve an individual watchlist screening
* [watchlist_screening_individual_history_list](docs/sdks/plaidsdk/README.md#watchlist_screening_individual_history_list) - List history for individual watchlist screenings
* [watchlist_screening_individual_hit_list](docs/sdks/plaidsdk/README.md#watchlist_screening_individual_hit_list) - List hits for individual watchlist screening
* [watchlist_screening_individual_list](docs/sdks/plaidsdk/README.md#watchlist_screening_individual_list) - List Individual Watchlist Screenings
* [watchlist_screening_individual_program_get](docs/sdks/plaidsdk/README.md#watchlist_screening_individual_program_get) - Get individual watchlist screening program
* [watchlist_screening_individual_program_list](docs/sdks/plaidsdk/README.md#watchlist_screening_individual_program_list) - List individual watchlist screening programs
* [watchlist_screening_individual_review_create](docs/sdks/plaidsdk/README.md#watchlist_screening_individual_review_create) - Create a review for an individual watchlist screening
* [watchlist_screening_individual_review_list](docs/sdks/plaidsdk/README.md#watchlist_screening_individual_review_list) - List reviews for individual watchlist screenings
* [watchlist_screening_individual_update](docs/sdks/plaidsdk/README.md#watchlist_screening_individual_update) - Update individual watchlist screening
* [webhook_verification_key_get](docs/sdks/plaidsdk/README.md#webhook_verification_key_get) - Get webhook verification key
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

### Example

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

req = components.AccountsBalanceGetRequest(
    access_token='string',
    options=components.AccountsBalanceGetRequestOptions(
        account_ids=[
            'string',
        ],
    ),
)

res = None
try:
    res = s.plaid.accounts_balance_get(req)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.accounts_get_response is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://production.plaid.com` | None |
| 1 | `https://development.plaid.com` | None |
| 2 | `https://sandbox.plaid.com` | None |

#### Example

```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    server_idx=2,
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.AccountsBalanceGetRequest(
    access_token='string',
    options=components.AccountsBalanceGetRequestOptions(
        account_ids=[
            'string',
        ],
    ),
)

res = s.plaid.accounts_balance_get(req)

if res.accounts_get_response is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import dateutil.parser
import plaid
from plaid.models import components

s = plaid.Plaid(
    server_url="https://production.plaid.com",
    security=components.Security1(
        client_id="<YOUR_API_KEY_HERE>",
        plaid_version="<YOUR_API_KEY_HERE>",
        secret="<YOUR_API_KEY_HERE>",
    ),
)

req = components.AccountsBalanceGetRequest(
    access_token='string',
    options=components.AccountsBalanceGetRequestOptions(
        account_ids=[
            'string',
        ],
    ),
)

res = s.plaid.accounts_balance_get(req)

if res.accounts_get_response is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import plaid
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = plaid.Plaid(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name            | Type            | Scheme          |
| --------------- | --------------- | --------------- |
| `client_id`     | apiKey          | API key         |
| `plaid_version` | apiKey          | API key         |
| `secret`        | apiKey          | API key         |

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
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

req = components.AccountsBalanceGetRequest(
    access_token='string',
    options=components.AccountsBalanceGetRequestOptions(
        account_ids=[
            'string',
        ],
    ),
)

res = s.plaid.accounts_balance_get(req)

if res.accounts_get_response is not None:
    # handle response
    pass
```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
