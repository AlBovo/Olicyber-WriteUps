<?php
require 'vendor/autoload.php';
require 'history.php';
require 'searcher.php';

$session = cookieSession();

if (isset($_POST['search'])) {
    $searchTerm = $_POST['search'];
    $searcher = new Searcher($searchTerm, $session);
    $searchResults = $searcher->searchResults;
    $searchTerm = $searcher->searchTerm;
    if (!isset($session->history)) {
        $session->history = new History();
    }
    $session->history->searches[] = $searchTerm;
    saveCookie($session);
} else {
    $searchTerm = '';
    $searchResults = array();
}

?>    

<html>
    <head>
        <title>Redacted blog</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <div class="container mx-auto bg-gray-100 br-4 rounded-lg border-4 p-4 flex gap-6">
        <div>
            <h1 class="text-4xl font-bold">Redacted blog</h1>
            <img src="/gab.png" class="mx-auto w-[200px] my-4 rounded-2xl">
            <form action="/" method="post">
                <input type="text" name="search" placeholder="gabibbo" value="<?php echo $searchTerm; ?>" class="border border-gray-400 p-2">
                <input type="submit" value="Search" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            </form>
        </div>
        <div class="ml-4">
            <h2 class="text-2xl font-bold">Cronologia</h2>
            <ul>
                <?php foreach ($session->searches as $search): ?>
                    <li class="italic"><?php echo $search; ?></li>
                <?php endforeach; ?>
            </ul>
        </div>
        <?php if (isset($_POST['search'])): ?>
        <div class="ml-4">
            <h2 class="text-2xl font-bold">Risultati di ricerca</h2>
            <div class="flex flex-wrap gap-2">
                <?php foreach ($searchResults as $result): ?>
                    <div class="w-full">
                        <h4 class="text-md font-bold"><?php echo $result->title; ?></h3>
                        <p><?php 
                         if (str_contains($result->description, 'flag'))
                         {
                            echo 'redacted';
                         } else {
                            echo $result->description; 
                         }?>
                        </p>
                    </div>
                <?php endforeach; ?>
                </div>
        </div>
        <?php endif; ?>
    </div>
</html>





