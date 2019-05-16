import random

def random_site(request):
  sites = [ "https://www.themoviedb.org/assets/2/v4/footers_v2/TheDarkKnight-7bc76e8795dbf0a2ac7995f4e47f330ba3d4a58ffe952ab86582f666ab0215e9.jpg",
               "https://www.themoviedb.org/assets/2/v4/footers_v2/IronMan-f01af499111f9be05deb806fdaf52e2d138fefa1fae09f33339348c032923d15.jpg",
                "https://www.themoviedb.org/assets/2/v4/footers_v2/FamilyGuy-157ce987f45266a74584f1b695db2e23edb6e14b600bdd8ea1aa27edd710a3fb.jpg",
                "https://www.themoviedb.org/assets/2/v4/footers_v2/Minions-7626a4bff6ef7b6a7afa6a8641278e23b094d6a882da4129d9a8928d05b3b911.jpg"]
  site = random.choice(sites)
  return {'site': site}