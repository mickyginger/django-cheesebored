import React from 'react'
import axios from 'axios'
import Auth from '../../lib/Auth'

class Edit extends React.Component {

  constructor() {
    super()
    this.state = {
      formData: {},
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/cheeses/${this.props.match.params.id}`)
      .then(res => this.setState({ formData: res.data }))
  }

  handleChange(e) {
    const formData = { ...this.state.formData, [e.target.name]: e.target.value }
    const errors = { ...this.state.errors, [e.target.name]: '' }
    this.setState({ formData, errors })
  }

  handleSubmit(e) {
    e.preventDefault()

    const token = Auth.getToken()
    const cheeseId = this.props.match.params.id

    axios.put(`/api/cheeses${cheeseId}`, this.state.formData, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push(`/cheeses/${cheeseId}`))
      .catch(err => this.setState({ errors: err.response.data }))
  }

  render() {
    return (
      <section className="section">
        <div className="container">
          <form onSubmit={this.handleSubmit}>
            <div className="field">
              <label className="label">Name</label>
              <div className="control">
                <input
                  className="input"
                  name="name"
                  placeholder="eg: Cheddar"
                  onChange={this.handleChange}
                  value={this.state.formData.name || ''}
                />
              </div>
              {this.state.errors.name && <small className="help is-danger">{this.state.errors.name}</small>}
            </div>
            <div className="field">
              <label className="label">Origin</label>
              <div className="control">
                <input
                  className="input"
                  name="origin"
                  placeholder="eg: England"
                  onChange={this.handleChange}
                  value={this.state.formData.origin || ''}
                />
              </div>
              {this.state.errors.origin && <small className="help is-danger">{this.state.errors.origin}</small>}
            </div>
            <div className="field">
              <label className="label">Image</label>
              <div className="control">
                <input
                  className="input"
                  name="image"
                  placeholder="eg: http://cheeseworld.co.uk/images/cheddar.png"
                  onChange={this.handleChange}
                  value={this.state.formData.image || ''}
                />
              </div>
              {this.state.errors.image && <small className="help is-danger">{this.state.errors.image}</small>}
            </div>
            <div className="field">
              <label className="label">Tasting notes</label>
              <div className="control">
                <textarea
                  className="textarea"
                  name="tasting_notes"
                  placeholder="eg: Sharp and tangy"
                  onChange={this.handleChange}
                  value={this.state.formData.tasting_notes || ''}
                />
              </div>
              {this.state.errors.tasting_notes && <small className="help is-danger">{this.state.errors.tasting_notes}</small>}
            </div>

            <button className="button is-primary">Submit</button>
          </form>
        </div>
      </section>
    )
  }
}

export default Edit
