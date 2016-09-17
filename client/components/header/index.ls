require './index.styl'
react = require 'react'
{div} = react.DOM


class Header extends react.Component

  render: ->
    div className: 'c-header',
      div className: 'name', 'Here Comes a Thought'


module.exports = Header
