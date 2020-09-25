#!/usr/bin/env python
#coding: utf-8

import requests
import os, sys
import time, random
from datetime import datetime

tempo = datetime.now()

os.system("clear")
cores = ["\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m", "\033[1;37m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m", "\033[37m", "\033[90m", "\033[m"]

def banner():
    try:
        msg = "\t\t[ \033[1;31mFHC \033[1;37m-\033[1;31m FR13NDs Hackers Club \033[m ]\n"
        for i in msg:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
    except KeyboardInterrupt:
        msg = "\n\033[1;33m[\033[1;31m-\033[1;33m] \033[1;31mCtrl C \033[1;37m- \033[1;33mDetectado!\033[m\n"
        for i in msg:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
        exit(0)

    dados = """
    \033[1;33m==========================[ \033[1;36mDADOS\033[m\033[1;33m ]=============================
    | \033[1;31mAutor\033[1;37m:\033[m \033[31mHagbard Celine\033[1;33m                                        |
    | \033[1;32mGrupo\033[1;37m:\033[m \033[32mFHC - FR13NDs Hackers Club\033[1;33m                                   |
    | \033[1;34mFacebook\033[1;37m:\033[m \033[34mhttps://www.facebook.com/miraldino.paulodoria.3\033[1;33m    |
    | \033[1;35mPage FB\033[1;37m:\033[m \033[35mhttps://www.facebook.com/termuxoficial\033[1;33m              |
    \033[1;33m================================================================\033[m\033[31m
    """
    logo = """     _____ _           _              _       _           _       
    |  ___(_)_ __   __| |            / \   __| |_ __ ___ (_)_ __  
    | |_  | | '_ \ / _` |  _____    / _ \ / _` | '_ ` _ \| | '_ \ 
    |  _| | | | | | (_| | |_____|  / ___ \ (_| | | | | | | | | | |
    |_|   |_|_| |_|\__,_|         /_/   \_\__,_|_| |_| |_|_|_| |_|"""
    print(random.choice(cores)+logo)
    print(dados)

banner()
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0"}
print(r"┌─[hagbardceline@ccc─[ex: https://exemplo.com]")
try:
    site = raw_input(r"└──╼ $ ")
except KeyboardInterrupt:
        msg = "\n\n\033[1;33m[\033[1;31m-\033[1;33m] \033[1;31mCtrl C \033[1;37m- \033[1;33mDetectado!\033[m\n"
        for i in msg:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
        exit(0)
except:
        print("\033[1;33m[\033[1;31m-\033[1;33m] \033[1;32mOcorreu um erro! :(\033[m\n")
        sys.exit(0)

robots = site + "/robots.txt"
try:
    msginit = "\n\033[1;32m[\033[1;31m!\033[1;32m] \033[1;33mIniciando a Busca: \033[1;31m%s\033[m\n" % tempo
    for i in msginit:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
    robot = requests.get(robots, headers=header)
    code_robots = robot.status_code
    open_robots = robot.text
    if code_robots == 200:
        print "\n\033[1;32m[\033[1;33m+\033[1;32m] \033[36mFile robots.txt Found: \033[1;31m%s\033[m" % robots
        time.sleep(1.2)
        print "\n\033[34m============= \033[1;36mROBOTS.TXT\033[m \033[34m===============\033[37m"
        print open_robots
        print "\033[34m========================================\n"
        time.sleep(2)
    else:
        print "\n\033[37m============= \033[1;31mROBOTS.TXT\033[m \033[37m===============\033[37m"
        print "\033[1;33m[\033[1;31m!\033[1;33m] \033[36mFile robots.txt not found: \033[1;32m%s\033[m" % robots
        print "\033[37m========================================\n"
        time.sleep(1)
except KeyboardInterrupt:
    msg = "\n\n\033[1;33m[\033[1;31m-\033[1;33m] \033[1;31mCtrl C \033[1;37m- \033[1;33mDetectado!\033[m\n"
    for i in msg:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)
        sys.exit(0)
except:
        msg = "\033[1;33m[\033[1;31m-\033[1;33m] \033[1;32mOcorreu um erro! :(\033[m\n"
        for i in msg:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.03)
            sys.exit(0)

