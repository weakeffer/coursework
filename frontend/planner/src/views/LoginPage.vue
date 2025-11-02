<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
    <div class="flex flex-col items-center">
    <div class="bg-white rounded-2xl shadow-xl p-8 w-full min-w-xl border border-gray-100">
       <div class="text-center mb-4">
        <h1 class="text-xl font-bold text-gray-400 mb-2">Kairos</h1>
      </div>
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-gray-800 mb-2">Вход в систему</h1>
        <p class="text-gray-600">Введите ваши данные для входа</p>
      </div>

      <div v-if="backendErrors.general" class="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg">
        <p class="text-red-600 text-sm">{{ backendErrors.general }}</p>
      </div>

      <form @submit.prevent="handleLogin" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Email</label>
          <input 
            v-model="email" 
            type="email" 
            placeholder="your@email.com" 
            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 outline-none"
            required
            @input = 'clearBackendError("email")'>
            <div v-if="backendErrors.email" class="text-red-500 text-sm mt-2">
              {{ backendErrors.email }}
            </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-2">Пароль</label>
          <input 
            v-model="password" 
            type="password" 
            placeholder="Введите пароль" 
            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 outline-none"
            required
            @input="clearBackendError('password')">
            <div v-if="backendErrors.password" class="text-red-500 text-sm mt-2">
              {{ backendErrors.password }}
            </div>
        </div>
        <button 
          class="w-full bg-gradient-to-r from-blue-400 to-blue-600 hover:from-blue-500 hover:to-blue-800 text-white font-semibold py-3 px-4 rounded-lg shadow-md hover:shadow-lg transition-all duration-200 transform hover:-translate-y-0.5 focus:ring-2 focus:ring-green-300 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
          type="submit"
          :disabled="!isFormValid || isLoading">
          <span v-if="isLoading">Вход</span>
          <span v-else>Войти</span>
        </button>
        <div class="text-center pt-4 border-t border-gray-200">
          <a href="#" class="text-sm text-blue-600 hover:text-blue-800 transition-colors duration-200">
            Забыли пароль?
          </a>
        </div>
      </form>
      <div class="mt-8 text-center text-xs text-gray-500">
        © 2025 Kairos
      </div>
    </div>
    <div class="text-center pt-4">
          <span class="text-sm font-medium text-gray-700 mr-2">Ещё нет аккаунта?</span>
          <a href="/register" class="text-sm text-blue-600 hover:text-blue-800 transition-colors duration-200">
            Зарегистрироваться
          </a>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default{
    name: 'LoginPage',
    data() {
        return{
            email: '',
            password: '',
            isLoading: false,
            backendErrors: {
              email: '',
              password: '',
              general: '',
            }
        }
    },
    methods: {
      clearBackendError(field) {
        if (this.backendErrors[field]) {
          this.backendErrors[field] = ''
        }
        if (this.backendErrors.general) {
          this.backendErrors.general = ''
        }
      },
        
      clearAllErrors() {
        this.backendErrors = {
          email: '',
          password: '',
          general: ''
        }
      },
      async handleLogin() {
        if (!this.isFormValid) return;
        this.clearAllErrors();
        this.isLoading = true
        try {
          const response = await axios.post('http://localhost:8000/api/auth/login/', {
            email: this.email,
            password: this.password,
          },{
            headers:{
              'Content-Type': 'application/json'
            }
          });

          if (response.data.success) {
            localStorage.setItem('access_token', response.data.tokens.access);
            localStorage.setItem('refresh_token', response.data.tokens.refresh);
            localStorage.setItem('user', JSON.stringify(response.data.user));
            this.$router.push('/app')
          } else {
            this.handleBackendErrors(response.data.errors);
          }
        } catch (error){
          console.error('Ошибка входа:', error);
          this.handleError(error);
        } finally{
          this.isLoading = false
        }
      },
      handleBackendErrors(errors) {
            if (typeof errors === 'object') {
                for (const [field, messages] of Object.entries(errors)) {
                    if (this.backendErrors.hasOwnProperty(field)) {
                        this.backendErrors[field] = Array.isArray(messages) ? messages[0] : messages;
                    } else {
                        this.backendErrors.general = Array.isArray(messages) ? messages.join(', ') : messages;
                    }
                }
            } else if (typeof errors === 'string') {
                this.backendErrors.general = errors; 
            }
        },
      handleError(error) {
        if (error.response) {
          const responseData = error.response.data;

          // Обработка ошибок валидации Django
          if (responseData.detail) {
            this.backendErrors.general = responseData.detail;
          }
          else if (typeof responseData === 'object') {
            let hasFieldErrors = false;

            for (const [field, messages] of Object.entries(responseData)) {
              if (this.backendErrors.hasOwnProperty(field)) {
                this.backendErrors[field] = Array.isArray(messages) ? messages[0] : messages;
                hasFieldErrors = true;
              }
            }
            if (!hasFieldErrors) {
              this.backendErrors.general = 'Произошла ошибка при входе!';
            }
          } else {
            this.backendErrors.general = 'Произошла ошибка при входе!';
          }
        } else if (error.request) {
          this.backendErrors.general = 'Не удалось подключиться к серверу';
        } else {
          this.backendErrors.general = 'Ошибка: ' + error.message;
        }
      }
    },
    computed: {
        isFormValid () {
          return this.email &&
          this.password &&
          !this.isLoading
      }
    },
}
</script>

<style scoped>
.login-page {
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
}
</style>