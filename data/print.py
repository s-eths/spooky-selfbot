import fade

def cool_text(text):
    return f"                    {fade.fire(text)}"

def output_text(text):
    return f"                    {fade.greenblue(text)}"

def login_box(text):
    return fade.fire(f"""
                    ┌────────────────────────────────────┐                                                            
                      Sucessfully logged into {text}
                    └────────────────────────────────────┘
    """)

def logo():
    return fade.fire(f"""
  
                     .x+=:.                                               ..                   
                      z`    ^%                                        < .z@8"`        ..         
                         .   <k  .d``                u.          u.    !@88E         @L          
                       .@8Ned8"  @8Ne.   .u    ...ue888b   ...ue888b   '888E   u    9888i   .dL  
                     .@^%8888"   %8888:u@88N   888R Y888r  888R Y888r   888E u@8NL  `Y888k:*888. 
                    x88:  `)8b.   `888I  888.  888R I888>  888R I888>   888E`"88*"    888E  888I 
                    8888N=*8888    888I  888I  888R I888>  888R I888>   888E .dN.     888E  888I 
                     %8"    R88    888I  888I  888R I888>  888R I888>   888E~8888     888E  888I 
                      @8Wou 9%   uW888L  888' u8888cJ888  u8888cJ888    888E '888&    888E  888I 
                    .888888P`   '*88888Nu88P   "*888*P"    "*888*P"     888E  9888.  x888N><888' 
                    `   ^"F     ~ '88888F`       'Y"         'Y"      '"888*" 4888"   "88"  888  
                                   888 ^                                 ""    ""           88F  
                                   *8E                                                     98"   
                                   '8>                                                   ./"     
                                    "                                                   ~`       

""")