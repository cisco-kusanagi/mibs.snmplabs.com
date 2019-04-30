#
# PySNMP MIB module CISCO-VOICE-CARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-CARD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:02:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, Counter32, NotificationType, Gauge32, iso, TimeTicks, IpAddress, Unsigned32, ModuleIdentity, Integer32, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Counter32", "NotificationType", "Gauge32", "iso", "TimeTicks", "IpAddress", "Unsigned32", "ModuleIdentity", "Integer32", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVoiceCard = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 300576))
ciscoVoiceCard.setRevisions(('2002-02-15 00:00',))
if mibBuilder.loadTexts: ciscoVoiceCard.setLastUpdated('200202150000Z')
if mibBuilder.loadTexts: ciscoVoiceCard.setOrganization('Cisco Systems, Inc')
ciscoVoiceCardNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 0))
ciscoVoiceCardObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1))
cVoiceCardTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1), )
if mibBuilder.loadTexts: cVoiceCardTable.setStatus('current')
cVoiceCardEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1), ).setIndexNames((0, "CISCO-VOICE-CARD-MIB", "cVoiceCardIndex"))
if mibBuilder.loadTexts: cVoiceCardEntry.setStatus('current')
cVoiceCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: cVoiceCardIndex.setStatus('current')
cVoiceCardSlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cVoiceCardSlotNumber.setStatus('current')
cVoiceCardCodecComplexity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4))).clone(namedValues=NamedValues(("hc", 2), ("mc", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoiceCardCodecComplexity.setStatus('current')
cVoiceCardAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 300576, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cVoiceCardAdminStatus.setStatus('current')
ciscoVoiceCardConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2))
ciscoVoiceCardMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 1))
ciscoVoiceCardMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 2))
ciscoVoiceCardMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 1, 1)).setObjects(("CISCO-VOICE-CARD-MIB", "ciscoVoiceCardGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceCardMIBCompliance = ciscoVoiceCardMIBCompliance.setStatus('current')
ciscoVoiceCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 300576, 2, 2, 1)).setObjects(("CISCO-VOICE-CARD-MIB", "cVoiceCardSlotNumber"), ("CISCO-VOICE-CARD-MIB", "cVoiceCardCodecComplexity"), ("CISCO-VOICE-CARD-MIB", "cVoiceCardAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceCardGroup = ciscoVoiceCardGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-CARD-MIB", ciscoVoiceCardConformance=ciscoVoiceCardConformance, ciscoVoiceCardMIBCompliances=ciscoVoiceCardMIBCompliances, ciscoVoiceCardMIBCompliance=ciscoVoiceCardMIBCompliance, cVoiceCardIndex=cVoiceCardIndex, cVoiceCardTable=cVoiceCardTable, ciscoVoiceCardMIBGroups=ciscoVoiceCardMIBGroups, cVoiceCardEntry=cVoiceCardEntry, ciscoVoiceCardObjects=ciscoVoiceCardObjects, cVoiceCardSlotNumber=cVoiceCardSlotNumber, PYSNMP_MODULE_ID=ciscoVoiceCard, ciscoVoiceCard=ciscoVoiceCard, cVoiceCardCodecComplexity=cVoiceCardCodecComplexity, cVoiceCardAdminStatus=cVoiceCardAdminStatus, ciscoVoiceCardGroup=ciscoVoiceCardGroup, ciscoVoiceCardNotifications=ciscoVoiceCardNotifications)
