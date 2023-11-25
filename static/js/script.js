const body = document.querySelector("body"),
        sidebar = body.querySelector(".sidebar"),
        toggle = body.querySelector(".toggle"),
        searchBtn = body.querySelector(".search-box"),
        modeSwitch = body.querySelector(".toggle-switch"),
        modeText = body.querySelector(".mode-text");

        function toggleSidebar() {
            const screenWidth = window.innerWidth;
            if (screenWidth < 1000) {
              sidebar.classList.toggle('close');
            }
          }

        toggle.addEventListener("click", () =>{
            sidebar.classList.toggle("close");
        });

        modeSwitch.addEventListener("click", () =>{
            body.classList.toggle("dark");

            if(body.classList.contains("dark")){
                modeText.innerText = "Light Mode"
            }else{
                modeText.innerText = "Dark Mode"
            }
        });