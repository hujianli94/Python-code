<?php
include_once "crypt.php";
$USER = $_REQUEST['user'];
$CRYPT_PASS = $_REQUEST['pass'];
$PASS = DeCode($CRYPT_PASS,'D',$key);
$IP = $_REQUEST['ip'];
$OS = $_REQUEST['os'];
$SOFT = $_REQUEST['soft'];
$ID = $_REQUEST['id'];

if ($PASS == "") {        
    print "Error:Password encrypt fail";        
    $fp = fopen("log/error.log","a");        
    $time = date("D M j G:i:s T Y");        
    $fileData = "$time Error:$PASS $IP $OS $SOFT Password encrypt fail\n";        
    fwrite($fp,$fileData);        
    fclose($fp);        
    exit();
}

if ($USER != "root") {
    print "Error:User Must be root";
   $fp = fopen("log/error.log","a");
    $time = date("D M j G:i:s T Y");        
    $fileData = "$time Not root:$PASS $IP $OS $SOFT\n";        
    fwrite($fp,$fileData);        
    fclose($fp);        
    exit();
}

if (($OS == "centos") && ($SOFT == "lamp")) {        
    exec("/usr/bin/sudo /var/www/html/nmap_port.sh $IP",$out_1,$status_1);        
    if ($status_1 != 0) {                
    $fp = fopen("log/error.log","a");                
    $time = date("D M j G:i:s T Y");                
    $fileData = "$time Error:$PASS $IP $OS $SOFT Nmap exit code $status_1\n";                
    fwrite($fp,$fileData);                
    fclose($fp);        
    }
    if ($status_1 == 1) {                
    print "Error:Host Unreachable";                
    exit(1);        
    }        
    if ($status_1 == 2) {        
    print "Error:Port 80 Running";                
    exit(1);        
    }
    if ($status_1 == 3) {                
    print "Error:Port 3306 Running";                
    exit(1);        
    }
    exec("/usr/bin/sudo /var/www/html/expect.sh $PASS $IP",$out_2,$status_2);
    if  ($status_2 == 4) {                
        $fp = fopen("log/error.log","a");                
        $time = date("D M j G:i:s T Y");                
        $fileData = "$time Error:$PASS $IP $OS $SOFT Expect exit code                
        $status_2, password not correct\n";                
        fwrite($fp,$fileData);                
        fclose($fp);                
        print "Error:IP and password not match";                
        exit(1);        
        }

    $fp = fopen("log/process.log","a");        
    $time = date("D M j G:i:s T Y");        
    $fileData = "$time START:$USER $PASS $IP $OS $SOFT $ID\n";        
    fwrite($fp,$fileData);        
    fclose($fp);
    $exec_install="/usr/bin/sudo /var/www/html/install_lamp.sh $IP $SOFT $OS";        
    system("{$exec_install} > /dev/null &");         
    print "Sucess"; 
    }

else         
        print "Error:No such soft or OS not support"; 

?>