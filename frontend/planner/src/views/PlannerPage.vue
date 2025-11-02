<template>
    <div class="min-h-screen bg-gray-50">
        <!-- Хедер -->
        <Header />

        <!--Кнопка ассистента-->
        <div class="fixed bottom-6 right-6 z-40">
            <button 
                @click="toggleAIChat"
                class="w-16 h-16 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full shadow-lg hover:shadow-xl transform hover:scale-110 transition-all duration-300 flex items-center justify-center"
            >
                <span class="text-2xl">🤖</span>
            </button>
            
            <!-- окно помощника -->
            <div v-if="showAIChat" class="absolute bottom-16 right-0 w-94 bg-white rounded-2xl shadow-2xl border border-gray-200">
                <div class="p-4 border-b border-gray-200">
                    <div class="flex items-center space-x-3">
                        <div class="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center">
                            <span class="text-white text-lg">🤖</span>
                        </div>
                        <div>
                            <h3 class="font-semibold text-gray-900">AI Помощник</h3>
                            <p class="text-sm text-gray-500">Готов помочь с задачами</p>
                        </div>
                    </div>
                </div>
                
                <div class="p-4 max-h-60 overflow-y-auto">
                    <div class="space-y-3">
                        <div class="bg-blue-50 text-gray-700 rounded-lg p-3 text-sm">
                            <p>Привет! Я помогу проанализировать ваши задачи и найти оптимальное расписание</p>
                        </div>
                    </div>
                </div>
                
                <div class="p-4 border-t border-gray-200">
                    <div class="grid grid-cols-2 gap-2 mb-3">
                        <button @click="quickAction('analyze')" class="w-full px-3 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg text-sm transition-colors duration-200 text-gray-700">
                            📊 Анализ недели
                        </button>
                        <button @click="quickAction('priorities')" class="w-full px-3 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg text-sm transition-colors duration-200 text-gray-700">
                            🎯 Приоритеты
                        </button>
                    </div>
                    <div class="flex space-x-2">
                        <input 
                            v-model="aiMessage" 
                            @keyup.enter="sendAIMessage"
                            placeholder="Спросите у AI..."
                            class="flex-1 px-3 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                        >
                        <button @click="sendAIMessage" class="px-3 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">
                            ➤
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!--Вся страница-->
        <div class="pt-20 px-4 max-w-7xl mx-auto">
            <div class="flex flex-col lg:flex-row gap-8">
                <!-- Боковая панель -->
                <div class="lg:w-1/4 space-y-6">
                    <!-- карточка пользователя -->
                    <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
                        <a href="/profile" class="flex items-center space-x-4 p-2 rounded-lg hover:bg-gray-100 transition-colors duration-200">
                            <img src="@/assets/avatar.jpg" 
                                 alt="Аватар" 
                                 class="w-12 h-12 rounded-full object-cover border-2 border-blue-500">
                            <div>
                                <h3 class="font-semibold text-gray-900">Имя пользователя</h3>
                                <p class="text-sm text-gray-500">Почта пользователя</p>
                            </div>
                        </a>
                        
                        <!-- ежедневная статистика -->
                        <div class="mt-6 space-y-3">
                            <div class="flex justify-between text-sm">
                                <span class="text-gray-600">Задачи сегодня:</span>
                                <span class="font-semibold">5/8</span>
                            </div>
                            <div class="w-full bg-gray-200 rounded-full h-2">
                                <div class="bg-green-500 h-2 rounded-full" style="width: 62%"></div>
                            </div>
                        </div>
                    </div>

                    <!-- карточка быстрого доступа -->
                    <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
                        <h3 class="font-semibold text-gray-900 mb-4">Быстрые действия</h3>
                        <div class="space-y-2">
                            <button class="w-full flex items-center space-x-3 p-3 text-left rounded-lg hover:bg-blue-50 transition-colors duration-200">
                                <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                                </svg>
                                <span>Новая задача</span>
                            </button>
                            <button class="w-full flex items-center space-x-3 p-3 text-left rounded-lg hover:bg-green-50 transition-colors duration-200">
                                <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                                </svg>
                                <span>Создать проект</span>
                            </button>
                            <button @click="toggleAIChat" class="w-full flex items-center space-x-3 p-3 text-left rounded-lg hover:bg-purple-50 transition-colors duration-200">
                                <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                                </svg>
                                <span>AI Анализ</span>
                            </button>
                        </div>
                    </div>

                    <!-- проекты -->
                    <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="font-semibold text-gray-900">Проекты</h3>
                            <button class="text-blue-600 hover:text-blue-800 rounded-full hover:bg-green-100 transition-colors duration-200">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                                </svg>
                            </button>
                        </div>
                        <div class="space-y-2">
                            <div class="flex items-center space-x-3 p-2 rounded-lg hover:bg-gray-50 cursor-pointer">
                                <div class="w-3 h-3 bg-blue-500 rounded-full"></div>
                                <span class="text-sm">Дипломный проект</span>
                            </div>
                            <div class="flex items-center space-x-3 p-2 rounded-lg hover:bg-gray-50 cursor-pointer">
                                <div class="w-3 h-3 bg-green-500 rounded-full"></div>
                                <span class="text-sm">Рабочие задачи</span>
                            </div>
                            <div class="flex items-center space-x-3 p-2 rounded-lg hover:bg-gray-50 cursor-pointer">
                                <div class="w-3 h-3 bg-purple-500 rounded-full"></div>
                                <span class="text-sm">Личные цели</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- задачи и все основное -->
                <div class="lg:w-3/4 space-y-8">
                    <!-- окно приветствия -->
                    <div class="bg-gradient-to-r from-blue-500 to-purple-600 rounded-2xl p-6 text-white">
                        <h1 class="text-2xl font-bold mb-2">Добро пожаловать, имя пользователя! 👋</h1>
                        <p class="opacity-90">У вас запланировано 5 задач на сегодня. Давайте сделаем этот день продуктивным!</p>
                    </div>

                    <!-- задачи -->
                    <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
                        <div class="flex items-center justify-between mb-6">
                            <h2 class="text-xl font-bold text-gray-900">Сегодняшние задачи</h2>
                            <div class="flex space-x-2">
                                <button class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 transition-colors">
                                    Все
                                </button>
                                <button class="px-4 py-2 text-sm font-medium text-gray-600 rounded-lg hover:bg-gray-100 transition-colors">
                                    Активные
                                </button>
                                <button class="px-4 py-2 text-sm font-medium text-gray-600 rounded-lg hover:bg-gray-100 transition-colors">
                                    Завершенные
                                </button>
                            </div>
                        </div>
                        <div class="space-y-4">
                            <div class="flex items-center space-x-4 p-4 border border-gray-200 rounded-xl hover:shadow-md transition-all duration-200">
                                <button class="w-6 h-6 border-2 border-blue-500 rounded-full hover:bg-blue-100 transition-colors flex items-center justify-center">
                                    <svg v-if="false" class="w-4 h-4 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                                    </svg>
                                </button>
                                <div class="flex-1">
                                    <h4 class="font-semibold text-gray-900">Завершить дипломный проект</h4>
                                    <p class="text-sm text-gray-600 mt-1">Разработать главную страницу и настроить API</p>
                                    <div class="flex items-center space-x-4 mt-2">
                                        <span class="inline-flex items-center px-2 py-1 bg-blue-100 text-blue-700 rounded-full text-xs">
                                            <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                                            </svg>
                                            Сегодня
                                        </span>
                                        <span class="inline-flex items-center px-2 py-1 bg-purple-100 text-purple-700 rounded-full text-xs">
                                            Высокий приоритет
                                        </span>
                                    </div>
                                </div>
                                <button class="p-2 text-gray-400 hover:text-gray-600 transition-colors">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"/>
                                    </svg>
                                </button>
                            </div>
                        </div>
                        <button class="w-full mt-6 flex items-center justify-center space-x-2 p-4 border-2 border-dashed border-gray-300 rounded-xl text-gray-500 hover:border-blue-500 hover:text-blue-500 transition-all duration-200">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"/>
                            </svg>
                            <span>Добавить задачу</span>
                        </button>
                    </div>
                    <!--календарь-->
                    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
                            <div class="flex items-center justify-between mb-6">
                                <h3 class="font-semibold text-gray-900">Календарь</h3>
                                <div class="flex items-center space-x-2">
                                    <button @click="prevMonth" class="p-2 hover:bg-gray-100 rounded-lg">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
                                        </svg>
                                    </button>
                                    <span class="text-sm font-medium text-gray-700">{{ currentMonth }}</span>
                                    <button @click="nextMonth" class="p-2 hover:bg-gray-100 rounded-lg">
                                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                            <div class="w-full">
                                <div v-if="selectedDate" class="mt-4 p-3 bg-blue-50 rounded-lg">
                                    <h4 class="font-semibold text-blue-900 mb-1">
                                        {{ selectedDate.fullDate }}
                                    </h4>
                                    <p class="text-sm text-blue-700">
                                        {{ selectedDate.taskCount }} задач запланировано
                                    </p>
                                </div>
                                <div class="grid grid-cols-7 gap-1 mb-2">
                                    <div v-for="day in weekDays" :key="day" class="text-center text-xs font-medium text-gray-500 py-2">
                                        {{ day }}
                                    </div>
                                </div>
                                <div class="grid grid-cols-7 gap-1">
                                    <div 
                                        v-for="day in calendarDays" 
                                        :key="day.date"
                                        :class="[
                                            'aspect-square p-1 rounded-lg cursor-pointer hover:bg-gray-100 transition-colors duration-200 flex flex-col items-center justify-center text-sm relative',
                                            day.isCurrentMonth ? 'text-gray-900' : 'text-gray-400',
                                            day.isToday ? 'bg-blue-500 text-white' : '',
                                            day.hasTasks ? 'border-2 border-green-400' : ''
                                        ]"
                                        @click="selectDate(day)"
                                    >
                                        <span class="font-medium">{{ day.number }}</span>
                                        <div v-if="day.hasTasks" class="flex space-x-1 mt-1">
                                            <div class="w-1 h-1 bg-green-500 rounded-full"></div>
                                            <div v-if="day.taskCount > 1" class="w-1 h-1 bg-blue-500 rounded-full"></div>
                                            <div v-if="day.taskCount > 2" class="w-1 h-1 bg-purple-500 rounded-full"></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--карточка состояния задач на день-->
                        <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-6">
                            <h3 class="font-semibold text-gray-900 mb-4">Продуктивность</h3>
                            <div class="space-y-4">
                                <div>
                                    <div class="flex justify-between text-sm mb-1">
                                        <span>Завершено задач на этой неделе</span>
                                        <span>10/20</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-green-500 h-2 rounded-full" style="width: 60%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-sm mb-1">
                                        <span>Время фокусировки</span>
                                        <span>8.5ч</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-blue-500 h-2 rounded-full" style="width: 70%"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Header from '@/components/Header.vue';

