import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:client/l10n/app_localizations.dart';

class SetApiKeyButton extends StatelessWidget {
	const SetApiKeyButton({super.key});

  @override
  Widget build(BuildContext context) {
		final ButtonStyle style = ElevatedButton.styleFrom(textStyle: GoogleFonts.dmSerifText(fontSize: 20, fontWeight : FontWeight.bold));

		return Column(
			mainAxisAlignment: MainAxisAlignment.end,
			crossAxisAlignment: CrossAxisAlignment.end,
			children: <Widget>[
				Padding(
					padding: const EdgeInsets.fromLTRB(3, 0, 0, 5),
					child: SizedBox(
						width: 150,
						height: 50,
						child: ElevatedButton(
              style: style,
              onPressed: () {},
              child: Text(AppLocalizations.of(context)!.setApiKey),
            ),
					),
				),
			],
		);
  }
}