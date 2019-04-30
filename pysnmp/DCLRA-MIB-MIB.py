#
# PySNMP MIB module DCLRA-MIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DCLRA-MIB-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:21:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
DmiInteger64, dmiEventAssociatedGroup, dmiCompId, dmiEventStateKey, dmiEventSeverity, dmiEventDateTime, DmiDate, dmiEventSubSystem, dmiEventSystem = mibBuilder.importSymbols("DMTF-DMI-MIB", "DmiInteger64", "dmiEventAssociatedGroup", "dmiCompId", "dmiEventStateKey", "dmiEventSeverity", "dmiEventDateTime", "DmiDate", "dmiEventSubSystem", "dmiEventSystem")
InternationalDisplayString, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "InternationalDisplayString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, enterprises, Bits, ModuleIdentity, Counter32, Integer32, iso, TimeTicks, NotificationType, IpAddress, ObjectIdentity, MibIdentifier, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "enterprises", "Bits", "ModuleIdentity", "Counter32", "Integer32", "iso", "TimeTicks", "NotificationType", "IpAddress", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DmiCounter(Counter32):
    pass

class DmiCounter64(Counter64):
    pass

class DmiGauge(Gauge32):
    pass

class DmiInteger(Integer32):
    pass

class DmiOctetstring(OctetString):
    pass

class DmiDisplaystring(DisplayString):
    pass

class DmiCompId(Integer32):
    pass

class DmiGroupId(Integer32):
    pass

