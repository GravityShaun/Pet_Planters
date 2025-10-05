<template>
    


    <div class="reflectinBox">

        <div class="paperOverlay"></div>


        <div class="main_title_phone vhsFont" data-split-title='{ "stagger": 0.05, "duration": 1,  "start": "top bottom"}'>When you quiet the noise,<br>What remains is signal.</div>


                        
        <div class="reflectionGrid">
                        <CardsReflectionTitltPhone/>
                  

                        <div class="text_side" data-speed="0.95">

                           <h1 class="title">HAVEN</h1>
                    
                        <div data-speed="0.975">
                        <p class="text" data-split-text='{"start": "top bottom", "duration": 0.7}'>
                            Haven is a social experiment that allows you to connect with people in your local area. It's a way to meet new people, make new friends, and explore your city. Haven is about authentically connecting with people in a way that is serendipitous and human.
                        </p>

                        <div class="flexButtons">
                        <RetroGradient :text="'Apple Store'"/>
                        <RetroGradient :text="'Play Store'"/>
                        </div>
                        </div>
                </div>
            </div>
        </div>





</template>

<script setup>

const { splitText} = useAnimations()


</script>



<style scoped>




.reflectinBox{
            position: relative;
            margin-top:0vh;
            z-index:0;
            padding:15vh 0vh;
            width:100vw;
            background-color: #fff;
        }
      
    
    .main_title_phone{
        margin-left:10%;
        margin-top:0%;
        color:#1d1d1dd5;
        font-size:6.25rem;
        white-space: nowrap;
        line-height:1.25
    }

    .reflectionGrid{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
        padding-top:20vh
    }

    .title{
        color:#1ebf74;
        font-size:350%;
        padding-top:10%
    }

    .text{
        color:#1d1d1d;
        padding-top:9%;
        line-height:1.5;
        font-size:140%;
        font-weight:400;
        width:100%
    }

    .text_side{
        margin-left:0%;
        margin-top:10%
    }

    .flexButtons{
        display: flex;
        gap: 10%;
        margin-top:10%
    }




    @media only screen and (min-width: 0px) and (max-width: 376px) {

        .main_title_phone{
        font-size:4rem;
    }


    .text{
        line-height:1.5;
        font-size:100%;
        width:100%;
        text-align: justify;
    }

    .reflectionGrid{
        padding-top:10vh
    }

    .flexButtons{
        gap: 10vw;
        margin-top:20%;
        flex-direction: column;
    }

    .reflectionGrid{
        grid-template-columns: 1fr;
        grid-template-rows:  repeat(2, 1fr);
    }

    .text_side{
        margin-left:0%;
        margin-top:-30%
    }

}
  
@media only screen and (min-width: 376px) and (max-width: 576px) {
    .main_title_phone{
        font-size:4rem;
    }


    .text{
        line-height:1.5;
        font-size:105%;
        width:100%;
        text-align: justify;
    }

    .reflectionGrid{
        padding-top:10vh
    }

    .flexButtons{
        gap: 4vw;
        margin-top:20%;
        flex-direction: column;
    }

    .reflectionGrid{
        grid-template-columns: 1fr;
        grid-template-rows:  repeat(2, 1fr);
    }

    .text_side{
        margin-left:0%;
        margin-top:-5%
    }

}

@media only screen and (min-width: 576px) and (max-width: 768px) {
    .main_title_phone{
        font-size:4rem;
    }


    .text{
        line-height:1.5;
        font-size:115%;
        width:100%;
        text-align: justify;
    }

    .reflectionGrid{
        padding-top:10vh
    }

    .flexButtons{
        gap: 4vw;
        margin-top:20%;
        flex-direction: column;
    }

    .reflectionGrid{
        grid-template-columns: 1fr;
        grid-template-rows:  repeat(2, 1fr);
    }

    .text_side{
        margin-left:0%;
        margin-top:0%
    }

}

@media only screen and (min-width: 768px) and (max-width: 900px) {

    .main_title_phone{
        font-size:4rem;
    }


    .text{
        line-height:1.5;
        font-size:115%;
        width:100%;
        text-align: justify;
    }

    .reflectionGrid{
        padding-top:10vh
    }

    .flexButtons{
        gap: 4vw;
        margin-top:20%;
        flex-direction: column;
    }

    .reflectionGrid{
        grid-template-columns: 1fr;
        grid-template-rows:  repeat(2, 1fr);
    }

    .text_side{
        margin-left:0%;
        margin-top:5%
    }

}

@media only screen and (min-width: 900px) and (max-width: 1200px) {
    .text{
        line-height:1.5;
        font-size:115%;
        width:100%;
        text-align: justify;
    }
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}


@media only screen and (min-width: 1600px) and (max-width: 2000px) {
}

@media only screen and (min-width: 2000px) and (max-width: 2500px) {
}

@media only screen and (min-width: 2500px) and (max-width: 5600px) {
}



</style>

