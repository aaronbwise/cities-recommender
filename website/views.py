from flask import Blueprint, render_template, request
from app import recommender

views = Blueprint(
    "views", __name__, static_folder="static", template_folder="templates"
)


@views.route("/search", methods=["GET", "POST"])
def search():
    # Initialize target_msa outside of the request method checks
    target_msa = None

    if request.method == "GET":
        city_name = request.args.get("city_name", None)
        if city_name:
            target_msa = recommender.get_msa_code(city_name)

    elif request.method == "POST":
        target_msa = request.form.get("target_msa")

    # Check if target_msa was successfully retrieved/set
    if target_msa:
        # Use target_msa in recommender.predict_msa() to get the top 3 recommended MSAs
        predicted_msas = recommender.predict_msa(target_msa)
        all_msas = [target_msa] + predicted_msas
        
        city_names = recommender.get_city_names(all_msas)
        city_pop = recommender.get_city_pop(all_msas)
        city_rent = recommender.get_city_rent(all_msas)
        city_income = recommender.get_city_income(all_msas)
        city_home = recommender.get_city_home(all_msas)
        city_wiki_urls = recommender.get_city_wiki_url(all_msas)
        city_thumbnail_urls = recommender.get_city_wiki_thumbnail_url(all_msas)
        
        # Render template with the data for either POST or GET request
        return render_template(
            "search.html",
            city_name_0=city_names[0],
            city_name_1=city_names[1],
            city_name_2=city_names[2],
            city_name_3=city_names[3],
            city_wiki_urls_0=city_wiki_urls[0],
            city_pop_0=city_pop[0],
            city_rent_0=city_rent[0],
            city_income_0=city_income[0],
            city_home_0=city_home[0],
        )
    else:
        # If target_msa is not set, render the search template possibly with an error message or default state
        return render_template("search.html", error="No valid city name or MSA code provided.")


@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/methodology")
def methodology():
    return render_template("methodology.html")