export default {
    name: 'PlannerPage',
    components: {
        Header
    },
    data() {
        return {
            showAIChat: false,
            aiMessage: '',
            currentDate: new Date(),
            selectedDate: null,
            weekDays: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
        }
    },
    computed: {
        currentMonth() {
            return this.currentDate.toLocaleDateString('ru-RU', { 
                month: 'long', 
                year: 'numeric' 
            });
        },
        calendarDays() {
            const year = this.currentDate.getFullYear();
            const month = this.currentDate.getMonth();
            
            // Первый день месяца
            const firstDay = new Date(year, month, 1);
            // Последний день месяца
            const lastDay = new Date(year, month + 1, 0);
            // Первый день календаря (может быть из предыдущего месяца)
            const startDate = new Date(firstDay);
            startDate.setDate(startDate.getDate() - firstDay.getDay() + 1);
            
            const days = [];
            const today = new Date();
            
            for (let i = 0; i < 42; i++) {
                const date = new Date(startDate);
                date.setDate(startDate.getDate() + i);
                
                const isToday = date.toDateString() === today.toDateString();
                const isCurrentMonth = date.getMonth() === month;
                
                // Случайные задачи для демонстрации
                const hasTasks = Math.random() > 0.7;
                const taskCount = hasTasks ? Math.floor(Math.random() * 3) + 1 : 0;
                
                days.push({
                    date: date.toISOString(),
                    number: date.getDate(),
                    fullDate: date.toLocaleDateString('ru-RU'),
                    isCurrentMonth,
                    isToday,
                    hasTasks,
                    taskCount
                });
            }
            
            return days;
        }
    },
    methods: {
        toggleAIChat() {
            this.showAIChat = !this.showAIChat;
        },
        quickAction(action) {
            const messages = {
                analyze: "🤖 Анализирую вашу неделю... На основе ваших данных вижу, что наиболее продуктивные дни - вторник и четверг. Рекомендую планировать сложные задачи на эти дни.",
                priorities: "🎯 Проанализировав ваши задачи, рекомендую приоритеты: 1) Дипломный проект (срочно) 2) Подготовка презентации 3) Рабочие задачи"
            };
            
            // Здесь будет вызов AI API
            console.log(`AI Action: ${action}`);
            alert(messages[action]);
        },
        sendAIMessage() {
            if (this.aiMessage.trim()) {
                // Здесь будет вызов AI API
                console.log('AI Message:', this.aiMessage);
                this.aiMessage = '';
            }
        },
        prevMonth() {
            this.currentDate = new Date(
                this.currentDate.getFullYear(),
                this.currentDate.getMonth() - 1,
                1
            );
        },
        nextMonth() {
            this.currentDate = new Date(
                this.currentDate.getFullYear(),
                this.currentDate.getMonth() + 1,
                1
            );
        },
        selectDate(day) {
            this.selectedDate = day;
        }
    }
}
</script>