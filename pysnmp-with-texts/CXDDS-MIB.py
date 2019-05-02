#
# PySNMP MIB module CXDDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXDDS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:32:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
Alias, cxDds, SapIndex = mibBuilder.importSymbols("CXProduct-SMI", "Alias", "cxDds", "SapIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, Integer32, Counter32, NotificationType, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, Unsigned32, MibIdentifier, TimeTicks, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Integer32", "Counter32", "NotificationType", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "Unsigned32", "MibIdentifier", "TimeTicks", "ObjectIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ddsSlotTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1), )
if mibBuilder.loadTexts: ddsSlotTable.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotTable.setDescription('Identifies the configuration information for a specific DDS access point and its associated hardware port.')
ddsSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1), ).setIndexNames((0, "CXDDS-MIB", "ddsSlotNumber"))
if mibBuilder.loadTexts: ddsSlotEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotEntry.setDescription('Identifies the configuration information for a specific DDS access point and its associated hardware port.')
ddsSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotNumber.setDescription('Identifies a DDS access point by a numerical value. Each DDS access point has a unique value.')
ddsSlotAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 2), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotAlias.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotAlias.setDescription('Assigns a textual name to the DDS access point. Each access point requires a unique name. You may not assign the same name twice. Default Value: none Range of Values: up to 12 alphanumeric characters, the first must be a letter. Configuration Changed: operative')
ddsSlotRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotRowStatus.setDescription('Determines the status of the objects in a row. Default Value: valid Options: invalid (1): row is flagged, after next reset the values will be disabled and the row will be deleted from the table valid (2): values are enabled Configuration Changed: administrative')
ddsSlotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dds-not-present", 1), ("dds-present", 2), ("dds-present-failed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotStatus.setDescription('Identifies the status of the DDS option card as present, not present or present but failed. Default Value: none Options: dds-not-present (1) dds-present (2) dds-present-failed (3)')
ddsSlotConfigLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("telco-point-to-point", 1), ("telco-multipt", 2), ("ldm-timing-slave", 3), ("ldm-timing-master", 4))).clone('telco-point-to-point')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotConfigLineType.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotConfigLineType.setDescription('Assigns the DDS line configuration. Default Value: telco-point-to-point (1) Options: telco-point-to-point (1) telco-multipoint (2) idm-timing-slave (3) idm-timing-master (4) Configuration Changed: operative')
ddsSlotConfigLineService = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("clear-channel-64K", 1), ("switched-56K", 2), ("dds-56K", 3), ("dds-19200", 4), ("dds-9600", 5), ("dds-4800", 6), ("dds-2400", 7))).clone('dds-56K')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotConfigLineService.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotConfigLineService.setDescription('Assigns the DDS line service type. Default Value: dds-56K (2) Range of Values: clear-channel-64K (1) switched-56K (2) dds-56K (3) dds-19200 (4) dds-9600 (5) dds-4800 (6) dds-2400 (7) dds-1200 (8) Configuration Changed: operative')
ddsSlotConfigLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("no-loopback", 1), ("dte-loopback", 2), ("loop2", 3), ("loop3", 4), ("loop4", 5), ("remote-loop2", 6))).clone('no-loopback')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotConfigLoopback.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotConfigLoopback.setDescription('Specifies the DDS loopback type. Default Value: no-loopback (1) Range of Values: no-loopback (1) dte-loopback (2) loop2 (3), loop3 (4), loop4 (5) remote-loop2 (6) Configuration Changed: operative')
ddsSlotConfigRemLoop2LocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotConfigRemLoop2LocalAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotConfigRemLoop2LocalAddress.setDescription('Specifies the local address for V.54 remote loop2. Default Value: none Range of Values: 0 to 255 The 34 valid V.54 hex addresses include: 0x01, 0x03, 0x05, 0x07, 0x09, 0x0B, 0x0D, 0x0F, 0x11, 0x13, 0x15, 0x17, 0x19, 0x1B, 0x1D, 0x1F, 0x25, 0x27, 0x2B, 0x2D, 0x2F, 0x33, 0x35, 0x37, 0x3B, 0x3D, 0x3F, 0x55, 0x57, 0x5B, 0x5F, 0x6F, 0x77, 0x7F Configuration Changed: operative')
ddsSlotConfigRemLoop2RemoteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotConfigRemLoop2RemoteAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotConfigRemLoop2RemoteAddress.setDescription('Specifies the remote address for V.54 remote loop2. Range of Values: 0 to 255 Default Value: none Configuration Changed: operative')
ddsSlotConfigPatternGen = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no-pattern", 1), ("pattern-511", 2), ("pattern-511-with-errors", 3))).clone('no-pattern')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotConfigPatternGen.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotConfigPatternGen.setDescription('Specifies the type of pattern generated. Range of Values: no-pattern (1) pattern-511 (2) pattern-511-with-errors (3) Default Value: no-pattern (1) Configuration Changed: operative')
ddsSlotDialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotDialNumber.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotDialNumber.setDescription('Assigns the dial number for switched56 applications. Default Value: none Range of Values: 12 character octet string Configuration Changed: operative')
ddsSlotSoftwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotSoftwareRevision.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotSoftwareRevision.setDescription('Indicates the DDS firmware revision as an integer value from 0 to 255. Default Value: none Range of Values: 0-255')
ddsSlotStuffingOption = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ccc-installed", 1), ("ccc-not-installed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotStuffingOption.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotStuffingOption.setDescription('Identifies whether the clear channel chip (ccc) option (for 64K clear channel) is installed. Default Value: none Options: ccc-installed (1) ccc-not-installed (2)')
ddsSlotLineQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("link", 1), ("no-link", 2), ("network-error-oos", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotLineQuality.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotLineQuality.setDescription('Identifies whether the link is up, if no link exists or if a network error (OOS - out of service) has occurred. Default Value: none Options: link (1) no-link (2) network-error-oos (3)')
ddsSlotLineRelativeReceiveLevelMin = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotLineRelativeReceiveLevelMin.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotLineRelativeReceiveLevelMin.setDescription('Indicates the minimum relative receive line level. Default Value: none Range of Values: 0-255')
ddsSlotLineRelativeReceiveLevelMax = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotLineRelativeReceiveLevelMax.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotLineRelativeReceiveLevelMax.setDescription('Indicates the maximum relative receive line level. Default Value: none Range of Values: 0-255')
ddsSlotLineLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 1), ("csu-loopback", 2), ("dsu-loopback", 3), ("dte-loopback", 4), ("loop2", 5), ("loop3", 6), ("loop4", 7), ("remote-loop2", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotLineLoopback.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotLineLoopback.setDescription('Indicates the loopback status of the line. Options: none (1) csu-loopback (2) dsu-loopback (3) dte-loopback (4) loop2 (5) loop3 (6) loop4 (7) remote-loop2 (8) Default Value: none (1) ')
ddsSlotResultErtPatternDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-receiving-pattern", 1), ("receiving-pattern", 2), ("receiving-patt-with-errors", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotResultErtPatternDetect.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotResultErtPatternDetect.setDescription('Identifies the reception of the 511 bit pattern or not. Options: not-receiving-pattern (1) receiving-pattern (2) receiving-patt-with-errors (3) Default Value: none ')
ddsSlotResultPatternGen = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("no-pattern", 1), ("ert-pattern", 2), ("ert-with-errors", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotResultPatternGen.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotResultPatternGen.setDescription('Identifies what type of pattern the DDS is generating on the line. Options: no-pattern (1) ert-pattern (2) ert-with-errors (3) Default: none ')
ddsSlotResultDialing = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("dialing-idle", 1), ("dialing-now", 2), ("connection-made", 3), ("err-no-num-from-host", 4), ("err-no-link", 5), ("err-no-rx-idle", 6), ("err-no-wink", 7), ("err-invalid-wink", 8), ("err-no-answer", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotResultDialing.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotResultDialing.setDescription('Indicates the dialing result codes for switched56 service as: dialing, connection made, the connection is not switched56, that a number has not been supplied by the host, no link available, no wink available, wink invalid or no answer. Options: dialing-idle (1) dialing-now (2) connection-made (3) err-no-num-from-host (4) err-no-link (5) err-no-rx-idle (6) err-no-wink (7) err-invalid-wink (8) err-no-answer (9) Default Value: none ')
ddsSlotModel = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotModel.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotModel.setDescription('Indicates the Printed Circuit Board (PCB) model number . Range of Values: 0-7 Default: none')
ddsSlotRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotRevision.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotRevision.setDescription('Indicates the PCB revision level. Range of Values: 0-15 Default Value: none')
ddsSlotEco = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddsSlotEco.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotEco.setDescription('Indicates the PCB Engineering Change Order (ECO) level. Range of Values: 0-15 Default Value: none ')
ddsSlotLineTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotLineTrap.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotLineTrap.setDescription('Determines the status of the line trap. Options: disabled (1) enabled (2) Default Value: disabled (1) Configuration Changed: operative')
ddsSlotLoopTrap = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddsSlotLoopTrap.setStatus('mandatory')
if mibBuilder.loadTexts: ddsSlotLoopTrap.setDescription('Determines the status of the loopback change trap. Range of Values: disabled (1) enabled (2) Default Value: disabled (1) Configuration Changed: operative')
ddsSlotLineStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39) + (0,1)).setObjects(("CXDDS-MIB", "ddsSlotNumber"), ("CXDDS-MIB", "ddsSlotLineQuality"))
if mibBuilder.loadTexts: ddsSlotLineStatusChange.setDescription('Indicates that an alarm has occurred. The line quality currently in use at the DDS access point has changed state to any of the states defined in object ddsSlotLineQuality.')
ddsSlotLoopStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 39) + (0,2)).setObjects(("CXDDS-MIB", "ddsSlotNumber"), ("CXDDS-MIB", "ddsSlotLineLoopback"))
if mibBuilder.loadTexts: ddsSlotLoopStatusChange.setDescription('Indicates an alarm status has occurred. The loopback status currently in use at the DDS access point has changed state to any of the states defined in object ddsSlotLineLoopback.')
mibBuilder.exportSymbols("CXDDS-MIB", ddsSlotStuffingOption=ddsSlotStuffingOption, ddsSlotDialNumber=ddsSlotDialNumber, ddsSlotConfigLineService=ddsSlotConfigLineService, ddsSlotRevision=ddsSlotRevision, ddsSlotConfigRemLoop2LocalAddress=ddsSlotConfigRemLoop2LocalAddress, ddsSlotLineQuality=ddsSlotLineQuality, ddsSlotEco=ddsSlotEco, ddsSlotLineStatusChange=ddsSlotLineStatusChange, ddsSlotConfigPatternGen=ddsSlotConfigPatternGen, ddsSlotLineTrap=ddsSlotLineTrap, ddsSlotResultPatternGen=ddsSlotResultPatternGen, ddsSlotLineRelativeReceiveLevelMax=ddsSlotLineRelativeReceiveLevelMax, ddsSlotResultDialing=ddsSlotResultDialing, ddsSlotModel=ddsSlotModel, ddsSlotEntry=ddsSlotEntry, ddsSlotLineLoopback=ddsSlotLineLoopback, ddsSlotNumber=ddsSlotNumber, ddsSlotStatus=ddsSlotStatus, ddsSlotConfigLoopback=ddsSlotConfigLoopback, ddsSlotTable=ddsSlotTable, ddsSlotConfigLineType=ddsSlotConfigLineType, ddsSlotLineRelativeReceiveLevelMin=ddsSlotLineRelativeReceiveLevelMin, ddsSlotLoopStatusChange=ddsSlotLoopStatusChange, ddsSlotRowStatus=ddsSlotRowStatus, ddsSlotConfigRemLoop2RemoteAddress=ddsSlotConfigRemLoop2RemoteAddress, ddsSlotAlias=ddsSlotAlias, ddsSlotLoopTrap=ddsSlotLoopTrap, ddsSlotResultErtPatternDetect=ddsSlotResultErtPatternDetect, ddsSlotSoftwareRevision=ddsSlotSoftwareRevision)
