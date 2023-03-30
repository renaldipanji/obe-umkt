from django.core.mail import send_mail
from django.conf import settings 
import socket


def send_forget_password_mail(email , token, domain, ssl ):
    ssl_cek = ssl
    if not ssl_cek:
        domain = 'http://' + domain
    else:
        domain = 'https://' + domain

    host = socket.gethostname()
    subject = 'Reset Password akun Penilian CPL Kurikulum OBE'
    message = f" "
    link = domain + '/change-password/'+ token +'/'
    html_message = f"""
    
<!DOCTYPE html>
  <html lang="en" >
  <head>
    <meta charset="UTF-8">
    <title>{subject}</title>
    

  </head>
  <body>
  <!-- partial:index.partial.html -->
  <html>
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <title>{subject}</title>
    </head>
    
    <body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0"
    style="margin: 0pt auto; padding: 0px; background:#E3EEFE;">
      <table id="main" width="100%" height="100%" cellpadding="0" cellspacing="0" border="0"
      bgcolor="#E3EEFE">
        <tbody>
          <tr>
            <td valign="top">
              <table class="innermain" cellpadding="0" width="580" cellspacing="0" border="0"
              bgcolor="#E3EEFE" align="center" style="margin:0 auto; table-layout: fixed;">
                <tbody>
                  <tr>
                    <td colspan="4">
                      <table class="logo" width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tbody>
                          <tr>
                            <td colspan="2" height="30"></td>
                          </tr>
                          <tr>
                            <td valign="top" align="center">
                              <a href="https://dev.lastbit.io/" style="display:inline-block; cursor:pointer; text-align:center;">
                                <img src="https://i.postimg.cc/cJygr1FL/logo.png"
                                height="60" width="auto" border="0" alt="lastbit">
                              </a>
                            </td>
                          </tr>
                          <tr>
                            <td colspan="2" height="30"></td>
                          </tr>
                        </tbody>
                      </table>
                      
                      <!-- Main CONTENT -->
                      <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff"
                      style="border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        <tbody>
                          <tr>
                            <td height="40"></td>
                          </tr>
                          <tr style="font-family: -apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif; color:#4E5C6E; font-size:14px; line-height:20px; margin-top:20px;">
                            <td class="content" colspan="2" valign="top" align="center" style="padding-left:90px; padding-right:90px;">
                              <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff">
                                <tbody>
                                  <tr>
                                    <td align="center" valign="bottom" colspan="2" cellpadding="3">
                                      <img alt="lastbit" width="200" src="https://i.imgur.com/LXjRs5h.gif"
                                      />
                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="30" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                    <td align="center"> <span style="color:#00204A;font-size:22px;line-height: 24px;">
            Reset Password Akun LPPMEL
          </span>

                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="24" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                    <td height="1" bgcolor="#DAE1E9"></td>
                                  </tr>
                                  <tr>
                                    <td height="24" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                    <td align="center"> <span style="color:#00204A;font-size:14px;line-height:24px;">
            Kami menerima permintaan reset password akun Penilian CPL Kurikulum OBE anda
          </span><p style="color:#00204A;font-size:14px;line-height:24px;">
            Jika Anda tidak membuat permintaan ini, abaikan saja email ini. Jika tidak, silakan klik tombol di bawah ini untuk reset password akun Penilian CPL Kurikulum OBE anda.
          </p>

                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="20" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                    <td valign="top" width="50%" align="center"> <span>
            <a href="{link}" style="display:block; padding:15px 25px; background-color:#448EF6; color:#ffffff; border-radius:7px; text-decoration:none;">Reset Password akun Penilian CPL Kurikulum OBE</a>
          </span>

                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="20" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                    <td align="center">
                                      <img src="https://i.imgur.com/FjvPESc.png" width="54"
                                      height="2" border="0">
                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="20" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                          <tr>
                            <td height="60"></td>
                          </tr>
                        </tbody>
                      </table>
                  
                      <table id="promo" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:20px;">
                        <tbody>
                          <tr>
                            <td colspan="2" height="20"></td>
                          </tr>
                          <tr>
                            <td colspan="2" align="center"> <span style="font-size:14px; font-weight:500; margin-bottom:10px; color:#7E8A98; font-family: -apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;">Dapatkan Aplikasi SIPEL LPPMEL terbaru untuk ponsel Anda</span>

                            </td>
                          </tr>
                          <tr>
                            <td colspan="2" height="20"></td>
                          </tr>
                          <tr>
                            <td valign="top" width="50%" align="right">
                              <a href="#"
                              style="display:inline-block;margin-right:10px;">
                                <img src="https://i.imgur.com/T5zh5J3.png" height="40"
                                border="0" alt="lastbit iOS">
                              </a>
                            </td>
                            <td valign="top">
                              <a href="#"
                              style="display:inline-block;margin-left:5px;">
                                <img src="https://i.imgur.com/Gv7Z0W8.png"
                                height="40" border="0" alt="lastbit Android ">
                              </a>
                            </td>
                          </tr>
                          <tr>
                            <td colspan="2" height="20"></td>
                          </tr>
                        </tbody>
                      </table>
                  
                    
                      <table width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tbody>
                          <tr>
                            <td height="10">&nbsp;</td>
                          </tr>
                          <tr>
                            <td valign="top" align="center"> <span style="font-family: -apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif; color:#9EB0C9; font-size:10px;">&copy;
                              <a href="https://dev.lastbit.io/" target="_blank" style="color:#999999 !important; text-decoration:none;">LPPMEL 2022</a> 
                            </span>

                            </td>
                          </tr>
                          <tr>
                            <td height="50">&nbsp;</td>
                          </tr>
                        </tbody>
                      </table>
                      
                    </td>
                  </tr>
                </tbody>
              </table>
            </td>
          </tr>
        </tbody>
      </table>
    </body>

  </html>
  <!-- partial -->
    
  </body>
  </html>
"""
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list, html_message=html_message)
    return True

