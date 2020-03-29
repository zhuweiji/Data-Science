import imapclient
import datetime
import pyzmail

DAYS_TO_CHECK = 7
today = datetime.date.today()
last_week = today - datetime.timedelta(days=DAYS_TO_CHECK)

user = "wzhu002@e.ntu.edu.sg"   # "pigoichicken@gmail.com"
pingword = "1012973312wG"   # '1012978179tT'

conn = imapclient.IMAPClient('imap-mail.outlook.com', ssl=True)
conn.login(user, pingword)
conn.select_folder('INBOX', readonly=True)

# option = int(input("Enter 1 to search from a date,\n2 to search last week"))
# check_date = list(map(int, input("Date to check from in dd mm yy format:").split()))
# day, month, year = check_date

UIDS = conn.search(['SINCE', last_week])
if UIDS == 0:
    print("Error getting emails")
    conn.logout()
    exit(-1)

print(UIDS)
for email in UIDS:
    raw_email = conn.fetch([email], ['BODY[]', 'FLAGS'])
    message = pyzmail.parse.PyzMessage.factory(raw_email[email][b'BODY[]'])
    subject = message.get_subject()
    if "due soon" in subject:
        print(subject)
        try:
            body = message.text_part.get_payload().decode('UTF-8')
            key = body.find("Due" or "due")
            due_date = body[key+3:key+45]
            print(due_date)
            # print(datetime.datetime.strftime(due_date, "%A %B %-d %Y"))

        except UnicodeDecodeError:
            print("cannot parse", subject)

    # progress report
    if email == UIDS[::50]:
        print(" --------------------------- checked 50 emails ------------------------------- ")


conn.logout()
