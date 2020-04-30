/* https://www.w3schools.com/howto/howto_js_filter_lists.asp */
function filterList () {
  var input, filter, ul, li, a, i
  input = document.getElementById('search')
  filter = input.value.toUpperCase()
  ul = document.getElementById('articleList')
  li = ul.getElementsByTagName('li')
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName('a')[0]
    p = li[i].getElementsByTagName('p')[0]
    b = li[i].getElementsByTagName('h6')[1]
    if (a.innerHTML.toUpperCase().indexOf(filter) > -1 || b.innerHTML.toUpperCase().indexOf(filter) > -1 || p.innerHTML.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = ''
    } else {
      li[i].style.display = 'none'
    }
  }
}
