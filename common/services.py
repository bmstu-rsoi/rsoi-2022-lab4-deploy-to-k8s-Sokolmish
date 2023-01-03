import os

GATEWAY_PORT = 8080
LOYALTY_PORT = 8050
PAYMENT_PORT = 8060
RESERVATION_PORT = 8070

LOYALTY_ADDR = f'http://spread-loyalty:{LOYALTY_PORT}'
PAYMENT_ADDR = f'http://spread-payment:{PAYMENT_PORT}'
RESERVATION_ADDR = f'http://spread-reservation:{RESERVATION_PORT}'

DATABASE_ADDR = 'psql-smth-postgresql'
