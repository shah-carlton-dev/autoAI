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
          server="/api"
          name="files" /* sets the file input name, it's filepond by default */
          labelIdle='Drag & Drop your files or <span class="filepond--label-action">Browse</span>'
        />
      </Grid>
      <Grid xs={3}/>
    </Grid>
  );
}

export default UploadDataset;