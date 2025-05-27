package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strings"
)

type Post struct {
	ID          int    `json:"id"`
	Title       string `json:"title"`
	Description string `json:"description"`
	isPrivate   bool
}

// create some random posts
func getPosts(flag string) []Post {
	return []Post{
		{ID: 1, isPrivate: false, Title: "Il Gabibbo è stato trovato morto", Description: "Il Gabibbo è stato trovato morto in un vicolo di Milano"},
		{ID: 2, isPrivate: false, Title: "In realtà il Gabibbo è vivo", Description: "Il Gabibbo è vivo e vegeto, è stato visto in compagnia di un uomo misterioso"},
		{ID: 3, isPrivate: false, Title: "Hanno avvistato il Gabibbo a un matrimonio", Description: "Il Gabibbo è stato avvistato a un matrimonio in Sicilia"},
		{ID: 3, isPrivate: true, Title: "Il Gabibbo è una spia!", Description: `I nostri agenti hanno scopero la chiave per decifrare le comunicazioni del Gabibbo: ` + flag},
	}
}

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		search := r.URL.Query().Get("search")
		debug := r.URL.Query().Get("debug")

		// list of posts
		matchingPosts := []Post{}

		flag := os.Getenv("FLAG")
		posts := getPosts(flag)

		for _, post := range posts {
			if post.isPrivate && debug != "true" {
				continue
			}
			if search != "" && strings.Contains(strings.ToLower(post.Title), strings.ToLower(search)) {
				matchingPosts = append(matchingPosts, post)
			}
		}
		// return json representation of posts
		json.NewEncoder(w).Encode(matchingPosts)

	})
	http.HandleFunc("/analytics", func(w http.ResponseWriter, r *http.Request) {
		// to be implemented
		w.WriteHeader(http.StatusOK)
	})
	fmt.Println("Listening on port 8090")
	http.ListenAndServe(":8090", nil)
}
