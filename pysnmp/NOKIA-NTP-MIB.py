#
# PySNMP MIB module NOKIA-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOKIA-NTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ntcNtpMibs, ntcNtpReqs, ntcCommonModules = mibBuilder.importSymbols("NOKIA-COMMON-MIB-OID-REGISTRATION-MIB", "ntcNtpMibs", "ntcNtpReqs", "ntcCommonModules")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, Bits, Integer32, iso, ObjectIdentity, IpAddress, TimeTicks, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "Integer32", "iso", "ObjectIdentity", "IpAddress", "TimeTicks", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Unsigned32", "NotificationType")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
nokiaNtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 94, 1, 16, 5, 2))
nokiaNtpMIB.setRevisions(('1998-10-07 00:00',))
if mibBuilder.loadTexts: nokiaNtpMIB.setLastUpdated('9908050000Z')
if mibBuilder.loadTexts: nokiaNtpMIB.setOrganization('Nokia')
nokiaNtpObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1))
ntcNtpConf = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1))
ntcNtpRtcConf = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 2))
ntcNtpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 1))
ntcNtpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 2))
class EnabledDisabled(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TimeServerStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ok", 1), ("notReachable", 2), ("clockNotInSynch", 3), ("diffTooBig", 4), ("otherError", 5))

ntcNtpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 1), EnabledDisabled()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcNtpEnabled.setStatus('current')
ntcNtpServerTableNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcNtpServerTableNextIndex.setStatus('current')
ntcNtpServerTable = MibTable((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3), )
if mibBuilder.loadTexts: ntcNtpServerTable.setStatus('current')
ntcNtpServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1), ).setIndexNames((0, "NOKIA-NTP-MIB", "ntcNtpServerIndex"))
if mibBuilder.loadTexts: ntcNtpServerEntry.setStatus('current')
ntcNtpServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ntcNtpServerIndex.setStatus('current')
ntcNtpServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ntcNtpServerAddress.setStatus('current')
ntcNtpServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ntcNtpServerPort.setStatus('current')
ntcNtpServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 4), TimeServerStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ntcNtpServerStatus.setStatus('current')
ntcNtpServerPreferred = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 5), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ntcNtpServerPreferred.setStatus('current')
ntcNtpServerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ntcNtpServerRowStatus.setStatus('current')
ntcNtpRtcCurrentTime = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(11, 11)).setFixedLength(11)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcNtpRtcCurrentTime.setStatus('current')
ntcNtpRtcTimeZone = MibScalar((1, 3, 6, 1, 4, 1, 94, 1, 16, 7, 2, 1, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ntcNtpRtcTimeZone.setStatus('current')
nokiaNtpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 2, 1)).setObjects(("NOKIA-NTP-MIB", "ntcNtpMinimumRTCGroup"), ("NOKIA-NTP-MIB", "ntcNtpMandatoryNTPGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nokiaNtpCompliance = nokiaNtpCompliance.setStatus('current')
ntcNtpMinimumRTCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 1, 1)).setObjects(("NOKIA-NTP-MIB", "ntcNtpRtcCurrentTime"), ("NOKIA-NTP-MIB", "ntcNtpRtcTimeZone"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcNtpMinimumRTCGroup = ntcNtpMinimumRTCGroup.setStatus('current')
ntcNtpMandatoryNTPGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 94, 1, 16, 8, 2, 1, 2)).setObjects(("NOKIA-NTP-MIB", "ntcNtpEnabled"), ("NOKIA-NTP-MIB", "ntcNtpServerTableNextIndex"), ("NOKIA-NTP-MIB", "ntcNtpServerAddress"), ("NOKIA-NTP-MIB", "ntcNtpServerPort"), ("NOKIA-NTP-MIB", "ntcNtpServerStatus"), ("NOKIA-NTP-MIB", "ntcNtpServerPreferred"), ("NOKIA-NTP-MIB", "ntcNtpServerRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ntcNtpMandatoryNTPGroup = ntcNtpMandatoryNTPGroup.setStatus('current')
mibBuilder.exportSymbols("NOKIA-NTP-MIB", ntcNtpMandatoryNTPGroup=ntcNtpMandatoryNTPGroup, ntcNtpMinimumRTCGroup=ntcNtpMinimumRTCGroup, ntcNtpServerStatus=ntcNtpServerStatus, ntcNtpServerRowStatus=ntcNtpServerRowStatus, nokiaNtpMIB=nokiaNtpMIB, ntcNtpServerEntry=ntcNtpServerEntry, ntcNtpRtcTimeZone=ntcNtpRtcTimeZone, ntcNtpRtcConf=ntcNtpRtcConf, ntcNtpServerTableNextIndex=ntcNtpServerTableNextIndex, ntcNtpServerTable=ntcNtpServerTable, nokiaNtpCompliance=nokiaNtpCompliance, ntcNtpEnabled=ntcNtpEnabled, ntcNtpRtcCurrentTime=ntcNtpRtcCurrentTime, ntcNtpCompliances=ntcNtpCompliances, EnabledDisabled=EnabledDisabled, ntcNtpServerAddress=ntcNtpServerAddress, nokiaNtpObjs=nokiaNtpObjs, PYSNMP_MODULE_ID=nokiaNtpMIB, TimeServerStatus=TimeServerStatus, ntcNtpServerPreferred=ntcNtpServerPreferred, ntcNtpServerPort=ntcNtpServerPort, ntcNtpServerIndex=ntcNtpServerIndex, ntcNtpGroups=ntcNtpGroups, ntcNtpConf=ntcNtpConf)
