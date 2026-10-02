const questions = [
    {
        question: "Quel langage est principalement utilisé avec FastAPI ?",
        answers: [
            "Python",
            "Java",
            "C++",
            "PHP",
            "JavaScript"
        ],
        correct: 0
    },

    {
        question: "Quel outil permet de versionner le code source ?",
        answers: [
            "Docker",
            "Git",
            "Excel",
            "Figma",
            "Photoshop"
        ],
        correct: 1
    },

    {
        question: "Quel algorithme est utilisé par notre service IA E4 ?",
        answers: [
            "Decision Tree",
            "Bubble Sort",
            "K-Means",
            "DFS",
            "Recherche linéaire"
        ],
        correct: 0
    },

    {
        question: "Quel outil permet d'automatiser l'intégration continue ?",
        answers: [
            "PowerPoint",
            "Word",
            "GitHub Actions",
            "Excel",
            "Photoshop"
        ],
        correct: 2
    },

    {
        question: "Quel format est utilisé pour communiquer avec notre API ?",
        answers: [
            "PNG",
            "MP3",
            "DOCX",
            "JSON",
            "JPEG"
        ],
        correct: 3
    }
];


let currentQuestion = 0;
let score = 0;
let errors = 0;

let selectedAnswer = null;

let questionStartTime = 0;
let totalResponseTime = 0;


const questionTitle =
    document.getElementById("question-title");

const progressText =
    document.getElementById("progress-text");

const progress =
    document.getElementById("progress");

const question =
    document.getElementById("question");

const answers =
    document.getElementById("answers");

const validateButton =
    document.getElementById("validate-button");

const instruction =
    document.getElementById("instruction");

const resultSection =
    document.getElementById("result-section");

const scoreElement =
    document.getElementById("score");

const errorsElement =
    document.getElementById("errors");

const timeElement =
    document.getElementById("time");

const aiMessage =
    document.getElementById("ai-message");

const confidence =
    document.getElementById("confidence");

const restartButton =
    document.getElementById("restart-button");


function displayQuestion() {

    const current =
        questions[currentQuestion];


    selectedAnswer = null;

    validateButton.disabled = true;


    questionTitle.textContent =
        `Question ${currentQuestion + 1}`;


    progressText.textContent =
        `${currentQuestion + 1} / ${questions.length}`;


    const progressValue =
        ((currentQuestion + 1)
        / questions.length) * 100;


    progress.style.width =
        `${progressValue}%`;


    question.textContent =
        current.question;


    answers.innerHTML = "";


    const letters = [
        "A",
        "B",
        "C",
        "D",
        "E"
    ];


    current.answers.forEach(
        (answer, index) => {

            const button =
                document.createElement("button");


            button.className = "answer";


            button.innerHTML = `
                <span class="answer-letter">
                    ${letters[index]} -
                </span>

                <span class="radio"></span>

                <span>
                    ${answer}
                </span>
            `;


            button.addEventListener(
                "click",
                () => {

                    document
                        .querySelectorAll(".answer")
                        .forEach(
                            item =>
                                item.classList.remove(
                                    "selected"
                                )
                        );


                    button.classList.add(
                        "selected"
                    );


                    selectedAnswer = index;

                    validateButton.disabled =
                        false;


                    instruction.textContent =
                        "Réponse sélectionnée.";
                }
            );


            answers.appendChild(button);

        }
    );


    questionStartTime =
        performance.now();
}


validateButton.addEventListener(
    "click",
    () => {

        if (selectedAnswer === null) {
            return;
        }


        const responseTime =
            (
                performance.now()
                - questionStartTime
            ) / 1000;


        totalResponseTime +=
            responseTime;


        const current =
            questions[currentQuestion];


        if (
            selectedAnswer ===
            current.correct
        ) {

            score++;

        } else {

            errors++;

        }


        currentQuestion++;


        if (
            currentQuestion <
            questions.length
        ) {

            displayQuestion();

        } else {

            finishQuiz();

        }

    }
);


async function finishQuiz() {

    const averageTime =
        totalResponseTime /
        questions.length;


    const finalScore =
        (
            score /
            questions.length
        ) * 100;


    questionTitle.textContent =
        "Résultat";


    progressText.textContent =
        "Terminé";


    progress.style.width =
        "100%";


    document
        .querySelector(".question-section")
        .classList.add("hidden");


    document
        .querySelector(".qcm-footer")
        .classList.add("hidden");


    resultSection.classList.remove(
        "hidden"
    );


    scoreElement.textContent =
        `${score} / ${questions.length}`;


    errorsElement.textContent =
        errors;


    timeElement.textContent =
        `${averageTime.toFixed(1)} s`;


    aiMessage.textContent =
        "Analyse du résultat par le service IA...";


    confidence.textContent =
        "-- %";


    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/predict",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        score:
                            finalScore,

                        temps_moyen:
                            averageTime,

                        nb_erreurs:
                            errors

                    })
                }
            );


        if (!response.ok) {

            throw new Error(
                "Erreur du service IA"
            );

        }


        const prediction =
            await response.json();


        if (
            prediction.satisfait === 1
        ) {

            aiMessage.textContent =
                "L'analyse IA indique une expérience utilisateur satisfaisante.";

        } else {

            aiMessage.textContent =
                "L'analyse IA indique que l'expérience utilisateur pourrait être améliorée.";

        }


        confidence.textContent =
            `${(
                prediction.confidence * 100
            ).toFixed(1)} %`;


    } catch (error) {

        console.error(error);


        aiMessage.textContent =
            "Impossible de contacter le service IA.";


        confidence.textContent =
            "Indisponible";

    }
}


restartButton.addEventListener(
    "click",
    () => {

        currentQuestion = 0;

        score = 0;

        errors = 0;

        selectedAnswer = null;

        totalResponseTime = 0;


        resultSection.classList.add(
            "hidden"
        );


        document
            .querySelector(".question-section")
            .classList.remove("hidden");


        document
            .querySelector(".qcm-footer")
            .classList.remove("hidden");


        instruction.textContent =
            "Sélectionnez une réponse.";


        displayQuestion();

    }
);


displayQuestion();