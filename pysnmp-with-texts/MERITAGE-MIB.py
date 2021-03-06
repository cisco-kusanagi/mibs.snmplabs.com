#
# PySNMP MIB module MERITAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERITAGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:11:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
lannet, = mibBuilder.importSymbols("GEN-MIB", "lannet")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, TimeTicks, IpAddress, Counter32, iso, MibIdentifier, ObjectIdentity, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "TimeTicks", "IpAddress", "Counter32", "iso", "MibIdentifier", "ObjectIdentity", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
meritage = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 32))
meritageBase = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 32, 1))
meritageMSPV = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 32, 2))
meritageGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 32, 3))
meritageClock = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 32, 4))
meritageClockSource = MibIdentifier((1, 3, 6, 1, 4, 1, 81, 32, 5))
meritageBaseLEDs = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBaseLEDs.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBaseLEDs.setDescription('Summary of the hub LEDs. The coding of each LED is defined in meritageLedColour Number of bits per LED, currently 8 (1st byte) Number of LEDs, currently 8 (2nd byte) PS1 LED (3rd byte) PS2 LED PS3 LED Fan1 LED Fan2 LED MSPV1 LED MSPV2 LED Eth Sideband LED (last byte)')
meritageBaseTemperatureExceed = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("ok", 1), ("exceeded", 2), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBaseTemperatureExceed.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBaseTemperatureExceed.setDescription('Fault condition indicating that the temperature exceeded 70 degrees in at least one of the modules in the hub.')
meritageBaseXswitchConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("connected", 1), ("separated", 2), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBaseXswitchConfiguration.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBaseXswitchConfiguration.setDescription('The value of this attribute shows whether the two horizontal Xswitches are connected internally to form a single 14-slots-wide Xswitch in the Meritage, or not.')
meritageBaseFaultMask = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBaseFaultMask.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBaseFaultMask.setDescription('Each bit of this item describes a fault situation in the Meritage hub. bit 1: meritageBaseFanActivityStatus.1 = failed (2), bit 2: meritageBaseFanActivityStatus.2 = failed (2), bit 3: meritageBasePSUActivityStatus.1 = failed(2), bit 4: meritageBasePSUActivityStatus.2 = failed(2), bit 5: meritageBasePSUActivityStatus.3 = failed(2), bit 6: meritageMSPVBackupStatus = failed(2), bit 7: scGenSwitchOldVersionModules.1 = null, bit 8: scGenSwitchOldVersionModules.2 = null, bit 9: scGenSwitchVIDPNonSupportedModules.1 = null, bit 10: scGenSwitchVIDPNonSupportedModules.2 = null, bit 11: scGenSwitchSTAonSupportedModules.1 = null, bit 12: scGenSwitchSTAonSupportedModules.2 = null, bit 13: scGenSwitchIDSonSupportedModules.1 = null, bit 14: scGenSwitchIDSonSupportedModules.2 = null, bit 15: The highest priority source port is not the curent source (according to meritageClockCurrentSource), bit 16: meritageClockStatus is Not in locked (1) for more then 120 seconds AND not all priorities are 0 AND meritageClockAdminStatus = enable (1), bit 17: meritageClockSourceStatus.1 = failed (2), bit 18: meritageClockSourceStatus.2 = failed (2), bit 19: meritageClockSourceStatus.3 = failed (2), bit 20: meritageClockSourceStatus.4 = failed (2), ')
meritageBaseFanTable = MibTable((1, 3, 6, 1, 4, 1, 81, 32, 1, 5), )
if mibBuilder.loadTexts: meritageBaseFanTable.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBaseFanTable.setDescription('Table of attributes for Fan units in the Meritage.')
meritageBaseFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 32, 1, 5, 1), ).setIndexNames((0, "MERITAGE-MIB", "meritageBaseFanId"))
if mibBuilder.loadTexts: meritageBaseFanEntry.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBaseFanEntry.setDescription('An entry in the table, containing attributes for a single Fan unit in the Meritage.')
meritageBaseFanId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBaseFanId.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBaseFanId.setDescription('Fan index for identifying the Fan in the Meritage 1-left, 2-right.')
meritageBaseFanActivityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("failed", 2), ("none", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBaseFanActivityStatus.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBaseFanActivityStatus.setDescription('This attribute defines the status of the Fan.')
meritageBasePSUTable = MibTable((1, 3, 6, 1, 4, 1, 81, 32, 1, 6), )
if mibBuilder.loadTexts: meritageBasePSUTable.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBasePSUTable.setDescription('Table of configuration attributes for the Power Supply Units.')
meritageBasePSUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1), ).setIndexNames((0, "MERITAGE-MIB", "meritageBasePSUId"))
if mibBuilder.loadTexts: meritageBasePSUEntry.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBasePSUEntry.setDescription('An entry in the table, containing information for a single Power Supply Unit.')
meritageBasePSUId = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBasePSUId.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBasePSUId.setDescription('Index identifying the PSU.1-left, 2-middle, 3-right.')
meritageBasePSUType = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))).clone(namedValues=NamedValues(("m-ps500", 1), ("m-ps1250", 2), ("m-ps800", 3), ("m-ps800-dc", 4), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBasePSUType.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBasePSUType.setDescription('This attribute indicates the PSU type.')
meritageBasePSUHWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBasePSUHWVersion.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBasePSUHWVersion.setDescription('Hardware version of the PSU. Stored in ASCII format : first Byte - hardware major version number Second Byte - hardware minor version number (Configuration Symbol) last Byte - hardware debug version number.')
meritageBasePSURatedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBasePSURatedPower.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBasePSURatedPower.setDescription('This attribute indicates the rated power of the PSU in Watts.')
meritageBasePSUActivityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("active", 1), ("failed", 2), ("none", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBasePSUActivityStatus.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBasePSUActivityStatus.setDescription('This attribute defines the status of the PSU: active(1) - indicates that the PSU supplies power to the chassis. failed(2) - indicates PSU failure none(3) - indicates absence of PSU from the configuration.')
meritageBaseUpBckplnConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))).clone(namedValues=NamedValues(("singleDomain", 1), ("dualDomain", 2), ("notInstalled", 3), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBaseUpBckplnConfiguration.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBaseUpBckplnConfiguration.setDescription('Defines whether the Upper Backplane is constructed as a single domain (full), as a dual domain (split) or not installed. The hardware supports 2 bits for this purpose (A10, B10 MSB). single - 10 in the MSB HW registers dual - 01 in the MSB HW registers notInstalled - 11 in the MSB HW registers')
meritageBaseUpBckplnConfigurationSymbol = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageBaseUpBckplnConfigurationSymbol.setStatus('mandatory')
if mibBuilder.loadTexts: meritageBaseUpBckplnConfigurationSymbol.setDescription("Defines the Configuration Symbol of the Upper Backplane X.Y - where X & Y are integers: 1st byte (X) - Major version number 2nd byte - '.' 3rd byte (Y) - minor version number The hardware supports 2 bits for this purpose (D10, E10 LSB). Y will always be 0. X will change according to the HW registers. 00 is CS 1.0, 01 is 2.0, 10 is 3.0, 11 is 4.0. If no upper backplane is installed in the chassis, an empty string will be returned. ")
meritageMSPVBackupStatus = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))).clone(namedValues=NamedValues(("dormant", 1), ("failed", 2), ("none", 3), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageMSPVBackupStatus.setStatus('mandatory')
if mibBuilder.loadTexts: meritageMSPVBackupStatus.setDescription('This attribute defines the status of the backup M-SPV module in the Meritage: dormant (1) - indicates that the backup M-SPV is dormant and works ok. failed (2) - indicates that the backup M-SPV has failed. none (3) - indicates absence of the backup M-SPV from the hub.')
meritageMSPVMainPosition = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("mMSPV1", 1), ("mMSPV2", 2), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageMSPVMainPosition.setStatus('mandatory')
if mibBuilder.loadTexts: meritageMSPVMainPosition.setDescription('This attribute defines the position of the main M-SPV module in the Meritage: MSPV1 (1) - indicates that the main M-SPV is the one on the left slot MSPV2 (2) - indicates that the main M-SPV is the one on the right slot.')
meritageGroupTable = MibTable((1, 3, 6, 1, 4, 1, 81, 32, 3, 1), )
if mibBuilder.loadTexts: meritageGroupTable.setStatus('mandatory')
if mibBuilder.loadTexts: meritageGroupTable.setDescription('A table containing information about each group in the hub.')
meritageGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 32, 3, 1, 1), ).setIndexNames((0, "MERITAGE-MIB", "meritageGroupIndex"))
if mibBuilder.loadTexts: meritageGroupEntry.setStatus('mandatory')
if mibBuilder.loadTexts: meritageGroupEntry.setDescription('An entry containing information about a particular group in the hub.')
meritageGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageGroupIndex.setStatus('mandatory')
if mibBuilder.loadTexts: meritageGroupIndex.setDescription('Index into this table, by group number.')
meritageGroupTempExceed = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 255))).clone(namedValues=NamedValues(("ok", 1), ("exceeded", 2), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageGroupTempExceed.setStatus('mandatory')
if mibBuilder.loadTexts: meritageGroupTempExceed.setDescription('Fault condition indicating that temperature exceeded the threshold on the module.')
meritageGroupLEDsMap = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 3, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageGroupLEDsMap.setStatus('mandatory')
if mibBuilder.loadTexts: meritageGroupLEDsMap.setDescription('The status of all the Group LEDs in the form of a BIT Map. The coding of each LED is defined in MeritageLedColour. The structure of this item: Number of bits per LED = A (currently 8 bits) (1st byte) Number of Module level LEDs = B (currently 2) (2nd byte) Number of Ports = C (currently 12) (3rd byte) Number of Functions = D (currently 6) (4th byte) Module level LEDs (=B bytes) Ports LEDs for function #1 (=C bytes) Ports LEDs for function #2 (=C bytes) Ports LEDs for function #3 (=C bytes) ... Ports LEDs for function #D (=C bytes) The length of this item, with the current values, is 78 bytes.')
meritageClockAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: meritageClockAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockAdminStatus.setDescription('enable or disable the clock sync daughter board. When disabled, the M-SPS will use its own internal clock.')
meritageClockReset = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: meritageClockReset.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockReset.setDescription('Setting the value of this attribute to ON causes a reset only to the Clock Sync daughter board and not to the M-SPS.')
meritageClockWTR = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 4, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: meritageClockWTR.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockWTR.setDescription('The value in seconds of Wait Time to Restore. The time the M-SPS software will wait before restoring a healthy higher priority timing source as the sync source. This is to prevent toggling between two sources if one source is intermittently bad. If the WTR is set to infinity, a higher priority source will be active only if the current source fails or after reset. ranges 10-3600 seconds value = 9999 means infinity. default value - 20 sec. ')
meritageClockStatus = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("locked", 1), ("holdover", 2), ("freeRunning", 3), ("internal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageClockStatus.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockStatus.setDescription('The status of the Clock Sync daughter board: Locked - locked to the input timing source for more then 8 seconds. Holdover - Trying to simulate a clock it was previously locked to. FreeRunning - Outputting a timing source derived from none of the sources. Internal - Outputting the internal clock, because the clock sync is disabled.')
meritageClockCurrentSource = MibScalar((1, 3, 6, 1, 4, 1, 81, 32, 4, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageClockCurrentSource.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockCurrentSource.setDescription('The current clock source being used. This is the outcome of the status of the sources and the priority between the sources. possible values are: ATM A, ATM B, SYNC A, SYNC B, none (when there is no source, i.e. in Holdover, Free Running or Internal). A Trap will be sent on change. ')
meritageClockSourceTable = MibTable((1, 3, 6, 1, 4, 1, 81, 32, 5, 1), )
if mibBuilder.loadTexts: meritageClockSourceTable.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockSourceTable.setDescription('A table containing information about each clock source in the hub.')
meritageClockSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1), ).setIndexNames((0, "MERITAGE-MIB", "meritageClockSourceIndex"))
if mibBuilder.loadTexts: meritageClockSourceEntry.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockSourceEntry.setDescription('An entry containing information about a particular clock source in the hub.')
meritageClockSourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageClockSourceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockSourceIndex.setDescription('Index into this table, by clock source number 1-4. 1 - ATM A 2 - ATM B 3 - SYNC A 4 - SYNC B ')
meritageClockSourceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))).clone(namedValues=NamedValues(("ok", 1), ("los", 2), ("failed", 3), ("notSupported", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: meritageClockSourceStatus.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockSourceStatus.setDescription("The status of the source port ok - link ok los - loss of signal. failed - the source may have a link, but the M-SPS has failed 4 times to lock to it. The source will automatically be disabled (priority 0). The status can exit the failed status only if the user enables the source by raising it's priority.")
meritageClockSourcePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: meritageClockSourcePriority.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockSourcePriority.setDescription('The priority of the source port 0 - disabled 1 - lowest 4 - highest ')
meritageClockSourceConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: meritageClockSourceConfigPort.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockSourceConfigPort.setDescription('The port assigned to drive the Clock Source. In the format X.Y - where X & Y are integers: 1st byte (X) - Slot number 2nd byte - (.) 3rd byte (Y) - Port number The NMS can write values to index 1 and 2 only. Attempt to write a value to index 3 and 4 will cause genError. The NMS can read the value to see that the set was successful. For index 1 - for example = 3.1 For index 2 - for example = 3.2 For index 3 - value always = 15.1 For index 4 - value always = 15.2')
meritageClockSourceFraming = MibTableColumn((1, 3, 6, 1, 4, 1, 81, 32, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))).clone(namedValues=NamedValues(("e1-framed", 1), ("e1-unframed", 2), ("ds1-sf", 3), ("ds1-esf", 4), ("notSupported", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: meritageClockSourceFraming.setStatus('mandatory')
if mibBuilder.loadTexts: meritageClockSourceFraming.setDescription('The framing mode for the SYNC A SYNC B ports. Sources ATM A and ATM will reply with notSupported (255). For M-SPS/ER and EB, the values 1 and 2 are relevant. For M-SPS/T, the values 3 and 4 are relevant. ')
mibBuilder.exportSymbols("MERITAGE-MIB", meritageBaseFanId=meritageBaseFanId, meritageGroupLEDsMap=meritageGroupLEDsMap, meritageClockSource=meritageClockSource, meritageBaseFanEntry=meritageBaseFanEntry, meritageClockSourcePriority=meritageClockSourcePriority, meritageBaseUpBckplnConfigurationSymbol=meritageBaseUpBckplnConfigurationSymbol, meritageClockWTR=meritageClockWTR, meritageClockSourceIndex=meritageClockSourceIndex, meritageMSPVMainPosition=meritageMSPVMainPosition, meritageBaseLEDs=meritageBaseLEDs, meritageBaseFanTable=meritageBaseFanTable, meritageBasePSUEntry=meritageBasePSUEntry, meritageBasePSUType=meritageBasePSUType, meritageClockAdminStatus=meritageClockAdminStatus, meritageClockStatus=meritageClockStatus, meritageBasePSUActivityStatus=meritageBasePSUActivityStatus, meritageClockCurrentSource=meritageClockCurrentSource, meritageClockSourceTable=meritageClockSourceTable, meritageClockSourceConfigPort=meritageClockSourceConfigPort, meritageClockReset=meritageClockReset, meritageBaseFanActivityStatus=meritageBaseFanActivityStatus, meritageBase=meritageBase, meritageBaseUpBckplnConfiguration=meritageBaseUpBckplnConfiguration, meritageClockSourceStatus=meritageClockSourceStatus, meritageGroupTable=meritageGroupTable, meritageClockSourceFraming=meritageClockSourceFraming, meritageGroupIndex=meritageGroupIndex, meritageBasePSUHWVersion=meritageBasePSUHWVersion, meritageBaseXswitchConfiguration=meritageBaseXswitchConfiguration, meritageGroupEntry=meritageGroupEntry, meritageMSPVBackupStatus=meritageMSPVBackupStatus, meritageClockSourceEntry=meritageClockSourceEntry, meritage=meritage, meritageBaseFaultMask=meritageBaseFaultMask, meritageBaseTemperatureExceed=meritageBaseTemperatureExceed, meritageMSPV=meritageMSPV, meritageBasePSURatedPower=meritageBasePSURatedPower, meritageGroup=meritageGroup, meritageClock=meritageClock, meritageBasePSUTable=meritageBasePSUTable, meritageBasePSUId=meritageBasePSUId, meritageGroupTempExceed=meritageGroupTempExceed)
