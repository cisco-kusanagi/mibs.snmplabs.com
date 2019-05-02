#
# PySNMP MIB module CISCO-ENTITY-DISPLAY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-DISPLAY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:56:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Gauge32, Counter64, ObjectIdentity, Counter32, IpAddress, MibIdentifier, iso, TimeTicks, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Gauge32", "Counter64", "ObjectIdentity", "Counter32", "IpAddress", "MibIdentifier", "iso", "TimeTicks", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoEntityDisplayMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 344))
ciscoEntityDisplayMIB.setRevisions(('2009-10-05 00:00', '2003-03-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setRevisionsDescriptions(("Added the enumeration 'greenAndAmber' to CDisplayColor TEXTUAL-CONVENTION. Added support for ceDisplayBeaconGroup.", 'Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setLastUpdated('200910050000Z')
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-displaymib@cisco.com')
if mibBuilder.loadTexts: ciscoEntityDisplayMIB.setDescription('This MIB module provides information about the status of display devices such as Light Emitting Diodes (LEDs) and alphanumeric displays present on the physical entities contained by the managed system.')
class CDisplayType(TextualConvention, Integer32):
    description = 'An integer value that indicates the type of display device.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("led", 1), ("alphanumeric", 2))

class CDisplayColor(TextualConvention, Integer32):
    description = "An integer value that describes the color of the display. 'greenAndAmber' - Indicates that the display color toggles between green and amber."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 1), ("white", 2), ("red", 3), ("green", 4), ("yellow", 5), ("amber", 6), ("blue", 7), ("greenAndAmber", 8))

class CDisplayState(TextualConvention, Integer32):
    description = 'An integer value that describes the state of the display.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("off", 2), ("on", 3), ("blinking", 4))

ciscoEntityDisplayMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 1))
ceDisplayTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1), )
if mibBuilder.loadTexts: ceDisplayTable.setStatus('current')
if mibBuilder.loadTexts: ceDisplayTable.setDescription('This table provides information about the display devices on the physical entities in the managed system and their current display status.')
ceDisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-DISPLAY-MIB", "ceDisplayIndex"))
if mibBuilder.loadTexts: ceDisplayEntry.setStatus('current')
if mibBuilder.loadTexts: ceDisplayEntry.setDescription('An entry in the ceDisplayTable that provides information about an LED or an alphanumeric display in the system including its current display status.')
ceDisplayIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: ceDisplayIndex.setStatus('current')
if mibBuilder.loadTexts: ceDisplayIndex.setDescription('An arbitrary index that uniquely identifies an LED or an alphanumeric display on the physical entity identified by entPhysicalIndex.')
ceDisplayType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 2), CDisplayType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayType.setStatus('current')
if mibBuilder.loadTexts: ceDisplayType.setDescription('This object indicates the type of display described in this entry. i.e. whether it is an LED display or an alphanumeric display.')
ceDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayName.setStatus('current')
if mibBuilder.loadTexts: ceDisplayName.setDescription('This object provides a human-readable string which is the name for the display device specified in this entry.')
ceDisplayState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 4), CDisplayState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayState.setStatus('current')
if mibBuilder.loadTexts: ceDisplayState.setDescription('This object indicates the current display state for the display specified in this entry.')
ceDisplayColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 5), CDisplayColor()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayColor.setStatus('current')
if mibBuilder.loadTexts: ceDisplayColor.setDescription("This object indicates the color currently seen on the display specified in this entry. If the display specified by this entry is an alphanumeric display, i.e. ceDisplayType is of type 'alphanumeric' then, color may not apply and the agent may choose to indicate this by setting this object to 'unknown'.")
ceDisplayText = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceDisplayText.setStatus('current')
if mibBuilder.loadTexts: ceDisplayText.setDescription("This object provides a human-readable string which is the text currently displayed in the alphanumeric display specified in this entry. If the display specified by this entry is an LED, i.e. ceDisplayType is of type 'led' then, this object would be an empty string.")
ceDisplayBeaconTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2), )
if mibBuilder.loadTexts: ceDisplayBeaconTable.setStatus('current')
if mibBuilder.loadTexts: ceDisplayBeaconTable.setDescription('This table provides functionality to manage beacon display devices in the managed system.')
ceDisplayBeaconEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-DISPLAY-MIB", "ceDisplayIndex"))
if mibBuilder.loadTexts: ceDisplayBeaconEntry.setStatus('current')
if mibBuilder.loadTexts: ceDisplayBeaconEntry.setDescription('An entry containing management information of beacon functionality of a particular beacon display device. Only those display devices, as specified by entPhysicalIndex in ENTITY-MIB, that support beacon functionality will be populated in this table.')
ceDisplayBeaconEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceDisplayBeaconEnabled.setStatus('current')
if mibBuilder.loadTexts: ceDisplayBeaconEnabled.setDescription("This object specifies if the beacon functionality is administratively enabled for this display device. 'true' - beacon functionality is administratively enabled 'false' - beacon functionality is administratively disabled.")
ceDisplayMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2))
ceDisplayMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1))
ceDisplayMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2))
ceDisplayMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1, 1)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayLEDGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayAlphaNumericGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayMIBCompliance = ceDisplayMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ceDisplayMIBCompliance.setDescription('The compliance statement for entities that implement the CISCO-ENTITY-DISPLAY-MIB. This compliance statement is deprecated and superceded by ceDisplayMIBCompliance2.')
ceDisplayMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1, 2)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayLEDGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayAlphaNumericGroup"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayBeaconGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayMIBCompliance2 = ceDisplayMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: ceDisplayMIBCompliance2.setDescription('The compliance statement for entities that implement the CISCO-ENTITY-DISPLAY-MIB.')
ceDisplayGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 1)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayType"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayName"), ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayGroup = ceDisplayGroup.setStatus('current')
if mibBuilder.loadTexts: ceDisplayGroup.setDescription('A collection of managed objects that provide information about a display in the system including its current state.')
ceDisplayLEDGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 2)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayColor"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayLEDGroup = ceDisplayLEDGroup.setStatus('current')
if mibBuilder.loadTexts: ceDisplayLEDGroup.setDescription('A collection of objects relevant to LED display.')
ceDisplayAlphaNumericGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 3)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayAlphaNumericGroup = ceDisplayAlphaNumericGroup.setStatus('current')
if mibBuilder.loadTexts: ceDisplayAlphaNumericGroup.setDescription('A collection of objects relevant to alphanumeric display.')
ceDisplayBeaconGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 4)).setObjects(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayBeaconEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceDisplayBeaconGroup = ceDisplayBeaconGroup.setStatus('current')
if mibBuilder.loadTexts: ceDisplayBeaconGroup.setDescription('A collection of objects relevant to beacon functionality.')
mibBuilder.exportSymbols("CISCO-ENTITY-DISPLAY-MIB", ceDisplayMIBCompliance2=ceDisplayMIBCompliance2, ceDisplayMIBCompliances=ceDisplayMIBCompliances, ceDisplayText=ceDisplayText, ceDisplayState=ceDisplayState, CDisplayType=CDisplayType, CDisplayState=CDisplayState, ceDisplayBeaconGroup=ceDisplayBeaconGroup, ceDisplayAlphaNumericGroup=ceDisplayAlphaNumericGroup, ceDisplayIndex=ceDisplayIndex, ceDisplayBeaconTable=ceDisplayBeaconTable, ciscoEntityDisplayMIB=ciscoEntityDisplayMIB, ceDisplayEntry=ceDisplayEntry, ceDisplayTable=ceDisplayTable, ceDisplayName=ceDisplayName, ceDisplayBeaconEnabled=ceDisplayBeaconEnabled, CDisplayColor=CDisplayColor, ceDisplayGroup=ceDisplayGroup, ceDisplayMIBGroups=ceDisplayMIBGroups, ciscoEntityDisplayMIBObjects=ciscoEntityDisplayMIBObjects, PYSNMP_MODULE_ID=ciscoEntityDisplayMIB, ceDisplayBeaconEntry=ceDisplayBeaconEntry, ceDisplayColor=ceDisplayColor, ceDisplayMIBConformance=ceDisplayMIBConformance, ceDisplayLEDGroup=ceDisplayLEDGroup, ceDisplayType=ceDisplayType, ceDisplayMIBCompliance=ceDisplayMIBCompliance)
