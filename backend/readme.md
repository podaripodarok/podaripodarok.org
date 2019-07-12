yum update;

sudo yum -y install epel-release;
sudo yum -y install centos-release-scl;
sudo yum -y install rh-python36;
scl enable rh-python36 bash;

sudo yum -y install python-pip;

sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm;
sudo yum -y install python36u;
sudo yum -y install python36u-pip;
sudo yum -y install python36u-devel;

#Install venv
sudo chmod 777 -R pp
sudo python3.6 -m venv myvenv;
source myvenv/bin/activate;

#Install python libs
sudo pip install --upgrade pip;
pip install -r requirements.txt

#Install Docker
sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2;
sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo;
sudo yum -y install docker-ce docker-ce-cli containerd.io;
sudo systemctl start docker;
sudo docker run hello-world;

#Install docker-compose
sudo curl -L https://github.com/docker/compose/releases/download/1.17.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

sudo service postgresql stop;
docker-compose up -d
docker-compose down
sudo /usr/local/bin/docker-compose up

#Start Django
django-admin startproject podaripodarok .
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py startapp pp_app
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', '1111')" | python manage.py shell

#Copy files to AWS
sudo scp -r -i ~/.ssh/pp_key.pem /home/admin/Documents/projects/pp/backend/* centos@18.222.134.116:/opt/pp/backend/

#GraphQL
```
query {
  users{
    id, username, email
  }
}
```

```
mutation {createUser(username: "test", email: "test@test.test", password: "Aa123456!"){
  user{
    id, username, email
  }
}
}
```