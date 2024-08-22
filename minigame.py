print('''

            .        +          .      .          .
     .            _        .                    .
  ,              /;-._,-.____        ,-----.__
 ((        .    (_:#::_.:::. `-._   /:, /-._, `._,
  `                 \   _|`"=:_::.`.);  \ __/ /
                      ,    `./  \:. `.   )==-'  .
    .      ., ,-=-.  ,\, +#./`   \:.  / /           .
.           \/:/`-' , ,\ '` ` `   ): , /_  -o
       .    /:+- - + +- : :- + + -:'  /(o-) \)     .
  .      ,=':  \    ` `/` ' , , ,:' `'--".--"---._/`7
   `.   (    \: \,-._` ` + '\, ,"   _,--._,---":.__/
              \:  `  X` _| _,\/'   .-'
.               ":._:`\____  /:'  /      .           .
                    \::.  :\/:'  /              +
   .                 `.:.  /:'  }      .
           .           ):_(:;   \           .
                      /:. _/ ,  |
                   . (|::.     ,`                  .
     .                |::.    {\
                      |::.\  \ `.
                      |:::(\    |
              O       |:::/{ }  |                  (o
               )  ___/#\::`/ (O "==._____   O, (O  /`
          ~~~w/w~"~~,\` `:/,-(~`"~~~~~~~~"~o~\~/~w|/~
dew   ~~~~~~~~~~~~~~~~~~~~~~~\\W~~~~~~~~~~~~\|/~~
''')
print('''You are an intrepid explorer who has ventured into the heart of an ancient,
enchanted swamp. The dense fog wraps around you like a shroud, 
and the air is thick with the scent of decay and magic.
The swamp seems alive, whispering secrets through the rustling leaves
and eerie glow of unseen creatures. Mysterious lights flicker in the distance,
casting an otherworldly glow on the murky waters. Your only hope is to navigate
through this treacherous land and escape before the swamp's enchantments ensnare you forever.

''')

print("""
Your mission is to find your way out of this enchanted swamp.

""")
choice1 = input('''You\'re at a crossroad. \nWhere do you want to go? \ninto dark mist or follow some flickering blue lights?
                
    Type "dark mist" or "blue lights".\n''').lower()
