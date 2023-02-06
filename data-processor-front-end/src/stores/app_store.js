import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './counter_slice';
import globalReducer from './global_slice';

export default configureStore({
  reducer: {
    counter: counterReducer,
    global: globalReducer
  },
})