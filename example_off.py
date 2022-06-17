import requests
#Url
url_vapp = "https://your_vdc_link/api/sessions"
#Url Off
url_vapp_off ="https://your_vdc_link/api/vApp/your_vapp_link/power/action/shutdown"
#Payload
payload={}
#Headers
headers_vapp = {
  'Accept': 'application/*;version=35.0',
  'Authorization': 'Basic login@tenant:password'
  #login@tenant:password in base64
}
#Request API
answer_vapp = requests.post(url_vapp, headers=headers_vapp, data=payload)
token_vapp = answer_vapp.headers["x-vmware-vcloud-access-token"]
#Headers for Commands
headers_vapp_off = {
  'Accept': 'application/*;version=35.0',
  'Authorization': 'Bearer ' + token_vapp
}
#Commands On
vapp_off = requests.post(url_vapp_off, headers=headers_vapp_off, data=payload)