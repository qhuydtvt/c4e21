from gmail import GMail, Message

mail = GMail("c4e21.test", "codethechange18")
body = '''
<p><strong>Xin nghĩ ốm,&nbsp;</strong></p>
<p>&nbsp;</p>
<p><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-innocent.gif" alt="innocent" /><img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-laughing.gif" alt="laughing" /></p>
<p>Huy</p>
'''

msg = Message("HuyNQ - Xin nghỉ ốm", to="qhuydtvt@gmail.com", html=body)
mail.send(msg)