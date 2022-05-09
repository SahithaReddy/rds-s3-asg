from config import app,client
from flask import request

@app.route('/upload-image',methods=['POST'])
def upload_image():
    bucket='fresher1'
    content_type=request.mimetype
    obj=request.files['file']
    filename=obj.filename
    client.put_object(Body=obj,
          Bucket=bucket,
          Key=filename,
          ContentType=content_type
    )

    return {'message': 'file uploaded'}, 200

@app.route("/download-file/<string:filename>",methods=["GET"])
def getFileToDownload(filename):
      client.download_file('mybuck65',filename,"c:\\new-downloads\\"+filename)
      return {"message ": "check the download folder"}, 200 