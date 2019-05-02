#
# PySNMP MIB module LANART-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANART-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:05:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
rptrPortOperStatus, = mibBuilder.importSymbols("SNMP-REPEATER-MIB", "rptrPortOperStatus")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, ModuleIdentity, Bits, Counter32, MibIdentifier, Integer32, IpAddress, Unsigned32, enterprises, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "ModuleIdentity", "Bits", "Counter32", "MibIdentifier", "Integer32", "IpAddress", "Unsigned32", "enterprises", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lanart = MibIdentifier((1, 3, 6, 1, 4, 1, 712))
laMib1 = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1))
laProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1))
laHubMib = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 2))
laSys = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 2, 1))
laTpPort = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 2, 2))
laTpHub = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1))
laTpHub1 = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1))
etm120x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1, 12))
etm160x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1, 16))
etm240x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 1, 24))
laTpHub2 = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2))
ete120x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2, 12))
ete160x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2, 16))
ete240x = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 2, 24))
laTpHub3 = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3))
bbAui = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 0))
bbAuiTp = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 1))
bbAuiBnc = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 2))
bbAuiTpBnc = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 3))
bbAui10BASE_FL = MibIdentifier((1, 3, 6, 1, 4, 1, 712, 1, 1, 1, 3, 4)).setLabel("bbAui10BASE-FL")
laSysConfig = MibScalar((1, 3, 6, 1, 4, 1, 712, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("save", 1), ("load", 2), ("factory", 3), ("ok", 4), ("failed", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laSysConfig.setStatus('mandatory')
if mibBuilder.loadTexts: laSysConfig.setDescription('Setting this object to save(1) will save all configuration variables to non-volatile memory. Setting this object to load(2) will configure the hub according to the stored configuration. Setting this object to factory(3) will configure the hub according to the factory settings. A return value of ok(4) means the non-volatile memory is operational. A return value of failed(5) means the non-volatile memory has failed.')
laJoystick = MibScalar((1, 3, 6, 1, 4, 1, 712, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laJoystick.setStatus('mandatory')
if mibBuilder.loadTexts: laJoystick.setDescription('Setting this object to disabled(2) prevents use of the four-position switch on the front panel. Resetting this object to enabled(1) allows use of the switch.')
laLinkAlert = MibScalar((1, 3, 6, 1, 4, 1, 712, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("not-applicable", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laLinkAlert.setStatus('mandatory')
if mibBuilder.loadTexts: laLinkAlert.setDescription('Setting this object enables or disables the LinkALERT feature of the backbone 10BASE-T or 10BASE-FL port. A return value of not-applicable indicates that none of the backbone ports feature LinkALERT.')
laTpPortTable = MibTable((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1), )
if mibBuilder.loadTexts: laTpPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: laTpPortTable.setDescription('Table of descriptive and status information about the ports.')
laTpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1), ).setIndexNames((0, "LANART-MIB", "laTpPortGroupIndex"), (0, "LANART-MIB", "laTpPortIndex"))
if mibBuilder.loadTexts: laTpPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: laTpPortEntry.setDescription('An entry in the table, containing information about a single port.')
laTpPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: laTpPortGroupIndex.setStatus('mandatory')
if mibBuilder.loadTexts: laTpPortGroupIndex.setDescription('This object identifies the group containing the port for which this entry contains information.')
laTpPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024))).setMaxAccess("readonly")
if mibBuilder.loadTexts: laTpPortIndex.setStatus('mandatory')
if mibBuilder.loadTexts: laTpPortIndex.setDescription('This object identifies the port within the group for which this entry contains information.')
laTpLinkTest = MibTableColumn((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("failed", 3), ("not-applicable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laTpLinkTest.setStatus('mandatory')
if mibBuilder.loadTexts: laTpLinkTest.setDescription('Setting this object to disabled(2) disables the link test feature. This may be useful for interoperation with pre-10BASE-T equipment. Setting this object to enabled(1) enables the feature. A return value of failed(3) indicates a link test failure for this port. A return value of not-applicable(4) indicates that the specified port does not have a link test.')
laTpAutoPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 712, 1, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("corrected", 3), ("not-applicable", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: laTpAutoPolarity.setStatus('mandatory')
if mibBuilder.loadTexts: laTpAutoPolarity.setDescription('Setting this object to disabled(2) disables the auto polarity test for this port. Setting this object to enabled(1) enables the feature. A return value of corrected(3) indicates that the polarity test has sensed a reversal on the receive wiring pair, and has corrected this fault by inverting its receive signal. A return value of not-applicable(4) indicates that the specified port does not support polarity correction.')
laPortStatus = NotificationType((1, 3, 6, 1, 4, 1, 712) + (0,1)).setObjects(("SNMP-REPEATER-MIB", "rptrPortOperStatus"))
if mibBuilder.loadTexts: laPortStatus.setDescription('The laPortStatus trap conveys a change in status of a particular port. This trap is sent for a given port when either of the following status variables change for that port: rptrPortAdminStatus, laTpLinkTest The rptrHealth trap contains the rptrPortOperStatus object.')
mibBuilder.exportSymbols("LANART-MIB", laTpPortEntry=laTpPortEntry, laTpPort=laTpPort, laTpLinkTest=laTpLinkTest, bbAui=bbAui, laTpAutoPolarity=laTpAutoPolarity, laTpPortTable=laTpPortTable, bbAuiTp=bbAuiTp, etm160x=etm160x, bbAuiBnc=bbAuiBnc, ete240x=ete240x, laLinkAlert=laLinkAlert, laTpPortGroupIndex=laTpPortGroupIndex, laPortStatus=laPortStatus, laSysConfig=laSysConfig, lanart=lanart, laTpHub1=laTpHub1, laTpHub2=laTpHub2, laTpHub3=laTpHub3, laMib1=laMib1, laTpPortIndex=laTpPortIndex, bbAuiTpBnc=bbAuiTpBnc, ete160x=ete160x, etm120x=etm120x, laHubMib=laHubMib, laProducts=laProducts, laJoystick=laJoystick, etm240x=etm240x, bbAui10BASE_FL=bbAui10BASE_FL, laSys=laSys, laTpHub=laTpHub, ete120x=ete120x)
