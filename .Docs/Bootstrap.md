## bootstrap set up procedure

<details>
  <summary>1. files in templates folder</summary>

  [Bootstrap Examples](https://getbootstrap.com/docs/5.3/examples/)      
  1.1 find suitable examples  
  1.2 click out the page  
  1.3 use right click on the page to get the bootstrap code  
  1.4 copy the code to vs code  
  1.5 download Compiled CSS and JS  
  [download Compiled CSS and JS](https://getbootstrap.com/docs/5.3/getting-started/download/)  
  1.6 copy the bootstrap.min.css, bootstrap.min.css.map to css folder, and bootstrap.bundle.min.js to js folder  
  1.7 modify the related code, _base.j2 to the right file path with {{  }} jinja format 
  
      <link href="{{url_for('static', filename='css/bootstrap.min.css')}}" rel="stylesheet">     
      <link href="{{url_for('static', filename='css/index.css')}}" rel="stylesheet">      
      <script src="{{url_for('static',filename='js/bootstrap.bundle.min.js')}}"></script>   
  
  
  
  

</details>
<details>
  <summary>n. ---</summary>
  
    a---
</details>
<details>
  <summary>n. ---</summary>
  
    a---
</details>



[]()    
[]()    
