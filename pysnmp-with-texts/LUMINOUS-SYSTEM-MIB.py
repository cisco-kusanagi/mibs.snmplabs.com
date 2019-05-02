#
# PySNMP MIB module LUMINOUS-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LUMINOUS-SYSTEM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:09:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
LumSimpleIndex, LumSignalState, LumDescr, LumName, LumAdminStatus, LumVersionString, LumSlotNum, LumAlarmSeverity, LumResetCmd, LumOperStatus, LumCardBaseType, LumPortNum = mibBuilder.importSymbols("LUMINOUS-TC-MIB", "LumSimpleIndex", "LumSignalState", "LumDescr", "LumName", "LumAdminStatus", "LumVersionString", "LumSlotNum", "LumAlarmSeverity", "LumResetCmd", "LumOperStatus", "LumCardBaseType", "LumPortNum")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Bits, ObjectIdentity, IpAddress, Counter64, Integer32, Unsigned32, Counter32, MibIdentifier, Gauge32, ModuleIdentity, enterprises, NotificationType, ObjectName = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Bits", "ObjectIdentity", "IpAddress", "Counter64", "Integer32", "Unsigned32", "Counter32", "MibIdentifier", "Gauge32", "ModuleIdentity", "enterprises", "NotificationType", "ObjectName")
DisplayString, TextualConvention, RowStatus, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "DateAndTime")
luminous = MibIdentifier((1, 3, 6, 1, 4, 1, 4614))
lumADM = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1))
lumSystemMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4614, 1, 4))
lumSystemMIB.setRevisions(('1901-06-27 00:00', '1901-05-24 00:00', '1900-10-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: lumSystemMIB.setRevisionsDescriptions(('Added new LumAlarmSeverity TC and reformatted.', 'Added lumDownLoadImageType values: wdmBand1(24), wdmBand2(25), wdmBand3(26), wdmBand4(27), ds3cc12(28), ds3cc12IO(29), t3cc12(30), e3cc12(31)', 'Added ring primary and secorndary los.',))
if mibBuilder.loadTexts: lumSystemMIB.setLastUpdated('0007250000Z')
if mibBuilder.loadTexts: lumSystemMIB.setOrganization('Luminous Networks')
if mibBuilder.loadTexts: lumSystemMIB.setContactInfo(' Luminous Technical Support Postal: Luminous Networks, 14060 Bubb Road, Cupertino, CA 95014 Tel: +1 408 342 6400 Fax: +1 408 863 1100 E-mail: support@luminousnetworks.com')
if mibBuilder.loadTexts: lumSystemMIB.setDescription('The Luminous System MIB contains information related to the Luminous system configurations and monitoring.')
lumSoftwareDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1))
lumSystemReset = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2))
lumAlarms = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3))
lumAlarmType = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1))
lumAlarmSource = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 2))
lumAlarmLog = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4))
lumAlarmSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5))
lumAlarmTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 10))
lumAlarmV2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 0))
lumDownLoadImageType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 1), LumCardBaseType().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadImageType.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadImageType.setDescription('The type of image to be downloaded.')
lumDownLoadHost = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadHost.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadHost.setDescription('The IP address or name of the image downloading host.')
lumDownLoadUsrName = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadUsrName.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadUsrName.setDescription('The user logging name for accessing the image downloading host.')
lumDownLoadPasswd = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadPasswd.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadPasswd.setDescription('The password associated with the lumDownLoadUsrName when accessing the image downloading host.')
lumDownLoadFilePath = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadFilePath.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadFilePath.setDescription('The image file name and its directory path on the downloading host.')
lumDownLoadVersion = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 6), LumVersionString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadVersion.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadVersion.setDescription('The version number of the image file to be downloaded.')
lumDownLoadSlot = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 7), LumSlotNum()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadSlot.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadSlot.setDescription('The slot number to which the image will be downloaded to. When the slot number is 0, all the applicable cards are to be downloaded with the image.')
lumDownLoadTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 8), Integer32().clone(10)).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadTimeOut.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadTimeOut.setDescription('The length of time, in minutes, that agent allows the download process to continue.')
lumDownLoadCmd = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("download", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadCmd.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadCmd.setDescription('Set object to download(2) to active the image download process. The image downloading related objects should have been properly configuered. The download command will be rejected if the the lumDownLoadStatus has a value of download-in-progress(2).')
lumDownLoadStatus = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("download-in-progress", 2), ("download-succeeded", 3), ("download-failed", 4))).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumDownLoadStatus.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadStatus.setDescription('The status of a previously issued software download command.')
lumDownLoadAbort = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("abort", 2))).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumDownLoadAbort.setStatus('current')
if mibBuilder.loadTexts: lumDownLoadAbort.setDescription('Abort the software download process.')
lumSystemResetCardTable = MibTable((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1), )
if mibBuilder.loadTexts: lumSystemResetCardTable.setStatus('deprecated')
if mibBuilder.loadTexts: lumSystemResetCardTable.setDescription('The Luminous line card reset table.')
lumSystemResetCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1, 1), ).setIndexNames((0, "LUMINOUS-SYSTEM-MIB", "lumSystemResetCardIndex"))
if mibBuilder.loadTexts: lumSystemResetCardEntry.setStatus('deprecated')
if mibBuilder.loadTexts: lumSystemResetCardEntry.setDescription('An lumSystemResetCardEntry contains a line card to be reset.')
lumSystemResetCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1, 1, 1), LumSlotNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumSystemResetCardIndex.setStatus('deprecated')
if mibBuilder.loadTexts: lumSystemResetCardIndex.setDescription('The line card number.')
lumSystemResetCardCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 1, 1, 2), LumResetCmd()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumSystemResetCardCmd.setStatus('deprecated')
if mibBuilder.loadTexts: lumSystemResetCardCmd.setDescription('Reset a line card. This will always return none on read.')
lumSystemResetShelfCmd = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 2, 2), LumResetCmd()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lumSystemResetShelfCmd.setStatus('deprecated')
if mibBuilder.loadTexts: lumSystemResetShelfCmd.setDescription('Reset the Luminous shelf. This will always return none on read.')
lumProvisionAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("provCardFailedNoBackup", 1), ("provCardFailedWithBackup", 2))))
if mibBuilder.loadTexts: lumProvisionAlarmType.setStatus('current')
if mibBuilder.loadTexts: lumProvisionAlarmType.setDescription('The provision Alarms.')
lumAlarmCardAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("input0", 1), ("input1", 2), ("input2", 3), ("input3", 4), ("input4", 5), ("input5", 6), ("input6", 7), ("input7", 8), ("alarmCardFailedNoBackup", 9), ("alarmCardFailedWithBackup", 10), ("card-lost", 11))))
if mibBuilder.loadTexts: lumAlarmCardAlarmType.setStatus('current')
if mibBuilder.loadTexts: lumAlarmCardAlarmType.setDescription('The Alarm card Alarms.')
lumSysconAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cmmlf", 1), ("redundancy-lost", 2))))
if mibBuilder.loadTexts: lumSysconAlarmType.setStatus('current')
if mibBuilder.loadTexts: lumSysconAlarmType.setDescription('The Syscon card Alarms.')
lumT1AlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("bpv", 1), ("lof", 2), ("los", 3), ("ais", 4), ("rai", 5), ("ovrfl", 6), ("sf-ber", 7), ("sf-es", 8), ("sf-ses", 9), ("tcfl", 10))))
if mibBuilder.loadTexts: lumT1AlarmType.setStatus('current')
if mibBuilder.loadTexts: lumT1AlarmType.setDescription('The T1 card Alarms.')
lumTEN100AlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("an-fail", 1), ("los", 2), ("symer", 3), ("rxer", 4), ("frlex", 5), ("aler", 6), ("fcserr", 7))))
if mibBuilder.loadTexts: lumTEN100AlarmType.setStatus('current')
if mibBuilder.loadTexts: lumTEN100AlarmType.setDescription('The 10/100 card Alarms.')
lumSonetAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))).clone(namedValues=NamedValues(("laser-loop", 1), ("laser-bias", 2), ("laser-pwr", 3), ("loss-of-sync", 4), ("los-s", 5), ("lof-s", 6), ("ais-l", 7), ("rfi-l", 8), ("sf-ber", 9), ("sd-ber", 10), ("ais-p", 11), ("rfi-p", 12), ("lop-p", 13), ("uneq-p", 14), ("plm-p", 15), ("aps-k1", 16), ("aps-k2", 17), ("aps-mode", 18), ("aps-far-end", 19), ("aps-success", 20), ("aps-failed", 21))))
if mibBuilder.loadTexts: lumSonetAlarmType.setStatus('current')
if mibBuilder.loadTexts: lumSonetAlarmType.setDescription('The Sonet card Alarms.')
lumRingCardAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("los", 1), ("losynch", 2), ("sf-ber", 3), ("sd-ber", 4), ("pri-los", 5), ("sec-los", 6), ("io-west-lost", 7), ("io-east-lost", 8), ("io-card-lost", 9), ("switch-fabric-lost", 10), ("switch-fabric-redundancy-lost", 11))))
if mibBuilder.loadTexts: lumRingCardAlarmType.setStatus('current')
if mibBuilder.loadTexts: lumRingCardAlarmType.setDescription('The Ring card Alarms.')
lumUtilityAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("vltg", 1), ("hitmp", 2), ("pwra", 3), ("pwrb", 4), ("card-lost", 5))))
if mibBuilder.loadTexts: lumUtilityAlarmType.setStatus('current')
if mibBuilder.loadTexts: lumUtilityAlarmType.setDescription('The Utility card Alarms.')
lumEquipmentAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("fncrt", 1), ("fnmjr", 2), ("boot", 3), ("hwfl", 4), ("hitmp", 5), ("vltg", 6), ("trans-mea", 7), ("sgeo", 8), ("ueq", 9), ("mea", 10), ("prov-io-card-lost", 11), ("io-card-lost", 12), ("prov-io-card-mismatched", 13), ("io-card-mismatched", 14))))
if mibBuilder.loadTexts: lumEquipmentAlarmType.setStatus('current')
if mibBuilder.loadTexts: lumEquipmentAlarmType.setDescription('The Equipment Alarms.')
lumDataFlowAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sf-dfc", 1), ("sf-ifc", 2), ("sf-bfc", 3))))
if mibBuilder.loadTexts: lumDataFlowAlarmType.setStatus('current')
if mibBuilder.loadTexts: lumDataFlowAlarmType.setDescription('The Data Flow Alarms.')
lumDataBaseAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("saveFailed", 1), ("restoreFailed", 2))))
if mibBuilder.loadTexts: lumDataBaseAlarmType.setStatus('current')
if mibBuilder.loadTexts: lumDataBaseAlarmType.setDescription('The Data Base Alarms.')
lumPPPAlarmType = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("linkDown", 1))))
if mibBuilder.loadTexts: lumPPPAlarmType.setStatus('current')
if mibBuilder.loadTexts: lumPPPAlarmType.setDescription('The PPP Alarms.')
lumAlarmSlotId = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 2, 1), LumSlotNum())
if mibBuilder.loadTexts: lumAlarmSlotId.setStatus('current')
if mibBuilder.loadTexts: lumAlarmSlotId.setDescription("The card's slot number. Starts with 1 for the both front plane and for the back plane.")
lumAlarmPortId = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 2, 2), LumPortNum())
if mibBuilder.loadTexts: lumAlarmPortId.setStatus('current')
if mibBuilder.loadTexts: lumAlarmPortId.setDescription("The card's port number.")
lumAlarmStatus = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("alarmClear", 1), ("alarmSet", 2), ("alarmMasked", 3))))
if mibBuilder.loadTexts: lumAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: lumAlarmStatus.setDescription('The status of the alarm.')
lumAlarmSummaryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1))
lumAlarmSummaryState = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 1), LumAlarmSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmSummaryState.setStatus('current')
if mibBuilder.loadTexts: lumAlarmSummaryState.setDescription('This reflect the highest severity of any active alarm.')
lumAlarmSummaryCriticalStatus = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 2), LumSignalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmSummaryCriticalStatus.setStatus('current')
if mibBuilder.loadTexts: lumAlarmSummaryCriticalStatus.setDescription('This is active if one or more critical alarms are active.')
lumAlarmSummaryMajorStatus = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 3), LumSignalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmSummaryMajorStatus.setStatus('current')
if mibBuilder.loadTexts: lumAlarmSummaryMajorStatus.setDescription('This is active if one or more major alarms are active.')
lumAlarmSummaryMinorStatus = MibScalar((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 5, 1, 4), LumSignalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmSummaryMinorStatus.setStatus('current')
if mibBuilder.loadTexts: lumAlarmSummaryMinorStatus.setDescription('This is active if one or more minor alarms are active.')
lumAlarmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1), )
if mibBuilder.loadTexts: lumAlarmActiveTable.setStatus('current')
if mibBuilder.loadTexts: lumAlarmActiveTable.setDescription('The Luminous active alarms table which contains all the currently active alarms.')
lumAlarmActiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1), ).setIndexNames((0, "LUMINOUS-SYSTEM-MIB", "lumAlarmActiveIndex"))
if mibBuilder.loadTexts: lumAlarmActiveEntry.setStatus('current')
if mibBuilder.loadTexts: lumAlarmActiveEntry.setDescription('An lumAlarmActive Entry contains the information for an active alarm.')
lumAlarmActiveIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveIndex.setStatus('current')
if mibBuilder.loadTexts: lumAlarmActiveIndex.setDescription('This is the index to the actvie alarm log.')
lumAlarmActiveType = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("provision", 1), ("alarmCard", 2), ("syscon", 3), ("t1", 4), ("tEN100", 5), ("sonet", 6), ("ringCard", 7), ("utility", 8), ("equipment", 9), ("dataFlow", 10), ("dataBase", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveType.setStatus('current')
if mibBuilder.loadTexts: lumAlarmActiveType.setDescription('The alarm type which corresponds to one of the types defined under lumAlarmType.')
lumAlarmActiveValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveValue.setStatus('current')
if mibBuilder.loadTexts: lumAlarmActiveValue.setDescription('The specific alarm. The meaning of the value of this object can be found by looking up the enums defined uner lumAlarmType.')
lumAlarmActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("alarmClear", 1), ("alarmSet", 2), ("alarmMasked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveStatus.setStatus('current')
if mibBuilder.loadTexts: lumAlarmActiveStatus.setDescription('The active alarm status.')
lumAlarmActiveTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveTimeStamp.setStatus('current')
if mibBuilder.loadTexts: lumAlarmActiveTimeStamp.setDescription('The alarm time stamp.')
lumAlarmActiveSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 6), LumSlotNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActiveSlotId.setStatus('current')
if mibBuilder.loadTexts: lumAlarmActiveSlotId.setDescription("The card's slot number. Slot number 0 is used for alarms that do not associate with a particular slot.")
lumAlarmActivePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 1, 1, 7), LumPortNum()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmActivePortId.setStatus('current')
if mibBuilder.loadTexts: lumAlarmActivePortId.setDescription("The card's port number. Port number 0 is used for alarms that do not associate with a particular port.")
lumAlarmHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2), )
if mibBuilder.loadTexts: lumAlarmHistoryTable.setStatus('current')
if mibBuilder.loadTexts: lumAlarmHistoryTable.setDescription('The Luminous alarms history table which contains all the occured alarms. The actual retrieveable alarm entries depends on system memory utilization')
lumAlarmHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2, 1), ).setIndexNames((0, "LUMINOUS-SYSTEM-MIB", "lumAlarmHistoryIndex"))
if mibBuilder.loadTexts: lumAlarmHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: lumAlarmHistoryEntry.setDescription('An lumAlarmHistoryEntry contains the information for an occured alarm.')
lumAlarmHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmHistoryIndex.setStatus('current')
if mibBuilder.loadTexts: lumAlarmHistoryIndex.setDescription('This is the index to the alarm history table.')
lumAlarmHistoryData = MibTableColumn((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 4, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lumAlarmHistoryData.setStatus('current')
if mibBuilder.loadTexts: lumAlarmHistoryData.setDescription('The text message of the alarm.')
lumAlarmSummaryChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 4614, 1, 4, 3, 0, 1)).setObjects(("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryState"), ("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryCriticalStatus"), ("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryMajorStatus"), ("LUMINOUS-SYSTEM-MIB", "lumAlarmSummaryMinorStatus"))
if mibBuilder.loadTexts: lumAlarmSummaryChangeTrap.setStatus('current')
if mibBuilder.loadTexts: lumAlarmSummaryChangeTrap.setDescription('This notification is issued when the Alarm Summary information changes.')
mibBuilder.exportSymbols("LUMINOUS-SYSTEM-MIB", lumDownLoadCmd=lumDownLoadCmd, lumDataFlowAlarmType=lumDataFlowAlarmType, lumAlarmSummaryGroup=lumAlarmSummaryGroup, lumAlarmSummaryState=lumAlarmSummaryState, lumDownLoadStatus=lumDownLoadStatus, lumDataBaseAlarmType=lumDataBaseAlarmType, lumAlarmActiveEntry=lumAlarmActiveEntry, lumDownLoadUsrName=lumDownLoadUsrName, lumSystemResetCardTable=lumSystemResetCardTable, lumSysconAlarmType=lumSysconAlarmType, lumDownLoadSlot=lumDownLoadSlot, lumDownLoadImageType=lumDownLoadImageType, lumAlarmType=lumAlarmType, lumAlarmPortId=lumAlarmPortId, lumDownLoadPasswd=lumDownLoadPasswd, lumAlarmActiveValue=lumAlarmActiveValue, lumAlarmHistoryTable=lumAlarmHistoryTable, lumSystemResetCardCmd=lumSystemResetCardCmd, PYSNMP_MODULE_ID=lumSystemMIB, lumAlarmActiveIndex=lumAlarmActiveIndex, lumT1AlarmType=lumT1AlarmType, lumAlarmSlotId=lumAlarmSlotId, lumUtilityAlarmType=lumUtilityAlarmType, lumAlarmCardAlarmType=lumAlarmCardAlarmType, lumAlarmStatus=lumAlarmStatus, lumAlarmTraps=lumAlarmTraps, lumAlarmSummaryCriticalStatus=lumAlarmSummaryCriticalStatus, luminous=luminous, lumAlarmActiveType=lumAlarmActiveType, lumDownLoadFilePath=lumDownLoadFilePath, lumSystemResetCardEntry=lumSystemResetCardEntry, lumPPPAlarmType=lumPPPAlarmType, lumAlarmSummaryMinorStatus=lumAlarmSummaryMinorStatus, lumAlarmHistoryEntry=lumAlarmHistoryEntry, lumAlarmHistoryIndex=lumAlarmHistoryIndex, lumEquipmentAlarmType=lumEquipmentAlarmType, lumDownLoadTimeOut=lumDownLoadTimeOut, lumTEN100AlarmType=lumTEN100AlarmType, lumDownLoadHost=lumDownLoadHost, lumSystemResetShelfCmd=lumSystemResetShelfCmd, lumSystemMIB=lumSystemMIB, lumSystemReset=lumSystemReset, lumAlarmHistoryData=lumAlarmHistoryData, lumSoftwareDownload=lumSoftwareDownload, lumAlarmSummaryMajorStatus=lumAlarmSummaryMajorStatus, lumAlarmV2Traps=lumAlarmV2Traps, lumSystemResetCardIndex=lumSystemResetCardIndex, lumAlarmActiveSlotId=lumAlarmActiveSlotId, lumAlarmActivePortId=lumAlarmActivePortId, lumAlarmActiveStatus=lumAlarmActiveStatus, lumAlarmSummaryChangeTrap=lumAlarmSummaryChangeTrap, lumAlarmLog=lumAlarmLog, lumSonetAlarmType=lumSonetAlarmType, lumAlarmActiveTable=lumAlarmActiveTable, lumRingCardAlarmType=lumRingCardAlarmType, lumDownLoadAbort=lumDownLoadAbort, lumAlarmSummary=lumAlarmSummary, lumADM=lumADM, lumAlarmSource=lumAlarmSource, lumAlarms=lumAlarms, lumAlarmActiveTimeStamp=lumAlarmActiveTimeStamp, lumProvisionAlarmType=lumProvisionAlarmType, lumDownLoadVersion=lumDownLoadVersion)
