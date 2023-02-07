import Layout from './components/Layout';
import Home from './components/pages/Home';
import ConfigureDataset from './components/pages/ConfigureDataset';
import UploadDataset from './components/pages/UploadDataset';
import ViewDataset from './components/pages/ViewDatasets';
import { Routes, Route } from "react-router-dom";
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { useSelector } from 'react-redux'
import React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import routes from './constants/routes';

function App() {
  const mode = useSelector((state) => state.global.themeMode);
  console.log(mode)
  const theme = React.useMemo(
    () =>
      createTheme({
        palette: {
          mode: mode,
        },
      }),
    [mode],
  );

  return (
    <ThemeProvider theme={theme}> 
      <CssBaseline enableColorScheme/>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path={routes.configureDataset} element={<ConfigureDataset />} />
          <Route path={routes.uploadDataset} element={<UploadDataset/>} />
          <Route path={routes.viewDataset} element={<ViewDataset/>} />
          {/* Using path="*"" means "match anything", so this route
                acts like a catch-all for URLs that we don't have explicit
                routes for. */}
          <Route path="*" element={<div>Not Found</div>} />
        </Route>
      </Routes> 
    </ThemeProvider>
  );
}

export default App;
