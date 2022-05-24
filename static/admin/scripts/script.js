const search = document.querySelector('.searchbox');
const icon = document.querySelector('.search-icon');

icon.onclick=function()
{
	search.classList.toggle('active');
};

const togglebtn = document.querySelector('#toggle');
const submenu= document.querySelector('.navigation ul li ul');

togglebtn.onclick=function()
{
   submenu.classList.toggle('active');
}

const settings= document.querySelector('.navigation ul li:nth-child(3)');

settings.onmouseleave=function()
{
   submenu.classList.remove('active');
   console.log("out")
}