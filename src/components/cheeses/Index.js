import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

import Card from './Card'

class CheesesIndex extends React.Component {
  constructor() {
    super()

    this.state = { cheeses: [] }
  }

  componentDidMount() {
    axios.get('/api/cheeses/')
      .then(res => this.setState({ cheeses: res.data }))
  }

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-multiline">
            {this.state.cheeses.map(cheese =>
              <div
                key={cheese.id}
                className="column is-half-tablet is-one-quarter-desktop"
              >
                <Link to={`/cheeses/${cheese.id}`}>
                  <Card name={cheese.name} image={cheese.image} />
                </Link>
              </div>
            )}
          </div>
        </div>
      </section>
    )
  }
}

export default CheesesIndex
