import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import '../widgets/set_api_key_button.dart';
import '../widgets/create_new_session_button.dart';

class MainMenuScreen extends StatelessWidget {
	const MainMenuScreen({super.key});

	@override
	Widget build(BuildContext context) {
	  return Scaffold(
      appBar: AppBar(
        title: Text(
          'LLM Game Project',
          style: GoogleFonts.dmSerifText(
            fontSize: 24,
            fontWeight: FontWeight.bold,
            color: Color.fromARGB(255, 255, 255, 255)
          )
        ),
        backgroundColor: Color.fromARGB(255, 69, 1, 255),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(
            top: Radius.circular(3),
            bottom: Radius.circular(15)
          ),
        ),
      ),
      body: Row(
        children: <Widget>[
          Align(
            alignment: Alignment.bottomLeft,
            child: CreateNewSessionButton(),
          ),
          Align(
            alignment: Alignment.bottomRight,
            child: SetApiKeyButton(),
          )
        ],
      ),
      backgroundColor: Color.fromARGB(255, 26, 26, 26),
    );
	}
}