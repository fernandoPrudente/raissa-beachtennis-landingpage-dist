from pathlib import Path


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f"Pattern not found for {label}")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Pattern not unique for {label}: {count}")
    return text.replace(old, new, 1)


# HOME
path = Path("index.html")
html = path.read_text(encoding="utf-8")

html = replace_once(
    html,
    'content="Aulas de Beach Tennis em Belo Horizonte, Ribeirão das Neves e região com a professora Raissa. Aulas coletivas, particulares e atendimento para donos de quadra."',
    'content="Aulas de Beach Tennis em Belo Horizonte, Ribeirão das Neves e região com a professora Raissa. Para quem busca professor ou professora de Beach Tennis, com aulas coletivas, particulares e atendimento para quadras."',
    "home meta description",
)

html = replace_once(
    html,
    '''            <h2
              class="text-3xl font-black tracking-tight text-slate-950 sm:text-5xl"
            >
              Aulas de Beach Tennis para cada momento do seu jogo
            </h2>

            <p class="mt-5 text-lg leading-8 text-slate-700">
              Da primeira aula à rotina de treino, escolha o formato ideal com a
              professora Raissa.
            </p>''',
    '''            <h2
              class="text-3xl font-black tracking-tight text-slate-950 sm:text-5xl"
            >
              Procura professor ou professora de Beach Tennis? Veja as opções de aula
            </h2>

            <p class="mt-5 text-lg leading-8 text-slate-700">
              Se você chegou procurando professor de Beach Tennis em Belo Horizonte
              ou região, conheça os formatos de aula e treinamento oferecidos pela
              professora Raissa, do primeiro contato à evolução técnica.
            </p>''',
    "home services heading",
)

html = replace_once(
    html,
    '''              <h3 class="text-2xl font-black text-white">
                Para donos de quadra
              </h3>

              <p class="mt-4 leading-7 text-white/80">
                Atendimento para quadras que precisam de uma professora para
                aulas, turmas, eventos, captação e fidelização de alunos.
              </p>''',
    '''              <h3 class="text-2xl font-black text-white">
                Professor de Beach Tennis para sua quadra
              </h3>

              <p class="mt-4 leading-7 text-white/80">
                Para donos e gestores que procuram professor ou professora de Beach
                Tennis para aulas, turmas, eventos, captação e fidelização de alunos,
                a Raissa oferece atendimento profissional para o espaço.
              </p>''',
    "home court owners card",
)

html = replace_once(
    html,
    "                Sua quadra fica na Pampulha? Conheça o atendimento →",
    "                Professor de Beach Tennis na Pampulha para sua quadra →",
    "home Pampulha anchor",
)

html = replace_once(
    html,
    '''                clubes e arenas que procuram uma professora especialista para
                aulas e treinamentos. O atendimento também pode alcançar outros''',
    '''                clubes e arenas que procuram professor ou professora de Beach
                Tennis para aulas e treinamentos. O atendimento também pode alcançar outros''',
    "home regional card copy",
)

path.write_text(html, encoding="utf-8")


# ABOUT
path = Path("sobre-raissa-carvalho.html")
html = path.read_text(encoding="utf-8")

html = replace_once(
    html,
    'content="Conheça Raíssa Carvalho Barbosa, professora e atleta de Beach Tennis em Belo Horizonte. Veja sua trajetória competitiva, capacitações, metodologia e experiência em quadra."',
    'content="Conheça Raíssa Carvalho Barbosa, professora e atleta de Beach Tennis em Belo Horizonte. Para quem busca professor ou professora de Beach Tennis, veja sua trajetória, metodologia, capacitações e experiência em quadra."',
    "about meta description",
)

html = replace_once(
    html,
    '''            <p class="mt-6 text-lg leading-8 text-slate-700">
              A professora Raíssa oferece aulas de Beach Tennis para alunos
              iniciantes, intermediários e praticantes que querem evoluir
              fundamentos, movimentação, leitura de jogo e consistência na
              quadra.
            </p>

            <p class="mt-4 text-lg leading-8 text-slate-700">
              Além da atuação como professora, mantém uma trajetória competitiva''',
    '''            <p class="mt-6 text-lg leading-8 text-slate-700">
              A professora Raíssa oferece aulas de Beach Tennis para alunos
              iniciantes, intermediários e praticantes que querem evoluir
              fundamentos, movimentação, leitura de jogo e consistência na
              quadra.
            </p>

            <p class="mt-4 text-lg leading-8 text-slate-700">
              Para quem pesquisa por professor de Beach Tennis em Belo Horizonte
              e região, o atendimento é realizado pela professora Raíssa Carvalho,
              com treinos adaptados ao nível, ao objetivo e ao formato de cada aluno
              ou grupo.
            </p>

            <p class="mt-4 text-lg leading-8 text-slate-700">
              Além da atuação como professora, mantém uma trajetória competitiva''',
    "about visible professor query paragraph",
)

