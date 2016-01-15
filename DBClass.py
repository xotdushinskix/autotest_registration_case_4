from elasticsearch import Elasticsearch

es = Elasticsearch(hosts = 'xxx.bintime.com:1234')

class DB():
  #for all products
    def dbActionsWithAllProducts(self, category):
      return es.count(index = "gepard_product", doc_type = "product", body = {
  "query": {
          "term": {
            "multilingual.1.category_name.exact": {
              "value": category
        }
    }
  }
}

)

    #for in stock products
    def dbActionsWithInStockProducts(self, category):
      return es.count(index = "gepard_product", doc_type = "product", body = {
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "multilingual.1.category_name.exact": {
              "value": category
            }
          }
        },
        {
              "term": {
                "has_stock": "1"
              }
            },
        {
          "term": {
            "visibility": "1"
          }
        }
      ]
    }
  }
})
