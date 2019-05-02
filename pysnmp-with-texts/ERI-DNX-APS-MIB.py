#
# PySNMP MIB module ERI-DNX-APS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ERI-DNX-APS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:05:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
trapSequence, utilities, OneByteField, FunctionSwitch, DataSwitch, dnxTrapEnterprise, NestSlotAddress = mibBuilder.importSymbols("ERI-DNX-SMC-MIB", "trapSequence", "utilities", "OneByteField", "FunctionSwitch", "DataSwitch", "dnxTrapEnterprise", "NestSlotAddress")
eriMibs, = mibBuilder.importSymbols("ERI-ROOT-SMI", "eriMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, ModuleIdentity, IpAddress, Bits, Counter32, NotificationType, TimeTicks, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "ModuleIdentity", "IpAddress", "Bits", "Counter32", "NotificationType", "TimeTicks", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eriDNXApsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 644, 3, 13))
eriDNXApsMIB.setRevisions(('2002-05-14 00:00', '2002-04-29 00:00', '2002-04-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eriDNXApsMIB.setRevisionsDescriptions(('Nevio Poljak - eri_DnxNest MIB Rev 01.0a Added new enumeration err-invalid-aps-command (408) to apsSwitchCmdStatus field. Fixes Bug #3617.', 'Nevio Poljak - Release 14.2 Converted to SMIv2 format.', 'Nevio Poljak for Release 14.1 Initial Release of this MIB.',))
if mibBuilder.loadTexts: eriDNXApsMIB.setLastUpdated('200205140000Z')
if mibBuilder.loadTexts: eriDNXApsMIB.setOrganization('Eastern Research, Inc.')
if mibBuilder.loadTexts: eriDNXApsMIB.setContactInfo('Customer Service Postal: Eastern Research, Inc. 225 Executive Drive Moorestown, NJ 08057 Phone: +1-800-337-4374 Email: support@erinc.com')
if mibBuilder.loadTexts: eriDNXApsMIB.setDescription('The ERI Enterprise MIB Module for the Automatic Protection Switching.')
dnxAPS = MibIdentifier((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2))
class ApsSwitchRequestCode(TextualConvention, Integer32):
    description = 'The APS switch Request codes are used to perform protection switch actions. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 8, 10, 11, 12, 13, 14, 15, 31))
    namedValues = NamedValues(("noRequest", 0), ("doNotRevert", 1), ("reverseRequest", 2), ("manualSwitch", 8), ("signalDegradeLow", 10), ("signalDegradeHigh", 11), ("signalFailureLow", 12), ("signalFailureHigh", 13), ("forceSwitch", 14), ("lockout", 15), ("clearRequest", 31))

apsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1), )
if mibBuilder.loadTexts: apsConfigTable.setStatus('current')
if mibBuilder.loadTexts: apsConfigTable.setDescription("This is the APS Configuration table which consists of an entry for each STM1/STM1X or OC3/OC3X card in the system. The total number of entries depends on the number of STM1/OC3 cards in the Node. Changes to the APS Configuration must be made on a record or row by row basis. This means that any use of the Set command on writable fields must include the apsCfgCmdStatus field with a value of 'update' as the last variable in the SET PDU.")
apsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1), ).setIndexNames((0, "ERI-DNX-APS-MIB", "apsCfgAddr"))
if mibBuilder.loadTexts: apsConfigEntry.setStatus('current')
if mibBuilder.loadTexts: apsConfigEntry.setDescription("The conceptual row of the APS Configuration table. A row in this table cannot be added or deleted, only modified using the apsCfgCmdStatus field with a value of 'update' as the last variable in the SET PDU. The apsCfgCmdStatus field must be included as the last variable in a SET PDU for the action to take effect. If the apsCfgCmdStatus is missing from the SET PDU, the GET RESPONSE will contain the SNMP error status of 'genErr' for and an error index equal to the last variable.")
apsCfgAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 1), NestSlotAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsCfgAddr.setStatus('current')
if mibBuilder.loadTexts: apsCfgAddr.setDescription('This number uniquely identifies Nest/Slot configured location of the APS Device card. The format is represented using an IP address syntax (4 byte string). Note that the maximum valid slot number will vary depending on the specified Nest type: DNX11 or DNX4. The 1st byte represents the Nest Number (0-7) The 2nd byte represents the Slot Number (1-11) The 3rd byte is reserved for future use The 4th byte is reserved for future use ')
apsCfgResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsCfgResource.setStatus('current')
if mibBuilder.loadTexts: apsCfgResource.setDescription('Uniquely identifies an APS Device in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
apsCfgCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("stm1", 0), ("oc3", 1), ("stm1X", 2), ("oc3X", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsCfgCardType.setStatus('current')
if mibBuilder.loadTexts: apsCfgCardType.setDescription('Identifies the APS Device as an STM1, OC3, STM1X, or OC3X module.')
apsCfgSfThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsCfgSfThreshold.setStatus('current')
if mibBuilder.loadTexts: apsCfgSfThreshold.setDescription('The configured Signal Failure Threshold. The negated value of this number is used as the exponent of 10 for computing the threshold value for the Bit Error Rate(BER). For example, a value of 5 indicates a BER threshold of 10^-5.')
apsCfgSdThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsCfgSdThreshold.setStatus('current')
if mibBuilder.loadTexts: apsCfgSdThreshold.setDescription('The configured Signal Degrade Threshold. The negated value of this number is used as the exponent of 10 for computing the threshold value for the Bit Error Rate(BER). For example, a value of 5 indicates a BER threshold of 10^-5.')
apsCfgRdiSfCriteria = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 6), FunctionSwitch()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsCfgRdiSfCriteria.setStatus('current')
if mibBuilder.loadTexts: apsCfgRdiSfCriteria.setDescription('Enables or Disables switchover on Remote Defect Indication.')
apsCfgCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 101, 400, 401, 402, 403, 404, 450, 500, 501, 502))).clone(namedValues=NamedValues(("ready-for-command", 0), ("update-config", 1), ("update-successful", 101), ("err-general-aps-config-error", 400), ("err-invalid-asp-threshold", 401), ("err-invalid-rdi-criteria", 402), ("err-invalid-aps-dev-command", 403), ("err-aps-not-applicable", 404), ("err-data-locked-by-another-user", 450), ("err-snmp-parse-failed", 500), ("err-invalid-snmp-type", 501), ("err-invalid-snmp-var-size", 502)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsCfgCmdStatus.setStatus('current')
if mibBuilder.loadTexts: apsCfgCmdStatus.setDescription('The command status for this link configuration row/record. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. Default Response State used in GET RESPONSE Command ready-for-command (0) initial default status for a row APS Cfg Commands used in SET Command (1..199) update-config(1), Change existing APS Configuration APS Cfg Response States used in GET RESPONSE Command (100..199) update-successful (201) Device data has been successfully changed APS Config Error Codes used in GET RESPONSE Command (400..799) err-general-aps-config-error (400) Unknown APS configuration error occurred err-invalid-asp-threshold (401) Unrecognized APS SD or SF threshold number err-invalid-rdi-criteria (402) Unrecognized APS RDI setting err-invalid-aps-dev-command (403) Unrecognized APS device command-action err-aps-not-applicable (404) APS cannot be configured for this device err-data-locked-by-another-user (450) Another administrative user is making changes to this part of the system via a terminal session. Check Event Log for user name. err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big')
apsStatusTable = MibTable((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2), )
if mibBuilder.loadTexts: apsStatusTable.setStatus('current')
if mibBuilder.loadTexts: apsStatusTable.setDescription("This is the APS Status table which consists of an entry for each STM1/STM1X or OC3/OC3X card in the system. The total number of entries depends on the number of STM1/OC3 cards in the Node. Changes to the APS Configuration must be made on a record or row by row basis. This means that any use of the Set command on writable fields must include the apsCfgCmdStatus field with a value of 'update' as the last variable in the SET PDU.")
apsStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1), ).setIndexNames((0, "ERI-DNX-APS-MIB", "apsStatusAddr"))
if mibBuilder.loadTexts: apsStatusEntry.setStatus('current')
if mibBuilder.loadTexts: apsStatusEntry.setDescription("The conceptual row of the APS Status table. A row in this table cannot be added or deleted, only modified using the apsCfgCmdStatus field with a value of 'update' as the last variable in the SET PDU. The apsCfgCmdStatus field must be included as the last variable in a SET PDU for the action to take effect. If the apsCfgCmdStatus is missing from the SET PDU, the GET RESPONSE will contain the SNMP error status of 'genErr' for and an error index equal to the last variable.")
apsStatusAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 1), NestSlotAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusAddr.setStatus('current')
if mibBuilder.loadTexts: apsStatusAddr.setDescription('This number uniquely identifies Nest/Slot configured location of the APS Device card. The format is represented using an IP address syntax (4 byte string). Note that the maximum valid slot number will vary depending on the specified Nest type: DNX11 or DNX4. The 1st byte represents the Nest Number (0-7) The 2nd byte represents the Slot Number (1-11) The 3rd byte is reserved for future use The 4th byte is reserved for future use ')
apsStatusResource = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusResource.setStatus('current')
if mibBuilder.loadTexts: apsStatusResource.setDescription('Uniquely identifies an APS Device in the system. This number is provided as key to allow the manager to map this entry to a corresponding Resource Table entry.')
apsStatusCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("stm1Working", 1), ("stm1Protection", 2), ("oc3Working", 3), ("oc3Protection", 4), ("stm1XWorking", 5), ("stm1XProtection", 6), ("oc3XWorking", 7), ("oc3XProtection", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusCardType.setStatus('current')
if mibBuilder.loadTexts: apsStatusCardType.setDescription('Identifies the Type of APS Device module.')
apsStatusCardState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("standby", 1), ("online", 2), ("offline", 3), ("defective", 4), ("busError", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsStatusCardState.setStatus('current')
if mibBuilder.loadTexts: apsStatusCardState.setDescription('Identifies the current APS Device Card State.')
apsRedundancyState = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("detected", 0), ("notDetected", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsRedundancyState.setStatus('current')
if mibBuilder.loadTexts: apsRedundancyState.setDescription('Identifies the current APS Device Redundancy State.')
apsSignalFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 6), DataSwitch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsSignalFailure.setStatus('current')
if mibBuilder.loadTexts: apsSignalFailure.setDescription('Identifies the current APS SF State.')
apsSignalDegrade = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 7), DataSwitch()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsSignalDegrade.setStatus('current')
if mibBuilder.loadTexts: apsSignalDegrade.setDescription('Identifies the current APS SD State.')
apsLineRxK1Byte = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 8), OneByteField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsLineRxK1Byte.setStatus('current')
if mibBuilder.loadTexts: apsLineRxK1Byte.setDescription('Displays the SONET K1 byte APS protocol field. Bits are numbered from left to right. Bits 1-4 of the K1 byte indicate a request. 1111 Lockout of Protection 1110 Forced Switch 1101 SF - High Priority 1100 SF - Low Priority 1011 SD - High Priority 1010 SD - Low Priority 1001 not used 1000 Manual Switch 0111 not used 0110 Wait-to-Restore 0101 not used 0100 Exercise 0011 not used 0010 Reverse Request 0001 Do Not Revert 0000 No Request Bits 5-8 of the K1 byte indicate the channel associated with the request defined in bits 1-4. 0000 is the Null channel. 1-14 are working channels. 15 is the extra traffic channel ')
apsLineRxK2Byte = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 9), OneByteField()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsLineRxK2Byte.setStatus('current')
if mibBuilder.loadTexts: apsLineRxK2Byte.setDescription('Displays the SONET K2 byte APS protocol field. Bits are numbered from left to right. Bits 1-4 of the K2 byte indicate a channel. The channel is defined with the same syntax as K1 Bits 5-8. 0000 is the Null channel. 1-14 are working channels. 15 is the extra traffic channel Bit 5 of the K2 byte indicates the architecture. 0 if the architecture is 1+1 1 if the architecture is 1:n Bits 6-8 of the K2 byte indicates the mode. 000 - 011 are reserved for future use 100 indicates the mode is unidirectional 101 indicates the mode is bidirectional 110 RDI-L 111 AIS-L ')
apsSysRxReqCode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 10), ApsSwitchRequestCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsSysRxReqCode.setStatus('current')
if mibBuilder.loadTexts: apsSysRxReqCode.setDescription('Identifies the last APS Protocol Request received by this APS Device.')
apsSysTxReqCode = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 11), ApsSwitchRequestCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsSysTxReqCode.setStatus('current')
if mibBuilder.loadTexts: apsSysTxReqCode.setDescription('Identifies the last User APS Protocol Pending Request transmitted by this APS Device.')
apsUserPendingReq = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 12), ApsSwitchRequestCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apsUserPendingReq.setStatus('current')
if mibBuilder.loadTexts: apsUserPendingReq.setDescription('Identifies the current User APS Protocol Pending Request.')
apsSwitchCmdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 644, 2, 4, 1, 12, 2, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 8, 14, 31, 108, 114, 131, 400, 402, 406, 408, 500, 501, 502))).clone(namedValues=NamedValues(("readyForRequest", 0), ("manualSwitchReq", 8), ("forceSwitchReq", 14), ("clearRequest", 31), ("manual-successful", 108), ("force-successful", 114), ("clear-successful", 131), ("err-gen-aps-req-error", 400), ("err-invalid-aps-card-type", 402), ("err-field-cannot-be-set", 406), ("err-invalid-aps-command", 408), ("err-snmp-parse-failed", 500), ("err-invalid-snmp-type", 501), ("err-invalid-snmp-var-size", 502)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: apsSwitchCmdStatus.setStatus('current')
if mibBuilder.loadTexts: apsSwitchCmdStatus.setDescription('This is the command/status value for the APS Status Row. The value used in a SET will be replaced by a response value in the GET RESPONSE indicating success or failure. These commands can only be SET in the Working APS Device. Default Response State used in GET RESPONSE Command readyForRequest (0) initial default status for a row APS Requests used in SET Command (1..99) manualSwitchReq (8) Manually Switches the specified working device to the protection device. forceSwitchReq (14) Switches the specified working device to the protection device. clearRequest (31) Clears all of the switch commands for the specified APS device. Response States used in GET RESPONSE Command (100..199) manual-successful (108) Manual Switch command has been successfully processed force-successful (114) Forced Switch command has been successfully processed clear-successful (131) Switch commands been successfully cleared Error Codes used in GET RESPONSE Command (400..799) err-gen-aps-req-error (400) Unknown APS request error occurred err-invalid-aps-card-type (402) Requests cannot be processed by the protection card err-field-cannot-be-set (406) Read-only field was included in SET request err-invalid-aps-command (408) Invalid APS request err-snmp-parse-failed (500) Agent could not parse variable err-invalid-snmp-type (501) Variable ASN type does not match Agent defined type err-invalid-snmp-var-size (502) Variable size is too big')
apsConfigTrap = NotificationType((1, 3, 6, 1, 4, 1, 644, 2, 4, 0, 11)).setObjects(("ERI-DNX-SMC-MIB", "trapSequence"), ("ERI-DNX-APS-MIB", "apsCfgAddr"), ("ERI-DNX-APS-MIB", "apsCfgCmdStatus"))
if mibBuilder.loadTexts: apsConfigTrap.setStatus('current')
if mibBuilder.loadTexts: apsConfigTrap.setDescription('This trap is used to notify a NMS that a user has updated the configuration for a given APS Device entry.')
mibBuilder.exportSymbols("ERI-DNX-APS-MIB", apsCfgCardType=apsCfgCardType, eriDNXApsMIB=eriDNXApsMIB, apsCfgCmdStatus=apsCfgCmdStatus, apsLineRxK2Byte=apsLineRxK2Byte, apsSignalDegrade=apsSignalDegrade, apsLineRxK1Byte=apsLineRxK1Byte, apsCfgAddr=apsCfgAddr, ApsSwitchRequestCode=ApsSwitchRequestCode, apsStatusTable=apsStatusTable, apsSysTxReqCode=apsSysTxReqCode, apsConfigTable=apsConfigTable, apsStatusCardState=apsStatusCardState, apsUserPendingReq=apsUserPendingReq, PYSNMP_MODULE_ID=eriDNXApsMIB, apsCfgResource=apsCfgResource, apsRedundancyState=apsRedundancyState, apsConfigTrap=apsConfigTrap, apsStatusAddr=apsStatusAddr, apsCfgRdiSfCriteria=apsCfgRdiSfCriteria, apsConfigEntry=apsConfigEntry, apsSysRxReqCode=apsSysRxReqCode, apsStatusCardType=apsStatusCardType, apsStatusEntry=apsStatusEntry, apsSwitchCmdStatus=apsSwitchCmdStatus, apsCfgSfThreshold=apsCfgSfThreshold, apsSignalFailure=apsSignalFailure, dnxAPS=dnxAPS, apsCfgSdThreshold=apsCfgSdThreshold, apsStatusResource=apsStatusResource)
