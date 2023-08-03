import time
from flask import request
import requests
from flask_restful import Resource
import pandas as pd
import zipfile
import io
import os
from werkzeug.http import parse_options_header

class FileProcessingResource(Resource):
  def post(self):
    start_time = time.time()
    data = request.get_json()
    url = data['url']

    # download the file
    r = requests.get(url)

    # get the filename from the Content-Disposition header
    _, params = parse_options_header(r.headers.get('Content-Disposition', ''))
    filename = params.get('filename', '')

    if filename.endswith('.zip'):
      # it's a ZIP file
      z = zipfile.ZipFile(io.BytesIO(r.content))

      # find the first CSV file in the ZIP
      csv_file = next((f for f in z.namelist() if f.endswith('.csv')), None)
      if csv_file:
        df = pd.read_csv(z.open(csv_file))

        # perform your analysis here...
        analysis = df.describe().to_dict()
      else:
        return {'error': 'No CSV file in the ZIP'}, 400

    elif filename.endswith('.csv'):
      # it's a CSV file
      df = pd.read_csv(io.StringIO(r.text))

      # perform your analysis here...
      analysis = df.describe().to_dict()

    else:
      return {'error': 'Unsupported file type'}, 400

    # return the analysis
    processing_time = time.time() - start_time
    return {
      'processing_time': processing_time,
      'analysis': analysis
    }