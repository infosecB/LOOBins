# LOOBin Schema

<p>LOOBin base class</p>

<table>
<tbody>


</tbody>
</table>

## Properties

<table><thead><tr><th colspan="2">Name</th><th>Type</th></tr></thead><tbody><tr><td colspan="2"><a href="#name">name</a></td><td>String</td></tr><tr><td colspan="2"><a href="#author">author</a></td><td>String</td></tr><tr><td colspan="2"><a href="#short_description">short_description</a></td><td>String</td></tr><tr><td colspan="2"><a href="#full_description">full_description</a></td><td>String</td></tr><tr><td colspan="2"><a href="#created">created</a></td><td>String</td></tr><tr><td colspan="2"><a href="#example_use_cases">example_use_cases</a></td><td>Array</td></tr><tr><td colspan="2"><a href="#paths">paths</a></td><td>Array</td></tr><tr><td colspan="2"><a href="#detections">detections</a></td><td>Array</td></tr><tr><td colspan="2"><a href="#resources">resources</a></td><td>Array</td></tr><tr><td colspan="2"><a href="#acknowledgements">acknowledgements</a></td><td>Array</td></tr></tbody></table>



<hr />



## name


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Name</td>
    </tr>
    <tr>
      <th>Description</th>
      <td colspan="2">Name of the LOOBin</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>

  </tbody>
</table>






## author


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Author</td>
    </tr>
    <tr>
      <th>Description</th>
      <td colspan="2">Author of the LOOBin</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>

  </tbody>
</table>






## short_description


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Short Description</td>
    </tr>
    <tr>
      <th>Description</th>
      <td colspan="2">A short description of the LOOBin.This will display in the LOOBin card list and the LOOBins website search results.</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>

  </tbody>
</table>






## full_description


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Full Description</td>
    </tr>
    <tr>
      <th>Description</th>
      <td colspan="2">A full description of the LOOBin.This will display on the LOOBin&#x27;s single page.</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>

  </tbody>
</table>






## created


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Created</td>
    </tr>
    <tr>
      <th>Description</th>
      <td colspan="2">Date the LOOBin was created</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>
    <tr>
      <th>Format</th>
      <td colspan="2">date</td>
    </tr>
  </tbody>
</table>






## example_use_cases


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Example Use Cases</td>
    </tr>
    <tr>
      <th>Description</th>
      <td colspan="2">A list of example use cases for the LOOBin</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>

  </tbody>
</table>



### example_use_cases.name


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Name</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>

  </tbody>
</table>




### example_use_cases.description


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Description</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>

  </tbody>
</table>




### example_use_cases.code


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Code</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>

  </tbody>
</table>




### example_use_cases.tactics


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Tactics</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Array</td></tr>

  </tbody>
</table>




### example_use_cases.tags


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Tags</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Array</td></tr>

  </tbody>
</table>







## paths


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Paths</td>
    </tr>
    <tr>
      <th>Description</th>
      <td colspan="2">A list of paths to the LOOBin</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>

  </tbody>
</table>






## detections


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Detections</td>
    </tr>
    <tr>
      <th>Description</th>
      <td colspan="2">A list of detections for the LOOBin</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">Yes</td>
    </tr>

  </tbody>
</table>



### detections.name


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Name</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>

  </tbody>
</table>




### detections.url


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Url</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>

  </tbody>
</table>







## resources


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Resource</td>
    </tr>
    <tr>
      <th>Description</th>
      <td colspan="2">A list of useful resources for the LOOBin</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>

  </tbody>
</table>



### resources.name


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Name</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>

  </tbody>
</table>




### resources.url


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Url</td>
    </tr>
    <tr><th>Type</th><td colspan="2">String</td></tr>

  </tbody>
</table>







## acknowledgements


<table>
  <tbody>
    <tr>
      <th>Title</th>
      <td colspan="2">Acknowledgements</td>
    </tr>
    <tr>
      <th>Description</th>
      <td colspan="2">Acknowledgements for the LOOBin</td>
    </tr>
    <tr><th>Type</th><td colspan="2">Array</td></tr>
    <tr>
      <th>Required</th>
      <td colspan="2">No</td>
    </tr>

  </tbody>
</table>










<hr />

## Schema
```
{
    "title": "LOOBin",
    "description": "LOOBin base class",
    "type": "object",
    "properties": {
        "name": {
            "title": "Name",
            "description": "Name of the LOOBin",
            "type": "string"
        },
        "author": {
            "title": "Author",
            "description": "Author of the LOOBin",
            "type": "string"
        },
        "short_description": {
            "title": "Short Description",
            "description": "A short description of the LOOBin.This will display in the LOOBin card list and the LOOBins website search results.",
            "type": "string"
        },
        "full_description": {
            "title": "Full Description",
            "description": "A full description of the LOOBin.This will display on the LOOBin's single page.",
            "type": "string"
        },
        "created": {
            "title": "Created",
            "description": "Date the LOOBin was created",
            "type": "string",
            "format": "date"
        },
        "example_use_cases": {
            "title": "Example Use Cases",
            "description": "A list of example use cases for the LOOBin",
            "type": "array",
            "items": {
                "$ref": "#/definitions/ExampleUseCase"
            }
        },
        "paths": {
            "title": "Paths",
            "description": "A list of paths to the LOOBin",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "detections": {
            "title": "Detections",
            "description": "A list of detections for the LOOBin",
            "type": "array",
            "items": {
                "$ref": "#/definitions/Detection"
            }
        },
        "resources": {
            "title": "Resource",
            "description": "A list of useful resources for the LOOBin",
            "type": "array",
            "items": {
                "$ref": "#/definitions/Resource"
            }
        },
        "acknowledgements": {
            "title": "Acknowledgements",
            "description": "Acknowledgements for the LOOBin",
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": [
        "name",
        "author",
        "short_description",
        "full_description",
        "created",
        "example_use_cases",
        "paths",
        "detections"
    ],
    "definitions": {
        "ExampleUseCase": {
            "title": "ExampleUseCase",
            "description": "Use case base class",
            "type": "object",
            "properties": {
                "name": {
                    "title": "Name",
                    "type": "string"
                },
                "description": {
                    "title": "Description",
                    "type": "string"
                },
                "code": {
                    "title": "Code",
                    "type": "string"
                },
                "tactics": {
                    "title": "Tactics",
                    "type": "array",
                    "items": {
                        "enum": [
                            "Reconnaissance",
                            "Resource Development",
                            "Initial Access",
                            "Execution",
                            "Persistence",
                            "Privilege Escalation",
                            "Defense Evasion",
                            "Credential Access",
                            "Discovery",
                            "Lateral Movement",
                            "Collection",
                            "Exfiltration",
                            "Command and Control",
                            "Impact"
                        ],
                        "type": "string"
                    }
                },
                "tags": {
                    "title": "Tags",
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": [
                "name",
                "description"
            ]
        },
        "Detection": {
            "title": "Detection",
            "description": "Detection base class",
            "type": "object",
            "properties": {
                "name": {
                    "title": "Name",
                    "type": "string"
                },
                "url": {
                    "title": "Url",
                    "type": "string"
                }
            },
            "required": [
                "name",
                "url"
            ]
        },
        "Resource": {
            "title": "Resource",
            "description": "External reference base class",
            "type": "object",
            "properties": {
                "name": {
                    "title": "Name",
                    "type": "string"
                },
                "url": {
                    "title": "Url",
                    "type": "string"
                }
            },
            "required": [
                "name",
                "url"
            ]
        }
    }
}
```
