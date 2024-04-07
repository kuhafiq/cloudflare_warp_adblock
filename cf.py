import requests

# Replace these with your actual API key, email, and account ID
api_key = 'apikey'
email = 'email'
account_id = 'accid'
headers = {
    'X-Auth-Email': email,
    'X-Auth-Key': api_key,
    'Content-Type': 'application/json',
}

# User email to apply the policy
user_email = email



# Your domain list
domains = [
    "adsense.com",
    "adblade.com",
    "207.net",
    "247realmedia.com",
    "2mdn.net",
    "2o7.net",
    "33across.com",
    "abmr.net",
    "adbrite.com",
    "adbureau.net",
    "adchemy.com",
    "addthis.com",
    "addthisedge.com",
    "admeld.com",
    "admob.com",
    "adsonar.com",
    "advertising.com",
    "afy11.net",
    "aquantive.com",
    "atdmt.com",
    "atwola.com",
    "channelintelligence.com",
    "cmcore.com",
    "coremetrics.com",
    "crowdscience.com",
    "decdna.net",
    "decideinteractive.com",
    "doubleclick.com",
    "doubleclick.net",
    "esomniture.com",
    "fimserve.com",
    "flingwebads.com",
    "foxnetworks.com",
    "googleadservices.com",
    "googlesyndication.com",
    "google-analytics.com",
    "gravity.com",
    "hitbox.com",
    "imiclk.com",
    "imrworldwide.com",
    "insightexpress.com",
    "insightexpressai.com",
    "intellitxt.com",
    "invitemedia.com",
    "leadback.com",
    "lindwd.net",
    "mookie1.com",
    "myads.com",
    "netconversions.com",
    "nexac.com",
    "nextaction.net",
    "nielsen-online.com",
    "offermatica.com",
    "omniture.com",
    "omtrdc.net",
    "pm14.com",
    "quantcast.com",
    "quantserve.com",
    "realmedia.com",
    "revsci.net",
    "rightmedia.com",
    "rmxads.com",
    "ru4.com",
    "rubiconproject.com",
    "samsungadhub.com",
    "scorecardresearch.com",
    "sharethis.com",
    "shopthetv.com",
    "acoda.net",
    "targetingmarketplace.com",
    "themig.com",
    "trendnetcloud.com",
    "yieldmanager.com",
    "yieldmanager.net",
    "yldmgrimg.net",
    "youknowbest.com",
    "yumenetworks.com"
]

# Base URL for API
url = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/gateway/policies'

for domain in domains:
    # Define the policy payload
    policy_payload = {
        "name": "Block Ads",
        "precedence": 1,  # Adjust the precedence as needed
        "action": "block",
        "filters": [
            {
                "expression": {
                    "selector": "domain",
                    "operator": "is",
                    "value": domain
                },
                "identity": {
                    "selector": "useremail",
                    "operator": "is",
                    "value": user_email
                }
            }
        ]
    }
    try:
        response = requests.post(url, json=policy_payload, headers=headers)
        if response.status_code == 200:
            print(f'Successfully created policy for {domain}')
        else:
            print(f'Failed to create policy for {domain}: {response.status_code} {response.text}')
    except Exception as e:
        print(f'Error occurred for {domain}: {e}')

print("Script execution completed.")

