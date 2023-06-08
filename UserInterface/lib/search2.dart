import 'package:flutter/material.dart';
import 'package:ir_project/api_service.dart';
import 'package:ir_project/api_service2.dart';

class SearchTwo extends StatefulWidget {
  const SearchTwo({Key? key}) : super(key: key);

  @override
  State<SearchTwo> createState() => _SearchTwoState();
}

class _SearchTwoState extends State<SearchTwo> {
  TextEditingController id=TextEditingController();
  TextEditingController query=TextEditingController();
  List<dynamic> searchResultsTwo = [];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Center(
          child: Text(
            "Information Retrieval",
            style: TextStyle(color: Colors.white, fontSize: 20),
          ),
        ),
        backgroundColor: Colors.deepOrange,
      ),
      body: Column(
        children: [
          SizedBox(height: 100,),
          Padding(
            padding: const EdgeInsets.only(left: 300.0,right: 300),
            child: TextFormField(
              controller: id,


              onChanged: (val) {

                print(val);

              },
              cursorColor: Colors.deepOrange,
              decoration: InputDecoration(
                contentPadding:
                EdgeInsets.symmetric(vertical: 20),
                filled: true,
                fillColor: Colors.grey.shade50,
                hintText: 'Id',
                //hintStyle: searchStyle,
                prefixIcon: IconButton(
                  onPressed: () {
                    // controller.onSearchDoctors();
                    //    controller.search();
                  },
                  icon: Icon(Icons.numbers),
                  color: Colors.deepOrange,
                ),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15.0),
                  borderSide: BorderSide(color: Colors.grey),
                ),
                focusedBorder: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey),
                  borderRadius: BorderRadius.circular(15.0),
                ),
              ),
            ),
          ),
          SizedBox(height: 50,),

          Padding(
            padding: const EdgeInsets.only(left: 300.0,right: 300),
            child: TextFormField(
              controller: query,
              onChanged: (val) {
                print(val);
              },
              cursorColor: Colors.deepOrange,
              decoration: InputDecoration(
                contentPadding:
                EdgeInsets.symmetric(vertical: 20),
                filled: true,
                fillColor: Colors.grey.shade50,
                hintText: 'Query',

                prefixIcon: IconButton(
                  onPressed: () {
                    // controller.onSearchDoctors();
                    //    controller.search();
                  },
                  icon: Icon(Icons.text_fields),
                  color: Colors.deepOrange,
                ),
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15.0),
                  borderSide: BorderSide(color: Colors.grey),
                ),
                focusedBorder: OutlineInputBorder(
                  borderSide: BorderSide(color: Colors.grey),
                  borderRadius: BorderRadius.circular(15.0),
                ),
              ),
            ),
          ),

          SizedBox(height: 30,),
         /* ElevatedButton(
            onPressed: () async {

              final idText = id.text;
              final queryText = query.text;
              final results = await ApiService.search_two(idText, queryText);
              print(results);
              if (results != null && results.isNotEmpty) { // Check if results is not empty
                setState(() {
                  searchResults = results[1];
                });
              }

            },
            child: Text('Search'),
            style: ButtonStyle(
              backgroundColor: MaterialStateProperty.all(Colors.orangeAccent),
            ),
          ),*/

          ElevatedButton(
            onPressed:(){
              searchAya(id.text,query.text);
            },// searchAya(id.text,query.text),
            child: Text('Search'),
            style: ButtonStyle(
              backgroundColor: MaterialStateProperty.all(Colors.orangeAccent),
            ),
          ),

          SizedBox(height: 50,),

          Expanded(
            child: ListView.builder(
              itemCount: searchResultsTwo.length,
              itemBuilder: (BuildContext context, int index) {
                return Center(
                  child: ListTile(
                    title: Text(searchResultsTwo[index][0]),
                    subtitle: Text(searchResultsTwo[index][1].toString()),
                  ),
                );
              },
            ),
          ),

        ],
      ),
    );
  }

  searchAya(id,query) async
  {

    final results = await ApiService2.searchSecond(id, query);
    print(results);
    if (results != null && results.isNotEmpty) { // Check if results is not empty
      setState(() {
        searchResultsTwo = results[1];
      });
    }

  }
}
