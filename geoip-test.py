import requests


print(requests.get("https://nordvpn.com/wp-admin/admin-ajax.php?action=get_user_info_data&ip=73.19.32.8").json()["country"])