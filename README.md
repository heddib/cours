# Projet de CRUD en Python

Le projet de cette semaine est de faire un CRUD avec Python et Django.

## Lancement du projet

Le site étant fait avec Django (Python), il faut utiliser la commande python pour faire fonctionner le projet.

Il faut penser à faire les migrations.

Pour lancer le serveur : 
```bash
  python3 manage.py runserver
```

## URLs

Les urls pour le CRUD sont :

#### Récupérer tous les cours

```http
  GET /cours
```

#### Créer un cours

```http
  GET|POST /cours/create
```

#### Montrer un cours

```http
  GET /cours/show/${id}
```

| Paramètre | Type     | Description                          |
| :-------- | :------- | :----------------------------------- |
| `id`      | `int`    | **Requis**. Id du cours à récupérer  |

**Pour information :** Les cours peuvent être montrés depuis l'index des cours.

#### Mettre à jour un cours

```http
  GET|POST /cours/update/${id}
```

| Paramètre | Type     | Description                              |
| :-------- | :------- | :--------------------------------------- |
| `id`      | `int`    | **Requis**. Id du cours à mettre à jour  |

#### Supprimer un cours

```http
  GET /cours/delete/${id}
```

| Paramètre | Type     | Description                          |
| :-------- | :------- | :----------------------------------  |
| `id`      | `int`    | **Requis**. Id du cours à supprimer  |

**Pour information :** Les cours peuvent être supprimés depuis l'index des cours.

-- Heddi Brahiti