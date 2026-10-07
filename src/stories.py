# ---- Stories: real posts from Word drafts (ID 0001) ----
import json as _json, re as _re2
def _a(u,t): return '<a class="post-link" href="%s" target="_blank" rel="noopener noreferrer">%s</a>'%(u,t)
def _img(src,alt,cls='post-fig'): return '<figure class="%s"><img src="assets/%s" alt="%s" loading="lazy"></figure>'%(cls,src,alt)
def _pair(): return '<div class="post-fig-row"><img src="assets/story-0001-minecraft.png" alt="Minecraft logo" loading="lazy"><img src="assets/story-0001-gd.png" alt="Geometry Dash logo" loading="lazy"></div>'
def _p(t): return '<p>%s</p>'%t
def _q(t): return '<p class="post-quote">%s</p>'%t
def _hl(t): return '<h3 class="post-hl">%s</h3>'%t
def _lead(t): return '<p class="post-lead">%s</p>'%t
def build(T):
    L=T['L']; o=[]
    o.append(_p(T['p1'])); o.append(_p(T['p2']))
    o.append(_img('story-0001-hexacube.png','Hexacube logo','post-fig post-fig-logo'))
    o += [_p(T['p3']),_p(T['p4']),_p(T['p5']),_pair(),_p(T['p6']),_p(T['p7']),_p(T['p8']),_p(T['p9'])]
    o += [_q(T['q1']),_q(T['q2']),_q(T['q3']),_p(T['p10']),_p(T['p11'].replace('{A}',_a('https://x.com/bbbbb_old',T['a1']))),_p(T['p12']),_p(T['p13']),_p(T['p14'])]
    o += [_lead(T['n1']),_hl(T['h1']),_p(T['p15'])]
    o += [_lead(T['n2']),_hl(T['h2']),_p(T['p16']),_p(T['p17'].replace('{A}',_a('https://x.com/___youkun___','you'))),_p(T['p18'])]
    o += [_lead(T['n3']),_hl(T['h3']),_p(T['p19']),_p(T['p20']),_img('joker-mark.jpg','COPYRiGHT JOKER logo','post-fig post-fig-joker'),_p(T['p21']),_p(T['p22']),_p(T['p23'])]
    return ''.join(o).replace('SANY-ON',_a('https://x.com/sany_on_','SANY-ON'))
