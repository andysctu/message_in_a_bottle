react = require 'react'
Route = react.createFactory require 'react-router/lib/Route'
Router = react.createFactory require 'react-router/lib/Router'
Redirect = react.createFactory require 'react-router/lib/Redirect'
browserHistory = require 'react-router/lib/browserHistory'
Layout = require '../layout'


class Root extends react.Component

  render: ->
    Router history: browserHistory,
      Route path: '/', component: Layout


module.exports = Root
