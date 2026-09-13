import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    visible: true
    width: 1280
    height: 760
    title: "Kalz OmniSuite"
    icon: "../assets/kalz-venom.png"
    color: "#0d1117"
    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 24
        spacing: 16
        RowLayout {
            Layout.fillWidth: true
            Image { source: "../assets/kalz-venom-48.png"; Layout.preferredWidth: 48; Layout.preferredHeight: 48; fillMode: Image.PreserveAspectFit }
            Label { text: "KALZ OMNISUITE"; color: "#58a6ff"; font.pixelSize: 28; font.bold: true }
        }
        Label { text: "Native Linux Operations Console · Safe / Audited / Dry-run"; color: "#8b949e" }
        RowLayout {
            Layout.fillWidth: true
            Repeater {
                model: ["System Health", "Tool Registry", "Automation", "Audit Chain"]
                delegate: Rectangle { Layout.fillWidth: true; height: 130; radius: 12; color: "#161b22"; border.color: "#30363d"; Text { anchors.centerIn: parent; text: modelData; color: "#f0f6fc"; font.pixelSize: 18 } }
            }
        }
        TextArea { Layout.fillWidth: true; Layout.fillHeight: true; readOnly: true; text: "Ready. All system changes require preview and consent.\n\nUse Doctor, Plan, Audit, or Automation from the command palette."; color: "#c9d1d9"; background: Rectangle { color: "#010409"; radius: 8 } }
    }
}
