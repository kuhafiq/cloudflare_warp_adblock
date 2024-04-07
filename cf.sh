curl https://api.cloudflare.com/client/v4/accounts/{account_id__here_remove_bracket}/gateway/lists \
--header 'Content-Type: application/json' \
--header 'X-Auth-Email: {email_here_remove_bracket}}' \
--header 'X-Auth-Key: {api_key_remove_bracket}' \
--data '{
  "description": "Block Ads Domain List",
  "items": 
[{"value":"adsense.com"},{"value":"adblade.com"},{"value":"207.net"},{"value":"247realmedia.com"},{"value":"2mdn.net"},{"value":"2o7.net"},{"value":"33across.com"},{"value":"abmr.net"},{"value":"adbrite.com"},{"value":"adbureau.net"},{"value":"adchemy.com"},{"value":"addthis.com"},{"value":"addthisedge.com"},{"value":"admeld.com"},{"value":"admob.com"},{"value":"adsonar.com"},{"value":"advertising.com"},{"value":"afy11.net"},{"value":"aquantive.com"},{"value":"atdmt.com"},{"value":"atwola.com"},{"value":"channelintelligence.com"},{"value":"cmcore.com"},{"value":"coremetrics.com"},{"value":"crowdscience.com"},{"value":"decdna.net"},{"value":"decideinteractive.com"},{"value":"doubleclick.com"},{"value":"doubleclick.net"},{"value":"esomniture.com"},{"value":"fimserve.com"},{"value":"flingwebads.com"},{"value":"foxnetworks.com"},{"value":"googleadservices.com"},{"value":"googlesyndication.com"},{"value":"google-analytics.com"},{"value":"gravity.com"},{"value":"hitbox.com"},{"value":"imiclk.com"},{"value":"imrworldwide.com"},{"value":"insightexpress.com"},{"value":"insightexpressai.com"},{"value":"intellitxt.com"},{"value":"invitemedia.com"},{"value":"leadback.com"},{"value":"lindwd.net"},{"value":"mookie1.com"},{"value":"myads.com"},{"value":"netconversions.com"},{"value":"nexac.com"},{"value":"nextaction.net"},{"value":"nielsen-online.com"},{"value":"offermatica.com"},{"value":"omniture.com"},{"value":"omtrdc.net"},{"value":"pm14.com"},{"value":"quantcast.com"},{"value":"quantserve.com"},{"value":"realmedia.com"},{"value":"revsci.net"},{"value":"rightmedia.com"},{"value":"rmxads.com"},{"value":"ru4.com"},{"value":"rubiconproject.com"},{"value":"samsungadhub.com"},{"value":"scorecardresearch.com"},{"value":"sharethis.com"},{"value":"shopthetv.com"},{"value":"acoda.net"},{"value":"targetingmarketplace.com"},{"value":"themig.com"},{"value":"trendnetcloud.com"},{"value":"yieldmanager.com"},{"value":"yieldmanager.net"},{"value":"yldmgrimg.net"},{"value":"youknowbest.com"},{"value":"yumenetworks.com"}],
  "name": "Ads Block List",
  "type": "DOMAIN"
}'