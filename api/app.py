from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

# Custom logo
logo2 = """
 Developed By Termux_Team_BD_0
"""
@app.route('/', methods=['GET','POST'])
def index():
  return redirect("https://www.facebook.com/md.hr.o.o.2024", code=302)
@app.route('/call/api/v1', methods=['GET'])
def send_verification():
    # Get mobile number from URL parameter
    mobile_number = request.args.get('num')
    if mobile_number == "01621756366":
    	return " Fuck You🙂"
    
    if not mobile_number:
        return jsonify({
            "status": "error",
            "message": "Mobile number is required as 'num' parameter"
        }), 400

    url = "https://www.pkluck00.com/wps/verification/sms/register"

    headers = {
        "Host": "www.pkluck00.com",
        "Content-Length": "53",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Android WebView";v="128"',
        "Language": "BN",
        "sec-ch-ua-mobile": "?1",
        "Authorization": "",
        "User-Agent": "Mozilla/5.0 (Linux; Android 12; itel S665L Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.146 Mobile Safari/537.36",
        "Merchant": "pklubdtf4",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "ModuleID": "REGMOBVERF3",
        "sec-ch-ua-platform": '"Android"',
        "Origin": "https://www.pkluck00.com",
        "X-Requested-With": "mark.via.gp",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.pkluck00.com/m/register?affiliateCode=pklkdx117",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i"
    }

    data = {
        "mobileNo": mobile_number,
        "countryDialingCode": "880"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            return jsonify({
                "status": "success",
                "message": "Verification SMS sent successfully",
                "mobile_number": mobile_number,
                "logo": logo2,
                "owner": "Md:HR"
            })
        else:
            return jsonify({
                "status": "error",
                "code": response.status_code,
                "message": response.text,
                "mobile_number": mobile_number
            }), 400
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e),
            "mobile_number": mobile_number
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000)