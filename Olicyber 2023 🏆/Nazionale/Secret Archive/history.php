<?php

class History
{
   public $searches = array();

}

function saveCookie($session)
{
    $session = serialize($session);
    $session = json_encode(array("sess" => $session));
    $session = base64_encode($session);
    setcookie('sessionID', $session, time() + 3600, '/');
}

function cookieSession()
{
    if (isset($_COOKIE['sessionID'])) {
        $session = base64_decode($_COOKIE['sessionID']);
        $session = json_decode($session);
        $session = unserialize($session->sess);
        if (count($session->searches) > 9) {
            $session->searches = array_slice($session->searches, 1);
        }
        return $session;
    } else {
        $session = new History();
        saveCookie($session);
        return $session;
    }
}