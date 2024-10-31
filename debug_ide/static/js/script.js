let selectedQuestion = "";

function loadQuestions(level) {
    const questionsListDiv = document.getElementById('questions-list');
    questionsListDiv.style.display = 'block';

    let questions;
    switch(level) {
        case '一星題':
            questions = ['一星題目 1', '一星題目 2', '一星題目 3'];
            break;
        case '二星題':
            questions = ['二星題目 1', '二星題目 2', '二星題目 3'];
            break;
        case '三星題':
            questions = ['三星題目 1', '三星題目 2', '三星題目 3'];
            break;
    }

    questionsListDiv.innerHTML = '';
    questions.forEach((question, index) => {
        const questionElement = document.createElement('button');
        questionElement.className = 'question-button';
        questionElement.innerText = question;
        questionElement.onclick = function() {
            selectQuestion(question);
        };
        questionsListDiv.appendChild(questionElement);
    });
}

function selectQuestion(question) {
    selectedQuestion = question;
    localStorage.setItem('selectedQuestion', selectedQuestion);
    alert(`您已選擇: ${selectedQuestion}`);
    window.location.href = '/ide'; // 假設返回 ide 的路徑
}

document.addEventListener('DOMContentLoaded', () => {
    const viewQuestion = document.getElementById('view-question');
    if (viewQuestion) {
        viewQuestion.addEventListener('click', () => {
            const selected = localStorage.getItem('selectedQuestion') || '尚未選擇題目';
            alert(`您選擇的題目是：${selected}`);
        });
    }
});
