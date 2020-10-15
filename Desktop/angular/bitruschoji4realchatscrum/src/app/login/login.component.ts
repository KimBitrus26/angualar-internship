import { Component, OnInit } from '@angular/core';
import { ScrumdataService } from '../scrumdata.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  
  scrumUserLoginData = {
    'email': '',
    'password' : '',
    'projname' :''
  }

  constructor(private _scrumdataService: ScrumdataService) { }

  ngOnInit(): void {
  }
  

  onLoginSubmit(){
    console.log(this.scrumUserLoginData)
      this._scrumdataService.login(this.scrumUserLoginData).subscribe(
        data => console.log('Success', data),
        error => console.log('Error', error)
      );
      
  }
 

}
