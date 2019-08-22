import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import Auth from '../../lib/Auth'

class CheesesShow extends React.Component {
  constructor() {
    super()
    this.state = {}

    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/cheeses/${this.props.match.params.id}`)
      .then(res => this.setState({ cheese: res.data }))
  }

  handleDelete() {
    const token = Auth.getToken()

    axios.delete(`/api/cheeses${this.props.match.params.id}`, {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/cheeses'))
  }

  render() {
    if(!this.state.cheese) return null
    return (
      <section className="section">
        <div className="container">
          <h1 className="title is-2">{this.state.cheese.name}</h1>
          <h2 className="subtitle is-4">{this.state.cheese.origin}</h2>

          {Auth.isCurrentUser(this.state.cheese.user) &&
            <div className="buttons">
              <Link to={`/cheeses/${this.state.cheese.id}/edit`} className="button">Edit</Link>
              <button onClick={this.handleDelete} className="button is-danger">Delete</button>
            </div>
          }

          <hr />

          <div className="columns">
            <div className="column">
              <figure className="image">
                <img src={this.state.cheese.image} alt={this.state.cheese.name} />
              </figure>
            </div>
            <div className="column">
              <p>{this.state.cheese.tasting_notes}</p>
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default CheesesShow
