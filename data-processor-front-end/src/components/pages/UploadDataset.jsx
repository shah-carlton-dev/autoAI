import Grid from '@mui/material/Unstable_Grid2';
import React, { useState } from 'react';
import { FilePond, registerPlugin } from 'react-filepond';
import FilePondPluginGetFile from 'filepond-plugin-get-file';
import FilePondPluginFileEncode from 'filepond-plugin-file-encode';
import 'filepond/dist/filepond.min.css';
import 'filepond-plugin-get-file/dist/filepond-plugin-get-file.min.css';

registerPlugin(FilePondPluginGetFile, FilePondPluginFileEncode)

const UploadDataset = () => {
  const [files, setFiles] = useState([])
  
  return (
    <Grid container spacing={2}>
      <Grid xs={3}/>
      <Grid xs={6}>
        <FilePond
          files={files}
          onupdatefiles={setFiles}
          allowMultiple={true}
          maxFiles={3}
          server="/api/files/upload"
          name="filepond"
          labelIdle='Drag & Drop your files or <span class="filepond--label-action">Browse</span>'
          credits={false}
        />
        {/* <button onClick={(e) => {
          fetch('/api/files/getAll')
          .then(response => {
              // handle the response
              console.log(response)
          })
          .catch(error => {
              // handle the error
              console.log(error)
          });
        }}></button> */}
      </Grid>
      <Grid xs={3}/>
    </Grid>
  );
}

export default UploadDataset;