KR=dict(
p1='작곡 활동에 있어서 활동 명의를 짓는 것은 참 중요하다고 생각합니다.',
p2='저는 <b>“Hexacube”</b>라는 닉네임을, 초등학교 4학년 때부터 써 왔었던 걸로 기억합니다. 제 기억이 맞다면요. 음… 제가 작곡 활동을 2021년, 그러니까 고1 때부터 시작했으니, 그보다도 훨씬 전이라고 할 수 있죠.',
p3='<b>여러분은 제 곡을 들으면서, 이 명의가 어디에서 왔는지 궁금하신 적이 있나요?</b> 간혹 나오는 질문입니다. 뭔가 Hexa라는 키워드랑 cube라는 단어 자체가 잘 어울리기 때문에, 브랜딩을 애초부터 이런 식으로 할 걸 예상하고 고차원적으로 지은 거라고 예상하시는 분들이 많더라고요. 예를 들어 “Cube”를 생각한 뒤, 거기에 어울리는 접두어 중에서 Hexa가 나왔다던가, 하는 식으로요.',
p4='하지만, 실상은 전혀 관련 없습니다. 애초에 음악 활동을 할 걸 상정하고 만든 명의가 아니라는 건, 맨 위 문단에서 증명을 했죠.',
p5='디스코드나 트위터에서는 몇 번 얘기한 적 있습니다만, 알고 보면 그 계기가 정말 별거 아닙니다. 사실 한국 초등학생의 국룰 게임들로부터 시작된 아주 초딩스러운 이름이거든요.',
p6='이 두 게임입니다.',
p7='10년 전, 그러니까 제가 초등학생일 즈음에 한창 유행해서 누구나 하던 게임들입니다. 저 역시 그랬고요.',
p8='따지고 보면 둘 다 큐브랑 관련이 깊은 게임이잖아요? 그래서 여기까지 들으신 분들은 그래도 뭔가 그럴싸한 계기가 있겠구나! 하는 생각을 하실 겁니다.',
p9='하지만 결론적으로 유래를 설명하자면, 정말 아무도 안 궁금해할 것 같은 TMI가 나오는데…',
q1='<em>당시 Geometry Dash에서 열심히 하고 있던 맵 “Hexagon Force”에서 “Hexa”를 따옴.</em>',
q2='<em>당시 가장 친했던 단짝 친구와 함께 Minecraft를 열심히 했었는데, 게임을 처음 사고 이름을 지을 때 그 친구의 닉네임에 있던 “cube”를 따옴.</em>',
q3='<em>그렇게 해서 짜잔, “Hexacube”의 탄생입니다.</em>',
p10='결국 둘 다 큐브랑은 전혀 관련도 없었습니다. 풀고 보니 정말 초라하죠?',
p11='사실 이번에 리브랜딩을 준비하면서, {A}분이 디자인에 참고하기 위해 ‘Hexacube’의 이름에 특별한 의미가 있는지를 여쭤보셨었습니다. 거기에 대해 뭔가 말해드리고 싶었는데, 정말 할 말이 아무것도 없더라고요. 진짜 그냥 이렇게 우연히 지어진 이름이니까요. 그래서 위 계기를 설명해드리면서 저 스스로도 너무 초딩 같아서 조금 쪽팔렸던 기억이 있네요 ㅋㅋㅋ 이제 이 글도 썼으니까 앞으로는 안 말하고 다녀야겠다…',a1='로고 디자이너',
p12='근데 사실 어떻게 생각해보면 뭐 닉네임이라는 게 다 그렇지 않나 싶습니다. 여러분들도 이메일 어릴 때 아무 생각 없이 지은 거 그대로 쓰고 있는 분들 많으시잖아요? 그런 거죠. 저 같은 경우에는, 그게 잘 얻어걸린 거라고 생각합니다.',
p13='이것만 설명하고 글을 끝내기엔 너무 초라하다고 생각하기에, 명의에 대해 제가 가지고 있는 생각들을 조금 풀어보려고 합니다.',
p14='저 같은 경우에는 이 명의를 작곡 활동에서도 그대로 쓸 수 있었던 게, 제가 활동 명의에 대해서 가지고 있는 세 가지 신념을 만족했기 때문입니다. 아래에 나오는 것들은 제 주관적인 생각이며, 일반적인 기준이나 의견을 대변하지는 않습니다.',
n1='첫 번째는,',h1='명의는 읽기 쉬워야 한다!',
p15='입니다.<br>제 명의를 생각해보면, 4음절로 정확히 딱 떨어지죠. 영어로, 한국어로, 일본어로 읽어도 깔끔한 데다가 발음하는 맛까지 있다고 생각합니다. 아직까지 S3RL을 “에스삼알엘”로 읽고 있는 제 입장에서는 명의의 중요성이 클 수밖에 없죠.',
n2='두 번째는,',h2='명의는 다른 단어 / 유명한 고유명사와 안 겹쳐야 한다!',
p16='입니다.<br>제가 정말 좋아하는 Happy Hardcore / J-core 아티스트 한 명의 케이스를 소개해볼까 합니다. Smile Diary, Let’s Jump!, Toys Crown 등등 이쪽 음악에서 교과서처럼 소개되는 음악들을 십수 년간 써오신 분이시죠. 또한 퓨처 베이스나 카와이 뮤직, 보컬곡도 너무 잘 쓰시는 분이라 인지도가 높으십니다.',
p17='이분의 명의는 {A}입니다.',
p18='…제가 어떤 말을 할 지 눈치채셨으리라 생각합니다. 디깅하는 데 정말 힘들었던 기억이 있습니다. 이 분을 너무 존경하지만, 이 분을 보면서 또 배웠던 것은 명의만큼은 눈에 띄게 지어야겠다고 생각했었습니다… 뭐… 결국에 완전히 안 겹치는 건 힘들긴 합니다. 저 같은 경우에는 메이플스토리 아이템이나 싱가포르의 어떤 쇼핑몰이랑도 겹치더라고요. 예상치 못한 부분이지만, 그래도 지금은 검색하면 제가 제일 상단에 뜨기 때문에 괜찮습니다.',
n3='세 번째는,',h3='명의는 오래 써야 한다!',
p19='입니다.<br>오래 써야 그만큼 데이터도 쌓이고, 검색량도 늘어나고… 무엇보다 사람들의 기억에 쉽게 남기 때문인 것 같습니다. 사실 이건 Hexacube라는 명의를 정한 이유라기보다는 아직까지 이 명의를 고집하고 있는 가장 큰 이유입니다.',
p20='COPYRiGHT JOKER라는 새 명의를 만들 때도 아주 고민을 많이 했던 게 바로 이 이유였습니다. 하지만, 이 명의로도 계속해서 활동을 이어나가려고 합니다. 사실 하이퍼플립 만들 때 쓰는 명의도 분리하고 싶었는데, 일본에 초대까지 받아버린 지금 시점에서 바꾸기에는 너무 늦은 감이 있기에 그냥 그대로 하려고 합니다 ㅋㅋㅋ',
p21='참고로 COPYRiGHT JOKER라는 명의가 생기게 된 배경에는 제대로 음악적인 이유가 있는데요. 그야 당연히 음악을 시작하고 난 뒤에 지은 명의니까 그렇습니다. 먼저는, SANY-ON님의 샘플링 뮤직용 부명의 DENPA-SAMPLER를 참고하였습니다. 제가 추후 부명의를 활용할 방식이 딱 이 분이 쓰는 방식이었기 때문입니다. 그 후, 이쪽 음악에서 유명한 프레이즈 “Sampling Is God, Copyright Is Joke”에서 힌트를 얻어 탄생하게 되었습니다. 물론 명의 처음 만들고 나서는 이상한 음악만 했었지만 앞으로는 제대로 샘플링 뮤직을 하기 위해 활용해볼 예정입니다. 오래 쓰면, 사람들의 기억에 남겠죠!',
p22='사실 이 글은 사이트 브랜딩을 하고 뭔가 글이 하나라도 있어야 하지 않을까 싶어서 쓴 글인데, 생각보다 하고 싶은 말들을 쓰다 보니 길어졌군요.',
p23='앞으로도 가끔 글을 쓰고 싶을 때 이런 식으로 이야기를 풀어보고자 합니다. 앞으로의 활동에도, 많은 관심 부탁드립니다!',
L='kr')
EN=dict(
p1='I think picking an artist name is a really important part of making music.',
p2='As far as I remember, I\'ve been using the nickname <b>“Hexacube”</b> since 4th grade of elementary school. If my memory serves me right, anyway. Hmm… I started composing in 2021, my first year of high school, so this name goes back way before that.',
p3='<b>Have you ever wondered where this name came from while listening to my tracks?</b> It\'s a question I get every now and then. Since “Hexa” and “cube” go so well together, a lot of you seem to assume I planned the branding from the start and came up with it in some very clever way. Like, I thought of “Cube” first and then picked Hexa out of the prefixes that fit, or something like that.',
p4='But the truth is, it has nothing to do with that. As I proved in the very first paragraph, it\'s not a name I made up with a music career in mind.',
p5='I\'ve mentioned it a few times on Discord and Twitter, but the story behind it really is nothing special. It\'s a super elementary-schooler kind of name that came from the games every Korean kid played back then.',
p6='These two games.',
p7='Ten years ago, around when I was in elementary school, they were all the rage and everybody played them. Me too, of course.',
p8='Come to think of it, both of them are deeply tied to cubes, right? So those of you who\'ve read this far are probably thinking, “Okay, there must be a pretty decent reason behind it!”',
p9='But to explain where the name actually came from, here comes some TMI that probably nobody is curious about…',
q1='<em>I took “Hexa” from “Hexagon Force,” a map I was grinding away at in Geometry Dash back then.</em>',
q2='<em>I was playing Minecraft a lot with my closest best friend at the time, and when I bought the game and had to pick a name, I took “cube” from that friend\'s nickname.</em>',
q3='<em>And ta-da, that\'s how “Hexacube” was born.</em>',
p10='In the end, neither of them had anything to do with cubes. Pretty underwhelming once you know the answer, right?',
p11='Actually, while I was preparing this rebranding, the {A} asked me whether the name “Hexacube” has any special meaning, so they could use it as a reference for the design. I wanted to tell them something, but I really had nothing to say. It\'s just a name that happened to get made up by chance. So while explaining the story above, I felt kind of embarrassed at how childish it sounded lol Now that I\'ve written this post, I guess I can stop telling people about it…',a1='logo designer',
p12='But then again, isn\'t that how nicknames are in general? A lot of you are probably still using an email address you made up without thinking when you were little, right? Same thing. In my case, I think it just happened to work out really well.',
p13='Ending the post with just this feels too underwhelming, so I\'d like to share a few of my thoughts on artist names.',
p14='The reason I could keep using this name for my music is that it satisfied the three beliefs I hold about artist names. Everything below is just my personal opinion and doesn\'t speak for any general standard or opinion.',
n1='The first one is,',h1='An artist name should be easy to read!',
p15='That\'s the first one.<br>Take mine: in Korean it\'s exactly 4 syllables (헥-사-큐-브). It reads cleanly in English, Korean, and Japanese, and I think it\'s even satisfying to say. As someone who still reads S3RL as “es-sam-al-el” (Korean style, and yes, that\'s wrong), I can\'t help but feel how much a name matters.',
n2='The second one is,',h2='An artist name shouldn\'t overlap with other words / famous proper nouns!',
p16='That\'s the second one.<br>Let me introduce the case of one Happy Hardcore / J-core artist I really love. They\'ve been writing the kind of music that gets introduced as textbook examples of this scene for over a decade, like Smile Diary, Let\'s Jump!, and Toys Crown. They\'re also amazing at future bass, kawaii music, and vocal tracks, so they\'re very well known.',
p17='This artist\'s name is {A}.',
p18='…I think you can guess what I\'m going to say. Digging for their stuff was really hard. I respect this person a lot, but what I learned from watching them was that I should make my own name stand out, at the very least… Well… in the end, never overlapping at all is tough. In my case, I overlap with a MapleStory item and some shopping mall in Singapore. Totally unexpected, but I\'m at the top when you search for it now, so it\'s fine.',
n3='The third one is,',h3='An artist name should be used for a long time!',
p19='That\'s the third one.<br>The longer you use it, the more data piles up, the more search volume grows… and above all, people remember it more easily, I think. Actually, this isn\'t so much the reason I picked the name Hexacube as the biggest reason I\'m still sticking with it.',
p20='This was exactly why I agonized so much when I created a new name, COPYRiGHT JOKER. But I plan to keep going under this name too. Actually, I wanted to separate the name I use for HYPERFLIP as well, but now that I\'ve even been invited to Japan, it feels too late to change it, so I\'ll just leave it as is lol',
p21='By the way, COPYRiGHT JOKER has a proper musical reason behind it. Of course it does, since I came up with it after I started making music. First, I referenced DENPA-SAMPLER, SANY-ON\'s sub-alias for sampling music, because the way I planned to use a sub-alias was exactly how they use theirs. After that, I got a hint from the famous phrase in this scene, “Sampling Is God, Copyright Is Joke,” and that\'s how it was born. Sure, I\'ve only made weird music since first creating the name, but from now on I plan to use it to make proper sampling music. If I use it for long enough, people will remember it!',
p22='I wrote this post because I felt like the site needed at least one post after the rebranding, but as I wrote, it got longer than I expected.',
p23='I\'d like to keep telling stories like this whenever I feel like writing. Thank you for your continued support of my work!',
L='en')
JP=dict(
p1='作曲活動をするうえで、活動名義を決めることはとても大事だと思っています。',
p2='僕は<b>「Hexacube」</b>というニックネームを、小学4年生の頃から使ってきたと記憶しています。僕の記憶が合っていれば、ですが。うーん…。作曲活動を始めたのが2021年、つまり高1の頃なので、それよりもずっと前ということになりますね。',
p3='<b>皆さんは僕の曲を聴きながら、この名義がどこから来たのか気になったことはありますか?</b> たまに聞かれる質問です。Hexaというキーワードとcubeという単語がよく合っているので、最初からブランディングを想定して、かなり練って付けた名前だと思う方が多いみたいなんですよね。例えば「Cube」を先に思いついて、それに合う接頭辞の中からHexaが出てきた、みたいな感じで。',
p4='でも、実際は全然関係ありません。そもそも音楽活動をする前提で作った名義ではない、ということは、一番上の段落で証明しましたよね。',
p5='DiscordやTwitterでは何度かお話ししたことがあるんですが、実はきっかけは本当に大したことないんです。韓国の小学生なら誰もがやっていた定番ゲームから始まった、すごく小学生っぽい名前なんですよ。',
p6='この2つのゲームです。',
p7='10年前、ちょうど僕が小学生だった頃に大流行して、みんながやっていたゲームです。僕もそうでした。',
p8='考えてみると、どちらもキューブとの関わりが深いゲームですよね? なので、ここまで読んでくださった方は「それなりにそれっぽいきっかけがあるんだな!」と思われるはずです。',
p9='ですが、結論から由来を説明すると、たぶん誰も気にならないであろうTMIが出てきます…',
q1='<em>当時Geometry Dashで夢中になって遊んでいたマップ「Hexagon Force」から「Hexa」をもらった。</em>',
q2='<em>当時いちばん仲の良かった親友と一緒にMinecraftにハマっていて、ゲームを初めて買って名前を付けるときに、その友達のニックネームにあった「cube」をもらった。</em>',
q3='<em>そうして、じゃじゃーん、「Hexacube」の誕生です。</em>',
p10='結局、どちらもキューブとは全く関係なかったわけです。種明かしをしてみると、本当にしょぼいですよね?',
p11='実は今回のリブランディングを準備するときに、{A}の方が、デザインの参考にするために「Hexacube」という名前に特別な意味があるのかを聞いてくださったんです。何か答えたかったのですが、本当に言えることが何もなくて。ただ偶然こうして付けた名前ですからね。それで上のきっかけを説明しながら、自分でもあまりに小学生っぽくて、ちょっと恥ずかしかったのを覚えています(笑) この文章も書いたので、これからはもう言わないようにしようと思います…',a1='ロゴデザイナー',
p12='でも、よく考えると、ニックネームなんてだいたいそういうものじゃないでしょうか。皆さんも、子どもの頃に何も考えずに作ったメールアドレスをそのまま使っている方、多いですよね? そういうことです。僕の場合は、それがうまく当たったんだと思います。',
p13='これだけ説明して終わるのはあまりにも寂しいので、名義について僕が持っている考えを少しお話ししようと思います。',
p14='僕がこの名義を作曲活動でもそのまま使えたのは、活動名義について持っている3つの信念を満たしていたからです。以下に出てくるのは僕の主観的な考えであり、一般的な基準や意見を代弁するものではありません。',
n1='1つ目は、',h1='名義は読みやすくあるべし!',
p15='です。<br>僕の名義は、韓国語で読むとちょうど4音節(헥-사-큐-브)に収まっていますよね。英語でも、韓国語でも、日本語でも読みやすいうえに、発音したときの気持ちよさもあると思っています。いまだにS3RLを韓国語で「エスサムアルエル」と読んでいる僕としては、名義の大切さを実感せずにはいられません。',
n2='2つ目は、',h2='名義は他の単語 / 有名な固有名詞と被ってはいけない!',
p16='です。<br>僕が大好きなHappy Hardcore / J-coreアーティストの一人の例を紹介したいと思います。Smile Diary、Let’s Jump!、Toys Crownなど、このジャンルで教科書のように紹介される曲を十数年にわたって作ってこられた方です。さらにフューチャーベースやカワイイ音楽、ボーカル曲もとてもお上手で、知名度の高い方でもあります。',
p17='この方の名義は{A}です。',
p18='…僕が何を言いたいか、もうお察しかと思います。掘るのが本当に大変だった記憶があります。この方のことはとても尊敬していますが、この方を見て学んだのは、名義だけは目立つように付けようということでした…。まあ、完全に被らないようにするのは結局難しいんですけどね。僕の場合は、メイプルストーリーのアイテムや、シンガポールのあるショッピングモールとも被っていました。予想外でしたが、今は検索すると僕が一番上に出てくるので大丈夫です。',
n3='3つ目は、',h3='名義は長く使うべし!',
p19='です。<br>長く使うほどデータも溜まり、検索数も増え…何より、人の記憶に残りやすいからだと思います。実はこれはHexacubeという名義を決めた理由というより、今でもこの名義にこだわっている一番の理由です。',
p20='COPYRiGHT JOKERという新しい名義を作るときにも、まさにこの理由ですごく悩みました。でも、この名義でもこれから活動を続けていこうと思っています。実はHYPERFLIPを作るときに使う名義も分けたかったのですが、日本に招待までしていただいた今の時点で変えるのは遅すぎる気がするので、このままいこうと思います(笑)',
p21='ちなみに、COPYRiGHT JOKERという名義が生まれた背景には、ちゃんとした音楽的な理由があります。そりゃそうです、音楽を始めた後に付けた名義ですから。まず、SANY-ONさんのサンプリング音楽用サブ名義であるDENPA-SAMPLERを参考にしました。僕が今後サブ名義を使う方法が、まさにこの方の使い方だったからです。その後、このジャンルで有名なフレーズ「Sampling Is God, Copyright Is Joke」からヒントを得て誕生しました。もちろん、名義を作ってから今まで変な音楽ばかり作ってきましたが、これからはちゃんとしたサンプリング音楽をやるために活用していく予定です。長く使えば、人の記憶に残りますよね!',
p22='実はこの文章は、サイトのブランディングをして、何か記事が一つくらいはあったほうがいいかなと思って書いたのですが、思ったより書きたいことが多くて長くなってしまいました。',
p23='これからも、書きたくなったときにこんな感じでお話ししていこうと思います。今後の活動にも、ぜひご注目ください!',
L='jp')
POSTS={'kr':build(KR),'en':build(EN),'jp':build(JP)}
TITLE={'kr':'명의를 가지게 된 계기와 생각','en':'How I got my artist name, and what I think about it','jp':'名義を持つようになったきっかけと考え'}
SUM={'kr':'"Hexacube"라는 이름은 어디에서 왔을까?','en':'Where did the name “Hexacube” come from?','jp':'「Hexacube」という名前はどこから来たのか?'}
J=lambda o:_json.dumps(o,ensure_ascii=False)
card='''<article class="post-card" data-post="0001" tabindex="0" role="button">
              <div class="post-thumb"><img src="assets/story-0001-thumb.jpg" alt="Hexacube logo"></div>
              <div class="post-body">
                <span class="post-date">2026.10.07</span>
                <h3 class="i18n" data-kr=%s data-en=%s data-jp=%s></h3>
                <p class="i18n" data-kr=%s data-en=%s data-jp=%s></p>
                <span class="read-more"><span class="i18n" data-kr="더 보기" data-en="Read more" data-jp="続きを読む"></span> &rarr;</span>
              </div>
            </article>'''%tuple(_json.dumps(x[k],ensure_ascii=False) if False else '"%s"'%x[k].replace('&','&amp;').replace('"','&quot;') for x in (TITLE,SUM) for k in ('kr','en','jp'))
