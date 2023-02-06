import Layout from './components/Layout';
import Home from './components/pages/Home';
import ConfigureDataset from './components/pages/ConfigureDataset';
import UploadDataset from './components/pages/UploadDataset';
import ViewDataset from './components/pages/ViewDatasets';
import { Routes, Route } from "react-router-dom";
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { useSelector } from 'react-redux'
import React from 'react';

function App() {
  const mode = useSelector((state) => state.global.themeMode);
  const theme = React.useMemo(
    () =>
      createTheme({
        palette: {
          mode,
        },
      }),
    [mode],
  );

  return (
    <ThemeProvider theme={theme}>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="configureDataset" element={<ConfigureDataset />} />
          <Route path="uploadDataset" element={<UploadDataset/>} />
          <Route path="viewDataset" element={<ViewDataset/>} />
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
