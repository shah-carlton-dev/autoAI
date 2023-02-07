import Grid from '@mui/material/Unstable_Grid2';
import Typography from '@mui/material/Typography';
import React, { useState } from 'react';
import { FilePond, registerPlugin } from 'react-filepond';
import { useSelector, useDispatch } from 'react-redux';
import { setFiles } from '../../stores/global_slice';
import TextField from '@mui/material/TextField';
import FilePondPluginGetFile from 'filepond-plugin-get-file';
import FilePondPluginFileEncode from 'filepond-plugin-file-encode';
import '../../styles/uploadDataset.css';
import 'filepond/dist/filepond.min.css';
import 'filepond-plugin-get-file/dist/filepond-plugin-get-file.min.css';

registerPlugin(FilePondPluginGetFile, FilePondPluginFileEncode)

const UploadDataset = () => {
  // const [files, setFiles] = useState([]);
  const files = useSelector((state) => state.global.files); 
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('');
  
  return (
    <Grid container spacing={2}>
      <Grid xs={3}/>
      <Grid xs={6}>
        <Grid container spacing={2}>
          <Grid xs={12}>
            <Typography variant="body1" gutterBottom>
              Fill out this form to begin the upload of your dataset. The <b>File Title</b> and 
              <b> File Description</b> fields must be filled out before a file can be uploaded, and the 
              file uploaded must be a csv file. 
            </Typography>
          </Grid>
          <Grid xs={12}>
            <TextField 
              label="File Title" 
              variant="outlined"
              className='titleField'
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
          </Grid>
          <Grid xs={12}>
            <TextField 
              fullWidth
              label="File Description" 
              variant="outlined"
              value={desc}
              onChange={(e) => setDesc(e.target.value)}
            />
          </Grid>
          <Grid xs={12}>
            <FilePond
              files={files}
              onupdatefiles={setFiles}
              allowMultiple={true}
              maxFiles={1}
              server="/api/files/upload"
              name="filepond"
              instantUpload={false}
              labelIdle='Drag & Drop your file or <span class="filepond--label-action">Browse</span>'
              credits={false}
              disabled={!(title && desc)}
            />
          </Grid>
        </Grid>
      </Grid>
      <Grid xs={3}/>
    </Grid>
  );
}

export default UploadDataset;