<script>
import API from '../api/index'
export default {
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    login(username, password) {
      console.log('username', this.username)
      console.log('password', this.password)
      API.login(this.username, this.password).then(function(response) {
        if (response.status == 200) {
          alert('Login success!')
        } else {
          alert('Login failed: ' + response.status)
        }
      })
    }
  },
}
</script>

<template>
  <section class="section">
      <div class="container mt-5">
        <div class="row">
          <div class="col-12 col-sm-8 offset-sm-2 col-md-6 offset-md-3 col-lg-6 offset-lg-3 col-xl-4 offset-xl-4">
            <div class="login-brand">
              <img src="/assets/img/putt.png" alt="logo" width="100">
            </div>

            <div class="card card-primary">
              <div class="card-header"><h4>Login</h4></div>

              <div class="card-body">
                <!-- <form method="POST" action="#" class="needs-validation" novalidate=""> -->
                  <div class="form-group">
                    <label for="email">Email</label>
                    <input id="email" type="email" v-model="username" class="form-control" name="email" tabindex="1" required autofocus>
                    <div class="invalid-feedback">
                      Please fill in your email
                    </div>
                  </div>

                  <div class="form-group">
                    <div class="d-block">
                    	<label for="password" class="control-label">Password</label>
                      <div class="float-right">
                        <a href="auth-forgot-password.html" class="text-small">
                          Forgot Password?
                        </a>
                      </div>
                    </div>
                    <input id="password" type="password" v-model="password" class="form-control" name="password" tabindex="2" required>
                    <div class="invalid-feedback">
                      please fill in your password
                    </div>
                  </div>

                  <div class="form-group">
                    <div class="custom-control custom-checkbox">
                      <input type="checkbox" name="remember" class="custom-control-input" tabindex="3" id="remember-me">
                      <label class="custom-control-label" for="remember-me">Remember Me</label>
                    </div>
                  </div>

                  <div class="form-group">
                    <button type="submit" @click="login" class="btn btn-primary btn-lg btn-block" tabindex="4">
                      Login
                    </button>
                  </div>
                <!-- </form> -->
              </div>
            </div>
            
            <div class="simple-footer">
              Copyright &copy; Putt Admin 2021 - 2022 (Version: v0.1)
            </div>
          </div>
        </div>
      </div>
    </section>
</template>
