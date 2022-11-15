from Model.LeadActorModel import LeadActorModel
from Model.DirectorModel import DirectorModel
from Mapper.LeadActorMapper import LeadActorMapper
from Mapper.DirectorMapper import DirectorMapper
from Mapper.MovieDetailsMapper import MovieDetailsMapper
from Model.MovieDetailsModel import MovieDetailsModel
import pytest

test_json_row = {
    "movieDetail": [
        {
            "title": "Forrest Gump",
            "movieIMDbRating": 8.8,
            "totalRatingCount": 2016919,
            "totalUserReviews": "2.9K",
            "totalCriticReviews": "173",
            "director": {
                "directorName": "Robert Zemeckis",
                "otherFamousMovie": "Flight"
            },
            "datePublished": "1994-07-06",
            "leadActor": {
                "actorName": "Tom Hanks",
                "actorAge": 66
            },
            "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood swe...",
            "duration": 142
        }]}

_movieDetailsMapperObj = MovieDetailsMapper()
_leadActorMapperObj = LeadActorMapper()
_directorMapperObj = DirectorMapper()


@pytest.mark.xfail
@pytest.mark.one
def test_insert_directorDetails():
    _directorDetails = DirectorModel()
    _directorDetails.directorName = 'Robert Zemeckis'
    _directorDetails.otherFamousMovie = 'Flight'
    director_id = _directorMapperObj.insert_directorDetails(_directorDetails)
    assert director_id is None, 'Insertion failed because data already exists'


@pytest.mark.xfail
@pytest.mark.two
def test_insert_actorDetails():
    _actorDetails = LeadActorModel()
    _actorDetails.actorName = 'Tom Hanks'
    _actorDetails.actorAge = 66
    leadActor_id = LeadActorMapper().insert_actorDetails(_actorDetails)
    assert leadActor_id is None, 'Insertion failed because data already exists'


@pytest.mark.three
def test_get_actor_name():
    actor_name = _leadActorMapperObj.getRowByActorName('Tom Hanks')
    assert actor_name is not None, 'Will pass as actor exists'
    print('Actor already exists')
    actor_name_test = _leadActorMapperObj.getRowByActorName('Brinda Patel')
    assert actor_name_test is None, 'actor does not exists'


@pytest.mark.four
def test_get_director_name():
    director_name_test = DirectorMapper().getRowByDirectorName('Robert Zemeckis')
    assert director_name_test is not None, 'Will pass as actor exists'

    director_name_test = DirectorMapper().getRowByDirectorName('Konark Shah')
    assert director_name_test is None, 'Director does not exists'


@pytest.mark.five
def test_insert_movieDetails_Value():
    try_data = {"title": "Forrest Gump",
                "movieIMDbRating": 8.8,
                "totalRatingCount": 2016919,
                "totalUserReviews": "2.9K",
                "totalCriticReviews": "173",
                "datePublished": "1994-07-06",
                "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood swe...",
                "duration": 142
                }
    _movieDetailsModel = MovieDetailsModel()
    _movieDetailsModel.title = try_data['title']
    _movieDetailsModel.movieIMDbRating = try_data['movieIMDbRating']
    _movieDetailsModel.totalRatingCount = try_data['totalRatingCount']
    _movieDetailsModel.totalUserReviews = try_data['totalUserReviews']
    _movieDetailsModel.totalCriticReviews = try_data['totalCriticReviews']
    _movieDetailsModel.datePublished = try_data['datePublished']
    _movieDetailsModel.description = try_data['description']
    _movieDetailsModel.duration = try_data['duration']

    assert _movieDetailsMapperObj.insert_moviedetails(
        _movieDetailsModel) is None, 'Insertion failed beacuse of duplicate entry'


@pytest.mark.six
def test_select_specific_query():
    __movieDetailsMapperObj = MovieDetailsMapper()
    res = __movieDetailsMapperObj.select_specific({"movieIMDbRating": 8})
    assert len(res) != 0, 'Select specific rows Passed'


@pytest.mark.xfail
@pytest.mark.seven
def test_select_specific_query_movieIMDbRating():
    _movieDetailsMapperObj = MovieDetailsMapper()
    assert _movieDetailsMapperObj.select_specific(
        {"movieIMDbRating": 15}) is None, 'Select specific rows failed as no data found'


@pytest.mark.eight
def test_select_specific_query_director_name_exists():
    _movieDetailsMapperObj = MovieDetailsMapper()
    assert _movieDetailsMapperObj.select_specific(
        {"directorName": 'Robert Zemeckis'}) is not None, 'Select specific rows passed'


@pytest.mark.xfail
@pytest.mark.nine
def test_select_specific_query_director_name_not_exists():
    _movieDetailsMapperObj = MovieDetailsMapper()
    assert _movieDetailsMapperObj.select_specific(
        {"directorName": 'Divya Gupta'}) is None, 'Select specific rows failed as no data found'