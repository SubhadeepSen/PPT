package main

import (
	"encoding/json"
	"fmt"
	"log"
	"reflect"
)

var jsonString = `
{
	"data": [{
	  "type": "articles",
	  "id": "1",
	  "attributes": {
		"title": "JSON:API paints my bikeshed!",
		"body": "The shortest article. Ever.",
		"created": "2015-05-22T14:56:29.000Z",
		"updated": "2015-05-22T14:56:28.000Z"
	  },
	  "relationships": {
		"author": {
		  "data": {"id": "42", "type": "people"}
		}
	  }
	}],
	"included": [
	  {
		"type": "people",
		"id": "42",
		"attributes": {
		  "name": "John",
		  "age": 80,
		  "gender": "male"
		}
	  }
	]
  }
`

func main() {

	var jsonMap map[string]interface{}
	if err := json.Unmarshal([]byte(jsonString), &jsonMap); err != nil {
		log.Fatal("unable to unmarshal")
	}

	flatJson := flatJson(jsonMap)
	for k, v := range flatJson {
		fmt.Printf("%s = %v\n", k, v)
	}
}

func flatJson(jsonMap map[string]interface{}) map[string]interface{} {
	flatJsonMap := make(map[string]interface{})
	for key, value := range jsonMap {
		switch value.(type) {
		case map[string]interface{}:
			tempMap := flatJson(value.(map[string]interface{}))
			for k, v := range tempMap {
				flatJsonMap[fmt.Sprintf("%s.%s", key, k)] = v
			}
		case []interface{}:
			for index, val := range value.([]interface{}) {
				if reflect.TypeOf(val).String() == "map[string]interface {}" {
					tempMap := flatJson(val.(map[string]interface{}))
					for k, v := range tempMap {
						flatJsonMap[fmt.Sprintf("%s.%d.%s", key, index, k)] = v
					}
				} else {
					flatJsonMap[fmt.Sprintf("%s.%d", key, index)] = val
				}
			}
		default:
			flatJsonMap[key] = value
		}
	}

	return flatJsonMap
}
