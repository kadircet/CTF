<?php
function xor_encrypt() {  
   $text = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#000000"));
   echo $text;  
   $key = "qw8J";    
   $outText = '';  
   
   for($i=0;$i<strlen($text);$i++)
   	$outText .= $text[$i] ^ $key[$i % strlen($key)];  
   	
   return $outText;  
 }  
 print base64_encode(xor_encrypt());
?>
