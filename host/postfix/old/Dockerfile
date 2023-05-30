FROM ubuntu:latest

RUN apt update && apt install -y \
    postfix \
    mailutils \
    dovecot-core \
    dovecot-imapd \
    dovecot-pop3d \
    dovecot-lmtpd

COPY main.cf /etc/postfix/main.cf
COPY dovecot.conf /etc/dovecot/dovecot.conf

EXPOSE 25 993 995

CMD service dovecot start && postfix start-fg
