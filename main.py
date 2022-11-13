# connection = sqlite3.connect('dataset2.db')
# cursor = connection.cursor()
# # cursor.execute('select * from Covid_World_Data')
# # print(cursor.fetchall())
# # cursor.execute('DROP TABLE IF EXISTS Covid_Tracking')  # drop table if exists
# # cursor.execute(
# #     'Create Table Movie (movie_title varchar(20), movieIMDbRating float, totalRatingCount int, movieReleaseDate datetime, Description varchar(20))')
# # cursor.execute('Create Table Directors (director_name varchar(20))')
# # cursor.execute('Create Table Actors (Actor_name varchar(20))')

# # url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

# url = "https://raw.githubusercontent.com/Brinda-Patel/Dataset/main/metadata.json?token=GHSAT0AAAAAAB24U5N6Q6BHIM7LYX4QQTFMY3MYFIA"

# # headers = {
# #     "X-RapidAPI-Key": "8c86fec264msh6e986273003680fp1d329bjsnbbe0dd435331",
# #     "X-RapidAPI-Host": "corona-virus-world-and-india-data.p.rapidapi.com"
# # }

# response = json.load((open('metadata.json')))
# # response = requests.request("GET", url)

# # print(response.json()['countries_stat']

# traffic = response
# print(response, type(response))
# columns = ['movie_title', 'movieIMDbRating',
#            'totalRatingCount', 'movieReleaseDate', 'Description']
# columns1 = ['director_name']
# columes2 = ['Actor_name']

# i = 0
# for row in traffic:
#     print(row)
#     a = list(traffic.keys())[i]

#     for row1 in traffic[a]:
#         print(row1)
#         keys = tuple(row1[c] for c in columns)
#         cursor.execute(
#             f'INSERT INTO {a} VALUES (?, ?, ?, ?, ?)', keys)
#     i += 1
#     # if row == 'Movie':
#     #     for row1 in traffic['Movie']:
#     #         print(row1)
#     #         keys = tuple(row1[c] for c in columns)
#     #         cursor.execute('INSERT INTO Movie VALUES (?, ?, ?, ?, ?)', keys)
#     # if row == 'Director':
#     #     for row2 in traffic['Director']:
#     #         print(row2)
#     #         keys = tuple(row2[c] for c in columns1)
#     #         cursor.execute('INSERT INTO Directors VALUES (?)', keys)
#     # if row == 'Actor':
#     #     for row3 in traffic['Actor']:
#     #         print(row3)
#     #         keys = tuple(row3[c] for c in columes2)
#     #         cursor.execute('INSERT INTO Actors VALUES (?)', keys)

#     # if row["Movie"]:
#     #     keys = tuple(row["Movie"][c] for c in columns)
#     #     cursor.execute('Insert into Movie values(?,?,?,?,?)', keys)
#     # keys = tuple(row[c] for c in columns)
#     # cursor.execute(
#     #     'insert into Covid_World_Data values(?,?,?,?,?,?,?,?,?,?,?,?,?)', keys)

# connection.commit()
# connection.close()


# connection = sqlite3.connect('dataset5.db')
# cursor = connection.cursor()

# cursor.execute(
#     'Create Table if NOT EXISTS director (director_id INTEGER PRIMARY KEY AUTOINCREMENT, directorName varchar(20), otherFamousMovie varchar(20))')
# cursor.execute(
#     'Create Table if NOT EXISTS leadActor (leadActor_id INTEGER PRIMARY KEY AUTOINCREMENT, actorName varchar(20), actorAge int)')
# cursor.execute(
#     'CREATE TABLE if NOT EXISTS movieDetail (movieDetail_id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR (20), movieIMDbRating  DECIMAL (2, 1), totalRatingCount INTEGER, totalUserReviews VARCHAR (20), totalCriticReviews VARCHAR (20), director_id INTEGER REFERENCES director (director_id), datePublished DATE, leadActor_id INTEGER REFERENCES leadActor (leadActor_id), description TEXT, duration INTEGER)')