# replace the 3 sample cards
a=body.index('<article class="post-card" data-post="music-1"'); b=body.index('</div>\n          <div class="detail-view post-detail">')
body=body[:a]+card+'\n          '+body[b:]
# replace postsData / postOrder
a=body.index('  var postsData = {'); b=body.index("  var postOrder = { 'story':['music-1','dj-1','music-2'] };")+len("  var postOrder = { 'story':['music-1','dj-1','music-2'] };")
body=body[:a]+"  var postsData = {\n    '0001': { group:'story', date:'2026.10.07', title:%s, body:%s }\n  };\n  var postOrder = { 'story':['0001'] };"%(J(TITLE),J(POSTS))+body[b:]
# page-desc
KRD='작곡, 디제잉 등 다양한 면에 있어서 쓰고 싶었던 비하인드 스토리들을 블로그처럼 글로 모아놨습니다.'
ENX='A blog-style collection of behind-the-scenes stories I wanted to share, about composing, DJing, and everything in between. The translations of these posts were written with AI, so they may contain inaccuracies. Thank you for your understanding.'
JPX='作曲やDJなど、様々な面で書き残しておきたかった裏話をブログのような形でまとめています。記事の翻訳はAIで作成されているため、不正確な部分がある可能性があります。ご理解のほどよろしくお願いいたします。'
_m=_re2.search(r'(<p class="page-desc i18n" data-kr=")작곡, 디제잉[^>]*(>)',body); assert _m
body=body[:_m.start()]+'<p class="page-desc i18n" data-kr="%s" data-en="%s" data-jp="%s">'%(KRD,ENX,JPX)+body[_m.end():]
# CSS
CSS='''
  .post-thumb img{background:#fff;}
  .detail-body .post-fig{margin:22px auto;text-align:center;}
  .detail-body .post-fig img{max-width:100%;height:auto;display:inline-block;}
  .detail-body .post-fig-logo img{width:min(100%,480px);}
  .detail-body .post-fig-joker img{width:clamp(130px,26vw,190px);mix-blend-mode:multiply;}
  .detail-body .post-fig-row{display:flex;gap:18px;align-items:center;justify-content:center;margin:22px auto;max-width:65ch;}
  .detail-body .post-fig-row img{flex:1 1 0;min-width:0;max-width:100%;height:auto;}
  @media (max-width:480px){.detail-body .post-fig-row{flex-direction:column;gap:14px;}.detail-body .post-fig-row img{flex:none;width:86%;}}
  .detail-body .post-quote{max-width:none;margin:0 auto 10px;}
  .detail-body .post-lead{margin:26px 0 4px;}
  .detail-body .post-hl{font-size:clamp(19px,3.4vw,23px);font-weight:800;text-align:center;color:var(--ink);margin:6px 0 10px;line-height:1.4;}
  .post-detail .detail-body p{max-width:none;text-align:justify;word-break:keep-all;overflow-wrap:break-word;}
  .post-detail .detail-body p.post-quote{text-align:center;}
  .detail-body .post-fig-row{max-width:760px;}
  .detail-body .post-link{color:var(--accent-deep);font-weight:600;text-decoration:underline;text-underline-offset:2px;}
  .detail-body .post-link:hover{opacity:.75;}
'''
R('  .detail-title{font-size:26px;}',CSS+'  .detail-title{font-size:26px;}')
R('  .detail-title{font-size:26px;}','  #app.joker-theme .party-card,#app.joker-theme .detail-view{--meta-date:#0e8f84;--meta-venue:#3366cc;--meta-genre:#b45309;}\n  .detail-title{font-size:26px;}')
