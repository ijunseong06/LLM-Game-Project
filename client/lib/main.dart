import 'package:flutter/material.dart';

import 'screens/main_menu.dart';

void main() {
	runApp(const Main());
}

class Main extends StatelessWidget {
	const Main({super.key});

	@override
	Widget build(BuildContext context) {
		return MaterialApp(
			initialRoute: '/',
			routes: {
				'/': (context) => const MainMenuScreen()
			},
		);
	}
}