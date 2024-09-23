import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import {QueryClient,QueryClientProvider} from '@tanstack/react-query'
const queryClient = new QueryClient()
import Cookies from 'js-cookie'
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import SignUp from './Components/Session/SignUpPage.jsx'
import { restoreCSRF,csrfFetch} from '../csurf.js'
import { ReactQueryDevtools } from '@tanstack/react-query-devtools'
import UserProfile from './Components/Session/UserProfile.jsx'
import { ChakraProvider } from '@chakra-ui/react'
import LogInPage from './Components/Session/LogInPage.jsx'

if (process.env.NODE_ENV !== "production") {
  restoreCSRF();

  window.csrfFetch = csrfFetch;
  // window.store = store;
}
console.log('this is cookie',Cookies.get())
const router = createBrowserRouter([
  {
    path:'/',
    element:<h1>Home Page</h1>
  },
  {
    path: "/signup",
    element: <SignUp/>
  },
  {
    path:"/login",
    element:<LogInPage/>
  },
  {
    path:"/profile",
    element:<UserProfile/>
  }
]);
createRoot(document.getElementById('root')).render(

  <StrictMode>
    <QueryClientProvider client = {queryClient}>
      <ReactQueryDevtools initialIsOpen={false} />
      <RouterProvider router = {router}>
        <ChakraProvider>
          <App />
        </ChakraProvider>
      </RouterProvider>
    </QueryClientProvider>
  </StrictMode>,
)
