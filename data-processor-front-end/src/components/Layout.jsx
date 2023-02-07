import { Outlet, Link } from "react-router-dom";
import { useTheme } from '@mui/material/styles';
import { useDispatch } from 'react-redux';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';
import HomeIcon from '@mui/icons-material/Home';
import BuildIcon from '@mui/icons-material/Build';
import FormatListBulletedIcon from '@mui/icons-material/FormatListBulleted';
import UploadFileIcon from '@mui/icons-material/UploadFile';
import { toggleTheme } from '../stores/global_slice';
import Box from '@mui/material/Box';
import IconButton from '@mui/material/IconButton';
import routes from '../constants/routes';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Grid from '@mui/material/Unstable_Grid2';
import * as React from 'react';

function LinkTab(props) {
  return (
    <Tab
      component={Link}
      {...props}
    />
  );
}

const Layout = () => {
  const theme = useTheme();
  const dispatch = useDispatch();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Grid container spacing={2}>
      <Grid xs={11}>
        <Tabs value={value} onChange={handleChange}>
          <LinkTab icon={<HomeIcon/>} iconPosition='start' label={'Home'} to={routes.root}/>
          <LinkTab icon={<BuildIcon/>} iconPosition='start' label={'Configure Dataset'} to={routes.configureDataset}/>
          <LinkTab icon={<UploadFileIcon/>} iconPosition='start' label={'Upload Dataset'} to={routes.uploadDataset}/>
          <LinkTab icon={<FormatListBulletedIcon/>} iconPosition='start' label={'View Dataset'} to={routes.viewDataset}/>
        </Tabs>
      </Grid>
      <Grid xs={1} display="flex" justifyContent="center" alignItems="center">
        <IconButton sx={{ ml: 1 }} onClick={() => dispatch(toggleTheme())} color="inherit">
          {theme.palette.mode === 'dark' ? <Brightness7Icon /> : <Brightness4Icon />}
        </IconButton>
      </Grid>
      {/* An <Outlet> renders whatever child route is currently active,
        so you can think about this <Outlet> as a placeholder for
        the child routes we defined above. */}
      <Grid xs={12}>
        <Outlet />
      </Grid>
    </Grid>
  );
}

export default Layout;