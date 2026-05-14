#! /bin/bash

PSQL="psql -X --username=freecodecamp --dbname=salon --tuples-only -c"

echo -e "\n~~~~~ MY SALON ~~~~~\n"

MAIN_MENU() {
  if [[ $1 ]]
    then
        echo -e "\n$1"
          fi

            echo -e "\nHere are the services we offer:\n"
              echo "$($PSQL "SELECT service_id, name FROM services ORDER BY service_id")" | while read SERVICE_ID BAR NAME
                do
                    echo "$SERVICE_ID) $NAME"
                      done

                        echo -e "\nEnter a service_id:"
                          read SERVICE_ID_SELECTED

                            SERVICE=$($PSQL "SELECT name FROM services WHERE service_id=$SERVICE_ID_SELECTED")

                              if [[ -z $SERVICE ]]
                                then
                                    MAIN_MENU "That is not a valid option. Please try again."
                                      else
                                          echo -e "\nWhat is your phone number?"
                                              read CUSTOMER_PHONE

                                                  CUSTOMER_NAME=$($PSQL "SELECT name FROM customers WHERE phone='$CUSTOMER_PHONE'")

                                                      if [[ -z $CUSTOMER_NAME ]]
                                                          then
                                                                echo -e "\nI don't have a record for that phone number, what's your name?"
                                                                      read CUSTOMER_NAME
                                                                            INSERT_CUSTOMER=$($PSQL "INSERT INTO customers(phone, name) VALUES('$CUSTOMER_PHONE', '$CUSTOMER_NAME')")
                                                                                fi

                                                                                    echo -e "\nWhat time would you like your $(echo $SERVICE | xargs) appointment?"
                                                                                        read SERVICE_TIME

                                                                                            CUSTOMER_ID=$($PSQL "SELECT customer_id FROM customers WHERE phone='$CUSTOMER_PHONE'")

                                                                                                INSERT_APPOINTMENT=$($PSQL "INSERT INTO appointments(customer_id, service_id, time) VALUES($CUSTOMER_ID, $SERVICE_ID_SELECTED, '$SERVICE_TIME')")

                                                                                                    echo -e "\nI have put you down for a $(echo $SERVICE | xargs) at $SERVICE_TIME, $(echo $CUSTOMER_NAME | xargs)."
                                                                                                      fi
                                                                                                      }

                                                                                                      MAIN_MENU