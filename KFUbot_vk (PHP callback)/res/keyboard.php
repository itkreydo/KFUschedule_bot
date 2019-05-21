<?php	
$keyboard_sch=Array( 
    "one_time"=> false, 
    "buttons"=> Array( 
      Array(Array( 
        "action"=> Array( 
          "type"=> "text", 
          "payload"=> "{\"button\": \"1\"}", 
          "label"=> MON 
        ), 
        "color"=> "default" 
      ), 
     Array( 
        "action"=> Array( 
          "type"=> "text", 
          "payload"=> "{\"button\": \"2\"}", 
          "label"=> TUE 
        ), 
        "color"=> "default" 
      )),
      Array(Array( 
        "action"=> Array( 
          "type"=> "text", 
          "payload"=> "{\"button\": \"3\"}", 
          "label"=> WED 
        ), 
        "color"=> "default" 
      ), 
     Array( 
        "action"=> Array( 
          "type"=> "text", 
          "payload"=> "{\"button\": \"4\"}", 
          "label"=> THU 
        ), 
        "color"=> "default" 
      )),
      Array(Array( 
        "action"=> Array( 
          "type"=> "text", 
          "payload"=> "{\"button\": \"3\"}", 
          "label"=> FRI 
        ), 
        "color"=> "default" 
      ), 
     Array( 
        "action"=> Array( 
          "type"=> "text", 
          "payload"=> "{\"button\": \"4\"}", 
          "label"=> SAT 
        ), 
        "color"=> "default" 
      )),
	  Array(Array( 
        "action"=> Array( 
          "type"=> "text", 
          "payload"=> "{\"button\": \"3\"}", 
          "label"=> HZ 
        ), 
        "color"=> "primary" 
      )) 	  
    ) 
  );
  $keyboard_sch = json_encode($keyboard_sch,JSON_UNESCAPED_UNICODE);
  
  $keyboard_group=Array( 
    "one_time"=> false, 
    "buttons"=> Array( 
      Array(Array( 
        "action"=> Array( 
          "type"=> "text", 
          "payload"=> "{\"button\": \"1\"}", 
          "label"=> "09-641 (1)" 
        ), 
        "color"=> "default" 
      ), 
     Array( 
        "action"=> Array( 
          "type"=> "text", 
          "payload"=> "{\"button\": \"2\"}", 
          "label"=> "09-641 (2)"
        ), 
        "color"=> "default" 
      ))	  
    ) 
  );
   $keyboard_menu=Array( 
    "one_time"=> false, 
    "buttons"=> Array( 
      Array(Array( 
        "action"=> Array( 
          "type"=> "text", 
          "payload"=> "{\"button\": \"1\"}", 
          "label"=> CHANGE_GROUP 
        ), 
        "color"=> "primary" 
      ))	  
    ) 
  );
    $keyboard_group = json_encode($keyboard_group,JSON_UNESCAPED_UNICODE);
	$keyboard_menu = json_encode($keyboard_menu,JSON_UNESCAPED_UNICODE);
	$keyboards = Array("days"=>$keyboard_sch,"groups"=>$keyboard_group,"menu"=>$keyboard_menu);
  ?>