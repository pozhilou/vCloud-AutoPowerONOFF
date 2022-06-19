#Before running the script, you need to install the libraries to make it work. 
#Enter these commands in a Linux or Python terminal
#pip instlall requests
#pip install Timer
import requests
from datetime import datetime
from threading import Timer
time_now = datetime.today()
time_on = time_now.replace(day=time_now.day+0, hour=7, minute=30, second=0, microsecond=0)
hour_on = time_on - time_now
secs_on = hour_on.seconds+1
time_off = time_now.replace(day=time_now.day+0, hour=22, minute=30, second=0, microsecond=0)
hour_off = time_off - time_now
secs_off = hour_off.seconds+1
url = {
    'url_vcd_01': 'https://your_vcd_01/api/sessions',
    'url_vcd_02': 'https://your_vcd_02/api/sessions',
}
#login@tenant:password in base64
org_example_01 = {
    'test_01': 'login@tenant:password',
}
org_example_02 = {
    'test_02': 'login@tenant:password',
}
url_power_on = {
    'test_01': 'https://your_vcd_01/api/vApp/your_vapp_01/power/action/powerOn',
    'test_02': 'https://your_vcd_02/api/vApp/your_vapp_02/power/action/powerOn',
}
url_power_off = {
    'test_01': 'https://your_vcd_01/api/vApp/your_vapp_01/power/action/shutdown',
    'test_02': 'https://your_vcd_01/api/vApp/your_vapp_02/power/action/shutdown',
}
def get_token(url, org):
    headers = {
        'Accept': 'application/*;version=35.0',
        'Authorization': 'Basic ' + org
    }
    req = requests.post(url, headers=headers, data={})
    token = req.headers["x-vmware-vcloud-access-token"]
    return token
def req_pow (url, token):
    headers = {
        'Accept': 'application/*;version=35.0',
        'Authorization': 'Bearer ' + token
    }
    req_on = requests.post(url, headers=headers, data={})
def power_on():
    power_on = {
        'eiforia': req_pow(url_power_on['test_01'], get_token(url['url_vcd_01'], org_example_01['test_01'])),
        'antares': req_pow(url_power_on['test_02'], get_token(url['url_vcd_02'], org_example_02['test_02'])),
    }
def power_off():
    power_off = {
        'test01': req_pow(url_power_off['test_01'], get_token(url['url_vcd_01'], org_example_01['test_01'])),
        'test02': req_pow(url_power_off['test_02'], get_token(url['url_vcd_02'], org_example_02['test_02'])),
}
pow_on = Timer(secs_on, power_on)
pow_off = Timer(secs_off, power_off)
pow_on.start()
pow_off.start()
