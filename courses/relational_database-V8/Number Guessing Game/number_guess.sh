#!/bin/bash

PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"

SECRET_NUMBER=$((RANDOM % 1000 + 1))

echo "Enter your username:"
read USERNAME

USER_INFO=$($PSQL "SELECT user_id, games_played, best_game FROM users WHERE username='$USERNAME'")

if [[ -z $USER_INFO ]]
then
  echo "Welcome, $USERNAME! It looks like this is your first time here."
  $PSQL "INSERT INTO users(username, games_played) VALUES('$USERNAME', 0)" > /dev/null
  USER_ID=$($PSQL "SELECT user_id FROM users WHERE username='$USERNAME'")
else
  IFS='|' read -r USER_ID GAMES_PLAYED BEST_GAME <<< "$USER_INFO"
  echo "Welcome back, $USERNAME! You have played $GAMES_PLAYED games, and your best game took $BEST_GAME guesses."
fi

echo "Guess the secret number between 1 and 1000:"

NUMBER_OF_GUESSES=0

while true
do
  read GUESS

  if ! [[ $GUESS =~ ^[0-9]+$ ]]
  then
    echo "That is not an integer, guess again:"
  elif [[ $GUESS -lt $SECRET_NUMBER ]]
  then
    echo "It's higher than that, guess again:"
    ((NUMBER_OF_GUESSES++))
  elif [[ $GUESS -gt $SECRET_NUMBER ]]
  then
    echo "It's lower than that, guess again:"
    ((NUMBER_OF_GUESSES++))
  else
    ((NUMBER_OF_GUESSES++))
    echo "You guessed it in $NUMBER_OF_GUESSES tries. The secret number was $SECRET_NUMBER. Nice job!"

    CURRENT_GAMES=$($PSQL "SELECT games_played FROM users WHERE user_id=$USER_ID")
    NEW_GAMES=$((CURRENT_GAMES + 1))
    CURRENT_BEST=$($PSQL "SELECT best_game FROM users WHERE user_id=$USER_ID")

    if [[ -z $CURRENT_BEST ]] || [[ $NUMBER_OF_GUESSES -lt $CURRENT_BEST ]]
    then
      $PSQL "UPDATE users SET games_played=$NEW_GAMES, best_game=$NUMBER_OF_GUESSES WHERE user_id=$USER_ID" > /dev/null
    else
      $PSQL "UPDATE users SET games_played=$NEW_GAMES WHERE user_id=$USER_ID" > /dev/null
    fi

    break
  fi
done
