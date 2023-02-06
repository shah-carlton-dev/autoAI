import { Outlet, Link } from "react-router-dom";
import { useTheme } from '@mui/material/styles';
import { useDispatch } from 'react-redux';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';
import { toggleTheme } from '../stores/global_slice';
import Box from '@mui/material/Box';
import IconButton from '@mui/material/IconButton';

const Layout = () => {
  const theme = useTheme();
  const dispatch = useDispatch();

  return (
    <div>
      <Box
        sx={{
          display: 'flex',
          width: '100%',
          alignItems: 'center',
          justifyContent: 'center',
          bgcolor: 'background.default',
          color: 'text.primary',
          borderRadius: 1,
          p: 3,
        }}
      >
        {theme.palette.mode} mode
        <IconButton sx={{ ml: 1 }} onClick={() => dispatch(toggleTheme())} color="inherit">
            {theme.palette.mode === 'dark' ? <Brightness7Icon /> : <Brightness4Icon />}
        </IconButton>
      </Box>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/dashboard">Dashboard</Link>
          </li>
          <li>
            <Link to="/nothing-here">Nothing Here</Link>
          </li>
        </ul>
      </nav>

      <hr />

      {/* An <Outlet> renders whatever child route is currently active,
        so you can think about this <Outlet> as a placeholder for
        the child routes we defined above. */}
      <Outlet />
    </div>
  );
}

export default Layout;