import React, { Component } from 'react'
import {Table,Button,Form} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import './HomePage.css'

export class HomePage extends Component {
    constructor(props){
        super(props);
            this.state = {
                ProjectName: '',
                Description:'',
                State:'',
                Category:'',
                SubCategory:'',
                Month:'',
                Day:'',
                Hour:'',
                Goal:''



            };



 



    };


    ProjectNameChange = (event) =>{
        this.setState({
            ProjectName:event.target.value
         



        })
    }

    DescriptionChange = (event) =>{
        this.setState({
            Description:event.target.value
         



        })
    }


    ChangeState = (event) =>{
        this.setState({
            State:event.target.value
         



        })
    }

    ChangeCategory = (event) =>{
        this.setState({
            Category:event.target.value
         



        })
    }

    ChangSubCategory = (event) =>{
        this.setState({
            SubCategory:event.target.value
         



        })
    }


    ChangeMonth = (event) =>{
        this.setState({
            Month:event.target.value
         



        })
    }


    ChangeDay = (event) =>{
        this.setState({
            Day:event.target.value
         



        })
    }


    ChangeHour = (event) =>{
        this.setState({
            Hour:event.target.value
         



        })
    }


    ChangeGoal = (event) =>{
        this.setState({
            Goal:event.target.value
         



        })
    }







    render() {
        return (
            <div>
                <h1 style = {{'text-align':'center','color':'rgb(35, 214, 35)'}}>Kickstarter Classifier </h1>

            <form>

                <Table size = "lg" variant = "light" bordered striped>
                    <tbody style = {{'text-align':'center'}}>

                        
                    <tr><td>
                        <label for="pet-select">Choose State: </label><select onChange = {this.ChangeState} >
                        <option value="AL">Alabama</option>
                        <option value="AK">Alaska</option>
                        <option value="AZ">Arizona</option>
                        <option value="AR">Arkansas</option>
                        <option value="CA">California</option>
                        <option value="CO">Colorado</option>
                        <option value="CT">Connecticut</option>
                        <option value="DE">Delaware</option>
                        <option value="DC">District Of Columbia</option>
                        <option value="FL">Florida</option>
                        <option value="GA">Georgia</option>
                        <option value="HI">Hawaii</option>
                        <option value="ID">Idaho</option>
                        <option value="IL">Illinois</option>
                        <option value="IN">Indiana</option>
                        <option value="IA">Iowa</option>
                        <option value="KS">Kansas</option>
                        <option value="KY">Kentucky</option>
                        <option value="LA">Louisiana</option>
                        <option value="ME">Maine</option>
                        <option value="MD">Maryland</option>
                        <option value="MA">Massachusetts</option>
                        <option value="MI">Michigan</option>
                        <option value="MN">Minnesota</option>
                        <option value="MS">Mississippi</option>
                        <option value="MO">Missouri</option>
                        <option value="MT">Montana</option>
                        <option value="NE">Nebraska</option>
                        <option value="NV">Nevada</option>
                        <option value="NH">New Hampshire</option>
                        <option value="NJ">New Jersey</option>
                        <option value="NM">New Mexico</option>
                        <option value="NY">New York</option>
                        <option value="NC">North Carolina</option>
                        <option value="ND">North Dakota</option>
                        <option value="OH">Ohio</option>
                        <option value="OK">Oklahoma</option>
                        <option value="OR">Oregon</option>
                        <option value="PA">Pennsylvania</option>
                        <option value="RI">Rhode Island</option>
                        <option value="SC">South Carolina</option>
                        <option value="SD">South Dakota</option>
                        <option value="TN">Tennessee</option>
                        <option value="TX">Texas</option>
                        <option value="UT">Utah</option>
                        <option value="VT">Vermont</option>
                        <option value="VA">Virginia</option>
                        <option value="WA">Washington</option>
                        <option value="WV">West Virginia</option>
                        <option value="WI">Wisconsin</option>
                        <option value="WY">Wyoming</option>
                        </select>			
                        </td>
                        </tr>
                        <tr><td><input id = "RegForm" placeholder = "Project Name" onChange = {this.ProjectNameChange}/> </td></tr>

                        <tr><td><input id = "RegForm" placeholder = "Description" onChange = {this.DescriptionChange} /> </td></tr>


                        <tr><td><input id = "RegForm" placeholder = "Category" onChange = {this.ChangeCategory}/> </td></tr>

                        <tr><td><input id = "RegForm" placeholder = "SubCategory" onChange = {this.ChangeSubCategory}/> </td></tr>

                        <tr><td><input id = "RegForm" placeholder = "Goal" onChange = {this.ChangeGoal}/> </td></tr>

                        <tr><td><input id = "RegForm3" placeholder = "Month" onChange = {this.ChangeMonth} /><input id = "RegForm3" placeholder = "Day" onChange = {this.ChangeDay} /><input id = "RegForm3" placeholder = "Hour" onChange = {this.ChangeHour} /> </td></tr>

                        <tr><td><Button variant = "success" >Run Prediction</Button> </td></tr>
           
                    </tbody>
                </Table>

            
            </form>
            
            </div>
        )
    }
}

export default HomePage









