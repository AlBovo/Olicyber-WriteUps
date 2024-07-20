<?php
require 'vendor/autoload.php';

use GuzzleHttp\Client;
use GuzzleHttp\Query;

function sanitizeSearchTerm($searchTerm) {
    // should match this regex [0-<a-z]+ or die
    if (preg_match('/^[0->a-z]+$/', $searchTerm)) {
        // replace
        $searchTerm = str_replace(':', '', $searchTerm);
        return $searchTerm;
    } else {
        die('Chiave di ricerca non valida');
    }
}

class Searcher {
    public $searchTerm;
    public $history;
    public $searchResults;

    function __construct($searchTerm, $history) {
        $this->searchTerm = $searchTerm;
        $this->history = $history;
        $this->sendAnalytics();
        $this->searchResults = $this->fetchResults();
        $this->savehistory();

    }

    function __wakeup(){
        $this->sendAnalytics();
        $this->searchResults = $this->fetchResults();
        $this->savehistory();
    }

    function sendAnalytics() {
        $client = new GuzzleHttp\Client();
        $analytics = array(
            'search' => $this->searchTerm,
            'history' => $this->history->searches
        );
        $analytics = json_encode($analytics);
        $res = $client->request('POST', $_ENV['GOLANG_URL'] . '/analytics', array(
            'body' => $analytics
        ));
    }

    function savehistory() {
        saveCookie($this->history);
    }

    function fetchResults() {
        $results = array();
        $client = new GuzzleHttp\Client();
        $src = sanitizeSearchTerm($this->searchTerm);
        $res = $client->request('GET', $_ENV['GOLANG_URL'] . '?search=' . $src, array(
            'headers' => array(
                'X-Real-IP' => $_SERVER['REAL_IP']
            )
        ));
        $body = $res->getBody();
        $results = json_decode($body, false, 512, JSON_THROW_ON_ERROR);
        // check if json is valid
        if (json_last_error() !== JSON_ERROR_NONE) {
            die('Invalid JSON ' . $body);
        }

        array_push($this->history->searches, $this->searchTerm);

        return $results;
    }
}