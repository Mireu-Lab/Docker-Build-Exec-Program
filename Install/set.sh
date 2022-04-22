sudo cp Install/exec_maneger.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable exec_maneger
sudo systemctl start exec_maneger
sudo systemctl status exec_maneger