#
# PySNMP MIB module SW-STRCTURE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SW-STRCTURE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:12:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, Counter32, NotificationType, TimeTicks, ObjectIdentity, Integer32, NotificationType, Counter64, Gauge32, Unsigned32, IpAddress, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "Counter32", "NotificationType", "TimeTicks", "ObjectIdentity", "Integer32", "NotificationType", "Counter64", "Gauge32", "Unsigned32", "IpAddress", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
marconi = MibIdentifier((1, 3, 6, 1, 4, 1, 326))
systems = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2))
external = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20))
dlink = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1))
dlinkcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1))
golf = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2))
golfproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1))
es2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3))
golfcommon = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2))
marconi_mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)).setLabel("marconi-mgmt")
es2000Mgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28))
swStructure = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1))
swStructInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1))
swStructDevType = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructDevType.setStatus('mandatory')
if mibBuilder.loadTexts: swStructDevType.setDescription('Specifies the device type.')
swStructDevDescr = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructDevDescr.setStatus('mandatory')
if mibBuilder.loadTexts: swStructDevDescr.setDescription('Describes the type of the device.')
swStructDevPortEncodingFactor = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructDevPortEncodingFactor.setStatus('mandatory')
if mibBuilder.loadTexts: swStructDevPortEncodingFactor.setDescription('The factor to encode the global port ID from unit ID and the local port ID. This global port ID is required to access the bridge MIB and spanning tree MIB defined by the standard body. This global port ID will provide a unigue port ID for each port across the entire device. Example: supoposed that the encoding factor is 16, then port 2 located on module 2 will be encoded as port 18')
swStructDevLedInfo = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructDevLedInfo.setStatus('mandatory')
if mibBuilder.loadTexts: swStructDevLedInfo.setDescription('Provides the LED informations of the cpu slot. bit7 - cpu status(always 1) bit6 - console status(0: console not in used, 1: console in used) bit5 - power status(always 1) bit 4 ~ bit 0 - not used.')
swStructDevMaxModuleNum = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructDevMaxModuleNum.setStatus('mandatory')
if mibBuilder.loadTexts: swStructDevMaxModuleNum.setDescription('Maximum number of modules allowed on the unit.')
swStructDevMaxPortNum = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructDevMaxPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: swStructDevMaxPortNum.setDescription('Maximum number of ports allowed on the unit.')
swStructDevNumOfPortInUse = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructDevNumOfPortInUse.setStatus('mandatory')
if mibBuilder.loadTexts: swStructDevNumOfPortInUse.setDescription('Number of ports which has link being connected to the port.')
swStructDevOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("notAvail", 2), ("removed", 3), ("disabled", 4), ("normal", 5), ("nonFatalErr", 9), ("fatalErr", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructDevOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: swStructDevOperStatus.setDescription('Describes the operation status for the unit.')
swStructDevLastChange = MibScalar((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructDevLastChange.setStatus('mandatory')
if mibBuilder.loadTexts: swStructDevLastChange.setDescription('Provides the time that the unit is up last time.')
swStructModuleTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2), )
if mibBuilder.loadTexts: swStructModuleTable.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleTable.setDescription('A table that contains information about a module.')
swStructModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1), ).setIndexNames((0, "SW-STRCTURE-MIB", "swStructModuleUnitIndex"), (0, "SW-STRCTURE-MIB", "swStructModuleIndex"))
if mibBuilder.loadTexts: swStructModuleEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleEntry.setDescription('A list of information for a module.')
swStructModuleUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructModuleUnitIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleUnitIndex.setDescription('ID of the unit in the device.')
swStructModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructModuleIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleIndex.setDescription('ID of the Module in the device.')
swStructModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructModuleType.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleType.setDescription('Type of the module.')
swStructModuleDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructModuleDescr.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleDescr.setDescription('Type of the module in displayed string format.')
swStructModuleVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructModuleVersion.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleVersion.setDescription('Provides PCB version of the module.')
swStructModuleMaxPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructModuleMaxPortNum.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleMaxPortNum.setDescription('Maximum number of ports allowed on the module.')
swStructModuleEncodingOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructModuleEncodingOffset.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleEncodingOffset.setDescription('Each module has a offset for encoding the port ID relative to a unit. This encoding will provide a unigue port ID for ports located on the device. Example: Supposed that the offset for module 2 is 16, then port 2 located on module 2 will be encoded as port 18')
swStructModuleLEDInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructModuleLEDInfo.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleLEDInfo.setDescription('Gets LED informations on specifiled module.')
swStructModuleOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("notAvail", 2), ("removed", 3), ("disabled", 4), ("normal", 5), ("nonFatalErr", 9), ("fatalErr", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructModuleOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleOperStatus.setDescription('Provides operation status of the module.')
swStructModuleLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructModuleLastChange.setStatus('mandatory')
if mibBuilder.loadTexts: swStructModuleLastChange.setDescription('Provides the time that the module is up last time.')
swStructPowerTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3), )
if mibBuilder.loadTexts: swStructPowerTable.setStatus('mandatory')
if mibBuilder.loadTexts: swStructPowerTable.setDescription('A table that contains information about every power.')
swStructPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1), ).setIndexNames((0, "SW-STRCTURE-MIB", "swStructPowerIndex"))
if mibBuilder.loadTexts: swStructPowerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swStructPowerEntry.setDescription('A list of information for each power.')
swStructPowerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructPowerIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swStructPowerIndex.setDescription('ID of the power supply in the unit.')
swStructPowerInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructPowerInfo.setStatus('mandatory')
if mibBuilder.loadTexts: swStructPowerInfo.setDescription('Displays informations of power. Includes vendor, version and so on.')
swStructPowerTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructPowerTemperature.setStatus('mandatory')
if mibBuilder.loadTexts: swStructPowerTemperature.setDescription('Displays temperature value of power by Fahrenheit.')
swStructPowerVolt = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructPowerVolt.setStatus('mandatory')
if mibBuilder.loadTexts: swStructPowerVolt.setDescription('Displays volt value of power by V unit.')
swStructPowerAmp = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructPowerAmp.setStatus('mandatory')
if mibBuilder.loadTexts: swStructPowerAmp.setDescription('Displays amp value of power by A unit.')
swStructPowerFan1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fanOk", 1), ("fanFail", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructPowerFan1Status.setStatus('mandatory')
if mibBuilder.loadTexts: swStructPowerFan1Status.setDescription('Describes the operation status of the power fan1.')
swStructPowerFan2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fanOk", 1), ("fanFail", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructPowerFan2Status.setStatus('mandatory')
if mibBuilder.loadTexts: swStructPowerFan2Status.setDescription('Describes the operation status of the power fan2.')
swStructPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("acFailPsFail", 1), ("acPresentPsFail", 2), ("psGood", 3), ("other", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructPowerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: swStructPowerStatus.setDescription('Describes the operation status of the power supply.')
swStructSystemFanTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 4), )
if mibBuilder.loadTexts: swStructSystemFanTable.setStatus('mandatory')
if mibBuilder.loadTexts: swStructSystemFanTable.setDescription('A table that contains informations about system fans.')
swStructSystemFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 4, 1), ).setIndexNames((0, "SW-STRCTURE-MIB", "swStructSystemFanIndex"))
if mibBuilder.loadTexts: swStructSystemFanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: swStructSystemFanEntry.setDescription('A list of informations for each system fan.')
swStructSystemFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructSystemFanIndex.setStatus('mandatory')
if mibBuilder.loadTexts: swStructSystemFanIndex.setDescription('ID of designed system fans.')
swStructSystemFanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fanOk", 1), ("fanFail", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swStructSystemFanStatus.setStatus('mandatory')
if mibBuilder.loadTexts: swStructSystemFanStatus.setDescription('Describes the operation status of the system fans.')
powerTemperatureWarnning = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,5)).setObjects(("SW-STRCTURE-MIB", "swStructPowerIndex"))
if mibBuilder.loadTexts: powerTemperatureWarnning.setDescription('The trap is sent whenever the power state enter the temperature warnning state. ')
powerVoltWarnning = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,6)).setObjects(("SW-STRCTURE-MIB", "swStructPowerIndex"))
if mibBuilder.loadTexts: powerVoltWarnning.setDescription('The trap is sent whenever the power state enter the volt warnning state. ')
powerCurrentWarnning = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,7)).setObjects(("SW-STRCTURE-MIB", "swStructPowerIndex"))
if mibBuilder.loadTexts: powerCurrentWarnning.setDescription('The trap is sent whenever the power state enter the current warnning state. ')
powerFan1Fail = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,8)).setObjects(("SW-STRCTURE-MIB", "swStructPowerIndex"))
if mibBuilder.loadTexts: powerFan1Fail.setDescription('The trap is sent whenever the power state enter the power fan1 fail state. ')
powerFan2Fail = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,9)).setObjects(("SW-STRCTURE-MIB", "swStructPowerIndex"))
if mibBuilder.loadTexts: powerFan2Fail.setDescription('The trap is sent whenever the power state enter the power fan2 fail state. ')
systemFanFail = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,10)).setObjects(("SW-STRCTURE-MIB", "swStructSystemFanIndex"))
if mibBuilder.loadTexts: systemFanFail.setDescription('The trap is sent whenever the power state enter the system fans fail state. ')
powerRemoved = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,11)).setObjects(("SW-STRCTURE-MIB", "swStructPowerIndex"))
if mibBuilder.loadTexts: powerRemoved.setDescription('The trap is sent whenever the power is removed.')
powerInserted = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,12)).setObjects(("SW-STRCTURE-MIB", "swStructPowerIndex"))
if mibBuilder.loadTexts: powerInserted.setDescription('The trap is sent whenever the power is inserted.')
powerBad = NotificationType((1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3) + (0,13)).setObjects(("SW-STRCTURE-MIB", "swStructPowerIndex"))
if mibBuilder.loadTexts: powerBad.setDescription('The trap is sent whenever the power is bad.')
mibBuilder.exportSymbols("SW-STRCTURE-MIB", swStructPowerInfo=swStructPowerInfo, swStructPowerAmp=swStructPowerAmp, dlinkcommon=dlinkcommon, swStructModuleType=swStructModuleType, swStructModuleMaxPortNum=swStructModuleMaxPortNum, powerCurrentWarnning=powerCurrentWarnning, swStructDevMaxPortNum=swStructDevMaxPortNum, swStructPowerTable=swStructPowerTable, swStructDevPortEncodingFactor=swStructDevPortEncodingFactor, dlink=dlink, swStructPowerFan1Status=swStructPowerFan1Status, swStructModuleOperStatus=swStructModuleOperStatus, powerInserted=powerInserted, external=external, swStructPowerVolt=swStructPowerVolt, powerBad=powerBad, swStructModuleIndex=swStructModuleIndex, swStructModuleVersion=swStructModuleVersion, es2000Mgmt=es2000Mgmt, swStructModuleEntry=swStructModuleEntry, golfcommon=golfcommon, swStructPowerEntry=swStructPowerEntry, swStructModuleUnitIndex=swStructModuleUnitIndex, swStructPowerStatus=swStructPowerStatus, swStructModuleDescr=swStructModuleDescr, swStructModuleLEDInfo=swStructModuleLEDInfo, powerFan1Fail=powerFan1Fail, swStructPowerTemperature=swStructPowerTemperature, swStructModuleTable=swStructModuleTable, swStructDevLastChange=swStructDevLastChange, swStructDevType=swStructDevType, swStructPowerFan2Status=swStructPowerFan2Status, swStructDevMaxModuleNum=swStructDevMaxModuleNum, es2000=es2000, swStructModuleLastChange=swStructModuleLastChange, marconi=marconi, swStructSystemFanStatus=swStructSystemFanStatus, swStructModuleEncodingOffset=swStructModuleEncodingOffset, powerRemoved=powerRemoved, swStructInfo=swStructInfo, systemFanFail=systemFanFail, swStructSystemFanEntry=swStructSystemFanEntry, swStructSystemFanIndex=swStructSystemFanIndex, swStructDevOperStatus=swStructDevOperStatus, golf=golf, swStructSystemFanTable=swStructSystemFanTable, marconi_mgmt=marconi_mgmt, swStructPowerIndex=swStructPowerIndex, powerVoltWarnning=powerVoltWarnning, powerFan2Fail=powerFan2Fail, systems=systems, swStructDevDescr=swStructDevDescr, swStructDevNumOfPortInUse=swStructDevNumOfPortInUse, golfproducts=golfproducts, powerTemperatureWarnning=powerTemperatureWarnning, swStructDevLedInfo=swStructDevLedInfo, swStructure=swStructure)
