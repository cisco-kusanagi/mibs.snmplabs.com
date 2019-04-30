#
# PySNMP MIB module ENTERASYS-DIAGNOSTIC-MESSAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-DIAGNOSTIC-MESSAGE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, iso, Counter64, IpAddress, Unsigned32, NotificationType, Integer32, Gauge32, MibIdentifier, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter64", "IpAddress", "Unsigned32", "NotificationType", "Integer32", "Gauge32", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
etsysDiagnosticMessageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13))
etsysDiagnosticMessageMIB.setRevisions(('2003-01-10 21:17', '2002-06-07 14:28', '2001-12-03 19:51', '2001-08-08 00:00',))
if mibBuilder.loadTexts: etsysDiagnosticMessageMIB.setLastUpdated('200304252048Z')
if mibBuilder.loadTexts: etsysDiagnosticMessageMIB.setOrganization('Enterasys Networks')
class LongAdminString(TextualConvention, OctetString):
    reference = 'RFC2571 (An Architecture for Describing SNMP Management Frameworks)'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

etsysDiagnosticMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1))
etsysDiagnosticMessageDetails = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2))
etsysDiagnosticMessageCount = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageCount.setStatus('current')
etsysDiagnosticMessageChanges = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageChanges.setStatus('current')
etsysDiagnosticMessageTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3), )
if mibBuilder.loadTexts: etsysDiagnosticMessageTable.setStatus('current')
etsysDiagnosticMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1), ).setIndexNames((0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageIndex"))
if mibBuilder.loadTexts: etsysDiagnosticMessageEntry.setStatus('current')
etsysDiagnosticMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: etsysDiagnosticMessageIndex.setStatus('current')
etsysDiagnosticMessageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageTime.setStatus('current')
etsysDiagnosticMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageType.setStatus('current')
etsysDiagnosticMessageSummary = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageSummary.setStatus('current')
etsysDiagnosticMessageFWRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageFWRevision.setStatus('current')
etsysDiagnosticMessageStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 1, 3, 1, 6), Bits().clone(namedValues=NamedValues(("etsysDiagnosticMessageBadChecksum", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageStatus.setStatus('current')
etsysDiagnosticMessageDetailsTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1), )
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsTable.setStatus('current')
etsysDiagnosticMessageDetailsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1), ).setIndexNames((0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageIndex"), (0, "ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsIndex"))
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsEntry.setStatus('current')
etsysDiagnosticMessageDetailsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsIndex.setStatus('current')
etsysDiagnosticMessageDetailsText = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 2), LongAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsText.setStatus('current')
etsysDiagnosticMessageDetailsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 2, 1, 1, 3), Bits().clone(namedValues=NamedValues(("etsysDiagnosticMessageLastSegment", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysDiagnosticMessageDetailsStatus.setStatus('current')
etsysDiagnosticMessageConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3))
etsysDiagnosticMessageGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 1))
etsysDiagnosticMessageCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 2))
etsysDiagnosticMessageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 1, 1)).setObjects(("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageCount"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageChanges"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageTime"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageType"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageSummary"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageFWRevision"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageStatus"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsText"), ("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageDetailsStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDiagnosticMessageGroup = etsysDiagnosticMessageGroup.setStatus('current')
etsysDiagnosticMessageCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 13, 3, 2, 1)).setObjects(("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", "etsysDiagnosticMessageGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysDiagnosticMessageCompliance = etsysDiagnosticMessageCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-DIAGNOSTIC-MESSAGE-MIB", etsysDiagnosticMessageConformance=etsysDiagnosticMessageConformance, LongAdminString=LongAdminString, etsysDiagnosticMessageChanges=etsysDiagnosticMessageChanges, etsysDiagnosticMessageStatus=etsysDiagnosticMessageStatus, etsysDiagnosticMessageCompliances=etsysDiagnosticMessageCompliances, etsysDiagnosticMessageMIB=etsysDiagnosticMessageMIB, etsysDiagnosticMessageDetailsIndex=etsysDiagnosticMessageDetailsIndex, etsysDiagnosticMessageDetailsEntry=etsysDiagnosticMessageDetailsEntry, etsysDiagnosticMessageTable=etsysDiagnosticMessageTable, etsysDiagnosticMessageDetails=etsysDiagnosticMessageDetails, etsysDiagnosticMessageEntry=etsysDiagnosticMessageEntry, etsysDiagnosticMessageGroups=etsysDiagnosticMessageGroups, etsysDiagnosticMessageSummary=etsysDiagnosticMessageSummary, etsysDiagnosticMessageType=etsysDiagnosticMessageType, etsysDiagnosticMessageDetailsStatus=etsysDiagnosticMessageDetailsStatus, etsysDiagnosticMessageDetailsText=etsysDiagnosticMessageDetailsText, etsysDiagnosticMessageTime=etsysDiagnosticMessageTime, etsysDiagnosticMessageDetailsTable=etsysDiagnosticMessageDetailsTable, etsysDiagnosticMessageFWRevision=etsysDiagnosticMessageFWRevision, PYSNMP_MODULE_ID=etsysDiagnosticMessageMIB, etsysDiagnosticMessageGroup=etsysDiagnosticMessageGroup, etsysDiagnosticMessage=etsysDiagnosticMessage, etsysDiagnosticMessageIndex=etsysDiagnosticMessageIndex, etsysDiagnosticMessageCount=etsysDiagnosticMessageCount, etsysDiagnosticMessageCompliance=etsysDiagnosticMessageCompliance)