paths = ["/acceso.asp",
"/acceso.php",
"/access/",
"/access.php",
"/account/",
"/account.asp",
"/account.html",
"/account.php",
"/acct_login/",
"/_adm_/",
"/_adm/",
"/adm/",
"/adm2/",
"/adm/admloginuser.asp",
"/adm/admloginuser.php",
"/adm.asp",
"/adm_auth.asp",
"/adm_auth.php",
"/adm.html",
"/_admin_/",
"/_admin/",
"/admin/",
"/admin/",
"/admin/",
"/admin1/",
"/admin1.asp",
"/admin1.html",
"/admin1.php",
"/admin2/",
"/admin2.asp",
"/admin2.html",
"/admin2/index/",
"/admin2/index.asp",
"/admin2/index.php",
"/admin2/login.asp",
"/admin2/login.php",
"/admin2.php",
"/admin3/",
"/admin4/",
"/admin4_account/",
"/admin4_colon/",
"/admin5/",
"/admin/account.asp",
"/admin/account.html",
"/admin/account.php",
"/admin/add_banner.php/",
"/admin/addblog.php",
"/admin/add_gallery_image.php",
"/admin/add.php",
"/admin/add-room.php",
"/admin/add-slider.php",
"/admin/add_testimonials.php",
"/admin/admin/",
"/admin/adminarea.php",
"/admin/admin.asp",
"/admin/AdminDashboard.php",
"/admin/admin-home.php",
"/admin/AdminHome.php",
"/admin/admin.html",
"/admin/admin_index.php",
"/admin/admin_login.asp",
"/admin/admin-login.asp",
"/admin/adminLogin.asp",
"/admin/admin_login.html",
"/admin/admin-login.html",
"/admin/adminLogin.html",
"/admin/admin_login.php",
"/admin/admin-login.php",
"/admin/adminLogin.php",
"/admin/admin_management.php",
"/admin/admin.php",
"/admin/admin_users.php",
"/admin/adminview.php",
"/admin/adm.php",
"/admin_area/",
"/adminarea/",
"/admin_area/admin.asp",
"/adminarea/admin.asp",
"/admin_area/admin.html",
"/adminarea/admin.html",
"/admin_area/admin.php",
"/adminarea/admin.php",
"/admin_area/index.asp",
"/adminarea/index.asp",
"/admin_area/index.html",
"/adminarea/index.html",
"/admin_area/index.php",
"/adminarea/index.php",
"/admin_area/login.asp",
"/adminarea/login.asp",
"/admin_area/login.html",
"/adminarea/login.html",
"/admin_area/login.php",
"/adminarea/login.php",
"/admin.asp",
"/admin/banner.php",
"/admin/banners_report.php",
"/admin/category.php",
"/admin/change_gallery.php",
"/admin/checklogin.php",
"/admin/configration.php",
"/admincontrol.asp",
"/admincontrol.html",
"/admincontrol/login.asp",
"/admincontrol/login.html",
"/admincontrol/login.php",
"/admin/control_pages/admin_home.php",
"/admin/controlpanel.asp",
"/admin/controlpanel.html",
"/admin/controlpanel.php",
"/admincontrol.php",
"/admincontrol.php/",
"/admin/cpanel.php",
"/admin/cp.asp",
"/admin/CPhome.php",
"/admin/cp.html",
"/admincp/index.asp",
"/admincp/index.html",
"/admincp/login.asp",
"/admin/cp.php",
"/admin/dashboard/index.php",
"/admin/dashboard.php",
"/admin/dashbord.php",
"/admin/dash.php",
"/admin/default.php",
"/adm/index.asp",
"/adm/index.html",
"/adm/index.php",
"/admin/enter.php",
"/admin/event.php",
"/admin/form.php",
"/admin/gallery.php",
"/admin/headline.php",
"/admin/home.asp",
"/admin/home.html",
"/admin_home.php",
"/admin/home.php",
"/admin.html",
"/admin/index.asp"
"/admin/index-digital.php",
"/admin/index.html",
"/admin/index.php",
"/admin/index_ref.php",
"/admin/initialadmin.php",
"/administer/",
"/administr8/",
"/administr8.asp",
"/administr8.html",
"/administr8.php",
"/administracion.php",
"/administrador/",
"/administratie/",
"/administration/",
"/administration.html",
"/administration.php",
"/administrator",
"/_administrator_/",
"/_administrator/",
"/administrator/",
"/administrator/account.asp",
"/administrator/account.html",
"/administrator/account.php",
"/administratoraccounts/",
"/administrator.asp",
"/administrator.html",
"/administrator/index.asp",
"/administrator/index.html",
"/administrator/index.php",
"/administratorlogin/",
"/administrator/login.asp",
"/administratorlogin.asp",
"/administrator/login.html",
"/administrator/login.php",
"/administratorlogin.php",
"/administratorlogin.php",
"/administrator.php",
"/administrators/",
"/administrivia/",
"/admin/leads.php",
"/admin/list_gallery.php",
"/admin/login",
"/adminLogin/",
"/admin_login.asp",
"/admin-login.asp",
"/admin/login.asp",
"/adminLogin.asp",
"/admin/login-home.php",
"/admin_login.html",
"/admin-login.html",
"/admin/login.html",
"/adminLogin.html",
"/admin/login.html",
"/admin_login.php",
"/admin_login.php",
"/admin-login.php",
"/admin-login.php/",
"/admin/login.php",
"/adminLogin.php",
"/admin/login.php",
"/admin/login_success.php",
"/admin/loginsuccess.php",
"/admin/log.php",
"/admin_main.html",
"/admin/main_page.php",
"/admin/main.php/",
"/admin/ManageAdmin.php",
"/admin/manageImages.php",
"/admin/manage_team.php",
"/admin/member_home.php",
"/admin/moderator.php",
"/admin/my_account.php",
"/admin/myaccount.php",
"/admin/overview.php",
"/admin/page_management.php",
"/admin/pages/home_admin.php",
"/adminpanel/",
"/adminpanel.asp",
"/adminpanel.html",
"/adminpanel.php",
"/admin.php",
"/admin/private/",
"/adminpro/",
"/admin/product.php",
"/admin/products.php",
"/admins/",
"/admins.asp",
"/admin/save.php",
"/admins.html",
"/admin/slider.php",
"/admin/specializations.php",
"/admins.php",
"/admin_tool/",
"/AdminTools/",
"/admin/uhome.html",
"/admin/upload.php",
"/admin/userpage.php",
"/admin/viewblog.php",
"/admin/viewmembers.php",
"/admin/voucher.php",
"/AdminWeb/",
"/admin/welcomepage.php",
"/admin/welcome.php",
"/admloginuser.asp",
"/admloginuser.php",
"/admon/",
"/ADMON/",
"/adm.php",
"/affiliate.asp",
"/affiliate.php",
"/auth/",
"/auth/login/",
"/authorize.php",
"/autologin/",
"/banneradmin/",
"/base/admin/",
"/bb-admin/,"
"/bbadmin/",
"/bb-admin/admin.asp",
"/bb-admin/admin.html",
"/bb-admin/admin.php",
"/bb-admin/index.asp",
"/bb-admin/index.html",
"/bb-admin/index.php",
"/bb-admin/login.asp",
"/bb-admin/login.html",
"/bb-admin/login.php",
"/bigadmin/",
"/blogindex/",
"/cadmins/",
"/ccms/",
"/ccms/index.php",
"/ccms/login.php",
"/ccp14admin/",
"/cms/",
"/cms/admin/",
"/cmsadmin/",
"/cms/_admin/logon.php",
"/cms/login/",
"/configuration/",
"/configure/",
"/controlpanel/",
"/controlpanel.asp",
"/controlpanel.html",
"/controlpanel.php",
"/cpanel/",
"/cpanel_file/",
"/cp.asp",
"/cp.html",
"/cp.php",
"/customer_login/",
"/database_administration/",
"/Database_Administration/",
"/db/admin.php",
"/directadmin/",
"/dir-login/",
"/editor/",
"/edit.php",
"/evmsadmin/",
"/ezsqliteadmin/",
"/fileadmin/",
"/fileadmin.asp",
"/fileadmin.html",
"/fileadmin.php",
"/formslogin/",
"/forum/admin",
"/globes_admin/",
"/home.asp",
"/home.html",
"/home.php",
"/hpwebjetadmin/",
"/include/admin.php",
"/includes/login.php",
"/Indy_admin/",
"/instadmin/",
"/interactive/admin.php",
"/irc-macadmin/",
"/links/login.php",
"/LiveUser_Admin/",
"/login/",
"/login1/",
"/login.asp",
"/login_db/",
"/loginflat/",
"/login.html",
"/login/login.php",
"/login.php",
"/login-redirect/",
"/logins/",
"/login-us/",
"/logon/",
"/logo_sysadmin/",
"/Lotus_Domino_Admin/",
"/macadmin/",
"/mag/admin/",
"/maintenance/",
"/manage_admin.php",
"/manager/",
"/manager/ispmgr/",
"/manuallogin/",
"/memberadmin/",
"/memberadmin.asp",
"/memberadmin.php",
"/members/",
"/memlogin/",
"/meta_login/",
"/modelsearch/admin.asp",
"/modelsearch/admin.html",
"/modelsearch/admin.php",
"/modelsearch/index.asp",
"/modelsearch/index.html",
"/modelsearch/index.php",
"/modelsearch/login.asp",
"/modelsearch/login.html",
"/modelsearch/login.php",
"/moderator/",
"/moderator/admin.asp",
"/moderator/admin.html",
"/moderator/admin.php",
"/moderator.asp",
"/moderator.html",
"/moderator/login.asp",
"/moderator/login.html",
"/moderator/login.php",
"/moderator.php",
"/moderator.php/",
"/myadmin/",
"/navSiteAdmin/",
"/newsadmin/",
"/nsw/admin/login.php",
"/openvpnadmin/",
"/pages/admin/admin-login.asp",
"/pages/admin/admin-login.html",
"/pages/admin/admin-login.php",
"/panel/",
"/panel-administracion/",
"/panel-administracion/admin.asp",
"/panel-administracion/admin.html",
"/panel-administracion/admin.php",
"/panel-administracion/index.asp",
"/panel-administracion/index.html",
"/panel-administracion/index.php",
"/panel-administracion/login.asp",
"/panel-administracion/login.html",
"/panel-administracion/login.php",
"/panelc/",
"/paneldecontrol/",
"/panel.php",
"/pgadmin/",
"/phpldapadmin/",
"/phpmyadmin/",
"/phppgadmin/",
"/phpSQLiteAdmin/",
"/platz_login/",
"/pma/",
"/power_user/",
"/project-admins/",
"/pureadmin/",
"/radmind/",
"/radmind-1/",
"/rcjakar/admin/login.php",
"/rcLogin/",
"/server/",
"/server/",
"/serverAdministrator/",
"/server_admin_small/",
"/server.asp",
"/server.html",
"/server.php",
"/showlogin/",
"/simpleLogin/",
"/site/admin/",
"/siteadmin/",
"/siteadmin/index.asp",
"/siteadmin/index.php",
"/siteadmin/login.asp",
"/siteadmin/login.html",
"/site_admin/login.php",
"/siteadmin/login.php",
"/smblogin/",
"/sql-admin/",
"/sshadmin/",
"/ss_vms_admin_sm/",
"/staradmin/",
"/sub-login/",
"/Super-Admin/",
"/support_login/",
"/sys-admin/",
"/sysadmin/",
"/SysAdmin/",
"/SysAdmin2/",
"/sysadmin.asp",
"/sysadmin.html",
"/sysadmin.php",
"/sysadmins/",
"/system_administration/"
"/system-administration/"
"/typo3/",
"/ur-admin/",
"/ur-admin.asp",
"/ur-admin.html",
"/ur-admin.php",
"/useradmin/"
"/user.asp",
"/user.html",
"/UserLogin/"
"/user.php",
"/usuario/",
"/usuarios/",
"/usuarios/",
"/usuarios/login.php",
"/utility_login/",
"/vadmind/",
"/vmailadmin/",
"/webadmin/",
"/webAdmin/",
"/webadmin/admin.asp",
"/webadmin/admin.html",
"/webadmin/admin.php",
"/webadmin.asp",
"/webadmin.html",
"/webadmin/index.asp",
"/webadmin/index.html",
"/webadmin/index.php",
"/webadmin/login.asp",
"/webadmin/login.html",
"/webadmin/login.php",
"/webadmin.php",
"/webmaster/",
"/websvn/",
"/wizmysqladmin/",
"/wp-admin/",
"/wp-login/",
"/wplogin/",
"/wp-login.php",
"/xlogin/",
"/yonetici.asp",
"/yonetici.html",
"/yonetici.php",
"/yonetim.asp",
"/yonetim.html",
"/yonetim.php",]
for path in paths:
    url = site + path
    try:
        req = requests.get(url, headers=header)
        code = req.status_code
        if code == 200:
            print "\033[1;32m[\033[1;33m+\033[1;32m] \033[32mPage Found: \033[1;31m%s\033[m" % url
            time.sleep(1)
        else:
            print "\033[1;33m[\033[1;31m!\033[1;33m] \033[36mPage not found: \033[1;32m%s\033[m" % url
    except KeyboardInterrupt:
        msg = "\n\n\033[1;33m[\033[1;31m-\033[1;33m] \033[1;31mCtrl C \033[1;37m- \033[1;33mDetectado!\033[m\n"
        for i in msg:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.02)
        exit(0)
    except:
        print("\033[1;33m[\033[1;31m-\033[1;33m] \033[1;32mOcorreu um erro! :(\033[m\n")
        sys.exit(0)

msgf = "\n\033[1;32m[\033[1;31m!\033[1;32m] \033[1;33mBusca Terminada: \033[1;31m%s\033[m" % tempo
for i in msgf:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.02)
print
	
	
	
	
	
	
	
	
	
	
	
	
	