# for data in response['movieDetail']:
#     directorData = data['director']
#     leadActorData = data['leadActor']

# insert_directorDetails = "insert into director (directorName, otherFamousMovie) values ('%s','%s')" % (
#     directorData['directorName'], directorData['otherFamousMovie'])
# cursor.execute(insert_directorDetails)
# director_fk = cursor.lastrowid

# insert_leadActorDetails = "insert into leadActor (actorName,actorAge) values ('%s','%s')" % (
#     leadActorData['actorName'], leadActorData['actorAge'])
# cursor.execute(insert_leadActorDetails)
# leadActor_fk = cursor.lastrowid

# insert_moviedetails = "insert into movieDetail (title,movieIMDbRating,totalRatingCount,totalUserReviews,totalCriticReviews,datePublished,description,duration,director_id,leadActor_id) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
#     data['title'], data['movieIMDbRating'], data['totalRatingCount'], data['totalUserReviews'], data['totalCriticReviews'], data['datePublished'], data['description'], data['duration'], director_fk, leadActor_fk)
# cursor.execute(insert_moviedetails)
# print(data)

# def getAPI():
import json
import sqlite3
from connection_to_db import DBConnection
from Mapper.MovieDetailsMapper import MovieDetailsMapper
from Model.MovieDetails import MovieDetails
from Mapper.DirectorMapper import DirectorMapper
from Model.DirectorModel import DirectorModel
from Mapper.LeadActorMapper import LeadActorMapper
from Model.LeadActorModel import LeadActorModel


def main():

    url = "https://raw.githubusercontent.com/Brinda-Patel/Dataset/main/metadata.json?token=GHSAT0AAAAAAB24U5N6Q6BHIM7LYX4QQTFMY3MYFIA"

    response = json.load((open('metadata.json')))

    directorMapperObj = DirectorMapper()
    leadActorMapperObj = LeadActorMapper()

    directorDetails = DirectorModel()
    actorDetails = LeadActorModel()
    directorMapperObj.create_directorDetails()
    leadActorMapperObj.create_actorDetails()
    movieDetailsMapperObj = MovieDetailsMapper()
    movieDetailsMapperObj.create_moviedetails()
    movieDetails = MovieDetails()
    movieDetailsMapperObj.select()
    for data in response['movieDetail']:
        directorData = data['director']
        leadActorData = data['leadActor']

        # Inserting Director Details (foreign key)
        directorDetails.directorName = directorData['directorName']
        directorDetails.otherFamousMovie = directorData['otherFamousMovie']
        director_id = directorMapperObj.insert_directorDetails(directorDetails)

        # print("director_id" + str(director_id))
        directorDetails.set_director_id(director_id)

        existing_director_id = directorDetails.get_director_id()

        if existing_director_id != None:
            existing_director_id = existing_director_id

        # Inserting Lead Actor Details (foreign key)
        actorDetails.actorName = leadActorData['actorName']
        actorDetails.actorAge = leadActorData['actorAge']
        leadActor_id = leadActorMapperObj.insert_actorDetails(actorDetails)

        # print("leadActor_id" + str(leadActor_id))
        actorDetails.set_leadActor_id(leadActor_id)

        existing_leadActor_id = actorDetails.get_leadActor_id()

        # if existing_leadActor_id != None:
        #     existing_leadActor_id = existing_leadActor_id

        movieDetails.title = data['title']
        movieDetails.movieIMDbRating = data['movieIMDbRating']
        movieDetails.totalRatingCount = data['totalRatingCount']
        movieDetails.totalUserReviews = data['totalUserReviews']
        movieDetails.totalCriticReviews = data['totalCriticReviews']
        movieDetails.datePublished = data['datePublished']
        movieDetails.director_id = existing_director_id
        movieDetails.leadActor_id = existing_leadActor_id
        movieDetails.description = data['description']
        movieDetails.duration = data['duration']
        movieDetailsMapperObj.insert_moviedetails(movieDetails)


if __name__ == "__main__":

    main()

# cursor.close()
# connection.commit()
# connection.close()
