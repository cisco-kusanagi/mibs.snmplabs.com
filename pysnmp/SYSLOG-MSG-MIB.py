#
# PySNMP MIB module SYSLOG-MSG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SYSLOG-MSG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:06:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, TimeTicks, Counter32, Integer32, ObjectIdentity, ModuleIdentity, Bits, IpAddress, Unsigned32, NotificationType, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "TimeTicks", "Counter32", "Integer32", "ObjectIdentity", "ModuleIdentity", "Bits", "IpAddress", "Unsigned32", "NotificationType", "iso", "Counter64")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
SyslogSeverity, SyslogFacility = mibBuilder.importSymbols("SYSLOG-TC-MIB", "SyslogSeverity", "SyslogFacility")
syslogMsgMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 192))
syslogMsgMib.setRevisions(('2009-08-13 08:00',))
if mibBuilder.loadTexts: syslogMsgMib.setLastUpdated('200908130800Z')
if mibBuilder.loadTexts: syslogMsgMib.setOrganization('IETF OPSAWG Working Group')
class SyslogTimeStamp(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.3d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(10, 10), ValueSizeConstraint(13, 13), )
class SyslogParamValueString(TextualConvention, OctetString):
    reference = 'RFC 3629: UTF-8, a transformation format of ISO 10646'
    status = 'current'
    displayHint = '65535t'

syslogMsgNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 192, 0))
syslogMsgObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 192, 1))
syslogMsgConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 192, 2))
syslogMsgControl = MibIdentifier((1, 3, 6, 1, 2, 1, 192, 1, 1))
syslogMsgTableMaxSize = MibScalar((1, 3, 6, 1, 2, 1, 192, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogMsgTableMaxSize.setStatus('current')
syslogMsgEnableNotifications = MibScalar((1, 3, 6, 1, 2, 1, 192, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syslogMsgEnableNotifications.setStatus('current')
syslogMsgTable = MibTable((1, 3, 6, 1, 2, 1, 192, 1, 2), )
if mibBuilder.loadTexts: syslogMsgTable.setStatus('current')
syslogMsgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 192, 1, 2, 1), ).setIndexNames((0, "SYSLOG-MSG-MIB", "syslogMsgIndex"))
if mibBuilder.loadTexts: syslogMsgEntry.setStatus('current')
syslogMsgIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: syslogMsgIndex.setStatus('current')
syslogMsgFacility = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 2), SyslogFacility()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgFacility.setStatus('current')
syslogMsgSeverity = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 3), SyslogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgSeverity.setStatus('current')
syslogMsgVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgVersion.setStatus('current')
syslogMsgTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 5), SyslogTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgTimeStamp.setStatus('current')
syslogMsgHostName = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgHostName.setStatus('current')
syslogMsgAppName = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 48))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgAppName.setStatus('current')
syslogMsgProcID = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgProcID.setStatus('current')
syslogMsgMsgID = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgMsgID.setStatus('current')
syslogMsgSDParams = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgSDParams.setStatus('current')
syslogMsgMsg = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 2, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgMsg.setStatus('current')
syslogMsgSDTable = MibTable((1, 3, 6, 1, 2, 1, 192, 1, 3), )
if mibBuilder.loadTexts: syslogMsgSDTable.setStatus('current')
syslogMsgSDEntry = MibTableRow((1, 3, 6, 1, 2, 1, 192, 1, 3, 1), ).setIndexNames((0, "SYSLOG-MSG-MIB", "syslogMsgIndex"), (0, "SYSLOG-MSG-MIB", "syslogMsgSDParamIndex"), (0, "SYSLOG-MSG-MIB", "syslogMsgSDID"), (0, "SYSLOG-MSG-MIB", "syslogMsgSDParamName"))
if mibBuilder.loadTexts: syslogMsgSDEntry.setStatus('current')
syslogMsgSDParamIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: syslogMsgSDParamIndex.setStatus('current')
syslogMsgSDID = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: syslogMsgSDID.setStatus('current')
syslogMsgSDParamName = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: syslogMsgSDParamName.setStatus('current')
syslogMsgSDParamValue = MibTableColumn((1, 3, 6, 1, 2, 1, 192, 1, 3, 1, 4), SyslogParamValueString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: syslogMsgSDParamValue.setStatus('current')
syslogMsgNotification = NotificationType((1, 3, 6, 1, 2, 1, 192, 0, 1)).setObjects(("SYSLOG-MSG-MIB", "syslogMsgFacility"), ("SYSLOG-MSG-MIB", "syslogMsgSeverity"), ("SYSLOG-MSG-MIB", "syslogMsgVersion"), ("SYSLOG-MSG-MIB", "syslogMsgTimeStamp"), ("SYSLOG-MSG-MIB", "syslogMsgHostName"), ("SYSLOG-MSG-MIB", "syslogMsgAppName"), ("SYSLOG-MSG-MIB", "syslogMsgProcID"), ("SYSLOG-MSG-MIB", "syslogMsgMsgID"), ("SYSLOG-MSG-MIB", "syslogMsgSDParams"), ("SYSLOG-MSG-MIB", "syslogMsgMsg"))
if mibBuilder.loadTexts: syslogMsgNotification.setStatus('current')
syslogMsgGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 192, 2, 1))
syslogMsgCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 192, 2, 2))
syslogMsgFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 192, 2, 2, 1)).setObjects(("SYSLOG-MSG-MIB", "syslogMsgGroup"), ("SYSLOG-MSG-MIB", "syslogMsgSDGroup"), ("SYSLOG-MSG-MIB", "syslogMsgControlGroup"), ("SYSLOG-MSG-MIB", "syslogMsgNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogMsgFullCompliance = syslogMsgFullCompliance.setStatus('current')
syslogMsgReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 192, 2, 2, 2)).setObjects(("SYSLOG-MSG-MIB", "syslogMsgGroup"), ("SYSLOG-MSG-MIB", "syslogMsgSDGroup"), ("SYSLOG-MSG-MIB", "syslogMsgControlGroup"), ("SYSLOG-MSG-MIB", "syslogMsgNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogMsgReadOnlyCompliance = syslogMsgReadOnlyCompliance.setStatus('current')
syslogMsgNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 192, 2, 2, 3)).setObjects(("SYSLOG-MSG-MIB", "syslogMsgGroup"), ("SYSLOG-MSG-MIB", "syslogMsgSDGroup"), ("SYSLOG-MSG-MIB", "syslogMsgNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogMsgNotificationCompliance = syslogMsgNotificationCompliance.setStatus('current')
syslogMsgNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 192, 2, 1, 1)).setObjects(("SYSLOG-MSG-MIB", "syslogMsgNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogMsgNotificationGroup = syslogMsgNotificationGroup.setStatus('current')
syslogMsgGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 192, 2, 1, 2)).setObjects(("SYSLOG-MSG-MIB", "syslogMsgFacility"), ("SYSLOG-MSG-MIB", "syslogMsgSeverity"), ("SYSLOG-MSG-MIB", "syslogMsgVersion"), ("SYSLOG-MSG-MIB", "syslogMsgTimeStamp"), ("SYSLOG-MSG-MIB", "syslogMsgHostName"), ("SYSLOG-MSG-MIB", "syslogMsgAppName"), ("SYSLOG-MSG-MIB", "syslogMsgProcID"), ("SYSLOG-MSG-MIB", "syslogMsgMsgID"), ("SYSLOG-MSG-MIB", "syslogMsgSDParams"), ("SYSLOG-MSG-MIB", "syslogMsgMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogMsgGroup = syslogMsgGroup.setStatus('current')
syslogMsgSDGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 192, 2, 1, 3)).setObjects(("SYSLOG-MSG-MIB", "syslogMsgSDParamValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogMsgSDGroup = syslogMsgSDGroup.setStatus('current')
syslogMsgControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 192, 2, 1, 4)).setObjects(("SYSLOG-MSG-MIB", "syslogMsgTableMaxSize"), ("SYSLOG-MSG-MIB", "syslogMsgEnableNotifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    syslogMsgControlGroup = syslogMsgControlGroup.setStatus('current')
mibBuilder.exportSymbols("SYSLOG-MSG-MIB", syslogMsgGroup=syslogMsgGroup, SyslogTimeStamp=SyslogTimeStamp, syslogMsgVersion=syslogMsgVersion, syslogMsgEntry=syslogMsgEntry, syslogMsgProcID=syslogMsgProcID, syslogMsgMsg=syslogMsgMsg, SyslogParamValueString=SyslogParamValueString, syslogMsgReadOnlyCompliance=syslogMsgReadOnlyCompliance, PYSNMP_MODULE_ID=syslogMsgMib, syslogMsgSDParamName=syslogMsgSDParamName, syslogMsgNotification=syslogMsgNotification, syslogMsgSDTable=syslogMsgSDTable, syslogMsgNotificationCompliance=syslogMsgNotificationCompliance, syslogMsgSDID=syslogMsgSDID, syslogMsgConformance=syslogMsgConformance, syslogMsgSDEntry=syslogMsgSDEntry, syslogMsgControlGroup=syslogMsgControlGroup, syslogMsgSDGroup=syslogMsgSDGroup, syslogMsgGroups=syslogMsgGroups, syslogMsgTableMaxSize=syslogMsgTableMaxSize, syslogMsgSeverity=syslogMsgSeverity, syslogMsgNotifications=syslogMsgNotifications, syslogMsgMsgID=syslogMsgMsgID, syslogMsgAppName=syslogMsgAppName, syslogMsgHostName=syslogMsgHostName, syslogMsgNotificationGroup=syslogMsgNotificationGroup, syslogMsgEnableNotifications=syslogMsgEnableNotifications, syslogMsgSDParams=syslogMsgSDParams, syslogMsgSDParamIndex=syslogMsgSDParamIndex, syslogMsgObjects=syslogMsgObjects, syslogMsgSDParamValue=syslogMsgSDParamValue, syslogMsgIndex=syslogMsgIndex, syslogMsgTimeStamp=syslogMsgTimeStamp, syslogMsgMib=syslogMsgMib, syslogMsgTable=syslogMsgTable, syslogMsgControl=syslogMsgControl, syslogMsgFacility=syslogMsgFacility, syslogMsgFullCompliance=syslogMsgFullCompliance, syslogMsgCompliances=syslogMsgCompliances)
