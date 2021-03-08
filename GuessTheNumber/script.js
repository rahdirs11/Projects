'use strict';

var randomNumber = getRandomNumber(), highScore = 0;

document.querySelector('.again').addEventListener('click',
    function() {
        randomNumber = getRandomNumber()
        document.querySelector('.score').textContent = 20
        document.querySelector('.number').textContent = '?'
        document.querySelector('body').style.backgroundColor = '#222'
        displayMessage('Start guessing...')
    }
)

function getRandomNumber() {
    return Math.trunc(Math.random() * 20) + 1
}


function getCurrentScore() {
    return Number(document.querySelector('.score').textContent)
}


function getHighScore() {
    var currentScore = getCurrentScore()
    if (currentScore >= highScore) {
        highScore = currentScore
    }
    return highScore
}


function displayMessage(message) {
    document.querySelector('.message').textContent = message;
}


document.querySelector('.check').addEventListener('click',
    function() {
        let guessedValue = Number(document.querySelector('.guess').value)
        if (!guessedValue) {
            document.querySelector('.message').textContent = 'Choose a Number!!'
        } else {
            if (getCurrentScore() == 0) {
                displayMessage('YOU LOST!!')
            } else {
                if (guessedValue === randomNumber) {
                    displayMessage('VOILA')
                    document.querySelector('body').style.backgroundColor = '#60b347'
                    document.querySelector('.number').style.width = '30rem'
                    document.querySelector('.highscore').textContent = getHighScore()
                    document.querySelector('.number').textContent = guessedValue
                } else {
                    document.querySelector('.score').textContent = getCurrentScore() - 1
                    if (guessedValue < randomNumber) {
                        displayMessage('Too Low!')
                    } else {
                        displayMessage('Too High')
                    }
                }
            }
        }
    }
)
