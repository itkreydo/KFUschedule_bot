<?php
include_once("config.php"); 
Class bd extends SQLite3{
	public $conn;
	function __construct($fileName){
		$this->conn = new SQLite3($fileName);
	}
	function resultToArray ($result) { 
		$array=array(); 
		while(($row=$result->fetchArray(SQLITE3_ASSOC))!=false) 
			$array[]=$row; 
		return $array; 
	}
	function isRegistered($user_id){
		$sql = $this->conn->query("SELECT * FROM user WHERE vk_id =".intval($user_id));
		$result = $this->resultToArray($sql);
		$numRows = count($result);
		if ($numRows!=0){return True;}
		return False;
	}
	function getAllUsers(){
		$sql = $this->conn->query("SELECT * FROM user");
		$result = $this->resultToArray($sql);
		return $result;
	}
	function getUserGroup($user_id){
		$sql = $this->conn->query("SELECT `group` FROM user WHERE vk_id=".intval($user_id));
		$result = $this->resultToArray($sql);
		return $result[0]["group"];
	}
	function addUser($user_id,$user_name,$group){
		return $this->conn->query("INSERT INTO user('vk_id','vk_name','step','group') values('".intval($user_id)."','".$user_name."','1','".intval($group)."')");
	}
	function deleteUser($user_id){
		return $this->conn->query("DELETE FROM user WHERE vk_id =".intval($user_id));
	}	
	function updateGroup($user_id,$group){
		return $this->conn->query("UPDATE user SET `group`='".intval($group)."' WHERE vk_id=".intval($user_id));
	}
}
#$fileName="res/my.db";
#$bd = new bd($fileName);

#$sql="SELECT * FROM user";  


#$result = $bd->conn->query($sql);
#$res=$bd->resultToArray ($result);
#echo $bd->isRegistered("390428758");
#$bd->addUser("777","lol","0769");
#print_r($bd->getAllUsers());
#$db->conn->close();

#$jdb  = new Jsondb(BOT_BASE_DIRECTORY."/res/schbd.json");
?>