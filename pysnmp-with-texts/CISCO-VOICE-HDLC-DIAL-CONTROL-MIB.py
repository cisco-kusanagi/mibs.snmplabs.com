#
# PySNMP MIB module CISCO-VOICE-HDLC-DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOICE-HDLC-DIAL-CONTROL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
cCallHistoryIndex, = mibBuilder.importSymbols("CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
CvcGUid, = mibBuilder.importSymbols("CISCO-VOICE-COMMON-DIAL-CONTROL-MIB", "CvcGUid")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Integer32, iso, Bits, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, IpAddress, MibIdentifier, ModuleIdentity, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "iso", "Bits", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "IpAddress", "MibIdentifier", "ModuleIdentity", "Gauge32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVoiceHdlcDialControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 37))
if mibBuilder.loadTexts: ciscoVoiceHdlcDialControlMIB.setLastUpdated('9804140000Z')
if mibBuilder.loadTexts: ciscoVoiceHdlcDialControlMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoiceHdlcDialControlMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoVoiceHdlcDialControlMIB.setDescription('This MIB module enhances the IETF Dial Control MIB (RFC2128) by providing HDLC management information over a data network. ')
cvhdlcdcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 1))
cvHdlcCallHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1))
cvHdlcCallHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1), )
if mibBuilder.loadTexts: cvHdlcCallHistoryTable.setStatus('current')
if mibBuilder.loadTexts: cvHdlcCallHistoryTable.setDescription('This table is the HDLC extension to the call history table of IETF Dial Control MIB. It contains HDLC call leg information about specific voice over HDLC call. ')
cvHdlcCallHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"))
if mibBuilder.loadTexts: cvHdlcCallHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: cvHdlcCallHistoryEntry.setDescription('The information regarding a single HDLC call leg. An entry of this table is created when its associated call history entry in the IETF Dial Control MIB is created and the call history entry contains information for the call establishment to the peer on the data network backbone via a voice over HDLC peer. The entry is deleted when its associated call history entry in the IETF Dial Control MIB is deleted. ')
cvHdlcCallHistoryConnectionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 1), CvcGUid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistoryConnectionId.setStatus('current')
if mibBuilder.loadTexts: cvHdlcCallHistoryConnectionId.setDescription('The global call identifier for the tandem call.')
cvHdlcCallHistoryLowerIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 24))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistoryLowerIfName.setStatus('current')
if mibBuilder.loadTexts: cvHdlcCallHistoryLowerIfName.setDescription('The textual name of lower layer interface associated with this HDLC call.')
cvHdlcCallHistorySessionTarget = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 37, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvHdlcCallHistorySessionTarget.setStatus('current')
if mibBuilder.loadTexts: cvHdlcCallHistorySessionTarget.setDescription('The object specifies the session target of the peer that is used for the voice over HDLC call. A null string indicates that the value is unavailable.')
cvhdlcdcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3))
cvhdlcdcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 1))
cvhdlcdcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 2))
cvhdlcdcMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 1, 1)).setObjects(("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvhdlcdcMIBCompliance = cvhdlcdcMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: cvhdlcdcMIBCompliance.setDescription('The compliance statement for entities which implement the CISCO VOICE HDLC DIAL CONTROL MIB')
cvHdlcCallHistoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 37, 3, 2, 1)).setObjects(("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryConnectionId"), ("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistoryLowerIfName"), ("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", "cvHdlcCallHistorySessionTarget"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvHdlcCallHistoryGroup = cvHdlcCallHistoryGroup.setStatus('current')
if mibBuilder.loadTexts: cvHdlcCallHistoryGroup.setDescription('A collection of objects providing the HDLC Call capability.')
mibBuilder.exportSymbols("CISCO-VOICE-HDLC-DIAL-CONTROL-MIB", cvHdlcCallHistoryConnectionId=cvHdlcCallHistoryConnectionId, cvHdlcCallHistoryGroup=cvHdlcCallHistoryGroup, cvhdlcdcMIBObjects=cvhdlcdcMIBObjects, cvhdlcdcMIBGroups=cvhdlcdcMIBGroups, cvHdlcCallHistory=cvHdlcCallHistory, cvHdlcCallHistoryLowerIfName=cvHdlcCallHistoryLowerIfName, cvHdlcCallHistorySessionTarget=cvHdlcCallHistorySessionTarget, cvhdlcdcMIBCompliance=cvhdlcdcMIBCompliance, ciscoVoiceHdlcDialControlMIB=ciscoVoiceHdlcDialControlMIB, cvHdlcCallHistoryEntry=cvHdlcCallHistoryEntry, cvHdlcCallHistoryTable=cvHdlcCallHistoryTable, PYSNMP_MODULE_ID=ciscoVoiceHdlcDialControlMIB, cvhdlcdcMIBCompliances=cvhdlcdcMIBCompliances, cvhdlcdcMIBConformance=cvhdlcdcMIBConformance)
