import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter } from "react-router-dom";
import { Provider } from 'react-redux';
import { StyledEngineProvider } from '@mui/material/styles';
// import './styles/index.css';
import App from './App';
import store from './stores/app_store';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    {/* <StyledEngineProvider injectFirst> */}
      <BrowserRouter>
        <Provider store={store}>
          <App />
        </Provider>
      </BrowserRouter>
    {/* </StyledEngineProvider> */}
  </React.StrictMode>
);