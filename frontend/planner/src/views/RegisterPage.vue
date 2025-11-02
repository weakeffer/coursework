<template>
    <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
        <div class="flex flex-col items-center">
            <div class="bg-white rounded-xl shadow-xl p-8 w-full min-w-xl border border-gray-100">
                <div class="text-center mb-4">
                    <h1 class="text-xl font-bold text-gray-400 mb-2">Kairos</h1>
                </div>
                <div class="text-center mb-8">
                    <h1 class="text-xl font-bold text-gray-800 mb-2">Регистрация</h1>
                    <p class="text-gray-600">Введите ваши данные для регистрации</p>
                </div>

                <div v-if="backendErrors.general" class="mb-4 p-3 bg-red-50 border border-red-200 rounded-lg">
                    <p class="text-red-600 text-sm">{{ backendErrors.general }}</p>
                </div>

                <form @submit.prevent="handleRegister" class="space-y-6">
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                        <input
                            v-model="email"
                            type="email"
                            placeholder="email@email.com"
                            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 outline-none"
                            required
                            @input="clearBackendErrors('email')">
                            <div v-if="backendErrors.email" class="text-red-500 text-sm mt-2">
                                {{ backendErrors.email }}
                            </div>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Имя</label>
                        <input
                            v-model="name"
                            type="text"
                            placeholder="Введите имя"
                            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 outline-none"
                            required
                            @input="clearBackendErrors('name')">
                            <div v-if="backendErrors.name" class="text-red-500 text-sm mt-2">
                            {{ backendErrors.name }}
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
                            @input="validatePassword(); clearBackendErrors('password')">
                            <div v-if="backendErrors.password" class="text-red-500 text-sm mt-2">
                            {{ backendErrors.password }}
                        </div>
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-gray-700 mb-2">Подтвердите пароль</label>
                        <input
                            v-model="confirmPassword"
                            type="password"
                            placeholder="Введите пароль еще раз"
                            class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 outline-none"
                            required
                            :class="{'border-red-500': passwordError}"
                            @input="validatePassword">
                        <div v-if="passwordError" class="text-red-500 text-sm mt-2">
                            {{ passwordError }}
                        </div>
                    </div>
                    <button 
                        class="w-full bg-gradient-to-r from-blue-400 to-blue-600 hover:from-blue-500 hover:to-blue-800 text-white font-semibold py-3 px-4 rounded-lg shadow-md hover:shadow-lg transition-all duration-200 transform hover:-translate-y-0.5 focus:ring-2 focus:ring-green-300 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
                        type="submit"
                        :disabled="!isFormValid">
                        <span v-if="isLoading">Загрузка...</span>
                        <span v-else>Зарегистрироваться</span>
                    </button>
                </form>
                <div class="mt-8 text-center text-xs text-gray-500 border-t border-gray-200 pt-4">
                    © 2025 Kairos
                </div>
            </div>
            <div class="p-6 w-full max-w-md text-center">
                    <span class="text-sm font-medium text-gray-700 mr-2">Уже есть аккаунт?</span>
                    <a href="/login" class="text-sm text-blue-600 hover:text-blue-800 font-medium transition-colors duration-200">
                        Войти
                    </a>
                </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'RegisterPage',
    data() {
        return {
            email: '',
            name: '',
            password: '',
            confirmPassword: '',
            passwordError: '',
            isLoading: false,
            backendErrors: {
                email: '',
                name: '',
                password: '',
                general: ''
            }
        }
    },
    computed: {
        isFormValid() {
            return this.email &&
                   this.name &&
                   this.password &&
                   this.confirmPassword &&
                   !this.passwordError &&
                   this.password === this.confirmPassword &&
                   !this.isLoading
        }
    },
    methods: {
        validatePassword() {
            if (this.password !== this.confirmPassword) {
                this.passwordError = 'Пароли не совпадают!'
            } else if (this.password.length < 8) {
                this.passwordError = 'Пароль должен содержать минимум 8 символов!'
            } else {
                this.passwordError = ''
            }
        },
        
        clearBackendErrors(field) {
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
                name: '',
                password: '',
                general: ''
            }
            this.passwordError = ''
        },

        async handleRegister() {
            if (!this.isFormValid) return;
            
            this.clearAllErrors();
            this.isLoading = true;
            
            try {
                const response = await axios.post('http://localhost:8000/api/auth/register/', {
                    email: this.email,
                    name: this.name,
                    password: this.password,
                }, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                
                if (response.data.success) {
                    this.clearForm();
                    this.$router.push('/login');
                } else {
                    this.handleBackendErrors(response.data.errors);
                }
            } catch(error) {
                console.error('Ошибка регистрации:', error);
                this.handleError(error);
            } finally {
                this.isLoading = false;
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
                
                if (responseData.errors) {
                    this.handleBackendErrors(responseData.errors);
                } else if (responseData.error) {
                    this.backendErrors.general = responseData.error;
                } else {
                    this.backendErrors.general = 'Произошла ошибка при регистрации!';
                }
            } else if (error.request) {
                this.backendErrors.general = 'Не удалось подключиться к серверу';
            } else {
                this.backendErrors.general = 'Ошибка: ' + error.message;
            }
        },
        
        clearForm() {
            this.email = ''
            this.name = ''
            this.password = ''
            this.confirmPassword = ''
            this.passwordError = ''
            this.clearAllErrors()
        }
    },
    watch: {
        password() {
            this.validatePassword()
        },
        confirmPassword() {
            this.validatePassword()
        }
    }
}
</script>