import 'package:client/overlay/create_session_overlay.dart';
import 'package:flutter/cupertino.dart';

class CreateSessionOverlayDI {
  CreateSessionOverlay overlay = const CreateSessionOverlay();
  ValueNotifier<bool> state = ValueNotifier<bool>(false);
}

CreateSessionOverlayDI? createSessionUI;

getCreateSessionOverlay() {
  createSessionUI ??= CreateSessionOverlayDI();
  return createSessionUI;
}

showOverlay<T>(T widget) {
  if (widget is CreateSessionOverlayDI) {
    widget.state.value = true;
  }
}

hideOverlay<T>(T widget) {
  if (widget is CreateSessionOverlayDI) {
    widget.state.value = false;
  }
}