html = html.replace("553193281642", "5531993281642")
path.write_text(html, encoding="utf-8")


# PAMPULHA
path = Path("aulas-beach-tennis-pampulha.html")
html = path.read_text(encoding="utf-8")

html = replace_once(
    html,
    'content="Professora de Beach Tennis na Pampulha para aulas e treinamentos em quadras, condomínios, clubes e arenas, com atendimento também em outros bairros da região da Pampulha e áreas próximas, conforme agenda."',
    'content="Professora de Beach Tennis na Pampulha para quem busca professor ou professora de Beach Tennis para aulas e treinamentos em quadras, condomínios, clubes e arenas, inclusive em bairros próximos, conforme agenda."',
    "Pampulha meta description",
)

html = replace_once(
    html,
    '            "description": "Aulas e treinamentos de Beach Tennis na região da Pampulha para alunos que já possuem uma quadra definida e para responsáveis por quadras, clubes e arenas que procuram uma professora especialista.",',
    '            "description": "Aulas e treinamentos de Beach Tennis na região da Pampulha para alunos que já possuem uma quadra definida e para responsáveis por quadras, clubes e arenas que procuram professor ou professora de Beach Tennis para o espaço.",',
    "Pampulha service structured description",
)

faq_anchor = '''              {
                "@type": "Question",
                "name": "Sou responsável por uma quadra ou arena. Posso conversar com a Raíssa sobre aulas no espaço?",
                "acceptedAnswer": {
                  "@type": "Answer",
                  "text": "Sim. Responsáveis por quadras, clubes e arenas da região da Pampulha podem consultar disponibilidade e conversar sobre formatos de aulas e treinamentos no espaço."
                }
              }'''
faq_new = '''              {
                "@type": "Question",
                "name": "Sou responsável por uma quadra ou arena. Posso conversar com a Raíssa sobre aulas no espaço?",
                "acceptedAnswer": {
                  "@type": "Answer",
                  "text": "Sim. Responsáveis por quadras, clubes e arenas da região da Pampulha podem consultar disponibilidade e conversar sobre formatos de aulas e treinamentos no espaço."
                }
              },
              {
                "@type": "Question",
                "name": "Estou procurando professor de Beach Tennis na Pampulha. A Raíssa atende?",
                "acceptedAnswer": {
                  "@type": "Answer",
                  "text": "Sim. Para quem pesquisa por professor ou professora de Beach Tennis na Pampulha, a Raíssa atende alunos, grupos e responsáveis por quadras, conforme agenda, localização e disponibilidade do espaço."
                }
              }'''
html = replace_once(html, faq_anchor, faq_new, "Pampulha FAQ structured data")

html = replace_once(
    html,
    '''              <h3 class="mt-3 text-3xl font-black text-slate-950">
                Tem uma quadra, arena ou clube e procura uma professora de referência?
              </h3>''',
    '''              <h3 class="mt-3 text-3xl font-black text-slate-950">
                Procura professor de Beach Tennis para sua quadra, arena ou clube?
              </h3>''',
    "Pampulha court owner heading",
)

visible_faq_anchor = '''            <details
              class="group rounded-[2rem] border border-amber-200 bg-white p-6 shadow-sm"
            >
              <summary
                class="cursor-pointer list-none pr-8 text-lg font-black text-slate-950"
              >
                Sou dono ou responsável por uma quadra de Beach Tennis. Posso contratar a Raíssa para atender no espaço?
              </summary>
              <p class="mt-4 leading-7 text-slate-700">
                É possível consultar disponibilidade para aulas e treinamentos no
                espaço. Envie a localização da quadra e explique o formato que procura
                para que a Raíssa avalie agenda e possibilidades de atendimento.
              </p>
            </details>'''
visible_faq_new = visible_faq_anchor + '''

            <details
              class="group rounded-[2rem] border border-cyan-100 bg-white p-6 shadow-sm"
            >
              <summary
                class="cursor-pointer list-none pr-8 text-lg font-black text-slate-950"
              >
                Estou procurando professor de Beach Tennis na Pampulha. A Raíssa atende?
              </summary>
              <p class="mt-4 leading-7 text-slate-700">
                Sim. Se você chegou pesquisando por professor ou professora de Beach
                Tennis na Pampulha, a Raíssa atende alunos, grupos e responsáveis por
                quadras, conforme agenda, localização e disponibilidade do espaço.
              </p>
            </details>'''
html = replace_once(html, visible_faq_anchor, visible_faq_new, "Pampulha visible FAQ")

path.write_text(html, encoding="utf-8")
