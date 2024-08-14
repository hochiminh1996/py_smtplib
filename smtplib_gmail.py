# Objetivo: disparar e-mail utilizando a biblioteca sptmlib

import smtplib
# Importa o módulo smtplib, que permite o envio de emails usando o protocolo SMTP.
import email.message
# Importa o módulo email.message, que fornece classes para criar e manipular mensagens de email.

# função de envio de e-mail

def enviar_email():
    
    corpo_email = f"""
    <p>Prezados(a), <br>Bom dia.</p>

    <p>Teste inicial de disparo smtp</p>
    """
    # Define uma string contendo o corpo do email em formato HTML.

    msg = email.message.Message()
    # Cria uma nova instância da classe 'Message' para compor o email.

    msg['Subject'] = "SMTPLIB: Teste"
    # Define o assunto do email.

    msg['From'] = "windows1111011@gmail.com"
    # Define o remetente do email. Minhas credenciais de gmail. Teste outlook

    msg['To'] = "ambrsp@hotmail.com"
    # Define o destinatário

    password= "************"
    # Define a senha do email do remetente. Senha gerado pelo provedor smtp do meu e-mail gmail (necessário habilitar a verificação de duas etapas e gerar a senha em 'Senhas de app')

    msg.add_header("Content-Type", "text/html; charset=utf-8")
    # Adiciona um cabeçalho indicando que o conteúdo do email é HTML e utiliza a codificação UTF-8.

    msg.set_payload(corpo_email)
    # Define o conteúdo do email com o corpo especificado anteriormente.

    s = smtplib.SMTP("smtp.gmail.com: 587")
    # Conecta ao servidor SMTP do Gmail na porta 587.

    s.starttls()
    # Inicia uma conexão segura com o servidor usando TLS.

    s.login(msg['From'], password)
    # Realiza o login no servidor SMTP usando as credenciais do remetente.

    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode("utf-8"))
    # Envia o email utilizando o método 'sendmail', passando o remetente, destinatário e a mensagem.

    s.quit()
    # Encerra a conexão com o servidor SMTP.

    print("Sucesso")

enviar_email()
# chamando nossa função