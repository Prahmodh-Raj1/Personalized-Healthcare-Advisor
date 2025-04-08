import React from 'react'
import Advisor from './Advisor'

describe('<Advisor />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<Advisor />)
  })
})