dmtf = MibIdentifier((1, 3, 6, 1, 4, 1, 412))
dmtfStdMifs = MibIdentifier((1, 3, 6, 1, 4, 1, 412, 2))
dmtfDynOids = MibIdentifier((1, 3, 6, 1, 4, 1, 412, 3))
dmtfServiceLayerMIF = MibIdentifier((1, 3, 6, 1, 4, 1, 412, 2, 1))
dMTFComponentIDTable = MibTable((1, 3, 6, 1, 4, 1, 412, 2, 1, 1), )
if mibBuilder.loadTexts: dMTFComponentIDTable.setStatus('mandatory')
dMTFComponentIDEntry = MibTableRow((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1), ).setIndexNames((0, "DCLRA-MIB-MIB", "DmiCompId"), (0, "DCLRA-MIB-MIB", "DmiGroupId"))
if mibBuilder.loadTexts: dMTFComponentIDEntry.setStatus('mandatory')
manufacturerAtt1 = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manufacturerAtt1.setStatus('mandatory')
productAtt2 = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productAtt2.setStatus('mandatory')
versionAtt3 = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 3), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: versionAtt3.setStatus('mandatory')
serialNumberAtt4 = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumberAtt4.setStatus('mandatory')
installationAtt5 = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 5), DmiDate()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installationAtt5.setStatus('mandatory')
verifyAtt6 = MibTableColumn((1, 3, 6, 1, 4, 1, 412, 2, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("anErrorOccurredCheckStatusCode", 0), ("thisComponentDoesNotExist", 1), ("verificationIsNotSupported", 2), ("reserved", 3), ("thisComponentExistsButTheFunctionalityIsUntested", 4), ("thisComponentExistsButTheFunctionalityIsUnknown", 5), ("thisComponentExistsAndIsNotFunctioningCorrectly", 6), ("thisComponentExistsAndIsFunctioningCorrectly", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: verifyAtt6.setStatus('mandatory')
dell = MibIdentifier((1, 3, 6, 1, 4, 1, 674))
server2 = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10891))
dellLRAActionTableTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10891, 313), )
if mibBuilder.loadTexts: dellLRAActionTableTable.setStatus('mandatory')
dellLRAActionTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10891, 313, 1), ).setIndexNames((0, "DCLRA-MIB-MIB", "DmiCompId"), (0, "DCLRA-MIB-MIB", "DmiGroupId"), (0, "DCLRA-MIB-MIB", "actionNameAtt1"))
if mibBuilder.loadTexts: dellLRAActionTableEntry.setStatus('mandatory')
dellLRAActionTableState = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 0), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dellLRAActionTableState.setStatus('mandatory')
actionNameAtt1 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3, 7, 13, 14, 160, 168, 172, 200, 202, 204, 206, 208, 210, 212, 214, 220, 225))).clone(namedValues=NamedValues(("unknown", 0), ("adaptecHostAdapterFailed", 3), ("adaptecLogicalUnitFailed", 7), ("aPCSystemOnLowUtilityPower", 13), ("aPCSystemOnLowBatteryPower", 14), ("temperatureSensorDetectedAFailure", 160), ("fanSensorDetectedAFailure", 168), ("voltageSensorDetectedAFailure", 172), ("temperatureSensorWarningDetected", 200), ("voltageSensorWarningDetected", 202), ("fanSensorWarningDetected", 204), ("currentSensorDetectedAFailure", 206), ("currentSensorWarningDetected", 208), ("powerSupplyLostRedundancyDetected", 210), ("powerSupplyDegradedRedundancyDetected", 212), ("powerSupplyDetectedAFailure", 214), ("chassisIntrusionDetected", 220), ("lostConnectionToDiskPod", 225)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: actionNameAtt1.setStatus('mandatory')
actionResponseAtt2 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 2), DmiDisplaystring()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: actionResponseAtt2.setStatus('mandatory')
actionExecuteAtt3 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 3), DmiDisplaystring()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: actionExecuteAtt3.setStatus('mandatory')
actionSourceAtt4 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: actionSourceAtt4.setStatus('mandatory')
uDPInformationAtt5 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 313, 1, 5), DmiDisplaystring()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: uDPInformationAtt5.setStatus('mandatory')
dellLRACapabilitiesTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10891, 314), )
if mibBuilder.loadTexts: dellLRACapabilitiesTable.setStatus('mandatory')
dellLRACapabilitiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10891, 314, 1), ).setIndexNames((0, "DCLRA-MIB-MIB", "DmiCompId"), (0, "DCLRA-MIB-MIB", "DmiGroupId"))
if mibBuilder.loadTexts: dellLRACapabilitiesEntry.setStatus('mandatory')
lRACapabilitiesAtt1 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 314, 1, 1), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lRACapabilitiesAtt1.setStatus('mandatory')
dellLRABeepActionTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10891, 315), )
if mibBuilder.loadTexts: dellLRABeepActionTable.setStatus('mandatory')
dellLRABeepActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10891, 315, 1), ).setIndexNames((0, "DCLRA-MIB-MIB", "DmiCompId"), (0, "DCLRA-MIB-MIB", "DmiGroupId"))
if mibBuilder.loadTexts: dellLRABeepActionEntry.setStatus('mandatory')
beepClearAtt1 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 315, 1, 1), DmiDisplaystring()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: beepClearAtt1.setStatus('mandatory')
beepDelayAtt2 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 315, 1, 2), DmiDisplaystring()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: beepDelayAtt2.setStatus('mandatory')
dELLSystemsManagementSoftwareTable = MibTable((1, 3, 6, 1, 4, 1, 674, 10891, 400), )
if mibBuilder.loadTexts: dELLSystemsManagementSoftwareTable.setStatus('mandatory')
dELLSystemsManagementSoftwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 674, 10891, 400, 1), ).setIndexNames((0, "DCLRA-MIB-MIB", "DmiCompId"), (0, "DCLRA-MIB-MIB", "DmiGroupId"))
if mibBuilder.loadTexts: dELLSystemsManagementSoftwareEntry.setStatus('mandatory')
productAtt1 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 1), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: productAtt1.setStatus('mandatory')
versionAtt2 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 2), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: versionAtt2.setStatus('mandatory')
buildNumberAtt3 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 3), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: buildNumberAtt3.setStatus('mandatory')
descriptionAtt4 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 4), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: descriptionAtt4.setStatus('mandatory')
supportedProtocolsAtt5 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 5), DmiInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: supportedProtocolsAtt5.setStatus('mandatory')
preferredProtocolAtt6 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("sNMP", 1), ("dMIRPC", 2), ("cIMOM", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: preferredProtocolAtt6.setStatus('mandatory')
dMIRPCTypesAtt7 = MibTableColumn((1, 3, 6, 1, 4, 1, 674, 10891, 400, 1, 7), DmiDisplaystring()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dMIRPCTypesAtt7.setStatus('mandatory')
mibBuilder.exportSymbols("DCLRA-MIB-MIB", dellLRAActionTableState=dellLRAActionTableState, dellLRACapabilitiesEntry=dellLRACapabilitiesEntry, dMTFComponentIDEntry=dMTFComponentIDEntry, DmiGauge=DmiGauge, manufacturerAtt1=manufacturerAtt1, DmiCompId=DmiCompId, DmiGroupId=DmiGroupId, verifyAtt6=verifyAtt6, beepClearAtt1=beepClearAtt1, DmiOctetstring=DmiOctetstring, productAtt1=productAtt1, dellLRABeepActionEntry=dellLRABeepActionEntry, versionAtt2=versionAtt2, dmtfDynOids=dmtfDynOids, actionResponseAtt2=actionResponseAtt2, dmtfServiceLayerMIF=dmtfServiceLayerMIF, uDPInformationAtt5=uDPInformationAtt5, dellLRAActionTableTable=dellLRAActionTableTable, dMTFComponentIDTable=dMTFComponentIDTable, dell=dell, server2=server2, DmiCounter64=DmiCounter64, dELLSystemsManagementSoftwareEntry=dELLSystemsManagementSoftwareEntry, lRACapabilitiesAtt1=lRACapabilitiesAtt1, preferredProtocolAtt6=preferredProtocolAtt6, dmtfStdMifs=dmtfStdMifs, productAtt2=productAtt2, versionAtt3=versionAtt3, supportedProtocolsAtt5=supportedProtocolsAtt5, dMIRPCTypesAtt7=dMIRPCTypesAtt7, dellLRAActionTableEntry=dellLRAActionTableEntry, DmiCounter=DmiCounter, beepDelayAtt2=beepDelayAtt2, buildNumberAtt3=buildNumberAtt3, DmiDisplaystring=DmiDisplaystring, installationAtt5=installationAtt5, dELLSystemsManagementSoftwareTable=dELLSystemsManagementSoftwareTable, dellLRABeepActionTable=dellLRABeepActionTable, actionExecuteAtt3=actionExecuteAtt3, dellLRACapabilitiesTable=dellLRACapabilitiesTable, serialNumberAtt4=serialNumberAtt4, actionNameAtt1=actionNameAtt1, descriptionAtt4=descriptionAtt4, DmiInteger=DmiInteger, dmtf=dmtf, actionSourceAtt4=actionSourceAtt4)
