const body = document.querySelector("body"),
        searchBtn = body.querySelector(".search-box"),
        modeText = body.querySelector(".mode-text"),
        modeSwitch = body.querySelector(".toggle-switch");

        modeSwitch.addEventListener("click", () =>{
            body.classList.toggle("dark");

            if(body.classList.contains("dark")){
                modeText.innerText = "Light Mode"
            }else{
                modeText.innerText = "Dark Mode"
            }
        });

        document.querySelector('.user-menu').addEventListener('click', function () {
            this.classList.toggle('active');
        });