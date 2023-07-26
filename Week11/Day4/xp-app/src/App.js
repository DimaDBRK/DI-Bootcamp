
import './App.css';
import React from "react";
import  ErrorBoundary  from "./components/ErrorBoundary";
import PostList from './components/PostList';
import {BrowserRouter, Routes, Route, NavLink, Link} from "react-router-dom";
import Example1 from './components/Example1';
import Example2 from './components/Example2';
import Example3 from './components/Example3';
import ServerRequests from './components/ServerRequests';
import HeaderRequest from './components/HeaderRequest';

const HomeScreen = () => {
  return(
    <h1>Home screen</h1>
  )
}

const ProfileScreen = () => {
  return(
    <h1>Profile screen</h1>
  )
}

const ShopScreen = () => {
    throw new Error("Test err.");
}

const routes = (
  <Routes>
    <Route path="/" element={<HomeScreen />}></Route>
    <Route path="/shop" element={<ShopScreen />}></Route>
    <Route path="/profile" element={<ProfileScreen />}></Route>
  </Routes>

)


function MyNavbar() {
  // throw new Error("Test err.");
  return (
    <>
    <h1>Test</h1>
    <p>
      <NavLink to="/">Home</NavLink>
    </p>
    <p>
      <NavLink to="/profile">Profile</NavLink>
    </p>
    <p>
      <NavLink to="/shop">Shop</NavLink>
    </p>

  
    </>
  )
}


// Ex4
const TestHook = () => {
  const hookLink = "https://webhook.site/bb13098f-1a08-43fe-bc41-ea3f0f0d002b";
  const info = {
    key1: 'myusername',
    email: 'mymail@gmail.com',
    name: 'Isaac',
    lastname: 'Doe',
    age: 27
  }

  const webHookTEst = async () => {
    try {
      const res = await fetch(hookLink, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(info)
      });
      // const data = await res.json();
      console.log(res.status);
      console.log(res);
    } catch (e) {
      console.log(e);
    }
  }

  return (
    <button onClick={webHookTEst}>POST data</button>
  )
}

function App() {
  return (
    <>
    <h1>Ex1</h1>
    <ErrorBoundary>
      <BrowserRouter>
        <MyNavbar/>
        <ErrorBoundary>
          { routes }
        </ErrorBoundary>
      </BrowserRouter>
    </ErrorBoundary>

    <h1>Ex2</h1>
    <PostList/>

    <h1>Ex3</h1>
    <Example1/>
    <Example2/>
    <Example3/>
    <h1>Ex4</h1>
    <TestHook/>
    <h1>Daily Challenge</h1>
    <HeaderRequest />
    <ServerRequests />
  
    </>

  );
}

export default App;
