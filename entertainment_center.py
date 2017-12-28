# coding=utf-8
import media
import fresh_tomatoes

# creating instances of Movie
dose_dupla = media.Movie('Dose Dupla',
                         'Um poderoso traficante mexicano que atua nos Estados'
                         ' Unidos',
                         'http://br.web.img3.acsta.net/pictures/210/294/21029485_20130820170746615.jpg',  # NOQA
                         'https://www.youtube.com/watch?v=VXC8UBJmyu4')

homem_aranha = media.Movie('Homem Aranha',
                           'Um jovem Peter Parker/Homem-Aranha (Tom Holland), '
                           'que fez sua estreia sensacional em Capitão '
                           'América: Guerra Civil',
                           'http://t2.gstatic.com/images?q=tbn:ANd9GcT4O7xrHjQ1NMu_9kg6E9HUO4X7KtB9lVpVLglQfWH2BJIke3IB',  # NOQA
                           'https://www.youtube.com/watch?v=2x-2iYxgMFU')

vingadores_guerra_infinita = media.Movie('Vingadores: Guerra Infinita',
                                         'Thanos (Josh Brolin) enfim chega à '
                                         'Terra, disposto a reunir as Joias '
                                         'do Infinito. Para enfrentá-lo, os '
                                         'Vingadores precisam unir forças com '
                                         'os Guardiões da Galáxia, ao mesmo '
                                         'tempo em que lidam com desavenças '
                                         'entre alguns de seus integrantes.',
                                         'https://kanto.legiaodosherois.com.br/fnoop/wp-content/uploads/2017/08/legiao_hM0JOWENxy1Auo5R_qXnd7vLCcs8jprakSQeYGH6PB.jpg',  # NOQA
                                         'https://www.youtube.com/watch?v=3BXq73F2_z4')  # NOQA

deadpool = media.Movie('Deadpool',
                       'Deadpool é um filme de ação e comédia americano '
                       'dirigido por Tim Miller e distribuído pela 20th '
                       'Century Fox que tem como protagonista o icônico '
                       'personagem da Marvel que dá nome ao longa, sendo o '
                       'oitavo título da franquia X-Men.',
                       'http://t0.gstatic.com/images?q=tbn:ANd9GcRoIgB6qnXHGPWzm44be8hbsFpoWWcKPwcC1gWwMOdc2W_N28HG',  # NOQA
                       'https://www.youtube.com/watch?v=Xithigfg7dA')

logan = media.Movie('Logan',
                    'Em 2029, Logan (Hugh Jackman) ganha a vida como chofer de'
                    ' limousine para cuidar do nonagenário Charles Xavier '
                    '(Patrick Stewart). Debilitado fisicamente e esgotado '
                    'emocionalmente, ele é procurado por Gabriela '
                    '(Elizabeth Rodriguez), uma mexicana que precisa da ajuda '
                    'do ex-X-Men para defender a pequena Laura Kinney / X-23 ',
                    'https://s3.amazonaws.com/ffe-ugc/intlportal2/dev-temp/en-US/__595033e88ceb2.jpg',  # NOQA
                    'https://www.youtube.com/watch?v=XaE_9pfybL4')

velozes_e_furiosos_8 = media.Movie('Velozes & Furioso 8',
                                   'Dom (Vin Diesel) e Letty '
                                   '(Michelle Rodriguez) estão curtindo a lua '
                                   'de mel em Havana, mas a súbita aparição '
                                   'de Cipher (Charlize Theron) atrapalha os '
                                   'planos do casal. Ela logo arma um plano '
                                   'para chantagear Dom, de forma que ele '
                                   'traia seus amigos e passe a ajudá-la a '
                                   'obter ogivas nucleares.',
                                   'http://br.web.img3.acsta.net/pictures/17/03/27/09/49/121118.jpg',  # NOQA
                                   'https://www.youtube.com/watch?v=2DMpqplvADQ')  # NOQA

# creating list of movie
movies = [dose_dupla,
          homem_aranha,
          vingadores_guerra_infinita,
          deadpool,
          logan,
          velozes_e_furiosos_8,
          ]

# call function for create page
fresh_tomatoes.open_movies_page(movies)
