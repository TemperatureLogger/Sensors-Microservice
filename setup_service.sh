## Add service descriptor file
sudo cp ./sensor-data.service /lib/systemd/system/

## Give permissions to the service
sudo chmod 644 /lib/systemd/system/sensor-data.service

## Enable the service
sudo systemctl daemon-reload
sudo systemctl enable sample.service

## Run the service
sudo systemctl start sample.service

