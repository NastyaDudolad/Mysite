document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact_form');
    const popup = document.getElementById('popup-message');
    const popupText = document.getElementById('popup-text');
    const popupClose = document.getElementById('popup-close');

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const formData = new FormData(form)

        try {
            const response = await fetch('/process_form', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json'
                },
                body: formData
            });

            const result = await response.json();

            popup.classList.remove('popup-error'); // сброс стиля ошибки
            popupText.textContent = result.message || 'Form submitted.';

            if (!result.success) {
                popup.classList.add('popup-error'); // включить красный стиль
            }

            popup.style.display = 'flex';
        } catch (error) {
            popup.classList.add('popup-error');
            popupText.textContent = 'Server error. Try again later.';
            popup.style.display = 'flex';
            console.error(error);
        }
    });

    // Закрытие по крестику
    popupClose.addEventListener('click', () => {
        popup.style.display = 'none';
    });

    // Закрытие по фону
    popup.addEventListener('click', (e) => {
        if (e.target === popup) {
            popup.style.display = 'none';
        }
    });

    // Отладка checkbox'ов
    const checkboxes = document.querySelectorAll('.form-check-input');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            console.log(`Checkbox "${checkbox.name}" is ${checkbox.checked ? 'checked' : 'unchecked'}`);
        });
    });
});
