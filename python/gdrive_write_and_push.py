from googleapiclient import http

def mount_gdrive():
    """
    change dir to mounted client S3 dir
    this is to source the Google Drive API .json
    """
    from os import chdir, getcwd
    chdir("/dbfs/mnt/client/GoogleDrive/")
    return getcwd()

def mount_client_output(env):
    """
    change dir to mounted client S3 dir
    this is to source the Client Output Dir
    """
    from os import chdir, getcwd
    chdir("/dbfs/mnt/client-" + env + "/output/")
    return getcwd()

def gdrive_discovery_service(api_dir):
    """
    set up google drive discovery api and return the service built
    """
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError as HTTPError

    SCOPES = ['https://www.googleapis.com/auth/drive']
    json_key = 'my_key_12345678.json'
    sa_creds = service_account.Credentials.from_service_account_file(api_dir + str(json_key))
    scoped_creds = sa_creds.with_scopes(SCOPES)

    driveadmin = build(serviceName='drive', version='v3', credentials=scoped_creds, static_discovery=False)
    return driveadmin

def list_files_in_gdrive(driveadmin):
    """
    retrieve list of files in drive using google drive discovery service API
    in descending order. the most recent shows up first.
    """

    results = driveadmin.files().list(
    pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    first_item = results.get('files', [])[0]

    if not items:
        print("No files found")
    else:
        print("Files:")
    for item in items:
        print(u'{0} ({1})'.format(item['name'], item['id']))
        
    return first_item

def upload_file_to_gdrive(file_name, driveadmin, output_dir):
  """
  take a file from mounted S3 and upload to Google Drive
  returns a file ID from Google Drive
  """

  from googleapiclient.http import MediaFileUpload

  # upload a file
  file_metadata = {
      'name': file_name,
      'mimeType': 'application/vnd.google-apps.spreadsheet'
  }
  # it was MediaFileUpload
  media = MediaFileUpload(output_dir + "/" + file_name,
                          mimetype='application/vnd.ms-excel',
                          chunksize=1024*1024,
                          resumable=True)
  file = driveadmin.files().create(body=file_metadata,
                                      media_body=media,
                                      fields='id').execute()
  print('File ID: %s' % file.get('id'))
  return file.get('id')

def file_name():
    import datetime
    today = datetime.date.today()
    dateTagFinal = today.strftime("%Y_%m_%d")
    return "Client Info List_" + dateTagFinal + ".xlsx"

def email_report_stakeholders(driveadmin, email_address, file_id):
    """
    take the connection, the email, and the file ID to email stakeholders
    it doesn't return.
    """
    def _callback(request_id, response, exception):
        if exception:
            # Handle error
            print(exception)
        else:
            print("Permission Id: %s" % response.get('id'))

    batch = driveadmin.new_batch_http_request(callback=_callback)
    user_permission = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': email_address
    } 
    batch.add(driveadmin.permissions().create(
            fileId=file_id,
            body=user_permission,
            fields='id',
    ))
    domain_permission = {
        'type': 'domain',
        'role': 'reader',
        'domain': 'my_domain.com' # fill this in with actual domain, or param for domain
    }
    batch.add(driveadmin.permissions().create(
            fileId=file_id,
            body=domain_permission,
            fields='id',
    ))
    batch.execute()

if __name__ == '__main__':
    gdrive_file_id = upload_file_to_gdrive(
        file_name=file_name(), 
        driveadmin=gdrive_discovery_service(mount_gdrive()), 
        output_dir=mount_client_output("production")
        )
    emails_to_send = [
        "person1@my_domain.com", 
        "person2@my_domain.com", 
        "person3@my_domain.com", 
        "evonne.cho@my_domain.com"
        ]
    for email_address in emails_to_send:
        email_report_stakeholders(
            driveadmin=gdrive_discovery_service(mount_gdrive()), 
            email_address=email_address, 
            file_id=gdrive_file_id
            )