if choice1 == "blue lights":
    choice11 = input('''You arrive at a moonlit pond, 
its surface glowing with an otherworldly light. 
The air is filled with a hauntingly beautiful ancient melody, 
whispering secrets of the swamp.
Will you follow this mystical song into the unknown?
Type "yes" to follow or "no" to go into another direction. 
                            ___ --- ___
                      .--                  --.
                    ./    ()         .-.        \.
                   /   o     .      (   )         |
                  / .                '-'           |
                 | ()    .   O            .         |
                |                                    |
                |    o               ()              |
                |       .--.              O          |
                 | .   |    |                       |
                  \    `.__.'        o   .         /
                   \                              /
                    `\  o     ()                /' 
                      `--  ___         ___  --'
                                 ---)\n''')
    if choice11 == "yes":
        print('''Drawn by the mesmerizing melody, you wade deeper into the murky swamp, 
only to find the ground treacherously soft and shifting. Without warning, you sink into a hidden pit, 
surrounded by the eerie silence that follows the fading song. 
Caught and trapped, you realize too late that the melody was a lure — you lose...
    
     ;;;;;;;;;;;;;;;;;;;         ; 
     ;;;;;;;;;;;;;;;;;;;         ;;
     ;                 ;         ;';.
     ;                 ;         ;  ;;
     ;                 ;         ;   ;;
     ;                 ;         ;    ;;
     ;                 ;         ;    ;;
     ;                 ;         ;   ;'
     ;                 ;         ;  ' 
,;;;;;            ,;;;;;    ,;;;,; 
;;;;;;            ;;;;;;    ;;;;;;
`;;;;'            `;;;;'    `;;;;'

            _,-+-._
         .-'       ''-._
        /               ';
       '        ~.        ;
      /    ~`'    ) .=" ,  )
     |           I  (   ~ (
     \        '""    `='  +
      `.,_   `";:Y0U'   *'
          `~'~.'  )_L_0_S_E!\  
          
''')
    if choice11 == "no":
        choice12 = input('''Before you stands an ancient tree. 
Its gnarled bark adorned with mystical symbols that shimmer with an otherworldly glow.
The air around it hums with ancient power, inviting you to uncover its secrets. 
Do you dare to reach out and touch these enigmatic markings?
    type "touch" or "resist".''')
        if choice12 == "touch":
            print('''As your hand touches the mystical symbols, the swamp stirs with dark energy. 
        Sinister creatures with glowing eyes and twisted forms emerge from the shadows. 
        In an instant, their ferocious attack seals your fate.
        
             _,-+-._
         .-'       ''-._
        /               ';
       '        ~.        ;
      /    ~`'    ) .=" ,  )
     |           I  (   ~ (
     \        '""    `='  +
      `.,_   `";:Y0U'   *'
          `~'~.'  )_L_0_S_E!\  
          
''')
        if choice12 == "resist":
            choice5 = input('''A swamp guardian appears. And offers you to solve a riddle.
Do you want to try? type "yes" or "no".''').lower()
            if choice5 == "yes":
                choice6 = input('''The swamp guardian whispers her riddle:
I speak without a mouth and hear without ears.
I have no body, but I come alive with wind.
What am I?''').lower()
                if choice6 == "echo":
                    print(
                        "Well done, brave soul! \nI shall guide you out of this treacherous swamp and lead you to safety. \nFollow my path, and let the light of my guidance illuminate your way to freedom and new adventures.")
                    print('''
                                                  .

                          |					
                 .               /				
                  \       I     				
                              /
                      \  _
                       d888(`   ).                   _
             -  --==  888(      ).=--           .+(`   )`.
            )         Y8P(       '`.          :(   .    )
                    .+(`(       .   )     .--  `.  (     ) )
                   ((    (..__.:'-'   .=(   )   ` _`   ) )
            `.     `(       ) )       (   .  )     (   )  ._
              )      ` __.:'   )     (   (    ))     `-'.:(`    )
            )  )  ( )       --'       `- __.'         :(        ))
            .-'  (_.'          .')                    `(    )  ))
                              (_  )                     ` __.:'

            --..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-._.--.

            Now enjoy the sun and have some icecream!

                      _.-.
                   ,'/  // )
                  ///  //  /)
                 ///  //  //|
                ///  //  ///
               ///  //  ///
              (`:  //  ///
               `;` :  ///
               /  /: `:/
              /  /  ` '
             /  /
            (_ /  


            ''')
            if choice5 == "no":
                    print('''You doubt your own strength... How tragic. \nYour lack of faith has sealed your fate. \nNow, this swamp shall be your eternal prison, where your hopes will wither and fade away, forever lost in the mists.
            _,-+-._
         .-'       ''-._
        /               ';
       '        ~.        ;
      /    ~`'    ) .=" ,  )
     |           I  (   ~ (
     \        '""    `='  +
      `.,_   `";:Y0U'   *'
          `~'~.'  )_L_0_S_E!\   
          
''')
if choice1 == "dark mist":
    choice2 = input('''In the distance you see some golden dancing lights. 
you are not sure if it is a good idea to observe them. 
    Type "go on" to follow the road.
    Type "observe" to see what they are.''').lower()
    if choice2 == "go on":
        print('''Oh no! What is happening?! You stepped into quicksand-mud. You are lost forever..."
            _,-+-._
         .-'       ''-._
        /               ';
       '        ~.        ;
      /    ~`'    ) .=" ,  )
     |           I  (   ~ (
     \        '""    `='  +
      `.,_   `";:Y0U'   *'
          `~'~.'  )_L_0_S_E!\  
                ''')
    if choice2 == "observe":
        choice3 = input('''Will-o\'the-wisps appear. Do you want to follow them?
            type "yes" to follow. 
            type "no" to go on. ''').lower()
        if choice3 == "yes":
            print("Never trust a Will-o\'-the-wisp! You follow them in endless loops.")
            print("You are lost forever...")
            print('''
             __,aaPPPPPPPPaa,__
         ,adP"""'          `""Yb,_
      ,adP'                     `"Yb,
    ,dP'     ,aadPP"""""YYba,_     `"Y,
   ,P'    ,aP"'            `""Ya,     "Y,
  ,P'    aP'     _________     `"Ya    `Yb,
 ,P'    d"    ,adP""""""""Yba,    `Y,    "Y,
,d'   ,d'   ,dP"            `Yb,   `Y,    `Y,
d'   ,d'   ,d'    ,dP""Yb,    `Y,   `Y,    `b
8    d'    d'   ,d"      "b,   `Y,   `8,    Y,
8    8     8    d'    _   `Y,   `8    `8    `b
8    8     8    8     8    `8    8     8     8
8    Y,    Y,   `b, ,aP     P    8    ,P     8
I,   `Y,   `Ya    """"     d'   ,P    d"    ,P
`Y,   `8,    `Ya         ,8"   ,P'   ,P'    d'
 `Y,   `Ya,    `Ya,,__,,d"'   ,P'   ,P"    ,P
  `Y,    `Ya,     `""""'     ,P'   ,d"    ,P'
   `Yb,    `"Ya,_          ,d"    ,P'    ,P'
     `Yb,      ""YbaaaaaadP"     ,P'    ,P'
       `Yba,                   ,d'    ,dP'
          `"Yba,__       __,adP"     dP"
              `"""""""""""""'
            _,-+-._
         .-'       ''-._
        /               ';
       '        ~.        ;
      /    ~`'    ) .=" ,  )
     |           I  (   ~ (
     \        '""    `='  +
      `.,_   `";:Y0U'   *'
          `~'~.'  )_L_0_S_E!\  
''')
        if choice3 == "no":
            print("Wise decision! Never follow a Will-o\'the-wisp!\nYou follow a road until you see a hidden path on your left.")
            choice4 = input('''Do you want to take the hidden path?
            type "yes" to take the hidden path.
            type "no" to go on.''').lower()
            if choice4 == "no":
                print('''You will only go deeper into the swamp. 
                you are lost forever...
            _,-+-._
         .-'       ''-._
        /               ';
       '        ~.        ;
      /    ~`'    ) .=" ,  )
     |           I  (   ~ (
     \        '""    `='  +
      `.,_   `";:Y0U'   *'
          `~'~.'  )_L_0_S_E!\  
          ''')
            if choice4 == "yes":
                choice5 = input('''A swamp guardian appears. And offers you to solve a riddle.
                Do you want to try? type "yes" or "no".''').lower()
                if choice5 == "yes":
                    choice6 = input('''The swamp guardian whispers her riddle:
                I speak without a mouth and hear without ears.
                I have no body, but I come alive with wind.
                Again and again...again...again...again
                What am I?''').lower()
                    if choice6 == "echo":
                        print("Well done, brave soul! \nI shall guide you out of this treacherous swamp and lead you to safety. \nFollow my path, and let the light of my guidance illuminate your way to freedom and new adventures.")
                        print('''
                                      .
               					
              |					
     .               /				
      \       I     				
                  /
          \  _
           d888(`   ).                   _
 -  --==  888(      ).=--           .+(`   )`.
)         Y8P(       '`.          :(   .    )
        .+(`(       .   )     .--  `.  (     ) )
       ((    (..__.:'-'   .=(   )   ` _`   ) )
`.     `(       ) )       (   .  )     (   )  ._
  )      ` __.:'   )     (   (    ))     `-'.:(`    )
)  )  ( )       --'       `- __.'         :(        ))
.-'  (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'
                                        	
--..,___.--,--'`,---..-.--+--.,,-,,..._.--..-._.-a:f--.

Now enjoy the sun and have some icecream!

          _.-.
       ,'/  // )
      ///  //  /)
     ///  //  //|
    ///  //  ///
   ///  //  ///
  (`:  //  ///
   `;` :  ///
   /  /: `:/
  /  /  ` '
 /  /
(_ /  


''')
                if choice5 == "no":
                    print('''You doubt your own strength... How tragic. \nYour lack of faith has sealed your fate. \nNow, this swamp shall be your eternal prison, where your hopes will wither and fade away, forever lost in the mists.
            _,-+-._
         .-'       ''-._
        /               ';
       '        ~.        ;
      /    ~`'    ) .=" ,  )
     |           I  (   ~ (
     \        '""    `='  +
      `.,_   `";:Y0U'   *'
          `~'~.'  )_L_0_S_E!\  
          ''')

