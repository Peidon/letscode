from __future__ import print_function

from datetime import datetime
import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

CalenderIDs = \
    {"SG": "en.singapore.official#holiday@group.v.calendar.google.com",
     "ID": "en.indonesian.official#holiday@group.v.calendar.google.com",
     "TH": "en.th.official#holiday@group.v.calendar.google.com",
     "VN": "en.vietnamese.official#holiday@group.v.calendar.google.com",
     "PH": "en.philippines.official#holiday@group.v.calendar.google.com",
     "TW": "en.taiwan.official#holiday@group.v.calendar.google.com",
     "MY": "en.malaysia.official#holiday@group.v.calendar.google.com",
     "CN": "en.china.official#holiday@group.v.calendar.google.com",
     "BR": "en.brazilian.official#holiday@group.v.calendar.google.com"
     }


class Holiday:

    def __init__(self, start, end, description):
        self.start = start
        self.end = end
        self.description = description

    def toMap(self):
        return {"start": self.start, "end": self.end, "description": self.description}


def _start_with(key, prefix):
    prefix_len = len(prefix)
    return key[:prefix_len] == prefix


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    cred = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        cred = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            cred = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(cred.to_json())

    try:
        service = build('calendar', 'v3', credentials=cred)

        # page_token = None
        # while True:
        #     calendar_list = service.calendarList().list(pageToken=page_token).execute()
        #     for calendar_list_entry in calendar_list['items']:
        #         print(calendar_list_entry['id'] + ', ' + calendar_list_entry['summary'])
        #     page_token = calendar_list.get('nextPageToken')
        #     if not page_token:
        #         break

        h_maps = {}

        now = datetime.utcnow()
        year = now.year + 1

        for cid in CalenderIDs:
            calendar_id = CalenderIDs[cid]
            holiday_list = []

            # Call the Calendar API
            events_result = service.events().list(calendarId=calendar_id,
                                                  timeMin=datetime(year, 1, 1).isoformat() + 'Z', # 'Z' indicates UTC time
                                                  maxResults=100, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])

            # calendar = service.calendars().get(calendarId=calendar_id).execute()
            #
            # if not calendar:
            #     print('No calendar found, ' + "cid = " + cid)
            #     continue

            if not events:
                print('No upcoming events found.' + "cid = " + cid)
                continue

            print("holidays in " + cid)
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                if not _start_with(start, str(year)):
                    continue
                end = event['end'].get("dateTime", event['end'].get('date'))
                print(start, end, event['summary'])
                holiday_list.append(Holiday(start, end, event['summary']).toMap())

            h_maps[cid] = holiday_list

        conf_data = json.dumps(h_maps)
        with open("holidays" + ".json", "w") as f:
            n = f.write(conf_data)
            print("{} bytes have been writen into file".format(n))

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
