const caret=document.querySelector('.fa-caret-down');
const menu=document.querySelector('.submenu');

caret.onclick=function()
{
    menu.classList.toggle('active');
};