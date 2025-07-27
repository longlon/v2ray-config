import requests
import os
import base64

# Define the fixed text for the initial configuration
fixed_text = """#profile-title: base64:8J+GkyBHaXRodWIgfCBCYXJyeS1mYXIg8J+ltw==
#profile-update-interval: 1
#subscription-userinfo: upload=29; download=12; total=10737418240000000; expire=2546249531
#support-url: https://github.com/barry-far/V2ray-config
#profile-web-page-url: https://github.com/barry-far/V2ray-config
"""


ptt = os.path.abspath(os.path.join(os.getcwd(), '..'))
vmess_file = os.path.join(ptt, 'Splitted-By-Protocol/vmess.txt')
vless_file = os.path.join(ptt, 'Splitted-By-Protocol/vless.txt')
trojan_file = os.path.join(ptt, 'Splitted-By-Protocol/trojan.txt')
ss_file = os.path.join(ptt, 'Splitted-By-Protocol/ss.txt')
ssr_file = os.path.join(ptt, 'Splitted-By-Protocol/ssr.txt')

open(vmess_file, "w").close()
open(vless_file, "w").close()
open(trojan_file, "w").close()
open(ss_file, "w").close()
open(ssr_file, "w").close()

vmess = ""
vless = ""
trojan = ""
ss = ""
ssr = ""

# Read from local All_Configs_Sub.txt file instead of GitHub
local_config_file = os.path.join(ptt, 'All_Configs_Sub.txt')
if os.path.exists(local_config_file):
    with open(local_config_file, 'r', encoding='utf-8') as f:
        response_text = f.read()
else:
    # Fallback to GitHub if local file doesn't exist
    response_text = requests.get("https://raw.githubusercontent.com/barry-far/V2ray-config/main/All_Configs_Sub.txt").text

for config in response_text.splitlines():
    if config.startswith("vmess"):
        vmess += config + "\n"     
    elif config.startswith("vless"):
        vless += config + "\n"  
    elif config.startswith("trojan"):
        trojan += config + "\n"   
    elif config.startswith("ssr"):  # Check ssr first before ss
        ssr += config + "\n"
    elif config.startswith("ss"):   
        ss += config + "\n"
 
# Write all protocol files with headers
with open(vmess_file, "w", encoding="utf-8") as f:
    f.write(fixed_text + vmess)
with open(vless_file, "w", encoding="utf-8") as f:
    f.write(fixed_text + vless)
with open(trojan_file, "w", encoding="utf-8") as f:
    f.write(fixed_text + trojan)
with open(ss_file, "w", encoding="utf-8") as f:
    f.write(fixed_text + ss)
with open(ssr_file, "w", encoding="utf-8") as f:
    f.write(fixed_text + ssr)  
