// Ініціалізація Bootstrap модальних вікон
document.addEventListener('DOMContentLoaded', () => {
    // Отримати всі модальні вікна
    const bookingModal = document.getElementById('booking-modal');

    // Очистити вміст модального вікна після закриття
    bookingModal.addEventListener('hidden.bs.modal', () => {
        const modalContent = document.getElementById('modal-content');
        if (modalContent) {
            modalContent.innerHTML = ''; // Очищення вмісту
        }
    });

    console.log("Скрипт завантажено та готово до роботи.");
});

// AJAX-запити з htmx — відображення повідомлень про помилки
document.body.addEventListener('htmx:responseError', (event) => {
    alert('Помилка запиту: ' + event.detail.xhr.responseText);
});

// Додавання перевірки на валідацію форм (приклад для модального бронювання)
document.body.addEventListener('submit', (event) => {
    const form = event.target;

    if (form.checkValidity() === false) {
        event.preventDefault();
        event.stopPropagation();

        // Додати класи для Bootstrap
        form.classList.add('was-validated');
    }
});