def send_verif_mail(email , token, domain, ssl ):
    ssl_cek = ssl
    if not ssl_cek:
        domain = 'http://' + domain
    else:
        domain = 'https://' + domain

    host = socket.gethostname()
    subject = 'Verifikasi akun Penilian CPL Kurikulum OBE'
    message = f" "
    link = domain + '/verifikasi-berhasil/'+ token +'/'
    html_message = f'''
     <!DOCTYPE html>
  <html lang="en" >
  <head>
    <meta charset="UTF-8">
    <title>{subject}</title>
    

  </head>
  <body>
  <!-- partial:index.partial.html -->
  <html>
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <title>{subject}</title>
    </head>
    
    <body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0"
    style="margin: 0pt auto; padding: 0px; background:#E3EEFE;">
      <table id="main" width="100%" height="100%" cellpadding="0" cellspacing="0" border="0"
      bgcolor="#E3EEFE">
        <tbody>
          <tr>
            <td valign="top">
              <table class="innermain" cellpadding="0" width="580" cellspacing="0" border="0"
              bgcolor="#E3EEFE" align="center" style="margin:0 auto; table-layout: fixed;">
                <tbody>
                  <tr>
                    <td colspan="4">
                      <table class="logo" width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tbody>
                          <tr>
                            <td colspan="2" height="30"></td>
                          </tr>
                          <tr>
                            <td valign="top" align="center">
                              <a href="https://dev.lastbit.io/" style="display:inline-block; cursor:pointer; text-align:center;">
                                <img src="https://i.postimg.cc/cJygr1FL/logo.png"
                                height="60" width="auto" border="0" alt="lastbit">
                              </a>
                            </td>
                          </tr>
                          <tr>
                            <td colspan="2" height="30"></td>
                          </tr>
                        </tbody>
                      </table>
                      
                      <!-- Main CONTENT -->
                      <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff"
                      style="border-radius: 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                        <tbody>
                          <tr>
                            <td height="40"></td>
                          </tr>
                          <tr style="font-family: -apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif; color:#4E5C6E; font-size:14px; line-height:20px; margin-top:20px;">
                            <td class="content" colspan="2" valign="top" align="center" style="padding-left:90px; padding-right:90px;">
                              <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff">
                                <tbody>
                                  <tr>
                                    <td align="center" valign="bottom" colspan="2" cellpadding="3">
                                      <img alt="lastbit" width="200" src="https://i.imgur.com/LXjRs5h.gif"
                                      />
                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="30" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                    <td align="center"> <span style="color:#00204A;font-size:22px;line-height: 24px;">
            Verifikasi Email
          </span>

                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="24" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                    <td height="1" bgcolor="#DAE1E9"></td>
                                  </tr>
                                  <tr>
                                    <td height="24" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                    <td align="center"> <span style="color:#00204A;font-size:14px;line-height:24px;">
            Kami menerima permintaan verifikasi akun Penilian CPL Kurikulum OBE anda
          </span><p style="color:#00204A;font-size:14px;line-height:24px;">
            Jika Anda tidak membuat permintaan ini, abaikan saja email ini. Jika tidak, silakan klik tombol di bawah ini untuk verifikasi akun Penilian CPL Kurikulum OBE anda.
          </p>

                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="20" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                    <td valign="top" width="50%" align="center"> <span>
            <a href="{link}" style="display:block; padding:15px 25px; background-color:#448EF6; color:#ffffff; border-radius:7px; text-decoration:none;">Verifikasi Akun</a>
          </span>

                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="20" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                    <td align="center">
                                      <img src="https://i.imgur.com/FjvPESc.png" width="54"
                                      height="2" border="0">
                                    </td>
                                  </tr>
                                  <tr>
                                    <td height="20" &nbsp;=""></td>
                                  </tr>
                                  <tr>
                                  </tr>
                                </tbody>
                              </table>
                            </td>
                          </tr>
                          <tr>
                            <td height="60"></td>
                          </tr>
                        </tbody>
                      </table>
                  
                      <table id="promo" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:20px;">
                        <tbody>
                          <tr>
                            <td colspan="2" height="20"></td>
                          </tr>
                          <tr>
                            <td colspan="2" align="center"> <span style="font-size:14px; font-weight:500; margin-bottom:10px; color:#7E8A98; font-family: -apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif;">Dapatkan Aplikasi SIPEL LPPMEL terbaru untuk ponsel Anda</span>

                            </td>
                          </tr>
                          <tr>
                            <td colspan="2" height="20"></td>
                          </tr>
                          <tr>
                            <td valign="top" width="50%" align="right">
                              <a href="#"
                              style="display:inline-block;margin-right:10px;">
                                <img src="https://i.imgur.com/T5zh5J3.png" height="40"
                                border="0" alt="lastbit iOS">
                              </a>
                            </td>
                            <td valign="top">
                              <a href="#"
                              style="display:inline-block;margin-left:5px;">
                                <img src="https://i.imgur.com/Gv7Z0W8.png"
                                height="40" border="0" alt="lastbit Android ">
                              </a>
                            </td>
                          </tr>
                          <tr>
                            <td colspan="2" height="20"></td>
                          </tr>
                        </tbody>
                      </table>
                  
                    
                      <table width="100%" cellpadding="0" cellspacing="0" border="0">
                        <tbody>
                          <tr>
                            <td height="10">&nbsp;</td>
                          </tr>
                          <tr>
                            <td valign="top" align="center"> <span style="font-family: -apple-system,BlinkMacSystemFont,&#39;Segoe UI&#39;,&#39;Roboto&#39;,&#39;Oxygen&#39;,&#39;Ubuntu&#39;,&#39;Cantarell&#39;,&#39;Fira Sans&#39;,&#39;Droid Sans&#39;,&#39;Helvetica Neue&#39;,sans-serif; color:#9EB0C9; font-size:10px;">&copy;
                              <a href="https://dev.lastbit.io/" target="_blank" style="color:#999999 !important; text-decoration:none;">LPPMEL 2022</a> 
                            </span>

                            </td>
                          </tr>
                          <tr>
                            <td height="50">&nbsp;</td>
                          </tr>
                        </tbody>
                      </table>
                      
                    </td>
                  </tr>
                </tbody>
              </table>
            </td>
          </tr>
        </tbody>
      </table>
    </body>

  </html>
  <!-- partial -->
    
  </body>
  </html>
'''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list, html_message=html_message)
    return True