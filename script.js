let timer;
let timeLeft = 5;
let gameActive = true;

function startTimer() {
    timeLeft = 5;
    gameActive = true;
    document.getElementById('time').innerText = timeLeft;
    timer = setInterval(() => {
        timeLeft--;
        document.getElementById('time').innerText = timeLeft;
        if (timeLeft <= 0) {
            clearInterval(timer);
            if (gameActive) {
                document.getElementById('result').innerText = 'Time is up! You lose!';
                gameActive = false;
            }
        }
    }, 1000);
}

function playGame(playerChoice) {
    if (!gameActive) return;
    clearInterval(timer);
    gameActive = false;
    const choices = ['rock', 'paper', 'scissors'];
    const computerChoice = choices[Math.floor(Math.random() * 3)];
    let result = '';

    if (playerChoice === computerChoice) {
        result = 'It\'s a draw!';
    } else if (
        (playerChoice === 'rock' && computerChoice === 'scissors') ||
        (playerChoice === 'paper' && computerChoice === 'rock') ||
        (playerChoice === 'scissors' && computerChoice === 'paper')
    ) {
        result = 'You win!';
    } else {
        result = 'You lose!';
    }

    document.getElementById('result').innerText = `You chose ${playerChoice}, computer chose ${computerChoice}. ${result}`;
    document.querySelectorAll('.button').forEach(button => {
        button.classList.remove('chosen');
    });
    document.querySelector(`.button[onclick="playGame('${playerChoice}')"]`).classList.add('chosen');
}

document.addEventListener('DOMContentLoaded', (event) => {
    startTimer();
    document.querySelectorAll('.button').forEach(button => {
        button.addEventListener('click', () => {
            startTimer();
        });
    });
});
