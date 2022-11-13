# def getAPI():
import json
import sqlite3
from connection_to_db import DBConnection
from Mapper.MovieDetailsMapper import MovieDetailsMapper
from Model.MovieDetailsModel import MovieDetailsModel
from Mapper.DirectorMapper import DirectorMapper
from Model.DirectorModel import DirectorModel
from Mapper.LeadActorMapper import LeadActorMapper
from Model.LeadActorModel import LeadActorModel

from connection_to_db import DBConnection
from Mapper.DirectorMapper import DirectorMapper
from Mapper.LeadActorMapper import LeadActorMapper
from Mapper.MovieDetailsMapper import MovieDetailsMapper
from Model.DirectorModel import DirectorModel
from Model.LeadActorModel import LeadActorModel
from Model.MovieDetailsModel import MovieDetailsModel
from fastapi import FastAPI

app = FastAPI()


def main():
    # getting metadata.json from url
    url = "https://raw.githubusercontent.com/Brinda-Patel/Dataset/main/metadata.json?token=GHSAT0AAAAAAB24U5N6Q6BHIM7LYX4QQTFMY3MYFIA"

    response = json.load((open('metadata.json')))

    # objects of mapper
    directorMapperObj = DirectorMapper()
    leadActorMapperObj = LeadActorMapper()
    movieDetailsMapperObj = MovieDetailsMapper()

    # objects of model
    directorDetails = DirectorModel()
    actorDetails = LeadActorModel()
    movieDetails = MovieDetailsModel()

    # creating tables using mapper
    directorMapperObj.create_directorDetails()
    leadActorMapperObj.create_actorDetails()
    movieDetailsMapperObj.create_moviedetails()
    movieDetails = MovieDetailsModel()
    movieDetailsMapperObj.select()
    for data in response['movieDetail']:
        directorData = data['director']
        leadActorData = data['leadActor']

        # Inserting Director Details (foreign key)
        directorDetails.directorName = directorData['directorName']
        directorDetails.otherFamousMovie = directorData['otherFamousMovie']
        director_id = directorMapperObj.insert_directorDetails(directorDetails)

        directorDetails.set_director_id(director_id)

        existing_director_id = directorDetails.get_director_id()

        if existing_director_id != None:
            existing_director_id = existing_director_id

        # Inserting Lead Actor Details (foreign key)
        actorDetails.actorName = leadActorData['actorName']
        actorDetails.actorAge = leadActorData['actorAge']
        leadActor_id = leadActorMapperObj.insert_actorDetails(actorDetails)

        actorDetails.set_leadActor_id(leadActor_id)

        existing_leadActor_id = actorDetails.get_leadActor_id()

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


# API routing method calls
movieDetailsMapperObj = MovieDetailsMapper()

# API for displaying general MovieDetails


@app.get("/DisplayMovieDetails")
async def display_all_movie_Detail():
    result_ = movieDetailsMapperObj.select_all()
    return {"movieDetail": result_}

# API for displaying parameterized queries for MovieDetails:- eg: IMDbRating greater than a value, MovieDetail for given ActorName, DirectorName


@app.post("/DisplayMovieDetails/Specific")
async def select_specific(data: dict):
    result_ = movieDetailsMapperObj.select_specific(data)
    return {"movieDetail": result_}

if __name__ == "__main__":

    main()
