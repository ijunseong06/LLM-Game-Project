import 'package:client/l10n/app_localizations.dart';
import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';

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
				'/': (context) => MainMenuScreen()
			},
      localizationsDelegates: [
		AppLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [
        Locale('ko'),
        Locale('en')
      ],
		);
	}
}