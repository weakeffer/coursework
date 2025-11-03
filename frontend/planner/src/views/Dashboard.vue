<template>
    <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-indigo-100">
        <!-- хедер -->
        <header class="fixed top-0 left-0 right-0 z-50 bg-white/80 backdrop-blur-md border-b border-gray-200">
            <div class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
                <div class="flex items-center space-x-2">
                    <h1 class="text-xl font-bold text-gray-400">Kairos</h1>
                </div>
                <div class="flex items-center space-x-4">
                    <a href="/login" class="text-gray-600 hover:text-gray-900 transition-colors duration-200">
                        Вход
                    </a>
                    <a href="/register" 
                       class="bg-gradient-to-r from-blue-500 to-purple-600 text-white px-6 py-2 rounded-lg font-semibold hover:shadow-lg transition-all duration-200 transform hover:-translate-y-0.5">
                        Начать
                    </a>
                </div>
            </div>
        </header>

        <div class="pt-32 pb-16 px-4">
            <div class="max-w-7xl mx-auto">
                <!-- главная -->
                <div class="flex flex-col lg:flex-row items-center justify-between gap-12">
                    <!-- лево -->
                    <div class="flex-1 text-left space-y-8">
                        <div class="space-y-4">
                            <h1 class="text-5xl lg:text-6xl font-bold text-gray-900 leading-tight">
                                Организуйте свое время
                                <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">
                                    с умом
                                </span>
                            </h1>
                            <p class="text-xl text-gray-600 max-w-2xl leading-relaxed">
                                Kairos помогает эффективно управлять задачами, устанавливать приоритеты 
                                и достигать большего каждый день. Просто, интуитивно и мощно.
                            </p>
                        </div>

                        <!-- фишки -->
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 py-6">
                            <div class="flex items-start space-x-3 p-4 rounded-lg hover:bg-white hover:shadow-md transition-all duration-300">
                                <div class="flex-shrink-0 w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                                    <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                                    </svg>
                                </div>
                                <div>
                                    <h3 class="font-semibold text-gray-900">Планирование</h3>
                                    <p class="text-gray-600 text-sm mt-1">Автоматическая сортировка задач по приоритетам</p>
                                </div>
                            </div>

                            <div class="flex items-start space-x-3 p-4 rounded-lg hover:bg-white hover:shadow-md transition-all duration-300">
                                <div class="flex-shrink-0 w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
                                    <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                                    </svg>
                                </div>
                                <div>
                                    <h3 class="font-semibold text-gray-900">Внедрение AI</h3>
                                    <p class="text-gray-600 text-sm mt-1">Помощь AI в планировании</p>
                                </div>
                            </div>

                            <div class="flex items-start space-x-3 p-4 rounded-lg hover:bg-white hover:shadow-md transition-all duration-300">
                                <div class="flex-shrink-0 w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                                    <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                                    </svg>
                                </div>
                                <div>
                                    <h3 class="font-semibold text-gray-900">Детальная аналитика</h3>
                                    <p class="text-gray-600 text-sm mt-1">Отслеживайте прогресс и продуктивность</p>
                                </div>
                            </div>
                        </div>

                        <!-- кнопки -->
                        <div class="flex flex-col sm:flex-row gap-4 pt-6">
                            <a href="/register" 
                               class="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-white bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 hover:from-blue-700 hover:to-purple-700">
                                Начать бесплатно
                                <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"/>
                                </svg>
                            </a>
                            <a href="/login" 
                               class="inline-flex items-center justify-center px-8 py-4 text-lg font-semibold text-gray-700 bg-white border border-gray-300 rounded-xl shadow-lg hover:shadow-xl transform hover:-translate-y-1 transition-all duration-300 hover:bg-gray-50">
                                Войти в аккаунт
                            </a>
                        </div>
                    </div>

                    <!-- право -->
                    <div class="flex-1 relative">
                        <div class="relative max-w-lg mx-auto">
                            <!-- карточка -->
                            <div class="bg-white rounded-2xl shadow-2xl p-6 border border-gray-200 transform rotate-2 hover:rotate-0 transition-transform duration-500">
                                <div class="flex items-center justify-between mb-6">
                                    <h3 class="font-bold text-gray-900">Сегодняшние задачи</h3>
                                    <span class="text-sm text-blue-600 font-semibold">3 из 5 завершено</span>
                                </div>
                                
                                <!-- задачи тут типо круто  -->
                                <div class="space-y-3">
                                    <div class="flex items-center gap-3 p-3 bg-green-50 rounded-lg border border-green-200">
                                        <div class="w-6 h-6 bg-green-500 rounded-full flex items-center justify-center">
                                            <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                                            </svg>
                                        </div>
                                        <span class="text-gray-700 line-through">Решить математику</span>
                                    </div>
                                    
                                    <div class="flex items-center gap-3 p-3 bg-blue-50 rounded-lg border border-blue-200">
                                        <div class="w-6 h-6 border-2 border-blue-500 rounded-full"></div>
                                        <span class="text-gray-700 font-medium">Купить продукты</span>
                                    </div>
                                    
                                    <div class="flex items-center gap-3 p-3 bg-gray-50 rounded-lg border border-gray-200">
                                        <div class="w-6 h-6 border-2 border-gray-400 rounded-full"></div>
                                        <span class="text-gray-500">Подготовить презентацию</span>
                                    </div>
                                </div>
                                
                                <!-- прогресс -->
                                <div class="mt-6">
                                    <div class="flex justify-between text-sm text-gray-600 mb-2">
                                        <span>Прогресс дня</span>
                                        <span>60%</span>
                                    </div>
                                    <div class="w-full bg-gray-200 rounded-full h-2">
                                        <div class="bg-gradient-to-r from-blue-500 to-purple-500 h-2 rounded-full" style="width: 60%"></div>
                                    </div>
                                </div>
                            </div>

                            <!-- прикольные штучки -->
                            <div class="absolute -top-4 -right-4 w-22 h-22 bg-yellow-100 rounded-2xl flex items-center justify-center shadow-lg transform rotate-12">
                                <span class="text-yellow-600 font-bold text-sm">🔥 Удобно</span>
                            </div>
                            
                            <div class="absolute -bottom-6 -left-6 w-22 h-22 bg-purple-100 rounded-2xl flex items-center justify-center shadow-lg transform -rotate-6">
                                <span class="text-purple-600 font-bold text-xs">⭐ Надежно</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- какая то инфа -->
        <div class="bg-white border-t border-gray-200 py-16">
            <div class="max-w-7xl mx-auto px-4">
                <div class="grid grid-cols-2 md:grid-cols-2 gap-8 text-center">
                    <div>
                        <div class="text-3xl font-bold text-gray-900">0</div>
                        <div class="text-gray-600">пользователей</div>
                    </div>
                    <div>
                        <div class="text-3xl font-bold text-gray-900">очень много</div>
                        <div class="text-gray-600">задач выполнено</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Dashboard',
}
</script>