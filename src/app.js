import React from 'react'
import ReactDOM from 'react-dom'

import { HashRouter, Route, Switch } from 'react-router-dom'
import { ToastContainer } from 'react-toastify'

import Navbar from './components/common/Navbar'
import SecureRoute from './components/common/SecureRoute'
import CheesesIndex from './components/cheeses/Index'
import CheesesShow from './components/cheeses/Show'
import CheesesNew from './components/cheeses/New'
import CheesesEdit from './components/cheeses/Edit'
import Register from './components/auth/Register'
import Login from './components/auth/Login'
import Home from './components/pages/Home'

import 'react-toastify/dist/ReactToastify.css'
import './style.scss'

class App extends React.Component {

  render() {
    return (
      <HashRouter>
        <Navbar />
        <ToastContainer />

        <Switch>
          <SecureRoute path="/cheeses/:id/edit" component={CheesesEdit} />
          <SecureRoute path="/cheeses/new" component={CheesesNew} />
          <Route path="/cheeses/:id" component={CheesesShow} />
          <Route path="/cheeses" component={CheesesIndex} />
          <Route path="/register" component={Register} />
          <Route path="/login" component={Login} />
          <Route path="/" component={Home} />
        </Switch>
      </HashRouter>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
