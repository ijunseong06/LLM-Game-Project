import 'package:client/services/overlay_manager.dart';
import 'package:client/widgets/create_new_session_widget.dart';
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
      body: Stack(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: <Widget>[
              Align(
                alignment: Alignment.bottomRight,
                child: SetApiKeyButton(),
              ),
              Align(
                alignment: Alignment.bottomLeft,
                child: CreateNewSessionButton(), 
              ),
            ],
          ),
          CreateNewSessionWidget(manager: getCreateSessionOverlay())
        ],
      ),
      backgroundColor: Color.fromARGB(255, 26, 26, 26),
    );
	}
}