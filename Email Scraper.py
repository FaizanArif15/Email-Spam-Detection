import imaplib
import email
from email.header import decode_header
import csv
import os

# account credentials
username = "abc@gmail.com"
password = "defg hijk lmno pqrs"

# connect to the server and login
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

# function to decode email body with multiple encodings
def decode_email_body(body_bytes):
    encodings = ['utf-8', 'latin-1', 'windows-1252']
    for encoding in encodings:
        try:
            return body_bytes.decode(encoding)
        except UnicodeDecodeError:
            continue
    return body_bytes.decode('utf-8', errors='replace')

# open a CSV file to write the email details
with open('emails.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Folder', 'Subject', 'From', 'Date', 'Body']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    folders = ["inbox", "[Gmail]/Spam"]
    for folder in folders:
        mail.select(folder)
        # search emails using the filter
        status, messages = mail.search(None, 'SINCE "15-JUL-2024" BEFORE "18-JUL-2024"')
        if status != "OK":
            print(f"Failed to search emails in {folder}.")
            continue

        messages = messages[0].split()
        if not messages:
            print(f"No emails found in {folder} for the given date range.")
            continue

        for mail_id in messages:
            status, msg_data = mail.fetch(mail_id, "(RFC822)")
            if status != "OK":
                print(f"Failed to fetch email ID {mail_id} in {folder}.")
                continue

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    from_ = msg.get("From")
                    date = msg.get("Date")
                    body = ""

                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            try:
                                part_body = part.get_payload(decode=True)
                            except:
                                part_body = b""
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                body += decode_email_body(part_body)
                    else:
                        content_type = msg.get_content_type()
                        body_bytes = msg.get_payload(decode=True)
                        body = decode_email_body(body_bytes)

                    # write email details to the CSV file
                    writer.writerow({'Folder': folder, 'Subject': subject, 'From': from_, 'Date': date, 'Body': body})

# close the connection and logout
mail.close()
mail.logout()
