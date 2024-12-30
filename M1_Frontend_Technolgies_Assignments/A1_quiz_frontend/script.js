const questions = [
    {
        question: "What is the capital of France?",
        answers: ["Paris", "London", "Berlin", "Rome"],
        correct: "Paris"
    },
    {
        question: "Which planet is known as the Red Planet?",
        answers: ["Earth", "Venus", "Mars", "Jupiter"],
        correct: "Mars"
    },
    {
        question: "What is 2 + 2?",
        answers: ["3", "4", "5", "6"],
        correct: "4"
    },
    {
        question: "Which animal is known as the king of the jungle?",
        answers: ["Lion", "Tiger", "Elephant", "Giraffe"],
        correct: "Lion"
    },
    {
        question: "Which is the largest ocean on Earth?",
        answers: ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        correct: "Pacific Ocean"
    }
];

let currentQuestionIndex = 0;
let score = 0;
let timer;
let timeLeft = 30;

const questionElement = document.getElementById("question");
const answerButtonsElement = document.getElementById("answer-buttons");
const nextButton = document.getElementById("next-btn");
const scoreElement = document.getElementById("score");
const timeElement = document.getElementById("time");

function startQuiz() {
    currentQuestionIndex = Math.floor(Math.random() * questions.length);
    score = 0;
    timeLeft = 30;
    scoreElement.textContent = "";
    startTimer();
    showQuestion();
}

function showQuestion() {
    resetState();
    const currentQuestion = questions[currentQuestionIndex];
    questionElement.textContent = currentQuestion.question;

    currentQuestion.answers.forEach(answer => {
        const li = document.createElement("li");
        const button = document.createElement("button");
        button.textContent = answer;
        button.addEventListener("click", () => selectAnswer(answer, button));
        li.appendChild(button);
        answerButtonsElement.appendChild(li);
    });
}

function resetState() {
    while (answerButtonsElement.firstChild) {
        answerButtonsElement.removeChild(answerButtonsElement.firstChild);
    }
    nextButton.style.display = "none";
    clearInterval(timer);
}

function startTimer() {
    timer = setInterval(() => {
        timeLeft--;
        timeElement.textContent = timeLeft;
        if (timeLeft <= 0) {
            clearInterval(timer);
            selectAnswer("", null); // Auto select a wrong answer if time runs out
        }
    }, 1000);
}

function selectAnswer(selectedAnswer, button) {
    const currentQuestion = questions[currentQuestionIndex];

    // Show correct answer feedback
    if (selectedAnswer === currentQuestion.correct) {
        score++;
        button.classList.add("correct");
    } else {
        button.classList.add("wrong");
        const correctButton = Array.from(answerButtonsElement.children).find(li => li.textContent === currentQuestion.correct).children[0];
        correctButton.classList.add("correct"); // Highlight the correct answer
    }

    clearInterval(timer);
    nextButton.style.display = "block";
    scoreElement.textContent = `Score: ${score}`;
}

nextButton.addEventListener("click", () => {
    startQuiz();
});

startQuiz();
