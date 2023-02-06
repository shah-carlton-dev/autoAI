import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './counter_slice';

export default configureStore({
  reducer: {
    counter: counterReducer,
  },
})